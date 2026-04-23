# Agent Instructions — legal-skills repo

This file gives OpenCode / Claude Code / Cursor / other agents context about this repository.

## Project overview

This is an **open-source Agent Skills repository** for legal professionals. It ships one skill in v1.0:

- `skills/mapping-legal-cases/` — maps a folder of case documents into 10 structured analysis files

The skill follows the [agentskills.io](https://agentskills.io) open standard and works across 30+ AI platforms.

## When developing in this repo

### Priority: ship fast, accept contributions, don't over-engineer

This is a community-driven OSS project. Keep changes focused, documented, and backwards-compatible.

### Never commit real legal data

All examples, fixtures, tests must be fictional/synthetic. Never commit real PII, client data, or real case documents.

### Changes to SKILL.md require care

Any change to `skills/mapping-legal-cases/SKILL.md` changes behavior for all downstream users. Test thoroughly and update the CHANGELOG under `[Unreleased]`.

### Testing

```bash
pytest tests/ -v
python skills/mapping-legal-cases/scripts/extract.py --preflight --pretty
python skills/mapping-legal-cases/scripts/extract.py --scan examples/sample-case-folder --pretty
```

### When adding a new language pack

1. Copy the structure of `skills/mapping-legal-cases/references/keywords/common-en.md`
2. Save as `<lang>.md` using ISO 639-1 language code
3. Include privacy-pattern regex for jurisdiction-specific IDs
4. Update SKILL.md's language-pack loading list
5. Update README.md and README_HE.md language tables
6. Update CHANGELOG.md

### When modifying extract.py

1. Preserve the JSON output schema (breaking changes = major version bump)
2. Maintain graceful degradation — missing tools should never crash the run
3. Add a smoke test in tests/test_extract.py
4. Run CI locally: `pytest tests/ -v`

### File layout conventions

```
legal-skills/
├── README.md / README_HE.md              ← language-specific READMEs
├── skills/<skill-name>/SKILL.md           ← follows agentskills.io spec
├── skills/<skill-name>/scripts/           ← executable helpers
├── skills/<skill-name>/references/        ← loaded on demand by agents
├── skills/<skill-name>/assets/            ← illustrative samples
├── examples/sample-case-folder/           ← demo input
├── tests/                                 ← pytest tests
└── .github/workflows/                     ← CI
```

## Authoring style

- English primary language for code, comments, docs
- Hebrew translation of user-facing README maintained in `README_HE.md`
- Forward slashes in all file paths (Unix-style, works everywhere)
- Follow Anthropic's [skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
  - Third-person descriptions
  - Front-load the key use case
  - SKILL.md body under 500 lines
  - Progressive disclosure via `references/`

## Author

Chen Friedman / Lawcal AI — see [LICENSE](./LICENSE), [NOTICE](./NOTICE).
