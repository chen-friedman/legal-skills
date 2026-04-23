# Security Policy

## Reporting a Vulnerability

Because this project is used with legal documents — which often contain sensitive PII, privileged material, and confidential information — we take security seriously.

If you discover a security vulnerability, **please do not open a public issue**. Instead:

1. Email: **security@lawcal.ai**
2. Include:
   - A description of the issue
   - Steps to reproduce (if applicable)
   - The version / commit affected
   - Your assessment of the severity

We will acknowledge receipt within 72 hours and work with you on a coordinated disclosure.

## What qualifies as a security issue

- **Data exfiltration risks** — any way the skill could send document content or extracted data to external services without user consent
- **PII leaks** — bugs that cause sensitive data to leak into logs, error messages, or output files that were intended to be sanitized
- **Privacy masking failures** — cases where PRIVACY_FLAGS.md fails to mask values that the skill's documentation claims it will mask
- **Path traversal** — ways the extractor could be tricked into reading files outside the case folder
- **Code execution vulnerabilities** — any input that could cause arbitrary code execution
- **Dependency vulnerabilities** — known CVEs in required libraries

## What does NOT qualify

- Feature requests for new privacy patterns (open a normal issue / PR)
- Extraction failures on specific files (open a normal issue)
- Keyword dictionary gaps (open a normal issue / PR)

## Supported Versions

Only the latest version receives security updates. If a vulnerability is disclosed, we will:
1. Release a fixed version ASAP
2. Post an advisory in GitHub Security Advisories
3. Note the CVE ID in `CHANGELOG.md`

## Privacy considerations for users

This skill runs **entirely locally** by default. It does not make network calls unless:
- The user explicitly chose to install an optional backend that uses remote APIs (e.g., a cloud transcription service). Any such choice is the user's.

The `.casebase/.cache/` folder contains full extracted text of your documents. Treat it with the same care you'd treat the original files. Our recommendation is to keep `.casebase/.cache/` local-only and never share it.

## Disclosure timeline

We aim for:
- 72 hours: acknowledge receipt
- 14 days: initial assessment and fix plan
- 90 days: fix released OR coordinated disclosure with researcher

For critical issues (active exploitation), we accelerate this timeline aggressively.
