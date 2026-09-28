# 升级通知消息-gxyportal_upnotification

## 升级通知消息-主表 t_xkportal_upnotification

- **表名称：** 升级通知消息-主表
- **表名：** t_xkportal_upnotification

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmsgend | 消息有效期结束时间 | timestamp | 0 |  |  | null | 消息有效期结束时间 |
| 3 | fagainmsgtime | 消息再次提醒时间 | timestamp | 0 |  |  | null | 消息再次提醒时间 |
| 4 | fpatchtype | 补丁类型 | int4 | 32 |  | √ | 1 | 补丁类型 |
| 5 | fupdateendtime | 更新结束时间 | timestamp | 0 |  |  | null | 更新结束时间 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fhighlighttext | 高亮文本 | varchar | 255 |  |  | ' ' | 高亮文本 |
| 8 | fupdatestarttime | 更新开始时间 | timestamp | 0 |  |  | null | 更新开始时间 |
| 9 | fisactive | 当前有效 | bpchar | 1 |  | √ | '1' | 当前有效 |
| 10 | ftitle | 消息标题 | varchar | 50 |  | √ | ' ' | 消息标题 |
| 11 | fpatchtpl | 是否最新模板 | bpchar | 1 |  | √ | '0' | 是否最新模板 |
| 12 | fchangecount | 变更数量 | int4 | 32 |  | √ | 0 | 变更数量 |
| 13 | fmsgstart | 消息有效期开始时间 | timestamp | 0 |  |  | null | 消息有效期开始时间 |
| 14 | fcontent | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 15 | fversion | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkportal_upnotification |  | fid |
| 2 | idx_t_upnotification_isactive |  | fisactive |
