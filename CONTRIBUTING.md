# Contributing

Contributions are welcome.

## Principles

- Keep `SKILL.md` an orchestrator; do not turn it into a knowledge dump.
- Define each canonical rule in one place.
- Use `MUST` only for genuine correctness/safety/truth requirements.
- Keep framework mechanics out of `core/`.
- Keep domain-specific claims out of generic modules.
- Do not copy substantial text/code from another skill/repository without compatible licensing and required attribution.
- Add or update tests for routing, structural contracts, and validation behavior when applicable.

## Before opening a PR

Run:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Update `CHANGELOG.md` for user-visible behavior changes.
