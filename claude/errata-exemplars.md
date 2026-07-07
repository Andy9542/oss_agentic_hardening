# Errata к эталонам (§4-перепин на OWASP LLM Top 10 2025)

Причина: оба пилота размечены нумерацией OWASP-2023 (LLM02 = Insecure Output Handling, LLM06 = Sensitive Information Disclosure). Актуальная — 2025 (см. stage0 §B). Правки точечные, остальное тело эталонов не трогать.

---

## card-10-json-schema.md

**§4, find:**
```
сужает поверхность LLM02 Improper Output Handling
```
**replace:**
```
сужает поверхность LLM05 Improper Output Handling
```
Единственное вхождение LLM-тега в карточке. Смысл не меняется (Improper Output Handling), меняется только номер под пином 2025.

**Шапка — добавить строку пина** (после строки «Верификация: …»):
```
> Ось §4: OWASP LLM Top 10 2025 / Agentic Top 10 2026.
```

---

## card-16-ifc-taint.md

**§4 (строка 37), find:**
```
Indirect prompt injection, ведущий к экфильтрации приватных данных (LLM01 → LLM06).
```
**replace:**
```
Indirect prompt injection, ведущий к экфильтрации приватных данных (LLM01 → LLM02; при действии-как-выводе + LLM06 Excessive Agency).
```
Старый «LLM06» = Sensitive Information Disclosure в нумерации-2023; в 2025 это **LLM02**. Действие-как-вывод (переслать) добавляет **LLM06** Excessive Agency.

**Шапка — добавить строку пина** (после строки «Верификация якоря: …»):
```
> Ось §4: OWASP LLM Top 10 2025 / Agentic Top 10 2026.
```

---

После применения обе строки эталонов перестают быть `NEEDS-REPIN` и матрица собирается по ним механически (подтверждено смоук-тестом stage0 §C).
