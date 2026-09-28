# 智能执行方案-gl_intellexecschema

## 消息接收人-多选基础资料表 t_gl_intellnotifyusers

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_gl_intellnotifyusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_intellnotifyusers |  | fpkid |
| 2 | idx_gl_schema_id |  | fid |

---

## 操作单据体-子表 t_gl_intellexecoperentry

- **表名称：** 操作单据体-子表
- **表名：** t_gl_intellexecoperentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注： | varchar | 255 |  |  | ' ' | 备注： |
| 3 | fparam | 参数配置 | varchar | 1000 |  |  | ' ' | 参数配置 |
| 4 | fopersystem | fopersystem | int8 | 64 |  | √ | 0 |  |
| 5 | fdatafilter | 数据过滤 | text | 0 |  |  | null | 数据过滤 |
| 6 | fbussiness | 来源单据编码 | varchar | 50 |  | √ | ' ' | 来源单据编码 |
| 7 | foper | 执行操作编码 | varchar | 50 |  | √ | ' ' | 执行操作编码 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | feachbatchsize | 每批执行条数 | int4 | 32 |  | √ | 0 | 每批执行条数 |
| 10 | fdatafilter_tag | 数据过滤_详情 | text | 0 |  |  | null | 数据过滤_详情 |
| 11 | fappid | 应用 | varchar | 100 |  |  | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 13 | ftargetbooksid | ftargetbooksid | int8 | 64 |  | √ | 0 |  |
| 14 | fissingle | 是否单条执行 | bpchar | 1 |  | √ | '0' | 是否单条执行 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_intellexecoperentry_fid |  | fid |
| 2 | t_gl_intellexecoperentry_pkey |  | fentryid |

---

## 智能执行方案-多语言表 t_gl_intellaccountschema_l

- **表名称：** 智能执行方案-多语言表
- **表名：** t_gl_intellaccountschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fexceplanlang | 执行计划多语言 | varchar | 2000 |  | √ | ' ' | 执行计划多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_intellaccountschema_l_pkey |  | fpkid |
| 2 | idx_gl_intellaccountscheme_l |  | fid,flocaleid |

---

## 智能执行方案-主表 t_gl_intellaccountschema

- **表名称：** 智能执行方案-主表
- **表名：** t_gl_intellaccountschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fresponsiblepersonid | 消息接收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fnotificationconditions | 消息发送条件 | varchar | 64 |  | √ | ' ' | 消息发送条件,枚举: fail :执行失败 success :执行成功 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstopstarttime | 终止执行时间.开始 | int4 | 32 |  | √ | '-1' | 终止执行时间.开始 |
| 9 | fnotificationtypes | 消息发送方式 | varchar | 64 |  | √ | ' ' | 消息发送方式,枚举: yunzhijia :云之家 mcenter :消息中心 sms :短信 email :邮件 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fexecstatus | fexecstatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | flastexecdate | flastexecdate | timestamp | 0 |  |  | null |  |
| 15 | ffailretrystrategy | 重试策略 | varchar | 20 |  | √ | ' ' | 重试策略,枚举: ignore :直接挂起 tryagain :重试一次 tryagainthree :重试三次 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fexceplandesc | 执行计划 | varchar | 2000 |  | √ | ' ' | 执行计划 |
| 18 | fnumber | 机器人编码 | varchar | 50 |  | √ | ' ' | 机器人编码 |
| 19 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 20 | fstopendtime | 终止执行时间.结束 | int4 | 32 |  | √ | '-1' | 终止执行时间.结束 |
| 21 | fexceplan | 调度计划id | varchar | 255 |  | √ | ' ' | 调度计划id |
| 22 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_intellaccountschema |  | fcreatorid |
| 2 | t_gl_intellaccountschema_pkey |  | fid |

---

## 组织单据体-子表 t_gl_intellexecorgentry

- **表名称：** 组织单据体-子表
- **表名：** t_gl_intellexecorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_intellexecorgentry_fid |  | fid |
| 2 | t_gl_intellexecorgentry_pkey |  | fentryid |
