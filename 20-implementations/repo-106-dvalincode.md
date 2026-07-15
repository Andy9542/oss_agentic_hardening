---
type: repo-catalog
catalog-id: 106
method-id: 12
also-method-ids:
  - 14
  - 21
  - 23
  - 30
  - 35
  - 39
repo: https://github.com/arthurpanhku/dvalincode
language: TypeScript
license: MIT
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-tool-firewall-yaml
  - cluster-sandbox-isolation
  - cluster-egress-proxy-dlp
  - cluster-static-code-sast
  - cluster-observability
---

# arthurpanhku/dvalincode — каталог №106

## Репозиторий

- [arthurpanhku/dvalincode](https://github.com/arthurpanhku/dvalincode)
- Проверенный срез: [`d47516748f2acfc75111ca150ca2eda607187f82`](https://github.com/arthurpanhku/dvalincode/commit/d47516748f2acfc75111ca150ca2eda607187f82), 2026-07-15.
- Лицензия: [MIT](https://github.com/arthurpanhku/dvalincode/blob/d47516748f2acfc75111ca150ca2eda607187f82/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Смешанный runtime |
| Семейства | [[cluster-tool-firewall-yaml]], [[cluster-sandbox-isolation]], [[cluster-egress-proxy-dlp]], [[cluster-static-code-sast]], [[cluster-observability]] |

## Принцип работы

Coding-agent runtime сводит машинную и репозиторную политики сужением разрешений, проверяет операции в единой точке вызова tools, управляет сетевым выходом и сохраняет проверяемый журнал; отдельный Dvalin flow запускает сканирование, исправление и повторную проверку.

## Алгоритм

Zod-схема загружает policy layers, пересекает allowlists, объединяет denylists и выбирает наиболее строгие network и budget limits. Реестр tools сначала применяет policy targets, затем approval mode; MCP-запросы идут через governed fetch. События записываются в hash-chained JSONL, а remediation suite объединяет встроенный scanner, Semgrep, Trivy, OSV-Scanner и SARIF. Основной механизм — **способ №12**; дополнительно реализуются способы №14, №21, №23, №30, №35 и №39.

## Вариант в семействе

DvalinCode объединяет enforcement и агентный workflow в одном TypeScript/Bun runtime. Политика локального администратора tamper-evident, но не tamper-proof; сила process sandbox зависит от ОС, а security remediation остаётся частично вероятностным LLM-процессом.

## Детерминизм или машинное обучение

Разрешения, policy narrowing, approvals, egress checks, scanner orchestration и audit-chain verification детерминированы. Планирование, исправление кода и часть оценки findings зависят от LLM и внешних сканеров.

## Вердикт

**экспериментально** — хорошо разложенный policy-bound runtime с тестами chokepoints и аудита, но платформозависимая изоляция и быстро меняющийся агентный контур требуют независимой проверки.

## Детальные разборы

- [[impl-dvalincode]]
- [[dvalincode-remediation-suite]]
- [[dvalincode-hash-chain-audit]]

## Реализуемые способы

- [[12-tool-policies-yaml-rego]] — основной
- [[14-default-deny-allowlists]]
- [[21-одобрение-опасных-действий-человеком]]
- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
- [[30-static-analysis-code]]
- [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
- [[39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями]]
