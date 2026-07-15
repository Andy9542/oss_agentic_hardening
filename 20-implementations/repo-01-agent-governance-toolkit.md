---
type: repo-catalog
catalog-id: 1
method-id: 12
also-method-ids:
  - 11
  - 21
  - 22
  - 25
  - 26
  - 32
  - 35
  - 36
  - 37
  - 39
  - 41
repo: https://github.com/microsoft/agent-governance-toolkit
language: Python
license: ""
verdict: prod
tags:
  - agent-security
  - repo-catalog
clusters:
  - cluster-governance-platform
  - cluster-tool-firewall-yaml
  - cluster-llm-gateway
  - cluster-tool-firewall-pdp
  - cluster-supply-chain-scanners
  - cluster-artifact-trust
---

# microsoft/agent-governance-toolkit — каталог №1

## Репозиторий

[microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3+4 |
| Тип | Детерм. |
| Семейства | [[cluster-governance-platform]], [[cluster-tool-firewall-yaml]], [[cluster-llm-gateway]], [[cluster-tool-firewall-pdp]], [[cluster-supply-chain-scanners]], [[cluster-artifact-trust]] |

## Принцип работы

Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK

## Алгоритм

Agent OS: ядро политик, идентичность агента, песочницы, адаптеры для LangGraph/CrewAI/ADK.

Каталожная заметка: основной механизм — **способ №12**; дополнительно перекрывает: способ №11, способ №21, способ №26, способ №32, способ №36, способ №39.

## Вариант в семействе

Платформенный Agent OS: политики, идентичность, sandbox, compliance в одном дистрибутиве. Родственные реализации — только через семейства: платформы governance, YAML-файрволы tools, LLM-шлюзы, PDP-шлюзы, сканеры supply chain, доверие к артефактам.


## Детерминизм или машинное обучение

Тип из каталога: **Детерм.**.

## Вердикт

**готово к продакшену** — каталожная оценка по зрелости репозитория в экосистеме.


## Детальные разборы

- [[agt-agent-compliance]]
- [[agt-execution-rings]]
- [[agt-flight-recorder]]
- [[agt-mcp-scan]]
- [[agt-require-approval]]
- [[agt-token-rate-limits]]
- [[agt-trust-scoring]]
- [[impl-agt-agentmesh]]
- [[impl-agt-runtime]]


## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[11-ограничение-токенов-расходов-и-частоты-вызовов]]
- [[21-одобрение-опасных-действий-человеком]]
- [[22-kill-switch-circuit-breaker]]
- [[25-контроль-целостности-описаний-инструментов]]
- [[26-tool-poisoning-scan]]
- [[32-aibom-inventory]]
- [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
- [[36-crypto-agent-identity]]
- [[37-выявление-поведенческих-отклонений]]
- [[39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями]]
- [[41-сопоставление-защит-с-требованиями-стандартов]]
