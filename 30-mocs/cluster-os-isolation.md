---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-os-isolation

## Изоляция на уровне ОС (eBPF/IFC)

> [!NOTE] Общая суть
> Контроль потоков информации ядром ОС, не только контейнер.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №16 (16-ifc-capability-taint)
- способ №34 (34-os-sandbox-openshell)

## Варианты реализации (4)

- [[repo-103-openshell]] — NVIDIA/OpenShell: OS-level sandbox: YAML-политики на FS/сеть/syscall, gateway + k3s harness
- [[repo-16-actplane]] — eunomia-bpf/ActPlane: eBPF-контроль потоков информации на уровне ОС
- [[repo-56-camel-prompt-injection]] — google-research/camel-prompt-injection: CaMeL: capability-based контроль + разделение доверенных данных


- [[repo-111-h5i]] — h5i-dev/h5i: Rust CLI создаёт Git-addressed environments для агентов, выбирает наиболее сильный доступный isolation tier, фиксирует p

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
