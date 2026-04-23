# Legal Claims

**Analysis Date:** 2026-04-22
**Claims indexed:** 5

## Plaintiff's Claims

### Claim C1 — Breach of Contract (unpaid rent)
- **Source:** `pleadings/statement-of-claim.md:Count 1`
- **Legal basis:** Lease Agreement § 2 (rent obligation); doctrine of material breach
- **Relief sought:** $250,000 total ($45,000 outstanding + $180,000 accelerated + $25,000 interest/costs)
- **Supporting evidence:** E1 (lease), E2 (payment history), E3 (demand letter)
- **Status:** **partially-supported** — payment records confirm missed payments but quantum of damages depends on whether Defendant's set-off defense succeeds
- **Key facts alleged:**
  - Rent of $5,000/month due 1st of each month — per `contracts/lease-agreement.md:Article 2`
  - 9 months unpaid from 2024-09-01 — per `evidence/payment-history.csv`
  - Demand sent 2024-11-20 — per `correspondence/2024-11-20-demand-letter.md`

### Claim C2 — Declaratory Relief (lease termination)
- **Source:** `pleadings/statement-of-claim.md:Count 2`
- **Relief sought:** Declaration that Lease is terminated effective 2025-04-01
- **Status:** depends on outcome of C1

## Defendant's Claims / Defenses

### Defense D1 — Set-off (Lease § 8.2)
- **Source:** `pleadings/response.md:First Defense`
- **Legal basis:** Lease Agreement § 8.2 (set-off right for unperformed maintenance)
- **Supporting evidence:** E4 (witness statement confirming maintenance issues), E5 (defense response letter)
- **Status:** **partially-supported** — witness confirms issues reported but no evidence of specific repair costs substantiating $28,500

### Defense D2 — Constructive Eviction
- **Source:** `pleadings/response.md:Second Defense`
- **Legal basis:** common-law doctrine
- **Status:** **unclear** — corpus lacks evidence of actual unusability of premises

### Defense D3 — Prior Material Breach
- **Source:** `pleadings/response.md:Third Defense`
- **Legal basis:** doctrine of prior material breach
- **Status:** **partially-supported** — witness statement suggests Plaintiff's maintenance failures preceded Defendant's payment default

## Counter-claim

### Counter-claim CC1 — Maintenance costs + consequential damages
- **Source:** `pleadings/response.md:Counterclaim`
- **Relief sought:** $28,500 repair costs + $15,000 consequential damages
- **Status:** **unsupported in current corpus** — no invoices, receipts, or business-disruption documentation provided

## Cross-Reference Matrix

| Claim / Defense | Supporting Evidence | Contradicting Evidence |
|---|---|---|
| C1 (unpaid rent) | E1, E2, E3 | E4 (maintenance issues that trigger set-off) |
| C2 (termination) | C1 outcome | D1/D3 if successful |
| D1 (set-off) | E4, E5 | E1 (§ 8.2 requires 30-day written notice — unclear if satisfied) |
| D2 (constructive eviction) | E4 | corpus lacks evidence of actual unusability |
| D3 (prior breach) | E4 | — |
| CC1 (counterclaim damages) | — | no supporting invoices in corpus |

## Legal Authorities Cited

- **Lease Agreement § 8.2 (set-off)** — in `contracts/lease-agreement.md`, invoked in `pleadings/response.md`
- **Lease Agreement § 14.1 (forum-selection)** — in `contracts/lease-agreement.md`
- **Doctrine of prior material breach** — raised in `pleadings/response.md` (no specific authority cited)

## Potentially Unstated Claims

Based on corpus facts:
- **Waiver argument (Plaintiff):** Defendant continued using premises for 7 months while withholding rent without formal § 8.2 notice — could waive set-off defense
- **Implied covenant of good faith (either side):** corpus shows potentially incomplete communication from both parties

---
*Claims analysis by mapping-legal-cases on 2026-04-22*
