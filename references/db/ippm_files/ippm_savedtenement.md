# 租户是否已保存-ippm_savedtenement

## 租户是否已保存-主表 t_ippm_savedtenement

- **表名称：** 租户是否已保存-主表
- **表名：** t_ippm_savedtenement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 50 |  | √ | ' ' | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fissaved | 是否已保存 | bpchar | 1 |  | √ | '0' | 是否已保存 |
| 4 | ftenementid | 租户id | varchar | 50 |  | √ | ' ' | 租户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_savedtenement |  | fid |
| 2 | idx_t_ippm_savedtenement_fid |  | fid |
