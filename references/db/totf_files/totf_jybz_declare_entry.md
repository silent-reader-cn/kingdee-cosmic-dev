# 残疾人就业保障金申报子表-totf_jybz_declare_entry

## 残疾人就业保障金申报子表-主表 t_totf_jybz_declare

- **表名称：** 残疾人就业保障金申报子表-主表
- **表名：** t_totf_jybz_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 2 | fdeclaredate | 申报编制日期 | timestamp | 0 |  |  | null | 申报编制日期 |
| 3 | fismodified | fismodified | varchar | 50 |  | √ | ' ' |  |
| 4 | fqjje | 欠缴金额 | numeric | 23 | 10 | √ | 0 | 欠缴金额 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fsjje | 本期已缴费额 | numeric | 23 | 10 | √ | 0 | 本期已缴费额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbqdybtse | 本期应补（退）税额 | numeric | 23 | 10 | √ | 0 | 本期应补（退）税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_jybz_declare |  | fentryid |
| 2 | idx_totf_jybz_declare_fk |  | fid |
