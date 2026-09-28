# 标准集成消息日志-mbase_bzjclog

## 重发单据体-子表 t_mbase_bzjclogretryentry

- **表名称：** 重发单据体-子表
- **表名：** t_mbase_bzjclogretryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretrytouser | 消息接收人ID | varchar | 1000 |  | √ | ' ' | 消息接收人ID |
| 3 | fretryresponse | 消息结果 | varchar | 255 |  |  | ' ' | 消息结果 |
| 4 | fretrysendmessage_tag | 发送消息_详情 | text | 0 |  |  | null | 发送消息_详情 |
| 5 | fretryresponse_tag | 消息结果_详情 | text | 0 |  |  | null | 消息结果_详情 |
| 6 | fretrysendtime | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 7 | fretryrecordid | 记录内码 | varchar | 100 |  |  | ' ' | 记录内码 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fretryerrorcode | 错误码 | varchar | 30 |  | √ | ' ' | 错误码 |
| 10 | fretrysendmessage | 发送消息 | varchar | 255 |  |  | ' ' | 发送消息 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fretrysuccess | 是否成功 | varchar | 1 |  | √ | ' ' | 是否成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bzjclogretry_fid |  | fid |
| 2 | pk_mbase_bzjclogretryentry |  | fentryid |

---

## 标准集成消息日志-主表 t_mbase_bzjclog

- **表名称：** 标准集成消息日志-主表
- **表名：** t_mbase_bzjclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessagebody | 消息体数据 | varchar | 255 |  |  | ' ' | 消息体数据 |
| 3 | fopenids | 移动平台用户ID | varchar | 1000 |  | √ | ' ' | 移动平台用户ID |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcorpname | 企业团队名称 | varchar | 100 |  | √ | ' ' | 企业团队名称 |
| 6 | fresult | 消息状态 | varchar | 50 |  | √ | ' ' | 消息状态,枚举: 0 :成功 1 :部分成功 2 :失败 |
| 7 | fprocinstid | 实例内码 | int8 | 64 |  | √ | 0 | 实例内码 |
| 8 | fretrycount | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 9 | fappid | 应用内码 | int8 | 64 |  | √ | 0 | 应用内码 |
| 10 | fmodifyid | 最后修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 12 | fstatus | 消息类型 | varchar | 25 |  | √ | ' ' | 消息类型,枚举: NEW :待办 NEW_XB :协办 DEAL :已办 DELETE :删除 NOTICE :通知 PDELETE :删除流程 PHAVEDEAL :完成流程 |
| 13 | fuserids | 消息接收人ID | varchar | 1000 |  | √ | ' ' | 消息接收人ID |
| 14 | fcorpid | 企业团队ID | varchar | 80 |  | √ | ' ' | 企业团队ID |
| 15 | fappname | 应用名称 | varchar | 50 |  | √ | ' ' | 应用名称 |
| 16 | fmessagebody_tag | 消息体数据_详情 | text | 0 |  |  | null | 消息体数据_详情 |
| 17 | fcreateid | 消息发送人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftaskid | 任务内码 | int8 | 64 |  | √ | 0 | 任务内码 |
| 19 | fentryrole | 渠道 | varchar | 50 |  | √ | ' ' | 渠道,枚举: 0 :协同云 1 :企业微信 2 :钉钉 3 :WeLink 6 :飞书 9 :金蝶云APP 12 :Lark 5 :微信小程序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bzjclog_fcreattime |  | fcreatetime |
| 2 | pk_mbase_bzjclog |  | fid |
| 3 | idx_mbase_bzjclog_fprocinstid |  | fprocinstid |
| 4 | idx_mbase_bzjclog_ftaskid |  | ftaskid |

---

## 单据体-子表 t_mbase_bzjclogentry

- **表名称：** 单据体-子表
- **表名：** t_mbase_bzjclogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuccess | 是否成功 | varchar | 1 |  | √ | ' ' | 是否成功 |
| 3 | fresponse_tag | 消息结果_详情 | text | 0 |  |  | null | 消息结果_详情 |
| 4 | ferrorcode | 错误码 | varchar | 30 |  | √ | ' ' | 错误码 |
| 5 | frecordid | 记录内码 | varchar | 100 |  |  | ' ' | 记录内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftouser | 消息接收人ID | varchar | 1000 |  | √ | ' ' | 消息接收人ID |
| 8 | fresponse | 消息结果 | varchar | 255 |  |  | ' ' | 消息结果 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsendmessage | 发送消息 | varchar | 255 |  |  | ' ' | 发送消息 |
| 11 | fsendmessage_tag | 发送消息_详情 | text | 0 |  |  | null | 发送消息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_bzjclogentry_fid |  | fid |
| 2 | pk_mbase_bzjclogentry |  | fentryid |
