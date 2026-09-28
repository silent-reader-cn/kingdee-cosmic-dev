# 服务流程实例-isc_sf_proc_inst

## 服务流程实例-主表 t_isc_sf_proc_inst

- **表名称：** 服务流程实例-主表
- **表名：** t_isc_sf_proc_inst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 发起人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ferror_message | 失败日志 | varchar | 250 |  | √ | ' ' | 失败日志 |
| 4 | fcontext | 运行时上下文 | varchar | 255 |  | √ | ' ' | 运行时上下文 |
| 5 | fparent_proc_id | 父流程实例ID | int8 | 64 |  | √ | 0 | 父流程实例ID |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fparent_execution_id | 父流程执行节点ID | varchar | 50 |  | √ | ' ' | 父流程执行节点ID |
| 8 | fcontext_tag | 运行时上下文_详情 | text | 0 |  |  | null | 运行时上下文_详情 |
| 9 | fparent_execution_name | 父流程执行节点名称 | varchar | 50 |  | √ | ' ' | 父流程执行节点名称 |
| 10 | fcreated_time | 发起时间 | timestamp | 0 |  |  | null | 发起时间 |
| 11 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: Created :新建 Waiting :等待中 Running :执行中 Failed :已失败 Complete :已结束 Terminated :已撤销 Ignored :已忽略 Interrupted :中断 |
| 12 | fmodified_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fexec_time | 执行耗时(毫秒) | int4 | 32 |  | √ | 0 | 执行耗时(毫秒) |
| 14 | freleased_flow | 服务流程 | int8 | 64 |  | √ | 0 | 服务流程（已发布） isc_service_flow_r |
| 15 | fcontext_length | 上下文长度 | int4 | 32 |  | √ | 0 | 上下文长度 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fserver_instance | 服务器实例ID | varchar | 50 |  | √ | ' ' | 服务器实例ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_isc_sf_proc_inst_n |  | fnumber |
| 2 | idx_t_isc_sf_proc_inst_m |  | fmodified_time |
| 3 | idx_t_isc_sf_proc_inst_x |  | freleased_flow |
| 4 | t_isc_sf_proc_inst_pkey |  | fid |
| 5 | idx_t_isc_sf_proc_inst_t |  | fcreated_time |
| 6 | idx_t_isc_sf_proc_inst_s |  | fstate |
