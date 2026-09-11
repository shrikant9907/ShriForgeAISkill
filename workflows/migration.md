# Migration Workflow

Use for framework/CMS/hosting/routing/content-model/major architecture moves.

## Sequence

1. Inventory current routes, content, forms, metadata, redirects, analytics, integrations, environment variables, and deployment behavior.
2. Define parity requirements and intentional changes.
3. Map old URLs/data/contracts to new equivalents.
4. Migrate in testable increments.
5. Preserve search equity with redirects/canonicals where applicable.
6. Validate forms, integrations, content truth, analytics, accessibility, and deployment.
7. Remove old infrastructure only after parity/replacement is verified.


## Contract

- Inspect before editing when a repository exists.
- Establish project truth when factual content is involved.
- Load only required disciplines and one adapter if needed.
- Map change surface before shared or risky changes.
- Validate proportionally and re-run affected checks after fixes.
- Finish with an explicit completion state for substantial work.
