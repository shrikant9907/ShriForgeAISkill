# /truth-check

Scan the project for unverified claims, fabricated statistics, fake testimonials, leaked placeholders, or synthetic credentials.

## Usage

```text
/truth-check [optional directory or file path]
```

## Sequence

1. Load `core/project-truth.md` and `checklists/content-truth.md`.
2. If python is available, execute `scripts/audit_content_truth.py` on the target workspace:
   ```bash
   python scripts/audit_content_truth.py .
   ```
3. Manually review content surfaces for:
   - Claims regarding awards, rankings, accreditations, affiliations, and legal disclosures.
   - Numbers: student counts, customer counts, pass rates, pricing, years in business.
   - People: staff names, leadership titles, doctor/faculty credentials.
   - Contact details: real vs dummy phone numbers (`555-`, `1234567890`), addresses, emails.
   - Placeholder text: `Lorem Ipsum`, `TODO`, `TK`, sample images.
4. Classify all identified findings into `core/project-truth.md` tiers:
   - `FACT` (verified with source)
   - `UNVERIFIED_CLAIM` (must be verified or removed before production release)
   - `PLACEHOLDER` (leaked draft content)
5. Provide actionable remediation: either remove unsupported claims, mark them clearly as dev placeholders, or prompt the user for factual data.
