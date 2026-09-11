# Astro Adapter

Use for Astro websites (Astro 4+ / 5).

## Detection

Look for `astro` in `package.json` and `astro.config.mjs` or `astro.config.ts`.

## Core Rules

- Prefer static/server-rendered HTML by default. Keep JavaScript at zero until user interactivity requires it.
- Hydrate UI components (React, Vue, Svelte) only with explicit client directives.
- Use Astro Content Collections with schemas for verified editorial content.
- Use `astro:assets` for automatic format conversion (WebP/AVIF) and layout shift prevention.

## Production Recipes

### 1. Selective Island Hydration

Never default to `client:load` unless an element is above-the-fold and critical:

```astro
---
import InteractiveSearch from '../components/InteractiveSearch.jsx';
import MobileMenuModal from '../components/MobileMenuModal.jsx';
import FooterNewsletter from '../components/FooterNewsletter.jsx';
---

<!-- Critical above-the-fold interactive component -->
<InteractiveSearch client:idle />

<!-- Opens only on user action -->
<MobileMenuModal client:media="(max-width: 768px)" />

<!-- Below-the-fold widget: hydrate only when scrolled into view -->
<FooterNewsletter client:visible />
```

### 2. Type-Safe Content Collection (`src/content/config.ts`)

```typescript
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string().max(70),
    description: z.string().min(50).max(160),
    publishDate: z.date(),
    author: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { blog };
```

### 3. SEO Head Partial (`src/components/BaseHead.astro`)

```astro
---
interface Props {
  title: string;
  description: string;
  image?: string;
  canonicalURL?: URL | string;
}

const { title, description, image = '/og-image.jpg', canonicalURL = Astro.url } = Astro.props;
---

<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="canonical" href={canonicalURL} />

<title>{title}</title>
<meta name="description" content={description} />

<!-- Open Graph -->
<meta property="og:type" content="website" />
<meta property="og:url" content={Astro.url} />
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
<meta property="og:image" content={new URL(image, Astro.url)} />
```
