# 事件订阅-kem_subscribe

## 事件订阅-主表 t_kem_sub

- **表名称：** 事件订阅-主表
- **表名：** t_kem_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftriggertype | 触发方式 | bpchar | 1 |  | √ | ' ' | 触发方式,枚举: 1 : 2 : |
| 3 | fisvid | 开发商标识 | varchar | 20 |  | √ | ' ' | 开发商标识 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :草稿 B :已发布 F :废弃 |
| 6 | feventbusid | 事件通道（历史） | int8 | 64 |  | √ | 0 | [事件通道 kem_eventbus](../kem_files/kem_eventbus.md) |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fmatchscriptdesc | fmatchscriptdesc | varchar | 200 |  |  | ' ' |  |
| 10 | fversion | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |
| 11 | feventtype | feventtype | bpchar | 1 |  | √ | ' ' |  |
| 12 | ftriggertimetype | 触发周期 | bpchar | 1 |  | √ | ' ' | 触发周期,枚举: 1 :固定周期 2 :自定义Cron |
| 13 | fmatchscript_tag | 匹配脚本_详情 | text | 0 |  |  | null | 匹配脚本_详情 |
| 14 | fname | 订阅名称 | varchar | 50 |  | √ | ' ' | 订阅名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | feventdatasourceid | 来源数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 17 | feventid | 触发事件 | int8 | 64 |  | √ | 0 | [事件 kem_event](../kem_files/kem_event.md) |
| 18 | fmqtopicid | MQTopic | int8 | 64 |  | √ | 0 | [消息订阅主题 isc_mq_subscriber](../iscb_files/isc_mq_subscriber.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsrcsubtype | 来源 | bpchar | 1 |  | √ | '0' | 来源,枚举: 1 :开放事件 2 :组装流 0 :手工创建 |
| 21 | ftargetappname | 目标应用名称 | varchar | 40 |  | √ | ' ' | 目标应用名称 |
| 22 | ftriggerperiod | Cron表达式 | varchar | 50 |  | √ | ' ' | Cron表达式 |
| 23 | ffailovertype | 容错处理 | bpchar | 1 |  | √ | ' ' | 容错处理,枚举: 1 :异常容错 2 :异常中断 |
| 24 | fflowlimit | 限流控制（次/秒） | int4 | 32 |  | √ | 0 | 限流控制（次/秒） |
| 25 | fmatchscript | 匹配脚本 | varchar | 255 |  | √ | ' ' | 匹配脚本 |
| 26 | ffounderid | 初始版本 | int8 | 64 |  | √ | 0 | 初始版本 |
| 27 | fsrcsubid | 源订阅ID | int8 | 64 |  | √ | 0 | 源订阅ID |
| 28 | ftriggerperiodunit | 单位 | bpchar | 1 |  | √ | ' ' | 单位,枚举: 1 :秒 2 :分 3 :时 4 :天 5 :周 6 :月 |
| 29 | fretrytype | 重试机制 | bpchar | 1 |  | √ | ' ' | 重试机制,枚举: 2 : 1 : 3 : |
| 30 | fperiod | 固定周期 | int4 | 32 |  | √ | 0 | 固定周期 |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 订阅编码 | varchar | 100 |  | √ | ' ' | 订阅编码 |
| 33 | fdesc | fdesc | varchar | 1000 |  | √ | ' ' |  |
| 34 | feventsourceid | feventsourceid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_sub_eid |  | feventid |
| 2 | idx_kem_sub_number |  | fnumber |
| 3 | pk_t_kem_sub |  | fid |
| 4 | idx_kem_sub_ver |  | fversion,ffounderid |

---

## 订阅规则-子表 t_kem_subcond

- **表名称：** 订阅规则-子表
- **表名：** t_kem_subcond

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fleftbracket | 左括号 | bpchar | 5 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( ((( :((( |
| 3 | frightbracket | 右括号 | bpchar | 5 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) ))) :))) |
| 4 | fparadesc | fparadesc | varchar | 255 |  | √ | ' ' |  |
| 5 | fparavalue | 比较值 | varchar | 2000 |  | √ | ' ' | 比较值 |
| 6 | fparaname | 事件参数 | varchar | 250 |  | √ | ' ' | 事件参数 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparatype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :布尔值 double :浮点数 ENUM :枚举 STRUCT :结构 unknown :任意值 |
| 9 | fcondtype | 比较方式 | varchar | 50 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 10 | fandor | 逻辑连接符 | bpchar | 1 |  | √ | ' ' | 逻辑连接符,枚举: 0 :与 1 :或 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_subcond_fid |  | fid |
| 2 | pk_t_kem_subcond |  | fentryid |

---

## 订阅规则-多语言表 t_kem_subcond_l

- **表名称：** 订阅规则-多语言表
- **表名：** t_kem_subcond_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparadesc | 参数说明 | varchar | 255 |  |  | ' ' | 参数说明 |
| 2 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_subcond_l |  | fentryid,flocaleid |
| 2 | pk_t_kem_subcond_l |  | fpkid |

---

## 事件目标-子表 t_kem_subtarget

- **表名称：** 事件目标-子表
- **表名：** t_kem_subtarget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factionconfig_tag | 目标服务配置_详情 | text | 0 |  |  | null | 目标服务配置_详情 |
| 3 | factionconfig | 目标服务配置 | varchar | 255 |  | √ | ' ' | 目标服务配置 |
| 4 | factionnumber | 目标服务对象编码 | varchar | 50 |  | √ | ' ' | 目标服务对象编码 |
| 5 | faction_basedata | 目标基础资料 | int8 | 64 |  | √ | 0 | WebAPI登记 isc_apic_webapi |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | factiontype | 服务类型 | int8 | 64 |  | √ | 0 | [目标服务类型 kem_actiontype](../kem_files/kem_actiontype.md) |
| 8 | factionid | 目标服务对象ID | varchar | 50 |  | √ | ' ' | 目标服务对象ID |
| 9 | factionname | 目标服务对象名称 | varchar | 50 |  | √ | ' ' | 目标服务对象名称 |
| 10 | faction_basetype | 基础资料类型 | varchar | 50 |  |  | ' ' | 基础资料类型,枚举: isc_apic_webapi :WebAPI登记 isc_service_flow :服务流程 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | factiondatasourceid | 目标服务数据源Id | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kem_subtarget |  | fentryid |
| 2 | idx_kem_subtarget_fid |  | fid |

---

## 事件订阅-多语言表 t_kem_sub_l

- **表名称：** 事件订阅-多语言表
- **表名：** t_kem_sub_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 订阅名称 | varchar | 50 |  | √ | ' ' | 订阅名称 |
| 3 | fmatchscriptdesc | 规则说明 | varchar | 200 |  |  | ' ' | 规则说明 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdesc | 订阅描述 | varchar | 1000 |  |  | ' ' | 订阅描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kem_sub_l |  | fpkid |
| 2 | idx_kem_sub_l_fid |  | fid,flocaleid |
