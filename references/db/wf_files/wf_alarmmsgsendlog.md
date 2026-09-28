# 报警消息发送日志-wf_alarmmsgsendlog

## 报警消息发送日志-主表 t_wf_alarmmsgsendlog

- **表名称：** 报警消息发送日志-主表
- **表名：** t_wf_alarmmsgsendlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftimes | 已报警次数 | int4 | 32 |  | √ | 0 | 已报警次数 |
| 3 | fchannelname | 渠道名称 | varchar | 200 |  | √ | ' ' | 渠道名称 |
| 4 | freceiver | 接收人 | varchar | 2000 |  | √ | ' ' | 接收人 |
| 5 | falarmscene | 报警场景 | varchar | 200 |  | √ | ' ' | 报警场景,枚举: plugintimeouterror :插件执行超时 errorAddress :寻址异常没有进入流程时 conflict :找到多条满足条件的流程而没有进入流程时 notFind :无匹配的流程而没有进入流程时 |
| 6 | fmessageids | 消息id集合 | varchar | 255 |  | √ | ' ' | 消息id集合 |
| 7 | fmessageids_tag | 消息id集合_详情 | text | 0 |  |  | null | 消息id集合_详情 |
| 8 | ftitle | 消息标题 | varchar | 2000 |  | √ | ' ' | 消息标题 |
| 9 | falarmruleid | 报警规则id | int8 | 64 |  | √ | 0 | 报警规则id |
| 10 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: unfinish :未完成 suspend :中断 complete :完成 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fmodifydate | 报警时间 | timestamp | 0 |  |  | null | 报警时间 |
| 13 | fmonitorid | 关联mq监控id | int8 | 64 |  | √ | 0 | 关联mq监控id |
| 14 | fgroup | 报警场景关联key | varchar | 500 |  | √ | ' ' | 报警场景关联key |
| 15 | fcontent | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |
| 16 | fchannel | 发送渠道 | varchar | 200 |  | √ | ' ' | 发送渠道,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_alarmmsgsendlog_crdate |  | fcreatedate |
| 2 | idx_wf_alarmmsgsendlog_scene |  | falarmscene,fstate |
| 3 | pk_wf_alarmmsgsendlog |  | fid |

---

## 报警消息发送日志-多语言表 t_wf_alarmmsgsendlog_l

- **表名称：** 报警消息发送日志-多语言表
- **表名：** t_wf_alarmmsgsendlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 消息标题 | varchar | 2000 |  | √ | ' ' | 消息标题 |
| 3 | fchannelname | 渠道名称 | varchar | 200 |  | √ | ' ' | 渠道名称 |
| 4 | freceiver | 接收人 | varchar | 2000 |  | √ | ' ' | 接收人 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fcontent | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_alarmmsgsendlog_l |  | fpkid |
| 2 | idx_wf_alarmmsgsendlog_l |  | fid,flocaleid |
