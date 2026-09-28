# 报表维度发生数据-didc_rpt_dimension

## 报表维度发生数据-主表 t_didc_rpt_dimension

- **表名称：** 报表维度发生数据-主表
- **表名：** t_didc_rpt_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrencycode | 币种编码 | varchar | 255 |  | √ | ' ' | 币种编码 |
| 3 | fconscopename | 合并范围名称 | varchar | 255 |  | √ | ' ' | 合并范围名称 |
| 4 | facctorgname | 核算组织名称 | varchar | 255 |  | √ | ' ' | 核算组织名称 |
| 5 | fconscopecode | 合并范围编码 | varchar | 255 |  | √ | ' ' | 合并范围编码 |
| 6 | fconschecode | 合并方案编码 | varchar | 255 |  | √ | ' ' | 合并方案编码 |
| 7 | fcurrencyname | 币种名称 | varchar | 255 |  | √ | ' ' | 币种名称 |
| 8 | facctpolicyname | 会计政策名称 | varchar | 255 |  | √ | ' ' | 会计政策名称 |
| 9 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 10 | facctpolicycode | 会计政策编码 | varchar | 255 |  | √ | ' ' | 会计政策编码 |
| 11 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | facctorgcode | 核算组织编码 | varchar | 255 |  | √ | ' ' | 核算组织编码 |
| 13 | fconschename | 合并方案名称 | varchar | 255 |  | √ | ' ' | 合并方案名称 |
| 14 | fperiodtype | 周期类型 | varchar | 255 |  | √ | ' ' | 周期类型,枚举: MONTHLY :月报 QUARTERLY :季报 SEMI_ANNUAL :半年报 ANNUAL :年报 |
| 15 | ftenant_datacenter_name | 租户数据中心名称 | varchar | 255 |  | √ | ' ' | 租户数据中心名称 |
| 16 | fperiod | 期间 | varchar | 255 |  | √ | ' ' | 期间 |
| 17 | freporttype | 报表类型 | varchar | 255 |  | √ | ' ' | 报表类型,枚举: REPORT :报表 INDIVIDUAL_REPORT :个别报表 CONSOLIDATED_REPORT :合并报表 |
| 18 | ftenant_datacenter | 租户数据中心 | int8 | 64 |  | √ | 0 | 租户数据中心 |
| 19 | facctsysname | 核算体系名称 | varchar | 255 |  | √ | ' ' | 核算体系名称 |
| 20 | famountunitname | 金额单位名称 | varchar | 255 |  | √ | ' ' | 金额单位名称 |
| 21 | facctsyscode | 核算体系编码 | varchar | 255 |  | √ | ' ' | 核算体系编码 |
| 22 | famountunitcode | 金额单位编码 | varchar | 255 |  | √ | ' ' | 金额单位编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_rpt_dimension |  | fid |
| 2 | idx_didc_rpt_dimension |  | ftenant_datacenter |
