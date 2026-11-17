# 🧰 Maintenance and technical debt

## Routine
- Compile after Java changes.
- Run documentation and structure validators.
- Review GitHub Actions failures.
- Review dependency advisories if dependencies are introduced.
- Keep README, data format, architecture and security docs synchronized.
- Review issues and roadmap.
- Keep runtime data out of commits.

## Technical debt
| ID | Debt | Impact | Priority |
|---|---|---|---|
| TD-01 | One class owns UI, logic and persistence | Hard to test/extend | High |
| TD-02 | Plaintext source credentials | Credential exposure | Critical before real use |
| TD-03 | No delimiter escaping | Data corruption | High |
| TD-04 | Date shape only | Invalid calendar dates | Medium |
| TD-05 | Inconsistent menu input handling | Runtime interruption | High |
| TD-06 | Help/menu mismatch | User confusion | Medium |
| TD-07 | No Java unit tests | Regression risk | High |
| TD-08 | No update/delete, backup or audit | Limited operations | Medium |

For record format or credential changes, document migration and retain recoverable copies.
