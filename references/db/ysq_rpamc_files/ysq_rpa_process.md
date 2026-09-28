# 流程-ysq_rpa_process

## 流程-多语言表 tk_ysq_rpa_process_l

- **表名称：** 流程-多语言表
- **表名：** tk_ysq_rpa_process_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 3 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fk_ysq_proc_name | 流程名 | varchar | 64 |  | √ | ' ' | 流程名 |
| 6 | fk_ysq_proc_desc | 流程描述信息 | varchar | 254 |  | √ | ' ' | 流程描述信息 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__ysq_rpa_process_l_0 |  | fid,flocaleid |
| 2 | pk_tk_ysq_rpa_process_l |  | fpkid |

---

## 流程-主表 tk_ysq_rpa_process

- **表名称：** 流程-主表
- **表名：** tk_ysq_rpa_process

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_studio_ver | 设计器版本 | varchar | 64 |  | √ | ' ' | 设计器版本 |
| 3 | fk_ysq_version_count | 版本数 | int8 | 64 |  |  | null | 版本数 |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 5 | fk_ysq_publish_time | 流程发布时间 | timestamp | 0 |  |  | null | 流程发布时间 |
| 6 | fk_ysq_fail_try_times | 失败重试次数 | int8 | 64 |  |  | null | 失败重试次数 |
| 7 | fk_ysq_proc_ver | 流程版本 | varchar | 64 |  | √ | ' ' | 流程版本 |
| 8 | fk_ysq_param_tag | ysq_param_详情 | text | 0 |  |  | null | ysq_param_详情 |
| 9 | fk_ysq_status_ctime | 状态上次修改时间 | timestamp | 0 |  |  | null | 状态上次修改时间 |
| 10 | fk_ysq_proc_name | 流程名 | varchar | 64 |  | √ | ' ' | 流程名 |
| 11 | fk_ysq_proc_desc | 流程描述信息 | varchar | 254 |  | √ | ' ' | 流程描述信息 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fk_ysq_dispatch_time | 调度数 | int8 | 64 |  |  | null | 调度数 |
| 14 | fk_ysq_pending_timeout | 等待超时时间，分钟 | int8 | 64 |  |  | null | 等待超时时间，分钟 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fk_ysq_proc_file | 流程文件 | varchar | 2000 |  | √ | ' ' | 流程文件 |
| 17 | fk_ysq_key_words | 关键字(多个用空格) | varchar | 254 |  | √ | ' ' | 关键字(多个用空格) |
| 18 | fk_ysq_param | ysq_param | varchar | 255 |  | √ | ' ' | ysq_param |
| 19 | fk_ysq_hand_do_min | 人工执行耗时，分钟 | int8 | 64 |  |  | null | 人工执行耗时，分钟 |
| 20 | fk_ysq_auto_stop_time | 自动停止时长，分钟 | int8 | 64 |  |  | null | 自动停止时长，分钟 |
| 21 | fk_ysq_proc_type | 流程类型 | varchar | 50 |  | √ | 'common' | 流程类型,枚举: common :普通 standard :标准 |
| 22 | fbillno | 流程单据编号 | varchar | 32 |  | √ | ' ' | 流程单据编号 |
| 23 | fk_ysq_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 25 | fk_ysq_run_times | 任务运行次数 | int8 | 64 |  |  | null | 任务运行次数 |
| 26 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 27 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fk_ysq_work_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: edit :编辑中 pre_release :待发布 release :已发布 |
| 31 | fk_ysq_is_assistant | 是否开启助手 | bpchar | 1 |  | √ | '1' | 是否开启助手 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fk_ysq_pro_change | ysq_pro_change | varchar | 64 |  | √ | ' ' | ysq_pro_change |
| 34 | fk_ysq_is_start_up |  | bpchar | 1 |  | √ | '0' |  |
| 35 | fk_ysq_fail_times | 运行失败次数 | int8 | 64 |  |  | null | 运行失败次数 |
| 36 | fk_ysq_running_timeout | 运行超时时间，分钟 | int8 | 64 |  |  | null | 运行超时时间，分钟 |
| 37 | fk_ysq_dev_user_fid | 开发者ID | int8 | 64 |  |  | null | 开发者ID |
| 38 | fk_ysq_owner_user_fid | 所有者id | int8 | 64 |  |  | null | 所有者id |
| 39 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_ysq_rpa_process_code_0 |  | fk_ysq_proc_code |
| 2 | pk_tk_ysq_rpa_process |  | fid |
