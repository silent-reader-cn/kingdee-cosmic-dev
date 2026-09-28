# 数据集成方案-isc_data_copy

## 过滤条件-子表 t_iscb_data_copy_filters

- **表名称：** 过滤条件-子表
- **表名：** t_iscb_data_copy_filters

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 3 | ffilter_value_param | ffilter_value_param | varchar | 30 |  | √ | ' ' |  |
| 4 | ffield | ffield | int8 | 64 |  | √ | 0 |  |
| 5 | fvalue_text | fvalue_text | varchar | 100 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fvalue_expr | fvalue_expr | varchar | 100 |  | √ | ' ' |  |
| 8 | ftest_filter_field | ftest_filter_field | varchar | 30 |  | √ | ' ' |  |
| 9 | fright_bracket | 右括号 | varchar | 30 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |
| 10 | fvalue_fixed | 固定比较值 | varchar | 255 |  | √ | ' ' | 固定比较值 |
| 11 | fleft_bracket | 左括号 | varchar | 30 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |
| 12 | flink | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 13 | ffilter_column | 条件字段 | varchar | 150 |  | √ | ' ' | 条件字段 |
| 14 | ffilter_label | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 15 | fvalue_var | 过滤条件参数 | varchar | 100 |  | √ | ' ' | 过滤条件参数,枚举: |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_data_copy_filters_pkey |  | fentryid |
| 2 | idx_iscb_data_copy_filters_0 |  | fid |

---

## 排序设置-子表 t_iscb_data_copy_sort

- **表名称：** 排序设置-子表
- **表名：** t_iscb_data_copy_sort

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsort_field | 源表排序字段 | varchar | 100 |  | √ | ' ' | 源表排序字段 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsort_field_label | 字段描述 | varchar | 100 |  |  | ' ' | 字段描述 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcombofield | 排序方式 | varchar | 30 |  | √ | ' ' | 排序方式,枚举: ASC :顺序 DESC :逆序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_data_copy_sort_pkey |  | fentryid |
| 2 | idx_iscb_data_copy_sort_0 |  | fid |

---

## 参数-子表 t_iscb_data_copy_params

- **表名称：** 参数-子表
- **表名：** t_iscb_data_copy_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flabel | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 5 | fdata_type | 参数类型 | varchar | 30 |  | √ | ' ' | 参数类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fis_customized | 是否自定义 | bpchar | 1 |  | √ | '1' | 是否自定义 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_data_copy_params_0 |  | fid |
| 2 | t_iscb_data_copy_params_pkey |  | fentryid |

---

## 关系映射-子表 t_iscb_data_copy_rm

- **表名称：** 关系映射-子表
- **表名：** t_iscb_data_copy_rm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelation_type | 关系类型 | varchar | 30 |  | √ | ' ' | 关系类型,枚举: entry_table :分录表 ref_table :外键表 |
| 3 | fmaster_field | 引用数据表关联字段 | varchar | 100 |  | √ | ' ' | 引用数据表关联字段 |
| 4 | fmaster_ref_field | 主数据表关联字段 | varchar | 50 |  | √ | ' ' | 主数据表关联字段 |
| 5 | fentry_order_by | 分录表排序字段 | varchar | 150 |  | √ | ' ' | 分录表排序字段 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftable_alias | ftable_alias | varchar | 20 |  | √ | ' ' |  |
| 8 | ftable_data_source | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 9 | fdata_table | 引用数据表 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 10 | ftable_primary_key | ftable_primary_key | varchar | 100 |  | √ | ' ' |  |
| 11 | frelation_alias | 关系别名 | varchar | 50 |  | √ | ' ' | 关系别名 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fmaster_table | 主数据表 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_data_copy_rm_pkey |  | fentryid |
| 2 | idx_iscb_data_copy_rm_0 |  | fid |

---

## 目标单操作分录-子表 t_isc_data_copy_tar_act

- **表名称：** 目标单操作分录-子表
- **表名：** t_isc_data_copy_tar_act

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftar_act_params_desc | 操作参数描述 | varchar | 255 |  | √ | ' ' | 操作参数描述 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftar_action_label | 操作名称 | varchar | 150 |  | √ | ' ' | 操作名称,枚举: |
| 5 | ftar_action_type | 操作类型 | varchar | 20 |  | √ | ' ' | 操作类型,枚举: save :新增+修改 delete :删除 insert :新增 update :修改 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftar_action_number | 操作编码 | varchar | 150 |  | √ | ' ' | 操作编码 |
| 8 | ftar_action_params | 操作参数 | varchar | 500 |  | √ | ' ' | 操作参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_data_copy_tar_act_pkey |  | fentryid |
| 2 | idx_isc_dctact_fid |  | fid |

---

## 字段映射-子表 t_iscb_data_copy_mapping

- **表名称：** 字段映射-子表
- **表名：** t_iscb_data_copy_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue_conver_rule | 值转换规则 | int8 | 64 |  | √ | 0 | [值转换规则 isc_value_conver_rule](../iscb_files/isc_value_conver_rule.md) |
| 3 | fprivacy_num | 数据标签 | varchar | 255 |  | √ | ' ' | 数据标签 |
| 4 | faggr_fn | 聚合运算 | varchar | 300 |  | √ | ' ' | 聚合运算 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ffixed_value | 直接赋值 | varchar | 255 |  | √ | ' ' | 直接赋值 |
| 7 | ftar_desc | 目标字段描述 | varchar | 510 |  | √ | ' ' | 目标字段描述 |
| 8 | fmapping_src_column | 源对象字段 | varchar | 100 |  | √ | ' ' | 源对象字段 |
| 9 | fmapping_tar_column | 目标对象字段 | varchar | 100 |  | √ | ' ' | 目标对象字段 |
| 10 | fdisable_key | 是否禁用 | bpchar | 1 |  | √ | ' ' | 是否禁用 |
| 11 | fsrc_desc | 源字段描述 | varchar | 100 |  | √ | ' ' | 源字段描述 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcandidate_key | 是否候选键 | bpchar | 1 |  | √ | ' ' | 是否候选键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_data_copy_mapping_0 |  | fid |
| 2 | t_iscb_data_copy_mapping_pkey |  | fentryid |

---

## 数据集成方案-多语言表 t_iscb_data_copy_l

- **表名称：** 数据集成方案-多语言表
- **表名：** t_iscb_data_copy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_data_copy_l_0 |  | fid,flocaleid |
| 2 | t_iscb_data_copy_l_pkey |  | fpkid |

---

## 数据集成方案-主表 t_iscb_data_copy

- **表名称：** 数据集成方案-主表
- **表名：** t_iscb_data_copy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuse_src_att_create_time | 使用源附件创建时间 | bpchar | 1 |  | √ | '0' | 使用源附件创建时间 |
| 3 | froot_node_creteria | 目标对象的根节点判断标准 | varchar | 200 |  | √ | ' ' | 目标对象的根节点判断标准 |
| 4 | ftarget_handler | 目标数据处理类 | varchar | 150 |  | √ | ' ' | 目标数据处理类 |
| 5 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 6 | fsource_schema | 源对象 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fparent_field | 目标对象的上级对象字段 | varchar | 50 |  | √ | ' ' | 目标对象的上级对象字段 |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fradiogroupfield | 单选按钮组1 | varchar | 30 |  | √ | ' ' | 单选按钮组1,枚举: |
| 12 | fsrc_retrieve_script | 来源数据查询脚本 | varchar | 510 |  | √ | ' ' | 来源数据查询脚本 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | frecord_oid_mappings | 记录源单/目标单ID关联关系 | bpchar | 1 |  | √ | ' ' | 记录源单/目标单ID关联关系 |
| 17 | fdata_target | 目标系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 18 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 19 | fproxy_user | 代理用户 | varchar | 50 |  | √ | ' ' | 代理用户 |
| 20 | fschema_category | 方案分类 | int8 | 64 |  | √ | 0 | [自定义分类 isc_schema_category](../iscb_files/isc_schema_category.md) |
| 21 | fmode | 模式 | varchar | 30 |  | √ | ' ' | 模式,枚举: RequiresTransaction :单个事务 BreakOnError :错误时中止 ResumeOnError :错误时忽略 |
| 22 | ftarget_script_tag | 目标数据处理脚本_详情 | text | 0 |  |  | null | 目标数据处理脚本_详情 |
| 23 | ftarget_script | 目标数据处理脚本 | varchar | 510 |  | √ | ' ' | 目标数据处理脚本 |
| 24 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | freader_script | 来源数据处理脚本 | varchar | 510 |  | √ | ' ' | 来源数据处理脚本 |
| 27 | fwrite_back_rule | 回写值转换规则 | int8 | 64 |  | √ | 0 | [值转换规则 isc_value_conver_rule](../iscb_files/isc_value_conver_rule.md) |
| 28 | ftarget_schema | 目标对象 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 29 | fsupports_file_copy | 附件同步 | bpchar | 1 |  | √ | '0' | 附件同步 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | freader_script_tag | 来源数据处理脚本_详情 | text | 0 |  |  | null | 来源数据处理脚本_详情 |
| 32 | frecord_oid_log | 记录单据集成日志 | bpchar | 1 |  | √ | '0' | 记录单据集成日志 |
| 33 | fdata_source | 源系统 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 34 | fcontains_dynamic_filter | 过滤条件参数值包含变量 | bpchar | 1 |  | √ | '0' | 过滤条件参数值包含变量 |
| 35 | fdefault_root_parent | 目标对象的根节点的上级对象ID | varchar | 50 |  | √ | ' ' | 目标对象的根节点的上级对象ID |
| 36 | fenable | 启用 | varchar | 30 |  | √ | ' ' | 启用,枚举: 0 :禁用 1 :可用 |
| 37 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 38 | fsrc_retrieve_script_tag | 来源数据查询脚本_详情 | text | 0 |  |  | null | 来源数据查询脚本_详情 |
| 39 | fmapping_script_tag | 转换脚本_详情 | text | 0 |  |  | null | 转换脚本_详情 |
| 40 | fattach_creator_rule | 附件创建人值转换规则 | int8 | 64 |  | √ | 0 | [值转换规则 isc_value_conver_rule](../iscb_files/isc_value_conver_rule.md) |
| 41 | fmapping_script | 转换脚本 | varchar | 510 |  | √ | ' ' | 转换脚本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_data_copy_tar |  | fdata_target |
| 2 | idx_iscb_data_copy_src |  | fdata_source |
| 3 | t_iscb_data_copy_pkey |  | fid |

---

## 函数分录-子表 t_iscb_data_copy_fn

- **表名称：** 函数分录-子表
- **表名：** t_iscb_data_copy_fn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 资源类别 | varchar | 100 |  | √ | 'isc_custom_function' | 资源类别,枚举: isc_custom_function :自定义函数 isc_apic_for_external_api :外部系统API isc_apic_webapi :WebAPI登记 |
| 3 | ffunction_number | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 4 | ffunction_description | ffunction_description | varchar | 200 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffunction | 引用资源 | int8 | 64 |  | √ | 0 | 自定义函数 isc_custom_function |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dc_fn_fk |  | fid |
| 2 | t_iscb_data_copy_fn_pkey |  | fentryid |
