# 先进先出余额表-cal_balance_fifo

## 先进先出余额表-主表 t_cal_balance_fifo

- **表名称：** 先进先出余额表-主表
- **表名：** t_cal_balance_fifo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fbegincost | 期初成本(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本(废弃) |
| 4 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 5 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 6 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 7 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 11 | fbeginqty | 期初数量(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量(废弃) |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | flot | 批次 | varchar | 80 |  | √ | ' ' | 批次 |
| 14 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 16 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | fperiodid | 期间(废弃) | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 19 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fendunitcost | 结存单价 | numeric | 23 | 10 | √ | 0.0000000000 | 结存单价 |
| 21 | fbeginunitcost | 期初单价(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 期初单价(废弃) |
| 22 | fentryseq | 分录序号 | int8 | 64 |  | √ | 0 | 分录序号 |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 26 | fendcost | 结存成本 | numeric | 23 | 10 | √ | 0.0000000000 | 结存成本 |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fcalrptid | 结转报告ID | int8 | 64 |  | √ | 0 | 结转报告ID |
| 29 | fendqty | 结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 结存数量 |
| 30 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 31 | fbillentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 32 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_balfifo_mpc |  | fmaterialid,fperiodid,fcostaccountid |
| 2 | idx_cal_balfifo_beidce |  | fbillentryid,fcostsubelementid |
| 3 | t_cal_balance_fifo_pkey |  | fid |
