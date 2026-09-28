# 往来数据修复日志-gl_reci_datarepair_log

## 往来数据修复日志-主表 t_gl_reci_datarepair_log

- **表名称：** 往来数据修复日志-主表
- **表名：** t_gl_reci_datarepair_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 修复状态 | int4 | 32 |  | √ | 0 | 修复状态 |
| 3 | fbackuptable | 备份数据库名称 | varchar | 50 |  | √ | ' ' | 备份数据库名称 |
| 4 | fmessage | 多行文本 | varchar | 2000 |  |  | ' ' | 多行文本 |
| 5 | fmodeltype | 模块类型 | int4 | 32 |  | √ | 0 | 模块类型 |
| 6 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | foperateuserid | 操作人 | int8 | 64 |  | √ | 0 | 操作人 |
| 8 | fchecktype | 修复类型 | int4 | 32 |  | √ | 0 | 修复类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_reci_datarepair_log |  | fchecktype |
| 2 | pk_t_gl_reci_datarepair_log |  | fid |
