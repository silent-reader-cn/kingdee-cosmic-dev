# 未开票收入台账列表数据表-tcvat_wkpsr_listentry

## 未开票收入台账列表数据表-主表 t_tcvat_wkpsr_listentry

- **表名称：** 未开票收入台账列表数据表-主表
- **表名：** t_tcvat_wkpsr_listentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbqyysbdwkjfpxsehj | 本期用于申报的未开具发票销售额合计 | numeric | 23 | 10 | √ | 0 | 本期用于申报的未开具发票销售额合计 |
| 2 | fid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 3 | fyssrhj | 应税收入合计 | numeric | 23 | 10 | √ | 0 | 应税收入合计 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 5 | fwkjfpxsetzlhj | 未开具发票销售额调整列合计 | numeric | 23 | 10 | √ | 0 | 未开具发票销售额调整列合计 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 8 | fbqsjsbwkjfpsehj | 本期实际申报未开具发票税额合计 | numeric | 23 | 10 | √ | 0 | 本期实际申报未开具发票税额合计 |
| 9 | fqcwkjfpxsehj | 期初未开具发票销售额合计 | numeric | 23 | 10 | √ | 0 | 期初未开具发票销售额合计 |
| 10 | fqmwkjfpxseyehj | 期末未开具发票销售额余额合计 | numeric | 23 | 10 | √ | 0 | 期末未开具发票销售额余额合计 |
| 11 | fbqsjwkjfpxsehj | 本期实际未开具发票销售额合计 | numeric | 23 | 10 | √ | 0 | 本期实际未开具发票销售额合计 |
| 12 | fbqyysbdwkjfpxselms | 本期用于申报的未开具发票销售额列描述 | varchar | 50 |  | √ | ' ' | 本期用于申报的未开具发票销售额列描述 |
| 13 | fykpsrhj | 已开票收入合计 | numeric | 23 | 10 | √ | 0 | 已开票收入合计 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_wkpsr_listentry |  | fentryid |
| 2 | idx_tcvat_wkpsr_listentry_fk |  | fid |
