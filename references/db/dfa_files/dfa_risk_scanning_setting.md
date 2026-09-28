# 风险扫描设置-dfa_risk_scanning_setting

## 风险扫描设置-主表 t_dfa_risk_scan_settting

- **表名称：** 风险扫描设置-主表
- **表名：** t_dfa_risk_scan_settting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscan_start_day_num | 执行每期开始天数 | int8 | 64 |  | √ | 0 | 执行每期开始天数 |
| 3 | fpolicy_code | 会计政策.编码 | varchar | 50 |  | √ | ' ' | 会计政策.编码 |
| 4 | fscantype | 扫描类型 | varchar | 50 |  | √ | ' ' | 扫描类型,枚举: REPORT :报表 INDIVIDUAL_REPORT :个别报表 CONSOLIDATED_REPORT :合并报表 |
| 5 | fcurrencycode | 币种.编码 | varchar | 50 |  | √ | ' ' | 币种.编码 |
| 6 | fconsolidationscheme_code | 合并方案.编码 | varchar | 50 |  | √ | ' ' | 合并方案.编码 |
| 7 | fis_per_scan | 每期定时扫描 | bpchar | 1 |  | √ | '0' | 每期定时扫描 |
| 8 | fexecutetime | 执行时间 | int4 | 32 |  | √ | '-1' | 执行时间 |
| 9 | fcurrencyname | 币种.名称 | varchar | 255 |  | √ | ' ' | 币种.名称 |
| 10 | faccountingorg_code | 核算体系.编码 | varchar | 50 |  | √ | ' ' | 核算体系.编码 |
| 11 | fpolicy_name | 会计政策.名称 | varchar | 255 |  | √ | ' ' | 会计政策.名称 |
| 12 | fdata_center | 租户数据中心 | int8 | 64 |  | √ | 0 | [租户数据中心 dfa_tenant_datacenter](../dfa_files/dfa_tenant_datacenter.md) |
| 13 | faccountingorg_name | 核算体系.名称 | varchar | 255 |  | √ | ' ' | 核算体系.名称 |
| 14 | fconsolidationscope_name | 合并范围.名称 | varchar | 255 |  | √ | ' ' | 合并范围.名称 |
| 15 | famount_unit_code | 金额单位.编码 | varchar | 50 |  | √ | ' ' | 金额单位.编码 |
| 16 | forg_name | 组织.名称 | varchar | 255 |  | √ | ' ' | 组织.名称 |
| 17 | fconsolidationscope_code | 合并范围.编码 | varchar | 50 |  | √ | ' ' | 合并范围.编码 |
| 18 | forg_code | 组织.编码 | varchar | 50 |  | √ | ' ' | 组织.编码 |
| 19 | fconsolidationscheme_name | 合并方案.名称 | varchar | 255 |  | √ | ' ' | 合并方案.名称 |
| 20 | fcycletype | 周期类型 | varchar | 50 |  | √ | ' ' | 周期类型,枚举: MONTHLY :月报 QUARTERLY :季报 SEMI_ANNUAL :半年报 ANNUAL :年报 |
| 21 | fexcutetime | fexcutetime | int4 | 32 |  | √ | '-1' |  |
| 22 | famount_unit_name | 金额单位.名称 | varchar | 255 |  | √ | ' ' | 金额单位.名称 |
| 23 | fcombofield | fcombofield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_risk_scan_settting |  | fdata_center |
| 2 | pk_dfa_risk_scan_settting |  | fid |
