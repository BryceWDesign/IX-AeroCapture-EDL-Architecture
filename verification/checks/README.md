# Verification Checks

Checks are intentionally simple and dependency-light.

Current checks:
- `check_result_against_ranges.py`
  - verifies required keys exist
  - verifies required substrings exist (for scaffold cases)
  - verifies numeric ranges when specified

Range format:
- If a metric is `null` in `expected_ranges.json`, it is not checked.
- Otherwise, provide:
  - `{ "min": <number>, "max": <number> }`
