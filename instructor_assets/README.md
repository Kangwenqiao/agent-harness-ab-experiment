# Instructor Assets

This directory is intentionally outside `baseline_repo/` and `harness_repo/`.

It contains the instructor-only evaluation logic:

- `tests_hidden/`: hidden pytest cases
- `check_layer_rules.py`: static layer check
- `check_visible_test_expansion.py`: verifies that the student expanded visible tests
- `evaluate_submission.py`: one-command evaluator for a student repo

Example:

```bash
baseline_repo/.venv/bin/python instructor_assets/evaluate_submission.py baseline_repo
harness_repo/.venv/bin/python instructor_assets/evaluate_submission.py harness_repo
```
