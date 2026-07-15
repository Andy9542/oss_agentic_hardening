---
type: moc
tags:
  - repo-catalog
---

# MOC — Кластеры репозиториев

Хаб для **семейств** из [[github-100-repo]]: репозитории с пересекающейся сутью, но разной реализацией.

**Граф:** `кластер → repo-NN → detail → способ`. Репозитории **не** связаны между собой напрямую. Один репозиторий может входить в **несколько** семейств, если реализует несколько механизмов.

## Семейства

- [[cluster-static-code-sast]] — SAST кода агентов
- [[cluster-artifact-trust]] — Доверие к артефактам и AIBOM
- [[cluster-benchmarks]] — Бенчмарки и eval-фреймворки
- [[cluster-capability-camel]] — Capability-based контроль (CaMeL)
- [[cluster-content-guardrails-mixed]] — Смешанные content guardrails
- [[cluster-content-guardrails-ml]] — ML-барьеры содержания
- [[cluster-egress-proxy-dlp]] — Egress-прокси и DLP исходящего трафика
- [[cluster-formal-policies]] — Формальные и enterprise политики
- [[cluster-governance-platform]] — Платформы governance агентов
- [[cluster-llm-gateway]] — LLM-шлюзы с guardrails
- [[cluster-mcp-gateway]] — MCP/A2A шлюзы и реестры
- [[cluster-mcp-trust-runtime]] — Runtime trust для MCP
- [[cluster-observability]] — Наблюдаемость и SIEM для агентов
- [[cluster-os-isolation]] — Изоляция на уровне ОС (eBPF/IFC)
- [[cluster-red-team]] — Красное тестирование и fuzzing
- [[cluster-runtime-hooks]] — Runtime hooks coding-агентов
- [[cluster-sandbox-isolation]] — Песочницы и изоляция исполнения
- [[cluster-standards-meta]] — Стандарты, каталоги и meta-инструменты
- [[cluster-supply-chain-scanners]] — Сканеры цепочки поставки агентов
- [[cluster-tool-firewall-pdp]] — PDP-шлюзы и zero-trust прокси
- [[cluster-tool-firewall-yaml]] — YAML/JSON файрволы на границе tool-call

## Покрытие

Все **118** репозиториев имеют каталожную заметку `repo-NN-slug` в `20-implementations/` с полем `catalog-id` и ссылкой на кластер.
