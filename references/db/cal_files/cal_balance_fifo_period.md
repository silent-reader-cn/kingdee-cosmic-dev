# 先进先出余额表（月末）-cal_balance_fifo_period

## 先进先出余额表（月末）-主表 t_cal_bal_fifo_period

- **表名称：** 先进先出余额表（月末）-主表
- **表名：** t_cal_bal_fifo_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fbegincost | 期初成本 | numeric | 23 | 10 | √ | 0 | 期初成本 |
| 4 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 9 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 10 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fbeginqty | 期初数量 | numeric | 23 | 10 | √ | 0 | 期初数量 |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 14 | flot | 批次 | varchar | 255 |  | √ | ' ' | 批次 |
| 15 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 17 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 20 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 21 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fendunitcost | 结存单价 | numeric | 23 | 10 | √ | 0 | 结存单价 |
| 23 | fbeginunitcost | 期初单价 | numeric | 23 | 10 | √ | 0 | 期初单价 |
| 24 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 25 | fentryseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 29 | fendcost | 结存成本 | numeric | 23 | 10 | √ | 0 | 结存成本 |
| 30 | fownerid | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fcalrptid | 结转报告ID | int8 | 64 |  | √ | 0 | 结转报告ID |
| 32 | fendqty | 结存数量 | numeric | 23 | 10 | √ | 0 | 结存数量 |
| 33 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 34 | fbillentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_balfifop_beidce |  | fbillentryid,fperiodid,fcostsubelementid |
| 2 | idx_cal_balfifop_mpc |  | fmaterialid,fperiodid,fcostaccountid |
| 3 | idx_cal_balfifop_cpm |  | fcostaccountid,fperiodid,fmaterialid |
| 4 | pk_cal_bal_fifo_period |  | fid |
