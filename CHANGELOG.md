# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
- Separate `README.md` (English) and `README_HE.md` (Hebrew) files, matching the structure of [awesome-legaltech](https://github.com/chen-friedman/awesome-legaltech).

## [1.0.0] - 2026-04-22

### Added
- Initial release of `mapping-legal-cases` skill
- Universal document extractor (`scripts/extract.py`) supporting:
  - PDF (PyMuPDF / pypdf / pdftotext fallback chain)
  - Word documents (pandoc / python-docx)
  - Excel (openpyxl)
  - Email (.eml stdlib, .msg via extract-msg)
  - Plain text, CSV, TSV, Markdown, JSON, HTML
  - Images with EXIF metadata (Pillow)
  - Audio / video metadata (ffprobe)
  - Automatic OCR via tesseract if installed
  - Automatic transcription via whisper / faster-whisper if installed
  - Graceful degradation — unsupported files flagged, never block the run
- Environment-aware preflight check (`--preflight`)
- Folder scanning mode (`--scan`)
- Persistent extraction cache (`.casebase/.cache/`)
- 10 output documents per case mapping:
  - DOCUMENTS.md — inventory
  - GLOSSARY.md — bilingual keyword index
  - PRIVACY_FLAGS.md — sensitive data locations (masked values)
  - PARTIES.md — people and entities
  - TIMELINE.md — chronological events
  - CLAIMS.md — legal arguments
  - EVIDENCE.md — evidence mapped to claims
  - GAPS.md — missing documents and contradictions
  - RISKS.md — case weaknesses
  - DEADLINES.md — forward-looking dates
- Plus MAPPING_LOG.md audit trail
- Keyword packs for 8 languages:
  - `common-en` (always loaded)
  - `he` (Hebrew) — Israeli legal system
  - `ar` (Arabic) — general Modern Standard Arabic legal terminology
  - `ru` (Russian) — Russian Federation legal system
  - `es` (Spanish) — Spain + Latin America (general)
  - `fr` (French) — France, Belgium, Switzerland, Quebec
  - `de` (German) — Germany, Austria
  - `pt` (Portuguese) — Brazil + Portugal
- Lazy loading of language packs based on detected corpus language (no wasted tokens)
- Apache 2.0 license
- Cross-platform compatibility (Windows, macOS, Linux)
- Compatible with all agentskills.io-compatible platforms (Claude Code, OpenCode, Cursor, GitHub Copilot, VS Code, Gemini CLI, OpenHands, Goose, Codex, Kiro, Roo Code, and others)
- Claude Code plugin marketplace manifest for one-command install
- Example case folder with expected outputs

### Security
- Sensitive data patterns (IDs, credit cards, bank accounts, medical records, phone numbers) automatically detected and masked in PRIVACY_FLAGS.md
- National ID patterns for multiple jurisdictions (US SSN/EIN, Israeli Teudat Zehut, Brazilian CPF/CNPJ, Spanish DNI/NIE, Mexican CURP/RFC, Argentine CUIT, Chilean RUT, German Steuer-ID, French NIR, Russian ИНН/СНИЛС, Portuguese NIF, and more)

## Roadmap

See `ROADMAP.md` for planned features in upcoming releases.
