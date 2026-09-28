# 任务分配规则查询-task_disrule_query

## 任务分配规则查询-主表 t_tk_disrule_query

- **表名称：** 任务分配规则查询-主表
- **表名：** t_tk_disrule_query

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffilterrule | 单据规则 | varchar | 2000 |  | √ | ' ' | 单据规则 |
| 3 | fusergroup | 用户组 | int8 | 64 |  | √ | 0 | [用户组 task_usergroup](../ssc_files/task_usergroup.md) |
| 4 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpriority | 执行顺序 | int8 | 64 |  | √ | 0 | 执行顺序 |
| 8 | frule_json_b | 单据规则json_bill | text | 0 |  |  | null | 单据规则json_bill |
| 9 | frule_json_c | 单据规则json_credit | text | 0 |  |  | null | 单据规则json_credit |
| 10 | ftaskbill | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 11 | fssccenter | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | frule_json_b_tag | 单据规则json_bill_详情 | text | 0 |  |  | null | 单据规则json_bill_详情 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fuserfield | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | frule_json_c_tag | 单据规则json_credit_详情 | text | 0 |  |  | null | 单据规则json_credit_详情 |
| 17 | ftask_disrule | 任务分配规则 | int8 | 64 |  | √ | 0 | [任务分配规则 task_disrule](../ssc_files/task_disrule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_disrulequery_org |  | forgfield |
| 2 | index_disrulequery_user |  | fuserfield |
| 3 | t_tk_disrule_query_pkey |  | fid |
| 4 | index_disrulequery_name |  | ftask_disrule |

---

## 任务分配规则查询-多语言表 t_tk_disrule_query_l

- **表名称：** 任务分配规则查询-多语言表
- **表名：** t_tk_disrule_query_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_disrule_query_l_pkey |  | fpkid |
| 2 | idx_tk_disrqry_l_locale |  | fid,flocaleid |
