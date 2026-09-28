# 数据导出任务-isc_export_file_trigger

## 执行参数-子表 t_iscb_ex_trigger_params

- **表名称：** 执行参数-子表
- **表名：** t_iscb_ex_trigger_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparams_value | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 3 | fparams_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fparams_data_type | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparams_label | 标题 | varchar | 100 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_ex_trigger_params |  | fentryid |

---

## 数据导出任务-主表 t_iscb_export_trigger

- **表名称：** 数据导出任务-主表
- **表名：** t_iscb_export_trigger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcompress | 是否压缩 | bpchar | 1 |  | √ | ' ' | 是否压缩 |
| 4 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 5 | ffiletype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: json :Json 对象格式·(*.json) xlsx :Excel 工作簿(*.xlsx) |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | ffileschema | 导出方案 | int8 | 64 |  | √ | 0 | [数据导出方案 isc_export_file](../iscb_files/isc_export_file.md) |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftype | 任务类型 | varchar | 30 |  | √ | ' ' | 任务类型,枚举: auto :定时启动 manual :人工启动 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 14 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | ffilesize | 文件大小（M） | int4 | 32 |  | √ | 0 | 文件大小（M） |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_export_trigger |  | fid |
| 2 | idx_iscb_export_trigger |  | ffileschema |
| 3 | idx_export_trigger_m |  | fmodifydate |
