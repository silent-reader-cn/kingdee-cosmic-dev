# 生产用料清单变更日志-pom_xmftstocklog

## 生产用料清单变更日志-主表 t_pom_xmftstocklog

- **表名称：** 生产用料清单变更日志-主表
- **表名：** t_pom_xmftstocklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbillno | 变更单编号 | varchar | 50 |  | √ | ' ' | 变更单编号 |
| 3 | fsrcbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 4 | fsrcbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 5 | fxbilljson | 变更单Json | varchar | 255 |  | √ | ' ' | 变更单Json |
| 6 | fxmdjson_tag | 变更md文本_详情 | text | 0 |  |  | null | 变更md文本_详情 |
| 7 | fxmdjson | 变更md文本 | varchar | 255 |  | √ | ' ' | 变更md文本 |
| 8 | fsrcbillversion | 单据版本 | int8 | 64 |  | √ | 0 | 单据版本 |
| 9 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 10 | fsrcbilljson | 订单Json | varchar | 255 |  | √ | ' ' | 订单Json |
| 11 | fbiztime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 12 | fsrcbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 13 | fxbillentryseq | 变更单分录行号 | varchar | 50 |  | √ | ' ' | 变更单分录行号 |
| 14 | fsrcbillentryseq | 单据分录行号 | varchar | 50 |  | √ | ' ' | 单据分录行号 |
| 15 | fxbillentryid | 变更单分录ID | int8 | 64 |  | √ | 0 | 变更单分录ID |
| 16 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fxbilljson_tag | 变更单Json_详情 | text | 0 |  |  | null | 变更单Json_详情 |
| 18 | fsrcbilljson_tag | 订单Json_详情 | text | 0 |  |  | null | 订单Json_详情 |
| 19 | fentrychangetype | 变更方式 | varchar | 30 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 20 | fxreason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_xmftstocklog_pkey |  | fid |
| 2 | idx_pom_xmftstocklog_fk |  | fxbillid |
