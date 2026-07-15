---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-content-guardrails-ml

## ML-барьеры содержания

> [!NOTE] Общая суть
> Классификаторы prompt injection, jailbreak, токсичности на вводе/выводе.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №1 (01-классификация-инъекций-машинным-обучением)
- способ №3 (03-правила-и-шаблоны-для-выявления-инъекций)
- способ №8 (08-toxicity-moderation)

## Варианты реализации (39)

- [[repo-02-pipelock]] — luckyPipewrench/pipelock: Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита
- [[repo-03-aegis]] — Justin0504/Aegis: Шлюз с PDP: перехват вызовов, RBAC, аудит, SDK на Go/Python
- [[repo-19-bifrost]] — maximhq/bifrost: AI-шлюз с встроенными барьерами и лимитами
- [[repo-25-skill-scanner]] — cisco-ai-defense/skill-scanner: YARA + LLM-судья + dataflow для навыков Codex/Cursor
- [[repo-37-purplellama]] — meta-llama/PurpleLlama: LlamaFirewall, CodeShield, CyberSecEval
- [[repo-38-guardrails]] — NVIDIA-NeMo/Guardrails: Программируемые рельсы на Colang
- [[repo-39-guardrails]] — guardrails-ai/guardrails: Валидаторы ввода/вывода, PII, структура
- [[repo-40-llm-guard]] — protectai/llm-guard: Сканеры prompt injection, токсичности, секретов
- [[repo-41-rebuff]] — protectai/rebuff: Эвристики + LLM-классификатор + canary-токены
- [[repo-42-vigil-llm]] — deadbits/vigil-llm: YARA + векторное сходство для инъекций
- [[repo-43-langkit]] — whylabs/langkit: Мониторинг инъекций, дрейфа, токсичности
- [[repo-44-circuit-breakers]] — GraySwanAI/circuit-breakers: «Автоматические выключатели» в весах модели
- [[repo-45-plexiglass]] — kortex-labs/plexiglass: Набор тестов и барьеров для LLM
- [[repo-46-invariant]] — invariantlabs-ai/invariant: Анализ трасс агентов, политики на цепочках вызовов
- [[repo-47-invariant-gateway]] — invariantlabs-ai/invariant-gateway: Шлюз с политиками для агентных трасс
- [[repo-48-heimdallm]] — amoffat/HeimdaLLM: Middleware-фильтр промптов
- [[repo-49-granite-guardian]] — ibm-granite/granite-guardian: Классификаторы риска для Granite-моделей
- [[repo-59-agent-threat-rules]] — panguard-ai/agent-threat-rules: «Sigma для агентов»: правила детекции угроз
- [[repo-62-prompt-injection-defenses]] — tldrsec/prompt-injection-defenses: Сводка практических защит от инъекций
- [[repo-67-injecagent]] — uiuc-kang-lab/InjecAgent: 1054 кейсов косвенных инъекций, 17+62 инструмента
- [[repo-71-open-prompt-injection]] — liu00222/Open-Prompt-Injection: Формализация атак и защит от инъекций
- [[repo-72-jailbreakbench]] — JailbreakBench/jailbreakbench: Открытый бенчмарк jailbreak-устойчивости
- [[repo-75-agentfence]] — agentfence/agentfence: Runtime-тесты: инъекции, утечки секретов
- [[repo-76-garak]] — NVIDIA/garak: 100+ детекторов уязвимостей LLM
- [[repo-77-pyrit]] — Azure/PyRIT: Оркестрация многоходовых атак
- [[repo-78-promptfoo]] — promptfoo/promptfoo: 50+ плагинов атак, регрессионные тесты
- [[repo-80-fuzzyai]] — cyberark/FuzzyAI: Фаззинг jailbreak и prompt injection
- [[repo-81-spikee]] — ReversecLabs/spikee: Набор для оценки и эксплуатации инъекций
- [[repo-82-augustus]] — praetorian-inc/augustus: Single-binary тестирование LLM
- [[repo-83-deepteam]] — confident-ai/deepteam: Red team для LLM-систем
- [[repo-84-moonshot]] — aiverify-foundation/moonshot: Модульный бенчмарк и red team
- [[repo-85-ps-fuzz]] — prompt-security/ps-fuzz: Фаззинг системных промптов
- [[repo-86-llmfuzzer]] — mnns/LLMFuzzer: Фаззинг LLM API-интеграций
- [[repo-87-promptmap]] — utkusen/promptmap: Сканер инъекций white/black-box
- [[repo-88-bipia]] — microsoft/BIPIA: Бенчмарк и защита от косвенных инъекций
- [[repo-89-autodefense]] — XHMY/AutoDefense: Мультиагентная защита от jailbreak
- [[repo-90-llm-self-defense]] — poloclub/llm-self-defense: Самопроверка: модель детектирует обман
- [[repo-91-baseline-defenses]] — neelsjain/baseline-defenses: Базовые защиты от adversarial-атак
- [[repo-92-prompt-injection-shield]] — MukundaKatta/prompt-injection-shield: Щит от инъекций для агентов


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
