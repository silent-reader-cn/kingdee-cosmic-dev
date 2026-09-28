# 预算调整单-xkbm_budgetadjust

## 调整明细-多语言表 t_xkbm_budgetadjustentry_l

- **表名称：** 调整明细-多语言表
- **表名：** t_xkbm_budgetadjustentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetadjustentry_l |  | fpkid |
| 2 | idx_xkbm_budgetadjustentry_l |  | fentryid,flocaleid |

---

## 调整明细-子表 t_xkbm_budgetadjustentry

- **表名称：** 调整明细-子表
- **表名：** t_xkbm_budgetadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgroupid | 维度组合ID | int8 | 64 |  | √ | 0 | 维度组合ID |
| 3 | fcheckamount | 核定调整额 | numeric | 23 | 10 | √ | 0 | 核定调整额 |
| 4 | fstartamountyear | fstartamountyear | numeric | 23 | 10 | √ | 0 |  |
| 5 | fdimensionlistno | 预算维度组合编码 | varchar | 2000 |  | √ | ' ' | 预算维度组合编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapplyamount | 申请调整额 | numeric | 23 | 10 | √ | 0 | 申请调整额 |
| 8 | fsheetid | 表页ID | varchar | 36 |  | √ | ' ' | 表页ID |
| 9 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 10 | ffinalamount | 调整后 | varchar | 50 |  | √ | '0' | 调整后 |
| 11 | fschemeidentry | fschemeidentry | int8 | 64 |  | √ | 0 |  |
| 12 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 13 | fperiodentry | fperiodentry | varchar | 50 |  | √ | ' ' |  |
| 14 | fdimensionlist | 预算维度组合 | varchar | 2000 |  | √ | ' ' | 预算维度组合 |
| 15 | fyearentry | fyearentry | varchar | 50 |  | √ | ' ' |  |
| 16 | fstartamount | 调整前 | varchar | 50 |  | √ | '0' | 调整前 |
| 17 | forgunitidentry | forgunitidentry | int8 | 64 |  | √ | 0 |  |
| 18 | ffinalamountyear | ffinalamountyear | numeric | 23 | 10 | √ | 0 |  |
| 19 | fbusinesstypeid | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | frptschemeid | 样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 22 | freportentry | freportentry | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetadjustentry |  | fentryid |
| 2 | idx_xkbm_budgetadjustentry |  | fid |

---

## 预算调整单-主表 t_xkbm_budgetadjust

- **表名称：** 预算调整单-主表
- **表名：** t_xkbm_budgetadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountunit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 3 | freportadjust | 预算调整表 | varchar | 36 |  | √ | ' ' | [预算调整表 xkbm_reportadjust](../xkbm_files/xkbm_reportadjust.md) |
| 4 | fbwbcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 7 | fadjustdept | 调整部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsheetid | fsheetid | varchar | 50 |  | √ | ' ' |  |
| 10 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fitemdatatypeid | fitemdatatypeid | int8 | 64 |  | √ | 0 |  |
| 13 | fadjusttype | 调整类型 | varchar | 30 |  | √ | ' ' | 调整类型,枚举: 1 :计划外调整(计入调整数) 2 :计划内调整(计入原始数) |
| 14 | fperiodenddate | 周期结束日期 | timestamp | 0 |  |  | null | 周期结束日期 |
| 15 | fperiodfilter | 期过滤 | int4 | 32 |  | √ | 0 | 期过滤 |
| 16 | fbudgetmulti | fbudgetmulti | bpchar | 1 |  | √ | '0' |  |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 19 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdeptid | 调整部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | cycledate | 预算期间 | timestamp | 0 |  |  | null | 预算期间 |
| 23 | fcurrentapprover | 流程当前节点及处理人 | varchar | 255 |  | √ | ' ' | 流程当前节点及处理人 |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fbudgetmultiorg | fbudgetmultiorg | bpchar | 1 |  | √ | '0' |  |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | freportid | 预算报表 | varchar | 36 |  | √ | ' ' | [预算报表 xkbm_report](../xkbm_files/xkbm_report.md) |
| 28 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fregulateamount | fregulateamount | numeric | 23 | 10 | √ | 0 |  |
| 30 | fisregulate | 是否调剂单 | bpchar | 1 |  | √ | '0' | 是否调剂单 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fautoadjust | 自动创建 | bpchar | 1 |  | √ | '0' | 自动创建 |
| 33 | fyearfilter | 年过滤 | int4 | 32 |  | √ | 0 | 年过滤 |
| 34 | fsampleid | fsampleid | varchar | 36 |  | √ | ' ' |  |
| 35 | fadjustamount | 调整总金额 | numeric | 23 | 10 | √ | 0 | 调整总金额 |
| 36 | fratetypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 37 | fyear | 预算年度 | varchar | 30 |  | √ | ' ' | 预算年度,枚举: |
| 38 | fperiod | 预算期间 | varchar | 30 |  | √ | ' ' | 预算期间,枚举: |
| 39 | famountnotzero | famountnotzero | bpchar | 1 |  | √ | '0' |  |
| 40 | fbusinesstypeid | fbusinesstypeid | int8 | 64 |  | √ | 0 |  |
| 41 | fcycleid | 预算周期 | varchar | 30 |  | √ | ' ' | 预算周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 42 | fregulateamountbwb | fregulateamountbwb | numeric | 23 | 10 | √ | 0 |  |
| 43 | fregulatecause | fregulatecause | varchar | 255 |  | √ | ' ' |  |
| 44 | frptschemeid | frptschemeid | int8 | 64 |  | √ | 0 |  |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fbilltype | fbilltype | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_budgetadjust |  | fbillno |
| 2 | pk_xkbm_budgetadjust |  | fid |
