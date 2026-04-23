# legal-skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![GitHub Stars](https://img.shields.io/github/stars/chen-friedman/legal-skills?style=social)](https://github.com/chen-friedman/legal-skills) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

### **מיומנויות AI פתוחות למקור לאנשי מקצוע בתחום המשפט — היקף גלובלי, רב-לשוני**

*מיומנויות AI מוכנות לפרודקשן שעובדות ב-Claude, Claude Code, OpenCode, Cursor ועוד 30+ פלטפורמות סוכן*

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue?style=for-the-badge&logo=apache&logoColor=white)](https://opensource.org/licenses/Apache-2.0)
[![Agent Skills Standard](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-purple?style=for-the-badge&logo=openstreetmap&logoColor=white)](https://agentskills.io)
[![Global Scope](https://img.shields.io/badge/Global-Multilingual-green?style=for-the-badge&logo=world&logoColor=white)](https://github.com/chen-friedman/legal-skills)

**[🇬🇧 English](./README.md) | [🇮🇱 עברית](./README_HE.md)**

---

## מה מיוחד במיומנויות האלה?

**חוצה פלטפורמות** → מיומנות אחת עובדת ב-Claude, Claude Code, OpenCode, Cursor, GitHub Copilot, OpenHands, Goose, Codex וכל שאר הכלים שתומכים ב-[agentskills.io](https://agentskills.io)
**רב-לשוני מעצם התכנון** → 8 חבילות שפה בהשקה (אנגלית, עברית, ערבית, רוסית, ספרדית, צרפתית, גרמנית, פורטוגזית) — נטענות לפי צורך, ללא בזבוז טוקנים
**פרטיות קודמת לכל** → רץ 100% מקומי. זיהוי אוטומטי של מידע רגיש עם מיסוך. ללא טלמטריה, ללא קריאות חיצוניות.
**מודעת סביבה** → מסתגלת לכלי החילוץ שמותקנים. יורדת בצורה חלקה כשחסרים כלים.
**נבנתה על ידי מומחים** → תוכננה על ידי עורכי דין וטכנולוגים משפטיים לזרימות עבודה אמיתיות של תיקים, לא הדגמות צעצוע.

> **חדש ב-Agent Skills?** ראו את [סקירת Agent Skills](https://agentskills.io) ו[שיטות עבודה מומלצות לכתיבת מיומנויות](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) של Anthropic.

---

## תוכן עניינים

| **ניווט** | **תוכן** | **שימוש** |
|---|---|---|
| [🎯 מיומנויות זמינות](#-מיומנויות-זמינות) | מיומנות אחת | הגרסה הנוכחית |
| [🚀 התחלה מהירה](#-התחלה-מהירה) | התקנה ושימוש | לרוץ תוך 2 דקות |
| [🔍 mapping-legal-cases](#-mapping-legal-cases) | המיומנות המרכזית | ניתוח תיקיות תיקים |
| [🌍 חבילות שפה](#-חבילות-שפה) | 8 שפות | כיסוי בינלאומי |
| [🔒 פרטיות ואבטחה](#-פרטיות-ואבטחה) | מקומי בלבד | טיפול במסמכים רגישים |
| [📦 התקנה לפי פלטפורמה](#-התקנה-לפי-פלטפורמה) | Claude Code, OpenCode, Claude.ai, API | כל סוכני ה-AI המרכזיים |
| [🗺️ מפת דרכים](#️-מפת-דרכים) | v1.1, v1.2, v1.3, v2.0 | פיצ'רים מתוכננים |
| [🤝 תרומה](#-תרומה-לפרויקט) | חבילות שפה, מנהלי קבצים | הצטרפו לקהילה |

---

## 🎯 מיומנויות זמינות

| **מיומנות** | **מה היא עושה** | **סטטוס** |
|---|---|---|
| [mapping-legal-cases](./skills/mapping-legal-cases/) | ממפה תיקיית מסמכי תיק ל-10 קבצי ניתוח מוצלבים (צדדים, ציר זמן, טענות, ראיות, פערים, סיכונים, מועדים, מלאי, אינדקס מילות מפתח, דגלי פרטיות) | ✅ v1.0 |
| drafting-legal-responses | ניסוח בקשות, תגובות ומכתבי התראה מתוך פלט `.casebase/` | 📋 מפת דרכים v1.4 |
| legal-research | שימוש ב-CLAIMS.md + GLOSSARY.md לזיהוי פסיקה רלוונטית | 📋 מפת דרכים v1.4 |

---

## 🚀 התחלה מהירה — בחרו את המסלול הקל ביותר עבורכם

> **כל הפקודות למטה נבדקו end-to-end. אם משהו לא עובד — [פתחו issue](https://github.com/chen-friedman/legal-skills/issues).**

### 🎯 אפשרות A — Claude Code (שתי פקודות)

בתוך Claude Code, הריצו:

```
/plugin marketplace add chen-friedman/legal-skills
/plugin install legal-skills@chen-friedman
```

זהו. הפעילו מחדש את Claude Code אם מתבקשים, ואז בכל תיקיית תיק שאלו:
> "מפה את תיקיית התיק הזו"

לוודא התקנה:
```
/plugin list
```
אמור להופיע `legal-skills@chen-friedman` עם סטטוס `enabled`.

### 🎯 אפשרות B — Claude.ai (אפליקציית ווב) — העלאת ZIP

1. הורידו את קובץ ה-ZIP של ה-skill: **[mapping-legal-cases.zip](https://github.com/chen-friedman/legal-skills/releases/latest/download/mapping-legal-cases.zip)**
2. היכנסו ל-**[claude.ai](https://claude.ai)** → **Settings** → **Customize** → **Skills**
3. לחצו **Upload custom skill**, בחרו את ה-ZIP
4. הפעילו, ובכל שיחה העלו את קבצי התיק ושאלו: *"מפה את תיקיית התיק הזו."*

זמין במסלולי Free, Pro, Max, Team ו-Enterprise עם **code execution מופעל**.

### 🎯 אפשרות C — OpenCode

```bash
git clone https://github.com/chen-friedman/legal-skills.git
# Windows PowerShell:
New-Item -ItemType SymbolicLink -Path "$HOME\.config\opencode\skills\mapping-legal-cases" -Target "$PWD\legal-skills\skills\mapping-legal-cases"
# macOS / Linux:
ln -s "$PWD/legal-skills/skills/mapping-legal-cases" ~/.config/opencode/skills/mapping-legal-cases
```

### 🎯 אפשרות D — Cursor / Copilot / Gemini CLI / OpenHands / Goose / Kiro / Roo Code / כל כלי אחר שתומך ב-[agentskills.io](https://agentskills.io)

```bash
git clone https://github.com/chen-friedman/legal-skills.git
```

ואז הצביעו על `legal-skills/skills/mapping-legal-cases/` דרך הכלי שלכם. ראו בתיעוד של הכלי את נתיב המיומנויות המדויק.

### 🎯 אפשרות E — ללא התקנה: הדביקו את ה-prompt הבא בכל AI

אם אי אפשר להתקין מיומנויות בכלי שלכם, העתיקו את ה-skill ישירות לצ'אט:

1. פתחו את [`skills/mapping-legal-cases/SKILL.md`](./skills/mapping-legal-cases/SKILL.md) ב-GitHub (raw)
2. הדביקו את כל התוכן לצ'אט (Claude, ChatGPT, Gemini וכו') עם ה-prompt הזה:

```
אני אתן לך הגדרת skill. קרא והפנים אותה, ואז יישם אותה על תיקיית התיק שלי.
אשר שטענת את ה-skill, בקש את נתיב תיקיית התיק, ואז הרץ את workflow המיפוי.

--- SKILL DEFINITION START ---
[הדביקו כאן את תוכן SKILL.md]
--- SKILL DEFINITION END ---
```

זה לא יעיל כמו התקנה ילידית, אבל עובד בכל מקום.

### ✅ בדיקת הסביבה (אחרי כל שיטת התקנה)

```bash
python skills/mapping-legal-cases/scripts/extract.py --preflight --pretty
```

זה מראה אילו מחלצים זמינים במכונה (PDF, Word, Excel, OCR, תמלול). ה-skill מסתגל אוטומטית למה שמותקן.

---

## 🔍 mapping-legal-cases

*המיומנות המרכזית. מצביעים את ה-AI על תיקייה של מסמכי תיק — מקבלים תמצית ניתוח מובנית.*

### מה נכנס

כל תערובת של:
- 📄 PDF (מקומי או סרוק)
- 📝 מסמכי Word (`.docx`, `.doc`, `.odt`, `.rtf`)
- 📊 גיליונות אלקטרוניים (`.xlsx`, `.xls`, `.csv`, `.tsv`)
- ✉️ מיילים (`.eml`, `.msg`)
- 📑 Markdown, טקסט רגיל, JSON, HTML
- 🖼️ תמונות (OCR אוטומטי אם מותקן tesseract)
- 🔊 אודיו (תמלול אוטומטי אם מותקן whisper)
- 🎥 וידאו (תמלול אוטומטי + מטא-דאטה)

### מה יוצא

תת-תיקייה `.casebase/` עם **10 מסמכים מובנים**, כל ממצא מצוטט חזרה למקור שלו:

| **מסמך** | **תוכן** |
|---|---|
| `DOCUMENTS.md` | מלאי מלא עם סיכומי שורה אחת |
| `GLOSSARY.md` | אינדקס מילות מפתח דו-לשוני (אילו מונחים מופיעים היכן) |
| `PRIVACY_FLAGS.md` | מיקומי מידע רגיש (ערכים **ממוסכים**) |
| `PARTIES.md` | מי הם — לקוח, צד נגדי, שופטים, מומחים, עדים |
| `TIMELINE.md` | כל תאריך בסדר כרונולוגי עם מקורות |
| `CLAIMS.md` | טענות משפטיות עם בסיס, סטטוס, ראיות תומכות |
| `EVIDENCE.md` | ראיות עם קישור לכל טענה |
| `GAPS.md` | מסמכים חסרים, סתירות, שאלות פתוחות |
| `RISKS.md` | חולשות בתיק, חומר המועיל לצד השני |
| `DEADLINES.md` | תאריכים עתידיים עם דגלי **עבר המועד** / **דחוף** |

בנוסף `MAPPING_LOG.md` — יומן ביקורת עם קבצים שעובדו ומה עדיין דורש OCR/תמלול.

### איך זה עובד

**ארכיטקטורת שני גלים** שומרת על שימוש נמוך בטוקנים:

**גל 1** — מחלץ כל קובץ פעם אחת באמצעות `scripts/extract.py`, שומר את הטקסט במטמון, בונה את אינדקס מילות המפתח וביקורת הפרטיות.

**גל 2** — ארבע משימות ניתוח במקביל קוראות מהמטמון ובונות את 10 הפלטים. על פלטפורמות שתומכות בסוכני משנה, אלה רצות במקביל למהירות.

ה-extractor **מסתגל אוטומטית** למה שמותקן:
- בסיס (ללא התקנות): טקסט, markdown, CSV, JSON, מיילים `.eml`, רשימות zip
- עם חבילות Python: PDF, Word, Excel, תמונות, מיילי Outlook
- עם כלי CLI: pandoc (פורמטים עשירים יותר), tesseract (OCR), ffmpeg (מדיה), whisper (תמלול)
- כלים חסרים? קבצים מסומנים `[PENDING OCR]` / `[PENDING TRANSCRIPTION]` — **אף פעם לא חוסם**

### דוגמת פלט

ראו את [`skills/mapping-legal-cases/references/output-templates.md`](./skills/mapping-legal-cases/references/output-templates.md) למבנה המדויק של כל אחד מ-10 המסמכים שנוצרים. תיקיית הדגמה מקצה-לקצה עם קבצי PDF, DOCX ומיילים אמיתיים תגיע בגרסה v1.1.

---

## 🌍 חבילות שפה

חבילות מילות המפתח **נטענות לפי צורך** בהתבסס על שפת המסמכים שזוהתה — ללא בזבוז טוקנים על שפות שהתיק שלכם לא משתמש בהן.

| **חבילה** | **סטטוס** | **כיסוי** |
|---|---|---|
| `common-en` (אנגלית) | ✅ בסיס | מונחים משפטיים אוניברסליים (נטען תמיד) |
| `he` (עברית) 🇮🇱 | ✅ v1.0 | מערכת המשפט הישראלית |
| `ar` (ערבית) 🌍 | ✅ v1.0 | ערבית ספרותית סטנדרטית — כללי |
| `ru` (רוסית) 🇷🇺 | ✅ v1.0 | הפדרציה הרוסית + ברה"מ לשעבר |
| `es` (ספרדית) 🌍 | ✅ v1.0 | ספרד + אמריקה הלטינית |
| `fr` (צרפתית) 🌍 | ✅ v1.0 | צרפת, בלגיה, שווייץ, קוויבק |
| `de` (גרמנית) 🌍 | ✅ v1.0 | גרמניה, אוסטריה |
| `pt` (פורטוגזית) 🌍 | ✅ v1.0 | ברזיל + פורטוגל |
| `it`, `nl`, `pl`, `tr`, `zh`, `ja`, `ko`, `hi`, ... | 📋 מפת דרכים | **תרמו משלכם!** ראו [CONTRIBUTING.md](./CONTRIBUTING.md) |

כל חבילה כוללת ~150 מונחים משפטיים ב-13 קטגוריות (תאריכים, כסף, צדדים, הליכים, בתי משפט, סוגי מסמכים, פלילי, משפחה, נדל"ן, עבודה, ביטוח, תבניות פרטיות, רמזי שמות קבצים) בנוסף לתבניות regex ספציפיות ליוריסדיקציה למידע רגיש.

---

## 🔒 פרטיות ואבטחה

- **רץ לחלוטין מקומי.** אף תוכן מסמך לא עוזב את המחשב שלכם (אלא אם בחרתם להתקין backend ענן אופציונלי).
- **סריקת מידע רגיש אוטומטית.** תעודות זהות, כרטיסי אשראי, חשבונות בנק, מספרי תיק רפואי, מספרי דרכון, טלפונים — כולם מזוהים ו**ממוסכים** ב-`PRIVACY_FLAGS.md`.
- **תבניות פרטיות לפי יוריסדיקציה**: תעודת זהות ישראלית, SSN/EIN אמריקאי, CPF/CNPJ ברזילאי, DNI/NIE ספרדי, CURP/RFC מקסיקני, CUIT ארגנטינאי, RUT צ'יליאני, Steuer-ID גרמני, NIR צרפתי, ИНН/СНИЛС רוסי, NIF פורטוגזי ועוד.
- **המטמון מקומי בלבד כברירת מחדל.** `.casebase/.cache/` מכיל טקסט גולמי שחולץ — התייחסו אליו כמו לקבצים המקוריים.
- **ללא טלמטריה, ללא מעקב, ללא קריאות חיצוניות.** בדקו את `scripts/extract.py` בעצמכם — קובץ אחד עצמאי.

ראו [SECURITY.md](./SECURITY.md) לדיווח על פגיעויות.

---

## 📦 התקנה לפי פלטפורמה

<details>
<summary><b>Claude Code</b> (הקל ביותר — פקודה אחת)</summary>

```bash
/plugin marketplace add chen-friedman/legal-skills
/plugin install legal-skills@chen-friedman
```

אחרי ההתקנה, פשוט הזכירו מיפוי תיק בכל שיחה.
</details>

<details>
<summary><b>OpenCode</b></summary>

```bash
git clone https://github.com/chen-friedman/legal-skills.git ~/legal-skills
# אופציה א: symlink
ln -s ~/legal-skills/skills/mapping-legal-cases ~/.config/opencode/skills/mapping-legal-cases

# אופציה ב: העתקה
cp -r ~/legal-skills/skills/mapping-legal-cases ~/.config/opencode/skills/
```

ב-PowerShell של Windows:
```powershell
New-Item -ItemType SymbolicLink -Path "$HOME\.config\opencode\skills\mapping-legal-cases" -Target "$HOME\legal-skills\skills\mapping-legal-cases"
```
</details>

<details>
<summary><b>Claude.ai (אפליקציית ווב)</b></summary>

1. הורידו / שכפלו את הריפו
2. עשו zip לתיקיית `skills/mapping-legal-cases/` ל-`mapping-legal-cases.zip`
3. פתחו את Claude.ai → Settings → Features → Skills → Upload custom skill
4. העלו את ה-zip
</details>

<details>
<summary><b>Claude API</b></summary>

השתמשו ב-[Skills API](https://docs.claude.com/en/api/skills-guide) להעלאת המיומנות. כותרות בטא נדרשות:
- `skills-2025-10-02`
- `code-execution-2025-08-25`
- `files-api-2025-04-14`
</details>

<details>
<summary><b>Cursor, GitHub Copilot, Gemini CLI, OpenHands, Goose, Codex, Kiro, Roo Code ו-20+ נוספות</b></summary>

כולן תומכות ב-[תקן Agent Skills הפתוח](https://agentskills.io). שכפלו את הריפו, הצביעו על `skills/mapping-legal-cases/` דרך הכלי שלכם, וזה יעבוד. ראו את התיעוד של כל כלי לנתיב המיומנויות המדויק.
</details>

### תלויות מומלצות

המיומנות עובדת עם **אפס תלויות** לטקסט רגיל / CSV / JSON / Markdown / מיילי `.eml`. התקינו מה שצריך לפורמטים עשירים יותר:

```bash
# חבילות Python (ליבה)
pip install pymupdf pdfplumber python-docx openpyxl Pillow

# אופציונלי — תמיכה ב-Outlook .msg
pip install extract-msg

# אופציונלי — תמלול אודיו/וידאו
pip install faster-whisper
```

כלים חיצוניים (ספציפיים למערכת הפעלה):

| כלי | Windows | macOS | Linux (Debian/Ubuntu) |
|---|---|---|---|
| pandoc (Word/ODT/RTF) | `winget install JohnMacFarlane.Pandoc` | `brew install pandoc` | `sudo apt install pandoc` |
| tesseract (OCR) | `winget install UB-Mannheim.TesseractOCR` | `brew install tesseract` | `sudo apt install tesseract-ocr` |
| ffmpeg (מטא-דאטה של מדיה) | `winget install Gyan.FFmpeg` | `brew install ffmpeg` | `sudo apt install ffmpeg` |
| libreoffice (`.doc` ישן) | `winget install TheDocumentFoundation.LibreOffice` | `brew install libreoffice` | `sudo apt install libreoffice` |

**הריצו את בדיקת המוכנות בכל רגע:**
```bash
python skills/mapping-legal-cases/scripts/extract.py --preflight --pretty
```

---

## 🗺️ מפת דרכים

### v1.1 — עוד שפות + OCR טוב יותר
- איטלקית, הולנדית, פולנית, טורקית, סינית, יפנית, קוריאנית
- EasyOCR מובנה כ-fallback
- אשף התקנה

### v1.2 — שדרוגי חילוץ מובנה
- זיהוי ישויות (NER) לזיהוי אוטומטי של אנשים, ארגונים, מיקומים
- ניתוח מודע טבלאות לטבלאות פיננסיות ולוחות חוזים
- זיהוי חתימה (מסמכים חתומים מול לא חתומים)
- קיבוץ גרסאות (v1, v2, סופי)
- זיהוי הסתרה/רדקציה

### v1.3 — ידע יוריסדיקציוני עמוק
- תתי-חבילות אזוריות (`en-us`, `en-uk`, `es-mx`, `fr-ca`, `de-at`, `de-ch`)
- חבילות סדר דין יוריסדיקציוני (FRCP לבית משפט פדרלי אמריקאי וכו')
- ספריית פורמטים של מספרי תיקים

### v1.4 — אינטגרציות זרימת עבודה
- מיומנות תואמת: `drafting-legal-responses`
- מיומנות תואמת: `legal-research`
- אינטגרציית לוח שנה (DEADLINES.md → iCal / Google Calendar)
- רדקציה משלימה (רדקציה אוטומטית לפי PRIVACY_FLAGS.md)

### v2.0 — ניתוח מתקדם
- חיפוש בין תיקים
- זיהוי תקדימים
- בדיקת ניגוד עניינים
- הערכת פשרה
- טיפול בקורפוס רב-לשוני

פרטים מלאים ← [ROADMAP.md](./ROADMAP.md)

---

## 🤝 תרומה לפרויקט

תרומות מתקבלות בברכה — במיוחד **חבילות שפה חדשות**!

תחומי תרומה בעלי ערך גבוה:
1. **חבילות שפה** — איטלקית, הולנדית, פולנית, טורקית, סינית, יפנית, קוריאנית, הינדי ועוד
2. **תתי-חבילות אזוריות** — `es-mx`, `en-uk`, `fr-ca` וכו'
3. **מטפלי סוגי קבצים חדשים** — `.numbers`, `.pages`, `.key`
4. **משוב מהעולם האמיתי** — מעורכי דין פעילים ביוריסדיקציות שונות

ראו [CONTRIBUTING.md](./CONTRIBUTING.md) למדריך המלא.

---

## 📚 פרויקטים קשורים

בדקו את [awesome-legaltech](https://github.com/chen-friedman/awesome-legaltech) — רשימה מובחרת של כלי AI משפטי וטכנולוגיה משפטית בקוד פתוח, מאגרי נתונים וקהילות.

אבני בניין רלוונטיות שבהן המיומנות הזו משתמשת:
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) — חילוץ PDF
- [Pandoc](https://pandoc.org) — ממיר מסמכים אוניברסלי
- [Tesseract](https://github.com/tesseract-ocr/tesseract) — מנוע OCR
- [faster-whisper](https://github.com/guillaumekln/faster-whisper) — דיבור לטקסט
- [תקן Agent Skills](https://agentskills.io) — פורמט מיומנויות חוצה פלטפורמות

---

## 📄 רישיון

רישיון Apache 2.0. ראו [LICENSE](./LICENSE) ו-[NOTICE](./NOTICE).

**שימוש מסחרי מותר.** Fork, שנו, שלחו במוצר שלכם — פשוט שמרו על הערת הייחוס.

---

## 👤 מחבר

**חן פרידמן** — מייסד, [Lawcal AI](https://lawcal.ai)
ייעוץ AI משפטי וממשלתי, ישראל 🇮🇱

- GitHub: [@chen-friedman](https://github.com/chen-friedman)
- ראו גם: [awesome-legaltech](https://github.com/chen-friedman/awesome-legaltech) — טכנולוגיה משפטית מובחרת בקוד פתוח

---

## 🌟 תמיכה

אם זה עוזר לכם:
- ⭐ תנו כוכב לריפו
- 🐛 פתחו issues על באגים או בקשות פיצ'רים
- 🌐 תרמו חבילת שפה ליוריסדיקציה שלכם
- 📢 שתפו עם קולגות שיכולים להיעזר בזה

**שאלות?** פתחו [דיון](https://github.com/chen-friedman/legal-skills/discussions) או ראו [SECURITY.md](./SECURITY.md) לדיווח על פגיעויות.

---

*נבנה ב-❤️ לאנשי מקצוע משפטיים ברחבי העולם.*
