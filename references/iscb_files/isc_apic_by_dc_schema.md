# 数据集成方案转API-isc_apic_by_dc_schema

## 数据集成方案转API-多语言表 t_iscb_apic_by_dc_schema_l

- **表名称：** 数据集成方案转API-多语言表
- **表名：** t_iscb_apic_by_dc_schema_l

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
| 1 | t_iscb_apic_by_dc_schema_l_pkey |  | fpkid |
| 2 | idx_iscb_apic_dc_schema_l |  | fid,fname |

---

## 数据集成方案转API-主表 t_iscb_apic_by_dc_schema

- **表名称：** 数据集成方案转API-主表
- **表名：** t_iscb_apic_by_dc_schema

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
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fschema_category | 分类 | int8 | 64 |  | √ | 0 | 自定义分类 isc_schema_category |
| 16 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 17 | ftrigger | 启动方案 | int8 | 64 |  | √ | 0 | 启动方案 isc_data_copy_trigger |
| 18 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 19 | fschema | 集成方案 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcheck_param_type | 校验参数格式 | bpchar | 1 |  | √ | '0' | 校验参数格式 |
| 22 | fpub_status | fpub_status | varchar | 30 |  | √ | ' ' |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fmax_count | 结果行数限制 | int8 | 64 |  | √ | 1000 | 结果行数限制 |
| 25 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 26 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 27 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 28 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 29 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: EXECUTE :从来源系统"取数推送"到目标系统 PULL :从来源系统"取数并转换"为目标单数据 PUSH :将源单数据"转换后推送"到目标系统 TRANSFER :将源单数据"转换"为目标单数据 |
| 30 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 31 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 32 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 33 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_apic_dc_cg |  | fschema_category |
| 2 | idx_iscb_apic_dc_schema |  | fschema,ftrigger |
| 3 | t_iscb_apic_by_dc_schema_pkey |  | fid |
