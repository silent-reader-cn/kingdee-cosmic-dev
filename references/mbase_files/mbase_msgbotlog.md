# 群消息日志-mbase_msgbotlog

## 群消息日志-主表 t_mbase_msgbotlog

- **表名称：** 群消息日志-主表
- **表名：** t_mbase_msgbotlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresponseinfo_tag | 返回信息_详情 | text | 0 |  |  | null | 返回信息_详情 |
| 3 | fsendername | 发送人 | varchar | 100 |  | √ | ' ' | 发送人 |
| 4 | frequestinfo_tag | 请求信息_详情 | text | 0 |  |  | null | 请求信息_详情 |
| 5 | fbotnumber | 机器人编码 | varchar | 100 |  | √ | ' ' | 机器人编码 |
| 6 | frequestinfo | 请求信息 | varchar | 255 |  |  | ' ' | 请求信息 |
| 7 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 8 | fstatus | 发送状态 | bpchar | 1 |  | √ | '1' | 发送状态,枚举: 0 :成功 1 :失败 |
| 9 | fresponseinfo | 返回信息 | varchar | 255 |  |  | ' ' | 返回信息 |
| 10 | fbusinessno | 业务编码 | varchar | 100 |  | √ | ' ' | 业务编码 |
| 11 | fbotname | 机器人名称 | varchar | 100 |  | √ | ' ' | 机器人名称 |
| 12 | ftraceno | 跟踪编码 | varchar | 100 |  | √ | ' ' | 跟踪编码 |
| 13 | fsenddatetime | 发送日期 | timestamp | 0 |  |  | null | 发送日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mbase_msgbotlog_02 |  | fbotnumber |
| 2 | idx_mbase_msgbotlog_03 |  | fbotname |
| 3 | idx_mbase_msgbotlog_01 |  | fbusinessno |
| 4 | pk_mbase_msgbotlog |  | fid |
| 5 | idx_mbase_msgbotlog_04 |  | ftraceno |
