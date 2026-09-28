# 自定义API-isc_apic_script

## 输入参数-子表 t_iscb_apic_script_input

- **表名称：** 输入参数-子表
- **表名：** t_iscb_apic_script_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 3 | finput_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 ENUM :枚举 STRUCT :结构 string2 :纯字符串 double :浮点数 unknown :任意值 |
| 4 | finput_is_array | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
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
| 1 | idx_iscb_apic_script_input_i |  | fid |
| 2 | t_iscb_apic_script_input_pkey |  | fentryid |

---

## 自定义API-多语言表 t_iscb_apic_script_l

- **表名称：** 自定义API-多语言表
- **表名：** t_iscb_apic_script_l

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
| 1 | t_iscb_apic_script_l_pkey |  | fpkid |
| 2 | idx_iscb_apic_script_l_i |  | fid,flocaleid |

---

## 结果字段-子表 t_iscb_apic_script_output

- **表名称：** 结果字段-子表
- **表名：** t_iscb_apic_script_output

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutput_field | 字段名 | varchar | 255 |  | √ | ' ' | 字段名 |
| 3 | foutput_is_array | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 4 | foutput_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 ENUM :枚举 STRUCT :结构 string2 :纯字符串 double :浮点数 unknown :任意值 |
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
| 1 | idx_iscb_apic_script_output_i |  | fid |
| 2 | t_iscb_apic_script_output_pkey |  | fentryid |

---

## 资源-子表 t_iscb_apic_script_res

- **表名称：** 资源-子表
- **表名：** t_iscb_apic_script_res

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 资源类别 | varchar | 30 |  | √ | ' ' | 资源类别,枚举: isc_data_source :数据源 isc_data_copy :集成方案 isc_custom_function :自定义函数 isc_apic_for_external_api :外部系统API isc_service_flow :服务流程 isc_apic_mservice :苍穹微服务 isc_apic_webapi :WebAPI登记 |
| 3 | fresouce | 引用资源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
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
| 1 | idx_iscb_apic_script_res_i |  | fid |
| 2 | t_iscb_apic_script_res_pkey |  | fentryid |

---

## 自定义API-主表 t_iscb_apic_script

- **表名称：** 自定义API-主表
- **表名：** t_iscb_apic_script

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 自定义分类 isc_schema_category |
| 3 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 4 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 5 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 6 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | '0' | 记录API调用日志 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fauth_required | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 10 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '0' | 不发布到开放平台 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 16 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 17 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 18 | fscript_tag_tag | API调用脚本_详情 | text | 0 |  |  | null | API调用脚本_详情 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fpub_status | fpub_status | varchar | 30 |  | √ | ' ' |  |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 23 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 24 | fomit_empty_params | 忽略空参数 | bpchar | 1 |  | √ | '0' | 忽略空参数 |
| 25 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fscript_tag | API调用脚本 | varchar | 255 |  | √ | ' ' | API调用脚本 |
| 28 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 29 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 30 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_script_g |  | fgroupid |
| 2 | idx_iscb_apic_script_n |  | fnumber |
| 3 | idx_iscb_apic_script_s |  | fstatus |
| 4 | t_iscb_apic_script_pkey |  | fid |
| 5 | idx_iscb_apic_script_m |  | fmodifytime |
