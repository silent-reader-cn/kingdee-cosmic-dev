# 出库序列记录-cal_outqueuerecord

## 出库序列记录-主表 t_cal_outqueuerecord

- **表名称：** 出库序列记录-主表
- **表名：** t_cal_outqueuerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fbilltypenum | 单据类型编码 | varchar | 50 |  | √ | ' ' | 单据类型编码 |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fcalbillentryid | 核算单据分录ID | int8 | 64 |  | √ | 0 | 核算单据分录ID |
| 7 | fsignum | 数值方向 | int8 | 64 |  | √ | 1 | 数值方向 |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | ffee | 采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 采购成本 |
| 10 | flocalcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 实际成本 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | funitprocesscost | 单位委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 单位委外费用 |
| 14 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 16 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | fcostrecordentryid | 成本记录分录ID | int8 | 64 |  | √ | 0 | 成本记录分录ID |
| 20 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 21 | fcalorgid | 核算组织ID | int8 | 64 |  | √ | 0 | 核算组织ID |
| 22 | fcalbillid | 核算单据ID | int8 | 64 |  | √ | 0 | 核算单据ID |
| 23 | fbillnumber | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 24 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 25 | fownerid | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fprocesscost | 委外费用 | numeric | 23 | 10 | √ | 0.0000000000 | 委外费用 |
| 29 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 30 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 31 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 32 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 33 | fwarehsid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |
| 35 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 36 | funitfee | 单位采购成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位采购成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_outqueuerecord_pkey |  | fid |
| 2 | idx_cal_outrd_billid |  | fcalbillid |
