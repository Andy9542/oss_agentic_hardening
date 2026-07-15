| Слой защиты       | Что ловит                                     |     |     |
| ----------------- | --------------------------------------------- | --- | --- |
| 1. Содержание     | Вредный текст, инъекции, утечки в ответах     |     |     |
| 2. Оценка         | Аномалии, диагностика "почему агент сделал X" |     |     |
| 3. Действие       | Небезопасный вызов инструмента                |     |     |
| 4. Инфраструктура | Побег из среды, выполнение вредоносного кода  |     |     |

## Каталог репозиториев

- [[MOC — Кластеры репозиториев]] — семейства дубликатов и вариантов реализации
- Каждый репозиторий: заметка `repo-NN-slug` в `20-implementations/`
- Детальные разборы модулей: `20-implementations/detail/` (связь detail → repo)

Формат: **№ | репозиторий | слой | тип | суть**

> Имя файла сохранено как стабильный канонический путь; фактический каталог расширен до 119 проектов.

### A. Среда выполнения и авторизация до вызова инструмента (20)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 1 | [[repo-01-agent-governance-toolkit|microsoft/agent-governance-toolkit]] | 3+4 | Детерм. | Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK |
| 2 | [[repo-02-pipelock|luckyPipewrench/pipelock]] | 3+4 | Детерм. | Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита |
| 3 | [[repo-03-aegis|Justin0504/Aegis]] | 3 | Детерм. | Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python |
| 4 | [[repo-04-rampart|peg/rampart]] | 3 | Детерм. | Файрвол для coding-агентов: политики на файловые и сетевые действия |
| 5 | [[repo-05-nomos|safe-agentic-world/nomos]] | 3 | Детерм. | Политики ALLOW / DENY / REQUIRE_APPROVAL на уровне инструментов |
| 6 | [[repo-06-zerotrust-agents|lokeshsk/zerotrust-agents]] | 3 | Детерм. | Zero-trust прокси между агентом и API |
| 7 | [[repo-07-agent-tool-firewall|SecAI-Hub/agent-tool-firewall]] | 3 | Детерм. | Default-deny YAML-политики на вызовах инструментов |
| 8 | [[repo-08-agent-airlock|sattyamjjain/agent-airlock]] | 3+4 | Детерм. | Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница |
| 9 | [[repo-09-agent-firewall|0xrem/agent-firewall]] | 3 | Детерм. | Pre-execution firewall: блокировка до выполнения |
| 10 | [[repo-10-progent|sunblaze-ucb/progent]] | 3 | Детерм. | Модульные политики привилегий + SMT-проверка |
| 11 | [[repo-11-janus|Agentic-AI-Risk-Mitigation/Janus]] | 3 | Детерм. | Политики на границе вызова инструмента |
| 12 | [[repo-12-agentgateway|agentgateway/agentgateway]] | 4 | Архит. | Шлюз MCP/A2A: маршрутизация, аутентификация, ограничение поверхностей |
| 13 | [[repo-13-avakill|log-bell/avakill]] | 3 | Детерм. | YAML-политики, три пути enforcement |
| 14 | [[repo-14-interlock|MaazAhmed47/Interlock]] | 3 | Детерм. | Слой доверия MCP в рантайме |
| 15 | [[repo-15-agentgate-public|ElamOlame31/agentgate-public]] | 3 | Детерм. | PDP AgentGate: решение до выполнения действия |
| 16 | [[repo-16-actplane|eunomia-bpf/ActPlane]] | 4 | Детерм. | eBPF-контроль потоков информации на уровне ОС |
| 17 | [[repo-17-agentguard|GoPlusSecurity/agentguard]] | 3 | Детерм. | Хуки в рантайме: сканирование навыков, блокировка опасных действий |
| 18 | [[repo-18-defenseclaw|cisco-ai-defense/defenseclaw]] | 3+4 | Смешан. | CodeGuard, песочница, SSRF-защита реестра, аудит |
| 19 | [[repo-19-bifrost|maximhq/bifrost]] | 1+3 | Смешан. | AI-шлюз с встроенными барьерами и лимитами |
| 20 | [[repo-20-litellm|BerriAI/litellm]] | 1+2 | Смешан. | Прокси LLM с guardrails, бюджетами, логированием |

### B. Сканеры цепочки поставок агентов и MCP (16)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 21 | [[repo-21-agent-scan|snyk/agent-scan]] | 2 | Статич. | Сканер агентов, MCP-серверов, навыков (преемник mcp-scan) |
| 22 | [[repo-22-aguara|garagon/aguara]] | 2 | Статич. | Go-сканер: паттерны, NLP, taint, rug-pull в навыках |
| 23 | [[repo-23-aguara-mcp|garagon/aguara-mcp]] | 2 | Статич. | Aguara как MCP-инструмент для CI |
| 24 | [[repo-24-mcp-scanner|cisco-ai-defense/mcp-scanner]] | 2 | Статич. | Анализ MCP: tools, prompts, malware, готовность к деплою |
| 25 | [[repo-25-skill-scanner|cisco-ai-defense/skill-scanner]] | 2 | Смешан. | YARA + LLM-судья + dataflow для навыков Codex/Cursor |
| 26 | [[repo-26-agent-audit|scadastrangelove/agent-audit]] | 2 | Статич. | 296 правил для coding-агентов и MCP-манифестов |
| 27 | [[repo-27-agentshield|affaan-m/agentshield]] | 2 | Статич. | Сканер конфигураций агентов, GitHub Action |
| 28 | [[repo-28-mcp-guardian|alexandriashai/mcp-guardian]] | 2 | Статич. | Детекция инъекций в описаниях MCP-инструментов |
| 29 | [[repo-29-agentic-radar|splx-ai/agentic-radar]] | 2 | Статич. | Карта потоков данных в LangGraph/CrewAI/n8n |
| 30 | [[repo-30-inkog|inkog-io/inkog]] | 2 | Статич. | Статический анализ LangChain/CrewAI/AutoGen |
| 31 | [[repo-31-medusa|Pantheon-Security/medusa]] | 2 | Статич. | Сканер репозиториев агентов и MCP |
| 32 | [[repo-32-clawsec|prompt-security/clawsec]] | 3 | Смешан. | Набор security-навыков для OpenClaw-семейства |
| 33 | [[repo-33-agentseal|getagentseal/agentseal]] | 2 | Статич. | Подпись и верификация артефактов агентов |
| 34 | [[repo-34-repo-forensics|alexgreensh/repo-forensics]] | 2 | Статич. | Офлайн-сканер навыков, плагинов, MCP |
| 35 | [[repo-35-skillguard|obielin/skillguard]] | 2 | Статич. | Защита навыков агентов от компрометации |
| 36 | [[repo-36-mcp-guardian|mcp-guardian/mcp-guardian]] | 3 | Детерм. | Runtime-защита MCP-серверов |

### C. Барьеры и фильтры содержания (14)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 37 | [[repo-37-purplellama|meta-llama/PurpleLlama]] | 1 | Вероятн. | LlamaFirewall, CodeShield, CyberSecEval |
| 38 | [[repo-38-guardrails|NVIDIA-NeMo/Guardrails]] | 1 | Смешан. | Программируемые рельсы на Colang |
| 39 | [[repo-39-guardrails|guardrails-ai/guardrails]] | 1 | Смешан. | Валидаторы ввода/вывода, PII, структура |
| 40 | [[repo-40-llm-guard|protectai/llm-guard]] | 1 | Вероятн. | Сканеры prompt injection, токсичности, секретов |
| 41 | [[repo-41-rebuff|protectai/rebuff]] | 1 | Вероятн. | Эвристики + LLM-классификатор + canary-токены |
| 42 | [[repo-42-vigil-llm|deadbits/vigil-llm]] | 1 | Вероятн. | YARA + векторное сходство для инъекций |
| 43 | [[repo-43-langkit|whylabs/langkit]] | 1+2 | Вероятн. | Мониторинг инъекций, дрейфа, токсичности |
| 44 | [[repo-44-circuit-breakers|GraySwanAI/circuit-breakers]] | 1 | Вероятн. | «Автоматические выключатели» в весах модели |
| 45 | [[repo-45-plexiglass|kortex-labs/plexiglass]] | 1 | Смешан. | Набор тестов и барьеров для LLM |
| 46 | [[repo-46-invariant|invariantlabs-ai/invariant]] | 1+2 | Смешан. | Анализ трасс агентов, политики на цепочках вызовов |
| 47 | [[repo-47-invariant-gateway|invariantlabs-ai/invariant-gateway]] | 1+3 | Смешан. | Шлюз с политиками для агентных трасс |
| 48 | [[repo-48-heimdallm|amoffat/HeimdaLLM]] | 1 | Вероятн. | Middleware-фильтр промптов |
| 49 | [[repo-49-granite-guardian|ibm-granite/granite-guardian]] | 1 | Вероятн. | Классификаторы риска для Granite-моделей |
| 50 | [[repo-50-agentshield|AdityaBelhekar/AgentShield]] | 3 | Детерм. | Runtime SDK: перехват вызовов в приложении |

### D. Песочницы и изоляция (8)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 51 | [[repo-51-e2b|e2b-dev/E2B]] | 4 | Архит. | Firecracker microVM для кода агента (~150 мс) |
| 52 | [[repo-52-sandbox|agent-infra/sandbox]] | 4 | Архит. | Универсальная песочница для агентов |
| 53 | [[repo-53-agent-sandbox|kubernetes-sigs/agent-sandbox]] | 4 | Архит. | K8s CRD для изоляции агентов |
| 54 | [[repo-54-sandboxai|substratusai/sandboxai]] | 4 | Архит. | Облачные песочницы для LLM-агентов |
| 55 | [[repo-55-openhands|All-Hands-AI/OpenHands]] | 4 | Архит. | Агент с Docker-изоляцией выполнения |
| 56 | [[repo-56-camel-prompt-injection|google-research/camel-prompt-injection]] | 3+4 | Детерм. | CaMeL: capability-based контроль + разделение доверенных данных |
| 57 | [[repo-57-pipelock-verify-python|luckyPipewrench/pipelock-verify-python]] | 2 | Детерм. | Верификатор криптографических квитанций Pipelock |
| 58 | [[repo-58-mcp-gateway-registry|agentic-community/mcp-gateway-registry]] | 4 | Архит. | Реестр и шлюз MCP с контролем доступа |

### E. Стандарты, правила, каталоги угроз (7)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 59 | [[repo-59-agent-threat-rules|panguard-ai/agent-threat-rules]] | 2 | Стандарт | «Sigma для агентов»: правила детекции угроз |
| 60 | [[repo-60-asamm|scadastrangelove/asamm]] | — | Фреймворк | OWASP SAMM для агентной разработки |
| 61 | [[repo-61-aibom-generator|GenAI-Security-Project/aibom-generator]] | 2 | Статич. | SBOM для ИИ-компонентов агента |
| 62 | [[repo-62-prompt-injection-defenses|tldrsec/prompt-injection-defenses]] | — | Каталог | Сводка практических защит от инъекций |
| 63 | [[repo-63-opa|open-policy-agent/opa]] | 3 | Детерм. | Движок политик Rego для авторизации |
| 64 | [[repo-64-genai-agent-security-initiative|GenAI-Security-Project/GenAI-Agent-Security-Initiative]] | — | Фреймворк | Инициатива OWASP по безопасности агентов |
| 65 | [[repo-65-modelscan|protectai/modelscan]] | 4 | Статич. | Сканирование сериализованных ML-файлов |

### F. Бенчмарки и среды оценки защит (10)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 66 | [[repo-66-agentdojo|ethz-spylab/agentdojo]] | — | Бенчмарк | Атаки и защиты в среде tool-using агентов |
| 67 | [[repo-67-injecagent|uiuc-kang-lab/InjecAgent]] | — | Бенчмарк | 1054 кейсов косвенных инъекций, 17+62 инструмента |
| 68 | [[repo-68-finbot-ctf|GenAI-Security-Project/finbot-ctf]] | — | CTF | Финансовый агент-мишень для red team |
| 69 | [[repo-69-rampart|microsoft/RAMPART]] | — | Бенчмарк | Оценка устойчивости агентов Microsoft |
| 70 | [[repo-70-agent-egress-bench|luckyPipewrench/agent-egress-bench]] | — | Бенчмарк | Корпус для оценки egress-контроля |
| 71 | [[repo-71-open-prompt-injection|liu00222/Open-Prompt-Injection]] | — | Бенчмарк | Формализация атак и защит от инъекций |
| 72 | [[repo-72-jailbreakbench|JailbreakBench/jailbreakbench]] | — | Бенчмарк | Открытый бенчмарк jailbreak-устойчивости |
| 73 | [[repo-73-inspect-ai|UKGovernmentBEIS/inspect_ai]] | — | Фреймворк | Фреймворк оценки безопасности LLM (UK AISI) |
| 74 | [[repo-74-inspect-evals|UKGovernmentBEIS/inspect_evals]] | — | Бенчмарк | Набор cyber/безопасностных eval |
| 75 | [[repo-75-agentfence|agentfence/agentfence]] | — | Тест-стенд | Runtime-тесты: инъекции, утечки секретов |

### G. Красное тестирование агентов (12)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 76 | [[repo-76-garak|NVIDIA/garak]] | — | Red team | 100+ детекторов уязвимостей LLM |
| 77 | [[repo-77-pyrit|Azure/PyRIT]] | — | Red team | Оркестрация многоходовых атак |
| 78 | [[repo-78-promptfoo|promptfoo/promptfoo]] | — | Red team | 50+ плагинов атак, регрессионные тесты |
| 79 | [[repo-79-agentic-security|msoedov/agentic_security]] | — | Red team | Сканер агентных систем: hijack, tool abuse |
| 80 | [[repo-80-fuzzyai|cyberark/FuzzyAI]] | — | Red team | Фаззинг jailbreak и prompt injection |
| 81 | [[repo-81-spikee|ReversecLabs/spikee]] | — | Red team | Набор для оценки и эксплуатации инъекций |
| 82 | [[repo-82-augustus|praetorian-inc/augustus]] | — | Red team | Single-binary тестирование LLM |
| 83 | [[repo-83-deepteam|confident-ai/deepteam]] | — | Red team | Red team для LLM-систем |
| 84 | [[repo-84-moonshot|aiverify-foundation/moonshot]] | — | Red team | Модульный бенчмарк и red team |
| 85 | [[repo-85-ps-fuzz|prompt-security/ps-fuzz]] | — | Red team | Фаззинг системных промптов |
| 86 | [[repo-86-llmfuzzer|mnns/LLMFuzzer]] | — | Red team | Фаззинг LLM API-интеграций |
| 87 | [[repo-87-promptmap|utkusen/promptmap]] | — | Red team | Сканер инъекций white/black-box |

### H. Исследовательские защиты (8)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 88 | [[repo-88-bipia|microsoft/BIPIA]] | 1 | Вероятн. | Бенчмарк и защита от косвенных инъекций |
| 89 | [[repo-89-autodefense|XHMY/AutoDefense]] | 1 | Вероятн. | Мультиагентная защита от jailbreak |
| 90 | [[repo-90-llm-self-defense|poloclub/llm-self-defense]] | 1 | Вероятн. | Самопроверка: модель детектирует обман |
| 91 | [[repo-91-baseline-defenses|neelsjain/baseline-defenses]] | 1 | Смешан. | Базовые защиты от adversarial-атак |
| 92 | [[repo-92-prompt-injection-shield|MukundaKatta/prompt-injection-shield]] | 1 | Вероятн. | Щит от инъекций для агентов |
| 93 | [[repo-93-agentvet|MukundaKatta/agentvet]] | 2 | Статич. | Веттинг конфигураций агентов |
| 94 | [[repo-94-agentguard|MukundaKatta/agentguard]] | 3 | Детерм. | Контроль сетевого egress агента |
| 95 | [[repo-95-agent-bound|ElPaisano/agent-bound]] | 3 | Детерм. | Ограничение границ действий агента |

### I. Наблюдаемость и шлюзы с безопасностью (5)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 96 | [[repo-96-agentops|AgentOps-AI/agentops]] | 2 | Наблюд. | Сессии, стоимость, ошибки, compliance |
| 97 | [[repo-97-openllmetry|traceloop/openllmetry]] | 2 | Наблюд. | OpenTelemetry для LLM/агентов |
| 98 | [[repo-98-phoenix|Arize-AI/phoenix]] | 2 | Наблюд. | Трассировка, eval RAG, галлюцинации |
| 99 | [[repo-99-presidio|microsoft/presidio]] | 1 | Детерм. | Детекция и анонимизация ПДн в потоках агента |
| 100 | [[repo-100-obot|obot-platform/obot]] | 4 | Архит. | MCP-шлюз с контролем доступа и аудитом |

### J. Дополнение: эталонные OSS для способов №18, №30, №34, №46 (4)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 101 | [[repo-101-semgrep|semgrep/semgrep]] | 4 | Статич. | Rule-based SAST для кода coding-агентов |
| 102 | [[repo-102-spicedb|authzed/spicedb]] | 3 | Детерм. | ReBAC (Zanzibar): CheckPermission user→agent→tool |
| 103 | [[repo-103-openshell|NVIDIA/OpenShell]] | 4 | Архит. | OS-level sandbox: YAML-политики FS/сеть/syscall |
| 104 | [[repo-104-agentpoison|BillChan226/AgentPoison]] | — | Red team | Red-team benchmark memory/RAG poisoning (NeurIPS 2024) |

---


### K. Дополнение обзора 2026 (12)

| № | Репозиторий | Слой | Тип | Основной способ | Суть |
|---|-------------|------|-----|-----------------|------|
| 105 | [pezhik/skilltotal](https://github.com/pezhik/skilltotal) | 2 | Статич. | №27 | Локальный regex+AST scanner skills, MCP, пакетов и AI-проектов; SARIF, baseline, diff и pre-install guard |
| 106 | [arthurpanhku/dvalincode](https://github.com/arthurpanhku/dvalincode) | 3+4 | Смешан. | №35 | Policy-bound coding-agent runtime: сужающиеся политики, approvals, sandbox и hash-chained audit |
| 107 | [ArmorerLabs/Armorer-Guard](https://github.com/ArmorerLabs/Armorer-Guard) | 1+3 | Смешан. | №19 | Локальный MCP proxy: secret redaction, semantic injection classifier и контроль аргументов до tool call |
| 108 | [agent-defense/parallax](https://github.com/agent-defense/parallax) | 2+3 | Детерм. | №15 | Out-of-band engine правил по lifecycle events: regex, Sigma, CEL и temporal SQL |
| 109 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 2 | Смешан. | №27 | Статический и опциональный LLM-анализ agent skills, taint/YARA/OSV, SARIF и baseline |
| 110 | [sleeepeer/PIArena](https://github.com/sleeepeer/PIArena) | — | Бенчмарк | №44 | Платформа сравнения prompt-injection атак и защит; AgentDojo, InjecAgent и AgentDyn |
| 111 | [h5i-dev/h5i](https://github.com/h5i-dev/h5i) | 4 | Архит. | №35 | Изолированные worktree, Git-аудит, replay, peer review и verify gates для coding-агентов |
| 112 | [onecli/onecli](https://github.com/onecli/onecli) | 3+4 | Архит. | №14 | Credential broker: scoped permissions и deny mode до подстановки секрета в outbound request |
| 113 | [aira-security/mcp-armor](https://github.com/aira-security/mcp-armor) | 2 | Смешан. | №25 | MCP inventory, poisoning/shadowing checks и baseline drift для rug-pull detection |
| 114 | [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 2 | Вероятн. | №30 | Diff-aware LLM security review в GitHub Actions с фильтрацией false positives |
| 115 | [highflame-ai/ramparts](https://github.com/highflame-ai/ramparts) | 2 | Смешан. | №26 | Единый Rust scanner MCP и skills: YARA, OSV, LLM, OWASP MCP mapping и SARIF |
| 116 | [HiveTrace/HiveTraceRed](https://github.com/HiveTrace/HiveTraceRed) | — | Red team | №44 | Multilingual regression framework: 80+ jailbreak-атак, async pipeline и evaluators |

### L. Источники из saved Telegram (3)

| № | Репозиторий | Слой | Тип | Основной способ | Суть |
|---|-------------|------|-----|-----------------|------|
| 117 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | 3 | Детерм. | №19 | Pre-execution hook: контекстный разбор shell-команд, allowlist и packs опасных операций; fail-open, не самостоятельная security boundary |
| 118 | [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) | 2 | Детерм. | №32 | Read-only endpoint inventory пакетов, расширений, tool metadata и MCP-конфигов с matching по exposure catalog |
| 119 | [scadastrangelove/awesome-ai-security-tools](https://github.com/scadastrangelove/awesome-ai-security-tools) | — | Meta-каталог | — | Discovery-источник по AI security и AI-assisted security; включение не является оценкой зрелости |

---

## Сравнительная матрица: топ-20 инструментов

| Инструмент | Слой | Детерм. | Рантайм | MCP | Аудит | Зрелость | Лучше для |
|------------|------|---------|---------|-----|-------|----------|-----------|
| **agent-governance-toolkit** | 3+4 | ✅ | ✅ | ✅ | ✅ | ★★★★☆ | Enterprise-агенты |
| **pipelock** | 3+4 | ✅ | ✅ | ✅ | ✅★ | ★★★★☆ | Egress/DLP |
| **progent** | 3 | ✅ | ✅ | ○ | ○ | ★★★☆☆ | Fine-grained ACL |
| **snyk/agent-scan** | 2 | ✅ | ✗ | ✅ | ○ | ★★★★★ | CI/CD supply chain |
| **agentgateway** | 4 | ✅ | ✅ | ✅ | ○ | ★★★★☆ | MCP/A2A mesh |
| **PurpleLlama** | 1 | ✗ | ✅ | ✗ | ✗ | ★★★★★ | Content filter |
| **invariant** | 1+2 | ○ | ✅ | ✅ | ✅ | ★★★☆☆ | Trace policies |
| **agent-airlock** | 3+4 | ✅ | ✅ | ○ | ✅ | ★★★☆☆ | LangChain/CrewAI |
| **Aegis** | 3 | ✅ | ✅ | ○ | ✅ | ★★★☆☆ | PDP-шлюз |
| **defenseclaw** | 3+4 | ✅ | ✅ | ✅ | ✅ | ★★★☆☆ | OpenClaw-стек |
| **e2b-dev/E2B** | 4 | ✅ | ✅ | ✗ | ○ | ★★★★★ | Code execution |
| **agentdojo** | — | — | — | — | — | ★★★★☆ | Eval защит |
| **garak** | — | — | — | — | — | ★★★★★ | Red team |
| **promptfoo** | — | — | — | — | — | ★★★★★ | CI regression |
| **llm-guard** | 1 | ✗ | ✅ | ✗ | ○ | ★★★★☆ | Input/output scan |
| **NeMo Guardrails** | 1 | ○ | ✅ | ○ | ○ | ★★★★☆ | Dialog policy |
| **CaMeL** | 3+4 | ✅ | ○ | ✗ | ○ | ★★☆☆☆ | Research |
| **Janus** | 3 | ✅ | ✅ | ○ | ○ | ★★☆☆☆ | Tool policies |
| **aguara** | 2 | ✅ | ✗ | ✅ | ○ | ★★★☆☆ | Skill scanning |
| **GoPlusSecurity/agentguard** | 3 | ✅ | ✅ | ○ | ✅ | ★★★☆☆ | Coding agents |

---

