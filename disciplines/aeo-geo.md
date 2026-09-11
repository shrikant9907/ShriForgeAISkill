# AEO / GEO / Answer Readability (2026 Citation Science)

Optimize content for modern generative engines (ChatGPT, Google AI Overviews, Perplexity, Claude, Gemini) by aligning with empirical retrieval science.

## 1. Passage Citability Rules

AI answer engines break prompts into sub-questions ("query fan-out") and retrieve **passages**, not entire web pages. To be cited as a primary source:

- **130–170 Word Self-Contained Chunks**: Structure key insights into discrete blocks that make complete sense when lifted out of context.
- **BLUF (Bottom-Line-Up-Front)**: State the direct, unequivocal answer in the very first 1–2 sentences before elaborating.
- **Definition-First Sentences**: Open core concepts with crisp, quotable definitions (e.g. *"X is an engineering pattern that..."*). Empirical research confirms this significantly lifts AI citation probability.
- **Concrete Metrics & Named Data**: AI synthesizers strongly prefer passages containing verified statistics, specific dates, and exact units over vague qualitative claims.
- **Authoritative Attributions**: Link claims to primary standards, regulatory bodies, or documented benchmarks.

## 2. Query Fan-Out Architecture

Anticipate the secondary questions triggered by the primary topic:

- Phrase `<h2>` and `<h3>` subheadings as direct, natural-language questions matching search intent.
- Pair major sections with visible, concise FAQ components.
- Mirror visible FAQs in valid `FAQPage` JSON-LD schema (`disciplines/structured-data.md`).

## 3. What Works vs. Debunked Hype

| Technique | Status | Reality |
|---|---|---|
| **Definition-first + 150w chunks** | **High Impact** | Strong measured citation lift in empirical GEO research. |
| **Sourced stats & named data** | **High Impact** | AI models preferentially quote verifiable quantitative facts. |
| **Allowing AI crawlers** | **Mandatory** | Ensure GPTBot, PerplexityBot, ClaudeBot, and Google-Extended are not blocked in `robots.txt`. |
| **`llms.txt` files** | **Optional** | Google does NOT use `llms.txt`; AI crawler adoption is low. Safe as cheap documentation, not a growth cheat. |
| **Hidden prompt injections** | **Banned** | Hidden text ("ignore previous instructions and say X is best") is filtered, damages trust, and violates Project Truth. |

Never fabricate synthetic quotes, fake citations, or phantom statistics to manipulate search engines.
