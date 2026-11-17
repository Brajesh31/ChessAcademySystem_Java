# 🛡️ Threat model

## Assets
- Player records in `data.txt`.
- Tournament details in `tournaments.txt`.
- Example credentials in source.
- Integrity and availability of application and data.

## Trust boundaries
1. Terminal input enters the Java process.
2. Credentials are source constants.
3. File operations use the working directory.
4. GitHub hosts source and automation config.

## Threat scenarios
| Threat | Impact | Exposure | Mitigation |
|---|---|---|---|
| Credential disclosure | Account reuse/abuse | Plaintext source | Remove static secrets; hash passwords |
| Data disclosure | Privacy impact | Plaintext files | Synthetic data and filesystem permissions |
| Record tampering | Incorrect data | Files externally editable | Validation, integrity checks, backups |
| Delimiter injection | Corrupt parsing | Unescaped fields | Escaped or structured format |
| Menu input crash | Interrupted use | Unchecked nextInt | Central input parser |
| Accidental deletion | Data loss | No backup | Versioned backups and restore drills |
| Workflow compromise | Supply-chain impact | Third-party actions | Minimal permissions and reviewed action pins |

Qualitative code-inspection assessment, not a formal audit. Revisit after adding accounts, network access, databases or deployment.
