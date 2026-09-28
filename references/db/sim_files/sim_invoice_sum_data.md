# 销项发票汇总数据-sim_invoice_sum_data

## 销项发票汇总数据-主表 t_sim_invoice_sum_data

- **表名称：** 销项发票汇总数据-主表
- **表名：** t_sim_invoice_sum_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcancelinvoicenum | 作废发票份数 | int8 | 64 |  | √ | 0 | 作废发票份数 |
| 3 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fblueinvoicenum | 蓝字发票份数 | int8 | 64 |  | √ | 0 | 蓝字发票份数 |
| 5 | fblueinvoicetax | 蓝字发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 蓝字发票税额 |
| 6 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 7 | fblueinvoiceamount | 蓝字发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 蓝字发票金额 |
| 8 | fcancelinvoicetax | 作废发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 作废发票税额 |
| 9 | fstatisticstype | 统计类型 | varchar | 8 |  | √ | ' ' | 统计类型,枚举: 0 :全部 1 :普通发票 2 :专用发票 |
| 10 | fdatadate | 数据日期 | timestamp | 0 |  |  | null | 数据日期 |
| 11 | finvoicetax | 发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票税额 |
| 12 | fredinvoicetax | 红字发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 红字发票税额 |
| 13 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 14 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 15 | finvoicenumber | 开票份数 | int8 | 64 |  | √ | 0 | 开票份数 |
| 16 | fredinvoiceamount | 红字发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 红字发票金额 |
| 17 | fredinvoicenum | 红字发票份数 | int8 | 64 |  | √ | 0 | 红字发票份数 |
| 18 | finventorynum | 库存份数 | int8 | 64 |  | √ | 0 | 库存份数 |
| 19 | fcancelinvoiceamount | 作废发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 作废发票金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_invoice_sum_data |  | fid |
| 2 | idx_sim_invoice_sum_data |  | forgfield |
