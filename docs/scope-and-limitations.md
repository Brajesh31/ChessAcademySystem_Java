# 🎯 Scope and limitations

## In scope now
- Terminal login loop with two hard-coded example roles.
- Role-specific menu rendering.
- Player creation, listing and admin-only search.
- Tournament creation, listing and search.
- Append-only local text persistence.
- Help and logout confirmation.

## Not implemented
- Online/multi-device operation or database.
- Web, GUI, or mobile interface.
- Coaches, lessons, attendance, fees and student enrollment.
- Tournament registration, rounds, pairings, scoring or results.
- Account creation, password reset, audit trail or backups.
- Import/export beyond plain text files.

## Technical constraints
- UI, role checks, validation and persistence are coupled.
- File paths are relative to working directory.
- Commas are not escaped; date validation checks shape only.
- Search is linear and prefix-based.
- Missing files produce generic I/O errors.
- Invalid numeric menu input may cause an uncaught exception.

Roadmap proposals are not current product claims.
