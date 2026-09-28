# 归档任务日志-bos_cbs_archi_log

## 归档任务日志-主表 t_cbs_archi_log

- **表名称：** 归档任务日志-主表
- **表名：** t_cbs_archi_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprogresstype | 操作类型 | varchar | 100 |  | √ | ' ' | 操作类型 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fentitynumber | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 5 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 6 | foperationlog | 日志 | varchar | 2000 |  | √ | ' ' | 日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_log |  | fentitynumber |
| 2 | pk_cbs_archi_log |  | fid |
