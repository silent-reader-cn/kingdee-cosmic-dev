# 成组消耗记录-cal_cr_group_cumrec

## 成组消耗记录-主表 t_cal_cr_group_cumrec

- **表名称：** 成组消耗记录-主表
- **表名：** t_cal_cr_group_cumrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 成组关系id | int8 | 64 |  | √ | 0 | 成组关系id |
| 3 | finqty | 来源入库数量 | numeric | 23 | 10 | √ | 0 | 来源入库数量 |
| 4 | foutqty | 目标出库数量 | numeric | 23 | 10 | √ | 0 | 目标出库数量 |
| 5 | fdestgroupid | 目标成组id | int8 | 64 |  | √ | 0 | 目标成组id |
| 6 | fsrcgroupqty | 来源成组数量 | numeric | 23 | 10 | √ | 0 | 来源成组数量 |
| 7 | finbookdate | 来源入库记账日期 | timestamp | 0 |  |  | null | 来源入库记账日期 |
| 8 | foutentryid | 目标出库分录id | int8 | 64 |  | √ | 0 | 目标出库分录id |
| 9 | foutbillno | 目标出库编码 | varchar | 50 |  | √ | ' ' | 目标出库编码 |
| 10 | finbillno | 来源入库单编码 | varchar | 50 |  | √ | ' ' | 来源入库单编码 |
| 11 | fdestgroupbillno | 目标成组编码 | varchar | 50 |  | √ | ' ' | 目标成组编码 |
| 12 | fincreatetime | 来源入库创建日期 | timestamp | 0 |  |  | null | 来源入库创建日期 |
| 13 | fcostaccountid | 目标单成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | fsrcgroupentryid | 来源成组分录id | int8 | 64 |  | √ | 0 | 来源成组分录id |
| 15 | finentryid | 来源入库单分录id | int8 | 64 |  | √ | 0 | 来源入库单分录id |
| 16 | foutcreatetime | 目标出库创建日期 | timestamp | 0 |  |  | null | 目标出库创建日期 |
| 17 | fdestgroupqty | 目标成组数量 | numeric | 23 | 10 | √ | 0 | 目标成组数量 |
| 18 | finbizdate | 来源入库业务日期 | timestamp | 0 |  |  | null | 来源入库业务日期 |
| 19 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fsrcgroupbillno | 来源成组编码 | varchar | 50 |  | √ | ' ' | 来源成组编码 |
| 21 | foutid | 目标出库id | int8 | 64 |  | √ | 0 | 目标出库id |
| 22 | fperiodid | 追溯期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 23 | foutmaterialid | 目标出库物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 24 | fcreatetime | 当前单创建时间 | timestamp | 0 |  |  | null | 当前单创建时间 |
| 25 | foutbizdate | 目标出库业务日期 | timestamp | 0 |  |  | null | 目标出库业务日期 |
| 26 | fdestgroupentryid | 目标成组分录id | int8 | 64 |  | √ | 0 | 目标成组分录id |
| 27 | finid | 来源入库单id | int8 | 64 |  | √ | 0 | 来源入库单id |
| 28 | fintype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: 0 :余额表 1 :核算成本记录 |
| 29 | finmaterialid | 来源入库物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 30 | foutauditdate | 目标出库审核时间 | timestamp | 0 |  |  | null | 目标出库审核时间 |
| 31 | frtpplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 32 | fsrcgroupid | 来源成组id | int8 | 64 |  | √ | 0 | 来源成组id |
| 33 | finauditdate | 来源入库审核时间 | timestamp | 0 |  |  | null | 来源入库审核时间 |
| 34 | foutbookdate | 目标出库记账日期 | timestamp | 0 |  |  | null | 目标出库记账日期 |
| 35 | fgrouptype | 成组类型 | varchar | 50 |  | √ | ' ' | 成组类型,枚举: group :成组关系 prodcum :生产消耗关系 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_cr_group_cumrec |  | fid |
| 2 | idx_ccgc_destgroupentryid |  | fdestgroupentryid |
| 3 | idx_ccgc_srcgroupentryid |  | fsrcgroupentryid |
