# Agent Harness A/B Demo

This workspace contains a ready-to-teach A/B experiment for comparing a single task prompt against a file-based agent harness.

## Layout

- `baseline_repo/`: starter repo for group A
- `harness_repo/`: starter repo for group B
- `instructor_assets/`: hidden tests and scoring logic for instructors only
- `TEACHER_GUIDE.md`: recommended experiment workflow

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

Instructor-only assets now live outside the student repos.

Use:

```bash
baseline_repo/.venv/bin/python instructor_assets/evaluate_submission.py baseline_repo
harness_repo/.venv/bin/python instructor_assets/evaluate_submission.py harness_repo
```

See `TEACHER_GUIDE.md` for the full experiment flow.
