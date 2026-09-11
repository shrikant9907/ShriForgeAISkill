# Repository Discovery

Use before substantial edits in an existing project.

## Inspect

1. Root files: README, package manifest, lockfile, ts/js config, lint/format config, env examples, deployment config.
2. Framework/layout: routes, app/pages/src directories, server/client boundaries, public assets.
3. UI: design system, component library, tokens, CSS/Tailwind configuration, typography.
4. Data/content: local content, CMS, database, APIs, schemas, generated data.
5. Quality: test runners, E2E, lint, typecheck, build, accessibility/performance tooling.
6. Search: metadata, sitemap, robots, canonicals, structured data, redirects.
7. Runtime: forms/actions/API routes, auth, uploads, email, third-party scripts.
8. Deployment: provider files, domains, environment variables, CI.

## Output

Create a mental or written project state containing:

- `existing_and_healthy`
- `existing_but_problematic`
- `missing_and_required`
- `unknown`

Do not replace `existing_and_healthy` merely because ShriForgeAISkill has another default.

If the repository already documents commands and architecture, trust those files over generic assumptions unless execution proves they are stale.
