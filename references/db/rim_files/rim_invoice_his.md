# 发票历史-rim_invoice_his

## 发票历史-主表 t_rim_invoice_his

- **表名称：** 发票历史-主表
- **表名：** t_rim_invoice_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdata_table | 表名 | varchar | 36 |  | √ | ' ' | 表名 |
| 3 | ftraceid | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 4 | fnew_value | 修改后 | varchar | 400 |  | √ | ' ' | 修改后 |
| 5 | fold_value | 修改前 | varchar | 400 |  | √ | ' ' | 修改前 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fdata_pk | 主键id | varchar | 50 |  | √ | ' ' | 主键id |
| 9 | foperate_type | 操作类型 | varchar | 2 |  | √ | ' ' | 操作类型,枚举: |
| 10 | ffield_name | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_his2 |  | ftraceid |
| 2 | pk_rim_invoice_his |  | fid |
| 3 | idx_rim_invoice_his |  | fdata_table,fdata_pk |
