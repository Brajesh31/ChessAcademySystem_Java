# 📖 Glossary and FAQ

| Term | Meaning |
|---|---|
| Admin | Configured account with role string `admin` |
| Regular user | Configured account with role string `regular` |
| Player record | Comma-separated line in `data.txt` |
| Tournament record | Comma-separated line in `tournaments.txt` |
| Working directory | Directory where relative file paths resolve |
| Append mode | Add content after existing file contents |
| Prefix search | Match starts with entered value plus comma |

**Does this use MySQL?** No, local text files.

**Is it a web application?** No, it runs in a terminal.

**Can regular users add players?** No.

**Can regular users search players?** The menu does not expose this; help text is inconsistent.

**Are passwords secure?** No, example passwords are plaintext in source.

**Are real dates validated?** No, only DD/MM/YYYY shape.

**Where are records stored?** Relative to the process working directory.

**Are there Java unit tests?** None were present in the inspected tree.
