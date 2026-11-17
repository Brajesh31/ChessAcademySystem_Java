# 🛠️ Installation and local development

## Prerequisites
Install a JDK with `javac` and `java`:
```bash
java -version
javac -version
```

## Clone, compile and run
```bash
git clone https://github.com/Brajesh31/ChessAcademySystem_Java.git
cd ChessAcademySystem_Java
javac -Xlint:all chessAcademy.java
java chessAcademy
```

## Working directory
The program resolves data files relative to the current working directory. Run in a writable directory and check IDE run configuration.

## Development loop
1. Inspect method and callers.
2. Define behavior and edge cases.
3. Make focused change.
4. Compile and exercise changed paths with synthetic data.
5. Run validators.
6. Update docs and diagrams.
7. Open focused PR.

No Maven or Gradle config exists.
