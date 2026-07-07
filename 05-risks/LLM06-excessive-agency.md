---
type: risk
framework: LLM
id: LLM06
tags:
  - owasp
  - llm
---

# LLM06 — Excessive Agency

| | |
|---|---|
| **Код** | `LLM06` |
| **English** | Excessive Agency |
| **Русский** | Избыточная автономия (агентность) |

## Суть

Системе на базе LLM выдано **слишком много полномочий** без пошагового контроля: широкий набор tools, отсутствие human-in-the-loop, возможность необратимых действий. У агентов разбито на [[ASI02-tool-misuse|ASI02]], [[ASI03-identity-privilege-abuse|ASI03]], [[ASI05-unexpected-code-execution|ASI05]], [[ASI10-rogue-agents|ASI10]].

## Пример атаки

Ассистент с правами «читать почту, отвечать, переводить деньги» без лимитов. Любая успешная инъекция сразу ведёт к финансовой операции — нет прослойки approve/deny.

## В матрице

- [[MOC — Матрица угроз#^matrix-row-asi02-single|Опасный вызов tool]]
- [[MOC — Матрица угроз#^matrix-row-asi02-chain|↳ цепочка вызовов]]
- [[MOC — Матрица угроз#^matrix-row-asi03-priv|Эскалация привилегий]]
- [[MOC — Матрица угроз#^matrix-row-asi05-sandbox|Побег из песочницы]]
- [[MOC — Матрица угроз#^matrix-row-asi10-rogue|Rogue agent]]


## Связи

- [[MOC — Матрица угроз]]
- [[source-owasp-llm-2025]]
