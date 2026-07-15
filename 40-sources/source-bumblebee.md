---
type: source
tags:
  - docs
  - savedtg
  - supply-chain
---

# Perplexity Bumblebee

## Суть

Bumblebee — read-only inventory collector для macOS и Linux developer endpoints. Он собирает локальные метаданные пакетов, lock-файлов, расширений редакторов/браузеров и поддерживаемых MCP-конфигураций, а затем при наличии exposure catalog отмечает точные совпадения с известной кампанией или advisory.

## URL

https://github.com/perplexityai/bumblebee

## Ключевые выводы

- Отвечает на узкий incident-response вопрос: на каких машинах сейчас виден известный пакет, расширение или версия.
- Не запускает package managers и не читает исходный код; выводит нормализованные NDJSON component/finding records.
- Значения секретов из `env`-блоков MCP-конфигов не включаются в записи.
- Без заранее подготовленного exposure catalog это inventory, а не детектор неизвестного вредоносного поведения.
- Проект новый; встроенный self-test проверяет end-to-end обнаружение на безопасных фикстурах.

## Связи

- [[32-aibom-inventory]]
- [[repo-118-bumblebee]]
