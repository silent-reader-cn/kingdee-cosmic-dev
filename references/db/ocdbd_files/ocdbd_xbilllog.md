# 变更日志-ocdbd_xbilllog

## 变更日志-主表 t_ocdbd_xbilllog

- **表名称：** 变更日志-主表
- **表名：** t_ocdbd_xbilllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 3 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 4 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fxbilljson | 变更单Json | varchar | 512 |  | √ | ' ' | 变更单Json |
| 6 | fxmdjson_tag | 变更md文本_详情 | text | 0 |  |  | null | 变更md文本_详情 |
| 7 | fxmdjson | 变更md文本 | varchar | 512 |  | √ | ' ' | 变更md文本 |
| 8 | fxbillchangejson_tag | 变更内容json_详情 | text | 0 |  |  | null | 变更内容json_详情 |
| 9 | fsrcbillversion | 源单版本 | int8 | 64 |  | √ | 0 | 源单版本 |
| 10 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 11 | fsrcbilljson | 源单Json | varchar | 512 |  | √ | ' ' | 源单Json |
| 12 | fbiztime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 13 | fxbillchangejson | 变更内容json | varchar | 512 |  | √ | ' ' | 变更内容json |
| 14 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fxbillentity | 变更单实体 | varchar | 80 |  | √ | ' ' | 变更单实体 |
| 16 | fsrcbillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 17 | fxbilljson_tag | 变更单Json_详情 | text | 0 |  |  | null | 变更单Json_详情 |
| 18 | fsrcbilljson_tag | 源单Json_详情 | text | 0 |  |  | null | 源单Json_详情 |
| 19 | fxreason | 变更原因 | varchar | 1000 |  | √ | ' ' | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_xbilllog |  | fid |
| 2 | idx_ocdbd_xbilllog_srcbillid |  | fsrcbillid |
| 3 | idx_ocdbd_xbilllog_xbillid |  | fxbillid |
