# 操作日志-ap_oplog

## 操作日志-主表 t_ap_oplog

- **表名称：** 操作日志-主表
- **表名：** t_ap_oplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclientip | 客户端地址 | varchar | 50 |  | √ | ' ' | 客户端地址 |
| 3 | fopname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 4 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 6 | fopdesc_tag | 操作描述_详情 | text | 0 |  |  | null | 操作描述_详情 |
| 7 | fopdesc | 操作描述 | varchar | 255 |  | √ | ' ' | 操作描述 |
| 8 | fbillinfo_tag | 单据信息_详情 | text | 0 |  |  | null | 单据信息_详情 |
| 9 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbizobjid | 操作对象 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fbillinfo | 单据信息 | varchar | 255 |  | √ | ' ' | 单据信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_oplog_pkey |  | fid |
| 2 | idx_ap_oplog_optime |  | foptime |
| 3 | idx_ap_oplog_traceid |  | ftraceid |
| 4 | idx_ap_oplog_billno |  | fbillno |
