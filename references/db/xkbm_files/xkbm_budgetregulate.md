# 预算调剂单-xkbm_budgetregulate

## 预算调剂单-多语言表 t_xkbm_budgetadjust_l

- **表名称：** 预算调剂单-多语言表
- **表名：** t_xkbm_budgetadjust_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fregulatecause | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_budgetadjust_l |  | fid,flocaleid |
| 2 | pk_t_xkbm_budgetadjust_l |  | fpkid |

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
| 4 | fstartamountyear | 年度调整前 | numeric | 23 | 10 | √ | 0 | 年度调整前 |
| 5 | fdimensionlistno | 预算维度组合编码 | varchar | 2000 |  | √ | ' ' | 预算维度组合编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapplyamount | 申请调整额 | numeric | 23 | 10 | √ | 0 | 申请调整额 |
| 8 | fsheetid | 表页ID | varchar | 36 |  | √ | ' ' | 表页ID |
| 9 | fadjustreason | fadjustreason | varchar | 255 |  | √ | ' ' |  |
| 10 | ffinalamount | 调整后 | varchar | 50 |  | √ | '0' | 调整后 |
| 11 | fschemeidentry | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 12 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 13 | fperiodentry | 预算期间 | varchar | 50 |  | √ | ' ' | 预算期间,枚举: |
| 14 | fdimensionlist | 预算维度组合 | varchar | 2000 |  | √ | ' ' | 预算维度组合 |
| 15 | fyearentry | 预算年度 | varchar | 50 |  | √ | ' ' | 预算年度,枚举: |
| 16 | fstartamount | 调整前 | varchar | 50 |  | √ | '0' | 调整前 |
| 17 | forgunitidentry | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 18 | ffinalamountyear | 年度调整后 | numeric | 23 | 10 | √ | 0 | 年度调整后 |
| 19 | fbusinesstypeid | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | frptschemeid | 样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 22 | freportentry | 预算报表 | varchar | 36 |  | √ | ' ' | [预算报表 xkbm_report](../xkbm_files/xkbm_report.md) |

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

## 预算调剂单-主表 t_xkbm_budgetadjust

- **表名称：** 预算调剂单-主表
- **表名：** t_xkbm_budgetadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | famountunit | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 3 | freportadjust | freportadjust | varchar | 36 |  | √ | ' ' |  |
| 4 | fbwbcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 7 | fadjustdept | 调整部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsheetid | 表页ID | varchar | 50 |  | √ | ' ' | 表页ID |
| 10 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fitemdatatypeid | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 13 | fadjusttype | fadjusttype | varchar | 30 |  | √ | ' ' |  |
| 14 | fperiodenddate | 周期结束日期 | timestamp | 0 |  |  | null | 周期结束日期 |
| 15 | fperiodfilter | 期过滤 | int4 | 32 |  | √ | 0 | 期过滤 |
| 16 | fbudgetmulti | 跨期调剂 | bpchar | 1 |  | √ | '0' | 跨期调剂 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 19 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdeptid | 调整部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | cycledate | 预算期间 | timestamp | 0 |  |  | null | 预算期间 |
| 23 | fcurrentapprover | 流程当前节点及处理人 | varchar | 255 |  | √ | ' ' | 流程当前节点及处理人 |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fbudgetmultiorg | 跨组织调剂 | bpchar | 1 |  | √ | '0' | 跨组织调剂 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | freportid | 预算报表 | varchar | 36 |  | √ | ' ' | [预算报表 xkbm_report](../xkbm_files/xkbm_report.md) |
| 28 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fregulateamount | 调剂总金额 | numeric | 23 | 10 | √ | 0 | 调剂总金额 |
| 30 | fisregulate | 是否调剂单 | bpchar | 1 |  | √ | '0' | 是否调剂单 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fautoadjust | fautoadjust | bpchar | 1 |  | √ | '0' |  |
| 33 | fyearfilter | 年过滤 | int4 | 32 |  | √ | 0 | 年过滤 |
| 34 | fsampleid | 预算模版 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 35 | fadjustamount | fadjustamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fratetypeid | 汇率类型 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 37 | fyear | 预算年度 | varchar | 30 |  | √ | ' ' | 预算年度,枚举: 2012 :2012 2013 :2013 2014 :2014 2015 :2015 2016 :2016 2017 :2017 2018 :2018 2019 :2019 2020 :2020 2021 :2021 2022 :2022 2023 :2023 2024 :2024 2025 :2025 2026 :2026 2027 :2027 2028 :2028 2029 :2029 2030 :2030 2031 :2031 2032 :2032 2033 :2033 2034 :2034 2035 :2035 2036 :2036 2037 :2037 2038 :2038 2039 :2039 2040 :2040 2041 :2041 2042 :2042 2043 :2043 2044 :2044 2045 :2045 2046 :2046 2047 :2047 2048 :2048 2049 :2049 2050 :2050 2051 :2051 2052 :2052 2053 :2053 2054 :2054 2055 :2055 2056 :2056 2057 :2057 2058 :2058 2059 :2059 2060 :2060 2061 :2061 2062 :2062 2063 :2063 2064 :2064 2065 :2065 2066 :2066 2067 :2067 2068 :2068 2069 :2069 2070 :2070 2071 :2071 2072 :2072 2073 :2073 2074 :2074 2075 :2075 2076 :2076 2077 :2077 2078 :2078 2079 :2079 2080 :2080 |
| 38 | fperiod | 预算期间 | varchar | 30 |  | √ | ' ' | 预算期间,枚举: |
| 39 | famountnotzero | 特殊批量调整 | bpchar | 1 |  | √ | '0' | 特殊批量调整 |
| 40 | fbusinesstypeid | 预算业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 41 | fcycleid | 预算周期 | varchar | 30 |  | √ | ' ' | 预算周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 42 | fregulateamountbwb | 调剂总金额(本位币) | numeric | 23 | 10 | √ | 0 | 调剂总金额(本位币) |
| 43 | fregulatecause | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 44 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: 1 :组织内调剂 2 :组织间调剂 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_budgetadjust |  | fbillno |
| 2 | pk_xkbm_budgetadjust |  | fid |
