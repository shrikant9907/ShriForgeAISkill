# Release Gates

Apply gates proportionally. `RELEASE` workflows should evaluate all applicable gates.

## Gates

1. **Requirements** — requested scope is implemented; material assumptions are visible.
2. **Repository integrity** — no accidental destructive rewrites or unnecessary dependency churn.
3. **Build/static quality** — configured build/type/lint/static checks pass or failures are documented.
4. **Functional behavior** — routes, navigation, CTAs, forms, error/loading/empty states work where relevant.
5. **Responsive UX** — mobile/tablet/desktop and touch/overflow behavior reviewed.
6. **Accessibility** — semantics, keyboard, focus, labels, contrast, alt text, motion, reflow appropriate to scope.
7. **Search** — metadata, indexing, canonical, sitemap/robots, internal links, schema appropriate to site.
8. **Content truth** — no unsupported claims or leaked development placeholders.
9. **Performance** — images, fonts, JS, rendering, third parties, caching reviewed proportionally.
10. **Security/privacy** — secrets, input trust boundaries, errors, data collection, third parties reviewed.
11. **Testing** — appropriate automated/manual checks performed.
12. **Maintainability** — structure and documentation are understandable for future maintainers.
13. **Deployment** — env/config/domain/build/deployment instructions are sufficient for the requested release.

## Completion states

- `PASS` — applicable gates passed.
- `PASS_WITH_NOTES` — production-ready for requested scope with non-blocking limitations.
- `BLOCKED` — a required gate cannot be completed due to missing information/access/external dependency.
- `FAIL` — known blocking defects remain.

Never claim a gate passed if it was not actually checked.
