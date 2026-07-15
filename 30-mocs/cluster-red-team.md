---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-red-team

## Красное тестирование и fuzzing

> [!NOTE] Общая суть
> Атакующие наборы, регрессионные тесты, orchestration multi-turn атак.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №44 (44-red-team-regression)
- способ №1 (01-классификация-инъекций-машинным-обучением)

## Варианты реализации (20)

- [[repo-104-agentpoison]] — BillChan226/AgentPoison: Red-team: backdoor через poisoning memory/RAG KB (NeurIPS 2024, arXiv:2407.12784)
- [[repo-44-circuit-breakers]] — GraySwanAI/circuit-breakers: «Автоматические выключатели» в весах модели
- [[repo-45-plexiglass]] — kortex-labs/plexiglass: Набор тестов и барьеров для LLM
- [[repo-66-agentdojo]] — ethz-spylab/agentdojo: Атаки и защиты в среде tool-using агентов
- [[repo-68-finbot-ctf]] — GenAI-Security-Project/finbot-ctf: Финансовый агент-мишень для red team
- [[repo-73-inspect-ai]] — UKGovernmentBEIS/inspect_ai: Фреймворк оценки безопасности LLM (UK AISI)
- [[repo-74-inspect-evals]] — UKGovernmentBEIS/inspect_evals: Набор cyber/безопасностных eval
- [[repo-75-agentfence]] — agentfence/agentfence: Runtime-тесты: инъекции, утечки секретов
- [[repo-76-garak]] — NVIDIA/garak: 100+ детекторов уязвимостей LLM
- [[repo-77-pyrit]] — Azure/PyRIT: Оркестрация многоходовых атак
- [[repo-78-promptfoo]] — promptfoo/promptfoo: 50+ плагинов атак, регрессионные тесты
- [[repo-79-agentic-security]] — msoedov/agentic_security: Сканер агентных систем: hijack, tool abuse
- [[repo-80-fuzzyai]] — cyberark/FuzzyAI: Фаззинг jailbreak и prompt injection
- [[repo-81-spikee]] — ReversecLabs/spikee: Набор для оценки и эксплуатации инъекций
- [[repo-82-augustus]] — praetorian-inc/augustus: Single-binary тестирование LLM
- [[repo-83-deepteam]] — confident-ai/deepteam: Red team для LLM-систем
- [[repo-84-moonshot]] — aiverify-foundation/moonshot: Модульный бенчмарк и red team
- [[repo-85-ps-fuzz]] — prompt-security/ps-fuzz: Фаззинг системных промптов
- [[repo-86-llmfuzzer]] — mnns/LLMFuzzer: Фаззинг LLM API-интеграций
- [[repo-87-promptmap]] — utkusen/promptmap: Сканер инъекций white/black-box


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
