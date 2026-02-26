---
title: "MacroeconomicDAO"
description: "Governance system with four classes of DAO"
---

## 4.6. MacroeconomicDAO: Governance System

MacroeconomicDAO is the central mechanism implementing Axiom 7 (self-governance). It is a transparent interaction and decision-making system based on blockchain and audited smart contracts in Solidity using the OpenZeppelin library.

### 4.6.1. Governance Architecture

```
Technical implementation:

  Governor Contract (OpenZeppelin Governor):
    — Deployed on BNB Smart Chain (BSC)
    — Accepts proposals from Gbr holders
    — Manages voting: counting votes,
      determining quorum, fixing results
    — Passes approved proposals to Timelock

  Timelock Contract:
    — Delay in executing approved decisions
      (24–48 hours — parameter determined by community)
    — Ensures ability to react urgently
      if malicious proposal detected
    — Automatic execution after delay expires

  Gnosis Safe (emergency multisig):
    — Emergency pause in case of
      critical vulnerability discovery
    — Keys held by trusted community members
      (determined by voting)
    — Cannot initiate spending — only pausing
```

### 4.6.2. Decision-Making Process

```
Standard governance cycle:

  1. Proposal:
     Any participant with active wallet and sufficient
     Gbr (Proposal Threshold) submits
     proposal to corresponding DAO.

     Requirement: wallet must be classified
     as "active" by verification algorithm — this
     prevents governance capture by large but
     inactive holders.

  2. Discussion:
     Proposal published in GSP project space
     linked to corresponding DAO.
     Discussion period: 1–2 days (Voting Delay).

  3. Voting:
     After discussion period expires,
     voting opens. Voting period: 3–7 days.
     Quorum: 10–20% of total supply
     (specific parameters determined by community).

     Voting mechanism may vary
     by DAO class and proposal type:
     simple majority, qualified
     majority, quadratic voting.

  4. Execution:
     Approved proposals automatically queued
     in Timelock. After delay expires —
     automatic execution of on-chain operations.

     For off-chain operations — authorized
     executors (implementers) proceed to work.

  5. Accountability:
     Execution results recorded on-chain.
     Implementers report through GSP.
     Reputation system records execution
     quality.
```

### 4.6.3. Four DAO Classes

MacroeconomicDAO unites four classes of decentralized organizations, each responsible for a specific category of decisions:

```
┌──────────────────────────────────────────────────────────────┐
│                    MacroeconomicDAO                           │
│              (meta-level coordination)                        │
│                                                              │
│  ┌─────────────────┐          ┌─────────────────┐            │
│  │   Social DAO     │          │    Code DAO      │           │
│  │                  │          │                  │           │
│  │ Social life of   │          │ Technical        │           │
│  │ community:       │          │ infrastructure:  │           │
│  │ norms, events,   │          │ codebase,        │           │
│  │ membership,      │          │ architecture,    │           │
│  │ disputes         │          │ standards        │           │
│  └─────────────────┘          └─────────────────┘            │
│                                                              │
│  ┌─────────────────┐          ┌─────────────────┐            │
│  │  Commerce DAO    │          │  Economic DAO    │           │
│  │                  │          │                  │           │
│  │ Commercial       │          │ Systemic         │           │
│  │ projects:        │          │ economic         │           │
│  │ crowdinvesting,  │          │ decisions:       │           │
│  │ business plans,  │          │ treasury,        │           │
│  │ profitability    │          │ strategy,        │           │
│  │                  │          │ large-scale      │           │
│  │                  │          │ projects         │           │
│  └─────────────────┘          └─────────────────┘            │
└──────────────────────────────────────────────────────────────┘
```

Detailed specification of each class presented in Section 5.

### 4.6.4. Wallet Activity Verification

A distinctive feature of MacroeconomicDAO is the requirement for **wallet activity verification**. To participate in governance (voting and signing proposals), a tokenholder's wallet must be classified as "active" by a special verification algorithm.

```
Verification algorithm checks:
  — Participation in ecosystem tasks (G-Plan data)
  — Interaction with projects (commits, discussions,
    financing)
  — Activity regularity (not one-time actions
    but sustained participation pattern)

Mechanism goals:
  — Preventing governance capture by inactive
    large holders
  — Ensuring governance power is exercised
    by participants involved in
    experiment's current activities
  — Aligning governance influence with active
    contribution rather than passive wealth
```
