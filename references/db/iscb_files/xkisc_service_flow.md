# 服务流程-xkisc_service_flow

## 服务流程-多语言表 t_isc_service_flow_l

- **表名称：** 服务流程-多语言表
- **表名：** t_isc_service_flow_l

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
| 1 | idx_isc_service_flow_l_i |  | fid,flocaleid |
| 2 | t_isc_service_flow_l_pkey |  | fpkid |

---

## 资源-子表 t_isc_service_flow_res

- **表名称：** 资源-子表
- **表名：** t_isc_service_flow_res

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcategory | 资源类别 | varchar | 30 |  | √ | ' ' | 资源类别,枚举: isc_data_source :数据源 isc_data_copy :集成方案 isc_data_copy_trigger :启动方案 isc_value_conver_rule :值转换规则 isc_metadata_schema :集成对象 isc_custom_function :自定义函数 isc_apic_webapi :WebAPI登记 isc_apic_script :自定义API isc_mq_subscriber :消息订阅主题 isc_apic_mservice :苍穹微服务 isc_mq_publisher :消息发布主题 isc_service_flow :服务流程 isc_data_comp :数据对比方案 isc_import_file_trigger :数据导入任务 isc_export_file_trigger :数据导出任务 isc_user_defined_event :集成云自定义事件 isc_apic_for_external_api :外部系统API登记 iscx_data_flow_trigger :数据流启动方案 |
| 3 | fresouce | 引用资源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fres_source_text | 数据源 | varchar | 255 |  | √ | ' ' | 数据源 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | falias | 别名 | varchar | 50 |  | √ | ' ' | 别名 |
| 8 | fsource | fsource | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_service_flow_res_pkey |  | fentryid |
| 2 | idx_isc_service_flow_res_i |  | fid |

---

## 变量-子表 t_isc_service_flow_var

- **表名称：** 变量-子表
- **表名：** t_isc_service_flow_var

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fis_input_param | 是否输入参数 | bpchar | 1 |  | √ | '0' | 是否输入参数 |
| 3 | fname | 变量名 | varchar | 50 |  | √ | ' ' | 变量名 |
| 4 | fcategory | 变量类别 | varchar | 30 |  | √ | ' ' | 变量类别,枚举: isc_type_simple_value :简单值 isc_metadata_schema :集成对象 |
| 5 | ftype | 数据类型 | int8 | 64 |  | √ | 0 | 数据类型 - 简单值 isc_type_simple_value |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdefault_value | 默认值 | varchar | 1000 |  | √ | ' ' | 默认值 |
| 8 | fdesc | 变量描述 | varchar | 150 |  | √ | ' ' | 变量描述 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fis_output_param | 是否输出参数 | bpchar | 1 |  | √ | '0' | 是否输出参数 |
| 11 | fsource | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 12 | fis_array | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_isc_service_flow_var_i |  | fid |
| 2 | t_isc_service_flow_var_pkey |  | fentryid |

---

## 服务流程-主表 t_isc_service_flow

- **表名称：** 服务流程-主表
- **表名：** t_isc_service_flow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | fmq_subscriber | 消息订阅主题 | int8 | 64 |  | √ | 0 | [消息订阅主题 isc_mq_subscriber](../iscb_files/isc_mq_subscriber.md) |
| 4 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 5 | fpriority | 优先级 | varchar | 10 |  | √ | '+0000' | 优先级,枚举: -9000 :最高 -7000 :很高 -5000 :高 -3000 :中高 +0000 :中 +3000 :中低 +5000 :低 +7000 :很低 +9000 :最低 |
| 6 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 7 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fis_released | 已发布 | bpchar | 1 |  | √ | '0' | 已发布 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 14 | floglevel | 日志级别 | varchar | 10 |  | √ | ' ' | 日志级别,枚举: info :信息 warn :警告 error :错误 |
| 15 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |
| 16 | fauto_save_time | 自动保存时间间隔（秒） | int8 | 64 |  | √ | 0 | 自动保存时间间隔（秒） |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcomment | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fjob_mutex | 硬件资源分配 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 21 | finit_mode | 启动方式 | varchar | 30 |  | √ | ' ' | 启动方式,枚举: MANUAL :人工启动 TIMER :定时启动 EVENT :事件触发 MESSAGE :消息启动 |
| 22 | fdefine_json | 流程定义 | varchar | 255 |  | √ | ' ' | 流程定义 |
| 23 | fproc_digest | 流程摘要模板 | varchar | 250 |  | √ | ' ' | 流程摘要模板 |
| 24 | fdefine_json_tag | 流程定义_详情 | text | 0 |  |  | null | 流程定义_详情 |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fclassification | 方案分类 | int8 | 64 |  | √ | 0 | [自定义分类 isc_schema_category](../iscb_files/isc_schema_category.md) |
| 27 | flog_record_count | 最大记录日志数 | int8 | 64 |  | √ | 0 | 最大记录日志数 |
| 28 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 29 | fdisable_trace | 禁止记录追溯信息 | varchar | 10 |  | √ | ' ' | 禁止记录追溯信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_service_flow_m |  | fmodifytime |
| 2 | t_isc_service_flow_pkey |  | fid |
| 3 | idx_isc_service_flow_i |  | fnumber |
