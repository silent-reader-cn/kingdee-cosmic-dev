# 财务指标参数配置-didc_finance_param

## 财务指标参数配置-主表 t_didc_finance_param

- **表名称：** 财务指标参数配置-主表
- **表名：** t_didc_finance_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrencycode | 币种编码 | varchar | 255 |  | √ | ' ' | 币种编码 |
| 3 | famountunit | 金额单位 | varchar | 255 |  | √ | ' ' | 金额单位 |
| 4 | facctorg | 核算组织 | varchar | 255 |  | √ | ' ' | 核算组织 |
| 5 | fconsche | 合并方案 | varchar | 255 |  | √ | ' ' | 合并方案 |
| 6 | fconscopecode | 合并范围编码 | varchar | 255 |  | √ | ' ' | 合并范围编码 |
| 7 | fconschecode | 合并方案编码 | varchar | 255 |  | √ | ' ' | 合并方案编码 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | facctpolicy | 会计政策 | varchar | 255 |  | √ | ' ' | 会计政策 |
| 11 | freporttype | 报告类型 | varchar | 255 |  | √ | ' ' | 报告类型,枚举: REPORT :报表 INDIVIDUAL_REPORT :个别报表 CONSOLIDATED_REPORT :合并报表 |
| 12 | fconscope | 合并范围 | varchar | 255 |  | √ | ' ' | 合并范围 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | facctsyscode | 核算体系编码 | varchar | 255 |  | √ | ' ' | 核算体系编码 |
| 15 | famountunitcode | 金额单位编码 | varchar | 255 |  | √ | ' ' | 金额单位编码 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 19 | fapi_env | API环境配置 | int8 | 64 |  |  | 0 | [API环境配置 didc_api_env](../didc_files/didc_api_env.md) |
| 20 | fcurrency | 币种 | varchar | 255 |  | √ | ' ' | 币种 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 22 | facctpolicycode | 会计政策编码 | varchar | 255 |  | √ | ' ' | 会计政策编码 |
| 23 | facctorgcode | 核算组织编码 | varchar | 255 |  | √ | ' ' | 核算组织编码 |
| 24 | findexsource | 指标数据源 | varchar | 255 |  | √ | ' ' | 指标数据源,枚举: flagship :星空旗舰版 enterprise :星空企业版 |
| 25 | fperiodtype | 报告周期 | varchar | 255 |  | √ | ' ' | 报告周期,枚举: |
| 26 | facctsys | 核算体系 | varchar | 255 |  | √ | ' ' | 核算体系 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_finance_param |  | fid |
| 2 | idx_didc_finance_param_m0 |  | fbillno |
