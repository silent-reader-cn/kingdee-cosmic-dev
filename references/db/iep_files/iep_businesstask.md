# 智能核算业务单据任务-iep_businesstask

## 智能核算业务单据任务-主表 t_gl_businesstask

- **表名称：** 智能核算业务单据任务-主表
- **表名：** t_gl_businesstask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foper | 操作 | varchar | 36 |  | √ | ' ' | 操作 |
| 3 | fentityid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 4 | fbusiness | 业务单据 | varchar | 36 |  | √ | ' ' | 业务单据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_businesstask_pkey |  | fid |
| 2 | idx_gl_businesstask |  | fbusiness,foper,fentityid |
| 3 | idx_gl_businesstask_entityid |  | fentityid |
