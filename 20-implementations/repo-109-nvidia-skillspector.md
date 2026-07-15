---
type: repo-catalog
catalog-id: 109
method-id: 27
also-method-ids:
  - 4
  - 25
  - 26
  - 28
  - 29
  - 30
repo: https://github.com/NVIDIA/SkillSpector
language: Python
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-supply-chain-scanners
  - cluster-static-code-sast
  - cluster-content-guardrails-mixed
---

# NVIDIA/SkillSpector — каталог №109

## Репозиторий

- [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- Проверенный срез: [`8f534e2951e0b7d0b8fb8e84832cd3605f95c032`](https://github.com/NVIDIA/SkillSpector/commit/8f534e2951e0b7d0b8fb8e84832cd3605f95c032), 2026-07-14.
- Лицензия: [Apache-2.0](https://github.com/NVIDIA/SkillSpector/blob/8f534e2951e0b7d0b8fb8e84832cd3605f95c032/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Смешанный static + LLM |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-static-code-sast]], [[cluster-content-guardrails-mixed]] |

## Принцип работы

LangGraph-конвейер разрешает Git/URL/ZIP/файл, строит общий контекст, параллельно запускает 22 анализатора и передаёт findings в опциональный LLM meta-analyzer перед score и отчётом.

## Алгоритм

Статика включает 68 паттернов в 17 категориях, Python AST, source-to-sink taint, YARA, OSV и MCP-проверки. LLM-фаза фильтрует и обогащает findings по файлам; baseline удаляет принятые findings перед score. Основной механизм — **способ №27**; дополнительно реализуются способы №4, №25, №26, №28, №29 и №30.

## Вариант в семействе

В отличие от SkillTotal, SkillSpector зависит от LangGraph/YARA и по умолчанию может отправлять содержимое файлов выбранному LLM-провайдеру; зато даёт семантическую перепроверку и отдельные MCP least-privilege/tool-poisoning анализаторы. От Ramparts отличается Python-графом анализа локального skill, а не Rust-клиентом живого MCP-сервера.

## Детерминизм или машинное обучение

Режим `--no-llm` преимущественно детерминирован; полный режим зависит от LLM. OSV lookup сетевой и при недоступности использует сокращённый fallback.

## Вердикт

**экспериментально** — широкий официальный alpha-scanner с unit/integration fixtures и стабильными форматами отчёта, но результат полного режима зависит от внешней модели, а runtime containment отсутствует.

## Детальные разборы

- [[impl-nvidia-skillspector]]
- [[skillspector-taint-analysis]]
- [[skillspector-mcp-rug-pull]]

## Реализуемые способы

- [[27-статическая-проверка-навыков-и-плагинов]] — основной
- [[04-unicode-normalization]]
- [[25-контроль-целостности-описаний-инструментов]]
- [[26-tool-poisoning-scan]]
- [[28-toxic-flow-analysis]]
- [[29-проверка-зависимостей-ci-и-сценариев-установки]]
- [[30-static-analysis-code]]
