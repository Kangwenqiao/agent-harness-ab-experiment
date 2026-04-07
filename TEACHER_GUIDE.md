# Teacher Guide

## Student-facing repos

- `baseline_repo/`: visible task, visible tests, source code
- `harness_repo/`: same starter code plus `AGENTS.md`, `ARCHITECTURE.md`, `QUALITY.md`, and product specs

Students should only receive one of these repos.
Do not distribute `instructor_assets/`.

## Student workflow

For either repo:

```bash
uv sync
bash scripts/run_visible_checks.sh
```

Prompt:

```text
请修复注册流程中的用户名规范化问题，并补上必要测试。完成后确保现有测试通过。
```

## Instructor workflow

After the student submits a patch, run exactly one evaluation command from the workspace root:

```bash
baseline_repo/.venv/bin/python instructor_assets/evaluate_submission.py baseline_repo
harness_repo/.venv/bin/python instructor_assets/evaluate_submission.py harness_repo
```

That command runs:

1. visible tests in the student repo
2. hidden tests stored outside the student repo
3. static layer checks
4. visible-test-expansion checks

## Why this layout is experimental-safe

- Students cannot read hidden tests from inside their repo.
- Students cannot read the scoring script from inside their repo.
- The only intended difference between baseline and harness remains the extra guidance files in `harness_repo/`.
