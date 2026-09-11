# Audit Workflow

Use when review/findings are the primary outcome.

## Sequence

1. Define audit scope and evidence available.
2. Inspect only relevant surfaces, expanding when a finding suggests broader risk.
3. Record evidence-based findings using the format below.
4. Prioritize blocker/high findings.
5. If fixes are requested, fix and re-validate affected areas.
6. State unverified areas and final completion state.

## Finding format

Each finding should contain:

- severity (`BLOCKER`, `HIGH`, `MEDIUM`, `LOW`);
- evidence/location;
- user/business/technical impact;
- recommended correction;
- status: observed / fixed / unable-to-verify.

Do not report theoretical checklist items as confirmed defects without evidence.

If the user asks for fixes too, apply the quality loop and re-audit changed areas.


## Contract

- Inspect before editing when a repository exists.
- Establish project truth when factual content is involved.
- Load only required disciplines and one adapter if needed.
- Map change surface before shared or risky changes.
- Validate proportionally and re-run affected checks after fixes.
- Finish with an explicit completion state for substantial work.
