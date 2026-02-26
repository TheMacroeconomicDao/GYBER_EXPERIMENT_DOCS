---
title: "Smart Contracts Overview"
description: "GybernatyUnitManager — decentralized hierarchical user management system"
---

# Smart Contracts

## GybernatyUnitManager

Decentralized hierarchical user management system with multi-level approval mechanisms.

### Key Features

- **Hierarchical User Management** — 4 user levels with increasing privileges
- **Token Management** — Level-based withdrawal limits, monthly restrictions
- **Approval System** — Multi-signature style approvals with time limits
- **Gybernaty Role** — Administrative powers for system governance

### Architecture

```
GybernatyUnitManager (Main Contract)
├── UserManager      — User registration, levels, roles
├── TokenManager     — Token operations, withdrawal limits
└── ApprovalManager  — Multi-level approval workflows
```

### Technical Stack

| Component | Technology |
|-----------|-----------|
| Language | Solidity ^0.8.27 |
| Framework | Hardhat |
| Testing | Vitest |
| Standards | OpenZeppelin Upgradeable |

### Contract Functions

#### User Management
- `proposeCreateUser()` — Create new user (requires approval)
- `proposeChangeLevel()` — Change user level
- `assignGybernaty()` — Assign Gybernaty role

#### Token Operations
- `proposeWithdraw()` — Propose token withdrawal
- `approve()` — Approve pending action
- `getWithdrawalLimit()` — Check level-based limits

#### Governance
- `vote()` — Cast governance vote
- `proposeAction()` — Propose system action

### Source Code

Full source code and tests available in the [`contracts/`](https://github.com/TheMacroeconomicDao/GYBER_EXPERIMENT_DOCS/tree/main/contracts) directory.

!!! info "Audit Status"
    Smart contracts are under active development. Community review and formal audit pending.
