# Astro Adapter

Use for Astro sites.

- Prefer static/server-rendered HTML by default.
- Hydrate islands only where interaction requires client JavaScript.
- Reuse Astro layouts/components/content collections when present.
- Keep metadata, canonical, sitemap, and content behavior aligned with the project's integrations.
- Avoid converting mostly-static pages into client-heavy React/Vue/Svelte islands without reason.
- Follow current official Astro guidance when adapter/integration APIs are uncertain.
