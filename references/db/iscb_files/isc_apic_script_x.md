# API登记-isc_apic_script_x

## API登记-主表 t_isc_apic_script_x

- **表名称：** API登记-主表
- **表名：** t_isc_apic_script_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fscript_tag_tag | 脚本_详情 | text | 0 |  |  | null | 脚本_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | API分类 isc_interface_category |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 7 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 8 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | '0' | 记录API调用日志 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fauth_required | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 12 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '1' | 不发布到开放平台 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fpreset | 是否预置 | bpchar | 1 |  | √ | '1' | 是否预置 |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 18 | fscript_tag | 脚本 | varchar | 255 |  | √ | ' ' | 脚本 |
| 19 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 20 | fdisable_trace | 禁止记录追溯信息 | bpchar | 1 |  | √ | '1' | 禁止记录追溯信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_apic_script_x |  | fid |
| 2 | idx_script_x_1 |  | fnumber |

---

## 输入参数-子表 t_isc_apic_script_in_x

- **表名称：** 输入参数-子表
- **表名：** t_isc_apic_script_in_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 3 | finput_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 ENUM :枚举 STRUCT :结构 string2 :纯字符串 double :浮点数 |
| 4 | finput_is_array | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 5 | finput_field | 字段名 | varchar | 255 |  | √ | ' ' | 字段名 |
| 6 | finput_description | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdefault_value | 默认值 | varchar | 500 |  | √ | ' ' | 默认值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_apic_script_in_x |  | fentryid |
| 2 | idx_script_in_x_1 |  | fid |

---

## 资源-子表 t_isc_apic_script_res_x

- **表名称：** 资源-子表
- **表名：** t_isc_apic_script_res_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 外部系统类型 | varchar | 30 |  | √ | ' ' | 外部系统类型,枚举: isc_cn_config :外部系统 |
| 3 | fresouce | 外部系统 | int8 | 64 |  | √ | 0 | 外部系统配置 isc_cn_config |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | falias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_apic_script_res_x |  | fentryid |
| 2 | idx_script_res_x_1 |  | fid |

---

## 结果字段-子表 t_isc_apic_script_out_x

- **表名称：** 结果字段-子表
- **表名：** t_isc_apic_script_out_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutput_field | 字段名 | varchar | 255 |  | √ | ' ' | 字段名 |
| 3 | foutput_is_array | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 4 | foutput_data_type | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 ENUM :枚举 STRUCT :结构 string2 :纯字符串 double :浮点数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | foutput_description | 字段描述 | varchar | 500 |  | √ | ' ' | 字段描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_apic_script_out_x |  | fentryid |
| 2 | idx_script_out_x_1 |  | fid |

---

## API登记-多语言表 t_isc_apic_script_x_l

- **表名称：** API登记-多语言表
- **表名：** t_isc_apic_script_x_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_script_x_l_1 |  | fid |
| 2 | pk_t_isc_apic_script_x_l |  | fpkid |
