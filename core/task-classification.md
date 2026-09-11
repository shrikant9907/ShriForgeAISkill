# Task Classification

Choose one primary class before selecting modules.

| Class | Use when | Typical validation |
|---|---|---|
| `NEW_SITE` | Empty/minimal repository or explicitly new website | Full foundational + release-relevant gates |
| `EXISTING_SITE` | Broad multi-area work in an existing site | Repository integrity + regression checks |
| `FEATURE` | Add/change one route, section, component, form, integration | Changed-surface + cross-cutting checks |
| `REDESIGN` | Primary goal is visual/UX change | UX, responsive, a11y, performance |
| `BUG_FIX` | Existing behavior is wrong | Reproduce, root cause, regression test |
| `CONTENT_UPDATE` | Mostly factual/editorial content | Truth, links, search consistency |
| `SEO_SEARCH` | Crawlability, metadata, entities, local or AI-search work | Search/content/schema checks |
| `AUDIT` | Review/report is primary goal | Evidence-based findings, no invented pass claims |
| `MIGRATION` | Framework, CMS, routing, hosting, or architecture move | Inventory, parity, redirects, deployment |
| `RELEASE` | Launch/final verification | All applicable release gates |

If a request spans multiple classes, choose the class that best represents the main outcome and treat the others as supporting modules.

Do not escalate a tiny task into a broad workflow unless risk justifies it.
