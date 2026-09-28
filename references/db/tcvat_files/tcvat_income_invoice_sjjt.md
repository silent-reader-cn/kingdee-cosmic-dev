# 一般纳税人计提收入台账开票收入明细-tcvat_income_invoice_sjjt

## 一般纳税人计提收入台账开票收入明细-主表 t_tcvat_income_invoice_jt

- **表名称：** 一般纳税人计提收入台账开票收入明细-主表
- **表名：** t_tcvat_income_invoice_jt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 50 |  | √ | ' ' | 所属月份 |
| 3 | ftaxamount | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 8 | ftaxaccountserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 9 | fconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 10 | ffiltercondition | 过滤条件设置 | varchar | 255 |  | √ | ' ' | 过滤条件设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_income_invoice_jt |  | fid |
| 2 | idx_income_invoice_serialno |  | ftaxaccountserialno |
