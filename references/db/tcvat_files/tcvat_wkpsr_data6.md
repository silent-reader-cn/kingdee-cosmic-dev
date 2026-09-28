# 未开票收入台账数据表6-tcvat_wkpsr_data6

## 未开票收入台账数据表6-主表 t_tcvat_wkpsr_data6

- **表名称：** 未开票收入台账数据表6-主表
- **表名：** t_tcvat_wkpsr_data6

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbqsjwkjfpxse | 本期实际未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 本期实际未开具发票销售额 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 4 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 5 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式 |
| 6 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 7 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 8 | fwkjfpxsetzl | 未开具发票销售额调整列 | numeric | 23 | 10 | √ | 0 | 未开具发票销售额调整列 |
| 9 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 10 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 11 | fqcwkjfpxse | 期初未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 期初未开具发票销售额 |
| 12 | fqmwkjfpxseye | 期末未开具发票销售额余额 | numeric | 23 | 10 | √ | 0 | 期末未开具发票销售额余额 |
| 13 | fbqyysbdwkjfpxse | 本期用于申报的未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 本期用于申报的未开具发票销售额 |
| 14 | fykpsr | 已开票收入 | numeric | 23 | 10 | √ | 0 | 已开票收入 |
| 15 | fsl | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 16 | fbqsjsbwkjfpse | 本期实际申报未开具发票税额 | numeric | 23 | 10 | √ | 0 | 本期实际申报未开具发票税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_wkpsr_data6 |  | fid |
| 2 | idx_t_tcvat_wkpsr_data6_fs |  | fsbbid,fewblxh |
