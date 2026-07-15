---
type: implementation-detail
parent-repo: repo-25-skill-scanner
method-id: 27
repo: https://github.com/cisco-ai-defense/skill-scanner
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: 41fec4a
commit-date: 2026-06-29
verified-date: 2026-07-15
tags:
  - agent-security
---

# skill-scanner — YARA-правила для навыков агента

## Репозиторий

- [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- Проверенный срез: `41fec4a`, дата коммита 2026-06-29; код проверен 2026-07-15.

## Что это за технология

**YARA** — язык сигнатур (как антивирусные правила): `strings` (текст/regex) + `condition` (булева логика). skill-scanner применяет pack `.yara` к файлам навыков (SKILL.md, scripts) Codex/Cursor/OpenClaw, плюс LLM-судью и dataflow. Это способ №27 (статическая проверка навыков).

## Где в коде

- Правила: `skill_scanner/data/packs/core/yara/*.yara`
- Реестр: pack.yaml + `tests/test_rule_registry.py`
- Примеры файлов: `prompt_injection_generic.yara`, `jailbreak_generic.yara`, `credential_harvesting_generic.yara`, …

## Алгоритм

1. Загрузить core pack (и опциональные packs).
2. Обойти файлы skill bundle.
3. Скомпилировать YARA rules → scan bytes/text.
4. Сопоставить hits с metadata (threat_type, classification).
5. Агрегировать с LLM-judge / dataflow findings → отчёт severity.

## Примеры реализации

Из `prompt_injection_generic.yara`:

```text
$instruction_override_strong = /\b(Bypass|Dis\W?gard|Forget|Ignore)\s+(all|any|every)\s+…(previous|prior|above|earlier)…(instruction|…|system\s*prompt)/i
$instruction_override_your = /\b(Bypass|…|Ignore)\s+(your|the\s+system('s)?)\s+(…instruction…)/i
$do_not_obey = /\bDo\s+not\s+(follow|obey)\s+(the\s+)?(previous|…|system)\s+(instruction|…)/i
$shadow_parameters = /\b(internalOnly|hiddenParam|shadowTool|bypassChecks|sandboxEscape)\b/i
```

Исключения FP: `# type: ignore`, `ignore_case` / `ignore_errors`.

Из `jailbreak_generic.yara`: `$dan_explicit` на `you are DAN` / `enable DAN mode`; `$persona_unrestricted` на uncensored/unrestricted AI persona.

## Пример: вход → решение

- SKILL.md содержит `Ignore all previous instructions` → rule `prompt_injection_generic` hit → harmful.
- Легитимный `# type: ignore` в Python → не матчит благодаря exclude strings.

## Детерминизм или машинное обучение

YARA — **детерминированный**; LLM-судья — вероятностный.

## Внешние зависимости

Python + yara-python; опционально LLM API.

## Ограничения

- Сигнатуры устаревают; обход парафразом.
- Нужен scan до install skill.

## Сигналы качества

- Тесты registry: каждая YARA rule должна быть в pack.yaml.

## Вердикт

**экспериментально** — сильный signature pack для skill supply chain.

## Связи

- Репозиторий: [[repo-25-skill-scanner]]
