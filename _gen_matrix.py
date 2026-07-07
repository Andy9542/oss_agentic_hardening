#!/usr/bin/env python3
"""Generate MOC — Матрица угроз.md for even methods (stdout)."""
from __future__ import annotations

import sys

sys.stdout.reconfigure(encoding="utf-8")

METHODS = {
    2: ("02-cot-reasoning-audit", "Покрытие рисков"),
    4: ("04-unicode-normalization", "Покрытие рисков"),
    6: ("06-content-dlp-inspection", "Покрытие рисков"),
    8: ("08-toxicity-moderation", "Покрытие рисков"),
    10: ("10-json-schema-constrained", "Покрытие рисков"),
    12: ("12-tool-policies-yaml-rego", "Покрытие рисков"),
    14: ("14-default-deny-allowlists", "Покрытие рисков"),
    16: ("16-ifc-capability-taint", "Покрытие рисков"),
    18: ("18-rebac-spicedb", "Покрытие рисков"),
    20: ("20-ghost-args-strict-typing", "Покрытие рисков"),
    22: ("22-kill-switch-circuit-breaker", "Покрытие рисков"),
    24: ("24-mcp-gateway-rbac", "Покрытие рисков"),
    26: ("26-tool-poisoning-scan", "Покрытие рисков"),
    28: ("28-toxic-flow-analysis", "Покрытие рисков"),
    30: ("30-static-analysis-code", "Покрытие рисков"),
    32: ("32-aibom-inventory", "Покрытие рисков"),
    34: ("34-os-sandbox-openshell", "Покрытие рисков"),
    36: ("36-crypto-agent-identity", "Покрытие рисков"),
    38: ("38-skill-attribution", "Покрытие рисков"),
    40: ("40-opentelemetry-siem", "Определение"),
    42: ("42-colang-dialog-rails", "Покрытие рисков"),
    44: ("44-red-team-regression", "Определение"),
    46: ("46-memory-protection", "Покрытие рисков"),
}
METHOD_IDS = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46]

RISKS = {
    "ASI01": "ASI01-agent-goal-hijack",
    "ASI02": "ASI02-tool-misuse",
    "ASI03": "ASI03-identity-privilege-abuse",
    "ASI04": "ASI04-agentic-supply-chain",
    "ASI05": "ASI05-unexpected-code-execution",
    "ASI06": "ASI06-memory-context-poisoning",
    "ASI07": "ASI07-insecure-inter-agent-communication",
    "ASI08": "ASI08-cascading-failures",
    "ASI09": "ASI09-human-agent-trust-exploitation",
    "ASI10": "ASI10-rogue-agents",
    "LLM01": "LLM01-prompt-injection",
    "LLM02": "LLM02-sensitive-information-disclosure",
    "LLM03": "LLM03-supply-chain",
    "LLM04": "LLM04-data-model-poisoning",
    "LLM05": "LLM05-improper-output-handling",
    "LLM06": "LLM06-excessive-agency",
    "LLM07": "LLM07-system-prompt-leakage",
    "LLM08": "LLM08-vector-embedding-weaknesses",
    "LLM09": "LLM09-misinformation",
    "LLM10": "LLM10-unbounded-consumption",
}

DASH = "\u2014"
HIGH = "\u0432\u044b\u0441."
MED = "\u0441\u0440."
LOW = "\u043d\u0438\u0437."
META = "\u043c\u0435\u0442\u0430"


def risk_link(code: str) -> str:
    return f"[[{RISKS[code]}#Пример атаки\\|{code}]]"


def codes_cell(val: str) -> str:
    if val == DASH:
        return DASH
    parts = [p.strip() for p in val.split(",")]
    return ", ".join(risk_link(p) for p in parts)


def scenario_link(primary: str, text: str) -> str:
    note = RISKS[primary]
    return f"[[{note}#Пример атаки\\|{text}]]"


def rating_cell(mid: int, val: str) -> str:
    val = val.strip()
    if val == DASH:
        return DASH
    if val == META:
        file, anchor = METHODS[44]
        return f"[[{file}#{anchor}\\|{META}]]"
    file, anchor = METHODS[mid]
    return f"[[{file}#{anchor}\\|{val}]]"


def header_method(mid: int) -> str:
    file, _ = METHODS[mid]
    return f"[[{file}#Определение\\|{mid}]]"


def blank() -> list[str]:
    return [DASH] * len(METHOD_IDS)


def row(block_id: str, asi: str, llm: str, primary: str, scenario: str, ratings: dict[int, str]) -> tuple:
    vals = blank()
    for mid, r in ratings.items():
        vals[METHOD_IDS.index(mid)] = r
    return (asi, llm, primary, scenario, block_id, vals)


ROWS = [
    row("row-asi01-hijack", "ASI01", "LLM01", "ASI01", "Захват цели агента (инъекция в промпт / косвенная)", {2: MED, 16: HIGH, 28: HIGH, 42: MED, 44: META}),
    row("row-asi01-bypass", "ASI01", "LLM01", "ASI01", "↳ обход фильтров (кодирование, Unicode)", {4: LOW, 44: META}),
    row("row-asi06-poison", "ASI06", "LLM01, LLM08", "ASI06", "Отравление памяти и контекста (RAG, долгий диалог)", {2: MED, 46: HIGH, 44: META}),
    row("row-llm02-pii", DASH, "LLM02", "LLM02", "↳ утечка персональных данных в тексте", {6: HIGH, 16: HIGH, 44: META}),
    row("row-llm02-secrets", DASH, "LLM02", "LLM02", "↳ утечка секретов и API-ключей в тексте", {6: MED, 44: META}),
    row("row-llm05-toxic", DASH, "LLM05", "LLM05", "Вредный / токсичный контент", {8: MED, 10: MED, 20: MED, 44: META}),
    row("row-llm09-halluc", DASH, "LLM09", "LLM09", "↳ галлюцинации (качество ответа, не атака)", {8: MED, 44: META}),
    row("row-asi08-loop", "ASI08", "LLM10", "ASI08", "↳ зацикливание агента, исчерпание ресурсов", {22: HIGH, 44: META}),
    row("row-asi02-single", "ASI02", "LLM06, LLM07", "ASI02", "Один опасный вызов инструмента", {10: MED, 12: HIGH, 14: HIGH, 16: MED, 18: MED, 20: HIGH, 44: META}),
    row("row-asi02-chain", "ASI02, ASI08", "LLM06", "ASI02", "↳ токсичная цепочка вызовов A→B", {12: MED, 16: HIGH, 22: MED, 28: HIGH, 44: META}),
    row("row-asi03-priv", "ASI03", "LLM06", "ASI03", "Эскалация привилегий", {12: HIGH, 18: HIGH, 24: MED, 36: MED, 44: META}),
    row("row-asi02-ssrf", "ASI02", DASH, "ASI02", "↳ SSRF и сетевая утечка через tool", {24: HIGH, 34: MED, 44: META}),
    row("row-asi04-rugpull", "ASI04", "LLM03, LLM07", "ASI04", "↳ rug-pull, отравление навыка / MCP", {26: HIGH, 28: MED, 32: HIGH, 44: META}),
    row("row-asi04-ci", "ASI04", "LLM03", "ASI04", "↳ вредонос в пакетах и CI", {26: HIGH, 30: MED, 32: MED, 44: META}),
    row("row-asi04-train", "ASI04", "LLM04", "ASI04", "Отравление обучения / артефактов модели", {26: MED, 46: MED, 44: META}),
    row("row-asi05-sandbox", "ASI05", "LLM06", "ASI05", "Побег из песочницы / неожиданное исполнение", {30: MED, 34: HIGH, 44: META}),
    row("row-asi07-multi", "ASI07", DASH, "ASI07", "Небезопасная связь между агентами", {24: MED, 36: MED, 44: META}),
    row("row-asi08-cascade", "ASI08", "LLM10", "ASI08", "Каскадные сбои (цепная реакция)", {16: MED, 22: HIGH, 28: MED, 34: MED, 44: META}),
    row("row-asi09-trust", "ASI09", "LLM09", "ASI09", "Обман оператора через доверие к агенту", {8: MED, 42: MED, 44: META}),
    row("row-asi10-rogue", "ASI10", "LLM06", "ASI10", "Скомпрометированный (rogue) агент", {18: MED, 22: MED, 36: MED, 38: MED, 40: LOW, 44: META}),
]

HEADER = f"""# Матрица угроз

Насколько **чётные** способы (№ 2, 4, 6 … 44, **46***) закрывают риски **OWASP ASI Top 10** и **OWASP LLM Top 10**.

Стандарты: [ASI (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [LLM (2025)](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## Как читать

| Колонка | Смысл |
| ------- | ----- |
| **ASI** | Пункт OWASP Top 10 для агентов. `—` = нет отдельного пункта. |
| **LLM** | Пункт OWASP LLM Top 10. |
| **Сценарий** | Как атака выглядит на практике. **↳** — уточнение. |
| **2 … 46** | Чётный способ; оценка силы. `мета` = тестовый/измеритель (№44). |

Способы — [[MOC — Чётные способы]].

## Покрытие: риск × способ

"""

FOOTER = """
## Зачем несколько строк на один код OWASP

Один код (например ASI02) покрывает разные **сценарии** атаки. Матрица оценивает способ по сценарию, не только по коду.

## Перегенерация

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```
"""


def main() -> None:
    header_cols = ["ASI", "LLM", "Сценарий"] + [header_method(m) for m in METHOD_IDS]
    lines = [
        HEADER,
        "| " + " | ".join(header_cols) + " |",
        "| " + " | ".join(["---"] * len(header_cols)) + " |",
    ]
    for asi, llm, primary, scenario, block_id, ratings in ROWS:
        assert len(ratings) == len(METHOD_IDS), (block_id, len(ratings))
        cols = [codes_cell(asi), codes_cell(llm), scenario_link(primary, scenario)]
        cols.extend(rating_cell(mid, r) for mid, r in zip(METHOD_IDS, ratings))
        lines.append("| " + " | ".join(cols) + f" ^matrix-{block_id} |")
    lines.append(FOOTER)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
