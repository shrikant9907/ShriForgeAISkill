# Visual Design

Create a deliberate, premium visual identity tailored to the organization and audience. Prevent generic "AI slop" (indiscriminate purple gradients, gray-on-gray low contrast, and uninspired layouts) by using structured design tokens.

## Design Token Vault

### 1. Curated Typography Pairings

Never rely on generic browser sans-serifs or unstyled Inter defaults. Use purpose-matched Google Fonts:

| Archetype | Display / Heading Font | Body / UI Font | Best For |
|---|---|---|---|
| **Modern Tech** | `Space Grotesk` or `Syne` | `Plus Jakarta Sans` or `Inter` | SaaS, Developer tools, AI platforms |
| **Editorial Luxury** | `Playfair Display` or `Fraunces` | `Outfit` or `Manrope` | High-end retail, Portfolios, Architecture |
| **Clean Institutional** | `Instrument Sans` or `Cabinet Grotesk` | `Inter` or `Geist` | Schools, Clinics, Enterprise B2B |
| **Warm Editorial** | `Newsreader` or `Lora` | `Work Sans` or `DM Sans` | Blogs, Storytelling, Publishing |

```html
<!-- Example import for Modern Tech -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
```

### 2. Semantic Color Systems

Always define colors through semantic CSS variables with guaranteed WCAG AA contrast (≥ 4.5:1 for body text):

```css
:root {
  /* Slate / Modern Tech Palette */
  --bg-canvas: #090a0f;
  --bg-surface: #13151f;
  --bg-surface-elevated: #1c1f2e;
  --text-primary: #f1f3f9;
  --text-muted: #9ba1b5;
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(255, 255, 255, 0.16);
  --accent-primary: #4f46e5;
  --accent-hover: #6366f1;
  --accent-glow: rgba(99, 102, 241, 0.15);
}
```

### 3. Layout & Touch Accessibility (Anti-Slop Rules)

- **Touch Targets**: All interactive elements (buttons, nav links, form inputs) must have a minimum clickable/tappable area of **44×44px** on mobile.
- **Spacing Scale**: Base layout rhythm on an 8pt scale (`8px`, `16px`, `24px`, `32px`, `48px`, `64px`).
- **Surface Elevation**: Layer depth with subtle borders (`1px solid var(--border-subtle)`) and ambient backdrop blurs rather than heavy drop shadows.
- **Micro-Interactions**: Use context-aware easing (`cubic-bezier(0.16, 1, 0.3, 1)`) with transitions between `150ms` and `250ms`. Never animate layout dimensions (`width`/`height`) that cause layout thrashing.
- **Motion Accessibility**: Always wrap keyframe and transform animations in `@media (prefers-reduced-motion: reduce)`.
