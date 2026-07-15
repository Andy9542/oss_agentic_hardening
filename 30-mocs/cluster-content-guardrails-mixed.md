---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-content-guardrails-mixed

## Смешанные content guardrails

> [!NOTE] Общая суть
> Colang/validators + правила + (опционально) ML; trace-aware политики.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №42 (42-colang-dialog-rails)
- способ №1 (01-классификация-инъекций-машинным-обучением)
- способ №15 (15-правила-последовательности-вызовов-и-потоков-данных)
- способ №5 (05-выявление-и-маскирование-персональных-данных)

## Варианты реализации (14)

- [[repo-08-agent-airlock]] — sattyamjjain/agent-airlock: Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница
- [[repo-29-agentic-radar]] — splx-ai/agentic-radar: Карта потоков данных в LangGraph/CrewAI/n8n
- [[repo-37-purplellama]] — meta-llama/PurpleLlama: LlamaFirewall, CodeShield, CyberSecEval
- [[repo-38-guardrails]] — NVIDIA-NeMo/Guardrails: Программируемые рельсы на Colang
- [[repo-39-guardrails]] — guardrails-ai/guardrails: Валидаторы ввода/вывода, PII, структура
- [[repo-43-langkit]] — whylabs/langkit: Мониторинг инъекций, дрейфа, токсичности
- [[repo-46-invariant]] — invariantlabs-ai/invariant: Анализ трасс агентов, политики на цепочках вызовов
- [[repo-47-invariant-gateway]] — invariantlabs-ai/invariant-gateway: Шлюз с политиками для агентных трасс
- [[repo-98-phoenix]] — Arize-AI/phoenix: Трассировка, eval RAG, галлюцинации
- [[repo-99-presidio]] — microsoft/presidio: Детекция и анонимизация ПДн в потоках агента


- [[repo-107-armorer-guard]] — ArmorerLabs/Armorer-Guard: Один локальный Rust binary нормализует текст, объединяет детерминированные правила, credential detector, TF-IDF linear c
- [[repo-108-parallax]] — agent-defense/parallax: Внешний Rust service принимает lifecycle events агента и прогоняет их через cost-ordered chain из regex, keyword, Sigma,
- [[repo-109-nvidia-skillspector]] — NVIDIA/SkillSpector: LangGraph-конвейер разрешает Git/URL/ZIP/файл, строит общий контекст, параллельно запускает 22 анализатора и передаёт fi
- [[repo-115-ramparts]] — highflame-ai/ramparts: Rust CLI подключается к живым MCP-серверам или читает agent skills, прогоняет данные через structural checks, YARA-X и о

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
