#!/usr/bin/env python3
"""Deterministic markdownlint checker/fixer.

Uses markdownlint-cli directly (same engine as the VS Code extension) and never
uses an LLM. Intended for non-destructive formatting repairs only.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import shlex
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


DEFAULT_EXCLUDES = [
    "**/.git/**",
    "**/.venv/**",
    "**/.astro/**",
    "**/node_modules/**",
    "**/dist/**",
    "**/site/dist/**",
]


@dataclass(frozen=True)
class LintIssue:
    line: int
    rule: str
    description: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Safe markdownlint workflow: check, dry-run fixes, or apply fixes"
    )
    parser.add_argument("--root", default=".", help="Repository root (default: current directory)")
    parser.add_argument(
        "--glob",
        action="append",
        default=None,
        help='Include glob for markdown files (repeatable). Default: "**/*.md"',
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help="Exclude glob for markdown files (repeatable)",
    )
    parser.add_argument(
        "--mode",
        choices=["check", "dry-run", "fix"],
        default="check",
        help="check: report only, dry-run: simulate fixes on temp copies, fix: apply safe fixes",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=0,
        help="Process at most N markdown files after filtering (0 = no limit)",
    )
    parser.add_argument(
        "--config",
        default=".markdownlint.json",
        help="Path to markdownlint config (default: .markdownlint.json)",
    )
    parser.add_argument(
        "--markdownlint-cmd",
        default="npx --yes markdownlint-cli@0.39.0",
        help="Command used to invoke markdownlint (default: npx --yes markdownlint-cli@0.39.0)",
    )
    parser.add_argument(
        "--markdownlint-timeout",
        type=int,
        default=45,
        help="Timeout in seconds for each markdownlint invocation (default: 45)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print per-file details",
    )
    return parser.parse_args()


def run_markdownlint(
    root: Path,
    config_path: Path,
    file_path: Path,
    markdownlint_cmd: str,
    markdownlint_timeout: int,
    *,
    fix: bool = False,
) -> tuple[int, str, str]:
    cmd = shlex.split(markdownlint_cmd) + ["--json", "--config", str(config_path)]
    if fix:
        cmd.append("--fix")
    cmd.append(str(file_path))

    try:
        proc = subprocess.run(
            cmd,
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=markdownlint_timeout,
        )
    except subprocess.TimeoutExpired as err:
        raise RuntimeError(
            f"markdownlint timed out after {markdownlint_timeout}s for {file_path}. "
            "Try a local binary via --markdownlint-cmd."
        ) from err

    return proc.returncode, (proc.stdout or "").strip(), (proc.stderr or "").strip()


def parse_lint_issues(stdout: str, stderr: str, exit_code: int, file_path: Path) -> list[LintIssue]:
    text = stdout or stderr
    if not text:
        if exit_code == 0:
            return []
        raise RuntimeError(f"markdownlint failed for {file_path}: no output")

    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        if exit_code == 0:
            return []
        raise RuntimeError(
            f"Could not parse markdownlint output for {file_path}\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}"
        )

    issues: list[LintIssue] = []
    for _, path_issues in payload.items():
        for item in path_issues:
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


def find_markdown_files(root: Path, includes: list[str], excludes: list[str]) -> list[Path]:
    files: set[Path] = set()
    for pattern in includes:
        files.update(root.glob(pattern))

    all_excludes = DEFAULT_EXCLUDES + excludes
    result: list[Path] = []
    for file_path in files:
        if not file_path.is_file():
            continue
        rel = file_path.relative_to(root).as_posix()
        if any(fnmatch.fnmatch(rel, pat) for pat in all_excludes):
            continue
        result.append(file_path)

    return sorted(result)


def lint_file(
    root: Path,
    config_path: Path,
    file_path: Path,
    markdownlint_cmd: str,
    markdownlint_timeout: int,
) -> list[LintIssue]:
    code, stdout, stderr = run_markdownlint(
        root,
        config_path,
        file_path,
        markdownlint_cmd,
        markdownlint_timeout,
    )
    return parse_lint_issues(stdout, stderr, code, file_path)


def dry_run_file(
    root: Path,
    config_path: Path,
    file_path: Path,
    markdownlint_cmd: str,
    markdownlint_timeout: int,
) -> tuple[int, int, bool]:
    before = lint_file(root, config_path, file_path, markdownlint_cmd, markdownlint_timeout)
    if not before:
        return 0, 0, False

    with tempfile.TemporaryDirectory(prefix="mdlint_") as tmp_dir:
        temp_path = Path(tmp_dir) / file_path.name
        temp_path.write_text(file_path.read_text(encoding="utf-8"), encoding="utf-8")

        run_markdownlint(
            root,
            config_path,
            temp_path,
            markdownlint_cmd,
            markdownlint_timeout,
            fix=True,
        )
        after = lint_file(root, config_path, temp_path, markdownlint_cmd, markdownlint_timeout)

        changed = temp_path.read_text(encoding="utf-8") != file_path.read_text(encoding="utf-8")
        return len(before), len(after), changed


def fix_file(
    root: Path,
    config_path: Path,
    file_path: Path,
    markdownlint_cmd: str,
    markdownlint_timeout: int,
) -> tuple[int, int, bool]:
    original_text = file_path.read_text(encoding="utf-8")
    before = lint_file(root, config_path, file_path, markdownlint_cmd, markdownlint_timeout)
    if not before:
        return 0, 0, False

    run_markdownlint(
        root,
        config_path,
        file_path,
        markdownlint_cmd,
        markdownlint_timeout,
        fix=True,
    )
    after = lint_file(root, config_path, file_path, markdownlint_cmd, markdownlint_timeout)
    new_text = file_path.read_text(encoding="utf-8")

    before_count = len(before)
    after_count = len(after)
    changed = new_text != original_text

    if after_count > before_count:
        file_path.write_text(original_text, encoding="utf-8")
        return before_count, before_count, False

    return before_count, after_count, changed


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    config_path = (root / args.config).resolve() if not Path(args.config).is_absolute() else Path(args.config)

    if not config_path.exists():
        print(f"ERROR: markdownlint config not found: {config_path}", file=sys.stderr)
        return 2

    include_globs = args.glob if args.glob else ["**/*.md"]
    files = find_markdown_files(root, include_globs, args.exclude)
    if args.max_files > 0:
        files = files[: args.max_files]

    print(f"Mode: {args.mode}")
    print(f"Config: {config_path}")
    print(f"Markdownlint command: {args.markdownlint_cmd}")
    print(f"Scanning {len(files)} markdown files under {root}")

    files_with_issues = 0
    files_changed = 0
    issue_reduction = 0
    files_skipped_no_gain = 0

    for file_path in files:
        rel = file_path.relative_to(root)
        try:
            if args.mode == "check":
                issues = lint_file(
                    root,
                    config_path,
                    file_path,
                    args.markdownlint_cmd,
                    args.markdownlint_timeout,
                )
                if not issues:
                    continue
                files_with_issues += 1
                if args.verbose:
                    print(f"[LINT ] {rel}: {len(issues)} issue(s)")
                continue

            if args.mode == "dry-run":
                before_count, after_count, changed = dry_run_file(
                    root,
                    config_path,
                    file_path,
                    args.markdownlint_cmd,
                    args.markdownlint_timeout,
                )
            else:
                before_count, after_count, changed = fix_file(
                    root,
                    config_path,
                    file_path,
                    args.markdownlint_cmd,
                    args.markdownlint_timeout,
                )

            if before_count == 0:
                continue

            files_with_issues += 1
            if after_count < before_count:
                issue_reduction += before_count - after_count
                if changed:
                    files_changed += 1
                label = "DRY" if args.mode == "dry-run" else "FIX"
                print(f"[{label:4}] {rel}: {before_count} -> {after_count}")
            else:
                files_skipped_no_gain += 1
                if args.verbose:
                    print(f"[KEEP ] {rel}: {before_count} -> {after_count}")

        except Exception as err:
            print(f"[ERROR] {rel}: {err}")

    print("\nSummary")
    print(f"- files with lint issues: {files_with_issues}")
    print(f"- files changed: {files_changed}")
    print(f"- issue reduction: {issue_reduction}")
    print(f"- files with no safe gain: {files_skipped_no_gain}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())