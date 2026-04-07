# ARCHITECTURE.md

## Layer responsibilities

- `api`: 解析输入、调用 service、格式化输出
- `services`: 编排流程，不承载领域规则
- `domain`: 用户名标准化与校验规则
- `repositories`: 数据存取

## Hard rules

- 用户名标准化只能在 domain 层定义
- service 和 api 不允许重复实现用户名规则
- 重复用户名判断必须基于标准化后的用户名
- 保留名检查属于领域规则，放在 domain 层
