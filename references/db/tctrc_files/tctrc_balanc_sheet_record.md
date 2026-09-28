# 资产负债表关键数据历史记录表-tctrc_balanc_sheet_record

## 单据体-子表 t_tctrc_sheet_record_djt

- **表名称：** 单据体-子表
- **表名：** t_tctrc_sheet_record_djt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbqybtse1 | 金额 | varchar | 50 |  | √ | ' ' | 金额 |
| 3 | fbqybtse0 | 金额 | varchar | 50 |  | √ | ' ' | 金额 |
| 4 | fbqybtse2 | 金额 | varchar | 50 |  | √ | ' ' | 金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fproject | 项目 | varchar | 300 |  | √ | ' ' | 项目 |
| 7 | fyearonyear2 | 同比变动 | varchar | 50 |  | √ | ' ' | 同比变动 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fyearonyear1 | 同比变动 | varchar | 50 |  | √ | ' ' | 同比变动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_sheet_record_djt |  | fentryid |
| 2 | idx_tctrc_sheet_record_djt_fk |  | fid |

---

## 资产负债表关键数据历史记录表-主表 t_tctrc_bala_sheet_record

- **表名称：** 资产负债表关键数据历史记录表-主表
- **表名：** t_tctrc_bala_sheet_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyearthree | 第三年 | varchar | 50 |  | √ | ' ' | 第三年 |
| 3 | fyeartwo | 第二年 | varchar | 50 |  | √ | ' ' | 第二年 |
| 4 | fsbbid | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 5 | fyearone | 第一年 | varchar | 50 |  | √ | ' ' | 第一年 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_balasr_sbbid |  | fsbbid |
| 2 | pk_tctrc_bala_sheet_record |  | fid |
