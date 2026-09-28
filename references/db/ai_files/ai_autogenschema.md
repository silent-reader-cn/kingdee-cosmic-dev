# 自动生成凭证方案-ai_autogenschema

## 单据体-子表 t_ai_acctbookentity

- **表名称：** 单据体-子表
- **表名：** t_ai_acctbookentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgfield | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fafterperiods | 允许执行未来期间数 | int4 | 32 |  | √ | 0 | 允许执行未来期间数 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fselectedbook | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 7 | facctbook | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 8 | fvchcreator | 凭证制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | faccountingmode | 记账模式 | bpchar | 1 |  | √ | '0' | 记账模式,枚举: 0 :模板记账 1 :AI记账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_acctbookentity |  | fid |
| 2 | pk_t_ai_acctbookentity |  | fentryid |

---

## 子单据体-子表 t_ai_srcbillsubentity

- **表名称：** 子单据体-子表
- **表名：** t_ai_srcbillsubentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funiontype | 汇总方式 | varchar | 50 |  | √ | ' ' | 汇总方式,枚举: 0 :一对一生成 1 :同种单据全部汇总 2 :同种单据匹配汇总 3 :同账簿所有单据全部汇总 4 :凭证模板设置的汇总方式 |
| 2 | ffiltercondition_tag | 单据过滤条件取值_详情 | text | 0 |  |  | null | 单据过滤条件取值_详情 |
| 3 | ffilterconditionmul | 单据过滤条件多语言 | varchar | 2000 |  | √ | ' ' | 单据过滤条件多语言 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmatchfieldkey | 匹配字段标识 | varchar | 250 |  | √ | ' ' | 匹配字段标识 |
| 6 | fregularcreator | 固定制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsystem | fsystem | varchar | 50 |  | √ | ' ' |  |
| 8 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fselectedbill | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 10 | ffilterconditiondesc | 单据过滤条件 | varchar | 2000 |  | √ | ' ' | 单据过滤条件 |
| 11 | fbillperson | 制单人取单据用户 | varchar | 50 |  | √ | ' ' | 制单人取单据用户 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fmatchfieldname | 匹配字段 | varchar | 250 |  | √ | ' ' | 匹配字段 |
| 15 | ffiltercondition | 单据过滤条件取值 | text | 0 |  |  | null | 单据过滤条件取值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_srcbillsubentity |  | fdetailid |
| 2 | idx_ai_srcbillsubentity |  | fentryid |

---

## 自动生成凭证方案-多语言表 t_ai_autogenschema_l

- **表名称：** 自动生成凭证方案-多语言表
- **表名：** t_ai_autogenschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fexceplanlang | 执行计划多语言 | varchar | 255 |  |  | ' ' | 执行计划多语言 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_autogenschema_l |  | fpkid |
| 2 | idx_ai_autogenschema_l |  | fid,flocaleid |

---

## 自动生成凭证方案-主表 t_ai_autogenschema

- **表名称：** 自动生成凭证方案-主表
- **表名：** t_ai_autogenschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fgeneratetype | 自动生成方式 | bpchar | 1 |  | √ | '1' | 自动生成方式,枚举: 1 :定时生成凭证 0 :实时生成凭证 |
| 5 | fvchperson | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fexecutorchoose | 凭证制单人选项 | bpchar | 1 |  | √ | '1' | 凭证制单人选项,枚举: 1 :取执行人 2 :按账簿指定 3 :按单据指定 4 :取凭证模板制单人 |
| 8 | fnotificationconditions | 消息发送条件 | varchar | 50 |  | √ | ' ' | 消息发送条件,枚举: fail :执行失败 success :执行成功 |
| 9 | fstopstarttime | 终止执行时间.开始 | int4 | 32 |  | √ | '-1' | 终止执行时间.开始 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fnotificationtypes | 消息发送方式 | varchar | 50 |  | √ | ' ' | 消息发送方式,枚举: yunzhijia :云之家 mcenter :消息中心 sms :短信 email :邮件 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fsheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fexecutor | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | ffailretrystrategy | 重试策略 | varchar | 50 |  | √ | ' ' | 重试策略,枚举: ignore :直接挂起 tryagain :重试一次 tryagainthree :重试三次 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fexceplandesc | 调度计划 | varchar | 255 |  | √ | ' ' | 调度计划 |
| 20 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 21 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 22 | fstopendtime | 终止执行时间.结束 | int4 | 32 |  | √ | '-1' | 终止执行时间.结束 |
| 23 | fexceplan | fexceplan | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_autogenschema |  | fid |
| 2 | idx_ai_auto_genscheme |  | fnumber |

---

## 消息接收人-多选基础资料表 t_ai_notificationusers

- **表名称：** 消息接收人-多选基础资料表
- **表名：** t_ai_notificationusers

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
| 1 | idx_ai_notificationusers |  | fid |
| 2 | pk_t_ai_notificationusers |  | fpkid |

---

## 子单据体-多语言表 t_ai_srcbillsubentity_l

- **表名称：** 子单据体-多语言表
- **表名：** t_ai_srcbillsubentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffilterconditionmul | 单据过滤条件多语言 | varchar | 2000 |  | √ | ' ' | 单据过滤条件多语言 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_srcbillsub_l_fdetailid |  | fdetailid,flocaleid |
| 2 | pk_ai_srcbillsubentity_l |  | fpkid |
