# 应收余额表-ar_balance

## 应收余额表-主表 t_ar_balance

- **表名称：** 应收余额表-主表
- **表名：** t_ar_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocalbusbalance | 期末暂估余额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末暂估余额折本位币 |
| 3 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | flocalreceivableamt | flocalreceivableamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fperiodreceivedamt | 期初未核销收款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初未核销收款余额 |
| 7 | ffinamt | 本期财务发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期财务发生额 |
| 8 | fperiodamt | fperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 10 | freceivedbalanceamt | freceivedbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fperiodfinamt | 期初财务余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初财务余额 |
| 12 | flocalreceivedperiodamt | flocalreceivedperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | freceivedamt | 本期未核销收款发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期未核销收款发生额 |
| 14 | freceivedbalance | 期末未核销收款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末未核销收款余额 |
| 15 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 16 | fperiodbusamt | 期初暂估余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初暂估余额 |
| 17 | flocalperiodbusamt | 期初暂估余额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初暂估余额折本位币 |
| 18 | fstopdate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 19 | flocalperiodreceivedamt | 期初未核销收款余额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初未核销收款余额折本位币 |
| 20 | flocalfinbalance | 期末财务余额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末财务余额折本位币 |
| 21 | festimatedamt | festimatedamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | flocalbalanceamt | flocalbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 24 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 25 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | flocalperiodfinamt | 期初财务余额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初财务余额折本位币 |
| 27 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | ffinbalance | 期末财务余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末财务余额 |
| 29 | freceivableamt | freceivableamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | flocalperiodamt | flocalperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | flocalbusamt | 本期暂估发生额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期暂估发生额折本位币 |
| 32 | flocalfinamt | 本期财务发生额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期财务发生额折本位币 |
| 33 | fbalanceamt | fbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | flocalreceivedbalanceamt | flocalreceivedbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fbusbalance | 期末暂估余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末暂估余额 |
| 36 | flocalreceivedbalance | 期末未核销收款余额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末未核销收款余额折本位币 |
| 37 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fcloseid | 关账序号 | int8 | 64 |  | √ | 0 | 关账序号 |
| 39 | fbusamt | 本期暂估发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期暂估发生额 |
| 40 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 41 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 42 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | flocalestimatedamt | flocalestimatedamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | flocalreceivedamt | 本期未核销收款发生额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期未核销收款发生额折本位币 |
| 45 | freceivedperiodamt | freceivedperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 47 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 48 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_balance_pkey |  | fid |
| 2 | idx_ar_bal_orgcloseid |  | forgid,fcloseid |
| 3 | idx_ar_bal_closeid |  | fcloseid |
