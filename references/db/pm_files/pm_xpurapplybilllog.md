# 采购申请单变更日志-pm_xpurapplybilllog

## 采购申请单变更日志-主表 t_pm_xpurapplybilllog

- **表名称：** 采购申请单变更日志-主表
- **表名：** t_pm_xpurapplybilllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 3 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 4 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 5 | fxbilljson | 变更单Json | varchar | 512 |  |  | null | 变更单Json |
| 6 | fxmdjson_tag | 变更md文本_详情 | text | 0 |  |  | null | 变更md文本_详情 |
| 7 | fxmdjson | 变更md文本 | varchar | 512 |  |  | null | 变更md文本 |
| 8 | fsrcbillversion | 源单版本 | varchar | 30 |  | √ | ' ' | 源单版本 |
| 9 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 10 | fsrcbilljson | 源单Json | varchar | 512 |  |  | null | 源单Json |
| 11 | fbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 12 | fcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fxbillentity | 变更单实体 | varchar | 36 |  | √ | ' ' | 变更单实体 |
| 14 | fsrcbillentity | 源单实体 | varchar | 36 |  | √ | ' ' | 源单实体 |
| 15 | fxbilljson_tag | 变更单Json_详情 | text | 0 |  |  | null | 变更单Json_详情 |
| 16 | fsrcbilljson_tag | 源单Json_详情 | text | 0 |  |  | null | 源单Json_详情 |
| 17 | fxreason | 变更原因 | varchar | 512 |  |  | null | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_xpurapplybilllog |  | fid |
| 2 | idx_pm_xpurapplybilllog_billno |  | fxbillno |
