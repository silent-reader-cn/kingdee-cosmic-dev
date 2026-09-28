# 校验规则-pa_verificationrule

## 单据体-子表 t_pa_ruleconditionentity

- **表名称：** 单据体-子表
- **表名：** t_pa_ruleconditionentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterstring_tag | 数据过滤条件_详情 | text | 0 |  |  | null | 数据过滤条件_详情 |
| 3 | fconditionsetting | 条件设置 | varchar | 500 |  | √ | ' ' | 条件设置 |
| 4 | fexpression | 表达式 | varchar | 500 |  | √ | ' ' | 表达式 |
| 5 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | ffilterstring | 数据过滤条件 | varchar | 255 |  | √ | ' ' | 数据过滤条件 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freturnresult | 不通过提示 | varchar | 200 |  | √ | ' ' | 不通过提示 |
| 9 | fconditionresult | 条件成立时 | bpchar | 1 |  | √ | ' ' | 条件成立时,枚举: A :通过 B :不通过 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_condition_fid |  | fid |
| 2 | pk_t_pa_ruleconditionentity |  | fentryid |

---

## 校验规则-使用范围表 t_pa_verificationrules_u

- **表名称：** 校验规则-使用范围表
- **表名：** t_pa_verificationrules_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pa_verificationrules_u_uo |  | fuseorgid |
| 2 | pk_t_pa_verificationrules_u |  | fdataid,fuseorgid |

---

## 校验规则-使用范围位图表 t_pa_verificationrules_m

- **表名称：** 校验规则-使用范围位图表
- **表名：** t_pa_verificationrules_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_verificationrules_m |  | forgid |

---

## 校验规则-多语言表 t_pa_verificationrules_l

- **表名称：** 校验规则-多语言表
- **表名：** t_pa_verificationrules_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_derivation_rule_l |  | fid,flocaleid |
| 2 | pk_t_pa_verificationrules_l |  | fpkid |

---

## 校验规则-主表 t_pa_verificationrules

- **表名称：** 校验规则-主表
- **表名：** t_pa_verificationrules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fanasystemsetting | 分析体系 | int8 | 64 |  | √ | 0 | [分析体系 pa_anasystemsetting](../pa_files/pa_anasystemsetting.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcontrolmode | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: A :强校验 B :弱校验 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbusinessorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fverificationlink | 校验环节 | bpchar | 1 |  | √ | ' ' | 校验环节,枚举: A :取数 B :调整 C :推导 D :分摊 E :聚合 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fanalysis_model | 分析模型 | int8 | 64 |  | √ | 0 | [分析模型 pa_analysismodel](../pa_files/pa_analysismodel.md) |
| 20 | fverificationtype | 校验类型 | bpchar | 1 |  | √ | ' ' | 校验类型,枚举: A :合规性校验 B :勾稽校验 |
| 21 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pa_verificationrules_master |  | fmasterid |
| 2 | idx_pa_verification_rule_1 |  | fnumber |
| 3 | idx_pa_verification_rule_2 |  | fanasystemsetting,fanalysis_model |
| 4 | pk_t_pa_verificationrules |  | fid |
| 5 | idx_t_pa_verificationrules_createorg |  | fcreateorgid |
