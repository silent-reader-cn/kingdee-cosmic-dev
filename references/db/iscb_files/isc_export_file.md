# 数据导出方案-isc_export_file

## 查询条件-子表 t_iscb_export_file_filter

- **表名称：** 查询条件-子表
- **表名：** t_iscb_export_file_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleft_bracket | 左括号 | varchar | 50 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |
| 3 | ffilter_column | 条件字段 | varchar | 150 |  | √ | ' ' | 条件字段 |
| 4 | fcompare | 比较方式 | varchar | 50 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 5 | flink | 逻辑连接符 | varchar | 50 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 6 | ffilter_label | 字段描述 | varchar | 200 |  | √ | ' ' | 字段描述 |
| 7 | fvalue_var | 比较值变量 | varchar | 50 |  | √ | ' ' | 比较值变量,枚举: |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fvalue_fixed | 固定比较值 | varchar | 225 |  | √ | ' ' | 固定比较值 |
| 11 | fright_bracket | 右括号 | varchar | 50 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_export_file_filter_fk |  | fid |
| 2 | pk_t_iscb_export_file_filter |  | fentryid |

---

## 参数分录-子表 t_iscb_export_file_param

- **表名称：** 参数分录-子表
- **表名：** t_iscb_export_file_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdata_type | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 4 | fparams_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparams_label | 标题 | varchar | 100 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_export_file_param_fk |  | fid |
| 2 | pk_t_iscb_export_file_param |  | fentryid |

---

## 排序设置-子表 t_iscb_export_file_order

- **表名称：** 排序设置-子表
- **表名：** t_iscb_export_file_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsort_field | 源表排序字段 | varchar | 50 |  | √ | ' ' | 源表排序字段 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsort_field_label | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcombofield | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: ASC :顺序 DESC :逆序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_export_file_order_fk |  | fid |
| 2 | pk_t_iscb_export_file_order |  | fentryid |

---

## 导出字段-子表 t_iscb_export_file_field

- **表名称：** 导出字段-子表
- **表名：** t_iscb_export_file_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finput_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |
| 3 | finput_field | 字段名 | varchar | 150 |  | √ | ' ' | 字段名 |
| 4 | finput_description | 字段描述 | varchar | 250 |  | √ | ' ' | 字段描述 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | falias | 别名 | varchar | 150 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_export_file_field |  | fentryid |
| 2 | idx_isc_export_file_field_fk |  | fid |

---

## 数据导出方案-主表 t_iscb_export_file

- **表名称：** 数据导出方案-主表
- **表名：** t_iscb_export_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 4 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 5 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: json :Json 对象格式(*.json) xlsx :Excel 工作簿(*.xlsx) xls :Excel 97-2003 工作簿(*.xls) csv :CSV 文件(*.csv) |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 9 | fexport_source_type | 导出对象类别 | varchar | 50 |  | √ | ' ' | 导出对象类别,枚举: isc_metadata_schema :集成对象 |
| 10 | fsrc_retrieve_script | 导出数据获取脚本 | varchar | 255 |  | √ | ' ' | 导出数据获取脚本 |
| 11 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :启用 1 :禁用 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fdelimiter | 自定义分隔符 | varchar | 30 |  | √ | ' ' | 自定义分隔符,枚举: COMMA :逗号（,） SEMICOLON :分号（;） VERTICAL :竖线（\|） TAB :制表符（\t） SPACE :空格（ ） |
| 16 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ffilesize | 文件大小（M） | int4 | 32 |  | √ | 0 | 文件大小（M） |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | fsrc_retrieve_script_tag | 导出数据获取脚本_详情 | text | 0 |  |  | null | 导出数据获取脚本_详情 |
| 20 | fexport_source | 导出对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_export_file_src |  | fgroupid |
| 2 | pk_t_iscb_export_file |  | fid |
| 3 | idx_export_file_m |  | fmodifydate |
