# 归档子任务-bos_cbs_archi_subtask

## 归档子任务-主表 t_cbs_archi_subtask

- **表名称：** 归档子任务-主表
- **表名：** t_cbs_archi_subtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmvtable | 子任务迁移表 | varchar | 50 |  | √ | ' ' | 子任务迁移表 |
| 3 | ftasktype | 任务类型 | varchar | 100 |  | √ | ' ' | 任务类型,枚举: same :同库迁移 cross :跨库迁移 clean :数据清理 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 6 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态 |
| 7 | fentitynumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 8 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 10 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_subtask_tid |  | ftaskid |
| 2 | pk_cbs_archi_subtask |  | fid |
| 3 | idx_cbs_archi_subtask |  | fentitynumber |
