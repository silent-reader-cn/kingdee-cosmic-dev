# 税金分布历史记录表-tctrc_taxation_record

## 税金分布历史记录表-主表 t_tctrc_taxation_record

- **表名称：** 税金分布历史记录表-主表
- **表名：** t_tctrc_taxation_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsbbid | 关联id | int8 | 64 |  | √ | 0 | 关联id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_trtrc_taxr_sbbid |  | fsbbid |
| 2 | pk_tctrc_taxation_record |  | fid |

---

## 单据体-子表 t_tctrc_taxati_record_djt

- **表名称：** 单据体-子表
- **表名：** t_tctrc_taxati_record_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | friskexpression | friskexpression | varchar | 50 |  | √ | ' ' |  |
| 3 | friskpoint | friskpoint | varchar | 50 |  | √ | ' ' |  |
| 4 | ftextfield6 | ftextfield6 | varchar | 50 |  | √ | ' ' |  |
| 5 | ftaxtypename | 税种 | varchar | 50 |  | √ | ' ' | 税种 |
| 6 | friskresult | friskresult | varchar | 50 |  | √ | ' ' |  |
| 7 | fratio | 占比 | varchar | 50 |  | √ | ' ' | 占比 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fskssqq | fskssqq | varchar | 50 |  | √ | ' ' |  |
| 10 | friskdes | friskdes | varchar | 50 |  | √ | ' ' |  |
| 11 | fbqybtse | 税金 | numeric | 23 | 10 | √ | 0 | 税金 |
| 12 | friskname | friskname | varchar | 50 |  | √ | ' ' |  |
| 13 | frisklevel | frisklevel | varchar | 50 |  | √ | ' ' |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_taxati_record_djt |  | fentryid |
| 2 | idx_tctrc_taxati_record_djt_fk |  | fid |
