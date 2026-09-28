# 模板样式方案-xkrpt_wizardscheme

## 报告维度单据体-子表 t_xkrpt_wizarddimension

- **表名称：** 报告维度单据体-子表
- **表名：** t_xkrpt_wizarddimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimpropnames | 显示属性 | varchar | 255 |  | √ | ' ' | 显示属性 |
| 3 | fdimensionid | 报告维度 | int8 | 64 |  | √ | 0 | 维度 xkrpt_dimension |
| 4 | fdimasstacttype | 对应核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 5 | fdimpropfields | 显示属性对应字段 | varchar | 255 |  | √ | ' ' | 显示属性对应字段 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_wizarddimension |  | fentryid |
| 2 | idx_xkrpt_wizarddimension |  | fid |

---

## 取数设置单据体-多语言表 t_xkrpt_wizardformula_l

- **表名称：** 取数设置单据体-多语言表
- **表名：** t_xkrpt_wizardformula_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccessformulashowname | 显示名称 | varchar | 2000 |  | √ | ' ' | 显示名称 |
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
| 1 | pk_t_xkrpt_wizardformula_l |  | fpkid |
| 2 | idx_xkrpt_wizardformula_l |  | fentryid,flocaleid |

---

## 报表项目单据体-子表 t_xkrpt_wizarditem

- **表名称：** 报表项目单据体-子表
- **表名：** t_xkrpt_wizarditem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewline | 另起一行/列 | bpchar | 1 |  | √ | '0' | 另起一行/列 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fitemindent | 缩进 | int8 | 64 |  | √ | 0 | 缩进 |
| 6 | fitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_wizarditem |  | fentryid |
| 2 | idx_xkrpt_wizarditem |  | fid |

---

## 取数设置单据体-子表 t_xkrpt_wizardformula

- **表名称：** 取数设置单据体-子表
- **表名：** t_xkrpt_wizardformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fformulatype | 公式类型 | varchar | 30 |  | √ | ' ' | 公式类型,枚举: 1 :函数 2 :函数+表内 3 :重分类 |
| 3 | faccessitemdatatypeid | 项目数据类型编码 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 4 | faccessformulashowname | 显示名称 | varchar | 510 |  | √ | ' ' | 显示名称 |
| 5 | faccessformulaitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | faccessformula | 取数公式 | varchar | 2000 |  | √ | ' ' | 取数公式 |
| 8 | fadddim | 追加公式维度 | bpchar | 1 |  | √ | '0' | 追加公式维度 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_wizardformula |  | fentryid |
| 2 | idx_xkrpt_wizardformula |  | fid |

---

## 项目数据类型单据体-子表 t_xkrpt_wizarddatatype

- **表名称：** 项目数据类型单据体-子表
- **表名：** t_xkrpt_wizarddatatype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finneritemformula | 取数公式 | varchar | 2000 |  | √ | ' ' | 取数公式 |
| 3 | fitemdatatypeid | 项目数据类型编码 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 4 | faccessstarperiod | 开始期间 | int8 | 64 |  | √ | 0 | 开始期间 |
| 5 | faccessendperiod | 结束期间 | int8 | 64 |  | √ | 0 | 结束期间 |
| 6 | faccesstype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | faccessyear | 会计年度 | int8 | 64 |  | √ | 0 | 会计年度 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdatatypeaccessformula | 取数方式 | varchar | 30 |  | √ | ' ' | 取数方式,枚举: 1 :ACCT 2 :ACCTCASH 3 :公式定义 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_wizarddatatype |  | fid |
| 2 | pk_t_xkrpt_wizarddatatype |  | fentryid |

---

## 特殊取数单据体-子表 t_xkrpt_wizardspformula

- **表名称：** 特殊取数单据体-子表
- **表名：** t_xkrpt_wizardspformula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspecialaccessformula | 取数公式 | varchar | 2000 |  | √ | ' ' | 取数公式 |
| 3 | fspecialitemdatatypeid | 项目数据类型编码 | int8 | 64 |  | √ | 0 | 项目数据类型 xkbd_rptitemdatatype |
| 4 | fspecialitemid | 报表项目编码 | int8 | 64 |  | √ | 0 | 报表项目 xkbd_rptitem |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fspecialformulatype | 公式类型 | varchar | 30 |  | √ | ' ' | 公式类型,枚举: 1 :函数 3 :重分类 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_wizardspformula |  | fentryid |
| 2 | idx_xkrpt_wizardspformula |  | fid |

---

## 模板样式方案-多语言表 t_xkrpt_wizardscheme_l

- **表名称：** 模板样式方案-多语言表
- **表名：** t_xkrpt_wizardscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_wizardscheme_l |  | fid,flocaleid |
| 2 | pk_t_xkrpt_wizardscheme_l |  | fpkid |

---

## 模板样式方案-主表 t_xkrpt_wizardscheme

- **表名称：** 模板样式方案-主表
- **表名：** t_xkrpt_wizardscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsumposition | 合计项位置 | varchar | 30 |  | √ | ' ' | 合计项位置,枚举: 1 :表尾 2 :表头 |
| 3 | ffillby | ffillby | bpchar | 1 |  | √ | '0' |  |
| 4 | fisautoindent | 报告维度自动缩进 | bpchar | 1 |  | √ | '0' | 报告维度自动缩进 |
| 5 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 6 | fitemisautoindent | 报表项目自动缩进 | bpchar | 1 |  | √ | '0' | 报表项目自动缩进 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fversiongroupid | 版本分组ID | int8 | 64 |  | √ | 0 | 版本分组ID |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fissummary | fissummary | bpchar | 1 |  | √ | '0' |  |
| 13 | fsplitattribanddim | 显示属性与维度分开显示 | bpchar | 1 |  | √ | '0' | 显示属性与维度分开显示 |
| 14 | fitemroworcol | 报表项目填充维度 | varchar | 30 |  | √ | ' ' | 报表项目填充维度,枚举: 1 :行维度 2 :列维度 |
| 15 | fdimroworcol | 报告维度填充维度 | varchar | 30 |  | √ | ' ' | 报告维度填充维度,枚举: |
| 16 | fisadjust | fisadjust | bpchar | 1 |  | √ | '0' |  |
| 17 | ftranssourceid | ftranssourceid | int8 | 64 |  | √ | 0 |  |
| 18 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 19 | fissingle | fissingle | bpchar | 1 |  | √ | '0' |  |
| 20 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fdatadirection | fdatadirection | varchar | 30 |  | √ | ' ' |  |
| 22 | fislastedver | 是否最新版本 | bpchar | 1 |  | √ | '0' | 是否最新版本 |
| 23 | fitemdatatyperoworcol | 项目数据类型填充维度 | varchar | 30 |  | √ | ' ' | 项目数据类型填充维度,枚举: 1 :行维度 2 :列维度 |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fitemindentbase | 报表项目自动缩进依据 | varchar | 30 |  | √ | ' ' | 报表项目自动缩进依据,枚举: 1 :编码 2 :资料上下级 |
| 28 | fstyletype | 样式类型 | varchar | 30 |  | √ | ' ' | 样式类型,枚举: 1 :固定样式报表 2 :动态罗列报表 |
| 29 | faccessroworcol | 报表项目填充维度 | varchar | 30 |  | √ | ' ' | 报表项目填充维度,枚举: 1 :行维度 2 :列维度 |
| 30 | fdescription | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 31 | fneedautofill | 填充Item公式 | bpchar | 1 |  | √ | '0' | 填充Item公式 |
| 32 | fisfirstcolumn | fisfirstcolumn | bpchar | 1 |  | √ | '0' |  |
| 33 | fdimitemindentbase | 报告维度缩进依据 | varchar | 30 |  | √ | ' ' | 报告维度缩进依据,枚举: 1 :编码 2 :资料上下级 |
| 34 | fisconsolidate | fisconsolidate | bpchar | 1 |  | √ | '0' |  |
| 35 | fattribbeforedim | 显示属性在维度前 | bpchar | 1 |  | √ | '0' | 显示属性在维度前 |
| 36 | felimtype | felimtype | int8 | 64 |  | √ | 0 |  |
| 37 | fiselimination | fiselimination | bpchar | 1 |  | √ | '0' |  |
| 38 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | fmetareporttype | 主表类型 | varchar | 30 |  | √ | ' ' | 主表类型,枚举: 1 :资产负债表 2 :利润表 3 :现金流量表 |
| 40 | fincludesum | 合计项 | bpchar | 1 |  | √ | '0' | 合计项 |
| 41 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 42 | frpttype | 报表类型 | varchar | 30 |  | √ | ' ' | 报表类型,枚举: 3 :报表 10 :个别报表 11 :合并报表 |
| 43 | fversionnum | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 44 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_wizardscheme |  | fid |
| 2 | idx_xkrpt_wizardscheme |  | fversiongroupid |
