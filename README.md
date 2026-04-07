# Agent Harness A/B Demo

This workspace contains a ready-to-teach A/B experiment for comparing a single task prompt against a file-based agent harness.

## Layout

- `baseline_repo/`: starter repo for group A
- `harness_repo/`: starter repo for group B

Both repos contain the same buggy Python implementation and the same task prompt. The only difference is that `harness_repo/` includes:

- `AGENTS.md`
- `ARCHITECTURE.md`
- `QUALITY.md`
- `docs/product-specs/new-user-onboarding.md`

## Suggested classroom flow

1. Give group A `baseline_repo/`
2. Give group B `harness_repo/`
3. Use the same model, tool, time limit, and task prompt for both groups
4. Ask students to submit a patch, test evidence, and a short explanation

## Teacher usage

Each repo includes:

- `tests/`: visible tests
- `tests_hidden/`: hidden tests for instructors
- `scripts/check_layer_rules.py`: static architecture check
- `scripts/score_submission.py`: automated rubric for the testable parts

Example:

```bash
cd harness_repo
python3 -m pip install pytest
python scripts/score_submission.py
```

If you want to hide the hidden tests before class, remove or relocate `tests_hidden/` and keep `scripts/run_hidden_checks.sh` for instructor use only.
