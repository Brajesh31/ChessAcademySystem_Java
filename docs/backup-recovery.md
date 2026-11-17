# 💾 Backup and recovery

The application implements no backup or restore function.

## Files to protect
- `data.txt` (player records)
- `tournaments.txt` (tournament records)

## Manual procedure
1. Stop the application before copying files.
2. Copy data to a protected location with restricted access.
3. Record backup time and application commit.
4. Maintain multiple recovery points if data matters operationally.
5. Restore into a separate working directory.
6. Compare record counts and inspect synthetic entries.
7. Protect backups to the same standard as originals.

No RTO or RPO is defined.
