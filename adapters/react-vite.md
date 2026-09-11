# React + Vite Adapter

Use for React Single Page Applications (SPAs) built with Vite.

## Detection

Look for `vite` and `react` in `package.json` with a `vite.config.ts` or `vite.config.js`.

## Core Rules

- **Crawlability Alert**: Client-only SPAs render empty HTML shells (`<div id="root"></div>`). For content-heavy or public search-critical sites, consider SSR (Next.js/Astro) or static prerendering.
- Keep client state local to components unless shared state justifies a context or store.
- Never expose server secrets or private keys in Vite. Only variables prefixed with `VITE_` are bundled to the client.
- Always configure server routing fallbacks (`/index.html`) on deployment targets (Vercel, Netlify, Cloudflare, Nginx) so deep links do not return 404.

## Production Recipes

### 1. Route Code-Splitting with Suspense

Prevent initial bundle bloat by lazy-loading separate pages:

```tsx
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

const HomePage = lazy(() => import('./pages/HomePage'));
const AboutPage = lazy(() => import('./pages/AboutPage'));
const ContactPage = lazy(() => import('./pages/ContactPage'));

export function AppRouter() {
  return (
    <BrowserRouter>
      <Suspense fallback={<div className="p-8 text-center">Loading page...</div>}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/contact" element={<ContactPage />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

### 2. Environment Variable Validation (`src/config/env.ts`)

```typescript
export const config = {
  siteUrl: import.meta.env.VITE_SITE_URL || 'http://localhost:5173',
  apiEndpoint: import.meta.env.VITE_API_ENDPOINT || '/api',
  isProduction: import.meta.env.PROD,
};

// Fail fast in development if critical configuration is missing
if (!config.apiEndpoint) {
  console.warn('Warning: VITE_API_ENDPOINT is not configured.');
}
```

### 3. SPA Route Fallback Config

For static hosting, ensure single-page routing rewrites all requests to `index.html`.

- **Vercel (`vercel.json`)**:
```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```
- **Netlify (`public/_redirects`)**:
```text
/*    /index.html   200
```
