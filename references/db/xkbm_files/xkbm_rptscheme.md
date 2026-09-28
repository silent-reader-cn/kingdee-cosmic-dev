# 预算模板样式方案-xkbm_rptscheme

## 项目数据类型预算数区域-子表 t_xkbm_datatypeentry

- **表名称：** 项目数据类型预算数区域-子表
- **表名：** t_xkbm_datatypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetdataformula | 预算表取数公式 | varchar | 2000 |  | √ | ' ' | 预算表取数公式 |
| 3 | fislock | 锁定 | bpchar | 1 |  | √ | '0' | 锁定 |
| 4 | fmultisjformula | 实际数多场景模式 | bpchar | 1 |  | √ | '0' | 实际数多场景模式 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsjdataformula | 实际数表取数公式 | varchar | 2000 |  | √ | ' ' | 实际数表取数公式 |
| 7 | fbusinesstype | 业务类型 | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 8 | fmultibudgetformula | 预算数多场景模式 | bpchar | 1 |  | √ | '0' | 预算数多场景模式 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_datatypeentry |  | fid |
| 2 | pk_xkbm_datatypeentry |  | fentryid |

---

## 维度-多语言表 t_xkbm_wizarddimension_l

- **表名称：** 维度-多语言表
- **表名：** t_xkbm_wizarddimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmulidimpropnames | 显示属性多语言 | varchar | 2000 |  | √ | ' ' | 显示属性多语言 |
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
| 1 | pk_xkbm_wizarddimension_l |  | fpkid |
| 2 | idx_xkbm_wizarddimension_l |  | fentryid,flocaleid |

---

## 维度-子表 t_xkbm_wizarddimension

- **表名称：** 维度-子表
- **表名：** t_xkbm_wizarddimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimpropnames | 显示属性 | varchar | 300 |  | √ | ' ' | 显示属性 |
| 3 | fdimensionindex | 维度位置 | varchar | 50 |  | √ | ' ' | 维度位置 |
| 4 | fmulidimpropnames | 显示属性多语言 | varchar | 2000 |  | √ | ' ' | 显示属性多语言 |
| 5 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 6 | fdimpropfields | 显示属性字段 | varchar | 300 |  | √ | ' ' | 显示属性字段 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fisshowtotals | 显示小计 | bpchar | 1 |  | √ | '1' | 显示小计 |
| 9 | fdimensionposition | 填充方向 | varchar | 30 |  | √ | ' ' | 填充方向,枚举: 0 :行 1 :列 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fautoindent | 自动缩进 | bpchar | 1 |  | √ | '0' | 自动缩进 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_wizarddimension |  | fentryid |
| 2 | idx_xkbm_wizarddimension |  | fid |

---

## 预算模板样式方案-多语言表 t_xkbm_rptscheme_l

- **表名称：** 预算模板样式方案-多语言表
- **表名：** t_xkbm_rptscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fdimensioninfo | 维度组合 | varchar | 2000 |  | √ | ' ' | 维度组合 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptscheme_l |  | fid,flocaleid |
| 2 | pk_xkbm_rptscheme_l |  | fpkid |

---

## 业务类型-多选基础资料表 t_xkbm_rptbusinesstypes

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_xkbm_rptbusinesstypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_rptbusinesstypes |  | fpkid |
| 2 | idx_xkbm_rptbusinesstypes |  | fid |

---

## 辅助编制区域公式子单据体-子表 t_xkbm_datatypeformulaact

- **表名称：** 辅助编制区域公式子单据体-子表
- **表名：** t_xkbm_datatypeformulaact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fformulaact | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 2 | fformulacategoryact | 公式类型 | varchar | 30 |  | √ | '0' | 公式类型,枚举: 0 :函数 1 :常规计算 2 :占比计算 |
| 3 | fconditionjsonact | 条件JSON | varchar | 2000 |  | √ | ' ' | 条件JSON |
| 4 | fformulatypeact | 类型 | varchar | 30 |  | √ | '0' | 类型,枚举: 0 :预算数 1 :实际数 |
| 5 | fconditionact | 条件 | varchar | 2000 |  | √ | ' ' | 条件 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fnotfilldimact | 不显示维度 | varchar | 2000 |  | √ | ' ' | 不显示维度 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_datatypeformulaact |  | fdetailid |
| 2 | idx_xkbm_datatypeformulaact |  | fentryid |

---

## 预算数区域公式子单据体-子表 t_xkbm_datatypeformula

- **表名称：** 预算数区域公式子单据体-子表
- **表名：** t_xkbm_datatypeformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fformulatype | 类型 | varchar | 30 |  | √ | '0' | 类型,枚举: 0 :预算数 1 :实际数 |
| 2 | fformula | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 3 | fnotfilldim | 不显示维度 | varchar | 2000 |  | √ | ' ' | 不显示维度 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcondition | 条件 | varchar | 2000 |  | √ | ' ' | 条件 |
| 6 | fconditionjson | 条件JSON | varchar | 2000 |  | √ | ' ' | 条件JSON |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fformulacategory | 公式类型 | varchar | 30 |  | √ | '0' | 公式类型,枚举: 0 :函数 1 :常规计算 2 :占比计算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_datatypeformula |  | fdetailid |
| 2 | idx_xkbm_datatypeformula |  | fentryid |

---

## 预算模板样式方案-主表 t_xkbm_rptscheme

- **表名称：** 预算模板样式方案-主表
- **表名：** t_xkbm_rptscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fismulorg | 多组织预算表 | bpchar | 1 |  | √ | '0' | 多组织预算表 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 模板样式方案分组 xkbm_rptschemegroup |
| 4 | fisshowgrandtotal | 显示总计 | bpchar | 1 |  | √ | '1' | 显示总计 |
| 5 | fdimensioninfo | 维度组合 | varchar | 2000 |  | √ | ' ' | 维度组合 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbudgetcalendar | 预算日历 | int8 | 64 |  | √ | 0 | 预算日历 xkbm_budgetcalendar |
| 9 | fversiongroupid | 版本分组id | int8 | 64 |  | √ | 0 | 版本分组id |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsplitshowname | 显示属性和维度分开显示 | bpchar | 1 |  | √ | '0' | 显示属性和维度分开显示 |
| 13 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 17 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | 预算业务服务 xkbm_businessservice |
| 18 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fshownameposition | 显示属性在维度前 | bpchar | 1 |  | √ | '0' | 显示属性在维度前 |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | fcycles | 报表包含周期 | varchar | 30 |  | √ | ' ' | 报表包含周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 24 | fislastedversion | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fcycle | 报表周期 | varchar | 30 |  | √ | ' ' | 报表周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 28 | frpttype | 报表类型 | varchar | 30 |  | √ | ' ' | 报表类型,枚举: 60 :预算报表 |
| 29 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_rptscheme |  | fid |
| 2 | idx_xkbm_rptscheme |  | fnumber |
| 3 | idx_xkbm_rptscheme_ver |  | fversiongroupid |

---

## 项目数据类型辅助编制区域-子表 t_xkbm_datatypeentryact

- **表名称：** 项目数据类型辅助编制区域-子表
- **表名：** t_xkbm_datatypeentryact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetdataformulaact | 预算表取数公式 | varchar | 2000 |  | √ | ' ' | 预算表取数公式 |
| 3 | factualfilltype | 显示在预算数 | varchar | 30 |  | √ | ' ' | 显示在预算数,枚举: 0 :之前 1 :之后 |
| 4 | fsjdataformulaact | 实际数表取数公式 | varchar | 2000 |  | √ | ' ' | 实际数表取数公式 |
| 5 | fmultisjformulaact | 实际数多场景模式 | bpchar | 1 |  | √ | '0' | 实际数多场景模式 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fitemdatatypeactual | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |
| 8 | fislockact | 锁定 | bpchar | 1 |  | √ | '0' | 锁定 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbusinesstypeactual | 业务类型 | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 11 | fmultibudgetformulaact | 预算数多场景模式 | bpchar | 1 |  | √ | '0' | 预算数多场景模式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_datatypeentryact |  | fid |
| 2 | pk_xkbm_datatypeentryact |  | fentryid |
