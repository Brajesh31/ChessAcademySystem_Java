# 🔐 Security overview

## Current posture
Credentials are hard-coded in plaintext in source. Records are plaintext local files. There is no hashing, encryption, account provisioning, lockout, audit log, or network API. Role checks execute inside one process. Delimiters are not escaped.

## Risk and improvement matrix
| Concern | Current state | Improvement |
|---|---|---|
| Authentication | Plaintext static credentials | Secure configuration and password hashing |
| Authorization | Menu/dispatcher checks | Enforce permissions inside protected operations |
| Data confidentiality | Plaintext files | Restrict filesystem access; assess encryption |
| Input validation | DOB shape only | Validate all values and real dates |
| Integrity | Append-only rows | Structured parsing, duplicate checks, backups |
| Auditability | No audit log | Define minimal privacy-aware event trail |
| Secret handling | Source-controlled examples | Remove and rotate before real deployment |

## Secure development
Never commit real data or secrets. Use synthetic fixtures. Validate and normalize input. Define escaping. Restrict file permissions. Keep tested backups. Avoid sensitive logging. Review dependencies and CI permissions.

Do not present roadmap controls as implemented controls.
