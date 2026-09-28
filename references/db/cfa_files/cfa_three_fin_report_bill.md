# 公司三大财务报表-cfa_three_fin_report_bill

## 公司三大财务报表-主表 t_cfa_three_fin_report

- **表名称：** 公司三大财务报表-主表
- **表名：** t_cfa_three_fin_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 3 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 4 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 5 | ffinreportitem | IPO财务报表项目 | int8 | 64 |  | √ | 0 | [财务报表项目 ipo_fin_report_item](../ipobase_files/ipo_fin_report_item.md) |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fsourcetype | fsourcetype | varchar | 50 |  | √ | ' ' |  |
| 8 | fcreater | fcreater | int8 | 64 |  | √ | 0 |  |
| 9 | fyear | fyear | int8 | 64 |  | √ | 0 |  |
| 10 | freporttype | freporttype | varchar | 50 |  | √ | ' ' |  |
| 11 | fperiod | fperiod | int8 | 64 |  | √ | 0 |  |
| 12 | fcycle | fcycle | varchar | 50 |  | √ | ' ' |  |
| 13 | fitemdatatype | fitemdatatype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_three_fin_report |  | fid |
| 2 | idx_fin_report_item_uq |  | fipoorgld,freportdate,ffinreportitem |
