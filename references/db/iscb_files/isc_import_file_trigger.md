# 数据导入任务-isc_import_file_trigger

## 数据导入任务-主表 t_iscb_import_trigger

- **表名称：** 数据导入任务-主表
- **表名：** t_iscb_import_trigger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 4 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: json :Json 对象格式(*.json) xlsx :Excel 工作簿(*.xlsx) |
| 5 | fbatch_size | 目标单批量大小 | int4 | 32 |  | √ | 0 | 目标单批量大小 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | ffileschema | 数据导入方案 | int8 | 64 |  | √ | 0 | 数据导入方案 isc_import_file |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftrace_all | 保存全部日志 | bpchar | 1 |  | √ | ' ' | 保存全部日志 |
| 12 | ftype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型,枚举: auto :定时启动 manual :人工启动 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_import_trigger |  | ffileschema |
| 2 | idx_import_trigger_m |  | fmodifydate |
| 3 | pk_t_iscb_import_trigger |  | fid |
