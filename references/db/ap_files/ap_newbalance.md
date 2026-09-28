# 应付余额表-ap_newbalance

## 应付余额表-主表 t_ap_newbalance

- **表名称：** 应付余额表-主表
- **表名：** t_ap_newbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprepaidbalanceamt | fprepaidbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | flocalprepaidamt | 本期未核销付款发生额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期未核销付款发生额折本币 |
| 5 | ffinamt | 本期财务发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期财务发生额 |
| 6 | flocalperiodprepaidamt | 期初未核销付款余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初未核销付款余额折本币 |
| 7 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 9 | fbuscostbalance | 期末暂估成本余额 | numeric | 23 | 10 | √ | 0 | 期末暂估成本余额 |
| 10 | fstopdate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 11 | fprepaidamt | 本期未核销付款发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期未核销付款发生额 |
| 12 | fpaymenttype | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 13 | flocalbalanceamt | flocalbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | flocalprepaidperiodamt | flocalprepaidperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 17 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 18 | fprepaidperiodamt | fprepaidperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | flocalperiodfinamt | 期初财务余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初财务余额折本币 |
| 20 | ffinbalance | 期末财务余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末财务余额 |
| 21 | flocalbusamt | 本期暂估发生额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期暂估发生额折本币 |
| 22 | flocalperiodamt | flocalperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fbusbalance | 期末暂估余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末暂估余额 |
| 24 | fbusamt | 本期暂估发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期暂估发生额 |
| 25 | fcloseid | 关账序号 | int8 | 64 |  | √ | 0 | 关账序号 |
| 26 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 27 | fperiodbuscostamt | 期初暂估成本余额 | numeric | 23 | 10 | √ | 0 | 期初暂估成本余额 |
| 28 | flocalperiodbuscostamt | 期初暂估成本余额折本币 | numeric | 23 | 10 | √ | 0 | 期初暂估成本余额折本币 |
| 29 | flocalbuscostamt | 本期暂估成本发生额折本币 | numeric | 23 | 10 | √ | 0 | 本期暂估成本发生额折本币 |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 32 | flocalbusbalance | 期末暂估余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末暂估余额折本币 |
| 33 | fperiodamt | fperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 35 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 36 | fperiodfinamt | 期初财务余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初财务余额 |
| 37 | fperiodbusamt | 期初暂估余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初暂估余额 |
| 38 | flocalperiodbusamt | 期初暂估余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初暂估余额折本币 |
| 39 | flocalfinbalance | 期末财务余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末财务余额折本币 |
| 40 | flocalprepaidbalance | 期末未核销付款余额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末未核销付款余额折本币 |
| 41 | fprepaidbalance | 期末未核销付款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末未核销付款余额 |
| 42 | flocalbuscostbalance | 期末暂估成本余额折本币 | numeric | 23 | 10 | √ | 0 | 期末暂估成本余额折本币 |
| 43 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 44 | fbuscostamt | 本期暂估成本发生额 | numeric | 23 | 10 | √ | 0 | 本期暂估成本发生额 |
| 45 | flocalfinamt | 本期财务发生额折本币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期财务发生额折本币 |
| 46 | fbalanceamt | fbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | flocalprepaidbalanceamt | flocalprepaidbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 49 | fperiodprepaidamt | 期初未核销付款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初未核销付款余额 |
| 50 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_newbal_orgcloseid |  | forgid,fcloseid |
| 2 | idx_ap_newbal_closeid |  | fcloseid |
| 3 | t_ap_newbalance_pkey |  | fid |
