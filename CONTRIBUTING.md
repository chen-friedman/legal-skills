# Contributing to legal-skills

Thank you for your interest! This project welcomes contributions from lawyers, developers, legal technologists, translators, and anyone who wants to help build better AI tooling for legal professionals worldwide.

## Ways to contribute

### 1. Submit a jurisdiction / language pack ⭐ (most wanted)

The skill currently ships with packs for: `common-en`, `he`, `ar`, `ru`, `es`, `fr`, `de`, `pt`.

**Most valuable contributions are additional language packs or jurisdiction-specific sub-packs**, for example:
- Italian (`it.md`), Dutch (`nl.md`), Polish (`pl.md`), Turkish (`tr.md`), Chinese (`zh.md`), Japanese (`ja.md`), Korean (`ko.md`), Hindi (`hi.md`), Indonesian (`id.md`), Vietnamese (`vi.md`)
- Regional legal-system variations (e.g. `es-mx.md` for Mexico-specific terms, `en-us.md` or `en-uk.md` for US vs. UK terminology)

**How:**
1. Copy `skills/mapping-legal-cases/references/keywords/common-en.md` as a template structure
2. Create a new file `skills/mapping-legal-cases/references/keywords/<lang>.md`
3. Fill in the 13 sections with legal terms in your target language
4. Include privacy patterns specific to that jurisdiction (national ID formats, tax IDs, bank account formats)
5. Open a PR using the "Jurisdiction pack" issue template

Aim for ~150 terms across the core categories. Quality over quantity — prescriptive terms used by lawyers in that jurisdiction are better than a dictionary dump.

### 2. Improve the extractor

`scripts/extract.py` handles document extraction. Improvements we welcome:
- New file type support (e.g., `.numbers`, `.pages`, `.key`)
- Better OCR integration (EasyOCR, PaddleOCR, Google Vision)
- Better transcription (Deepgram, AssemblyAI, local models)
- Encoding detection improvements
- Performance optimization for large folders

Requirements:
- Maintain graceful degradation — if an optional tool isn't installed, the file should still be noted, not fail the whole run
- Keep the JSON output schema stable (breaking changes require a major version bump)
- Add a test case in `tests/` for any new handler

### 3. Refine output templates

The 10 output documents (DOCUMENTS, GLOSSARY, PRIVACY_FLAGS, PARTIES, TIMELINE, CLAIMS, EVIDENCE, GAPS, RISKS, DEADLINES) are defined in `skills/mapping-legal-cases/references/output-templates.md`.

If you're a practicing lawyer and see a way to make these more actionable, open an issue to discuss.

### 4. Share real-world usage feedback

File issues for:
- False positives / negatives in keyword detection
- Extraction failures on common document types
- Missing categories in output templates
- Jurisdiction-specific needs

### 5. Improve documentation

- Translate `README.md` into additional languages (beyond the initial English + Hebrew)
- Add platform-specific installation guides
- Add example case folders (anonymized!) to help new users

### 6. Spread the word

If this tool helps you, please:
- Star the repo
- Share with colleagues
- Write a blog post / tutorial (we'll link back)

## Development setup

```bash
git clone https://github.com/<your-fork>/legal-skills
cd legal-skills

# Verify Python environment
python skills/mapping-legal-cases/scripts/extract.py --preflight --pretty

# Run extract.py tests
pytest tests/ -v
```

## Pull request guidelines

- One change per PR (easier to review and revert)
- For new language packs: if you want to add tests, generate fictional fixtures at runtime in `tests/` — never commit real case files
- Keep commits focused; squash if the PR has many fix-up commits
- Update `CHANGELOG.md` in the `[Unreleased]` section

## Privacy & anonymization ⚠️

**Never commit real legal documents, real client data, or real PII** to this repository.

All examples, fixtures, and test files must be:
- Fictional / fabricated, or
- Synthetically generated, or
- Public domain legal documents

If you're testing with real client files, keep them outside the repo. Add a `.gitignore` entry if necessary.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## Licensing

By contributing, you agree that your contributions will be licensed under the Apache License 2.0 (see `LICENSE`).

If you contribute a jurisdiction pack, you retain copyright over the specific content you added, but grant Apache 2.0 license terms to the project.

## Contact

- Issues: https://github.com/chen-friedman/legal-skills/issues
- Author: Chen Friedman / Lawcal AI (https://lawcal.ai)
