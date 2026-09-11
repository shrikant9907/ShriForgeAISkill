# Production Release Workflow

Use for final launch/readiness verification.

## Sequence

1. Confirm requested release scope and deployment target.
2. Run all applicable gates from `core/release-gates.md`.
3. Exercise critical user journeys and forms.
4. Check production environment variables/configuration without exposing secrets.
5. Verify canonical domain/indexing/redirect assumptions.
6. Fix blockers/high issues and re-run affected gates.
7. Produce a concise release report with evidence and completion state.

A successful build is necessary for many projects but never sufficient on its own.


## Contract

- Inspect before editing when a repository exists.
- Establish project truth when factual content is involved.
- Load only required disciplines and one adapter if needed.
- Map change surface before shared or risky changes.
- Validate proportionally and re-run affected checks after fixes.
- Finish with an explicit completion state for substantial work.
