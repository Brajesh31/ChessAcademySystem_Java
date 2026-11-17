# 📋 Requirements and use cases

## Functional requirements implemented
| ID | Requirement | Source method |
|---|---|---|
| FR-01 | Show login and exit choices | `main` |
| FR-02 | Match credentials against configured array | `login` |
| FR-03 | Return role after successful match | `login` |
| FR-04 | Display role-specific menu | `displayMenu` |
| FR-05 | Append player fields | `addPlayer` |
| FR-06 | Display player records | `displayPlayers` |
| FR-07 | Search by registration-number prefix | `searchPlayers` |
| FR-08 | Append tournament fields | `addTournament` |
| FR-09 | Display tournament records | `displayTournaments` |
| FR-10 | Search tournament-name prefix | `searchTournaments` |
| FR-11 | Display help | `displayHelp` |
| FR-12 | Confirm logout | `logout` |

## Non-functional assessment
| Area | Current status |
|---|---|
| Portability | Standard Java APIs; minimum JDK not declared |
| Persistence | Local files, working-directory dependent |
| Security | Not production-safe; plaintext source credentials |
| Reliability | Basic I/O catches; input/error paths incomplete |
| Performance | Linear file scans; no benchmark |
| Accessibility | Terminal-only; not evaluated |
| Maintainability | Single class; limited separation |
| Scalability | No concurrent or large-data design/measurement |

## Use cases
### UC-01: Admin adds a player
Admin selects option 1, enters registration number, names, DOB matching DD/MM/YYYY shape, and rating. The program appends a row to `data.txt`. Invalid DOB shape repeats the prompt; I/O failure prints a generic message.

### UC-02: User displays tournaments
Select option 5; the program reads and prints `tournaments.txt`. I/O error produces a generic message.

### UC-03: User searches tournaments
Select option 6 and enter a name. The first row beginning with that name plus comma is printed. If none matches, not-found is printed.

### UC-04: User logs out
Select option 8. Entering `yes` returns to the login screen; another response cancels logout.

## Future non-functional requirements
Validate input, preserve/migrate data, enforce permissions in operations, add tests, and update documentation with behavior changes.
