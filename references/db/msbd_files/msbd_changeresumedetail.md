# 变更履历详情-msbd_changeresumedetail

## 变更履历详情-主表 t_msbd_changeresumedetail

- **表名称：** 变更履历详情-主表
- **表名：** t_msbd_changeresumedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 3 | fsrcbillsubversion | 源单子版本号 | varchar | 30 |  | √ | ' ' | 源单子版本号 |
| 4 | fxbillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 5 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fcrdheadjson | 单据头变更履历json | varchar | 512 |  |  | null | 单据头变更履历json |
| 8 | fsrcbillversion | 变更版本 | varchar | 30 |  | √ | ' ' | 变更版本 |
| 9 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 10 | fcrdentryjson | 单据体变更履历json | varchar | 512 |  |  | null | 单据体变更履历json |
| 11 | fxcreatorid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fxbillentity | 变更单实体 | varchar | 80 |  | √ | ' ' | 变更单实体 |
| 13 | fcrdentryjson_tag | 单据体变更履历json_详情 | text | 0 |  |  | null | 单据体变更履历json_详情 |
| 14 | fsrcbillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 15 | fxreason | 变更原因 | varchar | 1000 |  |  | null | 变更原因 |
| 16 | fcrdheadjson_tag | 单据头变更履历json_详情 | text | 0 |  |  | null | 单据头变更履历json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_crdetail_srcbillld |  | fsrcbillid |
| 2 | pk_t_msbd_changeresumedetail |  | fid |
| 3 | idx_msbd_crdetail_xbillid |  | fxbillid |
