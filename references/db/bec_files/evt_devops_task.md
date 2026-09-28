# 运维任务表-evt_devops_task

## 运维任务表-主表 t_evt_devopstask

- **表名称：** 运维任务表-主表
- **表名：** t_evt_devopstask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 参数 | varchar | 500 |  | √ | ' ' | 参数 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型,枚举: 1 :挂起 2 :解挂 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsubscriptionid | 订阅id | int8 | 64 |  | √ | 0 | 订阅id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_devopstask_createdate |  | fcreatedate |
| 2 | pk_evt_devopstask |  | fid |
