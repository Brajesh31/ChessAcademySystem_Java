# ⚡ Performance considerations

Display and search scan each file sequentially. For N records, these operations are O(N). Search returns the first prefix match and has no index. Appends use append-mode file writing.

No benchmarks, workload limits, cache, or concurrency design are available. Large files increase scan time. Measure representative data before optimizing; do not add a database or caching layer without a demonstrated requirement.
