# Username Onboarding Demo

This repository is a small starter project for an agent coding exercise.

## Task

See `TASK.md`.

## Run checks

```bash
uv sync
bash scripts/run_visible_checks.sh
```

## Experiment Flow

```bash
cd harness_repo
uv sync
bash scripts/run_visible_checks.sh
```

使用同样的简单提示词修复：

```text
请修复注册流程中的用户名规范化问题，并补上必要测试。完成后确保现有测试通过。
```

建议修复前先阅读：

```text
docs/product-specs/new-user-onboarding.md
ARCHITECTURE.md
QUALITY.md
```

## Instructor Note

教师评测不在本仓库内进行。  
请在工作区根目录使用 `instructor_assets/evaluate_submission.py` 对提交结果进行统一评测。

## Notes

- The starter implementation is intentionally incomplete.
- Visible tests are intentionally narrower than the full business rules.
