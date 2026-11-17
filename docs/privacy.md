# 🕊️ Privacy and data handling

## Fields collected
Player creation asks for registration number, first/last name, date of birth and rating. Tournament creation asks for name, date and location.

## Storage and transmission
The Java source writes records to local plaintext files. No network transmission, cloud storage, analytics or cookie handling appears in the inspected implementation.

## Data minimization
Use synthetic data for demonstrations. Do not store real personal information without a defined purpose, appropriate notice, access controls, lawful basis and retention process.

## Retention and deletion
There is no built-in retention, export, correction or deletion workflow. Removing a line from a file does not remove copies in backups or Git history.

A GUI, shared database, cloud deployment or real academy data requires a fresh privacy assessment. This page is not a compliance certification.
