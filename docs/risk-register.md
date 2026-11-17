# ⚠️ Project risk register

| ID | Risk | Impact | Priority | Mitigation |
|---|---|---|---|---|
| R-01 | Plaintext credentials in source | Credential exposure | Critical | Remove before real use; rotate reused credentials |
| R-02 | Plaintext player records | Privacy exposure | High | Synthetic data, permissions, retention |
| R-03 | Unescaped delimiter characters | Corrupt records | High | Structured format and parser tests |
| R-04 | Unchecked menu numeric input | Unexpected exit | High | Central safe input parser |
| R-05 | No backup/recovery function | Permanent data loss | High | Backup and restore verification |
| R-06 | No Java unit tests | Undetected regressions | High | Extract testable domain logic |
| R-07 | Menu/help mismatch | Incorrect guidance | Medium | Synchronize menu and help |

Qualitative initial assessment from code inspection, not a formal audit.
