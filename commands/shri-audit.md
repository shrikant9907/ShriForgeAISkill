# /shri-audit

Execute an evidence-based production readiness audit across technical, UX, SEO, and content dimensions using parallel evaluation.

## Usage

```text
/shri-audit [optional scope or route]
```

## Sequence

1. Load `workflows/audit.md` and `checklists/pre-launch.md`.
2. Inspect project structure and configuration via `core/repository-discovery.md`.
3. When subagents are supported, delegate reviews in parallel:
   - Run `agents/truth-auditor.md` to verify all business claims and scan for dummy data.
   - Run `agents/web-architect.md` to review component architecture, responsive layouts, and CLS/INP risks.
   - Run `agents/release-evaluator.md` to evaluate the 13 gates and calculate the VATM score (`disciplines/seo.md`).
4. Execute automated verification tools:
   ```bash
   python scripts/audit_content_truth.py .
   python scripts/audit_seo_metadata.py .
   ```
5. Record all defects using the **Falsifiability Protocol** (Location, Impact, Fix, Verification Test).
6. Generate a structured audit report using `templates/audit-report.md`.
7. Deliver final release state: `PASS`, `PASS_WITH_NOTES`, `BLOCKED`, or `FAIL`.
