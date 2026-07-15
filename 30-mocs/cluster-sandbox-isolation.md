---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-sandbox-isolation

## Песочницы и изоляция исполнения

> [!NOTE] Общая суть
> microVM, контейнеры, K8s CRD — ограничение blast radius кода агента.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №33 (33-изоляция-агента-в-микровиртуальных-машинах-и-контейнерах)
- способ №35 (35-уровни-исполнения-и-изоляция-рабочего-каталога)
- способ №34 (34-os-sandbox-openshell)

## Варианты реализации (9)

- [[repo-04-rampart]] — peg/rampart: Файрвол для coding-агентов: политики на файловые и сетевые действия
- [[repo-08-agent-airlock]] — sattyamjjain/agent-airlock: Декоратор для LangChain/CrewAI: валидация аргументов, RBAC, E2B-песочница
- [[repo-103-openshell]] — NVIDIA/OpenShell: OS-level sandbox: YAML-политики на FS/сеть/syscall, gateway + k3s harness
- [[repo-18-defenseclaw]] — cisco-ai-defense/defenseclaw: CodeGuard, песочница, SSRF-защита реестра, аудит
- [[repo-51-e2b]] — e2b-dev/E2B: Firecracker microVM для кода агента (~150 мс)
- [[repo-52-sandbox]] — agent-infra/sandbox: Универсальная песочница для агентов
- [[repo-53-agent-sandbox]] — kubernetes-sigs/agent-sandbox: K8s CRD для изоляции агентов
- [[repo-54-sandboxai]] — substratusai/sandboxai: Облачные песочницы для LLM-агентов
- [[repo-55-openhands]] — All-Hands-AI/OpenHands: Агент с Docker-изоляцией выполнения


## Навигация

- [[github-100-repo]] — полный каталог 100 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
