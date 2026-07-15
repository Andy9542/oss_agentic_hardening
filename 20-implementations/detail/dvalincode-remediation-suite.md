---
type: implementation-detail
parent-repo: repo-106-dvalincode
method-id: 30
repo: https://github.com/arthurpanhku/dvalincode
language: TypeScript
license: MIT
verdict: экспериментально
commit-sha: d47516748f2acfc75111ca150ca2eda607187f82
commit-date: 2026-07-15
verified-date: 2026-07-15
tags:
  - agent-security
---

# DvalinCode — scanner-gated remediation

## Проверенная ревизия

`d47516748f2acfc75111ca150ca2eda607187f82`, дата коммита 2026-07-15; код проверен 2026-07-15.

## Где в коде

- Код: `src/remediation/scannerSuite.ts`, `src/remediation/localScan.ts`, `src/remediation/sarif.ts`, `src/remediation/automate.ts`, `src/remediation/worktree.ts`, `src/tools/runSecuritySuite.ts`.
- Тесты: `tests/remediationScannerSuite.test.ts`, `tests/remediationLocalScan.test.ts`, `tests/remediationSarif.test.ts`, `tests/remediationWorktree.test.ts`, `tests/remediationCases.test.ts`.

## Алгоритм

1. Suite запускает встроенные статические проверки и выбранные внешние engines: Semgrep, Trivy и OSV-Scanner; готовый SARIF нормализуется в общую модель finding.
2. Findings получают source, rule id, severity, путь и строку, после чего вычисляются score и grade.
3. Исправление выполняется в отдельной Git worktree и обязано воспроизвести finding, внести минимальное изменение и добавить целевой regression test.
4. Независимый verification prompt проверяет полный diff, тесты и повторный scan.
5. Gate пропускает результат только при исчезновении исходных findings, отсутствии новых high/critical findings, наличии изменений и точного маркера успешной проверки.

## Зависимости

Встроенный scanner работает в Bun/TypeScript runtime. Semgrep CE, Trivy, OSV-Scanner и Git опциональны; отсутствие внешнего engine возвращается как `missing`, а не как ошибка всего suite.

## Ограничения

Статический анализ ограничен доступными rulesets и поддерживаемыми manifests. Verification marker поступает из вывода LLM-агента и надёжен только вместе с фактическими результатами повторного scan. Нулевая выдача отсутствующего scanner не является доказательством безопасности.

## Вердикт

**экспериментально** — самостоятельный механизм способа №30 с воспроизводимым re-scan gate, но полнота зависит от внешних scanners и корректности агентного исправления.

## Связи

- Репозиторий: [[repo-106-dvalincode]]
