# 预算汇总表样式方案-xkbm_sumrptscheme

## 辅助编制区域-子表 t_xkbm_sumdatatypeact

- **表名称：** 辅助编制区域-子表
- **表名：** t_xkbm_sumdatatypeact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetdataformulaact | 预算表取数公式 | varchar | 2000 |  | √ | ' ' | 预算表取数公式 |
| 3 | factualfilltype | 显示在预算数 | varchar | 30 |  | √ | ' ' | 显示在预算数,枚举: 0 :之前 1 :之后 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fitemdatatypeactual | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbusinesstypeactual | 预算业务类型 | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 8 | fmultibudgetformulaact | 预算数多场景模式 | bpchar | 1 |  | √ | '0' | 预算数多场景模式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_sumdatatypeact |  | fentryid |
| 2 | idx_xkbm_sumdatatypeact |  | fid |

---

## 辅助编制区域公式子单据体-子表 t_xkbm_sumdataactformula

- **表名称：** 辅助编制区域公式子单据体-子表
- **表名：** t_xkbm_sumdataactformula

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
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_sumdataactformula |  | fentryid |
| 2 | pk_xkbm_sumdataactformula |  | fdetailid |

---

## 预算数区域公式子单据体-子表 t_xkbm_sumdatatypeformula

- **表名称：** 预算数区域公式子单据体-子表
- **表名：** t_xkbm_sumdatatypeformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fformulatype | 类型 | varchar | 30 |  | √ | '0' | 类型,枚举: 0 :预算数 1 :实际数 |
| 2 | fformula | 公式 | varchar | 2000 |  | √ | ' ' | 公式 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcondition | 条件 | varchar | 2000 |  | √ | ' ' | 条件 |
| 5 | fconditionjson | 条件JSON | varchar | 2000 |  | √ | ' ' | 条件JSON |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fformulacategory | 公式类型 | varchar | 30 |  | √ | '0' | 公式类型,枚举: 0 :函数 1 :常规计算 2 :占比计算 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_sumdatatypeformula |  | fdetailid |
| 2 | idx_xkbm_sumdatatypeformula |  | fentryid |

---

## 维度-多语言表 t_xkbm_sumwizarddimension_l

- **表名称：** 维度-多语言表
- **表名：** t_xkbm_sumwizarddimension_l

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
| 1 | pk_xkbm_sumwizarddimension_l |  | fpkid |
| 2 | idx_xkbm_sumwizarddimension_l |  | fentryid,flocaleid |

---

## 预算汇总表样式方案-主表 t_xkbm_sumrptscheme

- **表名称：** 预算汇总表样式方案-主表
- **表名：** t_xkbm_sumrptscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fismulorg | 多组织预算表 | bpchar | 1 |  | √ | '0' | 多组织预算表 |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 预算汇总表样式方案分组 xkbm_sumrptschemegroup |
| 4 | fisshowgrandtotal | 显示总计 | bpchar | 1 |  | √ | '0' | 显示总计 |
| 5 | fbwbcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fsumreportremark | 显示备注信息 | bpchar | 1 |  | √ | '0' | 显示备注信息 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fsumschemetype | 样式方案类型 | varchar | 30 |  | √ | ' ' | 样式方案类型,枚举: 2 :预算非周期汇总样式方案 3 :预算周期汇总样式方案 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsplitshowname | 显示属性和维度分开显示 | bpchar | 1 |  | √ | '0' | 显示属性和维度分开显示 |
| 13 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | 预算业务服务 xkbm_businessservice |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbudgetorgversion | 组织架构版本 | varchar | 50 |  | √ | ' ' | 组织架构版本,枚举: |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fbudgetorgid | 预算组织架构 | int8 | 64 |  | √ | 0 | 预算组织架构 xkbm_budgetorg |
| 20 | fshownameposition | 显示属性在维度前 | bpchar | 1 |  | √ | '0' | 显示属性在维度前 |
| 21 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 25 | frptschemeid | 模板样式方案 | int8 | 64 |  | √ | 0 | 预算模板样式方案 xkbm_rptscheme |
| 26 | fcurrencyid | 预算币别 | varchar | 100 |  | √ | ' ' | 预算币别,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_sumrptscheme |  | fid |
| 2 | idx_xkbm_sumrptscheme |  | frptschemeid |

---

## 维度-子表 t_xkbm_sumwizarddimension

- **表名称：** 维度-子表
- **表名：** t_xkbm_sumwizarddimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimeffectname | 维度过滤 | varchar | 2000 |  | √ | ' ' | 维度过滤 |
| 3 | fdimensionid | 维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdimeffectkey | 维度过滤条件 | varchar | 2000 |  | √ | ' ' | 维度过滤条件 |
| 6 | ffiltername | 维度范围 | varchar | 2000 |  | √ | ' ' | 维度范围 |
| 7 | fdimensionformid | 维度业务对象ID | varchar | 255 |  | √ | ' ' | 维度业务对象ID |
| 8 | fdimeffectdesc | 过滤条件json | varchar | 2000 |  | √ | ' ' | 过滤条件json |
| 9 | fdimpropnames | 显示属性 | varchar | 300 |  | √ | ' ' | 显示属性 |
| 10 | fisdimensionsum | 汇总 | bpchar | 1 |  | √ | '0' | 汇总 |
| 11 | fmulidimpropnames | 显示属性多语言 | varchar | 2000 |  | √ | ' ' | 显示属性多语言 |
| 12 | fdimpropfields | 属性对应字段 | varchar | 300 |  | √ | ' ' | 属性对应字段 |
| 13 | fisshowtotals | 显示小计 | bpchar | 1 |  | √ | '0' | 显示小计 |
| 14 | ffilterkey | 维度范围条件 | varchar | 2000 |  | √ | ' ' | 维度范围条件 |
| 15 | fdimensionposition | 维度类型 | varchar | 30 |  | √ | ' ' | 维度类型,枚举: 0 :行 1 :列 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fautoindent | 自动缩进 | bpchar | 1 |  | √ | '0' | 自动缩进 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_sumwizarddimension |  | fentryid |
| 2 | idx_xkbm_sumwizarddimension |  | fid |

---

## 预算汇总表样式方案-多语言表 t_xkbm_sumrptscheme_l

- **表名称：** 预算汇总表样式方案-多语言表
- **表名：** t_xkbm_sumrptscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_sumrptscheme_l |  | fpkid |
| 2 | idx_xkbm_sumrptscheme_l |  | fid,flocaleid |

---

## 预算数区域-子表 t_xkbm_sumdatatypeentry

- **表名称：** 预算数区域-子表
- **表名：** t_xkbm_sumdatatypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetdataformula | 预算表取数公式 | varchar | 2000 |  | √ | ' ' | 预算表取数公式 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbusinesstype | 预算业务类型 | int8 | 64 |  | √ | 0 | 预算业务类型 xkbm_businesstype |
| 5 | fmultibudgetformula | 预算数多场景模式 | bpchar | 1 |  | √ | '0' | 预算数多场景模式 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbm_rptitemdatatype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_sumdatatypeentry |  | fentryid |
| 2 | idx_xkbm_sumdatatypeentry |  | fid |
