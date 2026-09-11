# Architecture

ShriForgeAISkill is one Agent Skill with progressive disclosure.

`SKILL.md` owns orchestration. `core/` owns universal ShriForgeAISkill operating rules. `workflows/` owns task sequences. `disciplines/` owns canonical methodology. `adapters/` owns framework mechanics. `profiles/` owns domain specialization. Templates/checklists/examples support execution but are not automatically authoritative.

## Dependency direction

```text
SKILL.md
 ├─ core
 ├─ one workflow
 ├─ selected disciplines
 ├─ zero/one adapter
 └─ zero/one profile
```

Modules should not create circular instruction dependencies.

## Canonical ownership

If a rule applies everywhere, place it in `core/`. If it describes how to execute a task class, place it in a workflow. If it defines a practice such as accessibility or SEO, place it in one discipline. Framework-specific API mechanics belong only in an adapter. Domain facts/default intents belong only in a profile.

Do not repeat long policy blocks across layers; link to the canonical file.
