# Security & Privacy

Apply security proportional to the site's capabilities and risk.

Always:
- keep secrets server-side/out of committed code;
- validate untrusted input at trust boundaries;
- encode/render user-controlled content safely;
- use safe error messages;
- review file uploads, redirects, HTML injection, and external URLs when present;
- minimize collected personal data;
- document required environment variables without values.

When relevant, also review authentication/authorization, CSRF, abuse/spam controls, rate limits, secure headers, cookie settings, third-party scripts, analytics/consent, and dependency vulnerabilities.

Do not mechanically add every security control to every static website; apply controls to actual attack surfaces.
