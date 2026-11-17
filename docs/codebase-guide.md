# 🧑‍💻 Codebase and method reference

## Source
`chessAcademy.java` declares public class `chessAcademy`. It imports Java I/O and Scanner.

## Credential table
`USER_CREDENTIALS` rows contain username, plaintext password and role. Demonstration-only; unsuitable for real accounts.

## Method reference
| Method | Inputs | Effect |
|---|---|---|
| `main(String[])` | Unused arguments | Login loop and Scanner lifecycle |
| `login(Scanner)` | Shared scanner | Returns role after match |
| `displayMenu(Scanner,String)` | Scanner and role | Menu rendering and dispatch |
| `addPlayer(Scanner)` | Scanner | Appends to `data.txt` |
| `displayPlayers()` | None | Reads player file |
| `searchPlayers(Scanner)` | Scanner | Registration-number prefix search |
| `addTournament(Scanner)` | Scanner | Appends tournament file |
| `displayTournaments()` | None | Reads tournament file |
| `searchTournaments(Scanner)` | Scanner | Name prefix search |
| `displayHelp(String)` | Role | Role-dependent help |
| `logout(Scanner)` | Scanner | Returns confirmation result |

## Notes
- `FileWriter(file, true)` enables append.
- `BufferedWriter.newLine()` separates records.
- `BufferedReader.readLine()` reads records.
- Search stops at first prefix match.
- DOB regex checks shape, not calendar validity.
- Scanner mixes `nextInt()` and `nextLine()`.

Potential future classes: Player, Tournament, repositories, authentication service, console controller. Introduce with tested behavior, not empty scaffolding.
