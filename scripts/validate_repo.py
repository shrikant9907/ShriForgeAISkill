#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []

REQUIRED = [
    'SKILL.md','README.md','ARCHITECTURE.md','LICENSE','CONTRIBUTING.md','SECURITY.md',
    'core/task-classification.md','core/project-truth.md','core/intent-architecture.md','core/release-gates.md',
    'workflows/new-website.md','workflows/feature-development.md','workflows/production-release.md'
]

WORKFLOW_SECTIONS = ['# ', '## Sequence']


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def check_required() -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            err(f'missing required file: {rel}')


def check_skill() -> None:
    p=ROOT/'SKILL.md'
    if not p.exists(): return
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        err('SKILL.md missing YAML-style frontmatter')
        return
    m=re.match(r'^---\n(.*?)\n---\n', text, flags=re.S)
    if not m:
        err('SKILL.md frontmatter is malformed')
        return
    fm=m.group(1)
    if not re.search(r'^name:\s*shriforge-ai-skill\s*$', fm, flags=re.M):
        err('SKILL.md must declare name: shriforge-ai-skill')
    if not re.search(r'^description:\s*\S', fm, flags=re.M):
        err('SKILL.md must have a non-empty description')
    lines=len(text.splitlines())
    if lines > 500:
        err(f'SKILL.md is too large for progressive disclosure: {lines} lines > 500')


def check_json() -> None:
    for p in ROOT.rglob('*.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as e: err(f'invalid JSON {p.relative_to(ROOT)}: {e}')


def check_internal_refs() -> None:
    pattern=re.compile(r'`((?:core|workflows|disciplines|adapters|profiles|templates|checklists|examples|commands|agents)/[^`]+?\.(?:md|yml|json))`')
    for p in ROOT.rglob('*.md'):
        text=p.read_text(encoding='utf-8')
        for rel in pattern.findall(text):
            if not (ROOT/rel).exists():
                err(f'broken internal reference in {p.relative_to(ROOT)}: {rel}')


def check_commands_and_agents() -> None:
    for p in (ROOT/'commands').glob('*.md'):
        text=p.read_text(encoding='utf-8')
        if not text.startswith('# /'): err(f'command missing # / title: {p.name}')
        if '## Usage' not in text: err(f'command missing ## Usage section: {p.name}')

    for p in (ROOT/'agents').glob('*.md'):
        text=p.read_text(encoding='utf-8')
        if not text.startswith('# Subagent:'): err(f'agent missing # Subagent: title: {p.name}')
        if '## Primary Objective' not in text: err(f'agent missing ## Primary Objective: {p.name}')

    plugin_file = ROOT / '.claude-plugin' / 'plugin.json'
    if not plugin_file.exists():
        err('missing .claude-plugin/plugin.json manifest')
    else:
        try:
            data = json.loads(plugin_file.read_text(encoding='utf-8'))
            if data.get('name') != 'shriforge-ai-skill':
                err('.claude-plugin/plugin.json has invalid name')
        except Exception as e:
            err(f'malformed .claude-plugin/plugin.json: {e}')


def check_workflows() -> None:
    for p in (ROOT/'workflows').glob('*.md'):
        text=p.read_text(encoding='utf-8')
        if not text.startswith('# '): err(f'workflow missing title: {p.name}')
        if '## Sequence' not in text: err(f'workflow missing Sequence section: {p.name}')
        if 'completion state' not in text.lower() and 'release' not in p.name:
            warn(f'workflow does not explicitly mention completion state: {p.name}')


def check_duplicates() -> None:
    seen: dict[str,Path] = {}
    for p in ROOT.rglob('*'):
        if not p.is_file() or '.git' in p.parts or p.name == 'LICENSE': continue
        data=p.read_bytes()
        if len(data) < 100: continue
        h=hashlib.sha256(data).hexdigest()
        if h in seen:
            err(f'exact duplicate files: {seen[h].relative_to(ROOT)} and {p.relative_to(ROOT)}')
        else: seen[h]=p


def check_generic_residue() -> None:
    forbidden=['Privy','Solana wallet','prediction market']
    generic_dirs=['core','workflows','disciplines','adapters']
    for d in generic_dirs:
        for p in (ROOT/d).rglob('*.md'):
            t=p.read_text(encoding='utf-8')
            for term in forbidden:
                if term.lower() in t.lower():
                    err(f'domain-specific residue "{term}" in generic module {p.relative_to(ROOT)}')


def main() -> int:
    check_required(); check_skill(); check_json(); check_internal_refs(); check_commands_and_agents(); check_workflows(); check_duplicates(); check_generic_residue()
    print(f'ShriForgeAISkill validation: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)')
    for x in ERRORS: print('ERROR:', x)
    for x in WARNINGS: print('WARN: ', x)
    return 1 if ERRORS else 0

if __name__ == '__main__':
    raise SystemExit(main())
