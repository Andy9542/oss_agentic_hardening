---
type: repo-catalog
catalog-id: 105
method-id: 27
also-method-ids:
  - 3
  - 4
  - 7
  - 28
  - 29
  - 30
repo: https://github.com/pezhik/skilltotal
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
  - cluster-artifact-trust
---

# pezhik/skilltotal — каталог №105

## Репозиторий

- [pezhik/skilltotal](https://github.com/pezhik/skilltotal)
- Проверенный срез: [`7905d363ef9bb525ebb119cbc008e961c4517a5f`](https://github.com/pezhik/skilltotal/commit/7905d363ef9bb525ebb119cbc008e961c4517a5f), 2026-07-09.
- Лицензия: [Apache-2.0](https://github.com/pezhik/skilltotal/blob/7905d363ef9bb525ebb119cbc008e961c4517a5f/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Детерминированный SAST |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-static-code-sast]], [[cluster-artifact-trust]] |

## Принцип работы

Локально и без исполнения исследуемого компонента индексирует skills, MCP-серверы, npm/PyPI-пакеты и проекты, затем объединяет regex-правила, Python AST, корреляцию потоков и evidence-anchored findings.

## Алгоритм

Коллектор нормализует локальный путь, Git URL, архив или пакет; `file_index.py` один раз читает допустимые файлы; реестр `scanners/` выдаёт findings и `needs_review`; `engine.py` применяет baseline, выделяет capabilities и рассчитывает score. Основной механизм — **способ №27**; дополнительно реализуются способы №3, №4, №7, №28, №29 и №30.

## Вариант в семействе

В отличие от SkillSpector, движок SkillTotal не использует LLM и runtime-зависимости, анализирует не только skills и сохраняет строгий инвариант «finding только с файлом, строками и фрагментом». В отличие от Ramparts, он не подключается к живому MCP endpoint и не выполняет LLM-анализ; в отличие от MCP Armor, baseline относится к findings, а не к SHA-512-снимку MCP metadata.

## Детерминизм или машинное обучение

Статический OSS-движок детерминирован: Python stdlib, regex и AST; код компонента не исполняется.

## Вердикт

**экспериментально** — функционально полный локальный scanner с CI, SARIF, baseline/diff и тестами, но молодой проект без независимого benchmark и без runtime containment.

## Детальные разборы

- [[impl-skilltotal]]
- [[skilltotal-taint-correlation]]
- [[skilltotal-baseline-guard]]

## Реализуемые способы

- [[27-статическая-проверка-навыков-и-плагинов]] — основной
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[04-unicode-normalization]]
- [[07-выявление-секретов-в-тексте]]
- [[28-toxic-flow-analysis]]
- [[29-проверка-зависимостей-ci-и-сценариев-установки]]
- [[30-static-analysis-code]]
