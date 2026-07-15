---
type: incident
date: 2025-07-23
incident-kind: confirmed-supply-chain-incident
status: malicious-code-distributed-not-executed
affected: "Amazon Q Developer VS Code extension 1.84.0"
risk-ids:
  - ASI04
  - ASI05
  - LLM03
tags:
  - agent-security
  - incident
  - supply-chain
  - coding-agent
---

# Amazon Q Developer — malicious code в VS Code extension 1.84.0

## Что произошло

Из-за избыточно scoped GitHub token в CodeBuild threat actor смог внести malicious code в open-source repository Amazon Q Developer. Код автоматически попал в VS Code extension 1.84.0 и был распространён через release channels.

## Статус доказательств

AWS подтвердила compromise и дистрибуцию, но установила, что payload не выполнился из-за syntax error и не изменил customer environments. Поэтому это подтверждённый supply-chain incident без успешного customer-side execution.

## Связь с рисками

- [[ASI04-agentic-supply-chain]] — скомпрометирован CI credential и pipeline доверенного coding-agent extension.
- [[ASI05-unexpected-code-execution]] — вредоносный код был рассчитан на выполнение команд в developer environment, хотя конкретный payload сломался.
- [[LLM03-supply-chain]] — официальный marketplace release не соответствовал ожидаемому trusted source path.

## Последствия и реакция

AWS отозвала credentials, удалила код, сняла 1.84.0 с распространения и выпустила 1.85.0. Кейс показывает необходимость least-privilege CI tokens, protected release workflows, artifact signing и проверки опубликованного extension.

## Источники

- [AWS Security Bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/)
- [GitHub Advisory GHSA-7g7f-ff96-5gcw](https://github.com/aws/aws-toolkit-vscode/security/advisories/GHSA-7g7f-ff96-5gcw)
