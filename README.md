# legal-skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![GitHub Stars](https://img.shields.io/github/stars/chen-friedman/legal-skills?style=social)](https://github.com/chen-friedman/legal-skills) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### **Open-Source AI Agent Skills for Legal Professionals — Global Scope, Multilingual**

*Production-ready AI skills that work across Claude, Claude Code, OpenCode, Cursor, and 30+ other agent platforms*

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge&logo=apache&logoColor=white)](https://opensource.org/licenses/Apache-2.0)
[![Agent Skills Standard](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-purple?style=for-the-badge&logo=openstreetmap&logoColor=white)](https://agentskills.io)
[![Global Scope](https://img.shields.io/badge/Global-Multilingual-green?style=for-the-badge&logo=world&logoColor=white)](https://github.com/chen-friedman/legal-skills)

**[🇬🇧 English](./README.md) | [🇮🇱 עברית](./README_HE.md)**

---

## What Makes These Skills Special?

**Cross-Platform** → One skill works in Claude, Claude Code, OpenCode, Cursor, GitHub Copilot, OpenHands, Goose, Codex, and every other [agentskills.io](https://agentskills.io)-compatible tool
**Multilingual by Design** → 8 language packs at launch (English, Hebrew, Arabic, Russian, Spanish, French, German, Portuguese) — lazy-loaded, no wasted tokens
**Privacy-First** → Runs 100% locally. Automatic sensitive-data detection with masking. No telemetry, no external calls.
**Environment-Aware** → Adapts to whatever extraction tools are installed. Gracefully degrades when tools are missing.
**Practitioner-Built** → Designed by lawyers and legal technologists for real case workflows, not toy demos.

> **New to Agent Skills?** See the [Agent Skills overview](https://agentskills.io) and Anthropic's [skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices).

---

## Table of Contents

| **Navigation** | **Included** | **Use For** |
|---|---|---|
| [🎯 Available Skills](#-available-skills) | 1 skill | Current release |
| [🚀 Quick Start](#-quick-start) | Install & usage | Get running in 2 minutes |
| [🔍 mapping-legal-cases](#-mapping-legal-cases) | The flagship skill | Case folder analysis |
| [🌍 Language Packs](#-language-packs) | 8 languages | International coverage |
| [🔒 Privacy & Security](#-privacy--security) | Local-only | Sensitive document handling |
| [📦 Installation Per Platform](#-installation-per-platform) | Claude Code, OpenCode, Claude.ai, API | All major AI agents |
| [🗺️ Roadmap](#️-roadmap) | v1.1, v1.2, v1.3, v2.0 | Planned features |
| [🤝 Contributing](#-contributing) | Language packs, file handlers | Join the community |

---

## 🎯 Available Skills

| **Skill** | **What It Does** | **Status** |
|---|---|---|
| [mapping-legal-cases](./skills/mapping-legal-cases/) | Maps a folder of case documents into 10 cross-referenced analysis files (parties, timeline, claims, evidence, gaps, risks, deadlines, inventory, glossary, privacy flags) | ✅ v1.0 |
| drafting-legal-responses | Draft motions, responses, demand letters from `.casebase/` outputs | 📋 v1.4 roadmap |
| legal-research | Use CLAIMS.md + GLOSSARY.md to identify relevant case law | 📋 v1.4 roadmap |

---

## 🚀 Quick Start

### Claude Code (one command)

```bash
/plugin marketplace add chen-friedman/legal-skills
/plugin install legal-skills@chen-friedman
```

Then, in any case folder, simply ask:

```
Map this case folder
```

### OpenCode

```bash
git clone https://github.com/chen-friedman/legal-skills.git
# Copy or symlink skills/mapping-legal-cases to ~/.config/opencode/skills/
```

### Claude.ai (web)

1. Clone the repo
2. Zip the `skills/mapping-legal-cases/` folder
3. Upload in **Settings → Features → Skills**

### Any Other Agent Skills Platform

Clone the repo and point your tool at `skills/mapping-legal-cases/`. Works with [30+ compatible platforms](https://agentskills.io#clients).

**Verify your environment:**
```bash
python skills/mapping-legal-cases/scripts/extract.py --preflight --pretty
```

---

## 🔍 mapping-legal-cases

*The flagship skill. Point your AI at a folder of case documents — get a structured analysis brief.*

### What goes in

Any mix of:
- 📄 PDFs (native or scanned)
- 📝 Word documents (`.docx`, `.doc`, `.odt`, `.rtf`)
- 📊 Spreadsheets (`.xlsx`, `.xls`, `.csv`, `.tsv`)
- ✉️ Emails (`.eml`, `.msg`)
- 📑 Markdown, plain text, JSON, HTML
- 🖼️ Images (auto-OCR if tesseract installed)
- 🔊 Audio (auto-transcribe if whisper installed)
- 🎥 Video (auto-transcribe + metadata)

### What comes out

A `.casebase/` subfolder with **10 structured documents**, every finding cited back to its source:

| **Document** | **Contents** |
|---|---|
| `DOCUMENTS.md` | Full inventory with one-line summaries |
| `GLOSSARY.md` | Bilingual keyword index (which terms appear where) |
| `PRIVACY_FLAGS.md` | Sensitive data locations (**masked** values) |
| `PARTIES.md` | Who's who — client, opposing, judges, experts, witnesses |
| `TIMELINE.md` | Every date in chronological order with sources |
| `CLAIMS.md` | Legal arguments with basis, status, supporting evidence |
| `EVIDENCE.md` | Evidence cross-referenced to each claim |
| `GAPS.md` | Missing documents, contradictions, open questions |
| `RISKS.md` | Case weaknesses, opposing-favorable material |
| `DEADLINES.md` | Forward-looking dates with **OVERDUE** / **URGENT** flags |

Plus `MAPPING_LOG.md` — audit trail listing processed files and what still needs OCR/transcription.

### How it works

**Two-wave architecture** keeps token usage low:

**Wave 1** — extract every file once using `scripts/extract.py`, cache the text, build keyword index and privacy audit.

**Wave 2** — four parallel analysis tasks read from the cache to build the 10 outputs. On platforms with subagent support, these run in parallel for speed.

The extractor **auto-adapts** to whatever's installed:
- Baseline (zero installs): text, markdown, CSV, JSON, `.eml` emails, zip listings
- With Python packages: PDFs, Word, Excel, images, Outlook emails
- With CLI tools: pandoc (richer formats), tesseract (OCR), ffmpeg (media), whisper (transcription)
- Missing tools? Files are flagged `[PENDING OCR]` / `[PENDING TRANSCRIPTION]` — **never blocked**

### Example output

See [`skills/mapping-legal-cases/references/output-templates.md`](./skills/mapping-legal-cases/references/output-templates.md) for the exact structure of each of the 10 generated documents. Real end-to-end demo folder coming in v1.1 with proper PDFs, DOCX and emails.

---

## 🌍 Language Packs

Keyword packs are **lazy-loaded** based on detected document language — no tokens wasted on languages your case doesn't use.

| **Pack** | **Status** | **Coverage** |
|---|---|---|
| `common-en` (English) | ✅ baseline | Universal legal terms (always loaded) |
| `he` (Hebrew / עברית) 🇮🇱 | ✅ v1.0 | Israeli legal system |
| `ar` (Arabic / العربية) 🌍 | ✅ v1.0 | Modern Standard Arabic — general |
| `ru` (Russian / Русский) 🇷🇺 | ✅ v1.0 | Russian Federation + ex-Soviet |
| `es` (Spanish / Español) 🌍 | ✅ v1.0 | Spain + Latin America |
| `fr` (French / Français) 🌍 | ✅ v1.0 | France, Belgium, Switzerland, Quebec |
| `de` (German / Deutsch) 🌍 | ✅ v1.0 | Germany, Austria |
| `pt` (Portuguese / Português) 🌍 | ✅ v1.0 | Brazil + Portugal |
| `it`, `nl`, `pl`, `tr`, `zh`, `ja`, `ko`, `hi`, ... | 📋 roadmap | **Contribute yours!** See [CONTRIBUTING.md](./CONTRIBUTING.md) |

Each pack includes ~150 legal terms across 13 categories (dates, money, parties, procedures, courts, document types, criminal, family, property, labor, insurance, privacy patterns, filename signals) plus jurisdiction-specific privacy regex patterns.

---

## 🔒 Privacy & Security

- **Runs entirely locally.** No document content leaves your machine (unless you install an optional cloud backend).
- **Automatic sensitive-data scan.** National IDs, credit cards, bank accounts, medical record numbers, passport numbers, phone numbers — all detected and **masked** in `PRIVACY_FLAGS.md`.
- **Privacy patterns per jurisdiction**: US SSN/EIN, Israeli Teudat Zehut, Brazilian CPF/CNPJ, Spanish DNI/NIE, Mexican CURP/RFC, Argentine CUIT, Chilean RUT, German Steuer-ID, French NIR, Russian ИНН/СНИЛС, Portuguese NIF, and more.
- **Cache is local-only by default.** `.casebase/.cache/` contains raw extracted text — treat it like the original files.
- **No telemetry, no tracking, no external calls.** Audit `scripts/extract.py` yourself — one self-contained file.

See [SECURITY.md](./SECURITY.md) for vulnerability reporting.

---

## 📦 Installation Per Platform

<details>
<summary><b>Claude Code</b> (easiest — one command)</summary>

```bash
/plugin marketplace add chen-friedman/legal-skills
/plugin install legal-skills@chen-friedman
```

After install, just mention case mapping in any conversation.
</details>

<details>
<summary><b>OpenCode</b></summary>

```bash
git clone https://github.com/chen-friedman/legal-skills.git ~/legal-skills
# Option A: symlink
ln -s ~/legal-skills/skills/mapping-legal-cases ~/.config/opencode/skills/mapping-legal-cases

# Option B: copy
cp -r ~/legal-skills/skills/mapping-legal-cases ~/.config/opencode/skills/
```

On Windows PowerShell:
```powershell
New-Item -ItemType SymbolicLink -Path "$HOME\.config\opencode\skills\mapping-legal-cases" -Target "$HOME\legal-skills\skills\mapping-legal-cases"
```
</details>

<details>
<summary><b>Claude.ai (web app)</b></summary>

1. Download / clone the repo
2. Zip the `skills/mapping-legal-cases/` folder into `mapping-legal-cases.zip`
3. Open Claude.ai → Settings → Features → Skills → Upload custom skill
4. Upload your zip
</details>

<details>
<summary><b>Claude API</b></summary>

Use the [Skills API](https://docs.claude.com/en/api/skills-guide) to upload the skill. Required beta headers:
- `skills-2025-10-02`
- `code-execution-2025-08-25`
- `files-api-2025-04-14`
</details>

<details>
<summary><b>Cursor, GitHub Copilot, Gemini CLI, OpenHands, Goose, Codex, Kiro, Roo Code, and 20+ others</b></summary>

All support the [Agent Skills open standard](https://agentskills.io). Clone the repo, point your tool at `skills/mapping-legal-cases/`, and it'll work. See each tool's documentation for the exact skill directory path.
</details>

### Recommended Dependencies

The skill works with **zero dependencies** for plain text / CSV / JSON / Markdown / `.eml` emails. Install what you need for richer formats:

```bash
# Python packages (core)
pip install pymupdf pdfplumber python-docx openpyxl Pillow

# Optional — Outlook .msg support
pip install extract-msg

# Optional — audio/video transcription
pip install faster-whisper
```

External tools (OS-specific):

| Tool | Windows | macOS | Linux (Debian/Ubuntu) |
|---|---|---|---|
| pandoc (Word/ODT/RTF) | `winget install JohnMacFarlane.Pandoc` | `brew install pandoc` | `sudo apt install pandoc` |
| tesseract (OCR) | `winget install UB-Mannheim.TesseractOCR` | `brew install tesseract` | `sudo apt install tesseract-ocr` |
| ffmpeg (media metadata) | `winget install Gyan.FFmpeg` | `brew install ffmpeg` | `sudo apt install ffmpeg` |
| libreoffice (legacy `.doc`) | `winget install TheDocumentFoundation.LibreOffice` | `brew install libreoffice` | `sudo apt install libreoffice` |

**Run the preflight check any time:**
```bash
python skills/mapping-legal-cases/scripts/extract.py --preflight --pretty
```

---

## 🗺️ Roadmap

### v1.1 — More Languages + Better OCR
- Italian, Dutch, Polish, Turkish, Chinese, Japanese, Korean
- Built-in EasyOCR fallback
- Installation wizard

### v1.2 — Structured Extraction Upgrades
- Named-entity recognition (NER) for auto-detecting people, organizations, locations
- Table-aware parsing for financial tables and contract schedules
- Signature detection (signed vs. unsigned documents)
- Version grouping (v1, v2, final)
- Redaction detection

### v1.3 — Deeper Jurisdictional Knowledge
- Regional sub-packs (`en-us`, `en-uk`, `es-mx`, `fr-ca`, `de-at`, `de-ch`)
- Jurisdictional procedure packs (FRCP for US federal court, etc.)
- Case-number format library

### v1.4 — Workflow Integrations
- Companion skill: `drafting-legal-responses`
- Companion skill: `legal-research`
- Calendar integration (DEADLINES.md → iCal / Google Calendar)
- Redaction companion (auto-redact based on PRIVACY_FLAGS.md)

### v2.0 — Advanced Analysis
- Cross-case search
- Precedent detection
- Conflict-of-interest check
- Settlement valuation heuristics
- Multi-lingual corpus handling

Full details → [ROADMAP.md](./ROADMAP.md)

---

## 🤝 Contributing

Contributions are welcome — especially **new language packs**!

High-value contribution areas:
1. **Language packs** — Italian, Dutch, Polish, Turkish, Chinese, Japanese, Korean, Hindi, and more
2. **Regional sub-packs** — `es-mx`, `en-uk`, `fr-ca`, etc.
3. **New file type handlers** — `.numbers`, `.pages`, `.key`
4. **Real-world feedback** — from practicing lawyers across jurisdictions

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full guide.

---

## 📚 Related Projects

Check out [awesome-legaltech](https://github.com/chen-friedman/awesome-legaltech) — a curated list of open-source Legal AI & LegalTech tools, datasets, and communities.

Relevant building blocks used by this skill:
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) — PDF extraction
- [Pandoc](https://pandoc.org) — Universal document converter
- [Tesseract](https://github.com/tesseract-ocr/tesseract) — OCR engine
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) — Speech-to-text
- [Agent Skills standard](https://agentskills.io) — Cross-platform skill format

---

## 📄 License

Apache License 2.0. See [LICENSE](./LICENSE) and [NOTICE](./NOTICE).

**Commercial use allowed.** Fork it, modify it, ship it in your product — just keep the attribution notice.

---

## 👤 Author

**Chen Friedman** — founder, [Lawcal AI](https://lawcal.ai)
LegalTech / GovTech AI consultancy, Israel 🇮🇱

- GitHub: [@chen-friedman](https://github.com/chen-friedman)
- Also check out: [awesome-legaltech](https://github.com/chen-friedman/awesome-legaltech) — curated open-source legal tech

---

## 🌟 Support

If this helps you:
- ⭐ Star the repo
- 🐛 File issues for bugs or feature requests
- 🌐 Contribute a language pack for your jurisdiction
- 📢 Share with colleagues who could use it

**Questions?** Open a [discussion](https://github.com/chen-friedman/legal-skills/discussions) or see [SECURITY.md](./SECURITY.md) for vulnerability reporting.

---

*Built with ❤️ for legal professionals worldwide.*
