# Harness A/B 实验流程

## 目标

验证在相同模型、相同提示词、相同时间限制下：

- `baseline_repo/` 是否更容易只修表面问题
- `harness_repo/` 是否更容易依据仓库内规范文件完成更完整、更符合约束的修复

本实验的唯一设计差异应为：

- `baseline_repo/` 只有任务、源码、visible tests
- `harness_repo/` 在相同源码基础上，额外提供：
  - `AGENTS.md`
  - `ARCHITECTURE.md`
  - `QUALITY.md`
  - `docs/product-specs/new-user-onboarding.md`

教师专用评测资产不下发给学生，统一放在：

- `instructor_assets/`

## 目录说明

学生可见：

- `baseline_repo/`
- `harness_repo/`

教师专用，不对学生开放：

- `instructor_assets/`
- `TEACHER_GUIDE.md`
- 本文件 `EXPERIMENT_FLOW.md`

## 实验前准备

1. 确认学生只能拿到单个 repo。
2. 不要把 `instructor_assets/` 发给学生。
3. 两组使用相同模型配置。
4. 两组使用相同提示词。
5. 两组使用相同时间限制。
6. 每轮实验前，确保两个 repo 都回到同一个“未修复”初始状态。

## 推荐实验配置

- 模型：同一模型，同一 reasoning 级别
- 时间限制：15 到 25 分钟
- 允许工具：相同
- 初始提示词：完全一致

推荐提示词：

```text
请修复注册流程中的用户名规范化问题，并补上必要测试。完成后确保现有测试通过。
```

## 学生侧流程

### A 组：baseline

学生只拿到：

- `baseline_repo/`

操作流程：

```bash
cd baseline_repo
uv sync
bash scripts/run_visible_checks.sh
```

把上面的 visible failure 作为起点交给模型。

学生对模型输入：

```text
请修复注册流程中的用户名规范化问题，并补上必要测试。完成后确保现有测试通过。
```

学生完成修复后，只允许再次运行：

```bash
bash scripts/run_visible_checks.sh
```

学生提交内容：

1. 最终代码改动
2. visible tests 通过证据
3. 一段简短说明

### B 组：harness

学生只拿到：

- `harness_repo/`

操作流程：

```bash
cd harness_repo
uv sync
bash scripts/run_visible_checks.sh
```

学生对模型输入同样的提示词：

```text
请修复注册流程中的用户名规范化问题，并补上必要测试。完成后确保现有测试通过。
```

但允许学生或模型阅读仓库内的 harness 文件：

- `AGENTS.md`
- `ARCHITECTURE.md`
- `QUALITY.md`
- `docs/product-specs/new-user-onboarding.md`

学生完成修复后，只允许再次运行：

```bash
bash scripts/run_visible_checks.sh
```

学生提交内容：

1. 最终代码改动
2. visible tests 通过证据
3. 一段简短说明

## 教师侧评测流程

教师始终在工作区根目录执行，不进入学生仓库内部做 hidden 评测。

### 评测 baseline 提交

```bash
baseline_repo/.venv/bin/python instructor_assets/evaluate_submission.py baseline_repo
```

### 评测 harness 提交

```bash
harness_repo/.venv/bin/python instructor_assets/evaluate_submission.py harness_repo
```

这一个命令会统一完成：

1. visible tests
2. hidden tests
3. static layer check
4. visible test expansion check

## 评测维度

自动评分总分：16

- Visible tests：4
- Hidden tests：6
- Architecture check：4
- Visible test expansion：2

人工评分总分：4

- Change quality：2
- Delivery explanation：2

总分：20

## 建议记录方式

每组至少记录以下内容：

1. 初始 visible 失败输出
2. 学生最终 patch
3. 学生最终说明
4. 教师评测输出
5. 最终总分

建议记录模板：

```text
组别：
仓库：
模型：
reasoning：
开始时间：
结束时间：

初始 visible 结果：

最终提交说明：

教师评测结果：
- Visible tests:
- Hidden tests:
- Architecture check:
- Visible test expansion:
- Manual review:

最终结论：
```

## 公平性要求

必须保证：

1. 两组提示词完全相同
2. 两组模型完全相同
3. 两组时间限制完全相同
4. 两组起始代码完全相同
5. 只有 `harness_repo/` 多出规范文件
6. 学生都不能看到 `instructor_assets/`

## 严禁事项

以下行为会破坏实验：

1. 把 `tests_hidden/` 发给学生
2. 把评分脚本发给学生
3. 允许 baseline 组读取教师专用目录
4. 两组使用不同提示词
5. 两组使用不同模型
6. 在实验中途手工提示某一组隐藏规则

## 推荐观察指标

除了最终分数，建议重点比较：

1. 是否一次通过 hidden checks
2. 是否补了足够的 visible tests
3. 是否把规则写进错误层级
4. 修改的生产代码文件数
5. 是否出现“为了过测试硬编码”的行为
6. 最终说明是否能解释为什么这样改

## 当前实验的预期现象

修复前：

- `baseline_repo/` visible tests 失败
- `harness_repo/` visible tests 失败

修复后，理想情况下：

- `baseline_repo/` 更容易出现：
  - 只修 visible bug
  - 没补足测试
  - 规则放错层
  - hidden 或 architecture check 丢分
- `harness_repo/` 更容易出现：
  - 补全 canonical username 规则
  - 新增符合要求的 visible tests
  - 把规则放在 domain 层
  - hidden 和 score 表现更完整

## 一轮最小实验示例

### baseline

```bash
cd baseline_repo
uv sync
bash scripts/run_visible_checks.sh
```

把同一个提示词交给模型修复。

教师评测：

```bash
cd ..
baseline_repo/.venv/bin/python instructor_assets/evaluate_submission.py baseline_repo
```

### harness

```bash
cd harness_repo
uv sync
bash scripts/run_visible_checks.sh
```

把同一个提示词交给模型修复。

教师评测：

```bash
cd ..
harness_repo/.venv/bin/python instructor_assets/evaluate_submission.py harness_repo
```

## 实验后复盘建议

复盘时不要只看“最终是否修好”，而要看：

1. 是不是一次修好
2. 补测试是否主动且充分
3. 是否遵守分层约束
4. harness 文档是否被实际利用
5. 两组 patch 的质量差异是否清晰
