# 单据操作基础资料-task_operationbase

## 单据操作基础资料-主表 t_tk_operationentry

- **表名称：** 单据操作基础资料-主表
- **表名：** t_tk_operationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 3 | foperationname | 操作名称 | varchar | 80 |  | √ | ' ' | 操作名称 |
| 4 | foperationnumber | 操作码 | varchar | 80 |  | √ | ' ' | 操作码 |
| 5 | fentryid | entryid | int8 | 64 |  | √ | 0 | entryid |
| 6 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_operationentry |  | fid |
| 2 | t_tk_operationentry_pkey |  | fentryid |
