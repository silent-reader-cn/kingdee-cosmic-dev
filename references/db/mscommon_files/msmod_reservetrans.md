# 预留转移记录-msmod_reservetrans

## 预留转移记录-主表 t_msmod_reservetrans

- **表名称：** 预留转移记录-主表
- **表名：** t_msmod_reservetrans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fafrecordid | 转移后预留记录ID | int8 | 64 |  | √ | 0 | 转移后预留记录ID |
| 4 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 5 | ftranstype | 转移类型 | varchar | 50 |  | √ | ' ' | 转移类型,枚举: trans :预留转移 replace :预留替换 |
| 6 | ftransbill | 单据实体 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 9 | fbfrecordid | 转移前预留记录ID | int8 | 64 |  | √ | 0 | 转移前预留记录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_reservetrans_id |  | fbillid |
| 2 | pk_t_msmod_reservetrans |  | fid |
