# 🔐 Security Policy

## Supported versions
There is no published release or formal supported-version matrix. Fixes should target the default branch unless a maintainer identifies another supported line.

## Current security posture
Credentials are hard-coded in plaintext in Java source and player/tournament records are plaintext local files. There is no password hashing, credential rotation, lockout, encryption, account provisioning, audit trail, or network API. Role checks exist inside one process. Delimiter characters are not escaped.

Do not use real credentials or sensitive player information with this implementation.

## Reporting
Do not publish exploitable details in a public issue. Contact the repository owner privately using profile contact information. Include impact, affected file/commit, safe reproduction steps, and suggested mitigation. Do not include passwords or real player data.

## Disclosure
The maintainer will investigate reports as practical, coordinate remediation, and communicate guidance. No formal response-time commitment is currently offered.

## Contributor expectations
- Never commit secrets or real personal data.
- Use synthetic fixtures.
- Treat all input as untrusted.
- Review dependencies and minimize workflow permissions.
- Pin third-party actions to reviewed versions or immutable SHAs where practical.
- Rotate leaked credentials; deleting a secret from a later commit does not revoke it.

## Incident response
Invalidate exposed credentials first, assess affected data and history, restrict access, restore trusted versions where appropriate, and notify affected parties when required.
