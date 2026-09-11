# /shri-plan

Map audience intent and build a purpose-driven website architecture before writing code.

## Usage

```text
/shri-plan [optional scope or audience description]
```

## Sequence

1. Read `core/task-classification.md` to classify the requested work.
2. Read `core/intent-architecture.md` to establish the audience and information needs:
   - Identify primary and secondary audiences.
   - Map: `Audience → Intent → Information Need → Trust Evidence → Page/Section → Action`.
3. If an existing repository exists, read `core/repository-discovery.md` before planning file changes.
4. Select the matching workflow from `workflows/` (e.g. `workflows/new-website.md`, `workflows/feature-development.md`, or `workflows/redesign.md`).
5. Output a structured plan using `templates/project-plan.md` covering:
   - Goals & Success Conditions
   - Intent & Information Architecture
   - Verified Facts & Critical Unknowns
   - Affected Routes & Design Foundations
   - Step-by-step Execution & Validation Plan
