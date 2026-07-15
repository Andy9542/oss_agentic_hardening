---
type: incident
date: 2025-03-06
incident-kind: documented-influence-campaign
status: observed-output-contamination-mechanism-partly-inferred
affected: "Pravda/Portal Kombat web corpus and ten major AI chatbots tested by NewsGuard"
risk-ids:
  - LLM04
  - LLM09
tags:
  - agent-security
  - incident
  - data-poisoning
  - retrieval
  - misinformation
---

# Pravda / Portal Kombat — LLM grooming через массовое наполнение веба

## Что произошло

Сеть Pravda, также известная как Portal Kombat, массово публиковала и агрегировала ложные пророссийские нарративы в десятках стран и языков. Исследователи American Sunlight Project и NewsGuard связали масштаб публикаций с попыткой повлиять не только на людей, но и на поисковые системы, web crawlers и ответы AI-чатботов.

NewsGuard проверила десять крупных чатботов на выборке опровергнутых нарративов сети. Примерно в трети ответов системы воспроизводили эти утверждения; часть ответов прямо ссылалась на сайты Pravda как на источник.

## Статус доказательств

Подтверждены сама coordinated influence campaign, массовое размещение ложных материалов и наблюдаемое попадание нарративов в ответы production-чатботов. Однако публичные данные не позволяют для каждого продукта отделить влияние training data от live web search, retrieval или иных источников контекста.

Поэтому карточка не утверждает, что были отравлены веса конкретной модели. Связь с LLM04 относится к доказанному загрязнению внешнего data/retrieval corpus и наблюдаемому влиянию этого корпуса на ответы.

## Связь с рисками

- [[LLM04-data-model-poisoning]] — атакующая сторона массово наполняла индексируемую информационную среду ложными данными; чатботы затем воспроизводили и в ряде случаев цитировали эти источники. Это подтверждённый пример data/index poisoning, но не доказанное изменение model weights.
- [[LLM09-misinformation]] — production-системы представляли опровергнутые нарративы как факты или как заслуживающие доверия сообщения.

## Последствия и реакция

Кампания показывает, что provenance и reputation источника должны учитываться до помещения документа в search/RAG context. Одних масштабов публикации, SEO-сигналов и повторения текста недостаточно для повышения доверия; необходимы дедупликация, выявление coordinated networks, фактчекинг и явное указание неопределённости ответа.

## Источники

- [NewsGuard Reality Check: исследование влияния сети Pravda на AI-чатботы](https://www.newsguardrealitycheck.com/p/a-well-funded-moscow-based-global)
- [Axios: методика и результаты проверки десяти чатботов](https://www.axios.com/2025/03/06/exclusive-russian-disinfo-floods-ai-chatbots-study-finds)
- [The Washington Post: независимая проверка и разбор LLM grooming](https://www.washingtonpost.com/technology/2025/04/17/llm-poisoning-grooming-chatbots-russia/)
