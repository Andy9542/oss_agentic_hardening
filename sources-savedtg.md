---
type: source
tags:
  - inbox
  - savedtg
---

# Inbox: источники из saved Telegram

Сверка с обзором: `all-methods-top-20.md`, `description-top-20.md`, `github-100-repo.md`, vault (`10-methods/`, `20-implementations/`, `40-sources/`). Дата сверки: 2026-07-15.

> Нумерация актуализирована после слияния предыдущего дополнения: основной каталог уже содержал 116 уникальных репозиториев. Дубли №101–104 исправлены; новые позиции продолжают каталог как №117–119.

## Статусы

| Источник | URL | В основном обзоре | Действие |
|----------|-----|-------------------|----------|
| destructive_command_guard (dcg) | https://github.com/Dicklesworthstone/destructive_command_guard | да | [[source-destructive-command-guard]], [[impl-destructive-command-guard]], `github-100-repo` №117 |
| Habr / GhostCommit: PNG → утечка секретов | https://habr.com/ru/articles/1058368/ | источник атаки | [[source-habr-ghostcommit]] |
| T3MP3ST | https://github.com/elder-plinius/T3MP3ST | нет | **red-team трек** (отложен): [[source-t3mp3st]], [[impl-t3mp3st]] |
| Strix | https://github.com/usestrix/strix | нет | **red-team трек** (отложен): [[source-strix]], [[impl-strix]] |
| AIRQ report | https://airiskquadrant.com/report | источник | [[source-airq-report]]; отчёт, не OSS |
| SAIL (Pillar) | https://www.pillar.security/sail | источник | [[source-sail-framework]]; framework/продуктовый материал, не OSS |
| Bumblebee | https://github.com/perplexityai/bumblebee | да | [[source-bumblebee]], [[impl-bumblebee]], `github-100-repo` №118 |
| awesome-ai-security-tools | https://github.com/scadastrangelove/awesome-ai-security-tools | да (meta) | [[source-awesome-ai-security-tools]], №119; diff: [[source-awesome-ai-security-tools-diff]] |

## Diff: awesome-ai-security-tools vs github-100-repo

Источник: [scadastrangelove/awesome-ai-security-tools](https://github.com/scadastrangelove/awesome-ai-security-tools) README.

| Метрика | Значение |
|---------|----------|
| Уникальных `github.com/*` в awesome-list | 239 |
| Уже в `github-100-repo.md` | 55 |
| Отсутствуют в каталоге | 184 |

Пункты из этого inbox в awesome-list:

| Репозиторий | В awesome-list | Трек |
|-------------|----------------|------|
| `elder-plinius/T3MP3ST` | да | **red-team** (отложен, не в основном каталоге) |
| `usestrix/strix` | да | **red-team** (отложен, не в основном каталоге) |
| `Dicklesworthstone/destructive_command_guard` | нет | **основной обзор** №117 |
| `perplexityai/bumblebee` | нет | **основной обзор** №118 |
| `scadastrangelove/awesome-ai-security-tools` | нет (сам каталог) | **основной обзор** №119 (meta) |

Примеры отсутствующих в нашем каталоге: `DataDog/guarddog`, `Giskard-AI/giskard-oss`, `PortSwigger/ai-prompt-fuzzer`, `ReversecLabs/damn-vulnerable-llm-agent`, `MCP-Defender/MCP-Defender`, `NVISOsecurity/cyber-security-llm-agents`, `GreyDGL/PentestGPT`, `apiiro/malicious-code-ruleset`, `Tencent/AI-Infra-Guard`.

Полный список из 184 URL — [[source-awesome-ai-security-tools-diff]].

## Red team трек (отдельный, позже)

Не включаем T3MP3ST и Strix в основной каталог сейчас. Карточки сохранены в vault:

- [[source-t3mp3st]] / [[impl-t3mp3st]]
- [[source-strix]] / [[impl-strix]]

Связанный способ: [[44-red-team-regression]]. В каталоге уже есть блок красного тестирования (garak, PyRIT, promptfoo, …).

## Связи

- Каталог: [[github-100-repo]]
- Red team: [[44-red-team-regression]]
- Shell / аргументы: [[19-правила-против-инъекций-в-аргументах-инструментов]]
- Inventory supply chain: [[32-aibom-inventory]]
