---
type: repo-catalog
catalog-id: 112
method-id: 14
also-method-ids:
  - 11
  - 21
  - 23
repo: https://github.com/onecli/onecli
language: TypeScript/Rust
license: Apache-2.0
verdict: experimental
upstream-sha: 32b5852b
upstream-date: 2026-07-12
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-tool-firewall-pdp
  - cluster-egress-proxy-dlp
---

# onecli/onecli — каталог №112

## Репозиторий

[onecli/onecli](https://github.com/onecli/onecli)

Проверенная ревизия: `32b5852b` от 2026-07-12.

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 3 + 4 |
| Тип | Архитектурный, детерминированный |
| Семейства | [[cluster-tool-firewall-pdp]], [[cluster-egress-proxy-dlp]] |

## Принцип работы

OneCLI ставит HTTP(S)-шлюз между агентом и внешними API. Агент использует placeholder и собственный access token, а шлюз после проверки scoped permissions подставляет расшифрованный секрет непосредственно перед исходящим запросом.

## Алгоритм

1. Оператор сохраняет credential в зашифрованном хранилище и задаёт разрешённые операции.
2. Агент направляет запрос через gateway и аутентифицируется своим токеном.
3. Gateway сопоставляет метод, host, path и операцию с политикой; deny mode закрывает отсутствующие разрешения.
4. Дополнительные решения включают бюджет, rate limit и ручное одобрение.
5. После разрешения placeholder заменяется реальным credential, затем запрос уходит во внешний API.

Основной механизм — **способ №14**; дополнительно реализуются способы №11, №21 и №23.

## Вариант в семействе

Credential broker совмещён с PDP и egress proxy. В отличие от обычного API gateway, секрет не выдаётся агенту; в отличие от самостоятельного vault, решение принимается на каждом исходящем запросе.

## Вердикт

**experimental** — архитектура уменьшает доступ агента к секретам, но граница работает только при принудительном egress через gateway, включённом deny mode и проверенной изоляции хранилища.

## Детальные разборы

- [[impl-onecli]]
- [[impl-onecli-approval]]
- [[impl-onecli-rate-budget]]
- [[impl-onecli-egress-gateway]]

## Реализуемые способы

- [[14-default-deny-allowlists]] — основной
- [[11-ограничение-токенов-расходов-и-частоты-вызовов]]
- [[21-одобрение-опасных-действий-человеком]]
- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
