# 🏗️ Architecture

## Style
Single-process, single-class procedural console program. UI, domain rules, role checks and persistence remain coupled.

## Runtime components
| Component | Responsibility | Boundary |
|---|---|---|
| Console entry | Login/exit loop | Standard input/output |
| Credential table | Example accounts and roles | In-memory constant |
| Menu dispatcher | Role menu and action dispatch | Static methods |
| Player operations | Append, list and search | `data.txt` |
| Tournament operations | Append, list and search | `tournaments.txt` |
| Help/logout | Display help and return to login | Console |

## Context diagram
```mermaid
flowchart LR
 U[Admin / regular user] -->|input| APP[Java console process]
 APP -->|output| U
 C[In-source credentials] --> APP
 APP -->|read / append| P[(data.txt)]
 APP -->|read / append| T[(tournaments.txt)]
```

## Data flow
```mermaid
flowchart TD
 A[Terminal input] --> B[Method-level checks]
 B --> C{Operation}
 C -->|Add player| D[Build player row]
 C -->|Add tournament| E[Build tournament row]
 C -->|Display or search| F[Read file]
 D --> P[(data.txt)]
 E --> T[(tournaments.txt)]
 F --> O[Console output]
 P --> O
 T --> O
```

## Trust boundaries
The process trusts local input, source-controlled credentials, working directory, and local text files. No network boundary, encrypted store or backend exists.

Do not describe this as microservices, client-server, layered, or database-backed architecture. Introduce future abstractions only with real behavior and tests.
