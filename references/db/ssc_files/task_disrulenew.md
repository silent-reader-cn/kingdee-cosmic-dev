# 任务分配规则-old-task_disrulenew

## 组织范围-多选基础资料表 t_tk_disruleorgrange

- **表名称：** 组织范围-多选基础资料表
- **表名：** t_tk_disruleorgrange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 共享中心组织分配 task_org |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_disruleorgrange_pkey |  | fpkid |
| 2 | index_ssc_disruleorgrange |  | fbasedataid |

---

## 任务分配规则-old-多语言表 t_tk_disrule_new_l

- **表名称：** 任务分配规则-old-多语言表
- **表名：** t_tk_disrule_new_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_disrule_new_l_pkey |  | fpkid |
| 2 | idx_tk_disrulenewl_locale |  | fid,flocaleid |

---

## 组织与用户-子表 t_tk_disrule_org_user

- **表名称：** 组织与用户-子表
- **表名：** t_tk_disrule_org_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fgroupid | 处理人-用户组 | int8 | 64 |  | √ | 0 | 用户组 task_usergroup |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | forgrangeid | forgrangeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_disrule_org_user_pkey |  | fentryid |
| 2 | index_ssc_disrule_orguser |  | fid |

---

## 任务分配规则-old-主表 t_tk_disrule_new

- **表名称：** 任务分配规则-old-主表
- **表名：** t_tk_disrule_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ffilterrule | ffilterrule | varchar | 100 |  | √ | ' ' |  |
| 5 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 8 | fpriority | 执行顺序 | int8 | 64 |  | √ | 0 | 执行顺序 |
| 9 | fssccenterid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_disrule_new_pkey |  | fid |
| 2 | index_ssc_disrule_new |  | fnumber |

---

## 分配规则-子表 t_tk_disrule_rule

- **表名称：** 分配规则-子表
- **表名：** t_tk_disrule_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ffilterrule | 过滤规则 | varchar | 2000 |  | √ | ' ' | 过滤规则 |
| 4 | ffilterrulejson_tag | ffilterrulejson_tag | text | 0 |  |  | null |  |
| 5 | fapplycreditleveljoson_tag | fapplycreditleveljoson_tag | text | 0 |  |  | null |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffilterrulejson | ffilterrulejson | text | 0 |  |  | null |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fapplycreditleveljoson | fapplycreditleveljoson | text | 0 |  |  | null |  |
| 10 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_disrule_rule_pkey |  | fentryid |
| 2 | index_ssc_disrule_rule |  | fid |
