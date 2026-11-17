# 🧪 Testing strategy

## Current state
No Java test framework or test suite was present in the inspected tree. CI compiles the application and checks documentation. Interactive behavior still needs manual verification.

## Manual test matrix
| ID | Scenario | Expected observation |
|---|---|---|
| T-01 | Choose Exit at login | Program closes |
| T-02 | Invalid login menu number | Message and login prompt repeat |
| T-03 | Valid admin credentials | Admin menu appears |
| T-04 | Valid regular credentials | Regular menu appears |
| T-05 | Invalid credentials | Login prompt repeats |
| T-06 | Add player with shaped DOB | Row appended |
| T-07 | Add player with invalid DOB shape | DOB prompt repeats |
| T-08 | Display existing player file | Lines printed |
| T-09 | Search player as admin | First prefix match printed |
| T-10 | Add tournament with shaped date | Row appended |
| T-11 | Search existing tournament | First match printed |
| T-12 | Search absent tournament | Not-found message |
| T-13 | Confirm logout with yes | Login screen returns |
| T-14 | Cancel logout | Current menu remains |
| T-15 | Missing/unreadable record file | Generic I/O message |
| T-16 | Non-numeric menu choice | May expose uncaught input exception |

Use a temporary working directory and synthetic records. Remove test data after verification. Never commit real player details or credentials.

## Future automated tests
Test calendar validation, delimiter escaping, duplicates, search behavior, empty/missing/malformed files, permissions and invalid-input recovery. Extract pure parsing/validation functions before selecting a test framework.

CI compilation is not a substitute for interactive regression tests.
