# Sample Case Folder — FICTIONAL DATA ONLY

This folder contains fabricated documents for demonstrating `mapping-legal-cases`. All names, dates, case numbers, and content are fictional.

**Do not use this as a legal template — these are intentionally simple and do not reflect real legal drafting standards.**

## Scenario

A fictional commercial lease dispute:

- **Plaintiff:** John Doe
- **Defendant:** Acme Corporation Ltd.
- **Case type:** Breach of commercial lease
- **Court:** (fictional) Superior Court, Central District

## Files in this folder

- `pleadings/statement-of-claim.md` — the opening pleading
- `pleadings/response.md` — defendant's response
- `contracts/lease-agreement.md` — the underlying contract
- `correspondence/2024-11-20-demand-letter.md` — pre-suit demand
- `correspondence/2024-12-05-response.md` — defendant's reply
- `evidence/payment-history.csv` — payment records
- `evidence/witness-statement.md` — a fact witness statement

## To try the skill on this folder

```bash
# Using the extractor directly
python ../../skills/mapping-legal-cases/scripts/extract.py --scan . --pretty

# Or ask your AI (if the skill is installed)
"Map the case folder at examples/sample-case-folder"
```

See `../expected-output/` for what the 10 generated documents should look like.
