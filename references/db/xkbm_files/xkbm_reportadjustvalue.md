# 调整表调整记录-xkbm_reportadjustvalue

## 调整表调整记录-主表 t_xkbm_reportadjustvalue

- **表名称：** 调整表调整记录-主表
- **表名：** t_xkbm_reportadjustvalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 3 | fxkbmbusinessservice | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 4 | freportid | 调整表 | varchar | 36 |  | √ | ' ' | [预算报表 xkbm_report](../xkbm_files/xkbm_report.md) |
| 5 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 6 | foldvalue | 报表原值 | numeric | 23 | 10 | √ | 0 | 报表原值 |
| 7 | fbudgetvalue | 原始预算数 | numeric | 23 | 10 | √ | 0 | 原始预算数 |
| 8 | fvalid | 是否有效 | bpchar | 1 |  | √ | '1' | 是否有效 |
| 9 | fsheetid | sheetid | varchar | 50 |  | √ | ' ' | sheetid |
| 10 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 11 | fcalendarid | 预算日历 | int8 | 64 |  | √ | 0 | [预算日历 xkbm_budgetcalendar](../xkbm_files/xkbm_budgetcalendar.md) |
| 12 | fdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 13 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 14 | fgroup | group | varchar | 2000 |  | √ | ' ' | group |
| 15 | fadjustvalue | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 16 | fperiodtype | 期间类型 | varchar | 10 |  | √ | ' ' | 期间类型 |
| 17 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 18 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 19 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 20 | fdatatype | 项目数据类型类别 | varchar | 10 |  | √ | ' ' | 项目数据类型类别,枚举: 0 :金额 1 :数量 2 :单价 3 :比率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_adjustvalue_report |  | freportid |
| 2 | pk_xkbm_reportadjustvalue |  | fid |

---

## 调整表调整记录-多语言表 t_xkbm_reportadjustvalue_l

- **表名称：** 调整表调整记录-多语言表
- **表名：** t_xkbm_reportadjustvalue_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_adjustvalue_l |  | fid,flocaleid |
| 2 | pk_xkbm_reportadjustvalue_l |  | fpkid |
