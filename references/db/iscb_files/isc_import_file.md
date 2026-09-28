# 数据导入方案-isc_import_file

## 导入字段-子表 t_iscb_import_file_input

- **表名称：** 导入字段-子表
- **表名：** t_iscb_import_file_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finput_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |
| 3 | fis_judge_key | 候选键 | bpchar | 1 |  | √ | ' ' | 候选键 |
| 4 | finput_field | 字段名 | varchar | 100 |  | √ | ' ' | 字段名 |
| 5 | finput_description | 字段描述 | varchar | 150 |  | √ | ' ' | 字段描述 |
| 6 | fis_required | 必填 | bpchar | 1 |  | √ | ' ' | 必填 |
| 7 | fis_primary_key | 主键 | bpchar | 1 |  | √ | ' ' | 主键 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | falias | 别名 | varchar | 100 |  | √ | ' ' | 别名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_import_file_input_fk |  | fid |
| 2 | pk_t_iscb_import_file_input |  | fentryid |

---

## 数据导入方案-主表 t_iscb_import_file

- **表名称：** 数据导入方案-主表
- **表名：** t_iscb_import_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 4 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 5 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: json :Json 对象格式(*.json) xlsx :Excel 工作簿(*.xlsx) xls :Excel 97-2003 工作簿(*.xls) csv :CSV 逗号分隔值(*.csv) |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 9 | fimport_target | 导入对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 13 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fproxy_user | 代理用户 | varchar | 50 |  | √ | ' ' | 代理用户 |
| 15 | fmode | 模式 | varchar | 50 |  | √ | ' ' | 模式,枚举: RequiresTransaction :单个事务 BreakOnError :错误时中止 ResumeOnError :错误时忽略 |
| 16 | fimport_target_type | 迁入对象类别 | varchar | 50 |  | √ | ' ' | 迁入对象类别,枚举: isc_metadata_schema :集成对象 isc_data_copy_trigger :启动方案 isc_service_flow :服务流程 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | ftarget_script_tag | 导入数据处理脚本_详情 | text | 0 |  |  | null | 导入数据处理脚本_详情 |
| 19 | ftarget_script | 导入数据处理脚本 | varchar | 255 |  | √ | ' ' | 导入数据处理脚本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_import_file_m |  | fmodifydate |
| 2 | pk_t_iscb_import_file |  | fid |
| 3 | idx_iscb_import_file |  | fgroupid |

---

## 目标单操作分录-子表 t_iscb_import_file_act

- **表名称：** 目标单操作分录-子表
- **表名：** t_iscb_import_file_act

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | ftar_action_label | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称,枚举: |
| 4 | ftar_action_type | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: save :新增+修改 delete :删除 insert :新增 update :修改 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftar_action_number | 操作编码 | varchar | 50 |  | √ | ' ' | 操作编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_import_file_act |  | fentryid |
| 2 | idx_isc_import_file_act_fk |  | fid |
