# RESTful API（基础模型）-open_rest_api

## 过滤条件分录-子表 t_open_rest_filter_entry

- **表名称：** 过滤条件分录-子表
- **表名：** t_open_rest_filter_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilter_column | 条件字段 | varchar | 250 |  | √ | ' ' | 条件字段 |
| 3 | ffilter_compare | 比较方式 | varchar | 50 |  | √ | ' ' | 比较方式,枚举: = :等于 <> :不等于 in :在……中 not in :不在……中 IS_NULL :为空 IS_NOT_NULL :不为空 CONTAINS :包含 NOT_CONTAINS :不包含 > :大于 < :小于 >= :大于或等于 <= :小于或等于 STARTS_WITH :开头是 ENDS_WITH :结尾是 NOT_STARTS_WITH :开头不是 NOT_ENDS_WITH :结尾不是 |
| 4 | ffilter_constant | 比较常量 | varchar | 255 |  | √ | ' ' | 比较常量 |
| 5 | ffilter_right_bracket | 右括号 | varchar | 50 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) ))) :))) |
| 6 | ffilter_label | 字段描述 | varchar | 250 |  | √ | ' ' | 字段描述 |
| 7 | ffilter_link | 逻辑连接符 | varchar | 50 |  | √ | ' ' | 逻辑连接符,枚举: 0 :与 1 :或 |
| 8 | ffilter_var | 比较变量 | varchar | 50 |  | √ | ' ' | 比较变量,枚举: |
| 9 | ffilter_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ffilter_left_bracket | 左括号 | varchar | 50 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( ((( :((( |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_filter_entry |  | fentryid |
| 2 | idx_open_rest_filter_entry_fk |  | fid |

---

## Path参数-子表 t_open_rest_req_paths

- **表名称：** Path参数-子表
- **表名：** t_open_rest_req_paths

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freq_path_ext_tag | 配置详情_详情 | text | 0 |  |  | null | 配置详情_详情 |
| 3 | freq_path_name | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 4 | freq_path_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freq_path_required | 必填 | bpchar | 1 |  | √ | '1' | 必填 |
| 7 | freq_path_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | freq_path_type | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :string long :long integer :integer decimal :decimal boolean :boolean datetime :datetime date :date-only time :time-only |
| 10 | freq_path_ext | 配置详情 | varchar | 255 |  | √ | ' ' | 配置详情 |
| 11 | freq_path_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 12 | freq_path_default | 默认值 | varchar | 1024 |  | √ | ' ' | 默认值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_req_paths_fk |  | fid |
| 2 | pk_t_open_rest_req_paths |  | fentryid |

---

## 请求头-子表 t_open_rest_req_head

- **表名称：** 请求头-子表
- **表名：** t_open_rest_req_head

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freq_head_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 3 | freq_head_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 4 | freq_head_type | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :string long :long integer :integer decimal :decimal boolean :boolean datetime :datetime date :date-only time :time-only |
| 5 | freq_head_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 6 | freq_head_name | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 7 | freq_head_ext | 配置详情 | varchar | 255 |  | √ | ' ' | 配置详情 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freq_head_default | 默认值 | varchar | 1024 |  | √ | ' ' | 默认值 |
| 10 | freq_head_ext_tag | 配置详情_详情 | text | 0 |  |  | null | 配置详情_详情 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | freq_head_required | 必填 | bpchar | 1 |  | √ | '1' | 必填 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_req_head_fk |  | fid |
| 2 | pk_t_open_rest_req_head |  | fentryid |

---

## 请求头-多语言表 t_open_rest_req_head_l

- **表名称：** 请求头-多语言表
- **表名：** t_open_rest_req_head_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freq_head_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
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
| 1 | pk_t_open_rest_req_head_l |  | fpkid |
| 2 | idx_open_rest_req_head_l_0 |  | fentryid,flocaleid |

---

## 请求体-多语言表 t_open_rest_req_body_l

- **表名称：** 请求体-多语言表
- **表名：** t_open_rest_req_body_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | freq_body_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_req_body_l |  | fpkid |
| 2 | idx_open_rest_req_body_l_0 |  | fentryid,flocaleid |

---

## 排序分录-多语言表 t_open_rest_sort_entry_l

- **表名称：** 排序分录-多语言表
- **表名：** t_open_rest_sort_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsort_desc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
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
| 1 | idx_open_rest_sort_entry_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_open_rest_sort_entry_l |  | fpkid |

---

## 请求体-子表 t_open_rest_req_body

- **表名称：** 请求体-子表
- **表名：** t_open_rest_req_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freq_body_type | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :string object :object long :long integer :integer datetime :datetime decimal :decimal boolean :boolean date :date-only time :time-only ml_string :ml_string |
| 3 | freq_body_ext_tag | 配置详情_详情 | text | 0 |  |  | null | 配置详情_详情 |
| 4 | freq_body_root | 是否根节点 | varchar | 50 |  | √ | ' ' | 是否根节点,枚举: 0 :是 1 :否 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freq_body_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 7 | freq_body_name | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 8 | freq_body_full_name | 参数全路径 | varchar | 200 |  | √ | ' ' | 参数全路径 |
| 9 | freq_body_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 10 | freq_body_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 11 | freq_body_ext | 配置详情 | varchar | 255 |  | √ | ' ' | 配置详情 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 13 | freq_body_default | 默认值 | varchar | 1024 |  | √ | ' ' | 默认值 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | freq_body_required | 必填 | bpchar | 1 |  | √ | '1' | 必填 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_req_body_fk |  | fid |
| 2 | pk_t_open_rest_req_body |  | fentryid |

---

## 排序分录-子表 t_open_rest_sort_entry

- **表名称：** 排序分录-子表
- **表名：** t_open_rest_sort_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsort_field | 排序字段 | varchar | 250 |  | √ | ' ' | 排序字段 |
| 3 | fsort_mode | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: asc :顺序 desc :倒序 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsort_desc | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_sort_entry |  | fentryid |
| 2 | idx_open_rest_sort_entry_fk |  | fid |

---

## Query参数-子表 t_open_rest_req_querys

- **表名称：** Query参数-子表
- **表名：** t_open_rest_req_querys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freq_query_ext | 配置详情 | varchar | 255 |  | √ | ' ' | 配置详情 |
| 3 | freq_query_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 4 | freq_query_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 5 | freq_query_name | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freq_query_default | 默认值 | varchar | 1024 |  | √ | ' ' | 默认值 |
| 8 | freq_query_type | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :string long :long integer :integer decimal :decimal boolean :boolean datetime :datetime date :date-only time :time-only |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | freq_query_required | 必填 | bpchar | 1 |  | √ | '1' | 必填 |
| 11 | freq_query_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 12 | freq_query_ext_tag | 配置详情_详情 | text | 0 |  |  | null | 配置详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_req_querys |  | fentryid |
| 2 | idx_open_rest_req_querys_fk |  | fid |

---

## 200响应体-多语言表 t_open_rest_resp_body_l

- **表名称：** 200响应体-多语言表
- **表名：** t_open_rest_resp_body_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fresp_body_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
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
| 1 | idx_open_rest_resp_body_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_open_rest_resp_body_l |  | fpkid |

---

## Path参数-多语言表 t_open_rest_req_paths_l

- **表名称：** Path参数-多语言表
- **表名：** t_open_rest_req_paths_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | freq_path_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_req_paths_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_open_rest_req_paths_l |  | fpkid |

---

## RESTful API（基础模型）-主表 t_open_rest_api

- **表名称：** RESTful API（基础模型）-主表
- **表名：** t_open_rest_api

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 自定义分组 | int8 | 64 |  | √ | 0 | [分组 open_customgroup](../open_files/open_customgroup.md) |
| 3 | fudf_script | 自定义处理脚本 | varchar | 255 |  | √ | ' ' | 自定义处理脚本 |
| 4 | froute_unique_key | 路由唯一标识 | varchar | 512 |  | √ | ' ' | 路由唯一标识 |
| 5 | fmethod | 方法 | varchar | 50 |  | √ | ' ' | 方法,枚举: GET :GET POST :POST PUT :PUT PATCH :PATCH DELETE :DELETE |
| 6 | fresp_digest | 响应参数摘要模板 | varchar | 200 |  | √ | ' ' | 响应参数摘要模板 |
| 7 | foperation_number | 操作 | varchar | 50 |  | √ | ' ' | 操作,枚举: create_one :新增 create_batch :批量新增 create_entry :新增分录 create_batch_entry :批量新增分录 part_update :部分更新 full_update :全量更新 query_one :详情查询 query_list :列表查询 delete_one :删除 submit :提交 unsubmit :撤销 audit :审核 unaudit :反审核 enable :启用 disable :禁用 delete_one_entry :删除分录 delete_batch :批量删除 delete_batch_entry :批量删除分录 part_update_batch :批量部分更新 full_update_batch :批量全量更新 submit_batch :批量提交 unsubmit_batch :批量撤销 audit_batch :批量审核 unaudit_batch :批量反审核 enable_batch :批量启用 disable_batch :批量禁用 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 10 | fresource_path | 资源路径 | varchar | 255 |  | √ | ' ' | 资源路径 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fisdesensitize | 是否脱敏 | bpchar | 1 |  | √ | '0' | 是否脱敏 |
| 15 | fentry_key | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识,枚举: |
| 16 | floglevel | 日志级别 | varchar | 36 |  | √ | ' ' | 日志级别,枚举: default :默认 none :不记录 summary :基本日志（出入参仅记录摘要） detail :详细日志（出入参截取前2000字符） full :完整日志（出入参截取前10000字符） |
| 17 | fversion | 适用版本号 | varchar | 50 |  | √ | ' ' | 适用版本号 |
| 18 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fudf_script_tag | 自定义处理脚本_详情 | text | 0 |  |  | null | 自定义处理脚本_详情 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fdescription | 详细描述 | varchar | 512 |  | √ | ' ' | 详细描述 |
| 25 | freq_digest | 请求参数摘要模板 | varchar | 200 |  | √ | ' ' | 请求参数摘要模板 |
| 26 | ftype | 服务类型 | varchar | 50 |  | √ | ' ' | 服务类型,枚举: udf_script :自定义脚本 entity_action :实体服务 |
| 27 | freq_body_root_type | 请求体根类型 | varchar | 50 |  | √ | ' ' | 请求体根类型,枚举: object :对象（Object） array :数组（Array） |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 30 | foperation_type | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: query :查询 addnew :新增 update :更新 delete :删除 status_change :状态变更 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_api |  | fid |
| 2 | idx_open_rest_api_uk |  | froute_unique_key |
| 3 | idx_open_rest_api_number |  | fnumber |

---

## RESTful API（基础模型）-多语言表 t_open_rest_api_l

- **表名称：** RESTful API（基础模型）-多语言表
- **表名：** t_open_rest_api_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 详细描述 | varchar | 512 |  | √ | ' ' | 详细描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_api_l_0 |  | fid,flocaleid |
| 2 | pk_t_open_rest_api_l |  | fpkid |

---

## 操作参数-多语言表 t_open_rest_op_parameters_l

- **表名称：** 操作参数-多语言表
- **表名：** t_open_rest_op_parameters_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fop_param_desc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_op_params_l_0 |  | fentryid,flocaleid |
| 2 | pk_t_open_rest_op_parameters_l |  | fpkid |

---

## 操作参数-子表 t_open_rest_op_parameters

- **表名称：** 操作参数-子表
- **表名：** t_open_rest_op_parameters

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fop_param_name | 参数名 | varchar | 100 |  | √ | ' ' | 参数名 |
| 3 | fop_param_value | 值 | varchar | 150 |  | √ | ' ' | 值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fop_param_desc | 说明 | varchar | 255 |  | √ | ' ' | 说明 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_rest_op_parameters |  | fentryid |
| 2 | idx_open_rest_op_parameters_fk |  | fid |

---

## 过滤条件分录-多语言表 t_open_rest_filter_entry_l

- **表名称：** 过滤条件分录-多语言表
- **表名：** t_open_rest_filter_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffilter_label | 字段描述 | varchar | 250 |  | √ | ' ' | 字段描述 |
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
| 1 | pk_t_open_rest_filter_entry_l |  | fpkid |
| 2 | idx_open_rest_filter_entry_l_0 |  | fentryid,flocaleid |

---

## 200响应体-子表 t_open_rest_resp_body

- **表名称：** 200响应体-子表
- **表名：** t_open_rest_resp_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresp_body_type | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: string :string object :object long :long integer :integer datetime :datetime decimal :decimal boolean :boolean date :date-only time :time-only ml_string :ml_string |
| 3 | fresp_body_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 4 | fresp_body_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 5 | fresp_body_full_name | 参数全名 | varchar | 200 |  | √ | ' ' | 参数全名 |
| 6 | fresp_body_name | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | fresp_body_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_rest_resp_body_fk |  | fid |
| 2 | pk_t_open_rest_resp_body |  | fentryid |

---

## Query参数-多语言表 t_open_rest_req_querys_l

- **表名称：** Query参数-多语言表
- **表名：** t_open_rest_req_querys_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freq_query_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
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
| 1 | pk_t_open_rest_req_querys_l |  | fpkid |
| 2 | idx_open_rest_req_querys_l_0 |  | fentryid,flocaleid |
