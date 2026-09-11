# Bug Fix Workflow

Use when existing behavior is incorrect.

## Sequence

1. Reproduce or establish evidence of the failure.
2. Trace the smallest plausible cause before editing.
3. Add or identify a regression test when practical.
4. Apply the smallest safe fix.
5. Validate the original failure and nearby behavior.
6. Avoid opportunistic refactors unless they are required for correctness.

If reproduction is impossible, clearly separate confirmed facts from hypotheses.


## Contract

- Inspect before editing when a repository exists.
- Establish project truth when factual content is involved.
- Load only required disciplines and one adapter if needed.
- Map change surface before shared or risky changes.
- Validate proportionally and re-run affected checks after fixes.
- Finish with an explicit completion state for substantial work.
