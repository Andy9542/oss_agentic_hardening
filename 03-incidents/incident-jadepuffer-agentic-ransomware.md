---
type: incident
date: 2026-07-06
incident-kind: confirmed-active-exploitation
status: confirmed-researcher-attribution
affected: "Langflow < 1.3.0; downstream Nacos and MySQL"
risk-ids:
  - ASI02
  - ASI03
  - ASI05
  - ASI08
  - ASI10
  - LLM06
tags:
  - agent-security
  - incident
  - active-exploitation
  - ransomware
---

# JadePuffer — агентно оркестрированная атака через Langflow

## Что произошло

Sysdig Threat Research описала атаку на непатченый Langflow через CVE-2025-3248. После первоначального RCE процесс искал и повторно использовал credentials, извлекал данные, двигался к связанным Nacos и MySQL, создал ransom note, зашифровал 1 342 элемента конфигурации Nacos и удалил таблицы. Исследователи атрибутировали оркестрацию LLM-агенту по самокомментируемым payloads и способности исправлять ошибки по ходу выполнения.

## Статус доказательств

Эксплуатация CVE-2025-3248 подтверждена включением в CISA KEV; NVD отмечает active exploitation и unauthenticated RCE до Langflow 1.3.0. Утверждение об агентной оркестрации — вывод Sysdig по конкретному образцу, а не независимая атрибуция личности оператора. Поэтому карточка разделяет подтверждённую эксплуатацию уязвимости и исследовательскую атрибуцию автономности.

## Связь с рисками

- [[ASI02-tool-misuse]] — агент последовательно использовал shell, базы и сетевые инструменты для вредоносной цели.
- [[ASI03-identity-privilege-abuse]] — найденные API, cloud и database credentials использовались для расширения доступа.
- [[ASI05-unexpected-code-execution]] — первичный доступ и последующие действия включали произвольное выполнение кода.
- [[ASI08-cascading-failures]] — компрометация одного Langflow перешла в связанные Nacos/MySQL и разрушение конфигурации.
- [[ASI10-rogue-agents]] — наблюдалось длительное автономное вредоносное поведение с адаптацией к ошибкам.
- [[LLM06-excessive-agency]] — широкий набор полномочий позволил агенту пройти цепочку от разведки до destructive action без промежуточного контроля.

## Последствия и реакция

Кейс показывает, что известный RCE в AI-платформе может стать входом для масштабируемого агентного оператора. Защита требует своевременного patching, изоляции workflow runtime, короткоживущих credentials, egress-контроля и обнаружения цепочек действий, а не только отдельных команд.

## Источники

- [NVD: CVE-2025-3248 и статус CISA KEV](https://nvd.nist.gov/vuln/detail/CVE-2025-3248)
- [Business Insider: разбор наблюдений Sysdig](https://www.businessinsider.com/ai-ransomware-attack-sysdig-jade-puffer-2026-7)
- [TechRadar: техническая сводка атаки](https://www.techradar.com/pro/security/experts-warn-of-the-first-documented-case-of-agentic-ransomware-dangerous-jadepuffer-attack-run-entirely-by-an-llm)
