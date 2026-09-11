---
name: shriforge-ai-skill
description: Plan, design, build, improve, audit, and release production websites. Use for new websites, existing website changes, redesigns, content/search improvements, accessibility/performance/security work, framework migrations, and final production-readiness reviews. Inspect existing repositories before changing them, preserve verified project truth, route selectively to only the needed modules, and validate work before calling it complete.
---

# ShriForgeAISkill

ShriForgeAISkill is a production website engineering skill. It treats a website as a product to understand, design, implement, validate, improve, and ship—not as a page-generation task.

## Operating contract

Follow these rules throughout every task:

1. **Repository first.** For an existing project, inspect its framework, package manager, structure, conventions, content sources, tests, and deployment clues before editing.
2. **Evidence before claims.** Never invent business facts, awards, affiliations, reviews, ratings, statistics, people, addresses, fees, credentials, or regulatory claims. Use `core/project-truth.md` when factual content matters.
3. **Intent before pages.** Derive information architecture from audience goals and information needs, not from a generic page checklist. Use `core/intent-architecture.md` for new sites or structural redesigns.
4. **Selective routing.** Do not load every module. Classify the task, choose one workflow, then load only the disciplines, adapter, and profile required.
5. **Preserve project fit.** Reuse healthy infrastructure and conventions. Do not replace working architecture merely because another stack is preferred.
6. **Progressive complexity.** Prefer the simplest robust solution. Add dependencies, client JavaScript, state, animation, services, or abstractions only when they materially improve the result.
7. **Current authoritative guidance wins.** When framework APIs, browser behavior, standards, search guidance, or security requirements may have changed and tools permit verification, prefer current primary documentation over remembered details.
8. **Quality is iterative.** Build → validate → find failures → prioritize → fix → re-validate. A successful compile alone is never proof of production readiness.
9. **Proportional validation.** A one-line content fix should not trigger a full release audit; a production launch should.
10. **Explicit completion state.** End substantial work as `PASS`, `PASS_WITH_NOTES`, `BLOCKED`, or `FAIL` per `core/release-gates.md`.

## 1. Classify the task

Read `core/task-classification.md` when the task is not trivially obvious. Choose one primary workflow:

| Task | Workflow |
|---|---|
| New site from an empty/minimal project | `workflows/new-website.md` |
| Significant work in an existing site | `workflows/existing-website.md` |
| Add/change a feature or page | `workflows/feature-development.md` |
| Visual/UX redesign | `workflows/redesign.md` |
| Reproduce and fix a defect | `workflows/bug-fix.md` |
| Change factual/editorial content | `workflows/content-update.md` |
| Improve SEO/AEO/GEO/local discoverability | `workflows/search-optimization.md` |
| Review without broad implementation | `workflows/audit.md` |
| Move stack/framework/architecture | `workflows/migration.md` |
| Final launch/release verification | `workflows/production-release.md` |

## 2. Discover project state

For an existing repository, inspect before planning. Determine at minimum:

- framework/runtime and version clues;
- package manager and lockfile;
- route/page structure;
- component/design-system conventions;
- styling approach;
- data/content sources and CMS/database integrations;
- forms/server actions/APIs;
- metadata, sitemap, robots, schema, analytics;
- tests, linting, type checks, build commands;
- environment-variable documentation;
- hosting/deployment configuration;
- existing accessibility/performance/security tooling.

Use `core/repository-discovery.md` and `core/change-surface.md` for non-trivial existing-project work.

## 3. Establish project truth

When the task publishes or transforms factual business information, load `core/project-truth.md`.

Classify information as:

- `FACT` — verified from supplied project/source;
- `REQUIREMENT` — explicitly requested;
- `RULE` — applicable technical/product guidance;
- `DECISION` — implementation/design decision;
- `ASSUMPTION` — useful but unverified;
- `UNKNOWN` — missing.

Only verified `FACT`s may be presented as business facts. Assumptions can guide implementation but must not silently become published claims.

## 4. Model audience and intent when structure matters

For a new site, major redesign, navigation change, content architecture change, or search task, load `core/intent-architecture.md`.

Derive:

`Audience → Intent → Needed information → Trust evidence → Page/section → Content → CTA → Search entity`

Avoid pages that have no clear user or business purpose.

## 5. Select only applicable disciplines

Choose from `disciplines/` based on the task:

- requirements and scope → `product-requirements.md`
- navigation/content hierarchy → `information-architecture.md`
- flows/usability → `ux.md`
- visual direction/design system → `visual-design.md`
- copy/content → `content.md`
- implementation → `frontend-engineering.md`
- mobile/layout → `responsive-design.md`
- search metadata/crawlability → `seo.md`
- answer/AI-search readability → `aeo-geo.md`
- physical/local discoverability → `local-search.md`
- JSON-LD/schema → `structured-data.md`
- accessibility → `accessibility.md`
- performance → `performance.md`
- security/privacy/forms → `security-privacy.md`
- testing → `testing.md`
- release/handoff → `deployment-documentation.md`

Do not load a discipline only because it exists.

## 6. Select a framework adapter

Load exactly one adapter when framework-specific implementation matters:

- Next.js App Router → `adapters/nextjs-app-router.md`
- React + Vite → `adapters/react-vite.md`
- Astro → `adapters/astro.md`
- Static HTML/CSS/JS → `adapters/static-html.md`

If the repository uses something else, follow the repository and current authoritative framework documentation; do not force one of these adapters.

## 7. Select an optional domain profile

Profiles specialize the engine without replacing it:

- Indian school/college → `profiles/school-india.md`
- local business → `profiles/local-business.md`
- SaaS marketing → `profiles/saas-marketing.md`

Load a profile only when it matches the project.

## 8. Plan proportional to scope

For substantial work, record:

- goal and success condition;
- verified facts and material unknowns;
- affected routes/files/components/data;
- design/content implications;
- selected workflow, disciplines, adapter, profile;
- implementation steps;
- validation steps;
- blockers or assumptions.

Use `templates/project-plan.md` when a persistent plan is useful. Do not create project-management files for tiny changes unless requested or already conventional in the repository.

## 9. Implement the smallest coherent solution

During implementation:

- follow healthy local conventions;
- keep components and data boundaries understandable;
- use semantic HTML first;
- prefer server/static rendering when interactivity is unnecessary;
- make loading, empty, error, and success states explicit when relevant;
- keep responsive behavior intentional;
- avoid deceptive or unsupported content;
- do not expose secrets;
- validate user-controlled input at trust boundaries;
- preserve URLs/search equity during migrations where applicable.

## 10. Validate and iterate

Use `core/release-gates.md` plus the selected workflow's gates. Validate the changed surface first, then broader surfaces as risk demands.

Applicable checks can include:

- build/type/lint;
- route/navigation behavior;
- forms and validation;
- mobile/tablet/desktop layouts;
- keyboard/focus/labels/semantics;
- metadata/indexing/schema;
- content truth and placeholder leakage;
- performance regressions;
- security/privacy issues;
- tests and console/runtime errors;
- deployment/environment configuration.

Fix `BLOCKER` and `HIGH` issues when access and information permit. Re-run affected checks after fixes.

## 11. Completion report

For substantial tasks, finish with:

1. what changed;
2. validation actually performed;
3. remaining assumptions/placeholders/limitations;
4. release state: `PASS`, `PASS_WITH_NOTES`, `BLOCKED`, or `FAIL`.

Do not claim tests, audits, Lighthouse scores, schema validation, or deployments that were not actually run.

## Module loading rule

The files in this skill are references, not a checklist to read wholesale. Start with this file, then open only the workflow and modules needed for the current task. This progressive-disclosure rule is part of ShriForgeAISkill's design.
