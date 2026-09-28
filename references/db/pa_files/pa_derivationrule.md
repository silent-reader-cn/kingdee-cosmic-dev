# 推导规则-pa_derivationrule

## 赋值到目标维度-子表 t_pa_derivationmode_mt_t

- **表名称：** 赋值到目标维度-子表
- **表名：** t_pa_derivationmode_mt_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmtmtargetfieldnumber | 映射表字段编码 | varchar | 50 |  | √ | ' ' | 映射表字段编码 |
| 3 | fmttargetfieldnumber | 目标维度字段编码 | varchar | 50 |  | √ | ' ' | 目标维度字段编码 |
| 4 | fmtmdefaulttexte | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 5 | fmtmfieldtypeassistant | 辅助资料类型 | varchar | 50 |  | √ | ' ' | 辅助资料类型 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmttarget | 目标维度 | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |
| 8 | fmtmfieldtypebasedata | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型 |
| 9 | fmtmdefaulttext | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 10 | fmtmtargetfield | 基础资料字段 | varchar | 50 |  | √ | ' ' | 基础资料字段 |
| 11 | fmtmtargetfieldtype | 映射表字段类型 | varchar | 50 |  | √ | ' ' | 映射表字段类型 |
| 12 | fmttargetfield | 目标维度字段 | varchar | 50 |  | √ | ' ' | 目标维度字段 |
| 13 | fmttargetfieldtype | 目标维度字段类型 | varchar | 50 |  | √ | ' ' | 目标维度字段类型 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mt_t_fid |  | fid |
| 2 | pk_t_pa_derivationmode_mt_t |  | fentryid |

---

## 关联条件-子表 t_pa_derivationmode_mt_s

- **表名称：** 关联条件-子表
- **表名：** t_pa_derivationmode_mt_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmtmsourcefield | 基础资料字段 | varchar | 50 |  | √ | ' ' | 基础资料字段 |
| 3 | fmtmsourcefieldnumber | 映射表字段编码 | varchar | 50 |  | √ | ' ' | 映射表字段编码 |
| 4 | fmtmsourcefieldtype | 映射表字段类型 | varchar | 50 |  | √ | ' ' | 映射表字段类型 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmtsourcefieldnumber | 源维度字段编码 | varchar | 50 |  | √ | ' ' | 源维度字段编码 |
| 7 | fmtsourcefield | 源维度字段 | varchar | 50 |  | √ | ' ' | 源维度字段 |
| 8 | fmtsourcefieldtype | 源维度字段类型 | varchar | 50 |  | √ | ' ' | 源维度字段类型 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmtsource | 源维度 | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_derivationmode_mt_s |  | fentryid |
| 2 | idx_pa_derivationmode_mt_s |  | fid |

---

## 推导规则-使用范围位图表 t_pa_derivationrule_m

- **表名称：** 推导规则-使用范围位图表
- **表名：** t_pa_derivationrule_m

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
| 1 | pk_t_pa_derivationrule_m |  | forgid |

---

## 推导规则-多语言表 t_pa_derivationrule_l

- **表名称：** 推导规则-多语言表
- **表名：** t_pa_derivationrule_l

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
| 1 | idx_pa_derivationrule_l |  | fid,flocaleid |
| 2 | pk_t_pa_derivationrule_l |  | fpkid |

---

## 推导规则-使用范围表 t_pa_derivationrule_u

- **表名称：** 推导规则-使用范围表
- **表名：** t_pa_derivationrule_u

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
| 1 | pk_t_pa_derivationrule_u |  | fdataid,fuseorgid |
| 2 | idx_t_pa_derivationrule_u_uo |  | fuseorgid |

---

## 发送方单据体-子表 t_pa_derivationmode_send

- **表名称：** 发送方单据体-子表
- **表名：** t_pa_derivationmode_send

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensiontypeassistant | 辅助资料类型 | varchar | 50 |  | √ | ' ' | 辅助资料类型 |
| 3 | fdimensiontext | 大文本 | varchar | 255 |  | √ | ' ' | 大文本 |
| 4 | fdimensiontypebasedata | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型 |
| 5 | fsenddimension | 维度 | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fdimensiontext_tag | 大文本_详情 | text | 0 |  |  | null | 大文本_详情 |
| 9 | fcombofield | 条件 | varchar | 50 |  | √ | ' ' | 条件,枚举: A :在...中 B :不在...中 C :为空 D :不为空 E :全部 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_send_fid |  | fid |
| 2 | pk_t_pa_derivationmode_send |  | fentryid |

---

## 单据体-子表 t_pa_derivationmode_mr_s

- **表名称：** 单据体-子表
- **表名：** t_pa_derivationmode_mr_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcefield | 维度 | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_derivationmode_mr_s |  | fid |
| 2 | pk_t_pa_derivationmode_mr_s |  | fentryid |

---

## 单据体-子表 t_pa_derivationmode_mr_t

- **表名称：** 单据体-子表
- **表名：** t_pa_derivationmode_mr_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdefaulttext | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 3 | ftargetfield | 维度 | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |
| 4 | ffieldtypeassistant | 辅助资料类型 | varchar | 50 |  | √ | ' ' | 辅助资料类型 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdefaulttexte | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 8 | ffieldtypebasedata | 基础资料类型 | varchar | 50 |  | √ | ' ' | 基础资料类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_derivationmode_mr_t |  | fid |
| 2 | pk_t_pa_derivationmode_mr_t |  | fentryid |

---

## 推导规则-主表 t_pa_derivationrule

- **表名称：** 推导规则-主表
- **表名：** t_pa_derivationrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmappingrelationshipid | 映射关系 | int8 | 64 |  | √ | 0 | [映射关系 pa_mappingrelationship](../pa_files/pa_mappingrelationship.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fanalysissystemid | 分析体系 | int8 | 64 |  | √ | 0 | [分析体系 pa_anasystemsetting](../pa_files/pa_anasystemsetting.md) |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmappingmap | 来源基础资料 | varchar | 30 |  | √ | ' ' | 来源基础资料 |
| 12 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fderivationmode | 维度赋值来源 | bpchar | 1 |  | √ | 'A' | 维度赋值来源,枚举: A :通过基础资料取值 B :通过映射关系取值 |
| 17 | fanalysismodelid | 分析模型 | int8 | 64 |  | √ | 0 | [分析模型 pa_analysismodel](../pa_files/pa_analysismodel.md) |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fmappingmaptype | 映射表类型 | varchar | 30 |  | √ | ' ' | 映射表类型 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_derivationrule |  | fid |
| 2 | idx_t_pa_derivationrule_master |  | fmasterid |
| 3 | idx_pa_derivation_rule |  | fanalysismodelid |
| 4 | idx_t_pa_derivationrule_createorg |  | fcreateorgid |
