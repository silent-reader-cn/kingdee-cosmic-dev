# 报账初始化记录-dhc_datainitrecord

## 报账初始化记录-主表 t_dhc_datainitrecord

- **表名称：** 报账初始化记录-主表
- **表名：** t_dhc_datainitrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finitamount | 已初始化单据数 | int8 | 64 |  | √ | 0 | 已初始化单据数 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbilltotal | 单据总数 | int8 | 64 |  | √ | 0 | 单据总数 |
| 5 | ffailuretime | 失败数据的创建日期 | text | 0 |  |  | null | 失败数据的创建日期 |
| 6 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fexestatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 1 :执行中 2 :初始化成功 3 :初始化失败 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ffinishtime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 13 | fbillid | 初始化单据 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 14 | ffailuretime_tag | 失败数据的创建日期_详情 | text | 0 |  |  | null | 失败数据的创建日期_详情 |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsaveamount | 成功初始化单据数 | int8 | 64 |  | √ | 0 | 成功初始化单据数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_datinitrecord_blid |  | fbillid |
| 2 | t_dhc_datainitrecord_pkey |  | fid |
