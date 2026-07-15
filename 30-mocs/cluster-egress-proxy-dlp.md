---
type: moc
tags:
  - cluster
  - repo-catalog
---

# cluster-egress-proxy-dlp

## Egress-прокси и DLP исходящего трафика

> [!NOTE] Общая суть
> Единая точка исходящих HTTP/MCP/A2A с DLP, SSRF-защитой и аудитом.

Несколько репозиториев реализуют **одну идею** разными способами (язык, точка встраивания, зрелость). Каждый вариант — отдельная заметка `repo-NN-*`; связь на графе: **кластер → реализация → способ**.

## Связанные способы

- способ №23 (23-единый-прокси-исходящих-запросов-и-защита-от-ssrf)
- способ №6 (06-content-dlp-inspection)
- способ №7 (07-выявление-секретов-в-тексте)
- способ №39 (39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями)

## Варианты реализации (10)

- [[repo-02-pipelock]] — luckyPipewrench/pipelock: Прокси исходящего трафика: MCP, DLP, криптографические квитанции аудита
- [[repo-06-zerotrust-agents]] — lokeshsk/zerotrust-agents: Zero-trust прокси между агентом и API
- [[repo-18-defenseclaw]] — cisco-ai-defense/defenseclaw: CodeGuard, песочница, SSRF-защита реестра, аудит
- [[repo-57-pipelock-verify-python]] — luckyPipewrench/pipelock-verify-python: Верификатор криптографических квитанций Pipelock
- [[repo-70-agent-egress-bench]] — luckyPipewrench/agent-egress-bench: Корпус для оценки egress-контроля
- [[repo-94-agentguard]] — MukundaKatta/agentguard: Контроль сетевого egress агента
- [[repo-99-presidio]] — microsoft/presidio: Детекция и анонимизация ПДн в потоках агента


- [[repo-106-dvalincode]] — arthurpanhku/dvalincode: Coding-agent runtime сводит машинную и репозиторную политики сужением разрешений, проверяет операции в единой точке вызо
- [[repo-111-h5i]] — h5i-dev/h5i: Rust CLI создаёт Git-addressed environments для агентов, выбирает наиболее сильный доступный isolation tier, фиксирует p
- [[repo-112-onecli]] — onecli/onecli: OneCLI ставит HTTP(S)-шлюз между агентом и внешними API. Агент использует placeholder и собственный access token, а шлюз

## Навигация

- [[github-100-repo]] — полный каталог 118 репозиториев
- [[MOC — Кластеры репозиториев]] — все семейства
