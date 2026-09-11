# SEO (Search Engine Optimization)

Make public pages crawlable, indexable, structurally coherent, and ranked for real user intent.

## The VATM 100-Point Quality Rubric

Grade search-critical pages against the four non-negotiable axes (25 points each):

```text
VALUE (25 pts)        Solves ONE intent better than competitors; BLUF answer first;
                      complete workflow, examples, edge cases, and 6–10 genuine FAQs.
ACCESS (25 pts)       HTTP 200; self-referencing canonical; server-rendered key content;
                      CWV green (LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1); clean URLs; valid schema.
TRUST (25 pts)        Real identity (About/Contact); verified facts (Project Truth); author byline;
                      HTTPS; clear privacy/terms; no fake reviews.
MEASUREMENT (25 pts)  Documented target query cluster; GSC baseline clicks/impressions/CTR;
                      conversion event tracked; 7/14/30-day review scheduled.
```

Target Score: **90–100** to ship; **75–89** fix gaps first; **< 75** not production-ready.

## Technical Fundamentals Checklist

1. **Title & Meta Description**:
   - Unique `<title>`: 50–60 characters. Primary promise + brand name.
   - Unique `<meta name="description">`: 120–160 characters. Clear summary with call to action.
2. **Canonical Integrity**:
   - Every page has an absolute, self-referencing `<link rel="canonical">` matching its final redirected URL.
   - Trailing slash policy must be consistent sitewide (enforce 301 redirects).
3. **Hierarchy & Structure**:
   - Exactly **one** `<h1>` per page reflecting main intent.
   - Logical `<h2>` and `<h3>` heading tree without skipping levels.
4. **Crawl & Discovery**:
   - Clean `robots.txt` allowing essential crawlers and blocking admin/private utility routes.
   - XML sitemap containing only HTTP 200, self-canonical, indexable URLs.
5. **Schema Markup**:
   - Server-rendered JSON-LD matching visible page content (`disciplines/structured-data.md`).

## Anti-Patterns to Reject

- **No Keyword Stuffing**: Keyword density is a myth. Focus on intent coverage and semantic depth.
- **No Thin Doorway Pages**: Consolidate minor keyword variants into one authoritative pillar page.
- **No Orphan Pages**: Every public page must receive at least 2–3 contextual internal links from indexed pages.
