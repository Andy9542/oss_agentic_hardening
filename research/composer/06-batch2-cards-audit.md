# 06. Батч 2 (Действие): аудит карточек

> **Дата:** 2026-07-08

## Вердикт

**Батч 2 закрыт.** 5 карточек + эталон №16. Все соответствуют v1.1.

| № | Файл | Тип | Несущее | §12 |
|---|------|-----|---------|-----|
| 14 | `claude/card-14-default-deny.md` | экспресс | §8 | пусто |
| 12 | `claude/card-12-tool-policies.md` | полная | §4+§6 | есть |
| 18 | `claude/card-18-rebac-spicedb.md` | экспресс | §4 | карта |
| 20 | `claude/card-20-ghost-args.md` | экспресс | §5 | мини |
| 22 | `claude/card-22-kill-switch-circuit-breaker.md` | экспресс | §2+§4 | split-screen |
| 16 | `preflight/card-16-ifc-taint.md` | полная | §4 | есть |

## Матрица (механическая)

```
№14 | Действие | превентивный | экспресс | §8 | pre-tool-call | архит. | ASI02/03 косв.; LLM06 | M/M/L | adopt/hold | есть | пусто
№12 | Действие | превентивный | полная   | §4+§6 | pre-tool-call | inline | ASI02, ASI03; LLM06 | H/M/M | adopt/trial | есть | есть
№18 | Действие | превентивный | экспресс | §4 | pre-tool-call | inline | ASI03; частично ASI02 | M/M/M | adopt/trial | есть | есть
№20 | Действие | превентивный | экспресс | §5 | pre-tool-call | inline | LLM05; частично ASI02 | L/L/L | adopt/hold | есть | мини
№22 | Действие | реактивный   | экспресс | §2+§4 | post-factum/continuous | inline/архит. | ASI08; частично ASI10 | L/M/L | adopt/trial | есть | есть
```

## Замечания

- №12: Progent SMT с пином v3; CEL → №24.
- №20: factcheck #1 OPEN — Firecracker/Docker не в карточке.
- №22: расщепление 22a/22b по К4.
