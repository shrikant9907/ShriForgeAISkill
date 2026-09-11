# Next.js App Router Adapter

Use for projects using Next.js App Router (Next.js 13+ / 14 / 15).

## Detection

Look for `next` in `package.json` plus `app/` or `src/app/` structure.

## Core Rules

- Prefer Server Components by default; add `"use client"` only when browser state (`useState`), effects (`useEffect`), or event listeners (`onClick`) require it.
- Use framework metadata APIs for page/site metadata instead of manual `<head>` manipulation.
- Use route-level `loading.tsx`, `error.tsx`, and `not-found.tsx` boundaries.
- Keep secrets, private environment variables, and database connections strictly on the server.
- Validate Server Action inputs with schemas (e.g. Zod) before mutation.

## Production Recipes

### 1. Dynamic Sitemap (`app/sitemap.ts`)

```typescript
import { MetadataRoute } from 'next';

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://example.com';
  
  // Static routes
  const routes = ['', '/about', '/contact', '/services'].map((route) => ({
    url: `${baseUrl}${route}`,
    lastModified: new Date().toISOString(),
    changeFrequency: 'monthly' as const,
    priority: route === '' ? 1.0 : 0.8,
  }));

  return [...routes];
}
```

### 2. Crawl Directives (`app/robots.ts`)

```typescript
import { MetadataRoute } from 'next';

export default function robots(): MetadataRoute.Robots {
  const baseUrl = process.env.NEXT_PUBLIC_SITE_URL || 'https://example.com';
  return {
    rules: {
      userAgent: '*',
      allow: '/',
      disallow: ['/api/', '/admin/'],
    },
    sitemap: `${baseUrl}/sitemap.xml`,
  };
}
```

### 3. Safe Server Action Pattern

```typescript
'use server';

export type ActionState = {
  success: boolean;
  message?: string;
  errors?: Record<string, string[]>;
};

export async function submitInquiry(prevState: ActionState, formData: FormData): Promise<ActionState> {
  const name = formData.get('name')?.toString().trim();
  const email = formData.get('email')?.toString().trim();

  if (!name || !email) {
    return { success: false, message: 'Name and email are required fields.' };
  }

  try {
    // Process verified data on server boundary
    return { success: true, message: 'Inquiry received successfully.' };
  } catch (err) {
    return { success: false, message: 'An error occurred while processing your request.' };
  }
}
```

### 4. Performance-Safe Responsive Image

Always provide `sizes` on responsive `next/image` to prevent multi-megabyte image downloads on mobile:

```tsx
import Image from 'next/image';

export function HeroBanner({ src, alt }: { src: string; alt: string }) {
  return (
    <div className="relative w-full aspect-[16/9] overflow-hidden rounded-xl">
      <Image
        src={src}
        alt={alt}
        fill
        priority
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 80vw, 1200px"
        className="object-cover"
      />
    </div>
  );
}
```
