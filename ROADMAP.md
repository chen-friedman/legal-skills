# Roadmap

Planned features for upcoming releases.

Contributions welcome — see `CONTRIBUTING.md`.

---

## v1.0 — Foundation (released)

**Goal:** Ship a working, cross-platform skill with the core 10-document mapping workflow and 8 language packs.

- ✅ Universal document extractor with graceful degradation
- ✅ 10 output documents (inventory, glossary, privacy, parties, timeline, claims, evidence, gaps, risks, deadlines)
- ✅ Persistent extraction cache
- ✅ Language packs: English, Hebrew, Arabic, Russian, Spanish, French, German, Portuguese
- ✅ Auto-detect OCR / transcription tools when installed
- ✅ Claude Code plugin manifest
- ✅ Apache 2.0 licensed
- ✅ Example case folder and demo outputs

---

## v1.1 — More languages + better OCR

**Goal:** Expand language coverage and make OCR more accessible.

- [ ] **Italian** (`it.md`) — Italian legal system
- [ ] **Dutch** (`nl.md`) — Netherlands + Belgium (Dutch-speaking)
- [ ] **Polish** (`pl.md`) — Polish legal system
- [ ] **Turkish** (`tr.md`) — Turkish legal system
- [ ] **Chinese Simplified** (`zh.md`) — mainland China
- [ ] **Chinese Traditional** (`zh-tw.md`) — Taiwan, Hong Kong
- [ ] **Japanese** (`ja.md`)
- [ ] **Korean** (`ko.md`)
- [ ] **Built-in EasyOCR fallback** — when tesseract isn't available
- [ ] **Installation wizard** — `python extract.py --install-suggest` that auto-generates install commands for missing deps

---

## v1.2 — Structured extraction upgrades

**Goal:** Extract more structured data from documents.

- [ ] **Named-entity recognition (NER)** — integrate spaCy or similar to auto-detect people, organizations, locations (configurable, off by default)
- [ ] **Table-aware parsing** — better handling of financial tables in PDFs, contract schedules
- [ ] **Signature detection** — flag signed vs. unsigned documents (via PyMuPDF annotation scan)
- [ ] **Version grouping** — auto-detect and group multiple versions of the same document (contract v1, v2, final)
- [ ] **Redaction detection** — flag documents that appear to have been redacted
- [ ] **Chain-of-custody tracking** — build `CUSTODY.md` showing document provenance

---

## v1.3 — Deeper jurisdictional knowledge

**Goal:** Region-specific sub-packs beyond language level.

- [ ] **`en-us.md`, `en-uk.md`, `en-au.md`, `en-ca.md`** — Anglo-American variants
- [ ] **`es-mx.md`, `es-ar.md`, `es-co.md`, `es-cl.md`** — Latin American variants
- [ ] **`fr-ca.md`** — Quebec civil law
- [ ] **`de-at.md`, `de-ch.md`** — Austria, Swiss German
- [ ] **Jurisdictional procedure packs** — region-specific deadline rules (e.g., FRCP for US federal court)
- [ ] **Common case-number format library** — recognize format per jurisdiction

---

## v1.4 — Workflow integrations

**Goal:** Make mapping-legal-cases the foundation for downstream legal workflows.

- [ ] **Companion skill: `drafting-legal-responses`** — uses `.casebase/` to draft motions, responses, demand letters
- [ ] **Companion skill: `legal-research`** — uses GLOSSARY + CLAIMS to identify relevant case law
- [ ] **Export to legal-case-management platforms** — Clio, MyCase, PracticePanther, LawRuler integrations
- [ ] **Calendar integration** — DEADLINES.md → iCal/Google Calendar
- [ ] **Redaction companion** — auto-generate redacted copies of documents based on PRIVACY_FLAGS.md

---

## v2.0 — Advanced analysis

**Goal:** AI-driven legal insights beyond simple extraction.

- [ ] **Cross-case search** — search across multiple `.casebase/` folders for patterns
- [ ] **Precedent detection** — compare current case to similar prior cases in a firm's corpus
- [ ] **Automatic conflict-of-interest check** — scan for party-name overlap across cases
- [ ] **Settlement valuation heuristics** — flag amounts in the corpus that could support settlement analysis
- [ ] **Multi-lingual corpus handling** — cases with documents in multiple languages (e.g., bilingual contracts)

---

## Community wishlist

Items suggested by users that may or may not fit into specific releases:

- [ ] Court-specific rule packs (e.g., Local Rules for SDNY, Eastern District of Texas)
- [ ] Integration with Practical Law / Westlaw / Lexis (where APIs permit)
- [ ] Mobile / tablet UI for reviewing `.casebase/` outputs
- [ ] Collaborative mode: merge `.casebase/` outputs across teammates' work
- [ ] Audit-trail cryptographic signing (for evidence provenance)

---

## How to influence the roadmap

1. **File an issue** describing the use case
2. **Upvote issues** that match your needs
3. **Submit a PR** for features you want to see (language packs especially welcome)
4. **Sponsor development** — commercial sponsorship for specific features is welcome (contact: hello@lawcal.ai)

This roadmap is a living document. Priorities shift based on user feedback and community contributions.
