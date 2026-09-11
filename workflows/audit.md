# Audit Workflow

Use when evaluating an existing website or release candidate for technical health, UX, SEO, and content truth.

## Sequence

1. Define audit scope (Quick vs. Full) and collect repository/network evidence.
2. Delegate specialist reviews in parallel when subagents are supported:
   - `agents/truth-auditor.md` audits business claims, contact details, and placeholder leakage.
   - `agents/web-architect.md` audits component boundaries, layout shift (CLS), and mobile responsiveness.
   - `agents/release-evaluator.md` evaluates the 13 formal quality gates and VATM score.
3. Run automated verification scripts:
   - `python scripts/audit_content_truth.py .`
   - `python scripts/audit_seo_metadata.py .`
4. Record all findings using the **Falsifiability Protocol** below.
5. Prioritize issues (`BLOCKER`, `HIGH`, `MEDIUM`, `LOW`).
6. Deliver actionable report with explicit completion state (`PASS`, `PASS_WITH_NOTES`, `BLOCKED`, `FAIL`).

## Falsifiability Protocol (Evidence-Based Finding Format)

Every recorded finding must be testable and verifiable. Never report hypothetical issues without observable evidence:

```markdown
### [SEVERITY] Finding Title
- **Location / Evidence**: File path, line number, or exact HTTP header/response observed.
- **Impact**: Concrete risk to user experience, search indexing, or business trust.
- **Recommended Correction**: Exact code change or content replacement.
- **Falsifiable Verification Test**: Exactly how to prove this fix succeeded (e.g. `curl -I`, Rich Results Test, or test script pass).
- **Status**: `OPEN` / `VERIFIED_FIXED` / `UNABLE_TO_VERIFY`
```

## Contract

- Inspect before editing when a repository exists.
- Establish project truth when factual content is involved.
- Load only required disciplines and one adapter if needed.
- Map change surface before shared or risky changes.
- Validate proportionally and re-run affected checks after fixes.
- Finish with an explicit completion state for substantial work.
