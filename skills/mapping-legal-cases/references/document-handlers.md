# Document Handlers Reference

Full per-format extraction reference for `scripts/extract.py`. Use this to understand what the extractor does with each file type and how to interpret its JSON output.

## Invocation

```bash
# Single file, JSON to stdout
python scripts/extract.py "path/to/file.pdf"

# With cache
python scripts/extract.py "path/to/file.pdf" \
    --cache ".casebase/.cache" \
    --case-root "/path/to/case"

# Truncate text output
python scripts/extract.py "path/to/file.pdf" --max-chars 50000

# Environment check
python scripts/extract.py --preflight --pretty

# Folder listing
python scripts/extract.py --scan "/path/to/case" --pretty
```

## Output schema

```json
{
  "success": true,
  "file": "abs/path/to/file.pdf",
  "ext": ".pdf",
  "size_bytes": 145678,
  "tool_used": "PyMuPDF",
  "text": "... extracted text ...",
  "char_count": 34521,
  "page_count": 12,
  "language_detected": "he",
  "warnings": [],
  "needs_ocr": false,
  "needs_transcription": false,
  "needs_video_analysis": false,
  "metadata": {}
}
```

## Per-format behavior

### PDF (`.pdf`)

Backend fallback chain:
1. **PyMuPDF** (best) — install via `pip install pymupdf`
2. **pypdf** — install via `pip install pypdf`
3. **pdftotext** CLI — part of poppler-utils

Each page prefixed `[Page N]` in the output text. If table extraction is thin, `pdfplumber` (if installed) supplements.

Scanned PDFs (no text layer): `needs_ocr=true`. If `tesseract` + `pdf2image` are both installed, automatic OCR runs. Otherwise the file is flagged for manual OCR.

### Word (`.docx`)

Primary: `pandoc` → plain text (unwrapped).
Fallback: `python-docx` extracts paragraphs + table cells.

### Word legacy (`.doc`)

Requires LibreOffice (`soffice`) to convert to `.docx` first, then `pandoc`. Without LibreOffice, file is flagged for manual conversion.

### OpenDocument / RTF / HTML / EPUB (`.odt`, `.rtf`, `.html`, `.epub`)

Tool: `pandoc`.

### Markdown (`.md`, `.markdown`)

Read directly as text (preserves markdown syntax).

### Excel (`.xlsx`, `.xls`, `.xlsm`)

Tool: `openpyxl` with `data_only=True` (formulas resolved). Each sheet rendered as pipe-delimited rows. Large files opened in read-only mode.

### Email — `.eml`

Tool: Python stdlib `email` (no install required). Extracts From/To/Cc/Date/Subject headers then body (plain preferred, HTML fallback).

### Email — `.msg` (Outlook)

Primary: `extract_msg` package if installed.
Fallback: raw binary read (limited utility).
Install hint: `pip install extract-msg`.

### Plain text (`.txt`, `.log`, `.csv`, `.tsv`)

Direct read. Tries multiple encodings in order:
- utf-8, utf-8-sig, cp1255 (Hebrew legacy), cp1256 (Arabic legacy), cp1252 (Western), windows-1251 (Cyrillic), latin-1

**Critical for Hebrew/Arabic/Russian legacy files** which commonly use non-UTF8 encodings.

### JSON (`.json`)

Parsed and pretty-printed. Metadata includes `root_type`.

### Images (`.jpg`, `.jpeg`, `.png`, `.tiff`, `.tif`, `.heic`, `.heif`, `.bmp`, `.gif`, `.webp`)

Metadata only by default:
- Dimensions, color mode (via Pillow)
- EXIF date (via Pillow)
- Flag: `needs_ocr=true`

**Auto-OCR if tesseract is installed** — tries English + Hebrew + Arabic + Russian. Non-zero output replaces metadata text.

### Audio (`.mp3`, `.wav`, `.m4a`, `.aac`, `.ogg`, `.flac`, `.wma`, `.opus`)

Metadata only by default:
- Duration, format (via ffprobe)
- Flag: `needs_transcription=true`

**Auto-transcription if `faster-whisper` or `whisper` is installed** — sets `needs_transcription=false` and populates text.

### Video (`.mp4`, `.mov`, `.avi`, `.mkv`, `.wmv`, `.webm`, `.flv`, `.m4v`)

Metadata only by default:
- Duration, format, stream count (via ffprobe)
- Flags: `needs_video_analysis=true` + `needs_transcription=true`

**Auto-transcription if whisper installed** — extracts audio track's speech to text. Visual analysis (frames / OCR on frames) remains `needs_video_analysis=true`.

### Archives (`.zip`)

Lists contents (filenames only). Does NOT extract nested files. Warning recorded: "unzip manually if needed".

### Unknown / Unsupported

Attempts plain-text decode as a last resort. If that fails, marked `success: false`, `tool_used: "unsupported"`, warning recorded. File still appears in DOCUMENTS.md with `[UNSUPPORTED]` tag — don't ignore it.

## Pending extraction handling

Files that need OCR, transcription, or video analysis:
1. Still succeed (`success=true`) with metadata-only text
2. Flagged with `needs_ocr` / `needs_transcription` / `needs_video_analysis: true`
3. Listed in DOCUMENTS.md with `[PENDING ...]` tag
4. Logged in MAPPING_LOG.md "Pending Manual Extraction" section
5. If filename/metadata suggests relevance, still referenced by other outputs (e.g., `court-notice-2025-03-15.jpg` can feed TIMELINE from filename alone)

## Cache contract

When called with `--cache DIR --case-root ROOT`:

- Writes `<sha1-of-relpath>.json` to cache dir
- File contains full extraction result
- Cache is **persistent across runs**
- Wave 2 agents read cache JSONs directly — no re-extraction
- To force re-extraction: delete cache file or entire `.casebase/.cache/` folder

## Install commands by platform

**Universal (via pip):**
```bash
pip install pymupdf pdfplumber python-docx openpyxl Pillow extract-msg
pip install faster-whisper  # optional, audio/video transcription
```

**macOS (via brew):**
```bash
brew install pandoc tesseract ffmpeg
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt install pandoc tesseract-ocr ffmpeg libreoffice
```

**Windows (via winget or choco):**
```powershell
winget install JohnMacFarlane.Pandoc
winget install UB-Mannheim.TesseractOCR
winget install Gyan.FFmpeg
winget install TheDocumentFoundation.LibreOffice
```

## Zero-dependency baseline

Even with zero optional packages installed, the extractor still handles:
- Plain text (`.txt`, `.log`)
- Markdown (`.md`)
- CSV / TSV (`.csv`, `.tsv`)
- JSON (`.json`)
- `.eml` emails (Python stdlib only)
- Archive listings (`.zip`)

PDFs, Word docs, and Excel require their respective backends to be installed.
