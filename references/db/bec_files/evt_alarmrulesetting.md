# 报警消息设置-evt_alarmrulesetting

## 报警消息设置-主表 t_wf_alarmrule

- **表名称：** 报警消息设置-主表
- **表名：** t_wf_alarmrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fchannelname | 渠道名称 | varchar | 200 |  | √ | ' ' | 渠道名称 |
| 5 | ftimes | 报警次数 | int4 | 32 |  | √ | 0 | 报警次数 |
| 6 | fappnumber | 应用编码 | varchar | 20 |  | √ | 'wf' | 应用编码,枚举: wf :工作流 bec :业务实事件中心 |
| 7 | freceiver | 接收人 | varchar | 500 |  | √ | ' ' | 接收人 |
| 8 | falarmscene | 报警场景 | varchar | 50 |  | √ | ' ' | 报警场景,枚举: overtimeRemind :订阅执行超时隔离至慢队列 overtimeWarning :订阅执行超时拒绝重试并且隔离至慢队列 overtimeAbnormal :订阅执行超时直接挂起 failureRateRemind :订阅执行失败率过高隔离至慢队列 failureRateWarning :订阅执行失败率过高拒绝重试并且隔离至慢队列 failureRateAbnormal :订阅执行失败率过高直接挂起 |
| 9 | finterval | 报警间隔 | int4 | 32 |  | √ | 0 | 报警间隔 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fconfig | 配置参数 | varchar | 500 |  | √ | ' ' | 配置参数 |
| 12 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fchannel | 发送渠道 | varchar | 200 |  | √ | ' ' | 发送渠道,枚举: |
| 15 | freceivername | 接收人名称 | varchar | 500 |  | √ | ' ' | 接收人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_alarmrule_createdate |  | fcreatedate |
| 2 | pk_wf_alarmrule |  | fid |
| 3 | idx_wf_alarmrule_alarmscene |  | falarmscene |

---

## 报警消息设置-多语言表 t_wf_alarmrule_l

- **表名称：** 报警消息设置-多语言表
- **表名：** t_wf_alarmrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fchannelname | 渠道名称 | varchar | 200 |  | √ | ' ' | 渠道名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | freceivername | 接收人名称 | varchar | 500 |  | √ | ' ' | 接收人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_alarmrule_l |  | fid,flocaleid |
| 2 | pk_wf_alarmrule_l |  | fpkid |
