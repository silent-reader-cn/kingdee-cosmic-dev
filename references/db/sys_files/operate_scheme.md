# 操作方案-operate_scheme

## 操作方案-主表 t_bd_secondauthscheme

- **表名称：** 操作方案-主表
- **表名：** t_bd_secondauthscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fauthonce | 本次登录仅认证一次 | bpchar | 1 |  | √ | ' ' | 本次登录仅认证一次 |
| 3 | fformnumber | 业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 |
| 4 | fenable | 启用 | bpchar | 1 |  | √ | ' ' | 启用,枚举: 0 :启用 1 :禁用 |
| 5 | fverifymode | 验证方式 | bpchar | 1 |  | √ | ' ' | 验证方式,枚举: 0 :密码验证 1 :短信验证 |
| 6 | fverifyoperate | 验证操作 | varchar | 250 |  | √ | ' ' | 验证操作 |
| 7 | fbizappid | 应用 | varchar | 50 |  | √ | ' ' | 应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_operate_formnumber |  | fformnumber |
| 2 | pk_bd_secondauthscheme |  | fid |
| 3 | idx_bd_operate_bizappid |  | fbizappid |
