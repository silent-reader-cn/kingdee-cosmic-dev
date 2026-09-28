# 外部系统API登记-isc_apic_for_external_api

## 外部系统API登记-主表 t_iscb_external_api

- **表名称：** 外部系统API登记-主表
- **表名：** t_iscb_external_api

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 3 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 4 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 5 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | ' ' | 记录API调用日志 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fauth_required | 需要授权 | bpchar | 1 |  | √ | ' ' | 需要授权 |
| 9 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '0' | 不发布到开放平台 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 13 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 14 | fschema_category | 分类 | int8 | 64 |  | √ | 0 | 自定义分类 isc_schema_category |
| 15 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 16 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | fname | varchar | 30 |  | √ | ' ' |  |
| 19 | fcheck_param_type | 校验参数格式 | bpchar | 1 |  | √ | '0' | 校验参数格式 |
| 20 | fpub_status | fpub_status | varchar | 30 |  | √ | ' ' |  |
| 21 | fservice_url | 接口标识（URL） | varchar | 255 |  | √ | ' ' | 接口标识（URL） |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 24 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 25 | fomit_empty_params | 忽略空参数 | bpchar | 1 |  | √ | '0' | 忽略空参数 |
| 26 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 27 | fdata_source_id | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 28 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 30 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 31 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_external_api_n |  | fnumber |
| 2 | t_iscb_external_api_pkey |  | fid |
| 3 | idx_iscb_external_api_c |  | fschema_category |

---

## 输入参数-子表 t_iscb_external_api_in

- **表名称：** 输入参数-子表
- **表名：** t_iscb_external_api_in

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 是否必填 | varchar | 10 |  | √ | ' ' | 是否必填 |
| 3 | finput_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 unknown :任意值 |
| 4 | finput_is_array | 是否多值 | varchar | 20 |  | √ | '0' | 是否多值 |
| 5 | finput_field | 字段名 | varchar | 255 |  | √ | ' ' | 字段名 |
| 6 | finput_description | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdefault_value | 默认值 | varchar | 500 |  | √ | ' ' | 默认值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_external_api_in_pkey |  | fentryid |
| 2 | idx_iscb_external_api_in |  | fid |

---

## 结果字段-子表 t_iscb_external_api_out

- **表名称：** 结果字段-子表
- **表名：** t_iscb_external_api_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutput_field | 字段名 | varchar | 255 |  | √ | ' ' | 字段名 |
| 3 | foutput_is_array | 是否多值 | varchar | 20 |  | √ | '0' | 是否多值 |
| 4 | foutput_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 ENUM :枚举 STRUCT :结构 double :浮点数 unknown :任意值 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | foutput_description | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_external_api_out_pkey |  | fentryid |
| 2 | idx_iscb_external_api_out_i |  | fid |

---

## 外部系统API登记-多语言表 t_iscb_external_api_l

- **表名称：** 外部系统API登记-多语言表
- **表名：** t_iscb_external_api_l

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
| 1 | idx_iscb_external_api_l_i |  | fid,flocaleid |
| 2 | t_iscb_external_api_l_pkey |  | fpkid |
