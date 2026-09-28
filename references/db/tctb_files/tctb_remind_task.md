# 提醒任务-tctb_remind_task

## 提醒任务-主表 t_tctb_remind_task

- **表名称：** 提醒任务-主表
- **表名：** t_tctb_remind_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 提醒任务名称 | varchar | 200 |  | √ | ' ' | 提醒任务名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fremindtype | 提醒事项类型 | varchar | 50 |  | √ | ' ' | 提醒事项类型,枚举: |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fsheduleplanid | 调度计划id | varchar | 50 |  | √ | ' ' | 调度计划id |
| 9 | fcreatorid | 任务创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fsubscribe | 订阅名称 | int8 | 64 |  | √ | 0 | [事件订阅 evt_subscription](../bec_files/evt_subscription.md) |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fexceplandesc | 执行计划时间 | varchar | 1000 |  | √ | ' ' | 执行计划时间 |
| 14 | froletype | 消息接收人角色类型 | varchar | 50 |  | √ | ' ' | 消息接收人角色类型,枚举: common :通用角色 biz :业务角色 position :职位 |
| 15 | fposition | 消息接收人职位 | varchar | 50 |  | √ | ' ' | 消息接收人职位,枚举: 1 :董事长 2 :总经理 3 :财务负责人 4 :税务会计 6 :税务负责人 5 :其他 |
| 16 | fnumber | 提醒任务编码 | varchar | 30 |  | √ | ' ' | 提醒任务编码 |
| 17 | fendtime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_remind_task_fnumber |  | fnumber,fsheduleplanid,fsubscribe |
| 2 | pk_tctb_remind_task |  | fid |

---

## 提醒任务-多语言表 t_tctb_remind_task_l

- **表名称：** 提醒任务-多语言表
- **表名：** t_tctb_remind_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 提醒任务名称 | varchar | 200 |  | √ | ' ' | 提醒任务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_remind_task_l |  | fpkid |
| 2 | idx_tctb_remind_task_l_0 |  | fid,flocaleid |

---

## 组织单据体-子表 t_tctb_remind_org_range

- **表名称：** 组织单据体-子表
- **表名：** t_tctb_remind_org_range

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_remind_org_range |  | fentryid |
| 2 | idx_tctb_remind_org_range_fk |  | fid |

---

## 消息抄送人-多选基础资料表 t_tctb_remind_ccuser

- **表名称：** 消息抄送人-多选基础资料表
- **表名：** t_tctb_remind_ccuser

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
| 1 | idx_tctb_remind_ccuser_fk |  | fid |
| 2 | pk_tctb_remind_ccuser |  | fpkid |

---

## 规则单据体-子表 t_tctb_remind_rule

- **表名称：** 规则单据体-子表
- **表名：** t_tctb_remind_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffconditionjson | 过滤条件 | text | 0 |  |  | null | 过滤条件 |
| 3 | ftable | 数据源 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizname | 业务名称 | varchar | 100 |  | √ | ' ' | 业务名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffiltercondition | 过滤条件 | text | 0 |  |  | null | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_remind_rule_fk |  | fid |
| 2 | pk_tctb_remind_rule |  | fentryid |

---

## 消息接收人系统角色-多选基础资料表 t_tctb_remind_commsysrole

- **表名称：** 消息接收人系统角色-多选基础资料表
- **表名：** t_tctb_remind_commsysrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_remind_commsysrole |  | fpkid |
| 2 | idx_tctb_remind_commsysrole_fk |  | fid |

---

## 消息接收人系统角色-多选基础资料表 t_tctb_remind_bizsysrole

- **表名称：** 消息接收人系统角色-多选基础资料表
- **表名：** t_tctb_remind_bizsysrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务角色 perm_busirole](../base_files/perm_busirole.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_remind_bizsysrole |  | fpkid |
| 2 | idx_tctb_remind_bizsysrole_fk |  | fid |
