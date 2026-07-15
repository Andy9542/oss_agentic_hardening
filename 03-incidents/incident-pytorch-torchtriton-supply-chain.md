---
type: incident
date: 2022-12-30
incident-kind: confirmed-supply-chain-incident
status: confirmed-remediated
affected: "PyTorch nightly Linux via pip, December 25–30 2022"
risk-ids:
  - ASI04
  - ASI05
  - LLM03
tags:
  - agent-security
  - incident
  - supply-chain
  - pypi
---

# PyTorch nightly — dependency confusion в torchtriton

## Что произошло

Linux-установки PyTorch nightly через pip с 25 по 30 декабря 2022 года могли получить malicious package torchtriton из PyPI вместо dependency из официального PyTorch index из-за index precedence. При import вредоносный binary собирал environment/system data, читал файлы в HOME и .ssh и отправлял содержимое через encrypted DNS.

## Статус доказательств

PyTorch Foundation подтвердила supply-chain attack, опубликовала hash и индикаторы. Stable packages не были затронуты; binary выполнялся при explicit import triton, а не при любом стандартном запуске PyTorch.

## Связь с рисками

- [[ASI04-agentic-supply-chain]] — dependency resolution подменил компонент ML/agent runtime из другого registry.
- [[ASI05-unexpected-code-execution]] — malicious binary выполнялся внутри developer или workload environment.
- [[LLM03-supply-chain]] — публичный package index и совпадающее имя нарушили provenance dependency.

## Последствия и реакция

PyTorch переименовала dependency, зарезервировала dummy package и удалила затронутые nightlies. Защита: explicit index policy, hashes, lockfiles, signed artifacts и изоляция ML build/runtime.

## Источники

- [PyTorch Foundation: официальный incident notice](https://pytorch.org/blog/compromised-nightly-dependency/)
