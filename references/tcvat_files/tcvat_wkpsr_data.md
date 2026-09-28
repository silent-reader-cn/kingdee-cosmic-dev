# 未开票收入台账数据源-tcvat_wkpsr_data

## 未开票收入台账数据源-主表 t_tcvat_wkpsr_data

- **表名称：** 未开票收入台账数据源-主表
- **表名：** t_tcvat_wkpsr_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbqsjwkjfpxse | 本期实际未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 本期实际未开具发票销售额 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fseqno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 7 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式 |
| 8 | fyssr | 应税收入 | numeric | 23 | 10 | √ | 0 | 应税收入 |
| 9 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 10 | fwkjfpxsetzl | 未开具发票销售额调整列 | numeric | 23 | 10 | √ | 0 | 未开具发票销售额调整列 |
| 11 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 12 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 13 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 14 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 15 | fqcwkjfpxse | 期初未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 期初未开具发票销售额 |
| 16 | fqmwkjfpxseye | 期末未开具发票销售额余额 | numeric | 23 | 10 | √ | 0 | 期末未开具发票销售额余额 |
| 17 | fbqyysbdwkjfpxse | 本期用于申报的未开具发票销售额 | numeric | 23 | 10 | √ | 0 | 本期用于申报的未开具发票销售额 |
| 18 | fykpsr | 已开票收入 | numeric | 23 | 10 | √ | 0 | 已开票收入 |
| 19 | fsl | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 20 | fbqsjsbwkjfpse | 本期实际申报未开具发票税额 | numeric | 23 | 10 | √ | 0 | 本期实际申报未开具发票税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_wkpsr_data |  | fid |
| 2 | idx_t_tcvat_wkpsr_data |  | forgid,fskssqq,fskssqz |
