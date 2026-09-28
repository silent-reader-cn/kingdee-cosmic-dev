# 外部系统API消息-pbd_apimessage

## 外部系统API消息-主表 t_mal_apimessage

- **表名称：** 外部系统API消息-主表
- **表名：** t_mal_apimessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresult_tag | 消息详情_详情 | text | 0 |  |  | null | 消息详情_详情 |
| 3 | fstatus | 消息消费状态 | bpchar | 1 |  | √ | ' ' | 消息消费状态,枚举: 0 :未消费 1 :已消费 |
| 4 | fmsgid | 消息ID | varchar | 80 |  | √ | ' ' | 消息ID |
| 5 | fretrytimes | 自动重试次数 | int4 | 32 |  | √ | 0 | 自动重试次数 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmsgtime | 消息推送时间 | timestamp | 0 |  |  | null | 消息推送时间 |
| 8 | fresult | 消息详情 | text | 0 |  |  | null | 消息详情 |
| 9 | fsystype | 系统类型 | bpchar | 1 |  | √ | ' ' | 系统类型,枚举: 1 :自建 2 :京东 3 :苏宁 4 :得力 5 :西域 6 :晨光 7 :京东工业品 8 :鑫方盛 9 :震坤行 |
| 10 | fmsgtype | 消息类型 | varchar | 50 |  | √ | ' ' | 消息类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_apimessage |  | fid |
| 2 | idx_mal_apimessage_fmsgtime |  | fmsgtime |
| 3 | idx_mal_apimessage_fmsgid |  | fmsgid |
