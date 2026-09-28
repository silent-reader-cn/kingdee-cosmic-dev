# 同步消息配置-isc_messagepush

## 同步消息配置-主表 t_isc_msg_data

- **表名称：** 同步消息配置-主表
- **表名：** t_isc_msg_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 消息推送名称 | varchar | 30 |  | √ | 'msgpushinfo' | 消息推送名称 |
| 3 | fsendor | fsendor | varchar | 100 |  | √ | ' ' |  |
| 4 | fsendor2 | 消息发送人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fnumber | 消息推送编码 | varchar | 30 |  | √ | 'default' | 消息推送编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_msg_data_pkey |  | fid |
| 2 | idx_isc_msg_data_fname |  | fname |

---

## 单据体-子表 t_isc_msginfo

- **表名称：** 单据体-子表
- **表名：** t_isc_msginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreator | 单据创建人 | varchar | 30 |  | √ | 'No' | 单据创建人 |
| 3 | fexcute | 执行状态 | varchar | 30 |  | √ | '2' | 执行状态,枚举: 1 :成功 2 :失败 3 :部分成功 4 :等待反馈 |
| 4 | fperson | 消息接收人 | text | 0 |  |  | null | 消息接收人 |
| 5 | fguide | 集成方案 | text | 0 |  |  | null | 集成方案,枚举: |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fenable | 开启 | bpchar | 1 |  | √ | '0' | 开启 |
| 8 | fplugin | 业务插件 | text | 0 |  |  | null | 业务插件 |
| 9 | fmsgcontent | 消息内容 | text | 0 |  |  | null | 消息内容 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fchannel | 发送渠道 | varchar | 30 |  | √ | '1' | 发送渠道,枚举: 1 :系统消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_msginfo_pkey |  | fentryid |
| 2 | idx_isc_msginfo_fid |  | fid |
