# 🎯 Product overview

## Purpose
A small Java terminal application demonstrating role-aware menu navigation and local record storage for player records and tournament listings.

## Intended users
- **Administrator:** adds player and tournament records and can search players.
- **Regular user:** displays players and tournaments and searches tournament records.
- **Learner/reviewer:** studies Java loops, branching, console input, and basic file I/O.

These are application-level example roles, not independently managed accounts.

## Current value
The program demonstrates login-to-menu flow and append-only persistence without third-party dependencies.

## Product boundaries
No chess lessons, coaches, attendance, fees, participant enrollment, tournament pairings, results, rankings, online accounts, or multi-user service are implemented.

## Current record types
| Record | Fields | File |
|---|---|---|
| Player | Registration number, first name, last name, DOB, rating | `data.txt` |
| Tournament | Name, date, location | `tournaments.txt` |

## Success criteria
- Compiles with a compatible JDK.
- Configured credentials reach the appropriate menu.
- Records can be appended and read.
- Search returns a first prefix match or not-found message.
- Documentation accurately reflects limitations.
