---
type: repo-catalog
catalog-id: 115
method-id: 26
also-method-ids:
  - 3
  - 4
  - 7
  - 27
  - 29
  - 30
repo: https://github.com/highflame-ai/ramparts
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-supply-chain-scanners
  - cluster-mcp-trust-runtime
  - cluster-content-guardrails-mixed
---

# highflame-ai/ramparts — каталог №115

## Репозиторий

- [highflame-ai/ramparts](https://github.com/highflame-ai/ramparts)
- Проверенный срез: [`8fc73b56f124e10c5f58d553573d7faf74fde133`](https://github.com/highflame-ai/ramparts/commit/8fc73b56f124e10c5f58d553573d7faf74fde133), 2026-06-23.
- Лицензия: [Apache-2.0](https://github.com/highflame-ai/ramparts/blob/8fc73b56f124e10c5f58d553573d7faf74fde133/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 2 |
| Тип | Смешанный Rust scanner |
| Семейства | [[cluster-supply-chain-scanners]], [[cluster-mcp-trust-runtime]], [[cluster-content-guardrails-mixed]] |

## Принцип работы

Rust CLI подключается к живым MCP-серверам или читает agent skills, прогоняет данные через structural checks, YARA-X и опциональный LLM, добавляет OSV findings и выдаёт terminal/JSON/Markdown/SARIF.

## Алгоритм

Для MCP `MCPScanner` запрашивает tools/resources/prompts и анализирует их metadata; для skills парсер превращает тело в synthetic MCP prompt, проверяет frontmatter, `allowed-tools`, sensitive references и bundle-файлы. YARA findings, LLM issues и OSV advisories сводятся в общий результат. Основной механизм — **способ №26**; дополнительно реализуются способы №3, №4, №7, №27, №29 и №30.

## Вариант в семействе

В отличие от Python-сканеров SkillTotal и SkillSpector, Ramparts поставляется как Rust binary, умеет опрашивать живой MCP endpoint и отдельно валидирует agentskills.io bundles. От MCP Armor отличается YARA-X/LLM-конвейером, OSV для `npx`/`uvx` и более широким skill scanner; при этом тоже не является runtime firewall.

## Детерминизм или машинное обучение

Парсер, эвристики, YARA-X и форматирование детерминированы; OSV зависит от сети, LLM-фаза вероятностна и опциональна.

## Вердикт

**экспериментально** — широкий scanner с Rust-тестами, CI, releases и несколькими форматами вывода, но семантический результат зависит от провайдера, а fail-soft OSV не доказывает отсутствие уязвимостей.

## Детальные разборы

- [[impl-ramparts-highflame]]
- [[ramparts-skill-bundle-scan]]
- [[ramparts-osv-dependency-scan]]

## Реализуемые способы

- [[26-tool-poisoning-scan]] — основной
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[04-unicode-normalization]]
- [[07-выявление-секретов-в-тексте]]
- [[27-статическая-проверка-навыков-и-плагинов]]
- [[29-проверка-зависимостей-ci-и-сценариев-установки]]
- [[30-static-analysis-code]]
