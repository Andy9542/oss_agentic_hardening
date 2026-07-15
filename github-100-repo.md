| Слой защиты       | Что ловит                                     |     |     |
| ----------------- | --------------------------------------------- | --- | --- |
| 1. Содержание     | Вредный текст, инъекции, утечки в ответах     |     |     |
| 2. Оценка         | Аномалии, диагностика "почему агент сделал X" |     |     |
| 3. Действие       | Небезопасный вызов инструмента                |     |     |
| 4. Инфраструктура | Побег из среды, выполнение вредоносного кода  |     |     |

## Каталог 112 репозиториев

Формат: **№ | репозиторий | слой | тип | суть**

> Имя файла сохранено как стабильный канонический путь; фактический каталог расширен до 112 проектов.

### A. Среда выполнения и авторизация до вызова инструмента (20)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 1 | [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 3+4 | Детерм. | Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK |
| 2 | [luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock) | 3+4 | Детерм. | Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита |
| 3 | [Justin0504/Aegis](https://github.com/Justin0504/Aegis) | 3 | Детерм. | Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python |
| 4 | [peg/rampart](https://github.com/peg/rampart) | 3 | Детерм. | Файрвол для coding-агентов: политики на файловые и сетевые действия |
| 5 | [safe-agentic-world/nomos](https://github.com/safe-agentic-world/nomos) | 3 | Детерм. | Политики ALLOW / DENY / REQUIRE_APPROVAL на уровне инструментов |
| 6 | [lokeshsk/zerotrust-agents](https://github.com/lokeshsk/zerotrust-agents) | 3 | Детерм. | Zero-trust прокси между агентом и API |
| 7 | [SecAI-Hub/agent-tool-firewall](https://github.com/SecAI-Hub/agent-tool-firewall) | 3 | Детерм. | Default-deny YAML-политики на вызовах инструментов |
| 8 | [sattyamjjain/agent-airlock](https://github.com/sattyamjjain/agent-airlock) | 3+4 | Детерм. | Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница |
| 9 | [0xrem/agent-firewall](https://github.com/0xrem/agent-firewall) | 3 | Детерм. | Pre-execution firewall: блокировка до выполнения |
| 10 | [sunblaze-ucb/progent](https://github.com/sunblaze-ucb/progent) | 3 | Детерм. | Модульные политики привилегий + SMT-проверка |
| 11 | [Agentic-AI-Risk-Mitigation/Janus](https://github.com/Agentic-AI-Risk-Mitigation/Janus) | 3 | Детерм. | Политики на границе вызова инструмента |
| 12 | [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) | 4 | Архит. | Шлюз MCP/A2A: маршрутизация, аутентификация, ограничение поверхностей |
| 13 | [log-bell/avakill](https://github.com/log-bell/avakill) | 3 | Детерм. | YAML-политики, три пути enforcement |
| 14 | [MaazAhmed47/Interlock](https://github.com/MaazAhmed47/Interlock) | 3 | Детерм. | Слой доверия MCP в рантайме |
| 15 | [ElamOlame31/agentgate-public](https://github.com/ElamOlame31/agentgate-public) | 3 | Детерм. | PDP AgentGate: решение до выполнения действия |
| 16 | [eunomia-bpf/ActPlane](https://github.com/eunomia-bpf/ActPlane) | 4 | Детерм. | eBPF-контроль потоков информации на уровне ОС |
| 17 | [GoPlusSecurity/agentguard](https://github.com/GoPlusSecurity/agentguard) | 3 | Детерм. | Хуки в рантайме: сканирование навыков, блокировка опасных действий |
| 18 | [cisco-ai-defense/defenseclaw](https://github.com/cisco-ai-defense/defenseclaw) | 3+4 | Смешан. | CodeGuard, песочница, SSRF-защита реестра, аудит |
| 19 | [maximhq/bifrost](https://github.com/maximhq/bifrost) | 1+3 | Смешан. | AI-шлюз с встроенными барьерами и лимитами |
| 20 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 1+2 | Смешан. | Прокси LLM с guardrails, бюджетами, логированием |

### B. Сканеры цепочки поставок агентов и MCP (16)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 21 | [snyk/agent-scan](https://github.com/snyk/agent-scan) | 2 | Статич. | Сканер агентов, MCP-серверов, навыков (преемник mcp-scan) |
| 22 | [garagon/aguara](https://github.com/garagon/aguara) | 2 | Статич. | Go-сканер: паттерны, NLP, taint, rug-pull в навыках |
| 23 | [garagon/aguara-mcp](https://github.com/garagon/aguara-mcp) | 2 | Статич. | Aguara как MCP-инструмент для CI |
| 24 | [cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) | 2 | Статич. | Анализ MCP: tools, prompts, malware, готовность к деплою |
| 25 | [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) | 2 | Смешан. | YARA + LLM-судья + dataflow для навыков Codex/Cursor |
| 26 | [scadastrangelove/agent-audit](https://github.com/scadastrangelove/agent-audit) | 2 | Статич. | 296 правил для coding-агентов и MCP-манифестов |
| 27 | [affaan-m/agentshield](https://github.com/affaan-m/agentshield) | 2 | Статич. | Сканер конфигураций агентов, GitHub Action |
| 28 | [alexandriashai/mcp-guardian](https://github.com/alexandriashai/mcp-guardian) | 2 | Статич. | Детекция инъекций в описаниях MCP-инструментов |
| 29 | [splx-ai/agentic-radar](https://github.com/splx-ai/agentic-radar) | 2 | Статич. | Карта потоков данных в LangGraph/CrewAI/n8n |
| 30 | [inkog-io/inkog](https://github.com/inkog-io/inkog) | 2 | Статич. | Статический анализ LangChain/CrewAI/AutoGen |
| 31 | [Pantheon-Security/medusa](https://github.com/Pantheon-Security/medusa) | 2 | Статич. | Сканер репозиториев агентов и MCP |
| 32 | [prompt-security/clawsec](https://github.com/prompt-security/clawsec) | 3 | Смешан. | Набор security-навыков для OpenClaw-семейства |
| 33 | [getagentseal/agentseal](https://github.com/getagentseal/agentseal) | 2 | Статич. | Подпись и верификация артефактов агентов |
| 34 | [alexgreensh/repo-forensics](https://github.com/alexgreensh/repo-forensics) | 2 | Статич. | Офлайн-сканер навыков, плагинов, MCP |
| 35 | [obielin/skillguard](https://github.com/obielin/skillguard) | 2 | Статич. | Защита навыков агентов от компрометации |
| 36 | [mcp-guardian/mcp-guardian](https://github.com/mcp-guardian/mcp-guardian) | 3 | Детерм. | Runtime-защита MCP-серверов |

### C. Барьеры и фильтры содержания (14)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 37 | [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | 1 | Вероятн. | LlamaFirewall, CodeShield, CyberSecEval |
| 38 | [NVIDIA-NeMo/Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) | 1 | Смешан. | Программируемые рельсы на Colang |
| 39 | [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | 1 | Смешан. | Валидаторы ввода/вывода, PII, структура |
| 40 | [protectai/llm-guard](https://github.com/protectai/llm-guard) | 1 | Вероятн. | Сканеры prompt injection, токсичности, секретов |
| 41 | [protectai/rebuff](https://github.com/protectai/rebuff) | 1 | Вероятн. | Эвристики + LLM-классификатор + canary-токены |
| 42 | [deadbits/vigil-llm](https://github.com/deadbits/vigil-llm) | 1 | Вероятн. | YARA + векторное сходство для инъекций |
| 43 | [whylabs/langkit](https://github.com/whylabs/langkit) | 1+2 | Вероятн. | Мониторинг инъекций, дрейфа, токсичности |
| 44 | [GraySwanAI/circuit-breakers](https://github.com/GraySwanAI/circuit-breakers) | 1 | Вероятн. | «Автоматические выключатели» в весах модели |
| 45 | [kortex-labs/plexiglass](https://github.com/kortex-labs/plexiglass) | 1 | Смешан. | Набор тестов и барьеров для LLM |
| 46 | [invariantlabs-ai/invariant](https://github.com/invariantlabs-ai/invariant) | 1+2 | Смешан. | Анализ трасс агентов, политики на цепочках вызовов |
| 47 | [invariantlabs-ai/invariant-gateway](https://github.com/invariantlabs-ai/invariant-gateway) | 1+3 | Смешан. | Шлюз с политиками для агентных трасс |
| 48 | [amoffat/HeimdaLLM](https://github.com/amoffat/HeimdaLLM) | 1 | Вероятн. | Middleware-фильтр промптов |
| 49 | [ibm-granite/granite-guardian](https://github.com/ibm-granite/granite-guardian) | 1 | Вероятн. | Классификаторы риска для Granite-моделей |
| 50 | [AdityaBelhekar/AgentShield](https://github.com/AdityaBelhekar/AgentShield) | 3 | Детерм. | Runtime SDK: перехват вызовов в приложении |

### D. Песочницы и изоляция (8)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 51 | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | 4 | Архит. | Firecracker microVM для кода агента (~150 мс) |
| 52 | [agent-infra/sandbox](https://github.com/agent-infra/sandbox) | 4 | Архит. | Универсальная песочница для агентов |
| 53 | [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | 4 | Архит. | K8s CRD для изоляции агентов |
| 54 | [substratusai/sandboxai](https://github.com/substratusai/sandboxai) | 4 | Архит. | Облачные песочницы для LLM-агентов |
| 55 | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 4 | Архит. | Агент с Docker-изоляцией выполнения |
| 56 | [google-research/camel-prompt-injection](https://github.com/google-research/camel-prompt-injection) | 3+4 | Детерм. | CaMeL: capability-based контроль + разделение доверенных данных |
| 57 | [luckyPipewrench/pipelock-verify-python](https://github.com/luckyPipewrench/pipelock-verify-python) | 2 | Детерм. | Верификатор криптографических квитанций Pipelock |
| 58 | [agentic-community/mcp-gateway-registry](https://github.com/agentic-community/mcp-gateway-registry) | 4 | Архит. | Реестр и шлюз MCP с контролем доступа |

### E. Стандарты, правила, каталоги угроз (7)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 59 | [panguard-ai/agent-threat-rules](https://github.com/panguard-ai/agent-threat-rules) | 2 | Стандарт | «Sigma для агентов»: правила детекции угроз |
| 60 | [scadastrangelove/asamm](https://github.com/scadastrangelove/asamm) | — | Фреймворк | OWASP SAMM для агентной разработки |
| 61 | [GenAI-Security-Project/aibom-generator](https://github.com/GenAI-Security-Project/aibom-generator) | 2 | Статич. | SBOM для ИИ-компонентов агента |
| 62 | [tldrsec/prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses) | — | Каталог | Сводка практических защит от инъекций |
| 63 | [open-policy-agent/opa](https://github.com/open-policy-agent/opa) | 3 | Детерм. | Движок политик Rego для авторизации |
| 64 | [GenAI-Security-Project/GenAI-Agent-Security-Initiative](https://github.com/GenAI-Security-Project/GenAI-Agent-Security-Initiative) | — | Фреймворк | Инициатива OWASP по безопасности агентов |
| 65 | [protectai/modelscan](https://github.com/protectai/modelscan) | 4 | Статич. | Сканирование сериализованных ML-файлов |

### F. Бенчмарки и среды оценки защит (10)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 66 | [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo) | — | Бенчмарк | Атаки и защиты в среде tool-using агентов |
| 67 | [uiuc-kang-lab/InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) | — | Бенчмарк | 1054 кейсов косвенных инъекций, 17+62 инструмента |
| 68 | [GenAI-Security-Project/finbot-ctf](https://github.com/GenAI-Security-Project/finbot-ctf) | — | CTF | Финансовый агент-мишень для red team |
| 69 | [microsoft/RAMPART](https://github.com/microsoft/RAMPART) | — | Бенчмарк | Оценка устойчивости агентов Microsoft |
| 70 | [luckyPipewrench/agent-egress-bench](https://github.com/luckyPipewrench/agent-egress-bench) | — | Бенчмарк | Корпус для оценки egress-контроля |
| 71 | [liu00222/Open-Prompt-Injection](https://github.com/liu00222/Open-Prompt-Injection) | — | Бенчмарк | Формализация атак и защит от инъекций |
| 72 | [JailbreakBench/jailbreakbench](https://github.com/JailbreakBench/jailbreakbench) | — | Бенчмарк | Открытый бенчмарк jailbreak-устойчивости |
| 73 | [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | — | Фреймворк | Фреймворк оценки безопасности LLM (UK AISI) |
| 74 | [UKGovernmentBEIS/inspect_evals](https://github.com/UKGovernmentBEIS/inspect_evals) | — | Бенчмарк | Набор cyber/безопасностных eval |
| 75 | [agentfence/agentfence](https://github.com/agentfence/agentfence) | — | Тест-стенд | Runtime-тесты: инъекции, утечки секретов |

### G. Красное тестирование агентов (12)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 76 | [NVIDIA/garak](https://github.com/NVIDIA/garak) | — | Red team | 100+ детекторов уязвимостей LLM |
| 77 | [Azure/PyRIT](https://github.com/Azure/PyRIT) | — | Red team | Оркестрация многоходовых атак |
| 78 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | — | Red team | 50+ плагинов атак, регрессионные тесты |
| 79 | [msoedov/agentic_security](https://github.com/msoedov/agentic_security) | — | Red team | Сканер агентных систем: hijack, tool abuse |
| 80 | [cyberark/FuzzyAI](https://github.com/cyberark/FuzzyAI) | — | Red team | Фаззинг jailbreak и prompt injection |
| 81 | [ReversecLabs/spikee](https://github.com/ReversecLabs/spikee) | — | Red team | Набор для оценки и эксплуатации инъекций |
| 82 | [praetorian-inc/augustus](https://github.com/praetorian-inc/augustus) | — | Red team | Single-binary тестирование LLM |
| 83 | [confident-ai/deepteam](https://github.com/confident-ai/deepteam) | — | Red team | Red team для LLM-систем |
| 84 | [aiverify-foundation/moonshot](https://github.com/aiverify-foundation/moonshot) | — | Red team | Модульный бенчмарк и red team |
| 85 | [prompt-security/ps-fuzz](https://github.com/prompt-security/ps-fuzz) | — | Red team | Фаззинг системных промптов |
| 86 | [mnns/LLMFuzzer](https://github.com/mnns/LLMFuzzer) | — | Red team | Фаззинг LLM API-интеграций |
| 87 | [utkusen/promptmap](https://github.com/utkusen/promptmap) | — | Red team | Сканер инъекций white/black-box |

### H. Исследовательские защиты (8)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 88 | [microsoft/BIPIA](https://github.com/microsoft/BIPIA) | 1 | Вероятн. | Бенчмарк и защита от косвенных инъекций |
| 89 | [XHMY/AutoDefense](https://github.com/XHMY/AutoDefense) | 1 | Вероятн. | Мультиагентная защита от jailbreak |
| 90 | [poloclub/llm-self-defense](https://github.com/poloclub/llm-self-defense) | 1 | Вероятн. | Самопроверка: модель детектирует обман |
| 91 | [neelsjain/baseline-defenses](https://github.com/neelsjain/baseline-defenses) | 1 | Смешан. | Базовые защиты от adversarial-атак |
| 92 | [MukundaKatta/prompt-injection-shield](https://github.com/MukundaKatta/prompt-injection-shield) | 1 | Вероятн. | Щит от инъекций для агентов |
| 93 | [MukundaKatta/agentvet](https://github.com/MukundaKatta/agentvet) | 2 | Статич. | Веттинг конфигураций агентов |
| 94 | [MukundaKatta/agentguard](https://github.com/MukundaKatta/agentguard) | 3 | Детерм. | Контроль сетевого egress агента |
| 95 | [ElPaisano/agent-bound](https://github.com/ElPaisano/agent-bound) | 3 | Детерм. | Ограничение границ действий агента |

### I. Наблюдаемость и шлюзы с безопасностью (5)

| № | Репозиторий | Слой | Тип | Принцип работы |
|---|-------------|------|-----|----------------|
| 96 | [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops) | 2 | Наблюд. | Сессии, стоимость, ошибки, compliance |
| 97 | [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | 2 | Наблюд. | OpenTelemetry для LLM/агентов |
| 98 | [Arize-AI/phoenix](https://github.com/Arize-AI/phoenix) | 2 | Наблюд. | Трассировка, eval RAG, галлюцинации |
| 99 | [microsoft/presidio](https://github.com/microsoft/presidio) | 1 | Детерм. | Детекция и анонимизация ПДн в потоках агента |
| 100 | [obot-platform/obot](https://github.com/obot-platform/obot) | 4 | Архит. | MCP-шлюз с контролем доступа и аудитом |

---


### J. Дополнение обзора 2026 (12)

| № | Репозиторий | Слой | Тип | Основной способ | Суть |
|---|-------------|------|-----|-----------------|------|
| 101 | [pezhik/skilltotal](https://github.com/pezhik/skilltotal) | 2 | Статич. | №27 | Локальный regex+AST scanner skills, MCP, пакетов и AI-проектов; SARIF, baseline, diff и pre-install guard |
| 102 | [arthurpanhku/dvalincode](https://github.com/arthurpanhku/dvalincode) | 3+4 | Смешан. | №35 | Policy-bound coding-agent runtime: сужающиеся политики, approvals, sandbox и hash-chained audit |
| 103 | [ArmorerLabs/Armorer-Guard](https://github.com/ArmorerLabs/Armorer-Guard) | 1+3 | Смешан. | №19 | Локальный MCP proxy: secret redaction, semantic injection classifier и контроль аргументов до tool call |
| 104 | [agent-defense/parallax](https://github.com/agent-defense/parallax) | 2+3 | Детерм. | №15 | Out-of-band engine правил по lifecycle events: regex, Sigma, CEL и temporal SQL |
| 105 | [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | 2 | Смешан. | №27 | Статический и опциональный LLM-анализ agent skills, taint/YARA/OSV, SARIF и baseline |
| 106 | [sleeepeer/PIArena](https://github.com/sleeepeer/PIArena) | — | Бенчмарк | №45 | Платформа сравнения prompt-injection атак и защит; AgentDojo, InjecAgent и AgentDyn |
| 107 | [h5i-dev/h5i](https://github.com/h5i-dev/h5i) | 4 | Архит. | №35 | Изолированные worktree, Git-аудит, replay, peer review и verify gates для coding-агентов |
| 108 | [onecli/onecli](https://github.com/onecli/onecli) | 3+4 | Архит. | №23 | Credential broker: gateway подставляет секрет в outbound request, агент ключ не видит |
| 109 | [aira-security/mcp-armor](https://github.com/aira-security/mcp-armor) | 2 | Смешан. | №25 | MCP inventory, poisoning/shadowing checks и baseline drift для rug-pull detection |
| 110 | [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) | 2 | Вероятн. | №30 | Diff-aware LLM security review в GitHub Actions с фильтрацией false positives |
| 111 | [highflame-ai/ramparts](https://github.com/highflame-ai/ramparts) | 2 | Смешан. | №26 | Единый Rust scanner MCP и skills: YARA, OSV, LLM, OWASP MCP mapping и SARIF |
| 112 | [HiveTrace/HiveTraceRed](https://github.com/HiveTrace/HiveTraceRed) | — | Red team | №44 | Multilingual regression framework: 80+ jailbreak-атак, async pipeline и evaluators |

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

