---
type: repo-catalog
catalog-id: 111
method-id: 33
also-method-ids:
  - 7
  - 21
  - 23
  - 35
repo: https://github.com/h5i-dev/h5i
language: Rust
license: Apache-2.0
verdict: experimental
tags:
  - agent-security
  - repo-catalog
  - review-2026
clusters:
  - cluster-sandbox-isolation
  - cluster-os-isolation
  - cluster-governance-platform
  - cluster-egress-proxy-dlp
  - cluster-artifact-trust
---

# h5i-dev/h5i — каталог №111

## Репозиторий

- [h5i-dev/h5i](https://github.com/h5i-dev/h5i)
- Проверенный срез: [`c33cf7308169b95b6e68464e74b693bde7b60b9d`](https://github.com/h5i-dev/h5i/commit/c33cf7308169b95b6e68464e74b693bde7b60b9d), 2026-07-15.
- Лицензия: [Apache-2.0](https://github.com/h5i-dev/h5i/blob/c33cf7308169b95b6e68464e74b693bde7b60b9d/LICENSE).

## Слой и тип

| Поле | Значение |
|------|----------|
| Слой | 4 |
| Тип | Sandbox и governance runtime |
| Семейства | [[cluster-sandbox-isolation]], [[cluster-os-isolation]], [[cluster-governance-platform]], [[cluster-egress-proxy-dlp]], [[cluster-artifact-trust]] |

## Принцип работы

Rust CLI создаёт Git-addressed environments для агентов, выбирает наиболее сильный доступный isolation tier, фиксирует policy и evidence в `refs/h5i/*`, брокерит secrets и проводит human/peer review перед явным apply.

## Алгоритм

Environment объединяет code branch/worktree, context ref и pinned policy manifest. Capability probe выбирает `container > supervised > process > workspace` и отказывает при невозможности выполнить заявленную изоляцию. Process tier применяет Landlock, seccomp, user/network namespaces и rlimits; container tier использует rootless Podman. Orchestra журналирует submissions, reviews и durable gates. Основной механизм — **способ №33**; дополнительно реализуются способы №7, №21, №23 и №35.

## Вариант в семействе

h5i сочетает containment с Git-native provenance и multi-agent review. Уровень `workspace` изолирует изменения через worktree, но не является OS security boundary; domain egress allowlist поддерживается только там, где backend способен её enforce.

## Детерминизм или машинное обучение

Выбор tier, policy validation, confinement, secret brokering, Git refs, journals и apply gates детерминированы. Код, summaries и reviews создаются внешними LLM-агентами.

## Вердикт

**экспериментально** — амбициозная fail-closed архитектура с подробными tests и evidence model, но молодой проект, сложная Linux/Podman surface и неодинаковая сила tiers требуют независимого threat-model review.

## Детальные разборы

- [[impl-h5i]]
- [[h5i-secrets-broker]]
- [[h5i-durable-human-gate]]

## Реализуемые способы

- [[33-изоляция-агента-в-микровиртуальных-машинах-и-контейнерах]] — основной
- [[07-выявление-секретов-в-тексте]]
- [[21-одобрение-опасных-действий-человеком]]
- [[23-единый-прокси-исходящих-запросов-и-защита-от-ssrf]]
- [[35-уровни-исполнения-и-изоляция-рабочего-каталога]]
