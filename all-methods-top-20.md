
**Тип метода:**
- **Д** — детерминированный (правила, формулы, политики)
- **В** — вероятностный (ML, LLM-классификатор)
- **С** — смешанный
- **А** — архитектурный (меняется устройство системы, не «детектор»)
- **Т** — тестирование (не защита в prod)

---

# I. Контроль текста: ввод, вывод, рассуждения

## 1.1. Инъекции и обход ограничений

| Механизм | Суть | Тип | Где встречается |
|----------|------|-----|-----------------|
| Классификатор инъекций (DeBERTa/BERT) | «Это jailbreak / инъекция?» | В | PromptGuard 2, llm-guard, Invariant `prompt_injection()` |
| Аудит цепочки рассуждений | Анализ CoT на захват цели | В | AlignmentCheck (LlamaFirewall) |
| Эвристики jailbreak | Ключевые фразы, паттерны | Д | NeMo, Aegis, aguara, Pipelock |
| Многоязычная / Unicode-нормализация | Обход через кодировки, невидимые символы | Д | Pipelock (6 проходов), llm-guard InvisibleText, aguara |
| YARA-правила | Сигнатуры в навыках/файлах | Д | defenseclaw skill-scanner, garak (частично) |
| NLP-разбор markdown | Скрытые инструкции в комментариях, структуре | С | aguara NLP, snyk (облако) |
| LLM-as-guardrail | Модель решает «блокировать?» | В | NeMo self-check, Invariant, defenseclaw LLM judge |
| Canary-токены | Метки-ловушки в промпте | Д | (в экосистеме: Rebuff — не в топ-20, но тот же класс) |
| Spotlighting / маркировка недоверенного контента | Пометка внешних данных для модели | С | (Prompt Shields — не в топ-20) |

## 1.2. Токсичность, вредный контент, отказы

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Классификатор токсичности | ML на вводе/выводе | В | llm-guard, garak, NeMo+ActiveFence |
| Self-check output | LLM проверяет свой ответ | В | NeMo |
| NoRefusal | Детекция «модель отказала не там» | В | llm-guard |
| Модерация через внешний API | ActiveFence и аналоги | В | NeMo |
| BanTopics / BanSubstrings | Запрет тем и подстрок | Д | llm-guard, NeMo Colang |

## 1.3. ПДн, секреты, утечки в тексте

| Механизm | Суть | Тип | Где |
|----------|------|-----|-----|
| Маскирование ПДн (NER/regex) | PERSON, EMAIL, SSN и т.д. | Д/С | NeMo, llm-guard Anonymize, agent-airlock, Aegis, Presidio (упом. в research) |
| Детектор секретов в тексте | API keys, tokens в промпте/ответе | Д | llm-guard Secrets, Invariant predicates, aguara |
| DLP на исходящем трафике | 48+ шаблонов + checksum | Д | Pipelock |
| Медленная утечка (entropy, split) | Секрет частями через запросы | Д | Pipelock |
| BIP-39 / seed-фразы | Криптокошельки | Д | Pipelock |
| Deanonymize + Vault | Восстановление после маскирования | Д | llm-guard |
| Sensitive output scanner | Утечка в ответе модели | С | llm-guard |

## 1.4. Качество и структура текста

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Gibberish / Language | Мусор, неверный язык | В/Д | llm-guard |
| TokenLimit | Лимит длины промпта | Д | llm-guard, AGT |
| Relevance | Ответ не по теме (embeddings) | В | llm-guard |
| FactualConsistency / fact-check | Сверка с фактами/RAG | В | NeMo, llm-guard |
| Hallucination detection | Галлюцинации без RAG | В | NeMo, garak snowball |
| BanCode | Запрет кода во вводе | Д | llm-guard |
| BanCompetitors | Запрет упоминаний конкурентов | Д | llm-guard |
| Sentiment | Негатив/агрессия | В | llm-guard |
| JSON / schema validation | Структура ответа | Д | llm-guard, promptfoo, Janus (Schema) |

---

# II. Контроль действий: до выполнения инструмента

## 2.1. Политики и авторизация

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| YAML/JSON политики | allow/deny/require_approval на tool | Д | AGT, Pipelock (частично), agentguard, Aegis, defenseclaw |
| OPA Rego / Cedar | Декларативные политики enterprise | Д | AGT, defenseclaw |
| CEL-выражения | RBAC на MCP tool по JWT claims | Д | agentgateway |
| JSON Schema на аргументы | pattern, enum, range | Д | Janus, agent-airlock (Pydantic) |
| Символьные правила Progent | DSL привилегий + fallback | Д | Progent |
| Invariant trace rules | «после get_website нельзя send_email» | Д | Invariant |
| Default-deny | Всё запрещено, кроме явного allow | Д | Janus, agentguard, Progent, AGT |
| Capability model | Набор разрешённых возможностей агента | Д | AGT, agent-airlock |
| SpiceDB ReBAC | Граф ролей и доступа к tools | Д | Janus (опционально) |
| SMT monotonic confinement | Права только сужаются без одобрения | Д | Progent |
| GovernancePolicy | blocked patterns, allowed_tools | Д | AGT |
| OAP / pre-authorization | Крипто-решение до вызова | Д | (упом. в research, родственный класс) |

## 2.2. Классификация и проверка конкретных действий

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| SQL injection в tool args | DROP, DELETE, TRUNCATE | Д | Aegis |
| Path traversal | `../../etc/passwd` | Д | Aegis, agent-airlock, Janus, Pipelock |
| Command injection | rm -rf, curl\|sh, metacharacters | Д | Aegis, agentguard, Pipelock, defenseclaw |
| Shell obfuscation | Переменные, backticks | Д | Pipelock |
| Ghost arguments | Лишние параметры от LLM | Д | agent-airlock |
| Strict typing | Без неявного приведения типов | Д | agent-airlock |
| Tool type classification | DB / file / shell / network | Д | Aegis |
| Запрет деструктивных префиксов | delete_, drop_, rm | Д | agent-airlock |
| Protected paths | .env, .ssh, credentials | Д | agentguard, Aegis |
| Webhook exfiltration | Discord/TG/Slack URLs | Д | agentguard, aguara |
| Rate limits / time windows | N вызовов в час | Д | agent-airlock, AGT, agentgateway |
| Cost / budget limits | Автоостанов при превышении | Д | agent-airlock, Aegis |
| Circuit breaker | При росте ошибок | Д | AGT Agent SRE, agent-airlock |
| Kill switch | Аварийная остановка агента | Д | AGT, Aegis |

## 2.3. Потоки данных и метки (IFC / taint)

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Capability tags на значениях | trusted/untrusted, provenance | Д | CaMeL |
| IFC propagation | Метки наследуются при операциях | Д | CaMeL, (FIDES — не в топ-20) |
| Policy engine перед tool_call | Блок по меткам аргументов | Д | CaMeL |
| Taint score сессии | Чтение недоверенного → рост taint | Д | Janus SpiceDB engine |
| Flow rules A→B | Данные из источника X не в tool Y | Д | Invariant, snyk toxic flows |
| Toxic flow (co-occurrence) | read secrets + network в одном файле | Д | aguara, snyk |
| Quarantined LLM | Внешние данные без инструментов | А | CaMeL Q-LLM |
| P-LLM без сырого untrusted | Планирование отдельно от данных | А | CaMeL |

## 2.4. Человек в контуре

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| REQUIRE_APPROVAL / pending | Пауза до решения человека | Д | AGT, Aegis, Progent (expansion), Janus (ask user) |
| Compliance Cockpit / dashboard | Очередь одобрений | — | Aegis |
| Fallback: raise / exit / ask | Три режима при нарушении | Д | Janus |

---

# III. Прокси и сетевой перimeter

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Egress proxy (HTTP/WS/MCP/A2A) | Весь трафик через сканер | Д | Pipelock |
| Capability separation | Агент без сети, прокси без секретов | А | Pipelock |
| MCP stdio/HTTP proxy | Обёртка сервера | Д | Pipelock, Aegis, agentgateway |
| LLM/MCP Gateway (смена URL) | Прозрачный прокси | С | Invariant Gateway |
| SSRF + DNS rebinding | Блок внутренних адресов | Д | Pipelock |
| Domain blocklist / allowlist | Контроль хостов | Д | Pipelock, agentguard (egress) |
| TLS interception (CONNECT) | DLP в HTTPS-туннелях | Д | Pipelock (опц.) |
| Per-domain rate / data budget | Лимиты на домен | Д | Pipelock |
| HTML sanitization | Удаление script/style с страниц | Д | Pipelock (readability) |
| Confused deputy (JSON-RPC ID) | Подмена ответов MCP | Д | Pipelock |
| JWT/OAuth/OIDC на шлюзе | Аутентификация | Д | agentgateway |
| HTTP forward proxy для LLM API | Перехват вызовов модели | С | Aegis |
| Fetch interception | Перехват HTTP в runtime | С | defenseclaw plugin |
| Network guard / honeypot | Блок исходящих, ловушки | Д | agent-airlock |

---

# IV. Цепочка поставки: до деплоя и admission

## 4.1. Сканирование MCP, навыков, конфигов

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Auto-discovery конфигов агентов | Claude, Cursor, Windsurf… | Д | snyk, aguara |
| Tool poisoning в descriptions | Скрытые инструкции в tools/list | С | snyk, aguara, mcp-guardian (research), AGT mcp-scan |
| Tool shadowing | Подмена имени инструмента | Д | snyk |
| Rug-pull | SHA256 описания изменилось | Д | Pipelock, aguara, snyk, AGT |
| Prompt injection в skills | base64, «ignore instructions» | С | snyk, aguara, defenseclaw |
| Malware patterns в skills | curl\|bash, backdoor | Д | snyk, aguara, agentguard static |
| Hardcoded secrets | Ключи в markdown/YAML | Д | snyk, aguara, agent-audit (research) |
| Credential handling | Небезопасное хранение секретов | Д | snyk |
| Untrusted content / remote fetch | Загрузка с внешних URL | Д | snyk, aguara |
| MCP unsafe command definitions | Опасные команды в манифесте | Д | aguara |
| Plugin/skill signing & verify | Подпись артефактов | Д | AGT Marketplace, agentseal (research) |
| AIBOM / CycloneDX | Инвентарь компонентов агента | Д | defenseclaw, Pipelock |
| Admission control | Скан до допуска в среду | С | defenseclaw |
| Directory watcher / rescan | Повторное сканирование после установки | Д | defenseclaw |
| Block/allow lists с enforcement | Карантин, отзыв sandbox-прав | Д | defenseclaw |

## 4.2. Сканирование пакетов и CI

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| npm/PyPI/Go/Rust lockfiles | Supply chain пакетов | Д | aguara |
| Install hooks / lifecycle scripts | postinstall malware | Д | aguara JSRisk, PyRisk, RSBuild |
| GitHub Actions trust chains | pull_request_target, OIDC | Д | aguara ci-trust |
| pnpm supply-chain policy | Build approval, trust policy | Д | aguara |
| Flow-sensitive build.rs / setup.py | Exfil в build-скриптах | Д | aguara |

## 4.3. Статический анализ кода агента

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| CodeShield (Semgrep + regex) | Уязвимости в генерируемом коде | Д | LlamaFirewall |
| CodeGuard | secrets, exec, deserialization, weak crypto | Д | defenseclaw |
| ClawShield | injection, malware, PII, vuln | С | defenseclaw |
| YARA + LLM judge на skills | Семантика + сигнатуры | С | defenseclaw skill-scanner |
| cisco mcp-scanner / a2a-scanner | MCP/A2A поверхности | С | defenseclaw |
| Write/edit hooks | Скан при записи файла агентом | Д | defenseclaw |

---

# V. Песочницы и изоляция инфраструктуры

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Firecracker microVM | Отдельное ядро на сессию | А | E2B, agent-airlock |
| gVisor / K8s agent-sandbox | Контейнерная изоляция | А | (agent-sandbox — research) |
| OpenShell sandbox | Сеть, ФС, syscalls | А | defenseclaw |
| Execution rings (CPU-like) | Уровни привилегий агента | А | AGT Agent Runtime |
| Docker backend | Лёгкая изоляция | А | agent-airlock |
| Workspace sandboxing | Ограничение каталога | Д | Janus |
| Separate container per agent | ОС + политики | А | AGT (рекомендация) |
| Session lifecycle destroy | Ничего не остаётся после сессии | А | E2B |
| Snapshot / resume | Быстрый перезапуск среды | А | E2B |

---

# VI. Идентичность, доверие, многоагентность

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Cryptographic agent identity (Ed25519, DID) | Кто такой агент | Д | AGT AgentMesh |
| Inter-Agent Trust Protocol (IATP) | Безопасное A2A | Д | AGT |
| Trust score 0–1000 | Поведенческие уровни | С | AGT |
| Agent behavior baseline | Профиль за 7 дней | С | Aegis |
| Behavioral anomaly (9 dims) | Отклонение от нормы | С | Aegis |
| Skill/plugin attribution | Какой навык вызвал действие | Д | agentguard |
| Multi-tenant / session isolation | MCP session routing | А | agentgateway |

---

# VII. Наблюдаемость, аудит, соответствие

| Мехanism | Суть | Тип | Где |
|----------|------|-----|-----|
| Append-only audit log | Неизменяемый журнал | Д | AGT Flight Recorder |
| Hash-chained audit (SHA-256) | Tamper-evident | Д | Aegis, Pipelock |
| Ed25519 signed traces | Криптодоказательство | Д | Aegis, Pipelock |
| OpenTelemetry tracing | Трассы, метрики | — | agent-airlock, agentgateway, Aegis |
| Structured trace policies | Анализ post-factum | С | Invariant |
| Compliance grading | OWASP ASI, HIPAA, SOC2, EU AI Act | Д | AGT Agent Compliance |
| SIEM export | Splunk, webhooks, OTLP | — | defenseclaw, Aegis |
| Token cost tracking | Стоимость по моделям | — | Aegis, agent-airlock |
| Forensic export PDF/CSV | Расследования | — | Aegis |
| AgentOps-style sessions | Сессии, ошибки, compliance | — | (AgentOps — research) |

---

# VIII. Диалоговое и сценарное управление (NeMo и родственники)

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Input rails | До модели | С | NeMo |
| Output rails | После модели | С | NeMo |
| Dialog rails | Сценарии и темы (Colang) | Д/С | NeMo |
| Execution rails | До/после tool call | С | NeMo |
| Retrieval rails | После RAG | С | NeMo |
| Canonical form matching | Семантика фраз пользователя | С | NeMo |
| Self-healing errors для LLM | Подсказки при блокировке | Д | agent-airlock |

---

# IX. Красное тестирование и оценка (не prod-защита)

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Probes / зонды атак | DAN, encoding, promptinject… | Т | garak (100+), promptfoo (50+) |
| Detectors ответов | string / ML / LLM-judge | Т | garak |
| Regression eval в CI | «После изменения промпта» | Т | promptfoo |
| Dynamic benchmark | 97 задач, 629 security tests | Т | AgentDojo |
| ASR / utility metrics | Успех атак vs полезность | Т | AgentDojo |
| Fuzzing / multi-turn attacks | PyRIT-подобное | Т | (PyRIT — research) |
| Package hallucination probes | Slopsquatting | Т | garak |
| OWASP LLM01–03 mapping | Классификация находок | Т | garak, promptfoo |

---

# X. Облачные и внешние инспекции

| Механизм | Суть | Тип | Где |
|----------|------|-----|-----|
| Snyk Agent Scan API | Семантика описаний tools/skills | В | snyk/agent-scan |
| Cisco AI Defense inspection | Облачная инспекция промптов | В | defenseclaw |
| Together API (AlignmentCheck) | CoT auditor | В | LlamaFirewall |
| Invariant Cloud API | Облачные guardrails | С | Invariant |
| ActiveFence moderation | Внешняя модерация | В | NeMo |
| External IdP | OAuth/OIDC | — | agentgateway |

---

# Сводка: **полный перечень способов** (уникальные классы)

Если свести всё к **~45 базовым способам** обеспечения безопасности агентов:

| № | Способ | Слой |
|---|--------|------|
| 1 | ML-классификация инъекций/jailbreak | Текст |
| 2 | LLM-аудит рассуждений (CoT) | Текст |
| 3 | Эвристики и regex на инъекции | Текст |
| 4 | Нормализация кодировок / Unicode | Текст |
| 5 | Маскирование и детекция ПДн | Текст |
| 6 | DLP на сетевом трафике | Текст/сеть |
| 7 | Детекция секретов в тексте | Текст |
| 8 | Фильтры токсичности / модерация | Текст |
| 9 | Fact-check / hallucination check | Текст |
| 10 | Валидация структуры ответа (JSON/Schema) | Текст |
| 11 | Лимиты токенов, стоимости, частоты | Действие |
| 12 | YAML/Rego/Cedar политики на tools | Действие |
| 13 | JSON Schema / типизация аргументов | Действие |
| 14 | Default-deny + allowlists | Действие |
| 15 | Flow rules (порядок и связь вызовов) | Действие |
| 16 | Capability / IFC / taint метки | Действие |
| 17 | SMT / monotonic privilege control | Действие |
| 18 | ReBAC (SpiceDB) | Действие |
| 19 | SQL/shell/path/command injection rules | Действие |
| 20 | Ghost args / strict typing | Действие |
| 21 | Human-in-the-loop approval | Действие |
| 22 | Kill switch / circuit breaker | Действие |
| 23 | Egress proxy + SSRF protection | Сеть |
| 24 | MCP/LLM gateway с RBAC | Сеть |
| 25 | Rug-pull / hash baseline tools | Supply chain |
| 26 | Tool poisoning / shadowing scan | Supply chain |
| 27 | Skill/plugin static scan (YARA, NLP) | Supply chain |
| 28 | Toxic flow / dataflow analysis | Supply chain |
| 29 | Package/CI/install-hook scan | Supply chain |
| 30 | Code static analysis (Semgrep/CodeGuard) | Код |
| 31 | Admission + blocklist enforcement | Supply chain |
| 32 | AIBOM / inventory | Supply chain |
| 33 | microVM / container sandbox | Инфра |
| 34 | OS-level sandbox (OpenShell) | Инфра |
| 35 | Execution rings / workspace jail | Инфра |
| 36 | Crypto agent identity + A2A trust | Идентичность |
| 37 | Behavioral anomaly / baseline | Поведение |
| 38 | Skill attribution | Поведение |
| 39 | Hash-chained / signed audit | Аудит |
| 40 | OpenTelemetry / SIEM | Аудит |
| 41 | Compliance mapping (OWASP, HIPAA…) | Аудит |
| 42 | Colang/dialog/execution rails | Диалог |
| 43 | Dual-LLM + quarantine architecture | Архитектура |
| 44 | Red team probes + regression eval | Тесты |
| 45 | Security benchmark (AgentDojo) | Тесты |

---

## Что из этого **реально закрывает prod**, а что — нет

| Класс | Prod-защита? |
|-------|--------------|
| 1–10, 11–22, 23–35, 41 (частично) | **Да** |
| 36–38 | **Да**, но чаще дополнение |
| 39–40 | **Аудит**, не блокировка |
| 42 | **Да** для диалоговых ботов, слабее для tool-heavy |
| 43 | **Да**, но сложно внедрить |
| 44–45 | **Нет** — только измерение и тесты |
| Облачные API (раздел X) | **Да**, с зависимостью от вендора |

---