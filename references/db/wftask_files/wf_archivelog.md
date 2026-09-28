# 归档调度日志-wf_archivelog

## 归档调度日志-主表 t_msg_archivelog

- **表名称：** 归档调度日志-主表
- **表名：** t_msg_archivelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchiveserviceid | 归档服务ID | int8 | 64 |  | √ | 0 | 归档服务ID |
| 3 | ftargetdate | 父单据调度游标时间 | timestamp | 0 |  |  | null | 父单据调度游标时间 |
| 4 | fparententity | 父实体编码 | varchar | 100 |  | √ | ' ' | 父实体编码 |
| 5 | fentity | 实体编码 | varchar | 100 |  | √ | ' ' | 实体编码 |
| 6 | fstate | 状态 | varchar | 100 |  | √ | ' ' | 状态,枚举: success :成功 failed :失败 |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fscheduleid | 调度ID | int8 | 64 |  | √ | 0 | 调度ID |
| 9 | farchiveservice | 归档服务编码 | varchar | 100 |  | √ | ' ' | 归档服务编码 |
| 10 | fresourceids | 资源ID集合 | text | 0 |  |  | null | 资源ID集合 |
| 11 | fschstartdate | 调度开始时间 | timestamp | 0 |  |  | null | 调度开始时间 |
| 12 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 13 | fsummary | 调度迁移量 | int4 | 32 |  | √ | 0 | 调度迁移量 |
| 14 | fschenddate | 调度结束时间 | timestamp | 0 |  |  | null | 调度结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_archivelog_archiveid |  | farchiveserviceid |
| 2 | idx_msg_archivelog_schedule |  | fscheduleid |
| 3 | idx_msg_archivelog_taskid |  | ftaskid |
| 4 | pk_t_msg_archivelog |  | fid |
| 5 | idx_msg_archivelog_entity |  | fentity |
