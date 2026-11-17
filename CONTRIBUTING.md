# 🤝 Contributing Guide

Contributions should improve the actual Java console application or supporting documentation without overstating features.

## Before starting
1. Read [README](README.md), [Code of Conduct](CODE_OF_CONDUCT.md), and [Security Policy](SECURITY.md).
2. Search existing issues and pull requests.
3. For substantial work, open an issue with the problem, proposed approach, impact, and compatibility considerations.
4. Keep changes focused.

## Setup
Requirements: JDK with `javac` and `java`, Git, terminal.

```bash
git clone https://github.com/Brajesh31/ChessAcademySystem_Java.git
cd ChessAcademySystem_Java
javac chessAcademy.java
java chessAcademy
```

No build tool or third-party dependency manager is configured.

## Branches and commits
Use focused branch names such as `feat/player-validation`, `fix/menu-input-recovery`, `docs/data-format-guide`, and `test/player-search`. Use imperative commit messages with prefixes `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `build:`, or `chore:`.

## Java coding guidance
- Keep methods focused and use standard Java naming.
- Avoid credentials or personal data in source.
- Use try-with-resources for file operations.
- Validate input and report actionable errors.
- Avoid silently swallowing exceptions.
- Consider compatibility before changing persisted formats.
- Separate business logic from console interaction as the codebase grows.

## Data and security
Use synthetic records. Never commit real player data, passwords, tokens, private keys, or runtime records. Credential changes must explain storage, hashing, migration, and failure behavior.

## Documentation and verification
Update docs whenever behavior, formats, commands, limitations, or architecture change. Diagrams must match implementation.

```bash
javac -Xlint:all chessAcademy.java
python3 scripts/validate_docs.py
python3 scripts/validate_repo.py
```

## Pull request checklist
- [ ] Clear issue or documented need.
- [ ] Existing functionality and assets preserved.
- [ ] Java compilation succeeds if source changed.
- [ ] Input, file I/O and error paths considered.
- [ ] Documentation and diagrams match code.
- [ ] No secrets or real personal data committed.
- [ ] Validation scripts pass.
- [ ] Limitations and follow-up work disclosed.

Maintainers may request focused revisions, tests, or clearer documentation. A PR is ready when its purpose is clear and relevant checks have run.
