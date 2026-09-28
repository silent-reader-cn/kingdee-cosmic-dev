# 财务报表项目数据-fin_report_item_data

## 财务报表项目数据-主表 t_cfa_three_fin_report

- **表名称：** 财务报表项目数据-主表
- **表名：** t_cfa_three_fin_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famount | 金额 | numeric | 23 | 10 |  | null | 金额 |
| 3 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 4 | fipoorgld | IPO编制组织 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 5 | ffinreportitem | IPO财务报表项目 | int8 | 64 |  | √ | 0 | [财务报表项目 ipo_fin_report_item](../ipobase_files/ipo_fin_report_item.md) |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fsourcetype | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 1 :手工引入 2 :数据同步-旗舰版 3 :数据同步-企业版 |
| 8 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 10 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: 1 :个别报表 2 :合并报表 |
| 11 | fperiod | 期 | int8 | 64 |  | √ | 0 | 期 |
| 12 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 13 | fitemdatatype | 项目数据类型 | varchar | 50 |  | √ | ' ' | 项目数据类型,枚举: entrygrid :年初余额 newyear :期初余额 opening :本期发生额 currentperiod :本年累计 terminal :期末余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfa_three_fin_report |  | fid |
| 2 | idx_fin_report_item_uq |  | fipoorgld,freportdate,ffinreportitem |
