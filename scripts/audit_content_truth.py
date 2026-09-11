#!/usr/bin/env python3
"""
ShriForgeAISkill - Content Truth & Placeholder Auditor
Scans website codebases for leaked placeholders, dummy data, fake contact info,
and unverified claims before production release. Zero external dependencies.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Directories to ignore
IGNORED_DIRS = {
    ".git", ".next", ".astro", "node_modules", "dist", "build", "out",
    ".cache", "coverage", "__pycache__", ".vscode", ".idea"
}

# File extensions to scan
SCANNABLE_EXTENSIONS = {
    ".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte", ".astro",
    ".md", ".mdx", ".json", ".yml", ".yaml"
}

# Regex patterns for findings
PATTERNS = {
    "LOREM_IPSUM": (
        re.compile(r"\blorem\s+ipsum\b", re.IGNORECASE),
        "CRITICAL",
        "Placeholder Latin text detected (Lorem Ipsum)"
    ),
    "DEVELOPMENT_MARKER": (
        re.compile(r"\b(?:TODO|FIXME|TBD|TK|XXX)\b\s*[:\-]", re.IGNORECASE),
        "HIGH",
        "Unresolved development task/marker detected"
    ),
    "INSERT_PLACEHOLDER": (
        re.compile(r"\[(?:insert|replace|enter|add)\s+[^\]]+\]", re.IGNORECASE),
        "CRITICAL",
        "Unfilled bracket placeholder detected (e.g. [insert ...])"
    ),
    "DUMMY_PHONE": (
        re.compile(r"\b(?:555[.\-\s]?\d{4}|123[.\-\s]?456[.\-\s]?7890|0123456789|9876543210|9999999999)\b"),
        "HIGH",
        "Probable placeholder/dummy phone number detected"
    ),
    "DUMMY_EMAIL": (
        re.compile(r"\b[a-zA-Z0-9._%+-]+@(?:example\.com|test\.com|domain\.com|yoursite\.com)\b", re.IGNORECASE),
        "HIGH",
        "Sample/dummy email address detected"
    ),
    "DUMMY_ADDRESS": (
        re.compile(r"\b(?:123\s+Main\s+St|Anytown|Sample\s+City)\b", re.IGNORECASE),
        "HIGH",
        "Dummy street address or sample location detected"
    ),
    "SUSPICIOUS_SUPERLATIVE": (
        re.compile(r"\b(?:#1\s+ranked|best\s+in\s+the\s+world|100%\s+guaranteed|100%\s+placement\s+record|world's\s+leading)\b", re.IGNORECASE),
        "MEDIUM",
        "Unverified superlative claim requires factual evidence per Project Truth"
    ),
}

def scan_file(file_path: Path, root_path: Path) -> list[dict]:
    findings = []
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return findings

    lines = content.splitlines()
    for line_idx, line in enumerate(lines, start=1):
        # Skip commented-out instructions in markdown or docs
        for pattern_name, (regex, severity, desc) in PATTERNS.items():
            match = regex.search(line)
            if match:
                findings.append({
                    "file": str(file_path.relative_to(root_path)),
                    "line": line_idx,
                    "matched_text": match.group(0).strip(),
                    "category": pattern_name,
                    "severity": severity,
                    "description": desc,
                    "snippet": line.strip()[:120]
                })
    return findings

def audit_directory(target_path: Path) -> list[dict]:
    all_findings = []
    for root, dirs, files in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in SCANNABLE_EXTENSIONS:
                # Skip self if scanning workspace
                if p.name in {"audit_content_truth.py", "audit_seo_metadata.py", "test_shriforge_ai_skill.py", "validate_repo.py"}:
                    continue
                findings = scan_file(p, target_path)
                all_findings.extend(findings)
    return all_findings

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit codebase for leaked placeholders and unverified claims.")
    parser.add_argument("path", nargs="?", default=".", help="Root directory to scan (default: current directory)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit with code 1 if any CRITICAL or HIGH findings exist")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        print(f"Error: Target path does not exist: {target}", file=sys.stderr)
        return 2

    findings = audit_directory(target)

    if args.json:
        print(json.dumps({
            "target": str(target),
            "total_findings": len(findings),
            "findings": findings
        }, indent=2))
    else:
        print(f"\n--- ShriForgeAISkill Content Truth Audit ---")
        print(f"Target: {target}")
        print(f"Scanned files with extensions: {', '.join(sorted(SCANNABLE_EXTENSIONS))}\n")

        if not findings:
            print(" [PASS] No placeholder leakage or obvious unverified dummy data found.\n")
            return 0

        severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0}
        for f in findings:
            sev = f["severity"]
            severity_counts[sev] = severity_counts.get(sev, 0) + 1
            print(f"[{sev}] {f['file']}:{f['line']} -> {f['description']}")
            print(f"      Matched: \"{f['matched_text']}\"")
            print(f"      Snippet: {f['snippet']}\n")

        print("--- Summary ---")
        for sev, count in severity_counts.items():
            print(f"  {sev}: {count}")
        print(f"Total findings: {len(findings)}\n")

    if args.fail_on_findings:
        has_blockers = any(f["severity"] in {"CRITICAL", "HIGH"} for f in findings)
        return 1 if has_blockers else 0

    return 0

if __name__ == "__main__":
    sys.exit(main())
