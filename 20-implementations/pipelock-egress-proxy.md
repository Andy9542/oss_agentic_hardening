---
type: implementation
method-id: 23
repo: https://github.com/luckyPipewrench/pipelock
language: Go
license: Apache-2.0
verdict: prod
tags: [agent-security]
---

# Pipelock — прокси исходящего трафика и SSRF

## Репозиторий

[luckyPipewrench/pipelock](https://github.com/luckyPipewrench/pipelock) — один Go-бинарник (~20 МБ), без нейросетей.

## Где в коде

- Команды: `pipelock proxy`, `pipelock mcp proxy -- npx server`
- Слои конвейера описаны в README и [[description-top-20#2. Pipelock]]

## Алгоритм (11 слоёв, смысл каждого)

| № | Слой | Что делает |
|---|------|------------|
| 1 | Схема URL | Только http/https |
| 2 | CRLF | Инъекция в заголовки через URL |
| 3 | Path traversal | `../`, чувствительные пути |
| 4 | Чёрный список доменов | Известные exfil-хосты |
| 5 | DLP | 48 шаблонов секретов **до DNS** |
| 6 | Энтропия | Медленная утечка по частям |
| 7 | SSRF | Блок внутренних адресов |
| 8 | DNS rebinding | Повторная проверка IP |
| 9 | Лимиты | Частота и объём на домен |
| 10 | Ответ | Инъекции в HTML/MCP-ответах |
| 11 | MCP | Rug-pull, confused deputy |

**Принцип разделения:** процесс агента **не имеет** сырого сетевого доступа; весь трафик через Pipelock. Иначе агент обойдёт прокси отдельным сокетом.

## Детерминизм или машинное обучение

Полностью **детерминированный**. Режим **«закрыто при ошибке»**: таймаут, битый ответ, нечитаемое сжатие → блок.

## Внешние зависимости

Нет. Квитанции аудита Ed25519 — локально.

## Вердикт

**готово к продакшену** — эталон egress-архитектуры при **обязательной** сетевой изоляции агента (Docker `internal: true`, NetworkPolicy в Kubernetes).

## Связи

- Способ: [[23-egress-proxy-ssrf]]
