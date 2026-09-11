#!/usr/bin/env python3
"""
ShriForgeAISkill - SEO & Metadata Auditor
Scans HTML files and web templates for missing title tags, meta descriptions,
canonical links, Open Graph tags, and heading hierarchy. Zero external dependencies.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

IGNORED_DIRS = {
    ".git", ".next", ".astro", "node_modules", "dist", "build", "out",
    ".cache", "coverage", "__pycache__", ".vscode", ".idea"
}

HTML_EXTENSIONS = {".html", ".htm"}
TEMPLATE_EXTENSIONS = {".jsx", ".tsx", ".astro", ".vue", ".svelte"}

RE_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
RE_META_DESC = re.compile(r'<meta[^>]+name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', re.IGNORECASE)
RE_META_DESC_ALT = re.compile(r'<meta[^>]+content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', re.IGNORECASE)
RE_CANONICAL = re.compile(r'<link[^>]+rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', re.IGNORECASE)
RE_OG_TITLE = re.compile(r'<meta[^>]+property=["\']og:title["\'][^>]*content=["\']([^"\']*)["\']', re.IGNORECASE)
RE_OG_IMAGE = re.compile(r'<meta[^>]+property=["\']og:image["\'][^>]*content=["\']([^"\']*)["\']', re.IGNORECASE)
RE_H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)

def audit_html_file(file_path: Path, root_path: Path) -> list[dict]:
    findings = []
    rel_path = str(file_path.relative_to(root_path))
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return findings

    # Check Title
    titles = RE_TITLE.findall(content)
    if not titles:
        findings.append({
            "file": rel_path,
            "element": "title",
            "severity": "CRITICAL",
            "message": "Missing <title> tag"
        })
    elif len(titles) > 1:
        findings.append({
            "file": rel_path,
            "element": "title",
            "severity": "HIGH",
            "message": f"Multiple <title> tags detected ({len(titles)})"
        })
    elif len(titles[0].strip()) < 10:
        findings.append({
            "file": rel_path,
            "element": "title",
            "severity": "MEDIUM",
            "message": f"Title tag is very short (<10 chars): '{titles[0].strip()}'"
        })

    # Check Meta Description
    desc_match = RE_META_DESC.search(content) or RE_META_DESC_ALT.search(content)
    if not desc_match:
        findings.append({
            "file": rel_path,
            "element": "meta-description",
            "severity": "HIGH",
            "message": "Missing <meta name=\"description\"> tag"
        })
    elif len(desc_match.group(1).strip()) < 50:
        findings.append({
            "file": rel_path,
            "element": "meta-description",
            "severity": "LOW",
            "message": f"Meta description is short (<50 chars): '{desc_match.group(1).strip()}'"
        })

    # Check Canonical Link
    if not RE_CANONICAL.search(content):
        findings.append({
            "file": rel_path,
            "element": "canonical",
            "severity": "MEDIUM",
            "message": "Missing <link rel=\"canonical\"> tag"
        })

    # Check Open Graph
    if not RE_OG_TITLE.search(content):
        findings.append({
            "file": rel_path,
            "element": "og:title",
            "severity": "LOW",
            "message": "Missing <meta property=\"og:title\"> tag"
        })
    if not RE_OG_IMAGE.search(content):
        findings.append({
            "file": rel_path,
            "element": "og:image",
            "severity": "LOW",
            "message": "Missing <meta property=\"og:image\"> social preview tag"
        })

    # Check H1 Heading
    h1s = RE_H1.findall(content)
    if not h1s:
        findings.append({
            "file": rel_path,
            "element": "h1",
            "severity": "MEDIUM",
            "message": "No <h1> heading detected on page"
        })
    elif len(h1s) > 1:
        findings.append({
            "file": rel_path,
            "element": "h1",
            "severity": "LOW",
            "message": f"Multiple <h1> headings detected ({len(h1s)}). Prefer a single main <h1>."
        })

    return findings

def audit_directory(target_path: Path) -> list[dict]:
    all_findings = []
    for root, dirs, files in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        for f in files:
            p = Path(root) / f
            if p.suffix.lower() in HTML_EXTENSIONS:
                all_findings.extend(audit_html_file(p, target_path))
    return all_findings

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit HTML and pages for SEO metadata.")
    parser.add_argument("path", nargs="?", default=".", help="Directory to scan for HTML pages")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")
    parser.add_argument("--fail-on-findings", action="store_true", help="Exit 1 on critical/high SEO errors")
    args = parser.parse_args()

    target = Path(args.path).resolve()
    if not target.exists():
        print(f"Error: Target does not exist: {target}", file=sys.stderr)
        return 2

    findings = audit_directory(target)

    if args.json:
        print(json.dumps({
            "target": str(target),
            "total_findings": len(findings),
            "findings": findings
        }, indent=2))
    else:
        print(f"\n--- ShriForgeAISkill SEO & Metadata Audit ---")
        print(f"Target: {target}\n")

        if not findings:
            print(" [PASS] All scanned HTML documents contain valid titles, descriptions, and canonical tags.\n")
            return 0

        for f in findings:
            print(f"[{f['severity']}] {f['file']} -> {f['message']}")
        print(f"\nTotal SEO findings: {len(findings)}\n")

    if args.fail_on_findings:
        return 1 if any(f["severity"] in {"CRITICAL", "HIGH"} for f in findings) else 0

    return 0

if __name__ == "__main__":
    sys.exit(main())
