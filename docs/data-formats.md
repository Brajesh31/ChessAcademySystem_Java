# 🗃️ Data formats and persistence

The program uses two append-only local text files, relative to the process working directory.

## Player record
`registrationNumber,firstName,lastName,dateOfBirth,rating`

The prompt requests DD/MM/YYYY. Rating is accepted as text.

## Tournament record
`name,date,location`

Date is checked against DD/MM/YYYY shape.

## Integrity limitations
- Fields are not quoted or escaped.
- Newlines are not explicitly rejected.
- No schema version or uniqueness constraint exists.
- Malformed rows are printed as-is.
- Date shape is not calendar validation.
- No atomic transaction spans files.

Use synthetic records only. Back up files before manual edits. A future format change must provide migration and compatibility tests.
