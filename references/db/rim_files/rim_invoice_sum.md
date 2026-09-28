# 数据汇总-rim_invoice_sum

## 数据汇总-主表 t_rim_invoice_sum

- **表名称：** 数据汇总-主表
- **表名：** t_rim_invoice_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsum_count | 总份数 | int4 | 32 |  | √ | 0 | 总份数 |
| 3 | ftotal_amount | 总价税额 | numeric | 23 | 10 | √ | 0.0000000000 | 总价税额 |
| 4 | finput_invoice_type | 发票类型 | varchar | 50 |  | √ | ' ' | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 5 | fdata_date_time | 数据日期 | timestamp | 0 |  |  | null | 数据日期 |
| 6 | famount | 总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 总金额 |
| 7 | fcertified_count | 已认证份数 | int4 | 32 |  | √ | 0 | 已认证份数 |
| 8 | forg | 数据所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | freceived_count | 已到票份数 | int4 | 32 |  | √ | 0 | 已到票份数 |
| 11 | funreceive_count | 未到票份数 | int4 | 32 |  | √ | 0 | 未到票份数 |
| 12 | funcertified_count | 未认证份数 | int4 | 32 |  | √ | 0 | 未认证份数 |
| 13 | ftax_amount | 总税额 | numeric | 23 | 10 | √ | 0.0000000000 | 总税额 |
| 14 | fcreate_date | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_sum |  | fcreate_date |
| 2 | pk_rim_invoice_sum |  | fid |
