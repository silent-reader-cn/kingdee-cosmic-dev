# 同步任务-plm_sm_tasks

## 同步任务-主表 t_plmsm_tasks

- **表名称：** 同步任务-主表
- **表名：** t_plmsm_tasks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 代理任务id | int8 | 64 |  | √ | 0 | 代理任务id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 修改人 |
| 4 | fparentid | 父任务id | int8 | 64 |  | √ | 0 | 父任务id |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 6 | fneedmessage | fneedmessage | int4 | 32 |  | √ | 0 |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 8 | fstatus | 任务状态 | int4 | 32 |  | √ | 1 | 任务状态 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 创建人 |
| 10 | fnumber | 任务标志key | varchar | 100 |  | √ | ' ' | 任务标志key |
| 11 | fdesc | 任务描述 | varchar | 1024 |  | √ | ' ' | 任务描述 |
| 12 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 13 | fsendmessage | 是否需要发送消息 | int4 | 32 |  | √ | 0 | 是否需要发送消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_plm_sm_tasks |  | fnumber,ftaskid |
| 2 | pk_t_plmsm_tasks |  | fid |
