---
title: "DAO Taxonomy — Four-Class Model"
description: "Overview of the four classes of decentralized decision-making"
---

## 5. DAO Taxonomy: Four-Class Model of Decentralized Decision-Making

A distinguishing feature of GyberExperiment's governance architecture is the **four-class DAO taxonomy** — a structured classification of decentralized governance mechanisms that accounts for different categories of collective decision-making. This taxonomy reflects the recognition that not all decisions are identical in nature and that different types of decisions may require different governance processes, participation criteria, and execution mechanisms.

### 5.1 Social DAO (Social DAOs)

#### 5.1.1 Purpose

Social DAOs govern the **internal social life of the community** — decisions about community norms, social events, membership policies, communication standards, dispute resolution procedures, and other matters concerning the community as a social entity rather than as an economic or technical enterprise.

#### 5.1.2 Scope

Social DAO decisions include, but are not limited to:

- Organization of community events (conferences, hackathons, meetups, educational programs)
- Establishment and modification of community codes of conduct
- Decisions about community communication channels and platforms
- Membership and participation policies
- Recognition and rewards for contributions to community life
- Cultural and educational initiatives

#### 5.1.3 Characteristics

- **Low economic stakes:** Social DAO decisions typically do not involve significant financial resources (though may include distribution of small budgets for events).
- **Broad participation:** All community members can participate in Social DAO governance, reflecting the principle that social decisions should reflect the broadest consensus.
- **Simple majority:** Most Social DAO decisions can be approved by simple majority vote, given their relatively low stakes and reversibility.
- **High frequency:** Social decisions arise frequently in the community's daily life, requiring lightweight governance processes that do not create excessive burden.

### 5.2 Code DAO (Code DAOs)

#### 5.2.1 Purpose

Code DAOs govern the **community's technical infrastructure** — specifically, the DSP platform codebase and other common technical assets. The current state of the platform's code is defined by the state of the main branch of the GitHub repository, and changes to this branch require passage through the Code DAO process.

#### 5.2.2 Scope

Code DAO decisions include:

- Merging proposed code changes (pull requests) into the main branch
- Approving new modules for inclusion in the standard node configuration
- Selecting technical standards and architectural patterns
- Evaluating and approving security-critical changes
- Managing deprecation and removal of obsolete components
- Resolving technical disputes between competing implementations

#### 5.2.3 Characteristics

- **Technical competence requirement:** Voting in Code DAO may be weighted by technical reputation — participants with confirmed development contributions have greater weight in technical decisions. This reflects the principle that technical decisions should be determined by technical expertise while remaining transparent and contestable.
- **Review process:** Code DAO proposals typically include a mandatory technical review period during which qualified community members examine proposed changes for correctness, security, performance, and architectural consistency.
- **Meritocratic governance:** While any community member can propose code changes, voting power on technical matters is concentrated among those who have demonstrated relevant competence through contribution history.
- **Awareness of irreversibility:** Code changes in production systems can have significant consequences. Code DAO processes include mechanisms for phased deployment, testing requirements, and rollback procedures.
- **Continuous AI security audit (from A8):** Every pull request affecting smart contracts (Solidity/Vyper) automatically passes through an AI audit pipeline before being admitted to Code DAO voting. The pipeline includes:

```
AI Audit Pipeline (AiC implementation, Circuit 1):

  Git Push → CI/CD (GitHub Actions) → AI scanning:
    │
    │  Tools:
    │    — Octane Security: CI/CD-native analysis,
    │      exploitable vulnerability detection
    │    — Sherlock AI: analysis during writing,
    │      directed remediation
    │    — AuditAgent (Nethermind): attack scenario
    │      simulation based on real audits
    │
    ├─ Critical vulnerability →
    │    merge blocking + alert to ArchDev + Core
    ├─ Warning →
    │    PR comment + mandatory review
    └─ Clean →
         admission to Code DAO voting

  Deployed contracts → continuous monitoring
  of anomalous transaction patterns → alerts
  to Gnosis Safe signers
```

AI audit does not replace human review but complements it: models detect patterns that humans might miss, while humans evaluate context and business logic unavailable to the model. Audit parameters (sensitivity thresholds, list of checked vulnerabilities) are determined by Code DAO voting.

### 5.3 Commerce DAO (Commercial DAOs)

#### 5.3.1 Purpose

Commerce DAOs implement the concept of **decentralized crowdinvesting** — allowing entrepreneurs and enthusiasts within the community to propose business ideas or formal business plans for implementation using the community's collective resources, providing investors the opportunity to receive a share of the resulting profits.

#### 5.3.2 Scope

Commerce DAO decisions include:

- Evaluation and approval of proposed commercial projects
- Determination of internal token issuance and sale terms
- Determination of profit distribution schemes between implementers and investors
- Approval of partnerships and client agreements
- Project budget management and financial reporting
- Decisions about project continuation, modification, or termination based on results

#### 5.3.3 Characteristics

- **Economic stakes:** Commerce DAO decisions involve significant financial resources and economic risk. Governance processes are correspondingly more stringent.
- **Due diligence:** Commerce DAO proposals undergo a structured evaluation process including market analysis, technical feasibility assessment, financial projections, and risk assessment.
- **Investor protection:** Smart contracts governing Commerce DAO projects include mechanisms for fund custody, milestone-based staged release, transparent accounting, and (in certain circumstances) refunds.
- **Performance accountability:** Commercial projects are subject to regular performance reporting with defined metrics and benchmarks. Sustained unsatisfactory performance can trigger management actions, including leadership changes or project restructuring.

#### 5.3.4 Relationship to IPI Model

Commerce DAOs are the governance layer for phases 3-5 of the project lifecycle (Accumulation, Implementation, Functioning) for projects with commercial objectives. They operationalize the concept of the social-investment circle for revenue-generating projects.

### 5.4 Economic DAO (Economic DAOs)

#### 5.4.1 Purpose

Economic DAOs represent a **fundamentally new concept for organizing public financing, project management, and socio-economic interaction.** They ensure the accumulation of social, financial, and economic resources for the most effective implementation of any relevant public projects — including projects whose scale and ambition exceed the capabilities of traditional financing mechanisms.

#### 5.4.2 Distinction from Commerce DAO

While Commerce DAOs focus on individual commercial projects with defined profit models, Economic DAOs address **systemic economic decisions** affecting the community as a whole:

- Management of community treasury
- Resource allocation across multiple projects and initiatives
- Strategic investments in infrastructure, research, and capacity building
- Inter-community economic agreements and partnerships
- Gbr ecosystem monetary policy (e.g., decisions about staking parameters, liquidity provision, token burning)
- Long-term economic planning and resource allocation

#### 5.4.3 Characteristics

- **Highest economic stakes:** Economic DAO decisions affect the economic well-being and long-term viability of the entire community. Governance processes are the most stringent in the taxonomy.
- **Qualified majority requirement:** Critical Economic DAO decisions may require qualified majority approval (e.g., 67% or 75%) to ensure broad consensus before committing public resources.
- **Extended discussion periods:** Economic DAO proposals undergo extended discussion periods allowing thorough analysis and debate before voting begins.
- **Expert input:** Economic DAO governance may include advisory mechanisms — expert analysis, simulation results, historical precedent review — to inform the decision-making process while maintaining the principle that final decisions are made by the community through voting.
- **Systemic risk management:** Economic DAOs are responsible for monitoring and managing systemic risks to the community economy — excessive concentration in specific projects, liquidity risks, dependencies on specific external systems, and other threats to the ecosystem's economic health.
- **AI Treasury Advisor (from A8):** Economic DAO uses an AI agent to inform economic decisions:

```
AI Treasury Advisor (AiC implementation, Circuit 1):

  On-chain Analytics Agent:
    — Real-time economic flow monitoring:
      LP positions, trading volumes, TVL,
      token distribution, concentration
    — Visualization: integration with Dune Analytics

  Risk Assessment:
    — Systemic risk evaluation:
      Risk(ecosystem) = f(concentration, liquidity,
                          correlation, external_deps)
    — Early warning when approaching
      critical thresholds

  Simulation Engine (cadCAD):
    — Modeling consequences of economic
      proposals before voting:
      "if burn 5% of treasury → impact
       on liquidity, Gbr price, TVL"
    — Monte Carlo simulation on GyberComputer

  AI Treasury Advisor informs, does not decide:
  all analysis results are published as
  supplements to Economic DAO proposals,
  final decision rests with participants
```

#### 5.4.4 MacroeconomicDAO as Meta-Governance

**MacroeconomicDAO** functions as the meta-governance layer, coordinating the activities of the four DAO classes. It is the institutional expression of the community's collective economic intelligence — the mechanism through which the community exercises conscious, purposeful management of its socio-economic system.

MacroeconomicDAO is not a centralized authority overriding individual DAO decisions. Rather, it is a governance space where inter-class issues are resolved, resource allocation among DAO classes is coordinated, and the overall trajectory of the experiment is directed by the collective will of active participants.

**AI-enhanced DAO governance (from A8).** To counteract voter fatigue and cognitive overload as the community scales, all four DAO classes use AiC AI services:

- **AI proposal summarizer:** For each proposal, a structured summary is generated — essence, risks, economic consequences, arguments for/against. Participants receive an objective summary before voting, not replacing but complementing discussion.
- **Consequence simulator:** Before voting on economically significant proposals, modeling results are shown: impact on treasury, liquidity, GyberComputer load, SES parameters. Implementation via cadCAD on GyberComputer.
- **AI discussion summarization:** Automatic discussion summary with main arguments from both sides — for participants who cannot follow discussion in real time. Reduces barrier to informed participation (A6).

### 5.5 DAO Interaction and Conflict Resolution

The four DAO classes are not isolated from each other. Decisions in one class often have consequences for others:

- A Code DAO decision to adopt a new technical architecture may have economic consequences (costs, performance, scalability) requiring Economic DAO consideration
- A Commerce DAO project may require social coordination (community engagement, marketing) falling under Social DAO competence
- An Economic DAO decision about resource allocation may affect Commerce DAO project priorities

When inter-class conflicts arise, resolution follows a structured escalation process:

1. **Informal coordination:** Representatives of affected DAOs discuss the issue in common communication spaces, seeking consensus.
2. **Joint proposal:** If informal coordination produces a solution, it is formalized as a joint proposal submitted for ratification to the relevant DAOs.
3. **MacroeconomicDAO arbitration:** If informal coordination fails, the issue is escalated to MacroeconomicDAO for system-wide discussion and resolution.

```
Inter-class interaction model:

  ┌─────────────────────────────────────────────┐
  │          MacroeconomicDAO                    │
  │      (meta-governance, arbitration)          │
  └──────────────────┬──────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
  ┌─────▼─────┐ ┌───▼────┐ ┌────▼──────┐
  │  Social   │ │  Code  │ │ Commerce  │
  │   DAO     │◄┤  DAO   ├►│   DAO     │
  │           │ │        │ │           │
  └─────┬─────┘ └───┬────┘ └────┬──────┘
        │            │           │
        └────────────┼───────────┘
                     │
              ┌──────▼──────┐
              │  Economic   │
              │    DAO      │
              │ (systemic   │
              │  decisions) │
              └─────────────┘

  Interaction flows:
    Social ↔ Code: technical decisions with social consequences
    Social ↔ Commerce: marketing, engagement, social responsibility
    Code ↔ Commerce: technical implementation of commercial products
    Economic ↔ all: financing, resource allocation, monetary policy
    MacroeconomicDAO → all: arbitration, strategic direction
```

> 📊 **Professional version:** [View SVG](diagrams/process/fork_resolution.svg)

*Figure 5.1: Inter-class interaction model showing how the four DAO classes coordinate through MacroeconomicDAO. Arrows indicate interaction flows: Social ↔ Code (technical decisions with social consequences), Social ↔ Commerce (marketing, engagement), Code ↔ Commerce (technical implementation), Economic ↔ all (financing, resource allocation), and MacroeconomicDAO → all (arbitration, strategic direction).*

---

## 6. Applied Ecosystem: From Theory to Implementation

The theoretical constructs outlined in preceding sections find practical embodiment in concrete software products, protocols, and services comprising the GyberExperiment applied ecosystem. Each ecosystem element implements one or more principles of cybersocial economics, and collectively they form a fully functional environment for decentralized socio-economic interaction.

### 6.1 GSP — GyberSocial Platform (Decentralized Social Platform)

GSP is the ecosystem's central hub — a decentralized social platform providing infrastructure for all forms of participant interaction.

```
GSP Architecture:

  ┌──────────────────────────────────────────────┐
  │              GSP — Layers                     │
  ├──────────────────────────────────────────────┤
  │                                              │
  │  User layer:                                 │
  │    — Participant profiles (verification      │
  │      via digital signature)                  │
  │    — News feeds (aggregation                 │
  │      from project spaces)                    │
  │    — Reputation system (integration          │
  │      with UnitManager and G-Plan)            │
  │    — Direct communication (P2P encryption)   │
  │                                              │
  │  Project layer:                              │
  │    — Project spaces (for each                │
  │      IPI model project)                      │
  │    — Discussion catalogues                   │
  │    — Voting systems (integration             │
  │      with Governor contracts)                │
  │    — Task tracking (G-Plan)                  │
  │                                              │
  │  Infrastructure layer:                       │
  │    — Distributed storage (IPFS)              │
  │    — Blockchain integration (BSC, Ethereum)  │
  │    — P2P network (libp2p)                    │
  │    — End-to-end encryption                   │
  │                                              │
  │  Technology stack:                           │
  │    — Frontend: React/Next.js, TypeScript     │
  │    — Backend: Node.js, Rust (core modules)   │
  │    — Protocol: ActivityPub-compatible        │
  │    — Storage: IPFS + local cache             │
  │    — Identification: DID (Decentralized      │
  │      Identifiers) + Verifiable Credentials   │
  └──────────────────────────────────────────────┘
```

**AI personalization with data sovereignty (from A8, A3).**
GSP implements intelligent content personalization without violating user data sovereignty. Formally:

```
Let u ∈ U be a participant, D(u) their local data
(interaction history, preferences, subscriptions).

Personalization model M(u) is trained exclusively
on the user's device (on-device inference):

  M(u) : D(u) → R(u),

where R(u) is personalized content ranking.

Confidentiality invariant:
  ∀ u ∈ U : D(u) ∩ Server_Storage = ∅

No ecosystem server stores or processes
raw user data. On the server side, only
aggregated, anonymized signals are used
(federated aggregation):

  M_global = FedAvg({∇M(u₁), ∇M(u₂), ..., ∇M(uₙ)})

The global model improves through federated learning
(Flower framework), where only gradients,
not data, are transmitted from devices.
```

This fundamentally distinguishes GSP from Web2 platforms, where personalization is built on centralized collection and monetization of user data. In GSP, personalization is a user tool, not a tool for extracting value from the user.

GSP differs from traditional social platforms fundamentally: data belongs to users (Axiom A3), platform code is open (AGPL-3.0), governance is through Code DAO and Social DAO, and monetization is based on creating value for participants, not extracting value from their data.

### 6.2 GyberNet — Decentralized Network

GyberNet represents dedicated blockchain infrastructure ensuring transparency and immutability of all ecosystem transactions.

```
GyberNet Functions:

  — Transaction registry: all ecosystem economic
    operations are recorded on-chain
  — Smart contract execution environment:
    Governor, Timelock, UnitManager
  — DNS-like system: decentralized
    name resolution for projects and participants
  — Cross-network interaction: bridges
    to BSC, Ethereum, TON, Solana
  — Validation: Proof-of-Stake with reputational
    weight (active participants receive
    validation priority)

Technology stack:
  — Consensus: modified BFT
    (Byzantine Fault Tolerant)
  — Virtual machine: EVM-compatible
  — Contract language: Solidity, Vyper
  — Network layer: libp2p
  — State storage: Merkle Patricia Trie
```

### 6.3 GyberComputer — Distributed Computing Network

GyberComputer is a distributed network of computing nodes provided by community participants for executing resource-intensive tasks: training AI models, rendering, scientific computing.

```
GyberComputer Architecture:

  Participant nodes:
    — Provide computing resources
      (CPU, GPU, RAM, storage)
    — Receive Gbr rewards
      proportional to resources provided
    — Verification via Proof-of-Computation

  Task scheduler:
    — Task distribution across nodes
      accounting for available resources
    — Prioritization based on DAO voting
    — Fault tolerance: duplication
      of critical computations

  AiC integration:
    — Providing GPU power for
      model training (Circuit 1)
    — Distributed inference for
      AI services (Circuit 3)
    — Federated learning without
      raw data transmission

  Technology stack:
    — Orchestration: Kubernetes + custom
      Rust scheduler
    — Communication: gRPC, Protocol Buffers
    — Containerization: Docker, WASM
    — Monitoring: Prometheus, Grafana

  AI Compute Orchestrator (from A8):
    — Predictive Scheduling: ML model
      (Reinforcement Learning, PPO/SAC)
      predicts optimal task distribution
      across nodes accounting for latency,
      power, and availability
    — Anomaly Detection: early detection
      of node failures through metric analysis
      (Prophet/DeepAR) before computation loss
    — Auto-scaling: predictive scaling
      based on usage patterns —
      resource allocation before peak load
    — Proof-of-Computation Verification:
      AI verifies computation correctness,
      critical for federated learning (AiC)
```

### 6.4 G-Plan — Task Management and Activity Verification System

G-Plan is an integrated task management system that simultaneously serves as the activity verification mechanism for participants in the UnitManager system.

```
G-Plan Functions:

  Task management:
    — Creating, assigning, tracking tasks
      within IPI model projects
    — Task hierarchy: epics → stories → tasks
    — Binding to project milestones
    — Cross-project dependencies

  AI Task Orchestrator (from A8):
    — Decomposition: AI agent analyzes
      IPI model project specifications
      and proposes breakdown into tasks
      with complexity estimates and dependencies
    — Assignment: recommending executors
      based on competence profile, current
      load, and execution history
    — Predictive Analytics: forecasting
      completion dates, early warning
      of delay risks
    — Cross-project Dependency Resolver:
      identifying dependencies between tasks
      of different projects, order optimization
    — All AI Task Orchestrator recommendations
      are proposals: assignment approval
      rests with project leader

  Activity verification:
    — Recording completed tasks on-chain
    — Task confirmation by participants
      with higher status
    — Generating activity reports
      for UnitManager
    — Wallet classification algorithm:
      active / inactive

  Reputation system integration:
    — Task completion quality affects
      reputational weight
    — Reputation affects voting weight
      in Code DAO and Commerce DAO
    — Continuous verification:
      participant who stops activity
      loses right to rewards

  AI task quality verification (from A8):
    — Automatic quality assessment of completed
      tasks before human confirmation:
      Q(task) = AI_Review(deliverable, spec, context)
      Q ∈ [0, 1], where Q < θ_min → return for revision,
      Q ≥ θ_min → forward for review to participant
      with higher status
    — AI does not replace human confirmation
      but serves as first filter: reduces
      reviewer load and ensures basic control
      (spec compliance, completeness, formatting)
    — Threshold θ_min determined by Code DAO voting

  Sybil detection and farming protection (from A8):
    — Graph Neural Network analyzes wallet
      interaction graph, detecting clusters
      of coordinated/fake accounts:
      Sybil(wallet_cluster) = GNN(G_interactions)
    — Anomaly detection identifies atypical
      patterns: task wash trading, mass
      creation of identical tasks, suspicious
      confirmation chains
    — Proof of Personhood (ZK-cryptography):
      proof of "one person — one account"
      without revealing personal data (A3)
    — Sybil analysis results are advisory:
      final blocking decision made by Social DAO
```

### 6.5 LQD, SAPP, PowerSwapMeta, Contact — Auxiliary Ecosystem Projects

Beyond the main platform components, the GyberExperiment ecosystem includes several applied projects implemented or being implemented through the IPI model:

**LQD (Liquidity Deployer):**
- Automated deployment of liquidity pools for project tokens
- Integration with major DEXs (PancakeSwap, Uniswap)
- Customizable parameters: initial price, liquidity depth, LP-lock strategy
- LP Burn mechanism for initiating Accumulation phase (burning 0.1% of budget in Gbr)

**SAPP (Social Application Protocol Platform):**
- Protocol for creating decentralized social applications on top of GSP
- Developer SDK: API, widgets, templates
- Application marketplace managed by Commerce DAO
- Monetization through internal application tokens

**PowerSwapMeta:**
- DEX aggregator optimizing ecosystem token swaps
- Meta-transactions: users don't pay gas directly
- Integration with multiple blockchains (BSC, Ethereum, Polygon)
- Automatic routing through pools with best liquidity

**Contact:**
- Decentralized contact and identity management system
- Integration with DID (Decentralized Identifiers)
- Portable identity: one profile for all ecosystem projects
- Privacy: zero-knowledge proofs for verification without data disclosure

### 6.6 Portfolio Validation and Ecosystem Integration

All applied ecosystem components are connected by a unified economic circuit:

```
Ecosystem economic circuit:

  Participant
    │
    ├─► G-Plan: completes tasks → activity verified
    │     │
    │     └─► UnitManager: receives Gbr rewards
    │           │
    │           └─► Gbr token: used for
    │                 │
    │                 ├─► Voting in DAO
    │                 ├─► Staking (passive income)
    │                 ├─► Project investments (Commerce DAO)
    │                 └─► Service access (GyberComputer, AiC)
    │
    ├─► GSP: participates in social life
    │     │
    │     └─► Reputation: grows with activity → increases
    │           voting weight in DAO
    │
    └─► IPI projects: invests / works
          │
          └─► Project tokens → LP with Gbr → DEX
                │
                └─► Revenue → distribution via
                      smart contracts
```

This integration ensures implementation of all eight axioms:

| Axiom | Implementation in ecosystem |
|---|---|
| A1 (Decentralization) | P2P GSP architecture, distributed GyberComputer, multisig management |
| A2 (Transparency) | On-chain transactions in GyberNet, open code (AGPL-3.0) |
| A3 (Data sovereignty) | DID identification, IPFS storage, E2E encryption |
| A4 (Expandability) | Modular architecture, SAPP protocol, open APIs |
| A5 (Meritocratic fairness) | UnitManager, G-Plan verification, reputation system |
| A6 (Inclusivity) | PMIP (minimal participation threshold), multilingual, cross-chain |
| A7 (Self-governance) | Four-class DAO taxonomy, Governor contracts |
| A8 (Cognitive augmentation) | AiC (three circuits), federated learning, AI audit, AI summarization, human-in-the-loop for critical decisions |

---

**End of Sections 5 & 6 Translation**

*Translation of CyberSocium Foundation document*
*Original version: Russian, 2025*
*Translation: English, 2026*
