# 报警消息设置-wf_alarmrule

## 报警消息设置-主表 t_wf_alarmrule

- **表名称：** 报警消息设置-主表
- **表名：** t_wf_alarmrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fchannelname | 渠道名称 | varchar | 200 |  | √ | ' ' | 渠道名称 |
| 5 | ftimes | 报警次数 | int4 | 32 |  | √ | 0 | 报警次数 |
| 6 | freceiver | 接收人 | varchar | 500 |  | √ | ' ' | 接收人 |
| 7 | falarmscene | 报警场景 | varchar | 50 |  | √ | ' ' | 报警场景,枚举: plugintimeouterror :插件执行超时 errorAddress :寻址异常没有进入流程时 conflict :找到多条满足条件的流程而没有进入流程时 notFind :无匹配的流程而没有进入流程时 |
| 8 | finterval | 报警间隔 | int4 | 32 |  | √ | 0 | 报警间隔 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fconfig | 配置参数 | varchar | 500 |  | √ | ' ' | 配置参数 |
| 11 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 12 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fchannel | 发送渠道 | varchar | 200 |  | √ | ' ' | 发送渠道,枚举: |
| 14 | freceivername | 接收人名称 | varchar | 500 |  | √ | ' ' | 接收人名称 |

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
