#!/usr/bin/env python3
"""Generate MOC — Матрица угроз.md for ALL 46 methods (stdout).

Объединяет данные двух исследовательских веток: нечётные способы (№ 1, 3, … 45)
и чётные (№ 2, 4, … 44, 46). Перегенерация:

    python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
"""
from __future__ import annotations

import sys

# Позволяет и запуск как скрипта (python _gen_matrix.py > ...), и импорт
# как единого источника данных матрицы (ROWS / METHODS / RISKS) из
# аналитических модулей. В некоторых средах stdout не поддерживает
# reconfigure — в этом случае перекодировку молча пропускаем.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

METHODS = {
    1: ("01-классификация-инъекций-машинным-обучением", "Покрытие рисков"),
    2: ("02-cot-reasoning-audit", "Покрытие рисков"),
    3: ("03-правила-и-шаблоны-для-выявления-инъекций", "Покрытие рисков"),
    4: ("04-unicode-normalization", "Покрытие рисков"),
    5: ("05-выявление-и-маскирование-персональных-данных", "Покрытие рисков"),
    6: ("06-content-dlp-inspection", "Покрытие рисков"),
    7: ("07-выявление-секретов-в-тексте", "Покрытие рисков"),
    8: ("08-toxicity-moderation", "Покрытие рисков"),
    9: ("09-проверка-фактической-точности-и-галлюцинаций", "Покрытие рисков"),
    10: ("10-json-schema-constrained", "Покрытие рисков"),
    11: ("11-ограничение-токенов-расходов-и-частоты-вызовов", "Покрытие рисков"),
    12: ("12-tool-policies-yaml-rego", "Покрытие рисков"),
    13: ("13-проверка-аргументов-по-json-схеме", "Покрытие рисков"),
    14: ("14-default-deny-allowlists", "Покрытие рисков"),
    15: ("15-правила-последовательности-вызовов-и-потоков-данных", "Покрытие рисков"),
    16: ("16-ifc-capability-taint", "Покрытие рисков"),
    17: ("17-формальная-проверка-политик-и-сужение-привилегий", "Покрытие рисков"),
    18: ("18-rebac-spicedb", "Покрытие рисков"),
    19: ("19-правила-против-инъекций-в-аргументах-инструментов", "Покрытие рисков"),
    20: ("20-ghost-args-strict-typing", "Покрытие рисков"),
    21: ("21-одобрение-опасных-действий-человеком", "Покрытие рисков"),
    22: ("22-kill-switch-circuit-breaker", "Покрытие рисков"),
    23: ("23-единый-прокси-исходящих-запросов-и-защита-от-ssrf", "Покрытие рисков"),
    24: ("24-mcp-gateway-rbac", "Покрытие рисков"),
    25: ("25-контроль-целостности-описаний-инструментов", "Покрытие рисков"),
    26: ("26-tool-poisoning-scan", "Покрытие рисков"),
    27: ("27-статическая-проверка-навыков-и-плагинов", "Покрытие рисков"),
    28: ("28-toxic-flow-analysis", "Покрытие рисков"),
    29: ("29-проверка-зависимостей-ci-и-сценариев-установки", "Покрытие рисков"),
    30: ("30-static-analysis-code", "Покрытие рисков"),
    31: ("31-допуск-артефактов-и-отзыв-по-чёрному-списку", "Покрытие рисков"),
    32: ("32-aibom-inventory", "Покрытие рисков"),
    33: ("33-изоляция-агента-в-микровиртуальных-машинах-и-контейнерах", "Покрытие рисков"),
    34: ("34-os-sandbox-openshell", "Покрытие рисков"),
    35: ("35-уровни-исполнения-и-изоляция-рабочего-каталога", "Покрытие рисков"),
    36: ("36-crypto-agent-identity", "Покрытие рисков"),
    37: ("37-выявление-поведенческих-отклонений", "Покрытие рисков"),
    38: ("38-skill-attribution", "Покрытие рисков"),
    39: ("39-неизменяемый-журнал-с-цепочкой-хешей-и-подписями", "Покрытие рисков"),
    40: ("40-opentelemetry-siem", "Определение"),
    41: ("41-сопоставление-защит-с-требованиями-стандартов", "Покрытие рисков"),
    42: ("42-colang-dialog-rails", "Покрытие рисков"),
    43: ("43-две-модели-с-разделением-доверия-и-карантином", "Покрытие рисков"),
    44: ("44-red-team-regression", "Определение"),
    45: ("45-agentdojo-как-эталонный-набор-испытаний", "Определение"),
    46: ("46-memory-protection", "Покрытие рисков"),
}
METHOD_IDS = list(range(1, 47))

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

DASH = "—"
HIGH = "выс."
MED = "ср."
LOW = "низ."
META = "мета"


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
    file, anchor = METHODS[mid]
    return f"[[{file}#{anchor}\\|{val}]]"


def header_method(mid: int) -> str:
    file, _ = METHODS[mid]
    return f"[[{file}#Определение\\|{mid}]]"


def row(block_id: str, asi: str, llm: str, primary: str, scenario: str, ratings: dict[int, str]) -> tuple:
    vals = [DASH] * len(METHOD_IDS)
    for mid, r in ratings.items():
        vals[METHOD_IDS.index(mid)] = r
    return (asi, llm, primary, scenario, block_id, vals)


ROWS = [
    row("row-asi01-hijack", "ASI01", "LLM01", "ASI01", "Захват цели агента (инъекция в промпт / косвенная)", {1: MED, 2: MED, 3: MED, 15: HIGH, 16: HIGH, 27: MED, 28: HIGH, 42: MED, 43: HIGH, 44: META, 45: META}),
    row("row-asi01-bypass", "ASI01", "LLM01", "ASI01", "↳ обход фильтров (кодирование, Unicode)", {1: MED, 3: MED, 4: LOW, 27: LOW, 44: META, 45: META}),
    row("row-asi06-poison", "ASI06", "LLM01, LLM08", "ASI06", "Отравление памяти и контекста (RAG, долгий диалог)", {1: MED, 2: MED, 3: LOW, 15: HIGH, 27: MED, 43: HIGH, 44: META, 45: META, 46: MED}),
    row("row-llm02-pii", DASH, "LLM02", "LLM02", "↳ утечка персональных данных в тексте", {5: HIGH, 6: HIGH, 16: HIGH, 19: MED, 41: MED, 44: META, 45: META}),
    row("row-llm02-secrets", DASH, "LLM02", "LLM02", "↳ утечка секретов и API-ключей в тексте", {5: MED, 6: MED, 7: HIGH, 19: HIGH, 23: MED, 44: META, 45: META}),
    row("row-llm05-toxic", DASH, "LLM05", "LLM05", "Вредный / токсичный контент", {1: LOW, 3: LOW, 8: MED, 9: MED, 10: MED, 20: MED, 44: META, 45: META}),
    row("row-llm09-halluc", DASH, "LLM09", "LLM09", "↳ галлюцинации (качество ответа, не атака)", {8: MED, 9: MED, 44: META, 45: META}),
    row("row-asi08-loop", "ASI08", "LLM10", "ASI08", "↳ зацикливание агента, исчерпание ресурсов", {11: HIGH, 22: MED, 23: MED, 33: MED, 44: META, 45: META}),
    row("row-asi02-single", "ASI02", "LLM06, LLM07", "ASI02", "Один опасный вызов инструмента", {10: MED, 11: HIGH, 12: HIGH, 13: HIGH, 14: MED, 16: MED, 17: HIGH, 18: MED, 19: HIGH, 20: MED, 21: HIGH, 28: HIGH, 33: HIGH, 34: HIGH, 35: MED, 37: LOW, 43: HIGH, 44: META, 45: META}),
    row("row-asi02-chain", "ASI02, ASI08", "LLM06", "ASI02", "↳ токсичная цепочка вызовов A→B", {12: MED, 15: HIGH, 16: HIGH, 17: MED, 21: MED, 22: MED, 23: HIGH, 27: MED, 28: MED, 37: MED, 43: HIGH, 44: META, 45: META}),
    row("row-asi03-priv", "ASI03", "LLM06", "ASI03", "Эскалация привилегий", {12: HIGH, 17: HIGH, 18: MED, 21: HIGH, 24: MED, 33: HIGH, 35: MED, 36: MED, 43: HIGH, 44: META, 45: META}),
    row("row-asi02-ssrf", "ASI02", DASH, "ASI02", "↳ SSRF и сетевая утечка через tool", {21: HIGH, 24: MED, 33: MED, 34: MED, 43: MED, 44: META, 45: META}),
    row("row-asi04-rugpull", "ASI04", "LLM03, LLM07", "ASI04", "↳ rug-pull, отравление навыка / MCP", {25: MED, 26: HIGH, 27: MED, 28: MED, 31: MED, 32: MED, 44: META, 45: META}),
    row("row-asi04-ci", "ASI04", "LLM03", "ASI04", "↳ вредонос в пакетах и CI", {26: HIGH, 27: MED, 29: MED, 30: MED, 31: MED, 32: MED, 44: META, 45: META}),
    row("row-asi04-train", "ASI04", "LLM04", "ASI04", "Отравление обучения / артефактов модели", {25: MED, 26: MED, 27: MED, 29: MED, 31: MED, 44: META, 45: META, 46: MED}),
    row("row-asi05-sandbox", "ASI05", "LLM06", "ASI05", "Побег из песочницы / неожиданное исполнение", {30: MED, 33: HIGH, 34: HIGH, 35: MED, 44: META, 45: META}),
    row("row-asi07-multi", "ASI07", DASH, "ASI07", "Небезопасная связь между агентами", {15: MED, 17: LOW, 24: MED, 36: HIGH, 41: MED, 43: HIGH, 44: META, 45: META}),
    row("row-asi08-cascade", "ASI08", "LLM10", "ASI08", "Каскадные сбои (цепная реакция)", {11: HIGH, 15: HIGH, 16: MED, 17: HIGH, 21: MED, 22: MED, 23: HIGH, 27: MED, 28: MED, 33: HIGH, 34: HIGH, 37: MED, 43: HIGH, 44: META, 45: META}),
    row("row-asi09-trust", "ASI09", "LLM09", "ASI09", "Обман оператора через доверие к агенту", {1: LOW, 8: MED, 9: MED, 19: HIGH, 21: HIGH, 42: MED, 43: HIGH, 44: META, 45: META}),
    row("row-asi10-rogue", "ASI10", "LLM06", "ASI10", "Скомпрометированный (rogue) агент", {17: HIGH, 18: MED, 22: MED, 33: MED, 36: MED, 37: MED, 38: MED, 39: LOW, 40: LOW, 44: META, 45: META}),
]

# Обратный индекс. Нечётные строки — курированные (перенесены из нечётной ветки),
# чётные выводятся из данных ROWS функцией derive_reverse().
REVERSE_ODD = {
    1: ("ML-классификация инъекций", "01, 06", "01, 05"),
    3: ("Эвристики и regex", "01", "01"),
    5: ("Маскирование ПДн", "—", "02"),
    7: ("Детекция секретов", "—", "02"),
    9: ("Фактчек / галлюцинации", "09", "05, 09"),
    11: ("Лимиты токенов", "02, 08", "10"),
    13: ("Схема JSON", "02", "06, 07"),
    15: ("Правила потоков", "01, 06, 07, 08", "01, 06"),
    17: ("SMT / монотонность", "02, 03, 08, 10", "06"),
    19: ("Инъекции в args", "02", "—"),
    21: ("Человек в контуре", "02, 03, 08, 09", "06"),
    23: ("Прокси и SSRF", "02, 08", "02, 10"),
    25: ("Rug-pull / хеш", "04", "03, 04"),
    27: ("Сканирование навыков", "01, 04, 06", "02, 03, 04, 06"),
    29: ("Пакеты и CI", "04", "03, 04"),
    31: ("Admission / blocklist", "04, 10", "03, 04"),
    33: ("microVM / контейнер", "02, 03, 05, 08", "10"),
    35: ("Кольца / тюрьма каталога", "02, 03, 05", "06"),
    37: ("Поведенческая аномалия", "02, 08, 10", "06"),
    39: ("Цепочка хешей", "10", "—"),
    41: ("Compliance mapping", "все (отчёт)", "все (отчёт)"),
    43: ("Две LLM + карантин", "01, 02, 03, 06, 07, 08, 09", "01, 02, 06"),
    45: ("AgentDojo", "мета", "мета"),
}

EVEN_NAMES = {
    2: "Аудит CoT-рассуждений",
    4: "Unicode-нормализация",
    6: "Content DLP",
    8: "Модерация токсичности",
    10: "JSON-схема аргументов",
    12: "Tool-политики YAML/Rego",
    14: "Default-deny allowlists",
    16: "IFC / capability taint",
    18: "ReBAC (SpiceDB)",
    20: "Ghost args / строгая типизация",
    22: "Kill switch / circuit breaker",
    24: "MCP-шлюз RBAC",
    26: "Скан отравления инструментов",
    28: "Toxic flow analysis",
    30: "Статический анализ кода",
    32: "AIBOM-инвентаризация",
    34: "ОС-песочница (OpenShell)",
    36: "Криптоидентичность агентов",
    38: "Атрибуция навыков",
    40: "OpenTelemetry → SIEM",
    42: "Colang-рельсы диалога",
    44: "Red-team регрессия",
    46: "Защита памяти",
}


def derive_reverse() -> dict[int, tuple[str, str, str]]:
    out = {}
    for mid, name in EVEN_NAMES.items():
        if mid == 44:
            out[mid] = (name, "мета", "мета")
            continue
        asi, llm = set(), set()
        for a, l, _primary, _scenario, _bid, vals in ROWS:
            if vals[METHOD_IDS.index(mid)] in (DASH, META):
                continue
            if a != DASH:
                asi.update(p.strip()[3:] for p in a.split(","))
            if l != DASH:
                llm.update(p.strip()[3:] for p in l.split(","))
        fmt = lambda s: ", ".join(sorted(s)) if s else "—"
        out[mid] = (name, fmt(asi), fmt(llm))
    return out


HEADER = """# Матрица угроз

Насколько **все 46 способов** (нечётные № 1, 3, … 45 и чётные № 2, 4, … 44, **46***) закрывают риски **OWASP ASI Top 10** и **OWASP LLM Top 10**.

Стандарты: [ASI (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [LLM (2025)](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## Как читать

| Колонка      | Смысл                                                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| **ASI**      | Пункт OWASP Top 10 для агентов (`ASI01` … `ASI10`). `—` = для этого сценария в ASI нет отдельного пункта. Клик → `#Пример атаки` в карточке риска. |
| **LLM**      | Пункт OWASP LLM Top 10 (`LLM01` … `LLM10`). `—` = не относится. Клик → `#Пример атаки`. |
| **Сценарий** | Как атака выглядит на практике. Клик → тот же пример атаки. Строки с **↳** — уточнение внутри того же номера OWASP. |
| **1 … 46**   | Способ защиты; оценка силы. Клик по номеру → `#Определение`; клик по оценке → `#Покрытие рисков`. `—` не ссылается. |

В `covers:` у способов — **только** `ASI01`…`ASI10` и `LLM01`…`LLM10`, без собственных кодов vault.

Способы — [[MOC — Нечётные способы]] и [[MOC — Чётные способы]].

## Справочник OWASP ASI (2026)

Источники: [[source-owasp-asi-top10]], [[source-owasp-agentic-2026]].

| Код | English | Русский | Заметка |
|-----|---------|---------|---------|
| ASI01 | Agent Goal Hijack | Захват цели агента | [[ASI01-agent-goal-hijack]] |
| ASI02 | Tool Misuse and Exploitation | Злоупотребление и эксплуатация инструментов | [[ASI02-tool-misuse]] |
| ASI03 | Identity and Privilege Abuse | Злоупотребление идентичностью и привилегиями | [[ASI03-identity-privilege-abuse]] |
| ASI04 | Agentic Supply Chain Vulnerabilities | Уязвимости цепочки поставок агентных систем | [[ASI04-agentic-supply-chain]] |
| ASI05 | Unexpected Code Execution | Неожиданное исполнение кода | [[ASI05-unexpected-code-execution]] |
| ASI06 | Memory and Context Poisoning | Отравление памяти и контекста | [[ASI06-memory-context-poisoning]] |
| ASI07 | Insecure Inter-Agent Communication | Небезопасная связь между агентами | [[ASI07-insecure-inter-agent-communication]] |
| ASI08 | Cascading Failures | Каскадные сбои | [[ASI08-cascading-failures]] |
| ASI09 | Human-Agent Trust Exploitation | Эксплуатация доверия человека к агенту | [[ASI09-human-agent-trust-exploitation]] |
| ASI10 | Rogue Agents | Вредоносные (rogue) агенты | [[ASI10-rogue-agents]] |

## Справочник OWASP LLM (2025)

Источники: [[source-owasp-llm-top10]], [[source-owasp-llm-2025]].

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

## Легенда оценок

| Символ | Значение |
|--------|----------|
| **выс.** | сильное покрытие |
| **ср.** | частичное |
| **низ.** | слабое |
| **—** | не применимо |
| **мета** | способ только измеряет: №44 (red-team CI) и №45 (AgentDojo) |

## Покрытие: риск × способ
"""

FOOTER_TEMPLATE = """
## Зачем несколько строк с одним ASI или LLM

Один пункт OWASP в жизни проявляется **по-разному**. Пример: **ASI04** — и rug-pull навыка, и вредонос в CI; способы №25–31 закрывают их не одинаково. Поэтому в таблице несколько строк с **одним номером** и разными сценариями (↳), а не отдельные выдуманные ID.

Для отчёта аудитору достаточно сказать «покрываем **ASI04**»; для инженера — смотреть нужную строку с ↳.

## ASI и LLM: кто с кем пересекается

**ASI** — риски **агентов** (инструменты, память, цепочки). **LLM** — риски **моделей и текста** (инъекция, утечка, качество). Матрица использует оба, потому что способы затрагивают оба слоя.

| Если важен… | Смотрите в матрице |
|-------------|-------------------|
| Инъекции, захват цели | [[ASI01-agent-goal-hijack]], [[ASI06-memory-context-poisoning]] + [[LLM01-prompt-injection]] |
| Утечка данных | [[LLM02-sensitive-information-disclosure]] (две строки с ↳) |
| Инструменты, SSRF, цепочки | [[ASI02-tool-misuse]] (+ строки с ↳) |
| Привилегии | [[ASI03-identity-privilege-abuse]] |
| Supply chain | [[ASI04-agentic-supply-chain]] + [[LLM03-supply-chain]], [[LLM04-data-model-poisoning]] |
| Песочница | [[ASI05-unexpected-code-execution]] |
| Multi-agent | [[ASI07-insecure-inter-agent-communication]] (слабое покрытие) |
| DoS, каскады | [[ASI08-cascading-failures]] + [[LLM10-unbounded-consumption]] |
| Социальная инженерия через агента | [[ASI09-human-agent-trust-exploitation]] + [[LLM09-misinformation]] |
| Rogue agent | [[ASI10-rogue-agents]] |

**LLM06** (избыточные полномочия) в ASI разбит на ASI02, ASI03, ASI05, ASI10 — у агентов это отдельные механизмы защиты.

**Вне матрицы:** кража весов модели — не runtime-защита агента.

## Обратный индекс: способ → риски OWASP

Нечётные строки — курированная оценка нечётной ветки; чётные выведены из таблицы покрытия.

| № | Способ | ASI | LLM |
|---|--------|-----|-----|
__REVERSE__

## Не угрозы: детекция и GRC

| Способ | Роль |
|--------|------|
| №37 | обнаружение после начала атаки |
| №38 | атрибуция и форензика навыков |
| №39 | аудит и форензика (цепочка хешей) |
| №40 | телеметрия и SIEM — аудит, не барьер |
| №41 | сопоставление с чеклистами (не барьер) |
| №44 | red-team регрессия в CI (мета) |

## Пробелы

- **ASI07** — multi-agent почти не разобран (№36 закрывает частично).
- **ASI10** — нет сильного контроля rogue agent ни в одной из половин.
- Обход кодированием (**ASI01**) — нечётные детекторы дают лишь среднее; №4 (Unicode-нормализация) обязателен как гигиена.
- **LLM04** — poisoning обучения; мало runtime-инструментов.

## Перегенерация

```bash
python _gen_matrix.py > "30-mocs/MOC — Матрица угроз.md"
```

## Связанные документы

- [[MOC — Нечётные способы]]
- [[MOC — Чётные способы]]
- [[MOC — Выводы]]
- [[source-owasp-asi-top10]], [[source-owasp-agentic-2026]] — ASI01…ASI10
- [[source-owasp-llm-top10]], [[source-owasp-llm-2025]] — LLM01…LLM10
- `05-risks/` — карточки рисков с примерами атак
- `30-mocs/Правила связей.md`
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

    reverse = dict(REVERSE_ODD)
    reverse.update(derive_reverse())
    rev_lines = [f"| {mid} | {name} | {asi} | {llm} |" for mid, (name, asi, llm) in sorted(reverse.items())]
    lines.append(FOOTER_TEMPLATE.replace("__REVERSE__", "\n".join(rev_lines)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
