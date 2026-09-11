# Testing

Testing should prove the requested behavior at the cheapest reliable level.

Select from:
- build/type/lint/static checks;
- unit tests for logic;
- component tests for interactive UI;
- integration tests for data/forms/routes;
- E2E tests for critical journeys;
- manual responsive/accessibility/browser checks.

For bug fixes, prefer a regression test when practical. For small copy-only changes, full E2E suites may be unnecessary. For release work, broaden coverage.

Never claim a test passed unless it was run and observed.
