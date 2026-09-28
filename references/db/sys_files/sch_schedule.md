# 调度计划-sch_schedule

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

## 调度计划-多语言表 t_sch_schedule_l

- **表名称：** 调度计划-多语言表
- **表名：** t_sch_schedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 计划名称 | varchar | 500 |  | √ | ' ' | 计划名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_scd_l_id |  | fid,flocaleid |
| 2 | t_sch_schedule_l_pkey |  | fpkid |

---

## 调度计划-分表 t_sch_schedule_n

- **表名称：** 调度计划-分表
- **表名：** t_sch_schedule_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fmsgreceiver | 消息接收人（单选） | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fssuccessnotify | 成功 | bpchar | 1 |  | √ | '0' | 成功 |
| 4 | fsmsgcontent | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |
| 5 | fsnotifytype | 消息渠道 | varchar | 300 |  | √ | ' ' | 消息渠道,枚举: |
| 6 | fsaborted | 终止 | bpchar | 1 |  |  | null | 终止 |
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
| 1 | pk_t_sch_schedule_n |  | fid |
| 2 | idx_sch_scd_n |  | fschprincipal |

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

## 调度计划-主表 t_sch_schedule

- **表名称：** 调度计划-主表
- **表名：** t_sch_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fwed | fwed | bpchar | 1 |  |  | '0' |  |
| 3 | ftwentytwo | ftwentytwo | bpchar | 1 |  |  | '0' |  |
| 4 | fbydayorweek | fbydayorweek | varchar | 4 |  |  | null |  |
| 5 | ftues | ftues | bpchar | 1 |  |  | '0' |  |
| 6 | fsep | fsep | bpchar | 1 |  |  | '0' |  |
| 7 | fmar | fmar | bpchar | 1 |  |  | '0' |  |
| 8 | ftwentyseven | ftwentyseven | bpchar | 1 |  |  | '0' |  |
| 9 | ftwentythree | ftwentythree | bpchar | 1 |  |  | '0' |  |
| 10 | fsix | fsix | bpchar | 1 |  |  | '0' |  |
| 11 | fmay | fmay | bpchar | 1 |  |  | '0' |  |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | feleven | feleven | bpchar | 1 |  |  | '0' |  |
| 14 | ffourteen | ffourteen | bpchar | 1 |  |  | '0' |  |
| 15 | ftwelve | ftwelve | bpchar | 1 |  |  | '0' |  |
| 16 | fsun | fsun | bpchar | 1 |  |  | '0' |  |
| 17 | ftwo | ftwo | bpchar | 1 |  |  | '0' |  |
| 18 | ftimezoneid | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 19 | fnineteen | fnineteen | bpchar | 1 |  |  | '0' |  |
| 20 | fnov | fnov | bpchar | 1 |  |  | '0' |  |
| 21 | faug | faug | bpchar | 1 |  |  | '0' |  |
| 22 | fthirteen | fthirteen | bpchar | 1 |  |  | '0' |  |
| 23 | fthur | fthur | bpchar | 1 |  |  | '0' |  |
| 24 | fno | fno | varchar | 4 |  |  | null |  |
| 25 | feight | feight | bpchar | 1 |  |  | '0' |  |
| 26 | fsixteen | fsixteen | bpchar | 1 |  |  | '0' |  |
| 27 | ftwentyfour | ftwentyfour | bpchar | 1 |  |  | '0' |  |
| 28 | ftwentyone | ftwentyone | bpchar | 1 |  |  | '0' |  |
| 29 | fnumber | 计划编码 | varchar | 80 |  |  | null | 计划编码 |
| 30 | fdesc | 调度计划示例 | varchar | 360 |  | √ | ' ' | 调度计划示例 |
| 31 | ftwentysix | ftwentysix | bpchar | 1 |  |  | '0' |  |
| 32 | ftwenty | ftwenty | bpchar | 1 |  |  | '0' |  |
| 33 | fhost | host | varchar | 50 |  |  | ' ' | host |
| 34 | ftwentynine | ftwentynine | bpchar | 1 |  |  | '0' |  |
| 35 | ffour | ffour | bpchar | 1 |  |  | '0' |  |
| 36 | ftwentyeight | ftwentyeight | bpchar | 1 |  |  | '0' |  |
| 37 | ffifteen | ffifteen | bpchar | 1 |  |  | '0' |  |
| 38 | ften | ften | bpchar | 1 |  |  | '0' |  |
| 39 | fnine | fnine | bpchar | 1 |  |  | '0' |  |
| 40 | foct | foct | bpchar | 1 |  |  | '0' |  |
| 41 | ftwentyfive | ftwentyfive | bpchar | 1 |  |  | '0' |  |
| 42 | fthirtyone | fthirtyone | bpchar | 1 |  |  | '0' |  |
| 43 | fthirty | fthirty | bpchar | 1 |  |  | '0' |  |
| 44 | fstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 45 | fapr | fapr | bpchar | 1 |  |  | '0' |  |
| 46 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fseventeen | fseventeen | bpchar | 1 |  |  | '0' |  |
| 48 | ffive | ffive | bpchar | 1 |  |  | '0' |  |
| 49 | fmon | fmon | bpchar | 1 |  |  | '0' |  |
| 50 | ffri | ffri | bpchar | 1 |  |  | '0' |  |
| 51 | fthree | fthree | bpchar | 1 |  |  | '0' |  |
| 52 | fplan | cron表达式 | varchar | 300 |  | √ | ' ' | cron表达式 |
| 53 | fjan | fjan | bpchar | 1 |  |  | '0' |  |
| 54 | fnoweek | fnoweek | varchar | 4 |  |  | null |  |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fjobid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 57 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 58 | fbyweek | fbyweek | bpchar | 1 |  |  | '0' |  |
| 59 | frepeatmode | 重复时间单位 | varchar | 4 |  | √ | 'n' | 重复时间单位,枚举: n :不重复 mi :分钟 h :小时 d :天 w :星期 m :月 y :年 def :自定义 |
| 60 | fstarttime | 开始时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 开始时间 |
| 61 | fsat | fsat | bpchar | 1 |  |  | '0' |  |
| 62 | fone | fone | bpchar | 1 |  |  | '0' |  |
| 63 | fjun | fjun | bpchar | 1 |  |  | '0' |  |
| 64 | ffeb | ffeb | bpchar | 1 |  |  | '0' |  |
| 65 | fdec | fdec | bpchar | 1 |  |  | '0' |  |
| 66 | fjul | fjul | bpchar | 1 |  |  | '0' |  |
| 67 | fseven | fseven | bpchar | 1 |  |  | '0' |  |
| 68 | feighteen | feighteen | bpchar | 1 |  |  | '0' |  |
| 69 | fendtime | 失效时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 失效时间 |
| 70 | fcyclenum | 重复周期 | int8 | 64 |  | √ | 0 | 重复周期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sch_schedule_pkey |  | fid |
| 2 | idx_sch_scd_jobid |  | fjobid |
| 3 | idx_sch_scd_001 |  | fstarttime,fendtime,fstatus |
