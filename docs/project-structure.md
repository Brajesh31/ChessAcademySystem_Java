# 🗂️ Project structure

## Original repository tree observed
```text
ChessAcademySystem_Java/
├── .github/
│   └── workflows/
│       └── update-readme.yml
├── .idea/
│   ├── .gitignore
│   ├── ChessAcademySystem_Java.iml
│   ├── modules.xml
│   └── vcs.xml
├── README.md
├── chessAcademy.java
├── javaChessAcademy_Pro.drawio.xml
└── javaChessAcademy_Pro2.drawio.png
```

## Original files
| Path | Purpose |
|---|---|
| `chessAcademy.java` | Entire current application |
| `README.md` | Repository landing page |
| `javaChessAcademy_Pro.drawio.xml` | Editable Draw.io diagram |
| `javaChessAcademy_Pro2.drawio.png` | Existing diagram export |
| `.github/workflows/update-readme.yml` | Existing timestamp workflow |
| `.idea/` | IntelliJ project metadata |

## Added directories
| Directory | Purpose |
|---|---|
| `docs/` | Product, technical, security and operations guides |
| `docs/assets/` | SVG diagrams |
| `docs/templates/` | Reusable engineering templates |
| `scripts/` | Repository validators |
| `.github/ISSUE_TEMPLATE/` | Structured issue intake |
| `.github/workflows/` | CI and docs checks |

Runtime `data.txt` and `tournaments.txt` are created in the working directory and ignored by Git. Entry point is `main` in `chessAcademy.java`. Compile with `javac chessAcademy.java`; run with `java chessAcademy`.
