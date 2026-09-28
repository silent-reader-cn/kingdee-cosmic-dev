# 预算模板-xkbm_reportsample

## 主维度-多选基础资料表 t_xkbm_rptmdims

- **表名称：** 主维度-多选基础资料表
- **表名：** t_xkbm_rptmdims

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptmdims |  | fid |
| 2 | pk_t_xkbm_rptmdims |  | fpkid |

---

## 预算模板-多语言表 t_xkbm_report_l

- **表名称：** 预算模板-多语言表
- **表名：** t_xkbm_report_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 3 | fversionreason | 版本化原因 | varchar | 2000 |  | √ | ' ' | 版本化原因 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fdimensionvaluename | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 6 | fmaindimnamefilter | 主维度 | varchar | 600 |  |  | ' ' | 主维度 |
| 7 | frptschemename | 包含预算样式方案 | varchar | 2000 |  | √ | ' ' | 包含预算样式方案 |
| 8 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 9 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_report_l |  | fid |
| 2 | pk_xkbm_report_l |  | fpkid |

---

## 单据体-子表 t_xkbm_sheet

- **表名称：** 单据体-子表
- **表名：** t_xkbm_sheet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fsheettype | 表页类型 | int8 | 64 |  | √ | 0 | 表页类型 |
| 3 | fsumrptsettingid | 汇总设置 | int8 | 64 |  | √ | 0 | [预算汇总表设置 xkbm_sumrptsetting](../xkbm_files/xkbm_sumrptsetting.md) |
| 4 | fsheetname | 表页名称 | varchar | 50 |  | √ | ' ' | 表页名称 |
| 5 | fjsoncontent | 前端模型 | text | 0 |  |  | null | 前端模型 |
| 6 | fdimorgunitid | 多组织维度值 | text | 0 |  |  | null | 多组织维度值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdimorgunitid_tag | 多组织维度值_详情 | text | 0 |  |  | null | 多组织维度值_详情 |
| 9 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | [预算模板样式方案 xkbm_rptscheme](../xkbm_files/xkbm_rptscheme.md) |
| 10 | fsamplesheetid | 模版页签id | varchar | 50 |  | √ | ' ' | 模版页签id |
| 11 | fsheetid | fsheetid | varchar | 36 |  | √ | ' ' | id |
| 12 | fcontainrptscheme | 是否包含模板样式方案 | bpchar | 1 |  | √ | '0' | 是否包含模板样式方案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fsheetid | fsheetid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bm_sheet_frptid |  | fid |
| 2 | pk_xkbm_sheet |  | fsheetid |

---

## 多组织单据体-子表 t_xkbm_rptorgentryentity

- **表名称：** 多组织单据体-子表
- **表名：** t_xkbm_rptorgentryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fsampleidentry | 预算模板 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 3 | fdeptorgidentry | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 4 | forgunitidentry | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | forgtypeentry | 组织类型 | varchar | 10 |  | √ | ' ' | 组织类型,枚举: ORG :组织 DEPT :部门 |
| 7 | forgentrysheetid | sheet页id | varchar | 50 |  | √ | ' ' | sheet页id |
| 8 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptorgentryentity_fk |  | fid |
| 2 | pk_xkbm_rptorgentryentity |  | fentryid |

---

## 预算模板-主表 t_xkbm_report

- **表名称：** 预算模板-主表
- **表名：** t_xkbm_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [预算模板分组 xkbm_reportgroup](../xkbm_files/xkbm_reportgroup.md) |
| 3 | freplaystatus | 批复状态 | varchar | 50 |  | √ | ' ' | 批复状态,枚举: 1 :批复中 2 :部分批复 3 :已批复 |
| 4 | fbwbcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fdimensionid | 主维度值整数 | int8 | 64 |  | √ | 0 | 主维度值整数 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fiscurrencybwb | 综合本位币 | bpchar | 1 |  | √ | '0' | 综合本位币 |
| 8 | forgtype | 组织类型 | varchar | 10 |  | √ | ' ' | 组织类型,枚举: DEPT :部门 ORG :组织 |
| 9 | fuserorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frptschemename | 包含预算样式方案 | varchar | 2000 |  | √ | ' ' | 包含预算样式方案 |
| 12 | fmaindimflex | 主维度 | int8 | 64 |  | √ | 0 | null 010 |
| 13 | fismaindim | 主维度报表 | bpchar | 1 |  | √ | '0' | 主维度报表 |
| 14 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 报表编号 | varchar | 50 |  | √ | ' ' | 报表编号 |
| 16 | frptstyle | 前端模型 | text | 0 |  |  | null | 前端模型 |
| 17 | famountunitid | 金额单位 | int8 | 64 |  | √ | 0 | [金额单位 xkbd_amountunit](../fibd_files/xkbd_amountunit.md) |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fassistantid | 主维度值文本 | varchar | 50 |  | √ | ' ' | 主维度值文本 |
| 21 | fcurrentapprover | fcurrentapprover | varchar | 255 |  | √ | ' ' |  |
| 22 | fownerorgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fadjustversion | fadjustversion | int4 | 32 |  | √ | 0 |  |
| 24 | fmaindimnamefilter | 主维度 | varchar | 600 |  |  | ' ' | 主维度 |
| 25 | fstyletype | 报表样式 | varchar | 10 |  | √ | ' ' | 报表样式,枚举: 0 :交叉透视表 1 :普通罗列表 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 28 | fsampleid | 预算模板 | varchar | 36 |  | √ | ' ' | [组织模板查询 xkbm_orgreport](../xkbm_files/xkbm_orgreport.md) |
| 29 | fadjustreason | 调整事由 | varchar | 255 |  | √ | ' ' | 调整事由 |
| 30 | forglayersum | 逐层汇总 | bpchar | 1 |  | √ | '0' | 逐层汇总 |
| 31 | frptmodel | 后端模型 | text | 0 |  |  | null | 后端模型 |
| 32 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 33 | fversioncreator | fversioncreator | int8 | 64 |  | √ | 0 |  |
| 34 | fperiod | 期间 | varchar | 10 |  | √ | ' ' | 期间,枚举: |
| 35 | fbackupreportid | 备份的报表ID | varchar | 36 |  | √ | ' ' | 备份的报表ID |
| 36 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fexcutestatus | 执行状态 | varchar | 10 |  | √ | ' ' | 执行状态,枚举: 1 :未执行 2 :部分执行 3 :执行中 4 :部分关闭（未执行和已关闭） 5 :已关闭 6 :部分关闭（执行中和已关闭） 7 :部分关闭（未执行、执行中和已关闭） |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 40 | fversionnum | fversionnum | varchar | 50 |  | √ | ' ' |  |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fallowreload | 打开是否提示重新加载 | bpchar | 1 |  | √ | '0' | 打开是否提示重新加载 |
| 43 | fcontainformula | fcontainformula | bpchar | 1 |  | √ | '0' |  |
| 44 | fhasprocessformula | 是否处理过公式 | bpchar | 1 |  | √ | '0' | 是否处理过公式 |
| 45 | fschemeid | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 46 | fadjustdept | fadjustdept | int8 | 64 |  | √ | 0 |  |
| 47 | frptversion | frptversion | int8 | 64 |  | √ | 0 |  |
| 48 | fdimensiontypeid | 主维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 49 | fsourcesampleid | 关联分发模板 | varchar | 36 |  | √ | ' ' | [预算模板 xkbm_reportsample](../xkbm_files/xkbm_reportsample.md) |
| 50 | fislatestversion | fislatestversion | bpchar | 1 |  | √ | '0' |  |
| 51 | fmaindimref | 主维度引用 | int8 | 64 |  | √ | 0 | [主维度组合引用 xkbm_maindimref](../xkbm_files/xkbm_maindimref.md) |
| 52 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 55 | fadjusttype | fadjusttype | varchar | 50 |  | √ | ' ' |  |
| 56 | fdate | 报表日期 | timestamp | 0 |  |  | null | 报表日期 |
| 57 | fperiodfilter | fperiodfilter | int4 | 32 |  | √ | 0 |  |
| 58 | fmaindimnumberfilter | 主维度编码过滤 | varchar | 600 |  |  | ' ' | 主维度编码过滤 |
| 59 | forgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织选择 xkbm_orgselect](../xkbm_files/xkbm_orgselect.md) |
| 60 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 61 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 62 | fversionreason | 版本化原因 | varchar | 2000 |  | √ | ' ' | 版本化原因 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | fdimensionvaluename | 维度值 | varchar | 255 |  | √ | ' ' | 维度值 |
| 65 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 66 | fdeptorgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 67 | fissample | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 68 | fyearfilter | fyearfilter | int4 | 32 |  | √ | 0 |  |
| 69 | fismultiorg | 是否多组织报表 | bpchar | 1 |  | √ | '0' | 是否多组织报表 |
| 70 | fratetypeid | 汇率类型 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 71 | fyear | 年度 | varchar | 10 |  | √ | ' ' | 年度,枚举: |
| 72 | fcreatestyle | 创建方式 | varchar | 10 |  | √ | ' ' | 创建方式,枚举: 0 :标准 1 :舍位平衡 2 :共享 3 :共享(未检查) 8 :外币折算 4 :自动生成 5 :分发 |
| 73 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 74 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 60 :预算报表模板 61 :预算报表 62 :预算实际数模板 63 :预算实际数报表 |
| 75 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 76 | frecalculatedate | 列表重算时间 | timestamp | 0 |  |  | null | 列表重算时间 |
| 77 | fversioncreatetime | fversioncreatetime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_report |  | fid |
| 2 | idx_xkbm_report_fsampleid |  | fsampleid |
