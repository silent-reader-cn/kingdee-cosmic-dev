# 变更详情明细-bdtaxr_changeresumedetail

## 变更详情明细-主表 t_bdtaxr_changedetail

- **表名称：** 变更详情明细-主表
- **表名：** t_bdtaxr_changedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 3 | fsrcbillsubversion | 源单子版本号 | varchar | 50 |  | √ | ' ' | 源单子版本号 |
| 4 | fxbillno | 变更单编号 | varchar | 50 |  | √ | ' ' | 变更单编号 |
| 5 | fsrcbillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fcrdheadjson | 单据头变更履历json | varchar | 255 |  | √ | ' ' | 单据头变更履历json |
| 8 | fcurrentpagenum5 | 当前页 | int8 | 64 |  | √ | 0 | 当前页 |
| 9 | fsrcbillversion | 变更版本 | varchar | 50 |  | √ | ' ' | 变更版本 |
| 10 | fcurrentpagenum4 | 当前页 | int8 | 64 |  | √ | 0 | 当前页 |
| 11 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 12 | fcrdentryjson | 单据体变更履历json | varchar | 255 |  | √ | ' ' | 单据体变更履历json |
| 13 | fxcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcurrentpagenum3 | 当前页 | int8 | 64 |  | √ | 0 | 当前页 |
| 15 | fxbillentity | 变更单实体 | varchar | 50 |  | √ | ' ' | 变更单实体 |
| 16 | fcurrentpagenum2 | 当前页 | int8 | 64 |  | √ | 0 | 当前页 |
| 17 | fcurrentpagenum1 | 当前页 | int8 | 64 |  | √ | 0 | 当前页 |
| 18 | fcurrentpagenum0 | 当前页 | int8 | 64 |  | √ | 0 | 当前页 |
| 19 | fcrdentryjson_tag | 单据体变更履历json_详情 | text | 0 |  |  | null | 单据体变更履历json_详情 |
| 20 | fsrcbillentity | 源单实体 | varchar | 50 |  | √ | ' ' | 源单实体 |
| 21 | fxreason | 变更原因 | varchar | 600 |  | √ | ' ' | 变更原因 |
| 22 | fcrdheadjson_tag | 单据头变更履历json_详情 | text | 0 |  |  | null | 单据头变更履历json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_changde_xbid |  | fxbillid |
| 2 | pk_bdtaxr_changedetail |  | fid |
