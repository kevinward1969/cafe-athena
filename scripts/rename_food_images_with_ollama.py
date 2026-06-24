#!/usr/bin/env python3
"""AI-assisted image renamer for food/cooking photos.

- Scans a directory recursively for image files only.
- Uses Ollama vision to decide whether an image is food/cooking related.
- Proposes descriptive, slug-safe file names for related images.
- Dry run by default; writes only with --apply.

Example:
  python3 scripts/rename_food_images_with_ollama.py \
    --dir "Marketing/Resources/User Images" \
    --model gemma3:4b
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from functools import lru_cache
from dataclasses import dataclass
from pathlib import Path

from transformers import pipeline

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".tif", ".tiff", ".bmp"}

GENERIC_LABELS = {
        "ingredients",
        "food",
        "meal",
        "dish",
        "cooking",
        "kitchen",
        "photo",
        "image",
}

KNOWN_TERM_NORMALIZATION = {
        "beef burgionone": "beef bourguignonne",
        "beef bourguinone": "beef bourguignonne",
        "beef bourguignon": "beef bourguignonne",
        "smoked scheinshax": "smoked schweinshaxe",
        "scheinshax": "schweinshaxe",
}

PROMPT_TEMPLATE = """You are classifying a single photo for file naming in a cooking archive.

Rules:
- Mark related=true only if the image is food or cooking related:
  plated meal, ingredients, prep/mise en place, cookware in active use, cooking process, finished dish.
- Mark related=false for anything else: people portraits, pets, scenery, documents, random objects, screenshots.
- If food is present, label the edible item first (not cutting board/plate/tableware unless no food is visible).
- Prefer specific dish names when recognizable; use concise terms.
- Use one of these stages: dish, sandwich, bread, prep, ingredients, process, cookware, unknown.
- confidence is 0.00-1.00.

Allowed culinary hints to prefer when they match the image:
{hints_block}

Return JSON only in this exact shape:
{{"related": true, "label": "seared salmon with herbs", "stage": "dish", "confidence": 0.88}}
"""


@dataclass
class Decision:
    related: bool
    label: str
    stage: str
    confidence: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rename food/cooking images with Ollama vision")
    parser.add_argument("--dir", required=True, help="Directory to scan recursively")
    parser.add_argument(
        "--backend",
        choices=["hf", "hf-zs", "ollama"],
        default="hf-zs",
        help="Inference backend: hf, hf-zs (default), or ollama",
    )
    parser.add_argument("--model", default="gemma3:4b", help="Ollama model (default: gemma3:4b)")
    parser.add_argument(
        "--hf-model",
        default="prithivMLmods/Food-101-93M",
        help="Hugging Face image-classification model for --backend hf",
    )
    parser.add_argument(
        "--hf-zs-model",
        default="google/siglip2-base-patch16-224",
        help="Hugging Face zero-shot image model for --backend hf-zs",
    )
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/generate", help="Ollama generate endpoint")
    parser.add_argument("--min-confidence", type=float, default=0.20, help="Minimum confidence to rename (default: 0.20)")
    parser.add_argument("--max-files", type=int, default=0, help="Process at most N images (0 = all)")
    parser.add_argument(
        "--hints",
        default="",
        help=(
            "Comma-separated dish/subject hints (preferred labels when matched), "
            "e.g. 'smoked schweinshaxe, baguette, beef bourguignonne, sandwich'"
        ),
    )
    parser.add_argument(
        "--labels",
        default="",
        help="Comma-separated candidate labels for zero-shot backend",
    )
    parser.add_argument(
        "--labels-file",
        default="",
        help="Path to newline-separated candidate labels for zero-shot backend",
    )
    parser.add_argument(
        "--labels-from-manual",
        action="store_true",
        help="Add recipe titles from The Manual/ as zero-shot labels",
    )
    parser.add_argument(
        "--max-manual-labels",
        type=int,
        default=250,
        help="Max number of labels loaded from The Manual titles (default: 250)",
    )
    parser.add_argument(
        "--overrides",
        default="",
        help=(
            "Semicolon-separated overrides by filename stem or full filename, "
            "e.g. 'IMG_0264=smoked schweinshaxe;IMG_0274=baguette'"
        ),
    )
    parser.add_argument("--apply", action="store_true", help="Apply renames (default: dry run)")
    parser.add_argument("--verbose", action="store_true", help="Print model responses when parsing fails")
    return parser.parse_args()


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "food-photo"


def list_images(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTS:
            files.append(path)
    return sorted(files)


def parse_hints(raw_hints: str) -> list[str]:
    if not raw_hints.strip():
        return []
    hints = []
    for item in raw_hints.split(","):
        hint = item.strip()
        if hint:
            hints.append(hint)
    return hints


def parse_overrides(raw: str) -> dict[str, str]:
    out: dict[str, str] = {}
    if not raw.strip():
        return out
    for chunk in raw.split(";"):
        chunk = chunk.strip()
        if not chunk or "=" not in chunk:
            continue
        key, val = chunk.split("=", 1)
        key = key.strip().lower()
        val = val.strip()
        if key and val:
            out[key] = val
    return out


def parse_labels(raw_labels: str) -> list[str]:
    if not raw_labels.strip():
        return []
    labels = []
    for item in raw_labels.split(","):
        label = item.strip()
        if label:
            labels.append(label)
    return labels


def load_labels_file(path: str) -> list[str]:
    if not path.strip():
        return []
    p = Path(path).expanduser().resolve()
    if not p.exists() or not p.is_file():
        return []
    labels: list[str] = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            label = line.strip()
            if label and not label.startswith("#"):
                labels.append(label)
    return labels


def extract_manual_titles(repo_root: Path, limit: int) -> list[str]:
    manual_dir = repo_root / "The Manual"
    if not manual_dir.exists():
        return []

    titles: list[str] = []
    for md in sorted(manual_dir.rglob("*.md")):
        name = md.name
        if not re.match(r"^\[?\d{2}-\d{2}", name):
            continue
        t = re.sub(r"^\[?\d{2}-\d{2}[a-z]*(?:_\d+)?\]?\s*", "", name)
        t = t.replace(".md", "")
        t = re.sub(r"^(Café Athena\s*[-–—]\s*|Technique Folio\s*[-–—]\s*)", "", t)
        t = t.strip()
        if t:
            titles.append(t)
        if len(titles) >= limit:
            break
    return titles


def build_candidate_labels(args: argparse.Namespace, root: Path, hints: list[str]) -> list[str]:
    labels: list[str] = []
    labels.extend(parse_labels(args.labels))
    labels.extend(load_labels_file(args.labels_file))
    labels.extend(hints)
    if args.labels_from_manual:
        labels.extend(extract_manual_titles(root, args.max_manual_labels))

    # Add robust generic fallback classes.
    labels.extend([
        "sandwich",
        "baguette",
        "bread",
        "burger",
        "steak",
        "beef stew",
        "pork hock",
        "smoked pork",
        "roasted potatoes",
        "plated dish",
        "food prep",
        "ingredients",
    ])

    dedup: list[str] = []
    seen: set[str] = set()
    for label in labels:
        key = label.strip().lower()
        if not key:
            continue
        if key in seen:
            continue
        seen.add(key)
        dedup.append(label.strip())
    return dedup


def build_prompt(hints: list[str]) -> str:
    if hints:
        hints_block = "\n".join(f"- {h}" for h in hints)
    else:
        hints_block = "- (none provided)"
    return PROMPT_TEMPLATE.format(hints_block=hints_block)


@lru_cache(maxsize=4)
def get_hf_classifier(model_name: str):
    return pipeline("image-classification", model=model_name)


@lru_cache(maxsize=4)
def get_hf_zs_classifier(model_name: str):
    return pipeline("zero-shot-image-classification", model=model_name)


def map_stage_from_label(label: str) -> str:
    l = label.lower()
    if "sandwich" in l or "burger" in l:
        return "sandwich"
    if any(x in l for x in ("bread", "bagel", "pretzel", "croissant", "baguette", "toast")):
        return "bread"
    if any(x in l for x in ("salad", "soup", "stew", "pizza", "sushi", "curry", "paella", "dumpling", "pasta")):
        return "dish"
    if any(x in l for x in ("fries", "onion_ring", "onion ring", "chips")):
        return "dish"
    return "dish"


def pick_label_with_hints(predictions: list[dict], hints: list[str]) -> tuple[str, float]:
    if not predictions:
        return "food-photo", 0.0

    top_label = str(predictions[0].get("label", "food-photo")).replace("_", " ").strip()
    top_score = float(predictions[0].get("score", 0.0))

    if not hints:
        return top_label, top_score

    normalized_hints = [h.lower().strip() for h in hints]
    for pred in predictions:
        p = str(pred.get("label", "")).replace("_", " ").lower()
        s = float(pred.get("score", 0.0))
        for h in normalized_hints:
            # Accept explicit hint only when there is visible lexical overlap
            # and the class confidence is reasonably strong.
            overlap = set(h.split()) & set(p.split())
            if overlap and s >= 0.12:
                return h, s

    return top_label, top_score


def classify_with_hf(model_name: str, image_path: Path, hints: list[str]) -> Decision:
    classifier = get_hf_classifier(model_name)
    preds = classifier(str(image_path), top_k=5)
    label, score = pick_label_with_hints(preds, hints)
    label = KNOWN_TERM_NORMALIZATION.get(label.lower().strip(), label)
    stage = map_stage_from_label(label)
    return Decision(related=True, label=label, stage=stage, confidence=max(0.0, min(1.0, float(score))))


def classify_with_hf_zero_shot(model_name: str, image_path: Path, candidate_labels: list[str]) -> Decision:
    classifier = get_hf_zs_classifier(model_name)
    preds = classifier(str(image_path), candidate_labels=candidate_labels)
    if not preds:
        return Decision(related=False, label="", stage="unknown", confidence=0.0)

    top = preds[0]
    label = str(top.get("label", "food-photo")).strip()
    score = float(top.get("score", 0.0))
    label = KNOWN_TERM_NORMALIZATION.get(label.lower().strip(), label)
    stage = map_stage_from_label(label)
    return Decision(related=True, label=label, stage=stage, confidence=max(0.0, min(1.0, score)))


def call_ollama(url: str, model: str, image_path: Path, prompt: str) -> str:
    image_b64 = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "images": [image_b64],
        "options": {"temperature": 0.1},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        raw = resp.read().decode("utf-8")
    return json.loads(raw).get("response", "").strip()


def parse_json_response(text: str, verbose: bool = False) -> Decision | None:
    if not text:
        return None

    # Handle fenced JSON or extra prose.
    cleaned = text.strip().strip("`")
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        if verbose:
            print(f"    ! Could not parse model JSON: {text[:220]}")
        return None

    related = bool(data.get("related", False))
    label = str(data.get("label", "")).strip()
    stage = str(data.get("stage", "unknown")).strip().lower() or "unknown"
    conf_raw = data.get("confidence", 0.0)

    try:
        confidence = float(conf_raw)
    except (TypeError, ValueError):
        confidence = 0.0

    if stage not in {"dish", "sandwich", "bread", "prep", "ingredients", "process", "cookware", "unknown"}:
        stage = "unknown"

    if not label:
        label = "food-photo"

    normalized = label.lower().strip()
    label = KNOWN_TERM_NORMALIZATION.get(normalized, label)

    return Decision(related=related, label=label, stage=stage, confidence=max(0.0, min(1.0, confidence)))


def build_target_name(decision: Decision, ext: str) -> str:
    label = decision.label.strip()
    if label.lower() in GENERIC_LABELS:
        label = f"{decision.stage}-food-photo" if decision.stage != "unknown" else "food-photo"
    base = slugify(label)
    if decision.stage != "unknown":
        base = f"{decision.stage}-{base}"
    return f"{base}{ext.lower()}"


def unique_target(path: Path, proposed_name: str, reserved: set[Path]) -> Path:
    candidate = path.with_name(proposed_name)
    if candidate == path:
        return candidate

    stem = candidate.stem
    suffix = candidate.suffix
    i = 2
    while candidate.exists() or candidate in reserved:
        candidate = candidate.with_name(f"{stem}-{i:02d}{suffix}")
        i += 1
    return candidate


def main() -> int:
    args = parse_args()
    root = Path(args.dir).expanduser().resolve()

    if not root.exists() or not root.is_dir():
        print(f"Directory not found: {root}")
        return 1

    images = list_images(root)
    hints = parse_hints(args.hints)
    overrides = parse_overrides(args.overrides)
    prompt = build_prompt(hints)
    candidate_labels = build_candidate_labels(args, root, hints)
    if args.max_files > 0:
        images = images[:args.max_files]

    if not images:
        print("No image files found (non-image files were ignored).")
        return 0

    print(f"Scanning {len(images)} image files in: {root}")
    print(f"Mode: {'APPLY' if args.apply else 'DRY RUN'}")
    print(f"Backend: {args.backend}")
    if hints:
        print(f"Hints: {', '.join(hints)}")
    if overrides:
        print(f"Overrides: {len(overrides)}")
    if args.backend == "hf-zs":
        print(f"Zero-shot labels: {len(candidate_labels)}")
    print()

    renamed = 0
    skipped_non_related = 0
    skipped_low_conf = 0
    failed = 0
    planned_targets: set[Path] = set()

    for idx, img in enumerate(images, start=1):
        rel = img.relative_to(root)
        print(f"[{idx}/{len(images)}] {rel}")

        try:
            stem_key = img.stem.lower()
            name_key = img.name.lower()
            override_label = overrides.get(stem_key) or overrides.get(name_key)

            if override_label:
                stage = map_stage_from_label(override_label)
                decision = Decision(related=True, label=override_label, stage=stage, confidence=1.0)
            elif args.backend == "hf":
                decision = classify_with_hf(args.hf_model, img, hints)
            elif args.backend == "hf-zs":
                decision = classify_with_hf_zero_shot(args.hf_zs_model, img, candidate_labels)
            else:
                raw = call_ollama(args.ollama_url, args.model, img, prompt)
                decision = parse_json_response(raw, verbose=args.verbose)
                if not decision:
                    print("  -> skip (unparseable model output)")
                    failed += 1
                    continue

            if not decision.related:
                print("  -> skip (not food/cooking related)")
                skipped_non_related += 1
                continue

            if decision.confidence < args.min_confidence:
                print(f"  -> skip (low confidence {decision.confidence:.2f})")
                skipped_low_conf += 1
                continue

            target_name = build_target_name(decision, img.suffix)
            target = unique_target(img, target_name, planned_targets)
            planned_targets.add(target)

            if target == img:
                print("  -> keep (name already matches)")
                continue

            print(f"  -> rename to: {target.name} (conf {decision.confidence:.2f})")
            if args.apply:
                img.rename(target)
            renamed += 1

        except urllib.error.URLError as exc:
            print(f"  -> error (ollama): {exc}")
            failed += 1
        except Exception as exc:
            print(f"  -> error: {exc}")
            failed += 1

    print("\nSummary")
    print(f"- images scanned: {len(images)}")
    print(f"- planned/applied renames: {renamed}")
    print(f"- skipped non-related: {skipped_non_related}")
    print(f"- skipped low confidence: {skipped_low_conf}")
    print(f"- failed: {failed}")

    if not args.apply:
        print("\nDry run only. Re-run with --apply to perform renames.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
