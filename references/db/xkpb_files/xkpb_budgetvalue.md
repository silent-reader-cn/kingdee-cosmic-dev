# 项目预算预算数后台数据-xkpb_budgetvalue

## 项目预算预算数后台数据-主表 t_xkpb_budgetvalue

- **表名称：** 项目预算预算数后台数据-主表
- **表名：** t_xkpb_budgetvalue

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
| 14 | fbasevalue | 综合本位币数值 | numeric | 23 | 10 |  | null | 综合本位币数值 |
| 15 | fremark | 批注 | varchar | 255 |  | √ | ' ' | 批注 |
| 16 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 17 | fdeptorgid | 来源基础资料 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fvalid | 有效性 | bpchar | 1 |  | √ | '1' | 有效性 |
| 19 | fadjustentryid | 调整单分录 | int8 | 64 |  | √ | 0 | 调整单分录 |
| 20 | fvalue | 数值 | numeric | 23 | 10 |  | null | 数值 |
| 21 | fyearperiod | 年期组合 | int4 | 32 |  | √ | 0 | 年期组合 |
| 22 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 23 | fperiodtype | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 24 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 27 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkpb_budgetvalue_fperiod |  | fperiod |
| 2 | pk_xkpb_budgetvalue |  | fentryid |
| 3 | idx_xkpb_budgetvalue_funitorg |  | forgunitid |
| 4 | idx_xkpb_budgetvalue_fgroup |  | fgroupid |
| 5 | idx_xkpb_budgetvalue_periodty |  | fperiodtype |
| 6 | idx_xkpb_budgetvalue_nonindex |  | fyear,fperiod,fperiodtype,forgunitid |
