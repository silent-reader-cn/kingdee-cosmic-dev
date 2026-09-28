# 值转换规则-isc_value_conver_rule

## 值转换规则-多语言表 t_isc_value_conver_rule_l

- **表名称：** 值转换规则-多语言表
- **表名：** t_isc_value_conver_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_value_conver_rule_l_pkey |  | fpkid |
| 2 | idx_isc_vaconru_l_fid |  | fid,flocaleid |

---

## 值转换规则-主表 t_isc_value_conver_rule

- **表名称：** 值转换规则-主表
- **表名：** t_isc_value_conver_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsource_data_source | 源系统 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 3 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 4 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 5 | fisfuzzymatch | 开启模糊匹配 | bpchar | 1 |  | √ | ' ' | 开启模糊匹配 |
| 6 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fisc_script | 集成脚本 | varchar | 510 |  | √ | ' ' | 集成脚本 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 13 | fsql_tag | SQL脚本_详情 | text | 0 |  |  | null | SQL脚本_详情 |
| 14 | fclass_name | Java类名/微服务 | varchar | 300 |  | √ | ' ' | Java类名/微服务 |
| 15 | fsql | SQL脚本 | varchar | 510 |  | √ | ' ' | SQL脚本 |
| 16 | frun_copy_on_missed | 目标值不存在时执行数据集成 | bpchar | 1 |  | √ | ' ' | 目标值不存在时执行数据集成 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | frule_type | 规则类型 | varchar | 100 |  | √ | ' ' | 规则类型,枚举: tlb :常量转换 auto :候选键映射 composite :组合规则 sql :SQL script :脚本 java :Java/微服务 mapping :人工映射 |
| 20 | ftarget_data_source | 目标系统 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 21 | fdata_copy_schema | 数据集成方案 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 22 | fvalue_attribute | 取值属性 | varchar | 100 |  | √ | ' ' | 取值属性 |
| 23 | fiscached | 缓存转换结果 | bpchar | 1 |  | √ | ' ' | 缓存转换结果 |
| 24 | fdata_copy_trigger | 数据集成启动方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 25 | ftlb | 转换表 | varchar | 510 |  | √ | ' ' | 转换表 |
| 26 | ftlb_tag | 转换表_详情 | text | 0 |  |  | ' ' | 转换表_详情 |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fdefault_value | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 29 | fisc_script_tag | 集成脚本_详情 | text | 0 |  |  | null | 集成脚本_详情 |
| 30 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 31 | fsource_data_schema | 源对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 32 | ftarget_data_schema | 目标对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 33 | fmapping_type | 映射类型 | varchar | 30 |  | √ | ' ' | 映射类型,枚举: 1 :实体对实体 2 :实体对枚举 3 :实体对数据表 4 :枚举对实体 5 :枚举对枚举 6 :枚举对数据表 7 :数据表对实体 8 :数据表对枚举 9 :数据表对数据表 10 :未知 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_value_conver_rule_pkey |  | fid |
| 2 | idx_iscb_vaconru_num |  | fnumber |

---

## 值转换规则分录-子表 t_isc_value_conv_sub_rule

- **表名称：** 值转换规则分录-子表
- **表名：** t_isc_value_conv_sub_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsub_rule | 值转换规则 | int8 | 64 |  | √ | 0 | 值转换规则 isc_value_conver_rule |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_value_conv_sub_rule_pkey |  | fentryid |
| 2 | idx_isc_vcsr_fid |  | fid |
