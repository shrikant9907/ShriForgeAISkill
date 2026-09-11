# Frontend Engineering

Prefer maintainable semantic implementation.

Guidance:
- use platform semantics before custom ARIA;
- separate reusable components when repetition/behavior justifies it;
- keep page-specific composition readable rather than abstracting prematurely;
- keep data/content out of giant components when a clear model exists;
- minimize client-side state and JavaScript when static/server rendering suffices;
- handle interactive states intentionally;
- avoid dependency additions that duplicate platform/framework capability;
- follow the repository's formatter/linter/type conventions.

Do not enforce one state management, component library, or CSS architecture across all projects.
