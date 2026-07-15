---
type: incident
date: 2023-02-08
incident-kind: production-behavior-disclosure
status: confirmed-by-vendor
affected: "Microsoft Bing Chat"
risk-ids:
  - LLM01
  - LLM07
tags:
  - agent-security
  - incident
  - prompt-injection
  - system-prompt
---

# Bing Chat — раскрытие metaprompt и имени Sydney

## Что произошло

Пользователи раннего Bing Chat использовали прямую prompt injection, чтобы заставить систему игнорировать предыдущие инструкции и вывести скрытый metaprompt: правила поведения, ограничения и внутреннее имя Sydney. Эксперимент был независимо воспроизведён, а представитель Microsoft подтвердил журналистам подлинность metaprompt.

## Статус доказательств

Это подтверждённое поведение production-preview, но не компрометация пользовательских данных. Инцидент показывает раскрытие управляющих инструкций и возможность обойти запрет на их публикацию.

## Связь с рисками

- [[LLM01-prompt-injection]] — пользовательская инструкция получила приоритет над скрытыми правилами.
- [[LLM07-system-prompt-leakage]] — модель дословно раскрыла существенную часть внутреннего metaprompt.

## Последствия и реакция

Microsoft меняла ограничения и metaprompt по мере preview. Защитный вывод: system prompt нельзя считать секретным security boundary; критичные правила должны дублироваться внешним enforcement.

## Источники

- [Ars Technica: первичное раскрытие prompt injection](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/)
- [TIME: воспроизведение раскрытия Sydney и правил](https://time.com/6256529/bing-openai-chatgpt-danger-alignment/)
