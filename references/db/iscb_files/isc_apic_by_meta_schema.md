# 集成对象转API-isc_apic_by_meta_schema

## 集成对象转API-主表 t_iscb_apic_by_meta_data

- **表名称：** 集成对象转API-主表
- **表名：** t_iscb_apic_by_meta_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 3 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 4 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 5 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | '0' | 记录API调用日志 |
| 6 | fignore_error | 失败时继续 | bpchar | 1 |  | √ | '0' | 失败时继续 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fauth_required | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 10 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '0' | 不发布到开放平台 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fschema_category | 分类 | int8 | 64 |  | √ | 0 | [自定义分类 isc_schema_category](../iscb_files/isc_schema_category.md) |
| 16 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 17 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 18 | foperation | 操作类型 | varchar | 100 |  | √ | ' ' | 操作类型,枚举: |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcheck_param_type | 校验参数格式 | bpchar | 1 |  | √ | '0' | 校验参数格式 |
| 21 | fpub_status | fpub_status | varchar | 30 |  | √ | ' ' |  |
| 22 | fmetadata | 集成对象 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fmax_count | 行数限制 | int8 | 64 |  | √ | 1000 | 行数限制 |
| 25 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 26 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 27 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 28 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 29 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 31 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 32 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_apic_by_meta_data_pkey |  | fid |
| 2 | t_iscb_apic_by_master |  | fmasterid |
| 3 | t_iscb_apic_by_cg |  | fschema_category |
| 4 | t_iscb_apic_by_number |  | fnumber |

---

## 输入参数-子表 t_iscb_apic_by_meta_in

- **表名称：** 输入参数-子表
- **表名：** t_iscb_apic_by_meta_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finput_data_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 3 | finput_description | 字段描述 | varchar | 510 |  | √ | ' ' | 字段描述 |
| 4 | finput_field | 字段名 | varchar | 300 |  | √ | ' ' | 字段名 |
| 5 | fis_judge_key | 候选键 | bpchar | 1 |  | √ | ' ' | 候选键 |
| 6 | fis_required | 必填 | bpchar | 1 |  | √ | ' ' | 必填 |
| 7 | fis_primary_key | 主键 | bpchar | 1 |  | √ | ' ' | 主键 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_by_meta_in_fk |  | fid |
| 2 | t_iscb_apic_by_meta_in_pkey |  | fentryid |

---

## 条件字段-子表 t_iscb_apic_by_meta_ft

- **表名称：** 条件字段-子表
- **表名：** t_iscb_apic_by_meta_ft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilter_column | 条件字段 | varchar | 50 |  | √ | ' ' | 条件字段 |
| 3 | ffilter_compare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 4 | ffilter_right_bracket | 右括号 | varchar | 30 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |
| 5 | ffilter_label | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 6 | ffilter_link | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffilter_left_bracket | 左括号 | varchar | 30 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |
| 10 | ffilter_value | 比较变量 | varchar | 30 |  | √ | ' ' | 比较变量,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_by_meta_ft_i |  | fid |
| 2 | t_iscb_apic_by_meta_ft_pkey |  | fentryid |

---

## 结果字段-子表 t_iscb_apic_by_meta_out

- **表名称：** 结果字段-子表
- **表名：** t_iscb_apic_by_meta_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutput_field | 字段名 | varchar | 300 |  | √ | ' ' | 字段名 |
| 3 | foutput_data_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | foutput_description | 字段描述 | varchar | 510 |  | √ | ' ' | 字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_apic_by_meta_out_pkey |  | fentryid |
| 2 | idx_iscb_apic_by_meta_out_fk |  | fid |

---

## 集成对象转API-多语言表 t_iscb_apic_by_meta_data_l

- **表名称：** 集成对象转API-多语言表
- **表名：** t_iscb_apic_by_meta_data_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_by_schema_l |  | fid,flocaleid |
| 2 | t_iscb_apic_by_meta_data_l_pkey |  | fpkid |
