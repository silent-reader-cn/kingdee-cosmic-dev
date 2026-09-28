# 预留释放记录-reserve_releaserecord

## 预留释放记录-主表 t_reserve_releaserecord

- **表名称：** 预留释放记录-主表
- **表名：** t_reserve_releaserecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_base_qty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 3 | f_release_type | 释放类型 | varchar | 30 |  | √ | ' ' | 释放类型,枚举: release :出库释放 remove :预留解除 manualremove :手工释放 mrprelease :MRP释放 expirerelease :到期释放 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fbill_id | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 6 | fop | 操作 | varchar | 20 |  | √ | ' ' | 操作 |
| 7 | f_reserve_record_id | 预留记录ID | int8 | 64 |  | √ | 0 | 预留记录ID |
| 8 | fbill_obj | 单据实体 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 9 | f_creater_id | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbillno | 单据编码 | varchar | 128 |  | √ | ' ' | 单据编码 |
| 11 | fcreate_date | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fbill_entry_id | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_releaserecord |  | fid |
| 2 | idx_reserve_releasercd_eid |  | fbill_entry_id |
