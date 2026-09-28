# 归档错误日志-aef_errorlog

## 归档错误日志-主表 t_aef_errorlog

- **表名称：** 归档错误日志-主表
- **表名：** t_aef_errorlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorinfo | 错误信息 | varchar | 500 |  | √ | ' ' | 错误信息 |
| 3 | ftraceid | traceId | varchar | 50 |  | √ | ' ' | traceId |
| 4 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :归档 2 :反归档 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreattime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fschemeid | 归档方案 | int8 | 64 |  | √ | 0 | [归档方案 aef_archivescheme](../aef_files/aef_archivescheme.md) |
| 8 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 9 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aef_error_log |  | fid |
| 2 | idx_aef_erroelog_c |  | fcreattime |
