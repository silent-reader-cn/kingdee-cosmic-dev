# 任务管理-ysq_rpa_job

## 任务管理-主表 tk_ysq_rpa_job

- **表名称：** 任务管理-主表
- **表名：** tk_ysq_rpa_job

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_ysq_publish_time | 流程发布时间 | timestamp | 0 |  |  | null | 流程发布时间 |
| 4 | fk_ysq_parameter | 调度参数 | varchar | 255 |  | √ | ' ' | 调度参数 |
| 5 | fk_ysq_fail_try_times | 失败重试次数 | int8 | 64 |  |  | null | 失败重试次数 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fk_ysq_job_time | 产生时间 | timestamp | 0 |  |  | null | 产生时间 |
| 8 | fk_ysq_end_time | 结束运行时间 | timestamp | 0 |  |  | null | 结束运行时间 |
| 9 | fk_ysq_curr_robot_name | 执行机器人 | varchar | 128 |  | √ | ' ' | 执行机器人 |
| 10 | fk_ysq_sch_fid | 任务调度ID | int8 | 64 |  |  | null | 任务调度ID |
| 11 | fk_ysq_wait_time_interval | 等待时段 | varchar | 64 |  | √ | ' ' | 等待时段 |
| 12 | fk_ysq_proc_ver_desc | 流程说明 | varchar | 254 |  | √ | ' ' | 流程说明 |
| 13 | fk_ysq_exec_robots_names | 候选机器人主机名 | varchar | 255 |  | √ | ' ' | 候选机器人主机名 |
| 14 | fk_ysq_schedule_time | 计划时间 | timestamp | 0 |  |  | null | 计划时间 |
| 15 | fk_ysq_identity_desc | 运行者当前身份描述 | varchar | 64 |  | √ | ' ' | 运行者当前身份描述 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fk_ysq_job_type | 运行者 | varchar | 50 |  | √ | ' ' | 运行者,枚举: plan :计划 self :我 other :其他 |
| 18 | fk_ysq_apply_users_fids | 使用者信息 | varchar | 255 |  | √ | ' ' | 使用者信息 |
| 19 | fk_ysq_identity_fid | 运行者当前身份ID | int8 | 64 |  |  | null | 运行者当前身份ID |
| 20 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fk_ysq_wait_times | 等待次数 | int8 | 64 |  |  | null | 等待次数 |
| 23 | fk_ysq_exec_robots_no_tag | 候选机器人信息_详情 | text | 0 |  |  | null | 候选机器人信息_详情 |
| 24 | fk_ysq_apply_users_desc | 使用者描述信息 | varchar | 512 |  | √ | ' ' | 使用者描述信息 |
| 25 | fk_ysq_robot_start_time | 机器人开始时间 | timestamp | 0 |  |  | null | 机器人开始时间 |
| 26 | fk_ysq_start_time | 开始运行时间 | timestamp | 0 |  |  | null | 开始运行时间 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fk_ysq_proc_fid | 流程FID | int8 | 64 |  |  | null | 流程FID |
| 29 | fk_ysq_job_no | 任务编号 | varchar | 64 |  | √ | ' ' | 任务编号 |
| 30 | fk_ysq_wait_nocache_times | 等待无缓存次数 | int8 | 64 |  |  | null | 等待无缓存次数 |
| 31 | fk_ysq_job_order | 任务顺序 | int8 | 64 |  |  | null | 任务顺序 |
| 32 | fk_ysq_dev_user_fid | 开发者ID | int8 | 64 |  |  | null | 开发者ID |
| 33 | fk_ysq_sch_type | 调度类型 | varchar | 50 |  | √ | ' ' | 调度类型,枚举: manager :管理者 unManager :非管理者 |
| 34 | fk_ysq_owner_user_fid | 所有者ID | int8 | 64 |  |  | null | 所有者ID |
| 35 | fk_ysq_status | 运行状态 | varchar | 50 |  | √ | ' ' | 运行状态,枚举: pending :等待运行 running :正在运行 success :运行成功 failed :已失败 stopping :准备停止 stopped :已停止 cancelled :已取消 |
| 36 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fk_ysq_curr_robot_no | 当前执行机器人 | varchar | 128 |  | √ | ' ' | 当前执行机器人 |
| 38 | fk_ysq_result_change_type | 结果修改方式 | varchar | 50 |  | √ | ' ' | 结果修改方式,枚举: CLIENT :客户端修改 SERVER :服务端修改 |
| 39 | fk_ysq_run_time_sec | 运行时长 | int8 | 64 |  |  | null | 运行时长 |
| 40 | fk_ysq_studio_ver | 设计器版本 | varchar | 64 |  | √ | ' ' | 设计器版本 |
| 41 | fk_ysq_proc_hand_do_min | 人工执行耗时 | int8 | 64 |  |  | null | 人工执行耗时 |
| 42 | fk_ysq_proc_ver | 流程版本 | varchar | 64 |  | √ | ' ' | 流程版本 |
| 43 | fk_ysq_proc_name | 流程名称 | varchar | 64 |  | √ | ' ' | 流程名称 |
| 44 | fk_ysq_priority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :紧急 middle :普通 low :低级 higher :特急 |
| 45 | fk_ysq_pending_timeout | 等待超时时间 | int8 | 64 |  |  | null | 等待超时时间 |
| 46 | fk_ysq_exception_content | 异常内容 | varchar | 255 |  | √ | ' ' | 异常内容 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fk_ysq_produce_type | 产生方式 | varchar | 50 |  | √ | ' ' | 产生方式,枚举: manual_run :手工运行 task_scheduling :任务调度 |
| 49 | fk_ysq_description | 描述 | varchar | 254 |  | √ | ' ' | 描述 |
| 50 | fk_ysq_proc_file | 流程文件 | varchar | 2000 |  | √ | ' ' | 流程文件 |
| 51 | fk_ysq_parameter_tag | 调度参数_详情 | text | 0 |  |  | null | 调度参数_详情 |
| 52 | fk_ysq_exec_robots_names_tag | 候选机器人主机名_详情 | text | 0 |  |  | null | 候选机器人主机名_详情 |
| 53 | fk_ysq_auto_stop_time | 自动停止时长 | int8 | 64 |  |  | null | 自动停止时长 |
| 54 | fk_ysq_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fk_ysq_run_times | 运行次数 | int8 | 64 |  |  | null | 运行次数 |
| 57 | fk_ysq_exception_content_tag | 异常内容_详情 | text | 0 |  |  | null | 异常内容_详情 |
| 58 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 59 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 60 | fk_ysq_work_status | 版本当前状态 | varchar | 50 |  | √ | ' ' | 版本当前状态,枚举: edit :编辑 pre_release :待发布 release :已发布 |
| 61 | fk_ysq_exception_name | 异常名称 | varchar | 2000 |  | √ | ' ' | 异常名称 |
| 62 | fk_ysq_sch_name | 调度名称 | varchar | 64 |  | √ | ' ' | 调度名称 |
| 63 | fk_ysq_com_job_type | 任务类型（标准任务、普通任务） | varchar | 50 |  | √ | 'common' | 任务类型（标准任务、普通任务）,枚举: common :普通 standard :标准 |
| 64 | fk_ysq_robot_end_time | 机器人结束时间 | timestamp | 0 |  |  | null | 机器人结束时间 |
| 65 | fk_ysq_pending_time | 等待时长 | int8 | 64 |  |  | null | 等待时长 |
| 66 | fk_ysq_exec_robots_alias | 候选机器人别名 | varchar | 2000 |  | √ | ' ' | 候选机器人别名 |
| 67 | fk_ysq_running_timeout | 运行超时时间 | int8 | 64 |  |  | null | 运行超时时间 |
| 68 | fk_ysq_file_ref_count | 关联文件数 | int8 | 64 |  |  | null | 关联文件数 |
| 69 | fk_ysq_exec_robots_no | 候选机器人信息 | varchar | 255 |  | √ | ' ' | 候选机器人信息 |
| 70 | fk_ysq_apply_users_fids_tag | 使用者信息_详情 | text | 0 |  |  | null | 使用者信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_ysq_rpa_job_curr_robot_no_0 |  | fk_ysq_curr_robot_no |
| 2 | idx_tk_ysq_rpa_job_job_no_0 |  | fk_ysq_job_no |
| 3 | idx_tk_ysq_rpa_job_procode_0 |  | fk_ysq_proc_code |
| 4 | idx_tk_ysq_rpa_job_org_0 |  | forgid |
| 5 | idx_tk_ysq_rpa_job_sch_name_0 |  | fk_ysq_sch_name |
| 6 | idx_tk_ysq_rpa_job_status_0 |  | fk_ysq_status |
| 7 | pk_tk_ysq_rpa_job |  | fid |
| 8 | idx_tk_ysq_rpa_job_time_0 |  | fk_ysq_job_time |

---

## 任务管理-多语言表 tk_ysq_rpa_job_l

- **表名称：** 任务管理-多语言表
- **表名：** tk_ysq_rpa_job_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 3 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 4 | fk_ysq_exec_robots_alias | 候选机器人别名 | varchar | 2000 |  | √ | ' ' | 候选机器人别名 |
| 5 | fk_ysq_description | 描述 | varchar | 254 |  | √ | ' ' | 描述 |
| 6 | fk_ysq_apply_users_desc | 使用者描述信息 | varchar | 512 |  | √ | ' ' | 使用者描述信息 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fk_ysq_proc_name | 流程名称 | varchar | 64 |  | √ | ' ' | 流程名称 |
| 9 | fk_ysq_sch_name | 调度名称 | varchar | 64 |  | √ | ' ' | 调度名称 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 11 | fk_ysq_identity_desc | 运行者当前身份描述 | varchar | 64 |  | √ | ' ' | 运行者当前身份描述 |
| 12 | fk_ysq_curr_robot_name | 执行机器人 | varchar | 128 |  | √ | ' ' | 执行机器人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_rpa_job_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_rpa_job_l |  | fpkid |
