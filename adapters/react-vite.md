# React + Vite Adapter

Use for React applications built with Vite.

- Follow existing router choice; do not introduce one for a single-page marketing site without need.
- Keep client state local unless shared/complex state justifies another layer.
- Treat SEO needs carefully: client-only rendering may not meet crawlability/performance requirements for content-heavy sites; follow project hosting/prerender/SSR strategy.
- Use Vite environment-variable conventions without exposing server secrets to client bundles.
- Prefer code splitting for genuinely separate interactive surfaces/routes.
- Use the project package manager/scripts for build and tests.
