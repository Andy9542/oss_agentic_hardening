---
type: implementation-detail
parent-repo: repo-61-aibom-generator
method-id: 32
repo: https://github.com/GenAI-Security-Project/aibom-generator
language: Python
license: Apache-2.0
verdict: experimental
commit-sha: c5a3f2f
commit-date: 2026-04-27
verified-date: 2026-07-15
tags:
  - agent-security
---

# OWASP AIBOM Generator — CycloneDX 1.6 для моделей

## Репозиторий

- [GenAI-Security-Project/aibom-generator](https://github.com/GenAI-Security-Project/aibom-generator)
- Проверенный срез: `c5a3f2f`; код проверен 2026-07-15.

## Что это за технология

Генератор **AI Bill of Materials** из Hugging Face metadata → JSON CycloneDX (`bomFormat: CycloneDX`, `specVersion: 1.6`) + completeness scoring. Способ №32 (AIBOM inventory).

## Где в коде

- `src/models/service.py` — `generate_aibom`
- `src/models/extractor.py` — field lambdas
- `src/models/scoring.py` — validate CycloneDX / SPDX licenses
- `src/models/registry.py` — required_fields profiles

## Алгоритм

1. Указать HF model id.
2. Extract metadata → components/model card fields.
3. Emit AIBOM JSON; validate `bomFormat == CycloneDX`.
4. Score completeness (basic/model_card profiles); recommend missing fields.

## Примеры реализации

```python
'bomFormat': 'CycloneDX',
'specVersion': '1.6',
# scoring: INVALID_BOM_FORMAT if bomFormat != CycloneDX
# required_fields profiles: serialNumber, version, name, …
```

## Пример: вход → решение

- `meta-llama/…` → AIBOM with components + licenses.
- Missing name/version → completeness error + recommendations.

## Детерминизм или машинное обучение

**Детерминированная** extraction/validation (HF API data).

## Внешние зависимости

HF network; web UI owasp-genai-aibom.org.

## Ограничения

- Лучше для open HF models, чем закрытых API.
- Inventory ≠ vulnerability scan.

## Сигналы качества

- CycloneDX Tool Center; OWASP GenAI.

## Вердикт

**экспериментально** — практичный AIBOM generator.

## Связи

- Репозиторий: [[repo-61-aibom-generator]]
