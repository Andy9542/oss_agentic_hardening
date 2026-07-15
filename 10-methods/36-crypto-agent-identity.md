---
type: method
id: 36
layer: identity
method-type: D
prod-viable: false
effectiveness: medium
robustness: medium
evidence-level: strong
status: reviewed
tags:
  - agent-security
  - even-batch
sources:
  - source-microsoft-agt
covers:
  - ASI07
  - ASI03
  - ASI10
---

# Crypto agent identity + A2A trust

## Определение

Криптографическая идентичность агента и доверие agent-to-agent: DID, Ed25519, IATP на Signal protocol (X3DH + Double Ratchet), trust score 0–1000 / decay. Не cloud IAM.

## Как это работает пошагово

1. Агент получает DID и ключевую пару.
2. Handshake с другим агентом через IATP.
3. Trust score обновляется; при низком trust — block.
4. pre-tool-call (межагентные сообщения) × inline.

## От чего защищает

- **ASI07** Insecure Inter-Agent Communication.
- **ASI03** при spoofing агента.
- Частично **ASI10** rogue agents.

## От чего НЕ защищает

- Prompt injection; compromised legitimate agent.

## Реализации

```dataview
TABLE verdict AS "Вердикт", repo AS "Репозиторий"
FROM "20-implementations"
WHERE type = "repo-catalog" AND (method-id = this.id OR contains(also-method-ids, this.id))
SORT catalog-id ASC
```

## Доказательная база

- source-microsoft-agt

## Покрытие рисков

| Риск | Сценарий в матрице | Уровень | Почему такая оценка |
|------|--------------------|---------|---------------------|
| ASI07 | Небезопасная связь агентов | **ср.** | Крипто-идентичность и trust handshake. |
| ASI10 | Rogue agent | **ср.** | Trust score и decay. |

## Оценка эффективности

**Средняя** для multi-agent mesh.

## Оценка прочности

**Средняя** — stolen keys, trust gaming.

## Дополняет

- способ №24 (gateway auth)

## Требует

—

## Не заменяет

- способ №18 (ReBAC)

## Сценический тезис

> Crypto identity — паспорт агента в mesh: Ed25519, trust score, decay. Не ловит prompt injection.

## Демо-кандидат

Trust handshake diagram; score drop → block.
