# 🛣️ Roadmap

These are proposals based on the current single-file console application, not implemented features or commitments.

## 🎯 Priority 1: correctness and safety
- [ ] Handle invalid menu input consistently.
- [ ] Align regular-user help with available actions.
- [ ] Validate calendar dates, ratings and required fields.
- [ ] Handle missing and malformed data files predictably.
- [ ] Define escaping for delimiter characters.
- [ ] Add automated tests for parsing, validation, search and access.
- [ ] Remove hard-coded plaintext credentials before real use.

## 🧱 Priority 2: maintainable design
- [ ] Extract Player and Tournament model classes.
- [ ] Separate console I/O from business logic.
- [ ] Introduce storage abstractions with tests.
- [ ] Add safe update/delete operations.
- [ ] Prevent duplicate registration identifiers.
- [ ] Add backup/export and restore verification.

## ♟️ Priority 3: academy workflows
- [ ] Specify requirements for tournament participation.
- [ ] Add rounds, pairings and results only after domain rules are agreed.
- [ ] Evaluate database storage only if shared usage requires it.
- [ ] Consider GUI/web interface with explicit deployment design.

Prioritize credential security, data integrity, recoverable storage and testability before feature breadth.
