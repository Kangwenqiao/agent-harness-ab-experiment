# QUALITY.md

## Acceptance

- 现有 visible tests 必须通过
- 新增测试要覆盖：
  1. 前后空格 + 大小写混合输入
  2. 保留名
  3. 标准化后重复用户名
- 不允许为了过测试删除已有测试
- 不允许把规则写死在测试里

## Preferred change shape

- 生产代码改动不超过 3 个文件
- 尽量复用已有函数
- 不要在多个层重复写 regex 或 `strip`/`lower` 逻辑
