# API任务（定时）-isc_call_api_by_timer

## API任务（定时）-多语言表 t_isc_capi_by_timer_l

- **表名称：** API任务（定时）-多语言表
- **表名：** t_isc_capi_by_timer_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_a_tm_l_0 |  | fid,flocaleid |
| 2 | pk_t_isc_capi_by_timer_l |  | fpkid |

---

## API任务（定时）-主表 t_isc_capi_by_timer

- **表名称：** API任务（定时）-主表
- **表名：** t_isc_capi_by_timer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fformat_script_tag | API调用脚本_详情 | text | 0 |  |  | null | API调用脚本_详情 |
| 4 | fcaller | 调用者 | int8 | 64 |  | √ | 0 | API调用者 isc_apic_caller |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fend_time | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 9 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fapi_type | API类型 | varchar | 50 |  | √ | ' ' | API类型,枚举: isc_apic_for_external_api :外部系统API isc_apic_script :自定义API isc_apic_webapi :WebAPI登记 |
| 11 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | finterval | 执行频率 | varchar | 30 |  | √ | ' ' | 执行频率,枚举: 1 :执行频率 - 1次/小时 2 :执行频率 - 2次/小时 3 :执行频率 - 3次/小时 5 :执行频率 - 5次/小时 10 :执行频率 - 10次/小时 20 :执行频率 - 20次/小时 30 :执行频率 - 30次/小时 60 :执行频率 - 60次/小时 d :每天 w :每周 m :每月 d1 :每天凌晨一点 0 :自定义 |
| 14 | fformat_script | API调用脚本 | varchar | 255 |  | √ | ' ' | API调用脚本 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcron_expr | 触发间隔 | varchar | 50 |  | √ | ' ' | 触发间隔 |
| 19 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fexe_job_user | 执行作业的用户 | varchar | 100 |  | √ | ' ' | 执行作业的用户 |
| 22 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 23 | fapi | API | int8 | 64 |  | √ | 0 | 外部系统API登记 isc_apic_for_external_api |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_capi_by_timer |  | fid |
| 2 | idx_isc_atm_num |  | fnumber |
