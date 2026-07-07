# Исследование: №46* Защита памяти агента

> **Дата:** 2026-07-08  
> **Статус:** Материалы для карточки

## Краткое резюме

Класс №46* закрывает пробел V5: **долговременная память и RAG knowledge base** как вектор атаки, вне периметра пофлоуных меток №16 одной сессии. Якорь атаки — **AgentPoison** (arXiv:2407.12784, NeurIPS 2024) [1]: backdoor через poisoning memory/RAG с optimized trigger, ASR >80% при poison ratio <0.1% [1]. OWASP Agentic Top 10 2026: **ASI06 Memory & Context Poisoning** [2].

Граница: **context poisoning** (одна сессия, in-context) ≠ **memory poisoning** (persistent store); №16 не покрывает ASI06 по handoff.

## Якорь AgentPoison

| Параметр | Значение |
|----------|----------|
| Paper | arXiv:2407.12784 (v1, 17 Jul 2024) |
| Venue | NeurIPS 2024 [3] |
| Repo | https://github.com/BillChan226/AgentPoison |
| Механизм | Poison long-term memory / RAG KB; constrained trigger optimization |
| Метрики | ~82% ASR-retrieval, ~63% end-to-end; <0.1% poison ratio; <1% benign drop [1] |

Progent тестируется на AgentPoison benchmark `[проверено]` по handoff — защита через privilege control на действия после retrieval.

## Границы классов

| Класс | Объект | Отличие от №46* |
|-------|--------|-----------------|
| №1 PI-детект | Ввод сессии | Не память |
| №10 Schema | Форма вывода | Не provenance памяти |
| №16 IFC | Потоки данных сессии | Не persistent memory |
| №46* | Memory/RAG store | ASI06, write + retrieve time |

## Threat model (черновик для карточки)

**Закрывает (целевые митигации):**
- Poisoned entries в long-term memory / RAG
- Retrieval без provenance validation
- ASI06 Memory & Context Poisoning (persistent часть)

**НЕ закрывает:**
- In-session PI без записи в память
- Poison ниже порога детекции
- Semantic-only attacks без stored trigger

## Точки врезки

- **pre-write** — валидация перед записью в memory
- **retrieval-time** — фильтр/score при retrieve
- **provenance/TTL** — архитектурное свойство хранилища

## Источники

1. https://arxiv.org/abs/2407.12784 — AgentPoison paper
2. `preflight/stage0-preflight-results.md` — ASI06 в OWASP Agentic Top 10 2026
3. https://proceedings.neurips.cc/paper_files/paper/2024/file/eb113910e9c3f6242541c1652e30dfd6-Paper-Conference.pdf — NeurIPS 2024
