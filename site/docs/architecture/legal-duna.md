---
title: "Legal Framework (DUNA)"
description: "Gybernaty DUNA legal structure and compliance"
---

## 4.7. Legal Framework: Gybernaty DUNA

### 4.7.1. Rationale for Legal Form

The CyberSocial Corporation exists in the space of blockchain and smart contracts, but its interaction with the traditional economy — banking operations, contracts with counterparties, tax obligations, intellectual property protection — requires a legal entity. The choice of legal form is a critical decision: the wrong form can undermine axioms A1 (decentralization) and A7 (self-governance).

**Fundamental distinction: Gybernaty DUNA ≠ MacroeconomicDAO.** Gybernaty DUNA is a centralized legal gateway for the experiment's bootstrap phase. It serves as an administrative shell allowing organizers to conduct the experiment within the legal framework of traditional economy: opening bank accounts, signing contracts, paying taxes. DUNA is intentionally centralized at this stage — organizers retain control to ensure operational efficiency and project survival in its early phase. MacroeconomicDAO, described in section 5, is the target state of full decentralization toward which the experiment evolves as the community grows and protocol matures. The transition from DUNA to MacroeconomicDAO is a planned trajectory, not a one-time event.

```
Chosen form: DUNA (Decentralized Unincorporated
Nonprofit Association) — State of Wyoming, USA

Rationale:

  1. Specialized legal form for DAO:
     DUNA created in 2024 specifically for
     recognizing on-chain governance in legal field.
     This means Governor contract decisions
     have legal force — direct link between
     smart contract and legal entity.

  2. Exclusion of fiduciary duties:
     DUNA allows excluding fiduciary duties
     of members, enabling complete reliance
     on code and voting. This is critically important
     for realizing Axiom A7 (self-governance):
     decisions made by algorithm, not trustees.

  3. Limited liability:
     Limits participants' (community members')
     liability for DAO obligations — risk
     limitation for participants.

  4. Nonprofit status:
     Revenue reinvested, not distributed
     as dividends. This corresponds to CSC model
     where success criterion is social
     relevance, not profit maximization
     (Definition 3.2.1, item 6).

  5. Public smart contract identifier:
     Governor contract address specified
     during registration — creates direct legal
     link between legal entity and on-chain
     governance mechanism.
```

### 4.7.2. Control Architecture: Community → DUNA → Real World

```
Absolute control principle:

  Gybernaty Community (Gbr holders)
    │
    │ on-chain voting
    │ through Governor + Timelock
    ▼
  Gybernaty DUNA (legal entity)
    │
    │ legally binding
    │ voting decisions
    ▼
  Administrator (Ministerial Agent)
    │
    │ technical execution:
    │ fiat payments, taxes, compliance
    ▼
  Traditional economy
    (banks, counterparties, regulators)

Key Administrator limitations:
  — No right to initiate spending
    without on-chain voting
  — No access to crypto treasury
    (keys absent)
  — Cannot block approved decisions
  — Can be instantly replaced through
    Social DAO voting
  — Role is exclusively technical
    execution: ministerial agent,
    not manager

Two-tier treasury:

  Crypto treasury (DAO-managed):
    All crypto assets → Timelock contract
    Any movement → Governor vote
    Direct community control

  Fiat treasury:
    Treasury Fiat Account → DAO-managed
      (large payments, core funds)
    Operating Fiat Account → Administrator
      (small operational expenses within
       approved budget, max $2,000
       per transaction)

    Operating Account replenishment → only
    through governance vote (e.g., $10K/month)

    Surplus → automatic return
    to Treasury Account
```

### 4.7.3. Legal Value Extraction Mechanisms for Participants

CSC participants make real contributions — intellectual labor, code, research, coordination — and must receive compensation. DUNA provides legal mechanisms for this:

```
1. Service compensation:
   Participants contract with DUNA
   (strategic leadership, technical
    development, research, coordination).
   Compensation size approved by voting.
   Legal qualification: "reasonable compensation"
   permitted by law.

2. Research grants:
   DUNA issues grants for new product development,
   research, educational programs.
   Grants approved through Economic DAO or Social DAO.

3. Buyback & Burn:
   DUNA directs portion of revenue to buying back GBR
   from DEX and burning.
   Legal qualification: "asset management operation
   to maintain protocol liquidity", NOT profit
   distribution.
   Effect: deflationary pressure on supply → with
   stable demand → Gbr value growth → increased
   real value of UnitManager rewards.

All operations go through voting (crypto part
executed automatically through Timelock, fiat part —
through Administrator).
```

### 4.7.4. Axiom Compliance / Legal Limitations and Priorities

```
A1 (decentralization):
  — DUNA has no single controlling person
  — Governance pool (~80%+) distributed across dozens
    of wallets
  — No single participant < 25% control

A2 (transparency):
  — All voting on-chain on BSC
  — All crypto treasury operations through Timelock
  — Monthly Administrator reports
  — Public dashboard (Dune Analytics)
  — Mandatory smart contract audits

A3 (sovereignty):
  — Each participant controls their keys
  — No one has access to others' wallets

A5 (meritocracy):
  — Reward determined by activity (G-Plan)
    and status, not token quantity

A6 (inclusiveness):
  — Minimum entry barrier
  — Liability limitation through DUNA
  — Liquidity pools ensure participation in success
    of any project

A7 (self-governance):
  — Governor contract = legally recognized
    governance mechanism
  — Administrator subordinate to voting
  — All critical decisions through DAO

A8 (cognitive augmentation):
  — AI Administrator monitor: autonomous agent
    continuously analyzing Administrator actions
    for compliance with DAO decisions:
    ∀ action(Adm) : Verify(action, DAO_decisions) ∈ {compliant, alert}
  — Upon discrepancy detection (alert) —
    automatic notification to Social DAO
    with violation details
  — AI monitor has no executive authority:
    only observation and alerting (watchdog principle)
  — Monitoring logs recorded on-chain,
    ensuring control auditability
```

**Nonprofit constraint upon dissolution:** in accordance with Wyoming law, upon DUNA dissolution, association assets cannot be distributed among participants for their private benefit. Assets must be transferred to another nonprofit organization with similar mission. GBR token holders have no right to receive assets in exchange for tokens upon dissolution. This is a fundamental property of nonprofit form, ensuring ecosystem value cannot be "privatized."

**Agreement priority over code:** in case of discrepancy between Association Agreement text and smart contract behavior, legally the Agreement has priority. Smart contracts are tools implementing the Agreement, not its replacement. Upon discovering discrepancy, community must bring code into compliance with Agreement through voting. This is legal reality that doesn't undermine algorithmic governance principle: code implements law, doesn't create it.
