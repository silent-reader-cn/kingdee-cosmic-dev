# 需求运算记录-mrp_reqcalc_record

## 需求运算记录-主表 t_mrp_reqcalc_record

- **表名称：** 需求运算记录-主表
- **表名：** t_mrp_reqcalc_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | f_billentry_id | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 3 | f_bill_no | 需求单据编号 | varchar | 100 |  | √ | ' ' | 需求单据编号 |
| 4 | f_bill_obj_id | 需求单据实体 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 5 | flast_runtime | 最后运算时间 | timestamp | 0 |  |  | null | 最后运算时间 |
| 6 | flast_runlogno | 最后计划运算号 | varchar | 100 |  | √ | ' ' | 最后计划运算号 |
| 7 | f_billentry_seq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 8 | f_bill_id | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_reqcalc_record |  | fid |
| 2 | idx_mrp_reqcalc_record_b |  | f_bill_no |
| 3 | idx_mrp_reqcalc_record_g |  | flast_runlogno |
| 4 | idx_mrp_reqcalc_record_beid |  | f_billentry_id |
| 5 | idx_mrp_reqcalc_record_bid |  | f_bill_id |
