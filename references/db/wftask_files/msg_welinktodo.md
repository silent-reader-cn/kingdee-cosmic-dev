# welink待办-msg_welinktodo

## welink待办-主表 t_msg_welinktodo

- **表名称：** welink待办-主表
- **表名：** t_msg_welinktodo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | 应用秘钥 | varchar | 200 |  | √ | ' ' | 应用秘钥 |
| 3 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 4 | fresult | 待办结果 | varchar | 50 |  | √ | ' ' | 待办结果 |
| 5 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 6 | fretries | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 7 | fappid | 应用ID | varchar | 100 |  | √ | ' ' | 应用ID |
| 8 | fstate | 待办状态 | varchar | 50 |  | √ | ' ' | 待办状态 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fopenid | welink用户ID | varchar | 100 |  | √ | ' ' | welink用户ID |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcorpid | 企业ID | varchar | 200 |  | √ | ' ' | 企业ID |
| 13 | fappname | 应用名称 | varchar | 200 |  | √ | ' ' | 应用名称 |
| 14 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_welinktodo_pkey |  | fid |
| 2 | idx_msg_welinktodo_taskuser |  | ftaskid,fuserid |
