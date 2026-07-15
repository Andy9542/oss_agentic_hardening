---
type: implementation-detail
parent-repo: repo-53-agent-sandbox
method-id: 33
repo: https://github.com/kubernetes-sigs/agent-sandbox
language: Go
license: Apache-2.0
verdict: experimental
commit-sha: 6a15819
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# kubernetes-sigs/agent-sandbox — Sandbox CRD в Kubernetes

## Репозиторий

- [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
- Проверенный срез: `6a15819`; код проверен 2026-07-15.

## Что это за технология

**Kubernetes SIG проект**: CRD/controllers для ephemeral agent sandboxes в кластере — изоляция workloads агента через k8s primitives (pods, network policies). Способ №33 для cloud-native.

## Где в коде

- README — Sandbox API concepts
- Go controllers / CRD YAML under repo

## Алгоритм

1. Применить Sandbox CR.
2. Controller создаёт изолированный pod/workload.
3. Agent tools exec внутри sandbox namespace.
4. TTL/cleanup после session.

## Примеры реализации

Declarative: `kind: Sandbox` → scheduled isolated pod; NetworkPolicy ограничивает egress.

## Пример: вход → решение

- Agent SSRF к metadata IP → blocked NetworkPolicy.
- Job completes → sandbox deleted.

## Детерминизм или машинное обучение

**Детерминированный** k8s control plane.

## Внешние зависимости

Kubernetes cluster; privileges to install CRDs.

## Ограничения

- Ops complexity; cluster trust model.
- Не desktop/dev laptop out of box.

## Сигналы качества

- kubernetes-sigs governance; active commits.

## Вердикт

**экспериментально** — стандартный путь sandbox в k8s.

## Связи

- Репозиторий: [[repo-53-agent-sandbox]]
