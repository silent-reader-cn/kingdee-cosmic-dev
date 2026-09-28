# 销售订单变更日志-sm_xsalorderlog

## 销售订单变更日志-主表 t_sm_xsalorderlog

- **表名称：** 销售订单变更日志-主表
- **表名：** t_sm_xsalorderlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 3 | fsrcbillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 4 | fsrcbillid | 订单ID | int8 | 64 |  | √ | 0 | 订单ID |
| 5 | fxmdjson_tag | 变更md文本_详情 | text | 0 |  |  | null | 变更md文本_详情 |
| 6 | fxbilljson | 变更单Json | varchar | 512 |  |  | null | 变更单Json |
| 7 | fxmdjson | 变更md文本 | varchar | 512 |  |  | null | 变更md文本 |
| 8 | fsrcbillversion | 订单版本 | varchar | 30 |  | √ | ' ' | 订单版本 |
| 9 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 10 | fsrcbilljson | 订单Json | varchar | 512 |  |  | null | 订单Json |
| 11 | fbiztime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 12 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fxbilljson_tag | 变更单Json_详情 | text | 0 |  |  | null | 变更单Json_详情 |
| 14 | fsrcbilljson_tag | 订单Json_详情 | text | 0 |  |  | null | 订单Json_详情 |
| 15 | fxreason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_xsalorderlog_pkey |  | fid |
| 2 | idx_sm_xsalorderlog_billno |  | fxbillno |
