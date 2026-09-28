# 预留释放记录-msmod_release_record

## 预留释放记录-主表 t_msmod_release_record

- **表名称：** 预留释放记录-主表
- **表名：** t_msmod_release_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_base_qty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 3 | f_release_type | 释放类型 | varchar | 36 |  | √ | ' ' | 释放类型,枚举: release :出库释放 remove :预留解除 |
| 4 | fbill_id | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 5 | fop | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 6 | f_qty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 7 | f_reserve_record_id | 预留记录ID | int8 | 64 |  | √ | 0 | 预留记录ID |
| 8 | fbill_obj | 单据实体 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 9 | f_creater_id | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | f_qty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 11 | fcreate_date | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fbill_entry_id | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msmod_release_record |  | fid |
| 2 | idx_fbill_entry_id |  | fbill_entry_id |
| 3 | idx_msmod_release_rd_f_rerdid |  | f_reserve_record_id |
| 4 | idx_fbill_id |  | fbill_id |
