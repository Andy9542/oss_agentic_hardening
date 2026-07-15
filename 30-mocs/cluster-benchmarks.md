---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-benchmarks

## Бенчмарки и eval-фреймворки

> [!NOTE] Общая суть
> Измерение устойчивости защит; не барьер в продакшене.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №45 (45-agentdojo-как-эталонный-набор-испытаний)
- способ №44 (44-red-team-regression)

## Варианты реализации (14)

- [[repo-104-agentpoison]] — BillChan226/AgentPoison: Red-team: backdoor через poisoning memory/RAG KB (NeurIPS 2024, arXiv:2407.12784)
- [[repo-66-agentdojo]] — ethz-spylab/agentdojo: Атаки и защиты в среде tool-using агентов
- [[repo-67-injecagent]] — uiuc-kang-lab/InjecAgent: 1054 кейсов косвенных инъекций, 17+62 инструмента
- [[repo-68-finbot-ctf]] — GenAI-Security-Project/finbot-ctf: Финансовый агент-мишень для red team
- [[repo-69-rampart]] — microsoft/RAMPART: Оценка устойчивости агентов Microsoft
- [[repo-70-agent-egress-bench]] — luckyPipewrench/agent-egress-bench: Корпус для оценки egress-контроля
- [[repo-71-open-prompt-injection]] — liu00222/Open-Prompt-Injection: Формализация атак и защит от инъекций
- [[repo-72-jailbreakbench]] — JailbreakBench/jailbreakbench: Открытый бенчмарк jailbreak-устойчивости
- [[repo-73-inspect-ai]] — UKGovernmentBEIS/inspect_ai: Фреймворк оценки безопасности LLM (UK AISI)
- [[repo-74-inspect-evals]] — UKGovernmentBEIS/inspect_evals: Набор cyber/безопасностных eval
- [[repo-75-agentfence]] — agentfence/agentfence: Runtime-тесты: инъекции, утечки секретов
- [[repo-88-bipia]] — microsoft/BIPIA: Бенчмарк и защита от косвенных инъекций


- [[repo-110-piarena]] — sleeepeer/PIArena: Платформа сравнивает prompt-injection атаки и защиты на общих наборах данных, а также запускает агентные сценарии AgentD
- [[repo-116-hivetrace-red]] — HiveTrace/HiveTraceRed: Multilingual red-team framework генерирует jailbreak-промпты, асинхронно опрашивает целевые модели, оценивает ответы и ф

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
