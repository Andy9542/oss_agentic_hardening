# 07. Батч 3 (Сеть / Supply chain / Код): аудит карточек

> **Дата:** 2026-07-08

## Вердикт

**Батч 3 закрыт.** 5 карточек, старт с №28.

| № | Файл | Тип | Несущее |
|---|------|-----|---------|
| 28 | `claude/card-28-toxic-flow-analysis.md` | полная | §4+§8 |
| 26 | `claude/card-26-tool-poisoning-scan.md` | полная | §4 |
| 24 | `claude/card-24-mcp-gateway-rbac.md` | экспресс | §3 |
| 30 | `claude/card-30-static-analysis-code.md` | экспресс | §4 |
| 32 | `claude/card-32-aibom-inventory.md` | экспресс | §8 |

## Ключевые проверки

- №28: триада №15/№28/№16 раскрыта.
- №26: agentseal без подписи; metadata only.
- №24: CEL на gateway, не в №12.
- №30: Cisco scanners → №26.
