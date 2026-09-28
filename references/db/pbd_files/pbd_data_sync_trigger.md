# 全文检索数据同步方案-pbd_data_sync_trigger

## 全文检索数据同步方案-主表 t_pbd_data_sync_trigger

- **表名称：** 全文检索数据同步方案-主表
- **表名：** t_pbd_data_sync_trigger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjob_scheduleid | 调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 6 | fhandler | 处理器 | varchar | 255 |  | √ | ' ' | 处理器 |
| 7 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | finterval | 执行频率 | varchar | 10 |  | √ | ' ' | 执行频率,枚举: 1 :执行频率 - 1次/小时 2 :执行频率 - 2次/小时 3 :执行频率 - 3次/小时 5 :执行频率 - 5次/小时 10 :执行频率 - 10次/小时 20 :执行频率 - 20次/小时 30 :执行频率 - 30次/小时 60 :执行频率 - 60次/小时 d :每天 w :每周 m :每月 d1 :每天凌晨一点 0 :自定义 |
| 10 | fexpired_time | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fesconfigid | 全文检索配置 | int8 | 64 |  | √ | 0 | [全文检索配置 pbd_esconfig](../pbd_files/pbd_esconfig.md) |
| 15 | fexe_job_userid | 执行用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fschedule | 触发间隔 | varchar | 50 |  | √ | ' ' | 触发间隔 |
| 17 | ftotal_count | 触发次数 | int8 | 64 |  | √ | 0 | 触发次数 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fvalidated_time | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fevents | 触发事件 | varchar | 100 |  | √ | ' ' | 触发事件,枚举: |
| 22 | ftrigger_type | 启动类型 | varchar | 10 |  | √ | ' ' | 启动类型,枚举: auto :定时启动 manual :人工启动 event :事件触发 message :消息启动 |
| 23 | fjob_defineid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 24 | ftrigged_time | 最近触发时间 | timestamp | 0 |  |  | null | 最近触发时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pbd_data_sync_trigger |  | fid |
| 2 | idx_pbd_trigger_fnumber |  | fnumber |

---

## 全文检索数据同步方案-多语言表 t_pbd_data_sync_trigger_l

- **表名称：** 全文检索数据同步方案-多语言表
- **表名：** t_pbd_data_sync_trigger_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_trigger_l_fid |  | fid |
| 2 | pk_t_pbd_data_sync_trigger_l |  | fpkid |
