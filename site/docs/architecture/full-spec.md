---
title: "GyberExperiment Architecture"
description: "Technical specification — tokens, platforms, blockchain, DAO, legal, AI"
---

# Section 4: GyberExperiment Architecture — Technical Specification

## 4.1. From Theory to Implementation: Mapping Correspondences

Sections 1–3 laid the theoretical foundation: identified the problem, formulated axioms, introduced formal models of CSC, PMIP, SES, FRP, and described CyberSocium as a complex adaptive system. This section translates theory into architecture — describing how each theoretical construct is technically realized within GyberExperiment.

![Theory to Implementation Mapping](diagrams/architecture/theory_implementation_map.svg)

*Figure 4.2: Mapping of theoretical CyberSocium constructs to their technical implementations in GyberExperiment. Each axiom (A1-A7), principle (PMIP, SES), and theoretical element corresponds to specific infrastructure components and mechanisms.*

**System Architecture:**

```
                        ┌──────────────────────────────┐
                        │      MacroeconomicDAO         │
                        │  ┌────────┐  ┌────────┐      │
                        │  │Social  │  │ Code   │      │
                        │  │  DAO   │  │  DAO   │      │
                        │  └────────┘  └────────┘      │
                        │  ┌────────┐  ┌────────┐      │
                        │  │Commerce│  │Economic│      │
                        │  │  DAO   │  │  DAO   │      │
                        │  └────────┘  └────────┘      │
                        └──────────────┬───────────────┘
                                      │ governance
                        ┌─────────────▼────────────────┐
                        │     GyberNet Blockchain       │
                        │  (Security & Transparency)    │
                        └─────────────┬────────────────┘
                                      │ trust layer
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
    ┌─────────▼───────────┐ ┌────────▼─────────┐ ┌───────────▼──────────┐
    │  Gyber Social        │ │  GyberComputer   │ │  Gbr Token Economy   │
    │  Platform (GSP)      │ │  (Distributed    │ │                      │
    │                      │ │   Computing)     │ │ ┌──────────────────┐ │
    │ ┌──────────────────┐ │ │                  │ │ │ UnitManager      │ │
    │ │ Project Spaces   │ │ │ ┌──────────────┐ │ │ │ (BSC, Solidity)  │ │
    │ │ Chat / Voice     │ │ │ │ AI Models    │ │ │ ├──────────────────┤ │
    │ │ Video Hosting    │ │ │ │ (AiC Project)│ │ │ │ Project Liquidity│ │
    │ │ File Sharing     │ │ │ │ Compute      │ │ │ │ Pools            │ │
    │ │ G-Plan (Tasks)   │ │ │ │ Services     │ │ │ │ Staking Contracts│ │
    │ │ Reputation       │ │ │ └──────────────┘ │ │ │ Reputation Oracle│ │
    │ │ Shared Spaces    │ │ │                  │ │ └──────────────────┘ │
    │ └──────────────────┘ │ │                  │ │                      │
    └──────────────────────┘ └──────────────────┘ └──────────────────────┘
              │                       │                       │
              └───────────────────────┼───────────────────────┘
                                      │ data layer
                        ┌─────────────▼────────────────┐
                        │           IPFS               │
                        │  (Distributed File Storage)  │
                        │  + Community Pinning Nodes   │
                        └──────────────────────────────┘
```

> 📊 **Professional version:** [View SVG](diagrams/architecture/system_architecture.svg)

*Figure 4.1: GyberExperiment layered architecture showing the governance layer (MacroeconomicDAO with four DAO classes), trust layer (GyberNet Blockchain), application layer (GSP, GyberComputer, Gbr Token Economy), and data layer (IPFS distributed storage).*

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

## 4.3. Gyber Social Platform (GSP): Architecture

### 4.3.1. Overview and Principles

GSP is a social network owned by all users and governed by them through DAO. GSP is not merely a communication tool but the **operating system of CSC** — the environment where the entire project lifecycle (IPI) occurs, SICs form, AGs work, G-Plan functions, and participants' daily interactions take place.

**Architectural principles (following from axioms):**

```
From A1 (decentralization):
  — GSP is a network of nodes, not
    a client-server application
  — Each node contains a set of microservice containers
  — No single point of failure
  — Each participant can deploy their own node

From A3 (data sovereignty):
  — Three levels of data protection:
    Level 1 (basic): server-side encryption
      using client's public key
    Level 2 (enhanced): client-side encryption
      before sending to server
    Level 3 (maximum): full end-to-end
      encryption, server stores only encrypted
      data, keys only with user
  — Even basic level provides optimal protection
  — User has 100% control over their data

From A4 (extensibility):
  — Modular architecture: each user can
    write their own code module
  — Module can be included in node and offered
    to other participants
  — Each node can be augmented with any
    existing modules or new ones
  — Extensibility through GitHub repository
  — System expands in all directions

From A7 (self-governance):
  — Platform code state is determined by
    main branch of GitHub repository
  — Changes to main branch are made
    only through Code DAO voting
  — Each participant can propose changes
    (pull request), but acceptance through DAO

From A8 (cognitive augmentation):
  — AI content moderation: language model
    trained on community rules, classifies
    content in real-time. Model decisions
    are advisory — final decision made
    by Social DAO participants.
    Formally: flag(m) = LLM(m, Rules_DAO) ∈ {ok, review, reject},
    where review → human moderator queue
  — AI recommendations: project, task, and SIC
    recommendation system based on participant
    competency profile. Model runs locally (on-device),
    raw data doesn't leave device (A3)
  — AI participant assistant: contextual helper
    for ecosystem navigation — explaining
    DAO mechanics, helping draft proposals,
    summarizing discussions. Works as interface
    to documentation and on-chain data, without
    access to users' private data
```

## 4.4. GyberNet: Community Blockchain

GyberNet is a secure community blockchain used by the platform to ensure security and transparency of the experiment. GyberNet realizes Axiom A1 (decentralization) and A2 (transparency) at the infrastructure level.

```
Purpose:
  — Ensuring experiment security and transparency
  — Recording critical operations: voting, status
    changes, activity confirmations, document hashes
  — G-Plan data verification
  — Ensuring immutability of DAO decisions
  — Trust layer for entire ecosystem

Current state:
  — In experiment's initial phase, GyberNet functions
    are executed through BNB Smart Chain (BSC),
    providing low fees (~$0.01-0.03 per
    transaction), EVM compatibility, fast block
    time (~3 sec), and developed DeFi infrastructure
  — As experiment develops, GyberNet will be
    deployed as independent community blockchain
  — Migration will be executed through Code DAO voting

Prospective architecture:
  — Consensus: [determined by community through R&D]
  — Compatibility: EVM compatibility for reusing
    existing contracts
  — Validators: ecosystem participants with confirmed
    activity
  — Integration: bridge with BSC, Ethereum and other
    networks for cross-chain interaction
```

## 4.5. GyberComputer: Distributed Computing

GyberComputer is a private distributed computing network of the community, on which necessary functionality for participants' activities is deployed.

```
Purpose:
  — Providing computational resources for ecosystem
    projects without dependence on centralized
    cloud providers
  — Training and using AI models (AiC project)
  — Hosting GSP nodes
  — Ensuring IPFS content pinning
  — Running computationally intensive tasks

Architecture:
  — Network of nodes deployed by community participants
  — Each node provides computational resources
    (CPU, GPU, RAM, storage)
  — Task coordination through smart contracts
    or specialized orchestrator
  — Reward for provided resources
    through Gbr token

Connection to AiC project:
  — AiC (Artificial Intelligence Community) uses
    GyberComputer as computational foundation
  — AI models are trained and deployed in
    decentralized environment
  — DAO contracts regulate access to models,
    their development and reward distribution
  — AGPL licensing ensures openness
    of AI developments
```

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

## 4.8. AiC — Gybernaty Artificial Intelligence Department

### 4.8.1. Status and Role in Ecosystem

AiC (*Artificial Intelligence Community*) is not a separate project among others — it is an **internal department** of Gybernaty Community responsible for one of the key areas of computer science. Artificial intelligence permeates every aspect of community activities: from governance automation and participant activity verification to creating fundamentally new products entering the open market. AI integration into the experiment and everything Gybernaty does is one of the key aspects of community development.

This status fundamentally distinguishes AiC from external AI startups or isolated research labs. AiC is embedded in CSC architecture as its intellectual layer — like a nervous system is embedded in an organism rather than being a separate organ. Each GyberExperiment ecosystem component — GSP, G-Plan, MacroeconomicDAO, GyberComputer, GyberNet — is simultaneously a consumer and supplier of AI solutions.

**AiC Position in CyberSocium Architecture:**

The AiC Department serves as the intellectual layer of the ecosystem, providing AI capabilities to all components (GSP, G-Plan, MacroeconomicDAO, GyberComputer) through two divisions: Research Lab and Applied AI Engineering. These capabilities also extend to the open market through commercial AI products and services.

*See the full AiC architecture diagram at the end of this section.*

### 4.8.2. Problem AiC Solves

The current state of the artificial intelligence industry is characterized by a paradox structurally identical to the Phase 4 (platform capitalism) paradox described in Section 3.3. A technology that by nature is the result of decades of open academic research — from Rosenblatt's perceptron (1958) to Vaswani et al.'s transformers (2017) [51] — is monopolized by a narrow circle of corporations turning public knowledge into proprietary product.

```
Problem structure:

  1. Resource concentration:
     Training frontier models (GPT-4, Gemini, Claude)
     requires $50M–$500M+ computational resources.
     This creates oligopoly: only 5–7 organizations
     worldwide capable of training such models.

  2. Closedness:
     Despite fundamental architectures
     (Transformer, LSTM, CNN) published in open
     papers and implemented in open libraries
     (TensorFlow, PyTorch), final models —
     trained weights, training data, fine-tuning
     methods — are proprietary.

     Source paradox: open science → closed product.

  3. Data control:
     AI models trained on data generated by
     billions of users (text, images,
     interactions). Users receive neither
     control nor compensation for contributing data
     to creating billion-dollar models.

     Direct reproduction of problem described
     in Section 1.3: user data appropriation
     by outdated economic institutions.

  4. Opacity:
     Closed models are black boxes.
     Impossible to verify their safety,
     absence of bias, compliance with claimed
     properties. Direct violation of transparency
     principle (Axiom A2).

  5. Economic inaccessibility:
     Frontier model APIs cost $0.01–$0.06 per 1K tokens.
     For large-scale use (millions of requests)
     this amounts to hundreds of thousands of dollars per year —
     unaffordable for most developers,
     researchers, developing country organizations.

  6. Dependency risk:
     Dependence on closed AI providers creates
     strategic risk: provider can change
     terms, close access, impose censorship.
     This violates Axiom A3 (sovereignty) and Axiom A7
     (self-governance).
```

The open AI movement (Meta's LLaMA, Mistral, Stability AI, EleutherAI) partially addresses problems 2 and 4, but doesn't solve problems 1, 3, 5, and 6 — models remain products of individual corporations or collectives not embedded in sustainable economic systems ensuring long-term financing and democratic governance.

AiC proposes a systemic solution based on CyberSocium theory: **development and use of AI models as public good, financed through PMIP, governed through DAO, and deployed on decentralized GyberComputer infrastructure**.

### 4.8.3. AiC Architecture

```
Three functional circuits:

Circuit 1 — Internal (AI for ecosystem):

  AI integration into all GyberExperiment components.
  Goal: efficiency improvement, automation,
  user experience enhancement.

  Applications:

  GSP:
    — Recommendation systems: news feed
      personalization, project suggestions,
      finding like-minded people
    — Content moderation: automatic spam detection,
      violations, bad behavior without
      centralized censorship
      (federated moderation models)
    — NLP functions: automatic translation
      (critically important for global NFC),
      discussion summarization, extracting
      key decisions from discussions
    — Semantic search across projects,
      documentation, codebase
    — AI assistants for new participants:
      onboarding, ecosystem navigation

  G-Plan:
    — Automatic activity verification:
      analyzing repository commits,
      discussion participation, completed task
      quality — for confirming activity
      when requesting UnitManager reward
    — Task complexity assessment: automatic
      preliminary effort estimation
      based on historical data
    — Optimal task distribution:
      matching participants and tasks based on
      competencies, availability, workload
    — Timeline forecasting: ML models
      for estimating implementation time
      based on project characteristics
      and historical data
    — Risk identification: early detection
      of problematic projects (activity slowdown,
      declining SIC involvement, AG conflicts)

  MacroeconomicDAO:
    — Proposal analysis: automatic
      completeness, consistency,
      realism checking of proposals
    — Social relevance forecasting:
      ML models predicting |SIC(p)|
      based on project characteristics
    — Economic effect simulation:
      modeling proposed decisions' impact
      on tokenomics, liquidity,
      ecosystem growth
    — Anomaly detection: identifying
      suspicious voting patterns
      (sybil attacks, coordinated
      manipulation)
    — Information aggregation for voters:
      automatic discussion summaries,
      pro/con argument visualization

  GyberNet:
    — Network monitoring: anomaly detection
      in blockchain transactions
    — Consensus parameter optimization
    — Predictive load analytics

  GyberComputer:
    — Optimal computational task
      distribution across nodes
    — Predictive resource scaling
    — Node performance monitoring

Circuit 2 — Research (AI science):

  Organizing and conducting fundamental
  and applied AI research.
  Goal: advancing science and creating
  community intellectual potential.

  Directions:
    — Distributed model training
      (federated learning, distributed training)
    — Private machine learning
      (differential privacy, homomorphic encryption
       for training on confidential data)
    — AI alignment and safety
      (open research, critically
       important for society)
    — Efficient architectures for edge devices
      (models running on participant
       devices, without cloud)
    — Multimodal models
      (text, images, audio, video, code)
    — AI for scientific discovery
      (drug discovery, materials science,
       climate modeling — through Economic DAO)

  Organization:
    — Research groups form
      as SIC/AG in IPI model
    — Financing through Economic DAO
      or DUNA grants
    — Results published as open access
      (AGPL for code, CC-BY for papers)
    — Peer review within community
      and in international journals

Circuit 3 — Commercial (AI products):

  Creating AI products and services for
  open market. Goal: generating revenue
  for ecosystem (Loop 2 — liquidity).

  Model:
    — AI products developed through IPI
      (like any ecosystem project)
    — Products use models developed
      in Circuit 2 and Circuit 1 infrastructure
    — Market launch: through Commerce DAO
    — Tokenomics: internal project tokens →
      liquidity pool with Gbr → DEX
    — Client levels:
      external (fiat), special (Gbr),
      super clients (project tokens)

  Examples of potential products:
    — AI platform as service (AIaaS)
      based on GyberComputer
    — Specialized models for verticals:
      medicine, finance, education, law
    — Automation tools for developers
    — AI analytics for blockchain projects
    — Private AI assistants
      (running on user device,
       without sending data to servers)
```

### 4.8.4. AiC Technical Stack

```
Programming languages:
  — Python: primary language for ML/AI
    (TensorFlow, PyTorch, Keras, Scikit-learn,
     OpenCV, Hugging Face Transformers,
     LangChain, JAX)
  — C++: high-performance components,
    inference engines (ONNX Runtime, TensorRT)
  — Rust: safe system components,
    WASM modules for edge inference,
    blockchain infrastructure integration
  — TypeScript: AI integrations in GSP,
    web interfaces for AI tools
  — Solidity: smart contracts for DAO governance
    of AI resources

Frameworks and libraries:
  — Training: PyTorch (primary), TensorFlow, JAX
  — Distributed training: DeepSpeed,
    Megatron-LM, Hivemind,
    PyTorch Distributed
  — Inference: vLLM, TGI, ONNX Runtime,
    llama.cpp, ExLlamaV2
  — Computer Vision: OpenCV, Detectron2,
    Segment Anything
  — NLP: Hugging Face ecosystem, spaCy, NLTK
  — MLOps: MLflow, Weights & Biases, DVC
  — Privacy: PySyft, OpenDP,
    Microsoft SEAL (homomorphic encryption)

Blockchain integration:
  — Ethereum/BSC: DAO contracts for managing
    AI resources and models
  — TON: potential platform for
    AI micropayments (high throughput,
    low fees)
  — Solana: high-performance AI applications
    with on-chain components
  — IPFS/Filecoin: decentralized storage
    of training data and model weights

Licensing:
  — All AiC code: AGPL-3.0
    (guarantees any modifications
     and derivative works remain open)
  — Trained models: open weights
    (license determined for each model
     by Code DAO voting)
  — Research publications: CC-BY-4.0
  — Training data: open datasets
    or data collected with explicit
    participant consent (Axiom A3 — data sovereignty)
```

### 4.8.5. DAO Governance of AI Resources

One of AiC's fundamental innovations is managing AI models and resources through DAO mechanisms. This ensures democratic control over technology that in traditional model is controlled exclusively by corporate management.

```
Decisions made through DAO:

  Code DAO:
    — Accepting architectural decisions
      (choosing base models, frameworks)
    — Merging pull requests into main
      AI code repositories
    — Approving code quality and
      documentation standards
    — Model licensing decisions

  Social DAO:
    — Prioritizing research directions
    — Ethical questions: permissible and impermissible
      AI model applications
    — Data policy: what data used for training,
      how privacy ensured
    — Organizing AI conferences, hackathons,
      educational programs within community

  Commerce DAO:
    — Approving AI products for
      commercial market launch
    — AI service pricing
    — Partnerships with external organizations

  Economic DAO:
    — Financing large research
      programs (training large models,
      GPU acquisition, data collection)
    — Distributing GyberComputer computational
      resources among AiC tasks
    — AI infrastructure investments
```

### 4.8.6. AiC Economic Model

```
Financing sources:

  1. Gybernaty internal budget
     — Allocation from DUNA treasury through
       Economic DAO voting
     — Targeted infrastructure financing
       (GPU clusters, data storage)

  2. Grants and partnerships
     — Decentralized grant programs
       (Ethereum Foundation, Protocol Labs, etc.)
     — Academic partnerships
       with research institutes
     — Corporate partnerships for
       applied AI solutions

  3. Commercial revenue (Circuit 3)
     — AIaaS (AI as a Service) based on
       GyberComputer
     — Specialized model licensing
     — Consulting and AI solution integration
     — Private AI assistants for enterprises

  4. AiC tokenomics
     — Issuing AiC internal token
       through IPI model (Section 3.4)
     — AiC/Gbr liquidity pool on DEX
     — Staking: 10 / [total AiC tokens] %
       of project revenue

**Revenue distribution:**

- 40% → AiC token holders (SIC participants)
- 25% → Operating expenses (infrastructure, GPU, data storage)
- 20% → Research reinvestment (Circuit 2 — AI science)
- 10% → Gybernaty treasury (through Gbr LP)
- 5% → Staking rewards (for AiC token stakers)

**Key mechanism:** all revenue flows through AiC/Gbr liquidity pool, which ensures direct link between AiC success and Gbr ecosystem value — implementing Loop 2 (liquidity) from project lifecycle model.
```

### 4.8.7. CyberSocial Significance of AiC

AiC represents application of cybersocial principles to technology that is likely the most significant for the current era. By demonstrating that advanced AI development can be organized through decentralized, community-governed structures, AiC challenges the assumption that only centralized corporations with massive capital reserves can participate in AI frontier development.

AiC also provides a model for democratic AI system governance — a critically important need in an era when artificial intelligence increasingly shapes economic, social, and political outcomes. Within AiC:

- **Research priority decisions** made through community voting, not corporate board
- **Training data** collected with explicit consent and under participant control (Axiom A3)
- **Trained models** available to all participants and licensed as open (AGPL for code, open weights for models)
- **Commercialization revenue** distributed among participants through transparent smart contracts, not appropriated by shareholders
- **Ethical constraints** established democratically through Social DAO, ensuring public control over AI application

Thus AiC is not merely a technical project but an **institutional innovation** — a new model for organizing development and governance of technologies that determine humanity's future.

### 4.8.8. AiC as Ecosystem Infrastructure AI Layer

The three AiC circuits described above (Internal, Research, Commercial) have another fundamental dimension: AiC is an **infrastructure layer** providing AI augmentation of all cybersocial corporation processes. This is not a separate project alongside GSP, GyberNet and G-Plan — it's a horizontal layer permeating all ecosystem elements.

```
AiC Architectural Position in Ecosystem:

  ┌──────────────────────────────────────────────────┐
  │        Application Level                          │
  │   GSP    G-Plan    GyberNet    Commerce-projects  │
  ├──────────────────────────────────────────────────┤
  │        AiC — AI Infrastructure Layer              │
  │                                                    │
  │  ┌────────────┬────────────┬─────────────────┐    │
  │  │ AI-analyst │ AI-coordi- │ AI-assistant    │    │
  │  │ (E1, SES)  │ nator(PMIP)│ (IPI, FRP)      │    │
  │  ├────────────┼────────────┼─────────────────┤    │
  │  │ AI-auditor │ AI-monitor │ AI-knowledge    │    │
  │  │ (Code DAO) │ (Economic) │ base (E6, accum)│    │
  │  └────────────┴────────────┴─────────────────┘    │
  ├──────────────────────────────────────────────────┤
  │        Blockchain Level (BSC, GyberNet)           │
  │   Governor    UnitManager    Tokens    LP-pools   │
  └──────────────────────────────────────────────────┘
```

**AiC Connection to Theoretical Constructs:**

| Theoretical Element | AiC Function | Result |
|---|---|---|
| Axiom A8 (Cognitive augmentation) | AiC — institutional A8 realization | Democratic AI augmentation control |
| PMIP: C(p) → min | AI coordinator reduces project costs | individual_cost(p \| AI) < individual_cost(p) |
| SES: project selection | AI SR predictor improves selection quality | Directed evolution vs blind |
| E1: collective intelligence | AI analyst compensates cognitive limits | Scaling without quality loss |
| E2: antifragility | AI monitor ensures preventive adaptation | Active antifragility |
| E6: knowledge accumulation | AI knowledge base indexes all experience | Exponential knowledge growth |
| FRP: fork resolution | AI mediator reduces Deliberation cost | FRP from expensive → routine |

**Horizontality principle:** each ecosystem element accesses AiC AI services through standardized API. GSP uses AI for discussion summarization and recommendations. G-Plan uses AI for optimal task assignment and timeline forecasting. GyberNet uses AI for consensus parameter optimization. Commerce projects receive AI code review, security audit and analytics. All AI services follow the division principle (Axiom A8): AI decides, AI informs, AI has no right — depending on task class.

**AI layer economic model:**

```
AiC infrastructure financing:

  1. Basic AI services → financed from treasury
     (public good, available to all participants)

  2. Advanced AI services → freemium model
     (basic access free, extended for Gbr)

  3. Commercial AI products (Circuit 3) →
     revenue returns to ecosystem through
     distribution smart contracts

  This creates self-sustaining cycle:
  AI layer strengthens ecosystem → ecosystem grows →
  more data and resources for AI → AI strengthens →
  ecosystem strengthens even more

  Formally: positive feedback loop 7
  (AI Flywheel):
  quality(AI) ↑ → productivity(CSC) ↑ →
  revenue(ecosystem) ↑ → investment(AiC) ↑ →
  quality(AI) ↑
```

Thus AiC closes the theoretical cycle: Axiom A8 defines AI augmentation *principles*, theoretical sections (PMIP, SES, E1–E6) describe *mechanisms*, and AiC provides *institutional and infrastructure realization*, accountable to community through four-class DAO system.

---

**Contract Addresses (Appendix B Reference):**

- **GyberCommunityToken (Gbr)**: `0xa970cae9fa1d7cca913b7c19df45bf33d55384a9` (BSC)
- **GybernatyUnitManager**: [deployed on BSC, address in repository]
- **Governor Contract**: [to be deployed]
- **Timelock Contract**: [to be deployed]

**GitHub Repositories:**
- GSP: [repository URL]
- G-Plan: [repository URL]
- AiC models: [repository URL]
- Smart contracts: [repository URL]

---

*This translation preserves all technical specifications, smart contract addresses, tokenomics numbers, formulas, and code blocks as required. Section 4 provides complete technical architecture for GyberExperiment implementation of CyberSocium theory.*
