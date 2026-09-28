# 应收余额表-ar_balance

## 应收余额表-主表 t_ar_balance

- **表名称：** 应收余额表-主表
- **表名：** t_ar_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesmanid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | flocalreceivableamt | flocalreceivableamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | ffinamt | 本期财务发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期财务发生额 |
| 6 | flocalreceivedperiodamt | flocalreceivedperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | freceivingtypeid | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 8 | fstopdate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 9 | flocalbalanceamt | flocalbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 11 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 12 | flocalperiodfinamt | 期初财务余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初财务余额本位币 |
| 13 | ffinbalance | 期末财务余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末财务余额 |
| 14 | freceivableamt | freceivableamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | flocalperiodamt | flocalperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | flocalbusamt | 本期暂估发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期暂估发生额本位币 |
| 17 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 18 | flocalreceivedbalanceamt | flocalreceivedbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fbusbalance | 期末暂估余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末暂估余额 |
| 20 | flocalreceivedbalance | 期末未核销收款余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末未核销收款余额本位币 |
| 21 | fcloseid | 关账序号 | int8 | 64 |  | √ | 0 | 关账序号 |
| 22 | fbusamt | 本期暂估发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期暂估发生额 |
| 23 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | flocalreceivedamt | 本期未核销收款发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期未核销收款发生额本位币 |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 27 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 28 | flocalbusbalance | 期末暂估余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末暂估余额本位币 |
| 29 | fperiodreceivedamt | 期初未核销收款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初未核销收款余额 |
| 30 | fperiodamt | fperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 32 | freceivedbalanceamt | freceivedbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fperiodfinamt | 期初财务余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初财务余额 |
| 34 | freceivedamt | 本期未核销收款发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期未核销收款发生额 |
| 35 | freceivedbalance | 期末未核销收款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期末未核销收款余额 |
| 36 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 37 | fperiodbusamt | 期初暂估余额 | numeric | 23 | 10 | √ | 0.0000000000 | 期初暂估余额 |
| 38 | flocalperiodbusamt | 期初暂估余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初暂估余额本位币 |
| 39 | flocalperiodreceivedamt | 期初未核销收款余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期初未核销收款余额本位币 |
| 40 | flocalfinbalance | 期末财务余额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 期末财务余额本位币 |
| 41 | festimatedamt | festimatedamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fsalesdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 44 | flocalfinamt | 本期财务发生额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 本期财务发生额本位币 |
| 45 | fbalanceamt | fbalanceamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 48 | flocalestimatedamt | flocalestimatedamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | freceivedperiodamt | freceivedperiodamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 51 | fsalesgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |

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
