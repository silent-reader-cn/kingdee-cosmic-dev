# 抽取方案-tlmgt_extract_scheme

## 自定义抽取语言-多选基础资料表 t_tlmgt_custom_lang

- **表名称：** 自定义抽取语言-多选基础资料表
- **表名：** t_tlmgt_custom_lang

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_custom_lang |  | fpkid |
| 2 | idx_t_tlmgt_cus_lang |  | fid |

---

## 抽取方案-主表 t_tlmgt_extr_scheme

- **表名称：** 抽取方案-主表
- **表名：** t_tlmgt_extr_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fextractlang | 抽取语言 | varchar | 64 |  | √ | ' ' | 抽取语言,枚举: default :启用语言 custom :自定义语言 |
| 7 | fstatus | 数据状态 | varchar | 64 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 使用状态 | varchar | 32 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 32 |  | √ | ' ' | 编码 |
| 12 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fisdefault | 是否默认 | bpchar | 1 |  | √ | ' ' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_ex_scheme |  | fnumber |
| 2 | pk_t_tlmgt_extr_scheme |  | fid |

---

## 资源范围-子表 t_tlmgt_resource_scope

- **表名称：** 资源范围-子表
- **表名：** t_tlmgt_resource_scope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fwordcontenttype | 词条数据类型 | varchar | 64 |  | √ | ' ' | 词条数据类型 |
| 2 | fscopeenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdomainidentifier | 领域标识 | varchar | 64 |  | √ | ' ' | 领域标识 |
| 5 | fresourceidentifier | 资源标识 | varchar | 64 |  | √ | ' ' | 资源标识 |
| 6 | fwordtype | 词条类型 | varchar | 64 |  | √ | ' ' | 词条类型 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fmoduleidentifier | 模块标识 | varchar | 64 |  | √ | ' ' | 模块标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tlmgt_resource_scope |  | fdetailid |
| 2 | idx_t_tlmgt_resource_sco |  | fentryid |

---

## 抽取方案-多语言表 t_tlmgt_extr_scheme_l

- **表名称：** 抽取方案-多语言表
- **表名：** t_tlmgt_extr_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 64 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_extr_sch_l |  | fid |
| 2 | pk_t_tlmgt_extr_scheme_l |  | fpkid |

---

## 抽取方案资源-子表 t_tlmgt_scheme_resource

- **表名称：** 抽取方案资源-子表
- **表名：** t_tlmgt_scheme_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresourcetype | 资源类型 | int8 | 64 |  | √ | 0 | [资源类型 tlmgt_resource_type](../tlmgt_files/tlmgt_resource_type.md) |
| 3 | fresourceenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tlmgt_scheme_res |  | fid |
| 2 | pk_t_tlmgt_scheme_resource |  | fentryid |
