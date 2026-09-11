# Change Surface

Before non-trivial existing-project edits, map the areas that can regress.

Check whether the change affects:

- routes and navigation;
- shared components/layouts;
- data/content schemas;
- forms/actions/APIs;
- metadata/canonical/structured data;
- analytics or consent;
- accessibility semantics/focus;
- responsive layouts;
- tests and fixtures;
- environment variables;
- build/deployment;
- redirects and external links.

Validate the smallest affected surface first, then expand based on risk. Shared layout/navigation/data changes usually justify broader regression checks than isolated copy edits.
