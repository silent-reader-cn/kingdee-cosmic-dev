# 集成对象-isc_metadata_schema

## 函数分录-子表 t_iscb_dataschema_fn

- **表名称：** 函数分录-子表
- **表名：** t_iscb_dataschema_fn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffunction_number | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 3 | ffunction_description | ffunction_description | varchar | 200 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffunction | 自定义函数 | int8 | 64 |  | √ | 0 | 自定义函数 isc_custom_function |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_dataschema_fn_pkey |  | fentryid |
| 2 | idx_isc_ds_fn_fk |  | fid |

---

## 结果分录-子表 t_isc_dataresult

- **表名称：** 结果分录-子表
- **表名：** t_isc_dataresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresult_remark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fresult_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fresult_index | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 7 | fresult_number | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 8 | fresult_schema | 数据模型 | varchar | 100 |  | √ | ' ' | 数据模型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_dataresult_pkey |  | fentryid |
| 2 | idx_isc_dataresutl_fid |  | fid |

---

## 集成对象-多语言表 t_isc_dataschema_l

- **表名称：** 集成对象-多语言表
- **表名：** t_isc_dataschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 元数据名称 | varchar | 150 |  | √ | ' ' | 元数据名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dataschema_l_0 |  | flocaleid,fid |
| 2 | t_isc_dataschema_l_pkey |  | fpkid |
| 3 | idx_t_isc_dataschema_l_1 |  | fid |

---

## 操作分录-子表 t_isc_dataoperation

- **表名称：** 操作分录-子表
- **表名：** t_isc_dataoperation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | ftype | 类型 | varchar | 100 |  | √ | ' ' | 类型 |
| 4 | flabel | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | findex | 序号 | varchar | 100 |  | √ | ' ' | 序号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnumber | 操作编码 | varchar | 100 |  | √ | ' ' | 操作编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_dataoperation_pkey |  | fentryid |
| 2 | idx_isc_dataoperation_0 |  | fid |

---

## 参数分录-子表 t_isc_dataparam

- **表名称：** 参数分录-子表
- **表名：** t_isc_dataparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintegerfield | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 3 | fparam_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 4 | fparam_number | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 5 | fparam_schema | 数据模型 | varchar | 100 |  | √ | ' ' | 数据模型 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fparam_remark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dataparam_fid |  | fid |
| 2 | t_isc_dataparam_pkey |  | fentryid |

---

## 常量分录-子表 t_isc_dataconst

- **表名称：** 常量分录-子表
- **表名：** t_isc_dataconst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fvalue | 值 | varchar | 100 |  | √ | ' ' | 值 |
| 4 | flabel | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 5 | findex | 序号 | varchar | 100 |  | √ | ' ' | 序号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_dataconst_pkey |  | fentryid |
| 2 | idx_isc_dataconst_0 |  | fid |

---

## 属性分录-子表 t_isc_dataproperty

- **表名称：** 属性分录-子表
- **表名：** t_isc_dataproperty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fname | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 4 | flabel | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 5 | findex | 序号 | varchar | 100 |  | √ | ' ' | 序号 |
| 6 | fdata_schema | 数据模型 | varchar | 100 |  | √ | ' ' | 数据模型 |
| 7 | fis_primary_key | 主键 | bpchar | 1 |  | √ | ' ' | 主键 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fis_encrypt | 数据脱敏 | bpchar | 1 |  | √ | ' ' | 数据脱敏 |
| 10 | fcustomize | 自定义 | bpchar | 1 |  | √ | ' ' | 自定义 |
| 11 | frequired | 必填 | bpchar | 1 |  | √ | ' ' | 必填 |
| 12 | fdata_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dataproperty_fk |  | fid |
| 2 | idx_isc_dataproperty_s |  | fdata_schema |
| 3 | t_isc_dataproperty_pkey |  | fentryid |

---

## 集成对象-主表 t_isc_dataschema

- **表名称：** 集成对象-主表
- **表名：** t_isc_dataschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 3 | fresult_jst | 结果转换脚本 | varchar | 2000 |  | √ | ' ' | 结果转换脚本 |
| 4 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 5 | fresult_jst_tag | 结果转换脚本_详情 | text | 0 |  |  | null | 结果转换脚本_详情 |
| 6 | felement_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 int :整数 long :长整数 boolean :布尔值 decimal :小数 double :浮点数 datetime :日期/时间 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fview_sql | 视图SQL | varchar | 255 |  | √ | ' ' | 视图SQL |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fparam_jst | 参数转换脚本 | varchar | 2000 |  | √ | ' ' | 参数转换脚本 |
| 11 | fparam_jst_tag | 参数转换脚本_详情 | text | 0 |  |  | null | 参数转换脚本_详情 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fis_init | 已初始化 | bpchar | 1 |  | √ | ' ' | 已初始化 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 18 | ffull_name | 全名 | varchar | 200 |  | √ | ' ' | 全名 |
| 19 | fremark | 备注 | varchar | 150 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | ferror_stack_tag | 错误堆栈_详情 | text | 0 |  |  | null | 错误堆栈_详情 |
| 23 | fview_sql_tag | 视图SQL_详情 | text | 0 |  |  | null | 视图SQL_详情 |
| 24 | ferror_stack | 错误堆栈 | varchar | 2000 |  | √ | ' ' | 错误堆栈 |
| 25 | ftable_name | 数据表 | varchar | 150 |  | √ | ' ' | 数据表 |
| 26 | fstate | 同步状态 | varchar | 5 |  | √ | '0' | 同步状态,枚举: S :成功 F :失败 W :待同步 Z :自定义 |
| 27 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: ENTITY :实体 ENUM :枚举 TABLE :数据表 VIEW :视图 SERVICE :加载服务 QUERY :查询服务 STRUCT :结构 ELEMENT :元素 EVT_RSC :事件源 |
| 28 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_dataschema_pkey |  | fid |
| 2 | idx_isc_d_sch_creatime |  | fcreatetime |
| 3 | idx_isc_data_schema_groupid |  | fgroupid |
| 4 | idx_isc_data_schema_n |  | fnumber |

---

## 事件分录-子表 t_isc_dataevent

- **表名称：** 事件分录-子表
- **表名：** t_isc_dataevent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | flabel | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | findex | 序号 | varchar | 100 |  | √ | ' ' | 序号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnumber | 事件编码 | varchar | 100 |  | √ | ' ' | 事件编码 |
| 8 | fcustomize | 自定义 | bpchar | 1 |  | √ | ' ' | 自定义 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_dataevent_0 |  | fid |
| 2 | t_isc_dataevent_pkey |  | fentryid |
