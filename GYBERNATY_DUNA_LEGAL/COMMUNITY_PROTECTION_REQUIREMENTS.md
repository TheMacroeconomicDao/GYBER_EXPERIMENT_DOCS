# COMMUNITY PROTECTION REQUIREMENTS / ТРЕБОВАНИЯ ПО ЗАЩИТЕ ИНТЕРЕСОВ СООБЩЕСТВА
## Gybernaty DUNA — Checklist / Чеклист

---

# ENGLISH VERSION

---

## 1. GOVERNANCE SOVEREIGNTY

- [ ] On-chain governance is the sole and supreme decision-making authority
- [ ] No individual or entity holds discretionary power over Association affairs
- [ ] All governance decisions are binding and automatically executable
- [ ] Smart contract code implements this Agreement (Agreement prevails in conflicts)
- [ ] Governor contract uses snapshot-at-proposal-time to prevent flash loan attacks
- [ ] Voting power delegation does not transfer token ownership
- [ ] Governance parameters modifiable only by governance vote

---

## 2. TOKEN HOLDER RIGHTS

- [ ] One token = one vote (proportional voting power)
- [ ] Right to submit proposals (above threshold)
- [ ] Right to vote on all proposals (For / Against / Abstain)
- [ ] Full treasury oversight and transparency
- [ ] Access to all on-chain transaction data and governance records
- [ ] Right to delegate voting power without losing tokens
- [ ] No lock-up periods or forced transfer restrictions
- [ ] Fixed token supply — explicit prohibition on minting new GBR tokens
- [ ] Exit via open market at any time (free transferability)

---

## 3. TREASURY PROTECTION

- [ ] All crypto assets held in Timelock contract (no individual key holders)
- [ ] Every fund movement requires governance vote + Timelock delay
- [ ] Emergency multisig can only pause, never withdraw
- [ ] Circuit breaker on transactions exceeding threshold
- [ ] Rate limiting on daily/weekly outflows
- [ ] Two-tier fiat system: DAO-controlled Treasury + budget-limited Operating
- [ ] Operating Account balance cap ($20,000)
- [ ] Operating Account single payment cap ($2,000)
- [ ] Monthly Operating Account reporting by Administrator
- [ ] Annual independent financial audit (if treasury >$100k)
- [ ] Real-time public crypto treasury dashboard
- [ ] Quarterly financial statements from Administrator

---

## 4. ADMINISTRATOR CONTROLS

- [ ] Zero discretionary authority — execute only governance-approved actions
- [ ] No access to crypto treasury (no private keys)
- [ ] Cannot initiate expenditures without on-chain approval
- [ ] Cannot block or delay approved governance decisions
- [ ] Cannot enter contracts >$2,000 without governance approval
- [ ] Cannot hire staff without governance approval
- [ ] Cannot speak publicly for Association without authorization
- [ ] 48-hour response SLA to governance instructions
- [ ] 7-day execution SLA for approved fiat payments
- [ ] Monthly expense reporting obligation
- [ ] Immediate termination by governance vote for cause
- [ ] 30-day notice termination without cause
- [ ] Contractual liquidated damages for violations ($10k-$50k)
- [ ] 7-day cure period for non-critical violations
- [ ] Legal protection for refusing unlawful instructions (with written justification)
- [ ] Transition period: DAO-appointed Trusted Executors during Admin vacancy

---

## 5. DAO OPERATIONAL INDEPENDENCE

- [ ] Operations never depend on Administrator presence
- [ ] DAO can appoint Trusted Executors (individuals or companies) via governance vote at any time
- [ ] Trusted Executors can perform any ministerial function (fiat, legal, compliance)
- [ ] Executor authority limited to specific mandate, budget, and duration
- [ ] Executor term max 6 months without re-approval
- [ ] No mandatory requirement to have a permanent Administrator
- [ ] Immediate Executor removal by governance vote

---

## 6. ANTI-ABUSE AND CONFLICT OF INTEREST

- [ ] Mandatory public disclosure of conflicts before vote
- [ ] Mandatory recusal from self-dealing votes >$5,000
- [ ] Independent review for self-dealing transactions >$10,000
- [ ] 48-hour public comment period before self-dealing votes
- [ ] Market rate benchmarking for all compensation
- [ ] Proposal invalidation for undisclosed conflicts
- [ ] Governance-imposed penalties for non-disclosure
- [ ] Prohibition on profit distribution to token holders
- [ ] All compensation classified as "reasonable compensation for services"
- [ ] Buyback & burn explicitly classified as asset management, not profit distribution

---

## 7. GOVERNANCE ATTACK PROTECTION

- [ ] Snapshot-at-proposal-time for voting power (prevents flash loan attacks)
- [ ] Proposal threshold (0.5-1% of supply) prevents spam
- [ ] Timelock delay (24-48h) for all approved proposals — veto window
- [ ] Higher quorum (30-40%) for critical proposals
- [ ] Longer voting period (7-14d) for critical proposals
- [ ] Super-majority (66%) for Agreement amendments
- [ ] Super-majority (75%) for dissolution
- [ ] Emergency multisig subject to on-chain veto within 24-48h
- [ ] LP Burn mechanism rate limited (max N proposals/month)
- [ ] LP Burn minimum threshold ($1,000-$5,000)
- [ ] Anti-sybil: governance pool distributed across 10-50 independent wallets
- [ ] Smart contract upgrade requires 75% approval + 30% quorum + audit

---

## 8. SMART CONTRACT SECURITY

- [ ] Mandatory security audit before deployment (CertiK / OpenZeppelin / Trail of Bits)
- [ ] Re-audit after every contract upgrade
- [ ] Bug bounty program with defined rewards
- [ ] Smart contract insurance (Nexus Mutual or equivalent)
- [ ] Upgradeable contract pattern (UUPS proxy) with governance-only upgrade authority
- [ ] Timelock on all contract upgrades (72h minimum)
- [ ] Emergency pause capability (multisig only, no withdrawal)
- [ ] Rollback plan: governance can disable automation and revert to manual

---

## 9. BLOCKCHAIN CONTINUITY

- [ ] Documented migration plan to alternative EVM chain (Ethereum / Polygon / Arbitrum)
- [ ] Off-chain backup of all governance data and records
- [ ] Force majeure clause covering BSC failure / 51% attack
- [ ] Emergency Multisig authority during >90 day governance disruption
- [ ] Diversification strategy for multi-chain presence (future consideration)

---

## 10. FINANCIAL COMPLIANCE

- [ ] IRS Form 8832 (entity classification) filed
- [ ] Form 990 / 990-N filed annually
- [ ] EIN obtained
- [ ] BOI Report filed with FinCEN within 30 days of formation
- [ ] KYC for all fiat recipients >$600
- [ ] Form 1099-MISC issued for payments >$600
- [ ] W-9 / W-8 collected from grant recipients
- [ ] FATF Travel Rule compliance for transfers >$3,000
- [ ] Blockchain analytics (Chainalysis / Elliptic) for sanctions screening
- [ ] OFAC compliance screening on all transactions
- [ ] Legal opinion on GBR non-security status (Howey Test)
- [ ] Ongoing SEC guidance monitoring

---

## 11. INSURANCE COVERAGE

- [ ] D&O insurance for Administrator and Trusted Executors
- [ ] Smart contract insurance (Nexus Mutual or equivalent)
- [ ] General liability insurance for Association
- [ ] Cyber liability insurance (data breach, hacking, ransomware)
- [ ] Insurance coverage reviewed annually by governance vote
- [ ] Insurance premiums included in annual budget

---

## 12. INTELLECTUAL PROPERTY PROTECTION

- [ ] All IP created for Association owned by Gybernaty DUNA
- [ ] IP Assignment Agreement for all grant recipients and contractors
- [ ] "Gybernaty" trademark registered with USPTO
- [ ] Third-party trademark use requires governance approval
- [ ] Open-source licensing (MIT / Apache 2.0 / GPL) as default
- [ ] Commercial licensing requires governance vote
- [ ] Royalties from licensing flow to Association treasury
- [ ] Defensive patent policy (only against patent trolls)
- [ ] Patent applications require governance vote

---

## 13. DATA PRIVACY AND SECURITY

- [ ] Privacy Policy published
- [ ] GDPR compliance (if processing EU resident data)
- [ ] CCPA compliance (if processing California resident data)
- [ ] Data Protection Officer appointed (if required by GDPR)
- [ ] Data breach notification procedure (72h for GDPR)
- [ ] Minimal data collection principle (only what's legally required)
- [ ] Data retention limit: 12 months after purpose fulfilled
- [ ] On-chain governance pseudonymous (wallet addresses, not identities)
- [ ] API keys stored in decentralized secret management (Threshold Network)
- [ ] API key rotation every 90 days

---

## 14. TRANSPARENCY AND ACCOUNTABILITY

- [ ] All governance votes public and verifiable on-chain
- [ ] All treasury transactions public on blockchain explorer
- [ ] Public governance dashboard
- [ ] Administrator quarterly reports to token holders
- [ ] Annual community report
- [ ] All self-dealing transactions documented with market comparisons
- [ ] Governance forum for proposal discussion before votes
- [ ] IPFS publication of Association Agreement (immutable record)

---

## 15. WHISTLEBLOWER AND DISPUTE RESOLUTION

- [ ] Anonymous whistleblower channel for reporting violations
- [ ] Whistleblower protection against retaliation
- [ ] Internal disputes resolved by governance vote first
- [ ] Mandatory arbitration in Wyoming (AAA rules) for disputes >$10,000
- [ ] Court litigation as last resort (Wyoming state/federal courts)
- [ ] Severability clause (invalid provisions don't void Agreement)

---

## 16. DISSOLUTION PROTECTION

- [ ] Dissolution requires 75% vote + 40% quorum (highest threshold)
- [ ] Assets go to designated nonprofit (not to members)
- [ ] Debts settled before asset distribution
- [ ] Final tax returns filed
- [ ] Smart contracts rendered inoperable (keys burned)
- [ ] Dissolution announcement archived to IPFS

---

## 17. CONTINUITY AND SUCCESSION

- [ ] Key person risk mitigation: no single point of failure in governance
- [ ] Wallet backup procedures documented (seed phrases distributed securely)
- [ ] Administrator transition procedure: DAO-appointed Executors during vacancy
- [ ] Governance operational if individual contributors depart
- [ ] Knowledge base and documentation maintained for operational continuity

---

## COVERAGE STATUS (updated after Agreement v1.1 amendments)

**Fully covered in ASSOCIATION_AGREEMENT v1.1:**
Sections 1-7, 10-14, 16-17

**Added in v1.1:**
- Fixed supply guarantee (§3.2) — covers Section 2
- Admin transition + DAO-appointed Executors (§6.4) — covers Section 5 and 17
- Data breach notification procedure (§11.6) — covers Section 13
- Insurance section (§16) — covers Section 11

**Remaining items for future versions:**
- Section 8 (Smart Contract Security): bug bounty program not formalized in Agreement
- Section 9 (Blockchain Continuity): migration plan not in Agreement
- Section 15 (Whistleblower): mechanism not in Agreement

---

---

# РУССКАЯ ВЕРСИЯ

---

## 1. СУВЕРЕНИТЕТ УПРАВЛЕНИЯ

- [ ] Ончейн-управление является единственным и высшим органом принятия решений
- [ ] Ни одно лицо или организация не обладает дискреционными полномочиями над делами Ассоциации
- [ ] Все решения управления обязательны к исполнению и выполняются автоматически
- [ ] Код смарт-контрактов реализует настоящее Соглашение (при конфликтах Соглашение имеет приоритет)
- [ ] Governor-контракт использует снэпшот на момент создания предложения для предотвращения flash loan атак
- [ ] Делегирование голосов не передаёт право собственности на токены
- [ ] Параметры управления изменяются только через голосование

---

## 2. ПРАВА ДЕРЖАТЕЛЕЙ ТОКЕНОВ

- [ ] Один токен = один голос (пропорциональная голосующая сила)
- [ ] Право подавать предложения (при достижении порога)
- [ ] Право голосовать по всем предложениям (За / Против / Воздержался)
- [ ] Полный надзор за казначейством и прозрачность
- [ ] Доступ ко всем ончейн-данным транзакций и записям управления
- [ ] Право делегировать голоса без потери токенов
- [ ] Отсутствие периодов блокировки или принудительных ограничений на передачу
- [ ] Фиксированная эмиссия — явный запрет на минтинг новых GBR токенов
- [ ] Выход через открытый рынок в любое время (свободная передача токенов)

---

## 3. ЗАЩИТА КАЗНАЧЕЙСТВА

- [ ] Все крипто-активы хранятся в Timelock-контракте (ни у кого нет индивидуальных ключей)
- [ ] Каждое перемещение средств требует голосования + задержку Timelock
- [ ] Экстренный мультисиг может только поставить на паузу, не выводить средства
- [ ] Автоматический выключатель при транзакциях, превышающих порог
- [ ] Ограничение скорости на дневные/недельные оттоки
- [ ] Двухуровневая фиатная система: DAO-контролируемый Treasury + Operating с лимитами
- [ ] Лимит баланса Operating Account ($20,000)
- [ ] Лимит разового платежа Operating Account ($2,000)
- [ ] Ежемесячная отчётность Administrator по Operating Account
- [ ] Ежегодный независимый финансовый аудит (при казначействе >$100k)
- [ ] Публичный дашборд крипто-казначейства в реальном времени
- [ ] Ежеквартальная финансовая отчётность от Administrator

---

## 4. КОНТРОЛЬ НАД АДМИНИСТРАТОРОМ

- [ ] Нулевые дискреционные полномочия — исполнение только одобренных governance действий
- [ ] Нет доступа к крипто-казначейству (нет приватных ключей)
- [ ] Не может инициировать расходы без ончейн-одобрения
- [ ] Не может блокировать или задерживать одобренные решения
- [ ] Не может заключать контракты >$2,000 без одобрения governance
- [ ] Не может нанимать персонал без одобрения governance
- [ ] Не может публично выступать от имени Ассоциации без авторизации
- [ ] SLA ответа на инструкции governance — 48 часов
- [ ] SLA исполнения одобренных фиатных платежей — 7 дней
- [ ] Обязанность ежемесячной отчётности по расходам
- [ ] Немедленное увольнение голосованием при наличии оснований
- [ ] Увольнение без причины с уведомлением за 30 дней
- [ ] Договорные штрафные санкции за нарушения ($10k-$50k)
- [ ] 7-дневный период исправления для некритических нарушений
- [ ] Правовая защита за отказ от исполнения незаконных инструкций (с письменным обоснованием)
- [ ] Переходный период: доверенные исполнители DAO на время вакансии Admin

---

## 5. ОПЕРАЦИОННАЯ НЕЗАВИСИМОСТЬ DAO

- [ ] Операции никогда не зависят от наличия Administrator
- [ ] DAO может в любой момент назначить доверенных исполнителей (физлица или компании) через голосование
- [ ] Доверенные исполнители могут выполнять любые министериальные функции (фиат, юридические, комплаенс)
- [ ] Полномочия исполнителя ограничены конкретным мандатом, бюджетом и сроком
- [ ] Максимальный срок полномочий исполнителя — 6 месяцев без повторного одобрения
- [ ] Нет обязательного требования иметь постоянного Administrator
- [ ] Немедленное отстранение исполнителя голосованием

---

## 6. ПРОТИВОДЕЙСТВИЕ ЗЛОУПОТРЕБЛЕНИЯМ И КОНФЛИКТ ИНТЕРЕСОВ

- [ ] Обязательное публичное раскрытие конфликтов перед голосованием
- [ ] Обязательный самоотвод от голосований по self-dealing >$5,000
- [ ] Независимая проверка self-dealing транзакций >$10,000
- [ ] 48-часовой период публичных комментариев перед голосованиями по self-dealing
- [ ] Бенчмарк по рыночным ставкам для всех компенсаций
- [ ] Аннулирование предложения при нераскрытом конфликте
- [ ] Санкции governance за нераскрытие
- [ ] Запрет на распределение прибыли держателям токенов
- [ ] Вся компенсация классифицирована как «разумное вознаграждение за услуги»
- [ ] Buyback & burn явно классифицирован как управление активами, а не распределение прибыли

---

## 7. ЗАЩИТА ОТ АТАК НА УПРАВЛЕНИЕ

- [ ] Снэпшот голосующей силы на момент создания предложения (защита от flash loan атак)
- [ ] Порог предложения (0.5-1% от supply) предотвращает спам
- [ ] Задержка Timelock (24-48ч) для всех одобренных предложений — окно вето
- [ ] Повышенный кворум (30-40%) для критических предложений
- [ ] Увеличенный период голосования (7-14 дн.) для критических предложений
- [ ] Суперквалифицированное большинство (66%) для изменений Соглашения
- [ ] Суперквалифицированное большинство (75%) для роспуска
- [ ] Экстренный мультисиг подлежит ончейн-вето в течение 24-48ч
- [ ] Механизм LP Burn с ограничением частоты (макс. N предложений/месяц)
- [ ] Минимальный порог LP Burn ($1,000-$5,000)
- [ ] Анти-сибил: governance pool распределён по 10-50 независимым кошелькам
- [ ] Обновление смарт-контрактов требует 75% одобрения + 30% кворум + аудит

---

## 8. БЕЗОПАСНОСТЬ СМАРТ-КОНТРАКТОВ

- [ ] Обязательный аудит безопасности перед деплоем (CertiK / OpenZeppelin / Trail of Bits)
- [ ] Повторный аудит после каждого обновления контракта
- [ ] Программа Bug Bounty с определёнными наградами
- [ ] Страхование смарт-контрактов (Nexus Mutual или аналог)
- [ ] Обновляемый паттерн контракта (UUPS proxy) с полномочиями обновления только через governance
- [ ] Задержка Timelock на все обновления контрактов (минимум 72ч)
- [ ] Возможность экстренной паузы (только мультисиг, без вывода средств)
- [ ] План отката: governance может отключить автоматизацию и вернуться к ручному режиму

---

## 9. НЕПРЕРЫВНОСТЬ РАБОТЫ БЛОКЧЕЙНА

- [ ] Задокументированный план миграции на альтернативную EVM-сеть (Ethereum / Polygon / Arbitrum)
- [ ] Офчейн-резервное копирование всех данных управления и записей
- [ ] Пункт о форс-мажоре, покрывающий отказ BSC / атаку 51%
- [ ] Полномочия экстренного мультисига при прерывании governance >90 дней
- [ ] Стратегия диверсификации для мультичейн-присутствия (рассмотрение в будущем)

---

## 10. ФИНАНСОВЫЙ КОМПЛАЕНС

- [ ] Подана IRS Form 8832 (классификация организации)
- [ ] Form 990 / 990-N подаётся ежегодно
- [ ] Получен EIN
- [ ] BOI Report подан в FinCEN в течение 30 дней с момента регистрации
- [ ] KYC для всех фиатных получателей >$600
- [ ] Form 1099-MISC выпущена для платежей >$600
- [ ] W-9 / W-8 собраны у получателей грантов
- [ ] Соблюдение Travel Rule FATF для переводов >$3,000
- [ ] Блокчейн-аналитика (Chainalysis / Elliptic) для санкционного скрининга
- [ ] OFAC-скрининг всех транзакций
- [ ] Юридическое заключение о несекьюритизном статусе GBR (Howey Test)
- [ ] Постоянный мониторинг рекомендаций SEC

---

## 11. СТРАХОВОЕ ПОКРЫТИЕ

- [ ] D&O страхование для Administrator и доверенных исполнителей
- [ ] Страхование смарт-контрактов (Nexus Mutual или аналог)
- [ ] Страхование общей ответственности Ассоциации
- [ ] Страхование кибер-ответственности (утечки данных, хакинг, вымогательство)
- [ ] Ежегодный пересмотр страхового покрытия голосованием governance
- [ ] Страховые премии включены в годовой бюджет

---

## 12. ЗАЩИТА ИНТЕЛЛЕКТУАЛЬНОЙ СОБСТВЕННОСТИ

- [ ] Вся ИС, созданная для Ассоциации, принадлежит Gybernaty DUNA
- [ ] Договор об уступке ИС для всех получателей грантов и подрядчиков
- [ ] Товарный знак «Gybernaty» зарегистрирован в USPTO
- [ ] Использование товарного знака третьими лицами требует одобрения governance
- [ ] Open-source лицензирование (MIT / Apache 2.0 / GPL) по умолчанию
- [ ] Коммерческое лицензирование требует голосования governance
- [ ] Роялти от лицензирования поступают в казначейство Ассоциации
- [ ] Оборонительная патентная политика (только против патентных троллей)
- [ ] Патентные заявки требуют голосования governance

---

## 13. КОНФИДЕНЦИАЛЬНОСТЬ И БЕЗОПАСНОСТЬ ДАННЫХ

- [ ] Политика конфиденциальности опубликована
- [ ] Соответствие GDPR (при обработке данных резидентов ЕС)
- [ ] Соответствие CCPA (при обработке данных резидентов Калифорнии)
- [ ] Назначен ответственный за защиту данных (DPO) (при требовании GDPR)
- [ ] Процедура уведомления об утечке данных (72ч для GDPR)
- [ ] Принцип минимального сбора данных (только законодательно необходимые)
- [ ] Срок хранения данных: 12 месяцев после исполнения цели сбора
- [ ] Ончейн-управление псевдонимное (адреса кошельков, не личности)
- [ ] API-ключи хранятся в децентрализованном управлении секретами (Threshold Network)
- [ ] Ротация API-ключей каждые 90 дней

---

## 14. ПРОЗРАЧНОСТЬ И ПОДОТЧЁТНОСТЬ

- [ ] Все голосования публичны и верифицируемы ончейн
- [ ] Все транзакции казначейства публичны в блокчейн-эксплорере
- [ ] Публичный дашборд управления
- [ ] Ежеквартальные отчёты Administrator держателям токенов
- [ ] Ежегодный отчёт для сообщества
- [ ] Все self-dealing транзакции задокументированы с рыночными сравнениями
- [ ] Форум управления для обсуждения предложений перед голосованиями
- [ ] Публикация Association Agreement в IPFS (неизменяемая запись)

---

## 15. ИНФОРМАТОРЫ И РАЗРЕШЕНИЕ СПОРОВ

- [ ] Анонимный канал для сообщений о нарушениях
- [ ] Защита информаторов от преследования
- [ ] Внутренние споры разрешаются голосованием governance в первую очередь
- [ ] Обязательный арбитраж в Вайоминге (правила AAA) для споров >$10,000
- [ ] Судебное разбирательство как крайняя мера (суды штата/федеральные суды Вайоминга)
- [ ] Пункт о делимости (недействительные положения не отменяют Соглашение)

---

## 16. ЗАЩИТА ПРИ РОСПУСКЕ

- [ ] Роспуск требует 75% голосов + 40% кворум (наивысший порог)
- [ ] Активы передаются назначенной НКО (не участникам)
- [ ] Долги погашаются до распределения активов
- [ ] Подаются финальные налоговые декларации
- [ ] Смарт-контракты становятся неработоспособными (ключи сожжены)
- [ ] Объявление о роспуске архивируется в IPFS

---

## 17. НЕПРЕРЫВНОСТЬ И ПРЕЕМСТВЕННОСТЬ

- [ ] Снижение риска ключевых лиц: нет единой точки отказа в управлении
- [ ] Процедуры резервного копирования кошельков задокументированы (seed phrases распределены безопасно)
- [ ] Процедура перехода Administrator: доверенные исполнители DAO на время вакансии
- [ ] Управление работоспособно при уходе отдельных контрибьюторов
- [ ] База знаний и документация поддерживаются для операционной непрерывности

---

## СТАТУС ПОКРЫТИЯ (обновлено после правок Agreement v1.1)

**Полностью покрыто в ASSOCIATION_AGREEMENT v1.1:**
Разделы 1-7, 10-14, 16-17

**Добавлено в v1.1:**
- Гарантия фиксированной эмиссии (§3.2) — покрывает Раздел 2
- Переход Admin + доверенные исполнители DAO (§6.4) — покрывает Разделы 5 и 17
- Процедура уведомления об утечке данных (§11.6) — покрывает Раздел 13
- Секция страхования (§16) — покрывает Раздел 11

**Оставшиеся пункты для будущих версий:**
- Раздел 8 (Безопасность смарт-контрактов): программа bug bounty не формализована в Agreement
- Раздел 9 (Непрерывность блокчейна): план миграции отсутствует в Agreement
- Раздел 15 (Информаторы): механизм отсутствует в Agreement

---

**Document Version / Версия документа:** 1.1
**Created / Создан:** 2026-02-16
**Purpose / Назначение:** Comprehensive checklist of community protection requirements for Gybernaty DUNA / Полный чеклист требований по защите интересов сообщества Gybernaty DUNA
