---
title: "Gyber Social Platform"
description: "Decentralized social platform architecture"
---

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
