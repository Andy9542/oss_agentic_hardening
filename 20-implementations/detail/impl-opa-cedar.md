---
type: implementation-detail
parent-repo: repo-63-opa
method-id: 12
repo: https://github.com/open-policy-agent/opa
language: Go
license: Apache-2.0
verdict: prod
commit-sha: 8e2f180
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# OPA — policy-as-code на Rego (PDP)

## Репозиторий

- [open-policy-agent/opa](https://github.com/open-policy-agent/opa)
- Проверенный срез: `8e2f180`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Что это за технология

**OPA (Open Policy Agent)** — универсальный **Policy Decision Point**: отдельный процесс/библиотека, которая по входному JSON (`input`) и набору правил на языке **Rego** возвращает решение (обычно `allow`/`deny` или произвольный объект).

**Rego** — декларативный язык (Datalog-подобная семантика): правила задают, *когда* решение истинно, без императивных «if в коде приложения». Для агентов это способ №12: политики на tool-call, MCP, HTTP выносятся из промпта в проверяемый артефакт.

Cedar (AWS) — родственный enterprise-подход с другой грамматикой; в этом репозитории канон — OPA/Rego.

## Где в коде

- Движок Rego: пакеты `v1/rego/`, `v1/ast/`, `v1/topdown/`
- Пример политики контейнерной изоляции (ACI): `v1/rego/testdata/aci/policy.rego` + `framework.rego`
- CLI: `opa eval`, `opa test`, `opa run` (сервер `/v1/data/...`)

## Алгоритм

1. Загрузить bundle политик (`.rego` + data JSON).
2. Клиент (агент-шлюз) шлёт `input` — например `{ "tool": "shell.exec", "args": {…}, "user": "…" }`.
3. OPA вычисляет query (`data.agent.allow` или аналог): объединяет правила, где тело истинно.
4. Ответ: boolean / set / object. Enforcement Point (прокси tools) **обязан** исполнить deny — OPA сам ничего не блокирует.
5. Решения детерминированы при фиксированных data+input; частичные правила с `default allow := false` дают default-deny.

## Примеры реализации

Фрагмент духа политик из ACI fixture (`policy.rego`): декларативные списки `containers`, `env_rules` с `strategy: "string" | "re2"`, mounts, capabilities — OPA сверяет runtime-запрос с allowlist слоёв/команд.

Типовой паттерн для tool-firewall (иллюстрация стиля Rego, не файл репозитория агента):

```rego
package agent.authz

default allow := false

allow if {
    input.tool == "filesystem.read"
    startswith(input.args.path, "/workspace/")
}

allow if {
    input.tool == "web.search"
    not contains(lower(input.args.query), "password")
}
```

`default allow := false` = default-deny: неизвестный tool не проходит.

## Пример: вход → решение

- `input = {tool: "shell.exec", …}` при политике только `filesystem.read` → `allow = false`.
- `input = {tool: "filesystem.read", args: {path: "/workspace/a.txt"}}` → `allow = true`.
- `path: "/etc/passwd"` при `startswith … "/workspace/"` → false.

## Детерминизм или машинное обучение

Полностью **детерминированный** (при отсутствии внешних `http.send` в политике).

## Внешние зависимости

- Бинарник OPA или Go-библиотека; без GPU.
- Опционально: OPA Bundle Server, Envoy plugin, Kubernetes admission.

## Ограничения

- Качество = качество написанных Rego; ошибки политики — дыры.
- Сам OPA не изолирует процесс агента — нужен PEP (шлюз).
- Сложные политики требуют `opa test` и code review.

## Сигналы качества

- Крупнейший OSS PDP; тысячи тестов в репозитории.
- Широкое внедрение в k8s/API gateways; для агентов — через AGT, custom PEP.

## Вердикт

**готово к продакшену** — эталон policy-as-code; для агентов связывать с tool-gateway и default-deny.

## Связи

- Репозиторий: [[repo-63-opa]]
