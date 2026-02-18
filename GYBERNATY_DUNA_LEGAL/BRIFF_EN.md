# Gybernaty DUNA — Comprehensive Brief

**Full Brief: Registration of Gybernaty DUNA with Absolute Community Control via Tokens and On-Chain Treasury Governance**

---

## 1. Overall Objective

Establish a legally recognized structure (Decentralized Unincorporated Nonprofit Association, DUNA) in the State of Wyoming that enables the community (Gybernaty Community) to maintain full and unconditional control over all DAO assets and governance, while:

- Organizers and Administrator (Director) are external nominal parties responsible only for administrative and fiat operations
- All decisions, including financial operations from the crypto treasury and fiat payments, are made exclusively through on-chain voting by governance token holders
- The community controls 80%+ of tokens (distributed across community wallets for regulatory protection) and, consequently, all votes
- The Administrator has no right to initiate or block any operations without corresponding governance approval; their role is technical execution of approved decisions (fiat payments, taxes, compliance)

---

## 2. Legal Form: Wyoming DUNA

**Rationale for Choice:**

- DUNA (Decentralized Unincorporated Nonprofit Association) — legal form created in 2024 specifically for DAOs, recognizing on-chain governance
- Allows exclusion of fiduciary duties for members, enabling full reliance on code and voting
- Limits liability of participants (community members) for DAO obligations
- Suitable for protocols that may generate revenue (fees) but do not distribute it as dividends (revenue is reinvested or used for token buybacks)

**Registration Requirements:**

- File Articles of Organization with Wyoming Secretary of State
- Name must include "DUNA" suffix
- Include Notice of Restrictions on Duties
- Specify public identifier of governance smart contract (Governor contract address)

---

## 3. Roles and Limitations

| Role | Executor | Authority | Limitations | Community Control |
|------|----------|-----------|-------------|-------------------|
| **Organizer** | Nominal individual/service (registered agent) | File formation documents | No post-formation management rights or asset access | None |
| **Administrator (Director / Ministerial Agent)** | External company (legal/accounting firm) | • Open and maintain DUNA fiat bank accounts<br>• Sign tax returns (Form 8832, 990-N) and interact with IRS<br>• Receive official notices (court summons)<br>• Execute fiat payments approved by vote (e.g., AWS, legal fees)<br>• Maintain accounting and compliance (KYC of grant recipients) | • Cannot initiate any expenses without prior on-chain governance approval<br>• No access to crypto treasury (no keys)<br>• Cannot block or delay execution of approved decisions (penalty: termination by vote) | Gybernaty Community controls all Administrator actions via governance vote. Non-compliance leads to immediate replacement |
| **Token Holders (Gybernaty Community)** | Multiple independent community participants, each with their own keys | • Collective ownership of GBR governance tokens (distributed across dozens of independent wallets)<br>• Initiate and vote on all proposals<br>• Control crypto treasury via Governor + Timelock mechanism<br>• Receive compensation (salary/grants) from DUNA for services | • Participants with >25% control must disclose themselves in BOI Report (FinCEN)<br>• Are not formal directors or DUNA employees | — |

---

## 4. Mechanisms of Absolute Control

### 4.1. Token-Based Governance

- Governance token GBR (BEP-20 standard) deployed on BNB Smart Chain. Contract address: `0xa970cae9fa1d7cca913b7c19df45bf33d55384a9`
- Entire initial supply (100%) is under control of Gybernaty Community
- For regulatory protection and effective voting efficiency, tokens are distributed as follows:
  - **Governance pool (~80%+)**: Distributed across dozens of community wallets used for on-chain voting. Each wallet pays minimal fees (~$0.01-0.03) for voting on BSC
  - **Trading float (~20% or less)**: Listed on DEX (PancakeSwap) for liquidity and price discovery
- Technical implementation: master wallet (or group of trusted community wallets) delegates voting rights to child addresses via BEP-20 token delegation mechanism

### 4.2. Mechanisms for Legal Value Extraction

- **Salary / Compensation for Services**: Community members enter into service agreements with DUNA (e.g., "strategic guidance", "technical development"). Compensation amount approved by vote. This is "reasonable compensation" permitted by law
- **Research Grants**: DUNA awards grants to community members (or their teams) for new product development / research
- **Buyback & Burn**: If the protocol generates revenue (fees), DUNA may direct funds to buy back GBR governance tokens from DEX and subsequently burn them. This is a deflationary mechanism for maintaining token value — NOT profit distribution as dividends, but "protocol liquidity management operation"

**IMPORTANT**: Association Agreement must explicitly state that buyback & burn is a protocol liquidity management mechanism, not profit distribution among participants, to avoid token classification as a security.

All these operations proceed through voting and automatic execution (crypto portion) or through the Administrator (fiat portion).

---

## 5. Treasury Structure and Blockchain Architecture

### 5.1. Blockchain and Technical Infrastructure

| Parameter | Value |
|---|---|
| **Network** | BNB Smart Chain (BSC) |
| **Token** | GBR (BEP-20) |
| **Contract Address** | `0xa970cae9fa1d7cca913b7c19df45bf33d55384a9` |
| **Governor contract** | To be deployed on BSC (OpenZeppelin Governor or equivalent) |
| **Timelock contract** | To be deployed on BSC (standard Timelock) |
| **Emergency Multisig** | Gnosis Safe on BSC |

**Why BNB Smart Chain:**
- Low fees (~$0.01-0.03 per transaction) — critical for model with dozens of voting wallets
- EVM compatibility — can use proven OpenZeppelin contracts
- Fast block time (~3 sec) — responsive voting
- Developed DeFi ecosystem (PancakeSwap for liquidity)

### 5.2. Treasury Architecture

**Crypto Treasury:**
- All DUNA assets (GBR, BNB, stablecoins) stored in Timelock contract
- Any fund movement possible only after approval through Governor contract
- Execution delay (Timelock delay): **[TBD — requires discussion: 24h, 48h, 7d?]**
- Emergency multisig: **[TBD — requires configuration]**

**Fiat Treasury — Two-Tier System:**

**1. Treasury Fiat Account — DAO-Controlled:**
- **Provider:** Bridge (https://bridge.xyz) or Circle Business Account
- **Control:** Programmatically via API, controlled by governance through Chainlink Functions
- **Access:** No one has direct access, all operations only via on-chain governance vote
- **Purpose:**
  - Primary fiat treasury for DUNA
  - Large payments (>$5,000)
  - Transfers to Operating Account
- **Operations:**
  - Receive crypto and automatic conversion to USD
  - Wire transfers per governance-approved payments
  - Transfers to Operating Account (monthly budget)

**2. Operating Fiat Account — Administrator-Managed:**
- **Provider:** Traditional US bank (Mercury, SVB, or Wyoming local bank)
- **Control:** Administrator as sole signatory
- **Access:** Administrator can make payments within approved budget
- **Purpose:**
  - Routine small expenses (<$5,000)
  - Operational payments (hosting, SaaS, office expenses)
  - Emergency expenses (within limits)
- **Funding:** Governance votes on transfer from Treasury Account (e.g., $10k/month)
- **Limits:**
  - Maximum balance: $20,000 (excess returned to Treasury Account)
  - Maximum payment without additional approval: $2,000

**Division of Responsibilities:**
- **DAO controls:** Treasury Account (primary funds, large payments)
- **Administrator controls:** Operating Account (only operational expenses within budget)
- **Transparency:** Administrator reports monthly on all Operating Account expenses

**Crypto-to-Fiat Conversion — APPROVED MODEL:**

**Phase 1 (Launch, first 6-12 months):**
- **Minimize fiat:** Maximum expenses paid in crypto (BitPay, Coinbase Commerce for hosting/SaaS)
- **For fiat operations:** Administrator manually converts via MoonPay/Binance
- **Volume:** <$5,000/month fiat operations
- **Accounts:** Only Operating Account (traditional bank)

**Phase 2 (6-12 months, after treasury >$100k):**
- **Open Bridge Business Account** with API (Treasury Fiat Account)
- **Develop Automation Contract** on BSC with Chainlink Functions for:
  - Automatic crypto→USD conversion via Bridge API
  - Programmatic wire transfers per governance decisions
  - Automatic transfers to Operating Account (monthly budget)
- **Development cost:** ~$10,000-20,000 (approved by governance vote)

**Phase 3 (12+ months, full automation):**
- **90%+ operations without human:**
  - Governance vote → Timelock → Chainlink Oracle → Bridge API → wire transfer
  - Monthly automatic Operating Account replenishment
- **Administrator needed only for:**
  - Operating Account management (small expenses)
  - Compliance and tax matters
  - Emergency situations

**Technical Architecture (Phase 2-3):**

```
Governance Vote (on-chain)
    ↓
Timelock Contract (BSC)
    ↓
Automation Contract (BSC)
    ↓
Chainlink Functions (Oracle)
    ↓
Bridge/Circle API (off-chain)
    ↓
Treasury Fiat Account (USD)
    ↓
Wire Transfer / Operating Account Transfer
```

**API Key Security:**
- Bridge API keys stored in **Threshold Network** (decentralized secret storage)
- Smart contract obtains temporary access via threshold signature
- No one holds complete key (distributed key management)

**Benefits of Two-Tier System:**
- ✅ DAO retains control over primary funds (Treasury Account)
- ✅ Administrator can operationally pay small bills (Operating Account)
- ✅ Risk minimization — Operating Account has limits
- ✅ Automation of large payments without human intermediary
- ✅ Transparency — all operations logged on-chain or in monthly reports

---

## 6. Governance Parameters

**[Note: Specific values require community discussion and approval]**

| Parameter | Description | Recommended Value | Status |
|---|---|---|---|
| **Voting Delay** | Time between proposal creation and voting start | 1-2 days | TBD |
| **Voting Period** | Voting duration | 3-7 days | TBD |
| **Quorum** | Minimum % of tokens for vote validity | 10-20% of total supply | TBD |
| **Proposal Threshold** | Minimum tokens to create proposal | 0.5-1% of total supply | TBD |
| **Timelock Delay** | Execution delay after approval | 24-48 hours | TBD |

**Proposal Types:**
- **Routine operations** (grants <$10k, small expenses) — standard parameters
- **Critical decisions** (Administrator replacement, Governor contract changes, large expenses >$50k) — higher quorum **[TBD]**

**On-Chain Voting:**
- **Fully on-chain voting (Governor Bravo / OpenZeppelin Governor)**
  - All voting occurs on BSC via Governor smart contract
  - Each community wallet calls `castVote()` function directly on blockchain
  - After voting ends, approved transactions automatically queued in Timelock
  - After Timelock delay expires — executed automatically
  - Full transparency and autonomy without intermediaries

**Rationale:**
- Dozens of wallets (not thousands) — manageable quantity
- BSC with minimal fees makes on-chain voting accessible
- Absolute community control requires maximum transparency
- Automatic execution without human factor

---

## 7. Tokenomics and Value Maintenance

### 7.1. GBR Token Distribution

- **Governance pool (~80%+)**: Dozens of Gybernaty Community wallets for on-chain voting (largely stable community stabilization fund)
- **Trading float (~20% or less)**: On DEX (PancakeSwap) for liquidity and pricing
- **Total supply**: ✅ **Fixed supply** (all supply already minted, no new tokens will be created — deflationary model)
- **Transferability**: ✅ **Freely transferable tokens** (freely transferable, standard BEP-20)

**CRITICAL**: Freely tradeable tokens + buyback & burn require legal opinion to confirm GBR is not a security under Howey Test. Budget for legal opinion: $5,000-15,000.

**SEC Security Classification Protection:**
- Association Agreement explicitly states: "GBR tokens do NOT entitle holders to dividends or profit distributions"
- Buyback & burn structured as "asset management operation to maintain protocol liquidity", not profit distribution
- Tokens used for governance (utility), not investment (speculation)
- Obtain written legal opinion from securities law specialist

### 7.2. DEX Liquidity Pool — APPROVED MODEL

| Parameter | Solution |
|----------|---------|
| **DEX** | PancakeSwap v2 (possible migration to v3 after 6-12 months via governance vote) |
| **Trading Pairs** | GBR/BNB (50% liquidity) + GBR/USDT (50% liquidity) |
| **LP Provider** | **DUNA only** — exclusive base liquidity provider |
| **Locked Liquidity** | Team.Finance, locked for 12 months with renewal via governance vote |
| **Initial Capital** | $50,000-100,000 from DUNA treasury (approved by governance vote) |

**Rationale for 50/50 Distribution:**
- **GBR/BNB (50%)**: Primary trading pair for BSC users, high volumes
- **GBR/USDT (50%)**: Stable USD pricing, simplifies buyback & burn operations, less Impermanent Loss

**Liquidity Mechanism:**

1. **DUNA as Sole LP Provider:**
   - DUNA (via Timelock contract) deposits GBR + BNB/USDT into PancakeSwap v2
   - Receives LP tokens (CAKE-LP GBR-BNB and CAKE-LP GBR-USDT)
   - Trading fees (0.25% on v2) accumulate in LP position → DUNA treasury revenue
   - LP tokens managed via governance (add/remove liquidity only by vote)

2. **Locked Liquidity:**
   - LP tokens locked via Team.Finance for **12 months**
   - Public page with timer for transparency (rug pull protection)
   - After expiration, governance vote: renew for another 12 months or change strategy
   - Lock creates investor confidence and confirms project seriousness

3. **UNIQUE MECHANISM: LP Burn for Project/Research Initialization**

   **Concept (implemented in smart contracts, currently in testing):**
   
   Gybernaty community participants can **initiate new projects, research, or critical votes** via **LP token burning** mechanism as proof-of-commitment:

   **How it works:**
   - Community participant creates own LP position (GBR + BNB/USDT) on PancakeSwap
   - Receives LP tokens
   - **Burns LP tokens** via special Gybernaty contract
   - LP token burning **proves serious intent** (irreversible financial stake)
   - After burn, participant gains right to initiate:
     * New research project
     * Product development proposal
     * Critical governance vote (if participant lacks sufficient GBR tokens for Proposal Threshold)
   
   **Why burn LP instead of simply staking GBR?**
   - LP burn = **irreversible commitment** (cannot recover)
   - Spam and frivolous proposal filter
   - Participant stakes not only GBR but also BNB/USDT → double stake
   - On burn, liquidity remains in pool forever (deepens market), burner loses their share → benefit to entire ecosystem
   
   **Usage Example:**
   - Participant wants to launch research on new swarm intelligence algorithm
   - Creates LP position of $5,000 (GBR + BNB)
   - Burns LP tokens via contract
   - Gains right to submit proposal for $30,000 grant from DUNA (even with insufficient GBR for Proposal Threshold)
   - Community votes — if approved, participant receives grant
   - If rejected — burner lost $5,000 but deepened liquidity for all
   
   **Abuse Protection:**
   - Minimum LP burn threshold (e.g., $1,000-5,000)
   - Governance can set limit on LP burn proposals per month
   - Participants with successful project history may receive LP burn exemption (whitelist)

   **Status:** Contracts already implemented and testing. Will deploy with main governance infrastructure after audit.

**Benefits of "DUNA-Only LP" Model:**
- ✅ Full community control over liquidity via governance
- ✅ All trading fees go to DUNA treasury (revenue for operations and buyback)
- ✅ Guaranteed market depth (not dependent on individual LPs)
- ✅ Transparency — all liquidity visible on-chain, managed via Timelock
- ✅ LP burn mechanism creates unique economics for project initiation

### 7.3. Token Value Maintenance Mechanisms

- **Buyback**: DUNA directs portion of revenue (if any) to buy GBR from DEX
- **Burn**: Bought tokens are burned, reducing total supply
- **Effect**: With stable demand, reduced supply → price increase

**IMPORTANT**: Buyback & burn must be structured as "protocol liquidity management operation", NOT profit distribution, to avoid token classification as security.

---

## 8. Additional Critical Aspects

### 8.1. Intellectual Property (IP)

- **IP Ownership**: Who owns code, "Gybernaty" brand, domains?
  - If DUNA — need Assignment Agreement
  - If community — need license for DUNA use
- **Trademarks**: "Gybernaty" registration with USPTO (optional, for brand protection)
- **Code Licensing**: Open source (MIT, Apache) or proprietary?

### 8.2. Compliance and AML/KYC

- **Grant Recipient KYC**: Administrator must conduct KYC for all payment recipients >$600 (IRS Form 1099 requirement)
- **Wallet Screening**: Use Chainalysis or Elliptic to check incoming/outgoing transactions (required for bank account opening)
- **Travel Rule**: Transfers >$3,000 require recipient information disclosure (FATF)

### 8.3. Insurance

- **D&O Insurance**: Administrator liability insurance (lawsuit protection)
- **Smart Contract Insurance**: Nexus Mutual or equivalents for contract bug coverage
- **General Liability**: DUNA general insurance

### 8.4. Dissolution Procedure

- What happens when voting for DUNA dissolution?
- **Nonprofit Requirements**: Assets cannot be distributed to participants, must transfer to another nonprofit organization or charitable foundation
- Dissolution approval procedure: higher quorum (e.g., 66%)

### 8.5. Audit and Reporting

- **Smart Contracts**: Audit Governor, Timelock, Token contracts before launch (CertiK, OpenZeppelin, Trail of Bits)
- **Financial Reporting**: Quarterly or annual?
- **Public Dashboard**: On-chain treasury data (Dune Analytics or custom)
- **Annual Report**: Mandatory Form 990 (IRS) + public community report

---

## 9. Tax and Regulatory Obligations

**Beneficial Owners:** Any community participant with >25% control must file BOI Report (FinCEN). If no participant exceeds 25% — must report persons with 'substantial control' (senior officers, important decision-makers). Non-disclosure penalties are criminal.

**DUNA:** Files tax returns (Form 8832 for status election, then Form 990-N or other). DUNA income (if any) is subject to corporate income tax (or chosen regime). Expenses (salaries, grants) reduce taxable base.

**Community Participants (Personal Taxes):** Salaries and grants received by participants from DUNA are subject to income tax according to each participant's tax residency.

**Administrator:** Responsible for timely filing of returns and payment of DUNA taxes, but all decisions about hiring tax consultants and expenses are made via governance vote.

---

## 10. Budget and Launch Costs

**Legal Expenses:**
- DUNA registration in Wyoming: ~$100-200
- Registered Agent (annual): ~$50-150/year
- Legal firm (Association Agreement preparation, contracts): ~$5,000-15,000
- EIN acquisition: free
- BOI Report filing: free (can file independently)

**Operating Expenses (annual):**
- Administrator (accounting, compliance)
- Tax consultants
- Insurance (D&O, General Liability)
- Hosting, domains, infrastructure

---

## 11. Roadmap (Next Steps)

**Stage 1: Legal Structuring**

- Find and hire legal firm specializing in Wyoming DUNA
- Develop:
  - Association Agreement with key provisions (vote bindingness, Administrator role limitations, fiduciary duty exclusion)
  - Administrator contract (Ministerial Agent Agreement) with clear duties and penalties
  - Service agreement template with community members (for grants and compensation)
- Identify Administrator candidate (company/individual) and agree on terms

**Stage 2: DUNA Registration**

- Select nominal organizer (registered agent service)
- Prepare and file Articles of Organization specifying:
  - Name (e.g., "Gybernaty DUNA")
  - Notice of Restrictions on Duties
  - Governance smart contract address (can specify later or placeholder)
- Obtain EIN from IRS

**Stage 3: Technical Implementation**

- Develop and deploy smart contracts:
  - Governance Token (ERC-20) with delegation function
  - Governor contract with parameters (voting period, quorum)
  - Timelock contract
  - (Optional) contracts for distributing tokens across multiple wallets
- Configure multisig (Gnosis Safe) for emergencies (keys with trusted community members)
- Create voting interface (website / Snapshot)

**Stage 4: Launch and Initial Actions**

- Conduct vote on Association Agreement approval (off-chain signing by all parties)
- Vote on Administrator appointment and contract approval
- Vote on approval of initial grants and compensation to community members
- Administrator opens fiat bank account for DUNA
- File BOI Report (FinCEN) specifying persons with 'substantial control' over DUNA
- Transfer initial assets (crypto) to treasury (Timelock)

---

## 12. Risks and Mitigation

| Risk | Mitigation |
|---|---|
| **Administrator refuses to execute governance decision** | Immediate termination via vote, replacement; contractual liability; financial penalties in contract |
| **Loss of access to community token wallets** | Token distribution across dozens of wallets with seed phrase backups; multisig use; documented recovery procedure |
| **SEC regulatory claims that tokens are securities** | Token distribution among dozens of wallets, no dividends, utility emphasis (governance), legal opinion (Howey Test analysis), clear buyback structuring as "liquidity management" |
| **Bank refuses to open DUNA account** | Use crypto-friendly banks: Mercury, Relay, Wyoming Community Bank, or small local Wyoming banks; prepare detailed compliance package. **IMPORTANT**: Silvergate and Signature Bank closed (2023) |
| **Smart contract bugs** | Mandatory audit by leading firms (CertiK, OpenZeppelin, Trail of Bits); use standard, proven OpenZeppelin contracts; bug bounty program |
| **Wyoming DUNA law changes** | Monitor legislation; adapt structure if necessary (e.g., transition to LLC or other form) |
| **Treasury hack (smart contract or multisig)** | Timelock delay for all operations (minimum 24-48h); emergency multisig for pause function; smart contract insurance (Nexus Mutual); regular security audits |
| **Conflict of interest: community votes for own salaries/grants** | Public disclosure of all self-dealing transactions; salary size limitation to "reasonable compensation"; independent review (optional — advisory board); transparent reporting |
| **Regulator (IRS) challenges nonprofit status** | Strict compliance with nonprofit rules (no asset distribution, serving public benefit); legal structuring of buyback as asset operation, not dividends; consultations with tax attorney |
| **BSC shutdown or 51% attack** | Diversification: develop migration plan to another EVM-compatible network (Ethereum, Polygon, Arbitrum); off-chain governance data backups |

---

## Conclusion

The proposed structure fully meets Gybernaty Community requirements:

- Absolute control via tokens distributed across multiple Gybernaty Community wallets
- Legal bindingness of governance vote decisions for Administrator
- Automatic crypto transaction execution via Governor + Timelock
- Fiat operations limited to vote-approved payments only, with instant Administrator replacement capability
- Legal value extraction by participants via service salaries, research grants, and buyback & burn mechanism

This brief serves as foundation for further work with lawyers and developers. Let's proceed with implementation.

---

**Document Version:** 1.0  
**Created:** 2026-02-16  
**Language:** English  
**Russian Version:** See BRIFF.md
