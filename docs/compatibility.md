# 🌐 Compatibility

## Java
The source has no declared minimum JDK. CI uses Java 17 for compilation, a validation choice rather than a declared minimum.

## Operating systems
The application uses standard Java input and relative file I/O. OS/terminal combinations have not been exhaustively tested.

## Character encoding
FileReader and FileWriter use the runtime default charset in the current source. A future change should define UTF-8 explicitly and consider migration of existing files.
