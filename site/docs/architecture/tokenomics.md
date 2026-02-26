---
title: "Tokenomics (GBR)"
description: "GyberCommunityToken specification, emission, rewards, liquidity"
---

## 4.2. GyberCommunityToken (Gbr): Tokenomics

### 4.2.1. Token Specification

```
Name:               GyberCommunityToken
Ticker:             Gbr
Standard:           BEP-20 (Binance Smart Chain)
Contract address:   0xa970cae9fa1d7cca913b7c19df45bf33d55384a9
Type:               Utility Token
Total supply:       Fixed (defined at contract deployment)
Additional
emission:           Impossible (contract contains no mint function
                    after initialization)
```

**Token functions in the ecosystem:**

```
1. Governance:
   — Voting in DAOs (Social, Code, Commerce, Economic)
   — Signing proposals
   — Condition: wallet must be active
     (verified by special algorithm during voting)

2. Work evaluation:
   — Means of evaluating participant contributions to projects
   — Rewards through UnitManager
     (proportional to status and confirmed activity)

3. Infrastructure interaction:
   — Interaction with GyberNet Blockchain
   — Interaction with GyberComputer
   — Confirming seriousness of intent when initiating projects
     (burning 0.1% of C(p) when transitioning to Accumulation)

4. Staking:
   — Gbr staking: percentage determined by
     Economic DAO voting and adapted to ecosystem
     economic parameters
   — Improving participant reputation
   — Passive income

5. Medium of exchange:
   — Trading on DEX (PancakeSwap)
   — Interaction with project liquidity pools
   — Discounts for special project clients
```

### 4.2.2. Emission Distribution and Management

```
Distribution (fixed supply, deflationary model):

  Governance Pool (~80%+):
    — Controlled by initiators and key
      community members during experiment
      deployment phase
    — Used for on-chain voting, UnitManager funding,
      and reserve operations
    — As system automation progresses, funds are transferred
      to stabilization fund — smart contract
      managed exclusively through DAO voting
    — Managed through BEP-20 delegation mechanism

  Trading Float (~20% or less):
    — Listed on DEX (PancakeSwap)
      to provide liquidity and pricing
    — Creates market mechanism for determining Gbr value
```

### 4.2.3. Reward Mechanism: UnitManager

UnitManager is a smart contract implementing the RewardProtocol and serving as the technical realization of Axiom 5 (meritocratic fairness).

**Implementation status:** the current UnitManager version (GybernatyUnitManager) is a working prototype demonstrating the principle of automatic reward distribution based on participant status. The prototype implements four levels (Unit, Dev, LeadDev, ArchDev), a two-level approval system (confirmation by participants 1 and 2 levels higher), and withdrawal frequency limits (up to 2 times per month). G-Plan integration for activity verification is the next development stage.

**Reward payment algorithm:**

![UnitManager Reward Flow](diagrams/process/unitmanager_rewards.svg)

*Figure 4.4: UnitManager reward distribution process showing five steps: (1) Fixed reward by status level (Unit: 10M Gbr, Dev: 100M Gbr, LeadDev: 1B Gbr, ArchDev: 10B Gbr), (2) ×5 multiplier for project completion, (3) Activity confirmation via G-Plan, (4) Payment execution, and (5) On-chain recording for transparency.*

**Key mechanisms:**

1. **Fixed reward by Unit Type** — Each participant receives rewards based on their status level, paid for confirmed activity in the current period
2. **Project completion bonus (×5 multiplier)** — Teams that bring a project to Operation phase receive 5× their base reward, creating tremendous incentive to complete projects
3. **Activity confirmation** — UnitManager queries G-Plan to verify participation in tasks, task completion confirmed by higher-status participants, and overall involvement
4. **Payment** — Automatic transfer upon confirmation, or rejection if activity not verified
5. **Recording** — All operations recorded on BSC blockchain for complete transparency and auditability

**Connection to theory.** UnitManager implements several axioms simultaneously:
- A2 (transparency): all payments on blockchain, verifiable by anyone
- A5 (meritocracy): reward determined by status and activity, not capital
- A6 (inclusiveness): minimum status (Unit) accessible to every active participant

**Anti-free-riding mechanism:** reward is paid not for "presence in the system" but for verified completion of specific tasks in G-Plan. The x5 multiplier for project completion creates additional incentive for real contribution rather than minimal activity simulation. AI verification of task quality (section 6.4) provides primary filtering against formal completion without substantive results.

Critical difference from existing DAOs: in most DAOs, rewards are determined by tokenholder or administrator voting — creating subjectivity and politicization. In UnitManager, rewards are determined by **objectively verifiable activity** through G-Plan, with size tied to status determined by the community. This minimizes room for manipulation.

### 4.2.4. Liquidity Pools and Project Integration

The liquidity pool mechanism is a key element implementing Axiom 6 (inclusiveness) and Loop 2 (liquidity):

```
For each project pⱼ transitioning to Operation state:

1. Internal project tokens token(pⱼ) are issued
   (during Accumulation phase, for sale at 1 BUSD)

2. Before opening trading on DEX, a liquidity pool is created:
   Pool(pⱼ) = {token(pⱼ), Gbr}

3. This means token(pⱼ) trades in pair with Gbr

4. Consequence for participants:
   — Any Gbr holder can acquire token(pⱼ)
     through DEX, regardless of participation in SIC(pⱼ)
   — Active participants receiving Gbr through UnitManager
     automatically have access to tokens of any project
   — This implements the principle: "active community members
     receive tokens of any project, regardless of
     personal participation in specific project"

5. Internal token staking:
   token(pⱼ) staking: 10 / [total_supply(token(pⱼ))] %
   of project pⱼ revenue

   This creates a direct economic link between
   project success and reward for token holders.

6. Project client levels:
   — External clients: use fiat currency,
     pay full price
   — Special clients: use Gbr,
     receive discount
   — Super clients: use token(pⱼ),
     receive maximum discount

   This creates economic incentive for acquiring
   and holding Gbr and token(pⱼ), supporting
   token liquidity and value.
```

To prevent liquidity fragmentation as the ecosystem scales, minimum liquidity thresholds for each pool are established by Commerce DAO voting, along with aggregation mechanisms through PowerSwapMeta (section 6.5).
