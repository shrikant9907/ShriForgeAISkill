# /release-gate

Evaluate the 13 production release gates and deliver an unambiguous launch status.

## Usage

```text
/release-gate
```

## Sequence

1. Load `core/release-gates.md` and `workflows/production-release.md`.
2. Systematically evaluate each applicable release gate:
   - Gate 1: Scope & Requirements fulfillment
   - Gate 2: Repository integrity & dependency safety
   - Gate 3: Build, types, and lint verification
   - Gate 4: Functional behavior (routes, forms, CTAs, error states)
   - Gate 5: Responsive UX across mobile, tablet, and desktop
   - Gate 6: Accessibility (semantics, focus, labels, contrast)
   - Gate 7: Search (metadata, indexing, canonical, sitemap, schema)
   - Gate 8: Content truth (no fake claims or leaked placeholders)
   - Gate 9: Performance (images, fonts, bundles, caching)
   - Gate 10: Security & Privacy (no exposed secrets, safe input handling)
   - Gate 11: Testing & automated verification
   - Gate 12: Maintainability & clean documentation
   - Gate 13: Deployment readiness & environment variables
3. Output a formal release report using `templates/release-report.md`.
4. Conclude with an explicit, final status:
   - `PASS`
   - `PASS_WITH_NOTES`
   - `BLOCKED`
   - `FAIL`
