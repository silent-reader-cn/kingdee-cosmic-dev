# 电商对账规则-mal_statement_rule

## 电商对账规则-多语言表 t_mal_statementrule_l

- **表名称：** 电商对账规则-多语言表
- **表名：** t_mal_statementrule_l

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
| 1 | idx_t_mal_stmrule_l |  | fid,flocaleid |
| 2 | pk_t_mal_statementrule_l |  | fpkid |

---

## 电商对账规则-主表 t_mal_statementrule

- **表名称：** 电商对账规则-主表
- **表名：** t_mal_statementrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjob_scheduleid | 调度计划 | varchar | 36 |  | √ | ' ' | [调度计划 sch_schedule](../sys_files/sch_schedule.md) |
| 6 | fhandler | 处理器 | varchar | 512 |  | √ | ' ' | 处理器 |
| 7 | ffetchingapproach | 账单获取方式 | varchar | 10 |  | √ | ' ' | 账单获取方式,枚举: 1 :主动获取 2 :电商推送 |
| 8 | frepeatmode | 重复时间单位 | varchar | 50 |  | √ | ' ' | 重复时间单位,枚举: NONE :不重复 ByMinutes :分钟 ByHours :小时 ByDays :天 ByWeeks :星期 ByMonths :月 ByYears :年 ByCustomize :自定义 |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fecadmit | 电商平台 | int8 | 64 |  | √ | 0 | [电商授权 pmm_ecadmit](../pmm_files/pmm_ecadmit.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fexe_job_userid | 执行用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftotal_count | 触发次数 | int4 | 32 |  | √ | 0 | 触发次数 |
| 18 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 21 | fcyclenum | 对账间隔时间 | int4 | 32 |  | √ | 0 | 对账间隔时间 |
| 22 | fjob_defineid | 调度作业 | varchar | 36 |  | √ | ' ' | [调度作业 sch_job](../sys_files/sch_job.md) |
| 23 | ftrigged_time | 最近触发时间 | timestamp | 0 |  |  | null | 最近触发时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_stm_rule_number |  | fnumber |
| 2 | pk_t_mal_statementrule |  | fid |
