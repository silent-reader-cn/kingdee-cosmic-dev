# 数据项-ysq_rpa_queues_items

## 数据项-主表 tk_ysq_rpa_queues_items

- **表名称：** 数据项-主表
- **表名：** tk_ysq_rpa_queues_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_custom_field_tag | 自定义字段_详情 | text | 0 |  |  | null | 自定义字段_详情 |
| 3 | fk_ysq_sourceid | 数据空间编号 | int8 | 64 |  |  | null | 数据空间编号 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 5 | fk_ysq_item_no | 数据项编号 | varchar | 64 |  |  | NULL | 数据项编号 |
| 6 | fk_ysq_fail_try_times | 重试次数 | int8 | 64 |  |  | null | 重试次数 |
| 7 | fk_ysq_agent_no | 终端编号 | varchar | 64 |  |  | NULL | 终端编号 |
| 8 | fk_ysq_proc_name | 流程名称 | varchar | 254 |  |  | NULL | 流程名称 |
| 9 | fk_ysq_priority | 优先级 | varchar | 50 |  |  | NULL | 优先级,枚举: high :高 normal :中 low :低 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_ysq_queue_name | 数据空间名称 | varchar | 254 |  |  | NULL | 数据空间名称 |
| 12 | fk_ysq_end_time | 队列项执行结束时间 | timestamp | 0 |  |  | null | 队列项执行结束时间 |
| 13 | fk_ysq_org_code | org_code | int8 | 64 |  |  | null | org_code |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fk_ysq_faildesc | 失败描述 | varchar | 255 |  |  | NULL | 失败描述 |
| 16 | fk_ysq_queue_max_items | 队列最大值 | int8 | 64 |  |  | null | 队列最大值 |
| 17 | fk_ysq_agent_type | 终端类型 | varchar | 50 |  |  | NULL | 终端类型,枚举: robot :无人值守机器人 studio :设计器 assistant :有人值守机器人 standardRobot :应用机器人 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fk_ysq_proc_code | 流程编号 | varchar | 64 |  |  | NULL | 流程编号 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | fk_ysq_run_times | 运行次数 | int8 | 64 |  |  | null | 运行次数 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fk_ysq_start_time | 队列项执行开始时间 | timestamp | 0 |  |  | null | 队列项执行开始时间 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fk_ysq_job_no | 任务编号 | varchar | 64 |  |  | NULL | 任务编号 |
| 27 | fk_ysq_faildesc_tag | 失败描述_详情 | text | 0 |  |  | null | 失败描述_详情 |
| 28 | fk_ysq_robot_no | 机器人编号 | varchar | 64 |  |  | NULL | 机器人编号 |
| 29 | fk_ysq_custom_field | 自定义字段 | varchar | 255 |  |  | NULL | 自定义字段 |
| 30 | fk_ysq_deadline_null | ysq_deadline_null | int8 | 64 |  |  | null | ysq_deadline_null |
| 31 | fk_ysq_agent_alias | 终端别名 | varchar | 254 |  |  | NULL | 终端别名 |
| 32 | fk_ysq_deadline | 超时时间 | timestamp | 0 |  |  | null | 超时时间 |
| 33 | fk_ysq_status | 状态 | varchar | 50 |  |  | NULL | 状态,枚举: pending :等待运行 waittimeout :等待超时 running :正在运行 success :运行成功 failed :运行失败 retry :重新运行 deleted :已删除 |
| 34 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_queues_items |  | fid |
