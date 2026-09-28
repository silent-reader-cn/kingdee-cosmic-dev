# 抽取数据调度计划-evp_schedule

## 抽取数据调度计划-多语言表 t_evp_schedule_l

- **表名称：** 抽取数据调度计划-多语言表
- **表名：** t_evp_schedule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_schedule_l |  | fpkid |
| 2 | idx_evp_schedule_l |  | fid,flocaleid |

---

## 适用账簿-多选基础资料表 t_evp_schedulebooks

- **表名称：** 适用账簿-多选基础资料表
- **表名：** t_evp_schedulebooks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evp_schedulebooks |  | fid |
| 2 | pk_evp_scheduleorgs |  | fpkid |

---

## 抽取数据调度计划-主表 t_evp_schedule

- **表名称：** 抽取数据调度计划-主表
- **表名：** t_evp_schedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fperiodrange | 期间范围 | varchar | 50 |  | √ | ' ' | 期间范围,枚举: 0 :本期 1 :上期 2 :本期+上期 |
| 6 | fplandesc | 执行计划 | varchar | 2000 |  | √ | ' ' | 执行计划 |
| 7 | fnotificationconditions | 消息发送条件 | varchar | 200 |  | √ | ' ' | 消息发送条件,枚举: fail :执行失败 success :执行成功 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 10 | fnotificationtypes | 消息发送方式 | varchar | 200 |  | √ | ' ' | 消息发送方式,枚举: yunzhijia :云之家 mcenter :消息中心 sms :短信 email :邮件 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fnoticorid | 消息接收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbooktypeid | fbooktypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fperiodtypeid | 会计日历 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fmonthrange | 对账单月份范围 | varchar | 50 |  | √ | ' ' | 对账单月份范围,枚举: 0 :本月 1 :上月 2 :本月+上月 |
| 18 | frange | 抽取类型 | varchar | 50 |  | √ | ' ' | 抽取类型,枚举: 1 :凭证+关联票据 2 :银行对账单 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 22 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evp_schedule |  | fid |
| 2 | idx_evp_schedule |  | fnumber |
