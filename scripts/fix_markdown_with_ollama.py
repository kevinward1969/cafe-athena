#!/usr/bin/env python3
"""Auto-fix Markdownlint issues with a local Ollama model.

This script:
1. Finds Markdown files in the repository.
2. Runs markdownlint (via npx markdownlint-cli) against each file.
3. Sends the file + lint issues to Ollama for a corrected version.
4. Applies the update only if lint errors decrease.

Usage examples:
  python3 scripts/fix_markdown_with_ollama.py
  python3 scripts/fix_markdown_with_ollama.py --glob "The Manual/**/*.md" --max-iterations 2
  python3 scripts/fix_markdown_with_ollama.py --dry-run
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import time
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


DEFAULT_EXCLUDES = [
    "**/.git/**",
    "**/node_modules/**",
    "**/dist/**",
    "**/.astro/**",
    "**/.venv/**",
]


@dataclass(frozen=True)
class LintIssue:
    line: int
    rule: str
    description: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fix markdownlint issues with Ollama")
    parser.add_argument("--root", default=".", help="Repository root (default: current directory)")
    parser.add_argument(
        "--glob",
        action="append",
        default=None,
        help="Glob to include Markdown files (repeatable). Default: **/*.md",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Glob to exclude paths (repeatable)",
    )
    parser.add_argument("--model", default="llama3.2", help="Ollama model name")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434/api/generate", help="Ollama generate endpoint")
    parser.add_argument(
        "--ollama-timeout",
        type=int,
        default=120,
        help="Timeout in seconds for each Ollama request (default: 120)",
    )
    parser.add_argument(
        "--ollama-retries",
        type=int,
        default=2,
        help="Retry count for transient Ollama failures per attempt (default: 2)",
    )
    parser.add_argument(
        "--retry-delay",
        type=float,
        default=1.5,
        help="Base delay in seconds before retrying Ollama (default: 1.5)",
    )
    parser.add_argument("--max-iterations", type=int, default=3, help="Max fix attempts per file")
    parser.add_argument(
        "--max-file-chars",
        type=int,
        default=24000,
        help="Skip files larger than this many chars (default: 24000)",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Process at most N files after filtering (0 = no limit)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write changes")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print extra details for debugging",
    )
    return parser.parse_args()


def get_ollama_base_url(generate_url: str) -> str:
    marker = "/api/"
    if marker in generate_url:
        return generate_url.split(marker, 1)[0]
    return generate_url.rsplit("/", 1)[0]


def fetch_ollama_models(generate_url: str) -> List[str]:
    tags_url = f"{get_ollama_base_url(generate_url)}/api/tags"
    request = urllib.request.Request(tags_url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to query Ollama models at {tags_url}: {exc}") from exc

    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON from Ollama tags endpoint: {body[:400]}") from exc

    models = payload.get("models") or []
    names = [str(model.get("name", "")).strip() for model in models if str(model.get("name", "")).strip()]
    if not names:
        raise RuntimeError("Ollama returned no installed models")
    return names


def resolve_ollama_model(requested_model: str, installed_models: List[str]) -> str:
    if requested_model in installed_models:
        return requested_model

    if ":" not in requested_model:
        latest_match = f"{requested_model}:latest"
        if latest_match in installed_models:
            return latest_match

    prefix = requested_model.split(":", 1)[0]
    prefix_matches = [model for model in installed_models if model == prefix or model.startswith(f"{prefix}:")]
    if f"{prefix}:latest" in prefix_matches:
        return f"{prefix}:latest"
    if len(prefix_matches) == 1:
        return prefix_matches[0]
    if prefix_matches:
        return sorted(prefix_matches)[0]

    raise RuntimeError(
        f"Requested model '{requested_model}' is not installed. Available models: {', '.join(installed_models)}"
    )


def run_markdownlint(root: Path, file_path: Path) -> List[LintIssue]:
    cmd = [
        "npx",
        "--yes",
        "markdownlint-cli@0.39.0",
        "--json",
        "--config",
        str(root / ".markdownlint.json"),
        str(file_path),
    ]
    proc = subprocess.run(
        cmd,
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )

    stdout = (proc.stdout or "").strip()
    stderr = (proc.stderr or "").strip()

    # markdownlint-cli may emit JSON to stdout or stderr depending on version/flags.
    json_text = stdout or stderr
    if not json_text:
        if proc.returncode == 0:
            return []
        raise RuntimeError(f"markdownlint failed for {file_path}: no output")

    try:
        payload = json.loads(json_text)
    except json.JSONDecodeError:
        # If there is non-JSON output and non-zero exit code, treat as tool failure.
        if proc.returncode != 0:
            raise RuntimeError(
                f"Could not parse markdownlint output for {file_path}\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}"
            )
        return []

    issues: List[LintIssue] = []
    # markdownlint-cli ≥0.37 returns a flat list; older versions return a
    # dict keyed by file path. Handle both shapes.
    if isinstance(payload, list):
        items: List[dict] = payload
    else:
        items = []
        for path_issues in payload.values():
            items.extend(path_issues)

    for item in items:
        rule_names = item.get("ruleNames") or [""]
        rule = rule_names[0] if rule_names else ""
        issues.append(
            LintIssue(
                line=int(item.get("lineNumber", 0)),
                rule=rule,
                description=str(item.get("ruleDescription", "")).strip(),
                detail=str(item.get("errorDetail") or "").strip(),
            )
        )
    return issues


def find_markdown_files(root: Path, includes: Iterable[str], excludes: Iterable[str]) -> List[Path]:
    files: set[Path] = set()
    for pattern in includes:
        files.update(root.glob(pattern))

    all_excludes = list(DEFAULT_EXCLUDES) + list(excludes)
    result: List[Path] = []
    for file_path in files:
        if not file_path.is_file():
            continue
        rel = file_path.relative_to(root).as_posix()
        if any(fnmatch.fnmatch(rel, pat) for pat in all_excludes):
            continue
        result.append(file_path)
    return sorted(result)


def extract_markdown_response(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return stripped

    if stripped.startswith("```"):
        lines = stripped.splitlines()
        if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].strip() == "```":
            return "\n".join(lines[1:-1]).strip("\n") + "\n"
    return stripped if stripped.endswith("\n") else stripped + "\n"


def build_prompt(path: Path, markdown_text: str, issues: List[LintIssue]) -> str:
    issue_lines = "\n".join(
        f"- line {i.line}: {i.rule} | {i.description} | {i.detail}".strip() for i in issues
    )
    return textwrap.dedent(
        f"""
        You are fixing markdownlint issues in a Markdown file.

        Rules:
        - Return ONLY the full corrected Markdown document.
        - Do not wrap the answer in code fences.
        - Preserve meaning, sections, ordering, and wording unless a lint fix requires a minimal formatting edit.
        - Prefer minimal edits: blank lines, heading spacing, list spacing, emphasis style, trailing newline, etc.
        - Do not invent or remove recipe content.

        File path: {path.as_posix()}

        markdownlint issues:
        {issue_lines}

        Original Markdown:
        {markdown_text}
        """
    ).strip()


def ollama_generate(url: str, model: str, prompt: str, timeout_seconds: int, retries: int, retry_delay: float) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 32000,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")

    last_error: Exception | None = None
    max_attempts = max(1, retries + 1)
    for request_attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                body = response.read().decode("utf-8")
            break
        except urllib.error.HTTPError as exc:
            # Retry transient upstream/server errors.
            last_error = exc
            if exc.code in (408, 409, 425, 429, 500, 502, 503, 504) and request_attempt < max_attempts:
                time.sleep(retry_delay * request_attempt)
                continue
            raise RuntimeError(f"Failed to call Ollama at {url}: HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if request_attempt < max_attempts:
                time.sleep(retry_delay * request_attempt)
                continue
            raise RuntimeError(f"Failed to call Ollama at {url}: {exc}") from exc
    else:
        raise RuntimeError(f"Failed to call Ollama at {url}: {last_error}")

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON from Ollama: {body[:400]}") from exc

    text = str(parsed.get("response", ""))
    if not text.strip():
        raise RuntimeError("Ollama returned empty response")
    return extract_markdown_response(text)


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    if not (root / ".markdownlint.json").exists():
        print(f"ERROR: .markdownlint.json not found in {root}", file=sys.stderr)
        return 2

    try:
        installed_models = fetch_ollama_models(args.ollama_url)
        resolved_model = resolve_ollama_model(args.model, installed_models)
    except RuntimeError as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2

    if resolved_model != args.model:
        print(f"Resolved model '{args.model}' -> '{resolved_model}'")
    args.model = resolved_model

    include_globs = args.glob if args.glob else ["**/*.md"]
    files = find_markdown_files(root, include_globs, args.exclude)
    if args.max_files > 0:
        files = files[: args.max_files]
    print(f"Scanning {len(files)} markdown files under {root}")

    total_files_with_issues = 0
    total_files_fixed = 0
    total_issue_reduction = 0

    for file_path in files:
        rel = file_path.relative_to(root)
        try:
            issues = run_markdownlint(root, file_path)
        except RuntimeError as err:
            print(f"[ERROR] {rel}: {err}")
            continue
        except Exception as err:
            print(f"[ERROR] {rel}: unexpected markdownlint error: {err}")
            continue

        if not issues:
            continue

        total_files_with_issues += 1
        try:
            original_text = file_path.read_text(encoding="utf-8")
        except Exception as err:
            print(f"[ERROR] {rel}: failed to read file: {err}")
            continue
        if len(original_text) > args.max_file_chars:
            print(f"[SKIP ] {rel}: {len(original_text)} chars exceeds max {args.max_file_chars}")
            continue

        print(f"[LINT ] {rel}: {len(issues)} issue(s)")

        best_text = original_text
        best_count = len(issues)
        initial_count = best_count
        improved = False

        for attempt in range(1, args.max_iterations + 1):
            prompt = build_prompt(rel, best_text, issues)
            try:
                candidate = ollama_generate(
                    args.ollama_url,
                    args.model,
                    prompt,
                    args.ollama_timeout,
                    args.ollama_retries,
                    args.retry_delay,
                )
            except RuntimeError as err:
                print(f"[ERROR] {rel}: Ollama attempt {attempt} failed: {err}")
                break

            temp_path = file_path.with_suffix(file_path.suffix + ".tmp_ollama_fix")
            temp_path.write_text(candidate, encoding="utf-8")
            try:
                candidate_issues = run_markdownlint(root, temp_path)
            except RuntimeError as err:
                temp_path.unlink(missing_ok=True)
                print(f"[ERROR] {rel}: candidate lint failed on attempt {attempt}: {err}")
                break
            finally:
                temp_path.unlink(missing_ok=True)

            candidate_count = len(candidate_issues)
            if args.verbose:
                print(f"        attempt {attempt}: {best_count} -> {candidate_count}")

            if candidate_count < best_count:
                best_text = candidate
                best_count = candidate_count
                issues = candidate_issues
                improved = True
                if best_count == 0:
                    break
            else:
                break

        if improved:
            reduction = initial_count - best_count
            total_issue_reduction += max(reduction, 0)
            total_files_fixed += 1
            if args.dry_run:
                print(f"[DRY  ] {rel}: improved to {best_count} issue(s), no write")
            else:
                file_path.write_text(best_text, encoding="utf-8")
                print(f"[FIXED] {rel}: now {best_count} issue(s)")
        else:
            print(f"[KEEP ] {rel}: no improvement after {args.max_iterations} attempt(s)")

    print("\nSummary")
    print(f"- files with lint issues: {total_files_with_issues}")
    print(f"- files improved: {total_files_fixed}")
    print(f"- issue reduction estimate: {total_issue_reduction}")
    if args.dry_run:
        print("- mode: dry-run (no file writes)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        raise SystemExit(130)
