# 预算模板样式方案-xkbm_rptscheme

## 项目数据类型预算数区域-子表 t_xkbm_datatypeentry

- **表名称：** 项目数据类型预算数区域-子表
- **表名：** t_xkbm_datatypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetdataformula | 预算表取数公式 | varchar | 2000 |  | √ | ' ' | 预算表取数公式 |
| 3 | fmodeltype | 供应/需求 | varchar | 10 |  | √ | ' ' | 供应/需求,枚举: 1 :供应 2 :需求 |
| 4 | fnoallowadjust | 禁止调整 | bpchar | 1 |  | √ | '0' | 禁止调整 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbusinesstype | 业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 7 | fitemdatatypealiasname | 预算表显示名称 | varchar | 255 |  | √ | ' ' | 预算表显示名称 |
| 8 | fsjdatatypealiasname | 实际数表显示名称 | varchar | 255 |  | √ | ' ' | 实际数表显示名称 |
| 9 | fislock | 锁定 | bpchar | 1 |  | √ | '0' | 锁定 |
| 10 | fmultisjformula | 实际数多场景模式 | bpchar | 1 |  | √ | '0' | 实际数多场景模式 |
| 11 | fsjdataformula | 实际数表取数公式 | varchar | 2000 |  | √ | ' ' | 实际数表取数公式 |
| 12 | fmultibudgetformula | 预算数多场景模式 | bpchar | 1 |  | √ | '0' | 预算数多场景模式 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

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
| 2 | faliasname | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fmulirefdimensionfield | 来源维度字段多语言 | varchar | 300 |  | √ | ' ' | 来源维度字段多语言 |

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

## 维度映射方案-多选基础资料表 t_xkbm_rptscheme_dimmap

- **表名称：** 维度映射方案-多选基础资料表
- **表名：** t_xkbm_rptscheme_dimmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预算维度映射 xkbm_dimmapping](../xkbm_files/xkbm_dimmapping.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_rptscheme_dimmap |  | fpkid |
| 2 | idx_xkbm_rptscheme_dimmap |  | fdetailid |

---

## 维度-子表 t_xkbm_wizarddimension

- **表名称：** 维度-子表
- **表名：** t_xkbm_wizarddimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freportdimmt | 报表允许为空 | bpchar | 1 |  | √ | '0' | 报表允许为空 |
| 3 | fdimensionindex | 维度位置 | varchar | 50 |  | √ | ' ' | 维度位置 |
| 4 | frefdimensionfieldid | 关联维度字段id | varchar | 100 |  | √ | ' ' | 关联维度字段id |
| 5 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmaindim | 主维度 | bpchar | 1 |  | √ | '0' | 主维度 |
| 8 | frefdimensionid | 关联维度 | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 9 | fmulirefdimensionfield | 来源维度字段多语言 | varchar | 300 |  | √ | ' ' | 来源维度字段多语言 |
| 10 | fdimpropnames | 显示属性 | varchar | 300 |  | √ | ' ' | 显示属性 |
| 11 | fmulidimpropnames | 显示属性多语言 | varchar | 2000 |  | √ | ' ' | 显示属性多语言 |
| 12 | fsampledimmt | 模板允许为空 | bpchar | 1 |  | √ | '0' | 模板允许为空 |
| 13 | frptitemformula | 以报表项目公式为准 | bpchar | 1 |  | √ | '0' | 以报表项目公式为准 |
| 14 | fisrefdim | 关联维度 | bpchar | 1 |  | √ | '0' | 关联维度 |
| 15 | fdimpropfields | 显示属性字段 | varchar | 300 |  | √ | ' ' | 显示属性字段 |
| 16 | fisshowtotals | 显示小计 | bpchar | 1 |  | √ | '1' | 显示小计 |
| 17 | faliasname | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 18 | fdimensionposition | 填充方向 | varchar | 30 |  | √ | ' ' | 填充方向,枚举: 0 :行 1 :列 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fautoindent | 自动缩进 | bpchar | 1 |  | √ | '0' | 自动缩进 |

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

## 业务类型-多选基础资料表 t_xkbm_rptbusinesstypes

- **表名称：** 业务类型-多选基础资料表
- **表名：** t_xkbm_rptbusinesstypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
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

## 维度映射方案-多选基础资料表 t_xkbm_rptscheme_dimmapac

- **表名称：** 维度映射方案-多选基础资料表
- **表名：** t_xkbm_rptscheme_dimmapac

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [预算维度映射 xkbm_dimmapping](../xkbm_files/xkbm_dimmapping.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_rptscheme_dimmapac |  | fdetailid |
| 2 | pk_xkbm_rptscheme_dimmapac |  | fpkid |

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

## 项目数据类型预算数区域-多语言表 t_xkbm_datatypeentry_l

- **表名称：** 项目数据类型预算数区域-多语言表
- **表名：** t_xkbm_datatypeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fitemdatatypealiasname | 预算表显示名称 | varchar | 255 |  | √ | ' ' | 预算表显示名称 |
| 2 | fsjdatatypealiasname | 实际数表显示名称 | varchar | 255 |  | √ | ' ' | 实际数表显示名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_datatypeentry_l |  | fpkid |

---

## 预算模板样式方案-主表 t_xkbm_rptscheme

- **表名称：** 预算模板样式方案-主表
- **表名：** t_xkbm_rptscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fismulorg | 多组织预算表 | bpchar | 1 |  | √ | '0' | 多组织预算表 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [模板样式方案分组 xkbm_rptschemegroup](../xkbm_files/xkbm_rptschemegroup.md) |
| 4 | fisshowgrandtotal | 显示总计 | bpchar | 1 |  | √ | '1' | 显示总计 |
| 5 | fdimensioninfo | 维度组合 | varchar | 2000 |  | √ | ' ' | 维度组合 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbudgetcalendar | 预算日历 | int8 | 64 |  | √ | 0 | [预算日历 xkbm_budgetcalendar](../xkbm_files/xkbm_budgetcalendar.md) |
| 9 | fversiongroupid | 版本分组id | int8 | 64 |  | √ | 0 | 版本分组id |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsplitshowname | 显示属性和维度分开显示 | bpchar | 1 |  | √ | '0' | 显示属性和维度分开显示 |
| 13 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 17 | fxkbmbusinessservice | 所属应用 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 18 | fname | 名称 | varchar | 570 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fshownameposition | 显示属性在维度前 | bpchar | 1 |  | √ | '0' | 显示属性在维度前 |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | fmaindiminfo | fmaindiminfo | varchar | 1000 |  | √ | ' ' |  |
| 24 | fincludeauxpty | 考虑物料的辅助属性 | bpchar | 1 |  | √ | '0' | 考虑物料的辅助属性 |
| 25 | fcycles | 报表包含周期 | varchar | 30 |  | √ | ' ' | 报表包含周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 26 | fislastedversion | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 27 | feffectmrpcal | MRP运算项 | varchar | 10 |  | √ | ' ' | MRP运算项,枚举: 0 :MRP输入项 1 :MRP输出项 |
| 28 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fcycle | 报表周期 | varchar | 30 |  | √ | ' ' | 报表周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 30 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 31 | frpttype | 报表类型 | varchar | 30 |  | √ | ' ' | 报表类型,枚举: 60 :预算报表 |
| 32 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |

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

## 预算模板样式方案-多语言表 t_xkbm_rptscheme_l

- **表名称：** 预算模板样式方案-多语言表
- **表名：** t_xkbm_rptscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 570 |  | √ | ' ' | 名称 |
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

## 项目数据类型辅助编制区域-多语言表 t_xkbm_datatypeentryact_l

- **表名称：** 项目数据类型辅助编制区域-多语言表
- **表名：** t_xkbm_datatypeentryact_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fitemdataactualaliasname | 预算表显示名称 | varchar | 255 |  | √ | ' ' | 预算表显示名称 |
| 5 | fsjdataactualaliasname | 实际数表显示名称 | varchar | 255 |  | √ | ' ' | 实际数表显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_datatypeentryact_l |  | fpkid |

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

## 项目数据类型辅助编制区域-子表 t_xkbm_datatypeentryact

- **表名称：** 项目数据类型辅助编制区域-子表
- **表名：** t_xkbm_datatypeentryact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetdataformulaact | 预算表取数公式 | varchar | 2000 |  | √ | ' ' | 预算表取数公式 |
| 3 | factualfilltype | 显示在预算数 | varchar | 30 |  | √ | ' ' | 显示在预算数,枚举: 0 :之前 1 :之后 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fitemdatatypeactual | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |
| 6 | fitemdataactualaliasname | 预算表显示名称 | varchar | 255 |  | √ | ' ' | 预算表显示名称 |
| 7 | fsjdataformulaact | 实际数表取数公式 | varchar | 2000 |  | √ | ' ' | 实际数表取数公式 |
| 8 | fmultisjformulaact | 实际数多场景模式 | bpchar | 1 |  | √ | '0' | 实际数多场景模式 |
| 9 | fislockact | 锁定 | bpchar | 1 |  | √ | '0' | 锁定 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fbusinesstypeactual | 业务类型 | int8 | 64 |  | √ | 0 | [预算业务类型 xkbm_businesstype](../xkbm_files/xkbm_businesstype.md) |
| 12 | fmultibudgetformulaact | 预算数多场景模式 | bpchar | 1 |  | √ | '0' | 预算数多场景模式 |
| 13 | fsjdataactualaliasname | 实际数表显示名称 | varchar | 255 |  | √ | ' ' | 实际数表显示名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_datatypeentryact |  | fid |
| 2 | pk_xkbm_datatypeentryact |  | fentryid |

---

## 主维度多选基础资料-多选基础资料表 t_xkbm_rptscheme_maindim

- **表名称：** 主维度多选基础资料-多选基础资料表
- **表名：** t_xkbm_rptscheme_maindim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 xkrpt_dimension](../xkrpt_files/xkrpt_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_rptscheme_maindim |  | fpkid |
| 2 | idx_t_xkbm_rptsm_dim_id |  | fid,fbasedataid |
