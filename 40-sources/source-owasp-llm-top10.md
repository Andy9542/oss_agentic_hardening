---
type: source
tags:
  - framework
---

# OWASP LLM Top 10

## Суть

Инициатива **OWASP GenAI Security** — десять главных рисков для приложений на **больших языковых моделях** (редакция 2025).

## URL

https://genai.owasp.org/llm-top-10/

## Ключевые выводы

- Каркас для способ №41 и [[MOC — Матрица угроз]]
- У агентов **LLM06** разложен на ASI02, ASI03, ASI05, ASI10 — см. заметки ASI
- Кража весов модели (model theft из старых редакций) в матрице **не** runtime-риск агента

## LLM01–LLM10 (2025)

| Код | English | Русский | Заметка |
|-----|---------|---------|---------|
| LLM01 | Prompt Injection | Инъекция промпта | [[LLM01-prompt-injection]] |
| LLM02 | Sensitive Information Disclosure | Раскрытие конфиденциальной информации | [[LLM02-sensitive-information-disclosure]] |
| LLM03 | Supply Chain | Уязвимости цепочки поставок | [[LLM03-supply-chain]] |
| LLM04 | Data and Model Poisoning | Отравление данных и модели | [[LLM04-data-model-poisoning]] |
| LLM05 | Improper Output Handling | Неправильная обработка вывода | [[LLM05-improper-output-handling]] |
| LLM06 | Excessive Agency | Избыточная автономия | [[LLM06-excessive-agency]] |
| LLM07 | System Prompt Leakage | Утечка системного промпта | [[LLM07-system-prompt-leakage]] |
| LLM08 | Vector and Embedding Weaknesses | Слабости векторов и эмбеддингов | [[LLM08-vector-embedding-weaknesses]] |
| LLM09 | Misinformation | Дезинформация | [[LLM09-misinformation]] |
| LLM10 | Unbounded Consumption | Неограниченное потребление ресурсов | [[LLM10-unbounded-consumption]] |

Пересечения LLM ↔ ASI — в [[MOC — Матрица угроз#ASI и LLM: кто с кем пересекается]].

## Связи

- [[41-сопоставление-защит-с-требованиями-стандартов]]
- [[MOC — Матрица угроз]]
- [[source-owasp-llm-2025]] — заметка чётной ветки о том же стандарте
