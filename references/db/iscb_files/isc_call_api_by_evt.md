# API任务（事件触发）-isc_call_api_by_evt

## 取值字段-子表 t_isc_api_evt_fields

- **表名称：** 取值字段-子表
- **表名：** t_isc_api_evt_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdata_type | 字段类型 | varchar | 100 |  | √ | ' ' | 字段类型 |
| 3 | ffield | 集成对象字段 | varchar | 100 |  | √ | ' ' | 集成对象字段 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_api_evt_fields |  | fentryid |
| 2 | idx_isc_api_evt_fs_fk |  | fid |

---

## API任务（事件触发）-多语言表 t_isc_capi_by_evt_l

- **表名称：** API任务（事件触发）-多语言表
- **表名：** t_isc_capi_by_evt_l

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
| 1 | idx_isc_a_evt_l_0 |  | fid,flocaleid |
| 2 | pk_t_isc_capi_by_evt_l |  | fpkid |

---

## API任务（事件触发）-主表 t_isc_capi_by_evt

- **表名称：** API任务（事件触发）-主表
- **表名：** t_isc_capi_by_evt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcaller | 调用者 | int8 | 64 |  | √ | 0 | API调用者 isc_apic_caller |
| 4 | fformat_script_tag | API调用脚本_详情 | text | 0 |  |  | null | API调用脚本_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fmetaschema | 集成对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 8 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 9 | fapi_type | API类型 | varchar | 50 |  | √ | ' ' | API类型,枚举: isc_apic_for_external_api :外部系统API isc_apic_script :自定义API isc_apic_webapi :WebAPI登记 |
| 10 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fformat_script | API调用脚本 | varchar | 255 |  | √ | ' ' | API调用脚本 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fapi | API | int8 | 64 |  | √ | 0 | 外部系统API登记 isc_apic_for_external_api |
| 20 | fevents | 触发事件 | varchar | 1000 |  | √ | ' ' | 触发事件,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_capi_by_evt |  | fid |
| 2 | idx_isc_aevt_num |  | fnumber |
