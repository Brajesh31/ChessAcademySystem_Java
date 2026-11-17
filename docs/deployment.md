# 🚀 Build and deployment

## Current deployment
Local Java console application. No server, web host, container, database server, or production environment configuration is present.

## Build and run
```bash
javac -Xlint:all chessAcademy.java
java chessAcademy
```

## Operations
- Choose a controlled working directory.
- Back up both data files before upgrades.
- Do not run concurrent instances against shared files without locking.
- Keep runtime data out of Git.
- Test restores in a separate directory.

CI compiles source and validates documentation. It does not deploy a production service or publish a release artifact.

Future packaging/hosting requires explicit configuration, authentication, storage, migration, monitoring and recovery requirements.
