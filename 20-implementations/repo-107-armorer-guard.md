---
type: repo-catalog
catalog-id: 107
method-id: 1
also-method-ids:
  - 3
  - 4
  - 6
  - 7
  - 19
repo: https://github.com/ArmorerLabs/Armorer-Guard
language: Rust
license: MIT
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-content-guardrails-ml
  - cluster-content-guardrails-mixed
  - cluster-mcp-trust-runtime
  - cluster-tool-firewall-pdp
---

# ArmorerLabs/Armorer-Guard — каталог №107

## Репозиторий

- [ArmorerLabs/Armorer-Guard](https://github.com/ArmorerLabs/Armorer-Guard)
- Проверенный срез: [`674eb1009a56b50a54bc28163ea99e55c57f9d2a`](https://github.com/ArmorerLabs/Armorer-Guard/commit/674eb1009a56b50a54bc28163ea99e55c57f9d2a), 2026-06-22.
- Лицензия: [MIT](https://github.com/ArmorerLabs/Armorer-Guard/blob/674eb1009a56b50a54bc28163ea99e55c57f9d2a/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 1 |
| Тип | Локальный гибридный guard |
| Семейства | [[cluster-content-guardrails-ml]], [[cluster-content-guardrails-mixed]], [[cluster-mcp-trust-runtime]], [[cluster-tool-firewall-pdp]] |

## Принцип работы

Один локальный Rust binary нормализует текст, объединяет детерминированные правила, credential detector, TF-IDF linear classifiers, policy context и локальную feedback overlay; stdio MCP proxy применяет verdict до передачи `tools/call`.

## Алгоритм

Scanner строит варианты текста после декодирования и нормализации, запускает credential, semantic, similarity, policy, review и learning lanes и возвращает JSON с причинами, confidence и sanitized text. Production-профиль использует Rust-native word TF-IDF model; high-recall профиль может добавить char-wb classifier. Основной механизм — **способ №1**; дополнительно реализуются способы №3, №4, №6, №7 и №19.

## Вариант в семействе

В отличие от cloud guardrails, основной путь не делает сетевых запросов и может работать как тёплый JSONL sidecar. Guard не исполняет tools и не заменяет sandbox или систему авторизации; MCP proxy поддерживает line-delimited stdio JSON-RPC.

## Детерминизм или машинное обучение

Credential patterns, redaction, normalization и policy rules детерминированы. Semantic lane использует локальные линейные TF-IDF classifiers, а learning lane сравнивает с локальными exemplars без online mutation весов.

## Вердикт

**экспериментально** — функционально богатый local-first guard с тестами и явной границей Rust scanner, но benchmark в основном собственный, а лёгкая модель и новый runtime proxy нуждаются в независимой оценке.

## Детальные разборы

- [[impl-armorer-guard]]
- [[armorer-guard-credential-redaction]]
- [[armorer-guard-mcp-proxy]]

## Реализуемые способы

- [[01-классификация-инъекций-машинным-обучением]] — основной
- [[03-правила-и-шаблоны-для-выявления-инъекций]]
- [[04-unicode-normalization]]
- [[06-content-dlp-inspection]]
- [[07-выявление-секретов-в-тексте]]
- [[19-правила-против-инъекций-в-аргументах-инструментов]]
