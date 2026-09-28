# 服务流程转API-isc_apic_by_sf

## 服务流程转API-多语言表 t_iscb_apic_by_sf_l

- **表名称：** 服务流程转API-多语言表
- **表名：** t_iscb_apic_by_sf_l

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
| 1 | pk_t_iscb_apic_by_sf_l |  | fpkid |
| 2 | idx_iscb_apic_by_sf_l_0 |  | fid,flocaleid |

---

## 服务流程转API-主表 t_iscb_apic_by_sf

- **表名称：** 服务流程转API-主表
- **表名：** t_iscb_apic_by_sf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [自定义分类 isc_schema_category](../iscb_files/isc_schema_category.md) |
| 3 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 4 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 5 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 6 | frecord_log | 记录API调用日志 | bpchar | 1 |  | √ | '0' | 记录API调用日志 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fauth_required | 需要授权 | bpchar | 1 |  | √ | '0' | 需要授权 |
| 10 | fnot_publish | 不发布到开放平台 | bpchar | 1 |  | √ | '0' | 不发布到开放平台 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fnamespace | 命名空间 | varchar | 255 |  | √ | ' ' | 命名空间 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fservice_flow_id | 服务流程 | int8 | 64 |  | √ | 0 | [服务流程 isc_service_flow](../iscb_files/isc_service_flow.md) |
| 16 | fwsinputparam | 输入参数名 | varchar | 150 |  | √ | ' ' | 输入参数名 |
| 17 | fin_digest | API参数摘要模板 | varchar | 150 |  | √ | ' ' | API参数摘要模板 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcheck_param_type | fcheck_param_type | bpchar | 1 |  | √ | '0' |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fasyn | 启用异步模式 | bpchar | 1 |  | √ | '0' | 启用异步模式 |
| 22 | fout_digest | API结果摘要模板 | varchar | 150 |  | √ | ' ' | API结果摘要模板 |
| 23 | fdescription | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 24 | fopenapi_version | 开放平台版本 | varchar | 10 |  | √ | ' ' | 开放平台版本,枚举: 2 :2.0 1 :1.0 |
| 25 | fno_proc_inst | 启用无实例模式 | bpchar | 1 |  | √ | '0' | 启用无实例模式 |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 28 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |
| 29 | fwsoutputparam | 输出参数名 | varchar | 150 |  | √ | ' ' | 输出参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_apic_by_sf |  | fid |
| 2 | idx_iscb_apic_by_sf |  | fnumber |
