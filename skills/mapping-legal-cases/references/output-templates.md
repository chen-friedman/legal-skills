# Output Document Templates

Exact structure for each of the 10 output documents produced in `.casebase/`. All templates follow these rules:

1. **Cite every claim** — every fact references a source file path: `file.pdf:p3` or `email.eml`
2. **Match corpus language** — write in the detected primary language (Hebrew, English, Arabic, etc.)
3. **Forward slashes in paths** — Unix-style, cross-platform
4. **Mask privacy values** — never quote full ID numbers, account numbers, etc. in outputs
5. **Include pending-extraction items** — tag with `[PENDING OCR]`, `[PENDING TRANSCRIPTION]`, `[PENDING VIDEO ANALYSIS]`

All templates below are shown in English. Translate section headers, dates, and structural text to match the corpus language.

---

## DOCUMENTS.md

```markdown
# Document Inventory

**Analysis Date:** [YYYY-MM-DD]
**Case folder:** [relative path]
**Total files:** [N]
**Primary language:** [en/he/ar/ru/es/fr/de/pt]

## Summary by Type

| Type | Count | Total Size |
|---|---|---|
| PDF | N | N MB |
| Word | N | N MB |
| Spreadsheet | N | N KB |
| Email | N | N KB |
| Markdown | N | N KB |
| Text | N | N KB |
| Image | N (all PENDING OCR) | N MB |
| Audio | N (all PENDING TRANSCRIPTION) | N MB |
| Video | N (all PENDING VIDEO ANALYSIS) | N MB |
| Other | N | N MB |

## Extracted Successfully

| File | Type | Size | Pages | Lang | One-line Summary |
|---|---|---|---|---|---|
| `path/file.pdf` | PDF | 245 KB | 12 | en | Statement of claim filed 2025-03-15 |
| ... |

## Pending Manual Extraction

### Needs OCR (N files)
- `scanned/court-notice.pdf` (1.2 MB, 3 pages, no text layer)
- `photos/document-photo.jpg` (340 KB, 2048x1536)

### Needs Transcription (N files)
- `recordings/witness-interview.mp3` (15 min)

### Needs Video Analysis (N files)
- `surveillance/incident-clip.mp4` (2 min 10 sec)

### Failed / Unsupported (N files)
- `archive.rar` — unsupported format
- `corrupted.pdf` — extraction failed

## File Tree

```
case-folder/
├── pleadings/
│   ├── statement-of-claim.pdf
│   └── response.pdf
├── evidence/
│   └── contracts/
│       └── lease.docx
└── correspondence/
    └── 2025-03-20-email.eml
```

---
*Inventory by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## GLOSSARY.md

```markdown
# Glossary & Keyword Index

**Analysis Date:** [YYYY-MM-DD]
**Primary language:** [en/he/ar/...]
**Keyword packs loaded:** common-en [+ he + ar + ...]
**Files indexed:** [N]

## Dates & Time
- **date / תאריך / fecha / дата** — in `file1.pdf:p2`, `email.eml`, ...
- **deadline / מועד / plazo / срок** — in `court-notice.pdf:p1`
- ...

**Explicit dates found ([N] total):**
- 2025-03-15 → `statement-of-claim.pdf:p1`, `email-002.eml`
- 2025-04-01 → `court-notice.pdf:p1`
- ...

## Money & Currency
- **$ / USD / dollar** — `contract.pdf:p4`
- **€ / EUR / euro** — `invoice-DE.pdf`
- **₪ / NIS / shekel** — `invoice-001.pdf`
- ...

**Amounts found (sorted):**
- $250,000 → `claim.pdf:p4`
- €45,678 → `invoice-001.pdf`
- ...

## Parties & Roles
- **plaintiff / תובע** — `statement-of-claim.pdf:p1`, ...
- **defendant / נתבע** — ...
- ...

## Legal Procedures
- ...

## Courts & Tribunals
- ...

## Document Types
- ...

## [Other categories as applicable]

## Auto-Detected Entities
Proper nouns / company names appearing 3+ times:
- **Example Corp Ltd.** — appears 14 times in 6 files
- **John Smith** — appears 9 times in 4 files
- **Hon. Judge Rodriguez** — appears 6 times in 3 files

## File-Name Signals
- Files with dates in name: `2025-03-15-complaint.pdf`, `hearing-2025-04-10.docx`
- Version markers: `contract-v2-final.docx`, `response-draft.docx`
- Case numbers in filenames: `12345-67-89.pdf`

---
*Glossary by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## PRIVACY_FLAGS.md

```markdown
# Privacy Flags

**Analysis Date:** [YYYY-MM-DD]
**⚠️ Review this document before sharing `.casebase/` folder.**

Sensitive personal data was detected in these locations. **Values are masked** — refer to source files for actual content.

## National ID Numbers
- `client-file.pdf:p1` — 1 ID masked (e.g., 123-**-****)
- `contract.docx:p3` — 2 IDs masked
- **Total: [N] IDs across [M] files**

## Credit Card Numbers
- `payment-records.pdf:p2` — 1 card (****-****-****-1234)

## Bank Accounts / IBAN
- `bank-statement-2025-01.pdf` — 1 account
- `invoice-047.pdf:p1` — 1 IBAN

## Passport Numbers
- `ID-docs/passport-scan.pdf` — 1 passport

## Medical Record Numbers
- `medical-report.pdf:p1` — 2 MRNs

## Phone Numbers
- `contact-list.xlsx` — [N] phones
- **Total: [N] across [M] files**

## Email Addresses
([N] unique addresses — tracked for PARTIES reference, not typically sensitive)

## Recommendations
1. **Before sharing `.casebase/`:** redact source files or share only analysis outputs.
2. **`.casebase/.cache/` contains full extracted text** including sensitive values — consider local-only storage.
3. **If sending `.casebase/` to a client:** PRIVACY_FLAGS.md itself is safe (masked). Other outputs may include names — review before sharing.

---
*Privacy scan by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## PARTIES.md

```markdown
# Parties & Entities

**Analysis Date:** [YYYY-MM-DD]
**Case:** [case name or number]
**Primary language:** [en/he/...]

## Primary Parties

### Plaintiff / Applicant
**[Full Name]** ([role title])
- First appearance: `statement-of-claim.pdf:p1`
- Represented by: [attorney name]
- Also in: `file1.pdf`, `file2.docx`

### Defendant / Respondent
**[Full Name]**
- First appearance: `statement-of-claim.pdf:p1`
- Represented by: [attorney]
- Also in: [list]

## Attorneys
**[Attorney Name]** — for [party]
- Firm: [firm]
- Contact: [masked if private]
- First appearance: `retainer.pdf:p1`

## Court / Tribunal
**[Court name]**
- Case number: [number]
- Judge: [name]
- First appearance: `court-notice.pdf:p1`

## Witnesses
**[Name]** ([fact witness / expert])
- First appearance: `affidavit-witness1.pdf:p1`
- Testimony about: [topic]
- Referenced in: [files]

## Experts
**[Name]** ([specialty])
- First appearance: `expert-opinion.pdf:p1`
- Conclusions (brief): [summary]

## Third Parties / Other Entities
**[Name]** ([role])
- First appearance: [file]
- Relevance: [why they matter]

## Organizations / Companies
**[Name]**
- Role: [e.g., insurer, employer]
- First appearance: [file]

## Relationships Map
- Plaintiff ↔ Defendant: [relationship]
- Plaintiff ← represented by → [Attorney]
- Defendant ← represented by → [Attorney]

---
*Parties by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## TIMELINE.md

```markdown
# Timeline

**Analysis Date:** [YYYY-MM-DD]
**Events indexed:** [N]
**Earliest:** [date]
**Latest:** [date]

## Chronological Events

### [YYYY-MM-DD] — [Event summary]
- **Source:** `file.pdf:p2`
- **Parties:** [names]
- **Details:** [brief]
- **Confidence:** explicit | inferred

### [YYYY-MM-DD] — Contract signed
- **Source:** `lease.docx:p1`
- **Parties:** Plaintiff, Defendant
- **Details:** 3-year lease at $5,000/month
- **Confidence:** explicit

### [YYYY-MM-DD] — Demand letter sent
- **Source:** `demand-letter.docx:p1`
- **Parties:** Plaintiff's attorney → Defendant
- **Confidence:** explicit

### [YYYY-MM-DD] — Statement of claim filed
- **Source:** `statement-of-claim.pdf:p1`
- **Confidence:** explicit

...

## Dates Mentioned but Unclear
- "about a year ago" — `affidavit.pdf:p2` — needs clarification
- "in recent months" — `letter.docx` — unclear

## Gaps in Timeline
- No documents between [date A] and [date B] — possible missing correspondence
- Hearing date mentioned but no protocol found

---
*Timeline by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## CLAIMS.md

```markdown
# Legal Claims

**Analysis Date:** [YYYY-MM-DD]
**Claims indexed:** [N]

## Plaintiff's Claims

### Claim C1: [Brief title]
- **Source:** `statement-of-claim.pdf:pX`
- **Legal basis:** [statute / contract clause / case law]
- **Relief sought:** [damages / injunction / etc.]
- **Supporting evidence:** E1, E3, E7 (see EVIDENCE.md)
- **Status:** supported | partially-supported | unsupported | unclear
- **Key facts alleged:**
  - [Fact 1] — per `source.pdf:pN`
  - [Fact 2] — per `source.pdf:pN`

### Claim C2: ...

## Defendant's Claims / Defenses

### Defense D1: [Brief title]
- **Source:** `response.pdf:pX`
- **Legal basis:** [if stated]
- **Supporting evidence:** E2, E5
- **Status:** [as above]
- **Key facts asserted:**
  - [Fact] — `source.pdf:pN`

### Defense D2: ...

## Counter-claims
(If any)

### Counter-claim CC1: ...

## Cross-Reference Matrix

| Claim | Supporting Evidence | Contradicting Evidence |
|---|---|---|
| C1 | E1, E3, E7 | E8 |
| C2 | E3, E4 | E6 |
| D1 | E2, E5 | E3 |

## Legal Authorities Cited
- **[Statute reference]** — in `statement-of-claim.pdf:p3`
- **[Case name]** — in `response.pdf:p4`

## Potentially Unstated Claims
Based on facts in the corpus, these claims may be available but not formally pleaded:
- [Possible claim] — evidence suggests [basis] in `file.pdf:pN`

---
*Claims analysis by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## EVIDENCE.md

```markdown
# Evidence

**Analysis Date:** [YYYY-MM-DD]
**Evidence items: [N]**

## Documentary Evidence

### E1 — [Document name]
- **Source:** `lease.docx` (full document)
- **Nature:** original contract
- **What it shows:** terms, parties, signatures, date
- **Supports:** Claim C1, C2
- **Undermines:** Defense D1
- **Authenticity:** signed / notarized / disputed

### E2 — ...

## Witness Evidence

### E3 — Affidavit of [Name]
- **Source:** `affidavit-witness1.pdf`
- **Nature:** sworn statement
- **Key points:**
  - [Point 1] — p2
  - [Point 2] — p3
- **Supports:** C1

## Expert Evidence

### E4 — Expert opinion: [Specialty]
- **Source:** `expert-opinion.pdf`
- **Expert:** [Name], [qualifications]
- **Opinion summary:** [conclusion]
- **Methodology:** [brief]
- **Supports:** [claims]

## Physical / Digital Evidence

### E5 — Photographs
- **Source:** `photos/` folder (17 images) [PENDING OCR]
- **Nature:** photographic
- **Relevance:** based on filenames/metadata

## Audio / Video Evidence

### E6 — Witness interview
- **Source:** `recordings/witness.mp3` [PENDING TRANSCRIPTION]
- **Duration:** 15 min
- **Relevance:** based on filename context

## Coverage Matrix

| Evidence | Claims Supported | Claims Undermined |
|---|---|---|
| E1 | C1, C2 | D1 |
| E2 | D1 | C1 |
| E3 | C1, C2 | — |

## Evidentiary Gaps
- **No direct evidence of:** [element] — would strengthen C1
- **Chain of custody unclear for:** [item]
- **Hearsay concerns:** [if any]
- **Authentication needed for:** [documents]

---
*Evidence analysis by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## GAPS.md

```markdown
# Gaps & Open Questions

**Analysis Date:** [YYYY-MM-DD]

## Missing Documents
Documents referenced in other files but not present:

- **[Document name]** — referenced in `email-2025-02-15.eml` as "the attached invoice"; not found.
- **Court filing receipt** — filed per `court-notice.pdf`, but the stamped copy isn't here.

## Contradictions Between Documents

### Contradiction 1: Date of incident
- `affidavit-witness1.pdf:p2` says **March 10, 2025**
- `incident-report.pdf:p1` says **March 12, 2025**
- Needs clarification

### Contradiction 2: Amount
- `demand-letter.docx:p3` demands **$180,000**
- `statement-of-claim.pdf:p4` claims **$250,000**
- Discrepancy needs explanation

## Unclear / Ambiguous Information
- "Several months ago" in `affidavit.pdf:p2` — specific date needed
- Unnamed third party in `email-2025-01-20.eml` as "the other guy" — identity needed

## Unanswered Factual Questions
- Who authorized the payment on [date]?
- What was the condition of the property when Defendant took possession?
- Did Plaintiff attempt to mitigate damages?

## Procedural Gaps
- **Filing receipts:** [N] filings referenced, [M] receipts found
- **Hearing protocols:** [N] hearings mentioned, [M] protocols found
- **Service of process:** no proof-of-service for [filing]

## Chain of Custody Concerns
- **[Evidence item]:** provenance unclear between [date A] and [date B]

## Pending Extraction (Critical Context Not Yet Available)
- `surveillance.mp4` [PENDING VIDEO ANALYSIS] — possibly shows incident
- `voicemail.mp3` [PENDING TRANSCRIPTION] — possibly from opposing party
- `scanned-contract.pdf` [PENDING OCR] — appears to be the original agreement

## Recommended Follow-ups (prioritized)
1. **HIGH:** Obtain the invoice referenced in `email-2025-02-15.eml`
2. **HIGH:** Resolve date contradiction
3. **MEDIUM:** OCR `scanned-contract.pdf`
4. **MEDIUM:** Transcribe `witness-interview.mp3`
5. **LOW:** Clarify "several months ago" reference

---
*Gaps analysis by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## RISKS.md

```markdown
# Risks & Weaknesses

**Analysis Date:** [YYYY-MM-DD]

This catalogs vulnerabilities — content in the corpus that weakens the case or helps the opposing side.

## Case Weaknesses

### W1: [Description]
- **Nature:** legal / factual / procedural / evidentiary
- **Source:** `file.pdf:pN`
- **Problem:** [why this weakens]
- **Exposure:** how opposing side may use it
- **Mitigation:** [recommended strategy]

### W2: Delayed response to demand letter
- **Nature:** procedural
- **Source:** `demand-letter.docx` (2024-12-15); `response.pdf` (2025-02-20)
- **Problem:** 67-day delay could suggest acquiescence
- **Exposure:** waiver / laches argument
- **Mitigation:** document reason for delay

## Unfavorable Facts in Own Corpus
Facts in our own files that hurt us:
- **[Fact]** — per `our-client-email.eml` — our client acknowledged [damaging admission]
- **[Fact]** — per `internal-memo.docx` — suggests [unfavorable inference]

## Documents Helpful to Opposing Side
If opposing side accesses these in discovery:
- `email-2024-11-05.eml` — contains our client's admission
- `internal-note.docx` — contradicts current legal theory

## Weak Legal Arguments
Arguments thin on support:
- **Claim C3:** no evidence of [element] in corpus — consider dropping
- **Damages calculation in `claim.pdf:p4`:** inflated vs. actuals in `bank-statements/`

## Procedural Risks
- **Statute of limitations:** [date] — close to / past limit
- **Jurisdiction:** potential challenge based on [factor]
- **Standing:** [issues]

## Credibility Risks
- **Witness [name]:** inconsistent statement in `email-2024-09.eml` vs affidavit
- **Client's prior filings:** [if relevant]

## Opposing Side's Strongest Points
Anticipating opposing arguments based on corpus:
1. **[Argument]** — supported by [evidence in our corpus]
2. ...

## Risk-Reduction Recommendations (prioritized)
1. **URGENT:** Address W2 (delay) before [deadline]
2. **HIGH:** Prepare response to anticipated argument [X]
3. **MEDIUM:** Consider dropping Claim C3

---
*Risk analysis by mapping-legal-cases on [YYYY-MM-DD]*
```

---

## DEADLINES.md

```markdown
# Deadlines

**Analysis Date:** [YYYY-MM-DD]
**Today:** [YYYY-MM-DD]

## 🚨 OVERDUE

### [YYYY-MM-DD] — [Description] (X days overdue)
- **Source:** `court-notice.pdf:p1`
- **Context:** [brief]
- **Action required:** motion for extension?

## ⚠️ URGENT (within 14 days)

### [YYYY-MM-DD] — [Description] (X days away)
- **Source:** `filing-notice.pdf:p2`
- **Context:** [brief]
- **Action required:** [action]

## Upcoming

### [YYYY-MM-DD] — First hearing
- **Source:** `court-notice.pdf:p1`
- **Court:** [name]
- **Case #:** [number]
- **Preparation:** [brief]

### [YYYY-MM-DD] — Filing deadline for [document]
- **Source:** `court-order.pdf:p3`
- **Statutory basis:** [if any]

## Statutes of Limitations

### [Claim type] — expires [date] (X days remaining)
- **Basis:** [statute reference]
- **Trigger date:** [when clock started]
- **Source:** derived from `incident-report.pdf:p1`

## Long-term / Open-ended

### [YYYY-MM-DD] — Contract renewal date
### [YYYY-MM-DD] — Next significant date

## Ambiguous Forward-Looking References
- "in the near future" — `email.eml` — needs clarification
- "upon completion of work" — `contract.docx:p4` — trigger unclear

## Response Windows (verify applicable jurisdiction)
- Statement of defense: 30 days from service (generic civil procedure)
- Appeal: [X] days from judgment
- Motion for reconsideration: [X] days

---
*Deadlines tracker by mapping-legal-cases on [YYYY-MM-DD]*

**IMPORTANT:** Verify all deadlines against court records. This tool assists tracking but is not a substitute for professional calendaring.
```

---

## MAPPING_LOG.md (orchestrator audit trail)

```markdown
# Mapping Log

**Run:** [ISO timestamp]
**Case folder:** [path]
**Files scanned:** [N]
**Files extracted successfully:** [N]
**Files needing manual extraction:** [N]

## Pending Manual Extraction

### OCR Required ([count])
- `scanned/file.pdf`
- `photos/img.jpg`

### Transcription Required ([count])
- `recordings/witness.mp3`

### Video Analysis Required ([count])
- `surveillance/clip.mp4`

### Unsupported / Failed ([count])
- `archive.rar` — unsupported
- `corrupted.pdf` — extraction failed

## Warnings Summary
Aggregate warnings from cache JSONs, grouped by type.

## Documents Generated
| Document | Lines | Size |
|---|---|---|
| DOCUMENTS.md | N | N KB |
| GLOSSARY.md | N | N KB |
| ... | | |

## Environment
**Python:** [version]
**Capabilities:**
- PDF text: ✅ PyMuPDF
- Word: ✅ pandoc
- Excel: ✅ openpyxl
- OCR: ❌ (install tesseract)
- Transcription: ❌ (pip install faster-whisper)

## Next Steps
- Run OCR tool on pending files, then re-run `/legal/map-case`
- Run transcription on audio, then re-run
- Review PRIVACY_FLAGS.md before sharing

---
```
