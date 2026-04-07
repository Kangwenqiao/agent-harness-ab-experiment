# New User Onboarding

## Username policy

注册时用户名会被标准化：

- trim whitespace
- lowercase

标准化后的用户名必须满足：

- 长度 3-20
- 仅允许 a-z, 0-9, underscore

以下名称保留，不可注册：

- admin
- root
- system

重复用户名判断以标准化后的结果为准。

例如：

- ` Alice `
- `alice`
- `ALICE`

这三者应视为同一个用户名。
