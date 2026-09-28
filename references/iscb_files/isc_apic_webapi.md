# WebAPI登记-isc_apic_webapi

## WebAPI登记-多语言表 t_iscb_apic_webapi_l

- **表名称：** WebAPI登记-多语言表
- **表名：** t_iscb_apic_webapi_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_apic_webapi_l |  | fpkid |
| 2 | idx_iscb_apic_webapi_l_0 |  | fid,flocaleid |

---

## URL参数-子表 t_iscb_web_url_params

- **表名称：** URL参数-子表
- **表名：** t_iscb_web_url_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furl_param_name | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 3 | furl_param_required | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 4 | furl_param_value | 参数值 | varchar | 1024 |  | √ | ' ' | 参数值 |
| 5 | furl_param_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 6 | furl_param_type | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 unknown :任意值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | furl_param_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_web_url_params_fk |  | fid |
| 2 | pk_t_iscb_web_url_params |  | fentryid |

---

## 函数分录-子表 t_iscb_apic_webapi_fn

- **表名称：** 函数分录-子表
- **表名：** t_iscb_apic_webapi_fn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 资源类别 | varchar | 30 |  | √ | ' ' | 资源类别,枚举: isc_custom_function :自定义函数 |
| 3 | fresouce | 引用资源 | int8 | 64 |  | √ | 0 | 自定义函数 isc_custom_function |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | falias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_webapi_fn_i |  | fid |
| 2 | pk_t_iscb_apic_webapi_fn |  | fentryid |

---

## 请求体-子表 t_iscb_web_req_body

- **表名称：** 请求体-子表
- **表名：** t_iscb_web_req_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freq_b_param_value | 参数值 | varchar | 1024 |  | √ | ' ' | 参数值 |
| 3 | freq_b_param_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 4 | freq_b_param_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 5 | freq_b_param_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 6 | freq_b_param_name | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | freq_b_param_required | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 10 | freq_b_param_type | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 unknown :任意值 IERP_FILE :苍穹附件 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_web_req_body_fk |  | fid |
| 2 | pk_t_iscb_web_req_body |  | fentryid |

---

## 请求头-子表 t_iscb_web_req_header

- **表名称：** 请求头-子表
- **表名：** t_iscb_web_req_header

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freq_h_param_name | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | freq_h_param_required | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 5 | freq_h_param_value | 参数值 | varchar | 1024 |  | √ | ' ' | 参数值 |
| 6 | freq_h_param_type | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 unknown :任意值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | freq_h_param_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_web_req_head_fk |  | fid |
| 2 | pk_t_iscb_web_req_header |  | fentryid |

---

## 响应体-子表 t_iscb_web_resp_body

- **表名称：** 响应体-子表
- **表名：** t_iscb_web_resp_body

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresp_b_param_required | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fresp_b_param_is_array | 多值 | bpchar | 1 |  | √ | '0' | 多值 |
| 6 | fresp_b_param_name | 参数名 | varchar | 255 |  | √ | ' ' | 参数名 |
| 7 | fresp_b_param_value | 参数值 | varchar | 1024 |  | √ | ' ' | 参数值 |
| 8 | fresp_b_param_example | 示例值 | varchar | 1024 |  | √ | ' ' | 示例值 |
| 9 | fresp_b_param_desc | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fresp_b_param_type | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 unknown :任意值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_web_resp_fk |  | fid |
| 2 | pk_t_iscb_web_resp_body |  | fentryid |

---

## WebAPI登记-主表 t_iscb_apic_webapi

- **表名称：** WebAPI登记-主表
- **表名：** t_iscb_apic_webapi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 3 | fmethod |  | varchar | 50 |  | √ | ' ' | ,枚举: GET :GET POST :POST HEAD :HEAD OPTIONS :OPTIONS PUT :PUT DELETE :DELETE TRACE :TRACE PATCH :PATCH |
| 4 | fsourceapp | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 5 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | '0' | 记录API调用日志 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fneed_format_result | 格式化响应结果 | bpchar | 1 |  | √ | '0' | 格式化响应结果 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fauth_required | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 10 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '1' | 不发布到开放平台 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 14 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 15 | fis_multipart | multipart/form-data | bpchar | 1 |  | √ | '0' | multipart/form-data |
| 16 | fin_digest | API参数摘要模板 | varchar | 100 |  | √ | ' ' | API参数摘要模板 |
| 17 | ftimeout | 超时时长 | int8 | 64 |  | √ | 0 | 超时时长 |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcharset | 字符集 | varchar | 50 |  | √ | ' ' | 字符集 |
| 21 | furl_prefix | URL前缀 | varchar | 255 |  | √ | ' ' | URL前缀 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fscript_mode | 脚本模式 | bpchar | 1 |  | √ | '0' | 脚本模式 |
| 24 | fout_digest | API结果摘要模板 | varchar | 100 |  | √ | ' ' | API结果摘要模板 |
| 25 | fomit_empty_params | 忽略空参数 | bpchar | 1 |  | √ | '0' | 忽略空参数 |
| 26 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 27 | finvoke_script_tag | 调用脚本_详情 | text | 0 |  |  | null | 调用脚本_详情 |
| 28 | furl_path | URL路径 | varchar | 255 |  | √ | ' ' | URL路径 |
| 29 | finvoke_script | 调用脚本 | varchar | 255 |  | √ | ' ' | 调用脚本 |
| 30 | fconn_type | 连接类型 | varchar | 36 |  | √ | ' ' | 连接类型 isc_connection_type |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 33 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_webapi_g |  | fgroupid |
| 2 | pk_t_iscb_apic_webapi |  | fid |
| 3 | idx_iscb_apic_webapi_n |  | fnumber |
