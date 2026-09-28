# 还原追溯记录-cal_cr_retrospectrecord

## 还原追溯记录-主表 t_cal_cr_rtprecord

- **表名称：** 还原追溯记录-主表
- **表名：** t_cal_cr_rtprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | ' ' | 是否叶子节点 |
| 3 | fsrcid | 源单核算成本记录id | int8 | 64 |  | √ | 0 | 源单核算成本记录id |
| 4 | fisnested | 是否嵌套 | bpchar | 1 |  | √ | '0' | 是否嵌套 |
| 5 | fsrcentryid | 源单核算成本记录分录id | int8 | 64 |  | √ | 0 | 源单核算成本记录分录id |
| 6 | fdividebasiskeystr | 划分依据值 | varchar | 255 |  | √ | ' ' | 划分依据值 |
| 7 | fsrcbillno | 源单编码 | varchar | 50 |  | √ | ' ' | 源单编码 |
| 8 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 9 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 10 | fdestentryid | 目标核算成本记录分录id | int8 | 64 |  | √ | 0 | 目标核算成本记录分录id |
| 11 | fsrcsourcetype | 源单数据来源 | varchar | 50 |  | √ | ' ' | 源单数据来源,枚举: 0 :余额表 1 :核算成本记录 |
| 12 | fdestid | 目标核算成本记录id | int8 | 64 |  | √ | 0 | 目标核算成本记录id |
| 13 | funrealizeprofit | 未实现利润 | numeric | 23 | 10 | √ | 0 | 未实现利润 |
| 14 | fsrcbaseqty | 源单数量 | numeric | 23 | 10 | √ | 0 | 源单数量 |
| 15 | frangetype | 计算范围类型 | varchar | 50 |  | √ | ' ' | 计算范围类型,枚举: 1 :期末结存 2 :出库 3 :入库 |
| 16 | fpid | pid | varchar | 2000 |  | √ | ' ' | pid |
| 17 | fretrospectperiodid | 追溯期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 19 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsrcexrate | 源单汇率 | numeric | 23 | 10 | √ | 0 | 源单汇率 |
| 22 | fdestexrate | 目标单汇率 | numeric | 23 | 10 | √ | 0 | 目标单汇率 |
| 23 | fdestbillno | 目标单编码 | varchar | 50 |  | √ | ' ' | 目标单编码 |
| 24 | fsrcbaseunit | 源单计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 26 | fretrospectplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 27 | fcaldimensionkeystr | 核算维度值 | varchar | 255 |  | √ | ' ' | 核算维度值 |
| 28 | fcrentryid | 核算成本记录分录id | int8 | 64 |  | √ | 0 | 核算成本记录分录id |
| 29 | fcrid | 核算成本记录id | int8 | 64 |  | √ | 0 | 核算成本记录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cr_rtprecord_mo |  | fretrospectplanid |
| 2 | pk_t_cal_cr_rtprecord |  | fid |
