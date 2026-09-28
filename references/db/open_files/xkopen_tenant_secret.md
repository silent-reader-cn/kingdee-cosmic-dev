# 租户秘钥-xkopen_tenant_secret

## 租户秘钥-主表 t_open_gatetenantkey

- **表名称：** 租户秘钥-主表
- **表名：** t_open_gatetenantkey

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_secret | 租户秘钥 | varchar | 255 |  | √ | ' ' | 租户秘钥 |
| 3 | fenv | fenv | varchar | 10 |  | √ | ' ' |  |
| 4 | ftenantid | 租户id | varchar | 255 |  | √ | ' ' | 租户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_gatetenantkey |  | ftenantid |
| 2 | pk_t_open_gatetenantkey |  | fid |
