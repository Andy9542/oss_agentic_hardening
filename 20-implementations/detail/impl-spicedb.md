---
type: implementation-detail
parent-repo: repo-102-spicedb
method-id: 18
repo: https://github.com/authzed/spicedb
language: Go
license: Apache-2.0
verdict: готово к продакшену
tags:
  - agent-security
---

# SpiceDB — способ №18

## Репозиторий

https://github.com/authzed/spicedb — Google Zanzibar-style ReBAC.

## Алгоритм

CheckPermission на графе отношений user→agent→tool перед вызовом.

## Вердикт

**готово к продакшену** — enterprise ReBAC.

## Связи

- Репозиторий: [[repo-102-spicedb]]
