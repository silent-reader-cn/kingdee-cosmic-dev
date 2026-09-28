# 调度作业-sch_job

## 消息接收人-多选基础资料表 t_sch_jobmsgreceiver

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_sch_jobmsgreceiver

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
| 1 | pk_t_sch_jobmsgreceiver |  | fpkid |
| 2 | idx_sch_jobmsgreceiver_fk |  | fentryid |

---

## 调度作业-分表 t_sch_job_n

- **表名称：** 调度作业-分表
- **表名：** t_sch_job_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fnotifytype | 消息渠道 | varchar | 300 |  | √ | ' ' | 消息渠道,枚举: |
| 3 | fcaption | 消息标题 | varchar | 100 |  | √ | ' ' | 消息标题 |
| 4 | faborted | 终止 | bpchar | 1 |  |  | null | 终止 |
| 5 | ffailnotify | 失败 | bpchar | 1 |  | √ | '0' | 失败 |
| 6 | fsuccessnotify | 成功 | bpchar | 1 |  | √ | '0' | 成功 |
| 7 | fovertime | 超时 | bpchar | 1 |  | √ | '0' | 超时 |
| 8 | fmsgcontent | 消息内容 | varchar | 2000 |  |  | null | 消息内容 |
| 9 | fjobmsgreceiver | 消息接收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fjobprincipal | 作业负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_job_n_fcaption |  | fcaption |
| 2 | t_sch_job_n_pkey |  | fid |

---

## 调度作业-多语言表 t_sch_job_l

- **表名称：** 调度作业-多语言表
- **表名：** t_sch_job_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
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
| 1 | idx_sch_job_l_id |  | fid,flocaleid |
| 2 | t_sch_job_l_pkey |  | fpkid |

---

## 消息通知单据体-子表 t_sch_job_m

- **表名称：** 消息通知单据体-子表
- **表名：** t_sch_job_m

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
| 1 | idx_sch_job_m_fk |  | fid |
| 2 | idx_sch_job_m_fid |  | fid |
| 3 | pk_t_sch_job_m |  | fentryid |

---

## 调度作业-主表 t_sch_job

- **表名称：** 调度作业-主表
- **表名：** t_sch_job

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fjobtype | 类型 | varchar | 10 |  | √ | ' ' | 类型,枚举: BIZ :业务 WORKFLOW :工作流 REALTIME :实时作业 DETECT :探测任务 |
| 3 | frunbylang | 执行时语言环境 | varchar | 10 |  | √ | 'zh_CN' | 执行时语言环境,枚举: |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fconcurrent | 是否并发 | bpchar | 1 |  | √ | '1' | 是否并发 |
| 6 | fretrytime | 失败重试次数 | int4 | 32 |  | √ | 0 | 失败重试次数 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ftaskdefineid | 执行程序 | varchar | 36 |  |  | null | [调度执行程序 sch_taskdefine](../sys_files/sch_taskdefine.md) |
| 9 | fcanstop | 允许终止 | bpchar | 1 |  | √ | '0' | 允许终止 |
| 10 | ftasktrace | 任务追踪 | bpchar | 1 |  | √ | '0' | 任务追踪 |
| 11 | frunbyorgid | 执行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | frunbyuserid | 执行作业的用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fparams | 参数 | text | 0 |  |  | null | 参数 |
| 14 | fstrategy | 执行策略 | bpchar | 1 |  | √ | '0' | 执行策略,枚举: 0 :并发执行 1 :等待前一任务执行完毕 2 :覆盖前一任务 |
| 15 | ftaskclassname | 类名 | varchar | 300 |  | √ | ' ' | 类名 |
| 16 | frunmode | 执行模式 | bpchar | 1 |  | √ | '0' | 执行模式,枚举: 0 :单机执行 1 :广播分片 2 :任务分片 |
| 17 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fnumber | 编码 | varchar | 100 |  |  | null | 编码 |
| 21 | ftimeout | 超时时间(s) | int8 | 64 |  | √ | 0 | 超时时间(s) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sch_job_number |  | fnumber |
| 2 | pk_t_sch_job |  | fid |
| 3 | idx_sch_job_taskdefine |  | ftaskdefineid |
