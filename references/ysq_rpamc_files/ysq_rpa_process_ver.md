# 流程版本信息-ysq_rpa_process_ver

## 流程版本信息-多语言表 tk_ysq_rpa_process_ver_l

- **表名称：** 流程版本信息-多语言表
- **表名：** tk_ysq_rpa_process_ver_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 3 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 4 | fk_ysq_ver_explain | 版本说明 | varchar | 2000 |  | √ | ' ' | 版本说明 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fk_ysq_proc_desc | 流程版本描述 | varchar | 254 |  | √ | ' ' | 流程版本描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_rpa_process_ver_l |  | fpkid |
| 2 | idx__ysq_rpa_process_ver_l_0 |  | fid,flocaleid |

---

## 流程版本信息-主表 tk_ysq_rpa_process_ver

- **表名称：** 流程版本信息-主表
- **表名：** tk_ysq_rpa_process_ver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_ysq_studio_ver | 设计器版本 | varchar | 64 |  | √ | ' ' | 设计器版本 |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 4 | fk_ysq_publish_time | 版本发布时间 | timestamp | 0 |  |  | null | 版本发布时间 |
| 5 | fk_ysq_ver_explain | 版本说明 | varchar | 2000 |  | √ | ' ' | 版本说明 |
| 6 | fk_ysq_proc_ver | 流程版本号 | varchar | 64 |  | √ | ' ' | 流程版本号 |
| 7 | fk_ysq_param_tag | 运行参数模板_详情 | text | 0 |  |  | null | 运行参数模板_详情 |
| 8 | fk_ysq_proc_name | 流程名称 | varchar | 64 |  | √ | ' ' | 流程名称 |
| 9 | fk_ysq_status_ctime | 状态修改时间 | timestamp | 0 |  |  | null | 状态修改时间 |
| 10 | fk_ysq_proc_desc | 流程版本描述 | varchar | 254 |  | √ | ' ' | 流程版本描述 |
| 11 | fk_ysq_pro_run_info | 运行次数 | varchar | 50 |  | √ | ' ' | 运行次数 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fk_ysq_dispatch_time | 调度数 | int8 | 64 |  |  | null | 调度数 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fk_ysq_proc_file | 流程文件路径 | varchar | 2000 |  | √ | ' ' | 流程文件路径 |
| 16 | fk_ysq_param | 运行参数模板 | varchar | 255 |  | √ | ' ' | 运行参数模板 |
| 17 | fk_ysq_file_size | 文件大小 | int8 | 64 |  |  | null | 文件大小 |
| 18 | fk_ysq_textfield | 是否是应用机器人 | varchar | 50 |  | √ | ' ' | 是否是应用机器人 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fk_ysq_proc_code | 流程编号 | varchar | 32 |  | √ | ' ' | 流程编号 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 22 | fk_ysq_dev_user_alias | 开发者用户名 | varchar | 512 |  | √ | ' ' | 开发者用户名 |
| 23 | fk_ysq_run_times | 任务运行次数 | int8 | 64 |  |  | null | 任务运行次数 |
| 24 | fk_ysq_owner_user_alias | 所有者名称 | varchar | 512 |  | √ | ' ' | 所有者名称 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fk_ysq_work_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: edit :编辑中 pre_release :待发布 release :已发布 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fk_ysq_pro_change | 流程版本修改时间 | varchar | 64 |  | √ | ' ' | 流程版本修改时间 |
| 30 | fk_ysq_proc_fid | 流程ID | int8 | 64 |  |  | null | 流程ID |
| 31 | fk_ysq_fail_times | 运行失败次数 | int8 | 64 |  |  | null | 运行失败次数 |
| 32 | fk_ysq_is_activity | 是否活动 | varchar | 50 |  | √ | ' ' | 是否活动,枚举: yes :是 no :否 |
| 33 | fk_ysq_dev_user_fid | 开发者ID | int8 | 64 |  |  | null | 开发者ID |
| 34 | fk_ysq_owner_user_fid | 所有者ID | int8 | 64 |  |  | null | 所有者ID |
| 35 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_ysq_rpa_process_ver_proc_ver_0 |  | fk_ysq_proc_ver |
| 2 | idx_tk_ysq_rpa_process_ver_code_ver_0 |  | fk_ysq_proc_code,fk_ysq_proc_ver |
| 3 | pk_tk_ysq_rpa_process_ver |  | fid |
| 4 | idx_tk_ysq_rpa_process_ver_proc_code_0 |  | fk_ysq_proc_code |
