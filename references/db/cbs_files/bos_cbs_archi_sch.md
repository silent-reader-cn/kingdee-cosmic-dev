# 归档调度计划安排-bos_cbs_archi_sch

## 调度消息通知表-子表 t_sch_schedule_m

- **表名称：** 调度消息通知表-子表
- **表名：** t_sch_schedule_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fsmsgcontent | 消息内容 | varchar | 500 |  | √ | ' ' | 消息内容 |
| 3 | fsnotifytype | 消息渠道 | varchar | 100 |  | √ | ' ' | 消息渠道,枚举: |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmsgtype | 消息类型 | varchar | 200 |  | √ | ' ' | 消息类型,枚举: COMPLETED :成功 FAILED :失败 TIMEOUT :超时 ABORTED :终止 |
| 6 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_schedule_m_fk |  | fid |
| 2 | pk_t_sch_schedule_m |  | fentryid |

---

## 归档调度计划安排-主表 t_cbs_archi_sch

- **表名称：** 归档调度计划安排-主表
- **表名：** t_cbs_archi_sch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fhost | host | varchar | 50 |  | √ | ' ' | host |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frepeatmode | 重复时间单位 | varchar | 50 |  | √ | ' ' | 重复时间单位,枚举: n :不重复 mi :分钟 h :小时 d :天 w :星期 m :月 y :年 def :自定义 |
| 7 | fschplanid | 调度计划编码 | varchar | 50 |  | √ | ' ' | 调度计划编码 |
| 8 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fnumber | 计划编码 | varchar | 50 |  | √ | ' ' | 计划编码 |
| 13 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 14 | fdesc | 调度计划示例 | varchar | 2000 |  | √ | ' ' | 调度计划示例 |
| 15 | fcyclenum | 重复周期 | int8 | 64 |  | √ | 0 | 重复周期 |
| 16 | fplan | cron表达式 | varchar | 50 |  | √ | ' ' | cron表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_archi_sch |  | fid |
| 2 | idx_cbs_archi_sch_1 |  | fschplanid |

---

## 消息接收人-多选基础资料表 t_sch_schmsgreceiver

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_sch_schmsgreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sch_schmsgreceiver |  | fpkid |
| 2 | idx_sch_schmsgreceiver_fk |  | fentryid |

---

## 调度作业-子表 t_sch_schedule_entry

- **表名称：** 调度作业-子表
- **表名：** t_sch_schedule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fjobnumber | 作业编码 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sch_schedule_entry |  | fentryid |
| 2 | idx_sch_scdentry_fid |  | fid |
| 3 | idx_sch_scdentry_number |  | fjobnumber |

---

## 归档调度计划安排-分表 t_cbs_archi_sch_n

- **表名称：** 归档调度计划安排-分表
- **表名：** t_cbs_archi_sch_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fmsgreceiver | 消息接收人（单选） | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fssuccessnotify | 成功 | bpchar | 1 |  | √ | '0' | 成功 |
| 4 | fsmsgcontent | 消息内容 | varchar | 900 |  | √ | ' ' | 消息内容 |
| 5 | fsnotifytype | 消息渠道 | varchar | 50 |  | √ | ' ' | 消息渠道,枚举: |
| 6 | fsaborted | 终止 | bpchar | 1 |  | √ | '0' | 终止 |
| 7 | fschprincipal | 计划负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsfailnotify | 失败 | bpchar | 1 |  | √ | '0' | 失败 |
| 9 | fstimeout | 超时 | bpchar | 1 |  | √ | '0' | 超时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_sch_n |  | fschprincipal |
| 2 | pk_t_cbs_archi_sch_n |  | fid |
