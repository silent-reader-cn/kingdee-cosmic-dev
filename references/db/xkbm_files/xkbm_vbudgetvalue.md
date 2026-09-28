# 版本化的预算数据-xkbm_vbudgetvalue

## 版本化的预算数据-主表 t_xkbm_vbudgetvalue

- **表名称：** 版本化的预算数据-主表
- **表名：** t_xkbm_vbudgetvalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | sheet页 | varchar | 50 |  | √ | ' ' | sheet页 |
| 2 | ftext | 文本 | varchar | 510 |  | √ | ' ' | 文本 |
| 3 | fgroupid | 维度组合 | int8 | 64 |  | √ | 0 | 维度组合 |
| 4 | fbwbcurrencyid | 综合本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fformulatext | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 6 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 7 | fbusinesstype | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 8 | forgtype | 来源基础资料类型 | varchar | 50 |  | √ | ' ' | 来源基础资料类型,枚举: bos_org :业务单元 bos_adminorg :行政组织（部门） |
| 9 | fislock | 锁定性 | bpchar | 1 |  | √ | '0' | 锁定性 |
| 10 | fadjusttype | 调整类别 | varchar | 10 |  | √ | ' ' | 调整类别,枚举: 1 :计划外调整(记入调整数) 2 :计划内调整(记入原始数) |
| 11 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 12 | fisadjust | 是否调整 | bpchar | 1 |  | √ | '0' | 是否调整 |
| 13 | fadjustid | 调整单 | int8 | 64 |  | √ | 0 | 调整单 |
| 14 | fversion | 版本 | int4 | 32 |  | √ | 0 | 版本 |
| 15 | fbasevalue | 综合本位币数值 | numeric | 23 | 10 |  | null | 综合本位币数值 |
| 16 | fremark | 批注 | varchar | 255 |  | √ | ' ' | 批注 |
| 17 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 18 | fdeptorgid | 来源基础资料 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fvalid | 有效性 | bpchar | 1 |  | √ | '1' | 有效性 |
| 20 | fadjustentryid | 调整单分录 | int8 | 64 |  | √ | 0 | 调整单分录 |
| 21 | fvalue | 数值 | numeric | 23 | 10 |  | null | 数值 |
| 22 | fyearperiod | 年期组合 | int4 | 32 |  | √ | 0 | 年期组合 |
| 23 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 24 | fperiodtype | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 25 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 28 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_vbudgetvalue_fperiod |  | fperiod |
| 2 | idx_xkbm_vbudgetvalue_fgroup |  | fgroupid |
| 3 | idx_xkbm_vbudgetvalue_periodty |  | fperiodtype |
| 4 | idx_xkbm_vbudgetvalue_nonindex |  | fyear,fperiod,fperiodtype,forgunitid |
| 5 | idx_xkbm_vbudgetvalue_funitorg |  | forgunitid |
| 6 | pk_xkbm_vbudgetvalue |  | fentryid |
