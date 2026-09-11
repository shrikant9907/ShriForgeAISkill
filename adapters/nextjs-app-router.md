# Next.js App Router Adapter

Use only for projects using Next.js App Router.

## Detect

Look for `next` dependency plus `app/` or `src/app/` and App Router conventions.

## Guidance

- Prefer Server Components by default; add `"use client"` only when browser state/effects/event handlers require it.
- Use framework metadata APIs for page/site metadata instead of manual head manipulation where appropriate.
- Use route-level loading/error/not-found conventions when they improve UX.
- Keep secrets and privileged data access on the server.
- Use framework image/font optimizations when they fit the project.
- Preserve existing caching/rendering choices unless requirements justify change.
- Validate forms/actions on the server when they cross a trust boundary.
- Use the project's actual package manager and scripts.

Next.js APIs evolve. When an API or caching/metadata behavior is uncertain and research tools are available, verify against current official Next.js documentation.
