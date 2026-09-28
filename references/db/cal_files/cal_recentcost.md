# 即时成本-cal_recentcost

## 即时成本-主表 t_cal_recentcost

- **表名称：** 即时成本-主表
- **表名：** t_cal_recentcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | fprice | 即时单位成本 | numeric | 23 | 10 | √ | 0.0000000000 | 即时单位成本 |
| 11 | frecentcost | 最近结存成本 | numeric | 23 | 10 | √ | 0.0000000000 | 最近结存成本 |
| 12 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 13 | frecentqty | 最近结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 最近结存数量 |
| 14 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 15 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fcalrptid | 结转报告ID | int8 | 64 |  | √ | 0 | 结转报告ID |
| 17 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 18 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 20 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 21 | flot | 批次 | varchar | 80 |  | √ | ' ' | 批次 |
| 22 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_recost_ma |  | fmaterialid |
| 2 | t_cal_recentcost_pkey |  | fid |
