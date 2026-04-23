# Common Legal Keywords — English (Baseline)

**Status:** Always loaded.

This is the universal English keyword seed. Covers civil litigation, criminal, family, commercial, property, labor, tort, and contract law across common-law and civil-law systems.

**Language-specific packs** (loaded on-demand based on corpus language) extend this with jurisdiction-specific terms. See `he.md`, `ar.md`, `ru.md`, `es.md`, `fr.md`, `de.md`, `pt.md`.

## 1. Dates & Time

| Term | Notes |
|---|---|
| date | generic |
| deadline | procedural importance |
| by (date) | deadline marker |
| within X days | response window |
| within X business days | |
| before (date) | |
| after (date) | |
| starting from | effective date marker |
| effective date | contract |
| expiration date | contract/statute |
| statute of limitations | |
| urgent | |
| immediate | |
| without delay | |
| as soon as practicable | |
| upon receipt | |
| forthwith | |
| today / yesterday / tomorrow | relative |
| next (Monday, week, month) | relative |

**Date patterns to regex-match:**
- `\d{1,2}[./\-]\d{1,2}[./\-]\d{2,4}` — DD/MM/YYYY, DD.MM.YYYY, DD-MM-YY
- `\d{4}-\d{2}-\d{2}` — ISO
- `(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2},?\s+\d{4}` — Month DD, YYYY
- `\d{1,2}\s+(January|February|...|December)\s+\d{4}` — DD Month YYYY

## 2. Money & Currency

| Term | Symbol |
|---|---|
| dollar / dollars | $ / USD |
| euro / euros | € / EUR |
| pound / pounds (sterling) | £ / GBP |
| yen | ¥ / JPY |
| yuan | ¥ / CNY |
| amount | |
| payment | |
| expenses / costs | |
| compensation | |
| damages | |
| fine / penalty | |
| interest | |
| indexation / adjustment | |
| tax / taxes | |
| VAT / GST / sales tax | |
| principal | |
| liquidated damages | |
| punitive damages | |
| attorney fees | |
| court costs | |
| settlement amount | |

**Currency regex patterns:**
- `[\$£€¥]\s*[\d,]+(\.\d+)?` — symbol + amount
- `[\d,]+(\.\d+)?\s*(USD|EUR|GBP|JPY|CNY|INR|AUD|CAD)` — amount + code
- Numbers > 1,000 in proximity to currency keywords

## 3. Parties & Roles

| Term | Category |
|---|---|
| plaintiff / claimant | party |
| defendant | party |
| petitioner | party |
| respondent | party |
| appellant | party |
| appellee | party |
| applicant | party |
| third party / third-party | party |
| intervenor | party |
| counter-plaintiff / counter-defendant | party |
| cross-plaintiff / cross-defendant | party |
| client | |
| attorney / lawyer / counsel / esquire / esq. | attorney |
| attorney of record | attorney |
| law firm | attorney |
| paralegal | attorney |
| judge / justice / magistrate | court |
| the honorable / hon. | court |
| chief judge / chief justice | court |
| clerk of court | court |
| court reporter | court |
| witness / witnesses | evidence |
| fact witness | evidence |
| expert witness / expert | evidence |
| character witness | evidence |
| mediator | ADR |
| arbitrator | ADR |
| prosecutor / district attorney / DA / crown | criminal |
| accused / defendant | criminal |
| complainant / victim | criminal |
| minor / child | family |
| guardian / guardian ad litem | family |
| trustee | fiduciary |
| executor / administrator | probate |
| beneficiary | probate/trust |
| heir | probate |
| debtor / creditor | commercial |
| guarantor | commercial |
| assignor / assignee | contract |
| licensor / licensee | contract |
| lessor / lessee / landlord / tenant | property |
| buyer / seller / vendor / purchaser | commercial |
| employer / employee | labor |
| insurer / insured | insurance |

## 4. Legal Procedures & Actions

| Term |
|---|
| complaint / statement of claim / petition |
| answer / statement of defense / response |
| reply |
| notice of appeal |
| motion / application |
| motion to dismiss |
| motion for summary judgment |
| motion in limine |
| motion for reconsideration |
| brief / memorandum of law |
| response / opposition |
| reply brief |
| affidavit / declaration / sworn statement |
| verified pleading |
| demand letter / cease and desist |
| service of process |
| summons |
| subpoena |
| subpoena duces tecum |
| discovery |
| interrogatories |
| requests for production |
| requests for admission |
| deposition |
| hearing |
| trial |
| bench trial |
| jury trial |
| verdict |
| judgment / judgement |
| default judgment |
| order |
| temporary restraining order / TRO |
| preliminary injunction |
| permanent injunction |
| consent decree |
| settlement agreement |
| release / waiver |
| appeal |
| remand |
| reversal / affirmance |
| writ / writ of certiorari / writ of mandamus |
| stay of proceedings / stay of execution |
| lien / attachment |
| garnishment |
| execution |
| contempt of court |
| sanctions |

## 5. Courts & Tribunals

| Term |
|---|
| supreme court |
| court of appeals / appellate court |
| district court |
| superior court |
| circuit court |
| magistrate court |
| municipal court |
| family court |
| probate court |
| juvenile court |
| traffic court |
| small claims court |
| bankruptcy court |
| tax court |
| administrative law judge / ALJ |
| tribunal |
| panel |
| registrar |
| clerk |
| docket |
| case number |

**Case number patterns (varied by jurisdiction):**
- `\d+[-/]\d+[-/]\d+` — generic three-segment
- `\d+:\d+-[A-Z]{2,4}-\d+` — US federal style
- `[A-Z]{2,6}\s*\d+/\d+` — European style

## 6. Document Types

| Term |
|---|
| contract / agreement |
| memorandum of understanding / MOU |
| letter of intent / LOI |
| affidavit / declaration |
| certification / certificate |
| receipt / bill / invoice |
| bank statement / account statement |
| report |
| expert report / opinion |
| medical opinion / medical report |
| certificate of birth / death / marriage |
| power of attorney / POA |
| will / last will and testament |
| trust deed |
| notarized translation |
| transcript / protocol / minutes |
| letter / correspondence |
| email |
| text / SMS / WhatsApp / messaging |
| photograph / photo |
| video / recording |
| audio / recording |
| scan |

## 7. Criminal Law

| Term |
|---|
| offense / offence |
| felony |
| misdemeanor |
| infraction |
| indictment |
| information (criminal) |
| arraignment |
| plea |
| guilty / not guilty / no contest / nolo |
| investigation |
| arrest |
| detention / custody |
| bail / bail bond / surety |
| search warrant |
| arrest warrant |
| Miranda / caution |
| confession |
| acquittal |
| conviction |
| imprisonment / incarceration |
| probation |
| parole |
| suspended sentence |
| community service |
| fine |
| restitution |
| criminal record |

## 8. Family Law

| Term |
|---|
| divorce / dissolution |
| separation |
| alimony / spousal support / maintenance |
| child support |
| custody (sole / joint) |
| visitation / parenting time / access |
| property division / equitable distribution |
| marital property |
| separate property |
| prenuptial / antenuptial / postnuptial agreement |
| paternity |
| adoption |
| domestic violence / DV |
| protective order / restraining order |
| guardianship |
| emancipation |

## 9. Property & Real Estate

| Term |
|---|
| property |
| real estate / real property |
| apartment / unit |
| house / home |
| land / parcel / lot |
| title |
| deed |
| mortgage |
| lien / encumbrance |
| easement |
| lease / rental |
| tenant / lessee |
| landlord / lessor |
| security deposit |
| eviction |
| foreclosure |
| zoning |
| building permit |
| certificate of occupancy / CO |
| homeowners association / HOA |
| condominium / condo |

## 10. Labor & Employment

| Term |
|---|
| employee / employer |
| salary / wages / compensation |
| pay stub / payslip |
| severance / severance pay |
| notice period |
| termination / dismissal / firing |
| resignation |
| layoff |
| at-will employment |
| wrongful termination |
| vacation / annual leave / PTO |
| sick leave |
| maternity / paternity / parental leave |
| overtime |
| collective bargaining agreement / CBA |
| union |
| discrimination |
| harassment |
| retaliation |
| EEOC / equal employment |
| workers' compensation |

## 11. Insurance & Torts

| Term |
|---|
| insurance |
| policy |
| claim |
| insurance company / carrier |
| premium |
| deductible |
| coverage |
| damage / damages |
| bodily injury / personal injury |
| disability / disabled |
| accident |
| traffic accident / motor vehicle accident / MVA |
| work accident / workplace injury |
| negligence |
| gross negligence |
| strict liability |
| product liability |
| medical malpractice |
| wrongful death |
| pain and suffering |

## 12. Contracts & Commercial

| Term |
|---|
| contract / agreement |
| party / parties |
| consideration |
| offer / acceptance |
| breach / breach of contract |
| material breach |
| anticipatory breach |
| warranty |
| representation |
| indemnification / indemnity |
| limitation of liability |
| force majeure |
| termination clause |
| renewal |
| assignment |
| non-compete / noncompete |
| confidentiality / non-disclosure / NDA |
| governing law |
| choice of forum / jurisdiction clause |
| arbitration clause |
| severability |
| entire agreement / integration |

## 13. Privacy-Sensitive Patterns (for PRIVACY_FLAGS.md)

**Always flag and mask** matches of these patterns in output:

| Data Type | Pattern |
|---|---|
| Credit card | `\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b` |
| US SSN | `\b\d{3}-\d{2}-\d{4}\b` |
| US EIN | `\b\d{2}-\d{7}\b` near "EIN" or "Tax ID" |
| IBAN | `\b[A-Z]{2}\d{2}[\s]?[A-Z0-9]{4}[\s]?[A-Z0-9]{4}[\s]?[A-Z0-9]{4}[\s]?[A-Z0-9]{4}[\s]?[A-Z0-9]{0,7}\b` |
| Routing number (US) | `\b\d{9}\b` near "routing" or "ABA" |
| Passport (generic) | 6–10 alphanumeric after "passport" |
| Phone (US) | `\b\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b` |
| Phone (international) | `\+\d{1,3}[\s.-]?\d{2,14}` |
| Email | `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}` (not sensitive alone, but track) |
| Medical record | digits near "medical record", "MRN", "patient ID", "chart number" |
| Date of birth / DOB | date strings near "DOB", "born", "date of birth" |

**Masking rule:** In PRIVACY_FLAGS.md, replace matched values with asterisks keeping only first 3 characters: `123-**-****` or `****-****-****-1234` (last-4 for CC).

## 14. File-Name Signals

Filenames containing these patterns may indicate document type without reading content:

- Date in name: `\d{4}[-_.]?\d{2}[-_.]?\d{2}` (YYYY-MM-DD and variants)
- Version markers: `v\d+`, `draft`, `final`, `signed`, `executed`
- Document-type keywords: `contract`, `agreement`, `complaint`, `motion`, `order`, `judgment`, `affidavit`, `invoice`, `receipt`, `statement`, `letter`, `email`, `report`, `deposition`, `transcript`
- Case numbers in filenames
- Party initials / abbreviations
- `FINAL`, `SIGNED`, `EXECUTED`, `APPROVED`, `DRAFT`
