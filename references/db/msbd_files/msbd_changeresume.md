# 变更履历表-msbd_changeresume

## 变更履历表-主表 t_msbd_changeresume

- **表名称：** 变更履历表-主表
- **表名：** t_msbd_changeresume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 3 | fsrcbillsubversion | 源单子版本号 | varchar | 30 |  | √ | ' ' | 源单子版本号 |
| 4 | fxbillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 5 | fchangemodelid | 变更模型 | int8 | 64 |  | √ | 0 | [变更模型 plat_changemodel](../msbd_files/plat_changemodel.md) |
| 6 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 7 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 8 | fsrcbillversion | 源单版本 | varchar | 30 |  | √ | ' ' | 源单版本 |
| 9 | fxbillid | 变更单ID | int8 | 64 |  | √ | 0 | 变更单ID |
| 10 | fcurrentchangenumber | 当前变更次数 | int4 | 32 |  | √ | 0 | 当前变更次数 |
| 11 | fsrcbilljson | 源单Json | varchar | 512 |  |  | null | 源单Json |
| 12 | fxcreatorid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fxvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 14 | fxbillentity | 变更单实体 | varchar | 80 |  | √ | ' ' | 变更单实体 |
| 15 | fsrcbillentity | 源单实体 | varchar | 80 |  | √ | ' ' | 源单实体 |
| 16 | fsrcbilljson_tag | 源单Json_详情 | text | 0 |  |  | null | 源单Json_详情 |
| 17 | fxreason | 变更原因 | varchar | 1000 |  |  | null | 变更原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_cresume_srcbillid |  | fsrcbillid |
| 2 | pk_t_msbd_changeresume |  | fid |
| 3 | idx_msbd_cresume_xbillid |  | fxbillid |
