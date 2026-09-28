# 应付余额表(废弃)-ap_balance

## 应付余额表(废弃)-主表 t_ap_balance

- **表名称：** 应付余额表(废弃)-主表
- **表名：** t_ap_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprepaidbalanceamt | 期末余额（包含预付） | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额（包含预付） |
| 3 | forgid | 应付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ffinamt | 财务发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 财务发生额 |
| 5 | flocalprepaidamt | 预付金额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 预付金额折本币 |
| 6 | fperiodamt | 期初余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额 |
| 7 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 |
| 8 | fsettleamt | 本期结算金额（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 本期结算金额（废弃） |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fstopdate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 12 | fprepaidamt | 预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 预付金额 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | flocalbalanceamt | 期末余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额折本币 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | flocalprepaidperiodamt | 期初余额折本币（包含预付） | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额折本币（包含预付） |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fprepaidperiodamt | 期初余额（包含预付） | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额（包含预付） |
| 20 | flocalsettleamt | 本期结算金额折本币（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 本期结算金额折本币（废弃） |
| 21 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | flocalbusamt | 业务发生额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 业务发生额折本币 |
| 24 | flocalperiodamt | 期初余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初余额折本币 |
| 25 | flocalfinamt | 财务发生额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 财务发生额折本币 |
| 26 | fbalanceamt | 期末余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额 |
| 27 | flocalprepaidbalanceamt | 期末余额折本币（包含预付） | numeric | 23 | 10 | √ | 0.0000000000 | 期末余额折本币（包含预付） |
| 28 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | fbusamt | 业务发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 业务发生额 |
| 30 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 31 | fappname | 应用 | varchar | 5 |  | √ | ' ' | 应用,枚举: ar :应收 ap :应付 |
| 32 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_org_app |  | forgid,fappname,fstopdate |
| 2 | t_ap_balance_pkey |  | fid |
