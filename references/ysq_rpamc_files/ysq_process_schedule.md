# 调度-ysq_process_schedule

## 调度-主表 tk_ysq_process_schedule

- **表名称：** 调度-主表
- **表名：** tk_ysq_process_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 3 | fk_ysq_fail_try_times | 失败重试次数 | int8 | 64 |  |  | null | 失败重试次数 |
| 4 | fk_ysq_schedule_expre | 调度表达式 | varchar | 2000 |  | √ | ' ' | 调度表达式 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fk_ysq_end_time | 调度失效时间 | timestamp | 0 |  |  | null | 调度失效时间 |
| 7 | fk_ysq_calendar_fid | 日历编号 | int8 | 64 |  |  | null | 日历编号 |
| 8 | fk_ysq_exec_robots_names | 候选机器人主机名 | varchar | 255 |  | √ | ' ' | 候选机器人主机名 |
| 9 | fk_ysq_next_exe_time | 下次执行时间 | timestamp | 0 |  |  | null | 下次执行时间 |
| 10 | fk_ysq_schedule_time | 调度时间 | varchar | 32 |  | √ | ' ' | 调度时间 |
| 11 | fk_ysq_hand_do_min | 人工执行耗时（分钟） | int8 | 64 |  |  | null | 人工执行耗时（分钟） |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fk_ysq_robots_sel | 候选机器人 | varchar | 2000 |  | √ | ' ' | 候选机器人,枚举: |
| 14 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fk_ysq_exec_robots_no_tag | 候选机器人信息_详情 | text | 0 |  |  | null | 候选机器人信息_详情 |
| 17 | fk_ysq_start_time | 调度生效时间 | timestamp | 0 |  |  | null | 调度生效时间 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fk_ysq_script | 执行模式 | varchar | 50 |  | √ | ' ' | 执行模式,枚举: everyday :每日执行 workday :工作日执行 no_workday :非工作日 |
| 20 | fk_ysq_proc_fid | 流程ID | int8 | 64 |  |  | null | 流程ID |
| 21 | fk_ysq_schedule_command | 调度命令 | varchar | 512 |  | √ | ' ' | 调度命令 |
| 22 | fk_ysq_fk_ysq_proc_ver | fk_ysq_fk_ysq_proc_ver | varchar | 50 |  | √ | ' ' |  |
| 23 | fk_ysq_dev_user_fid | 开发者ID | int8 | 64 |  |  | null | 开发者ID |
| 24 | fk_ysq_sch_type | 调度类型 | varchar | 50 |  | √ | 'common' | 调度类型,枚举: common :普通调度 standard :标准应用调度 |
| 25 | fk_ysq_sch_job_nums | 生成任务数 | int8 | 64 |  |  | null | 生成任务数 |
| 26 | fk_ysq_owner_user_fid | 所有者ID | int8 | 64 |  |  | null | 所有者ID |
| 27 | fk_ysq_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: yes :启用 no :停用 |
| 28 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 29 | fk_ysq_studio_ver | 设计器版本 | varchar | 64 |  | √ | ' ' | 设计器版本 |
| 30 | fk_ysq_kd_planid | 调度计划ID | int8 | 64 |  |  | null | 调度计划ID |
| 31 | fk_ysq_proc_ver | 流程版本 | varchar | 64 |  | √ | ' ' | 流程版本,枚举: |
| 32 | fk_ysq_proc_name | 流程名称 | varchar | 64 |  | √ | ' ' | 流程名称 |
| 33 | fk_ysq_priority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :紧急 middle :普通 low :低级 |
| 34 | fk_ysq_pending_timeout | 等待超时时间 | int8 | 64 |  |  | null | 等待超时时间 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 36 | fk_ysq_app_run_type | 启动运行方式 | varchar | 50 |  |  | '3' | 启动运行方式 |
| 37 | fk_ysq_sch_param | 调度参数 | varchar | 255 |  | √ | ' ' | 调度参数 |
| 38 | fk_ysq_exec_robots_names_tag | 候选机器人主机名_详情 | text | 0 |  |  | null | 候选机器人主机名_详情 |
| 39 | fk_ysq_sch_expre_desc | 调度信息 | varchar | 254 |  | √ | ' ' | 调度信息 |
| 40 | fk_ysq_auto_stop_time | 自动停止时长（分钟） | int8 | 64 |  |  | null | 自动停止时长（分钟） |
| 41 | fk_ysq_sch_param_tag | 调度参数_详情 | text | 0 |  |  | null | 调度参数_详情 |
| 42 | fk_ysq_proc_code | 流程 | varchar | 50 |  | √ | ' ' | 流程,枚举: |
| 43 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 44 | fk_ysq_kd_jobid | 调度作业ID | int8 | 64 |  |  | null | 调度作业ID |
| 45 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 46 | fk_ysq_schedule_mode | 调度模式 | varchar | 50 |  | √ | ' ' | 调度模式,枚举: min :分钟 hour :小时 day :天 week :星期 month :月 cron :自定义 |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fk_ysq_exec_robots_no_sel | 待运行机器人 | varchar | 50 |  | √ | ' ' | 待运行机器人,枚举: -deptall- :部门机器人 2 :候选机器人 |
| 49 | fk_ysq_sch_name | 调度名称 | varchar | 64 |  | √ | ' ' | 调度名称 |
| 50 | fk_ysq_exec_robots_alias | 候选机器人别名 | varchar | 2000 |  | √ | ' ' | 候选机器人别名 |
| 51 | fk_ysq_start_reissue | 是否启动补发任务 | varchar | 50 |  | √ | ' ' | 是否启动补发任务,枚举: yes :是 no :否 |
| 52 | fk_ysq_running_timeout | 运行超时时间 | int8 | 64 |  |  | null | 运行超时时间 |
| 53 | fk_ysq_exec_robots_no | 候选机器人信息 | varchar | 255 |  | √ | ' ' | 候选机器人信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_process_schedule |  | fid |
| 2 | idx_tk_ysq_process_schedule_code_0 |  | fk_ysq_proc_code |

---

## 调度-多语言表 tk_ysq_process_schedule_l

- **表名称：** 调度-多语言表
- **表名：** tk_ysq_process_schedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 3 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 4 | fk_ysq_exec_robots_alias | 候选机器人别名 | varchar | 2000 |  | √ | ' ' | 候选机器人别名 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fk_ysq_proc_name | 流程名称 | varchar | 64 |  | √ | ' ' | 流程名称 |
| 7 | fk_ysq_sch_name | 调度名称 | varchar | 64 |  | √ | ' ' | 调度名称 |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 9 | fk_ysq_sch_expre_desc | 调度信息 | varchar | 254 |  | √ | ' ' | 调度信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_process_schedule_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_process_schedule_l |  | fpkid |
