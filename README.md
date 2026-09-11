# ShriForgeAISkill

> **Production Web Engineering Skill by Shrimo Innovations**

Created by **Shrikant Yadav**

**ShriForgeAISkill** is an open-source AI Agent Skill for planning, designing, building, improving, auditing, and shipping production-ready websites.

It gives coding agents a structured engineering methodology for turning requirements into reliable web experiences through repository-aware planning, evidence-based content decisions, intent-first architecture, selective workflows, and explicit quality gates.

[**Website**](https://shrimo-innovations.github.io/shriforge-ai-skill/) · [**Source**](https://github.com/shrimo-innovations/shriforge-ai-skill) · [**Issues**](https://github.com/shrimo-innovations/shriforge-ai-skill/issues) · **Apache-2.0**

---

## Why ShriForgeAISkill?

Building a website is more than generating components. A production website must also consider user intent, information architecture, visual design, responsive behavior, accessibility, performance, SEO and discoverability, structured data, security, privacy, maintainability, testing, and deployment readiness.

ShriForgeAISkill coordinates those concerns through one engineering system:

```text
Understand → Plan → Architect → Design → Build → Validate → Improve → Ship
```

It is deliberately **not** one giant prompt. The master skill routes only the workflows, disciplines, framework guidance, and domain knowledge relevant to the current task.

## What makes it different

### Repository-aware

For existing projects, ShriForgeAISkill inspects the repository before making significant changes. It aims to preserve healthy architecture, conventions, components, dependencies, and business logic instead of replacing working infrastructure unnecessarily.

### Evidence before claims

The **Project Truth** model separates information into:

```text
FACT · REQUIREMENT · RULE · DECISION · ASSUMPTION · UNKNOWN
```

Unverified business claims should never silently become published facts. This helps prevent fabricated achievements, affiliations, statistics, testimonials, ratings, credentials, locations, and organization details.

### Intent before pages

ShriForgeAISkill does not start with “what pages should we generate?” It derives architecture from what people need to accomplish:

```text
Audience → Intent → Information Need → Trust Requirement → Page / Section → Content → Action
```

### Selective execution

Different tasks activate different workflows:

```text
Build a complete website          → full website workflow
Add an admissions page           → feature workflow
Fix mobile navigation            → bug-fix workflow
Make the homepage more premium   → redesign workflow
Audit before launch              → audit + release gates
```

### Continuous quality loop

Generated code is not the finish line:

```text
BUILD → VALIDATE → FIND ISSUES → PRIORITIZE → FIX → RE-VALIDATE → PASS / ITERATE
```

## Capabilities

ShriForgeAISkill includes methodologies for:

- **Product & architecture** — requirements, repository discovery, information architecture, visitor intent, change-surface analysis, and technical decision making.
- **Design & experience** — UX planning, visual direction, responsive design, content hierarchy, interaction design, and component systems.
- **Frontend engineering** — framework-aware implementation, forms and validation, loading/error/empty states, and maintainable component architecture.
- **Search & discoverability** — SEO, AEO/GEO, local search, metadata, structured data, internal linking, and crawlability.
- **Quality engineering** — accessibility, performance, security, privacy, testing, deployment readiness, and final production audits.

## Supported workflows

```text
New Website
Existing Website
Feature Development
Redesign
Bug Fix
Content Update
Search Optimization
Website Audit
Migration
Production Release
```

Each workflow defines when to use it, required inputs, discovery and planning steps, execution sequence, applicable disciplines, validation gates, expected outputs, and blocker conditions.

## Framework architecture

The core methodology is framework-neutral. Framework-specific behavior is handled through adapters.

Current adapters cover:

- Next.js App Router
- React / Vite
- Astro
- Static HTML / CSS / JavaScript

## Domain profiles

Profiles specialize the same engineering system without duplicating it. Current profiles include:

- schools and educational institutions;
- local businesses;
- SaaS marketing websites.

## Install as a Claude Code skill

Clone the repository into a Claude Code skill directory supported by your environment.

Project-local example:

```bash
git clone https://github.com/shrimo-innovations/shriforge-ai-skill.git \
  .claude/skills/shriforge-ai-skill
```

The directory containing `SKILL.md` is the skill root.

Then ask Claude Code for outcomes such as:

> Build a production-ready website for a school in India. Make it professional, trustworthy and mobile-first. Handle architecture, design, implementation, SEO, accessibility, performance, testing, and final validation. Do not invent school facts.

Or:

> Inspect this repository first. Add a new admissions page that follows the existing architecture and design system. Validate accessibility, mobile behavior, metadata, and navigation before considering the task complete.

## Official project website

The repository includes a dependency-free GitHub Pages site under [`docs/`](docs/).

Once GitHub Pages is enabled from the `main` branch and `/docs` folder, it is available at:

**https://shrimo-innovations.github.io/shriforge-ai-skill/**

The site is built with semantic HTML, responsive CSS, accessible focus behavior, reduced-motion support, and minimal JavaScript. No build step is required.

## Repository structure

```text
ShriForgeAISkill/
├── SKILL.md          master orchestrator and operating contract
├── core/             routing, Project Truth, intent, decisions, release gates
├── workflows/        task-specific execution contracts
├── disciplines/      canonical product, design, and engineering methodologies
├── adapters/         framework-specific implementation guidance
├── profiles/         domain-specific specialization
├── checklists/       compact verification and release aids
├── templates/        optional planning, audit, and handoff artifacts
├── schemas/          structured schemas for ShriForgeAISkill state
├── examples/         non-authoritative routing examples
├── scripts/          repository validation utilities
├── tests/            behavioral and structural validation
└── docs/             official GitHub Pages website
```

## Core design principles

- **One brain, selective modules** — the master skill orchestrates while specialized knowledge stays modular.
- **Repository first** — understand an existing project before changing it.
- **Evidence before claims** — assumptions never silently become facts.
- **Intent before pages** — structure follows what users need to accomplish.
- **Progressive disclosure** — detailed guidance loads only when the task requires it.
- **Framework-neutral core** — general methodology is not tied to one stack.
- **Proportional validation** — validation matches scope and risk.
- **Explicit completion** — work ends with a clear release state.

## Release states

ShriForgeAISkill uses four completion states:

| State | Meaning |
|---|---|
| `PASS` | All applicable release gates passed. |
| `PASS_WITH_NOTES` | Ready with documented non-blocking limitations. |
| `BLOCKED` | Completion depends on missing information, credentials, infrastructure, or another dependency. |
| `FAIL` | Known blocking defects remain. |

## Validation

Run the repository validator:

```bash
python scripts/validate_repo.py
```

Run the test suite:

```bash
python -m unittest discover -s tests -v
```

The validation system checks required files, skill metadata, internal references, schemas, workflow contracts, duplicate content, routing expectations, Project Truth behavior, and repository consistency.

## Development philosophy

ShriForgeAISkill prefers:

```text
simple over unnecessary complexity
evidence over assumptions
intent over templates
clarity over cleverness
reuse over duplication
accessibility over visual gimmicks
performance over unnecessary JavaScript
maintainability over premature abstraction
validation over confidence
```

The goal is not to generate the largest amount of code. The goal is to produce the **smallest coherent implementation that satisfies the product requirement and passes the applicable quality gates**.

## Contributing

Contributions that improve engineering methodology, framework support, accessibility, design quality, testing, security, performance, domain profiles, documentation, or validation are welcome.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## Project information

- **Project:** ShriForgeAISkill
- **Organization:** Shrimo Innovations
- **Creator:** Shrikant Yadav
- **Category:** AI Agent Skill / Production Web Engineering
- **License:** Apache-2.0

## License

Licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE).

---

<p align="center">
  <strong>ShriForgeAISkill</strong><br>
  Production Web Engineering Skill by Shrimo Innovations
</p>

<p align="center"><em>From intent to production.</em></p>
