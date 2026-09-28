# 预留转移记录-reserve_transrecord

## 预留转移记录-主表 t_reserve_transrecord

- **表名称：** 预留转移记录-主表
- **表名：** t_reserve_transrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsrcbillno | 源单单据编码 | varchar | 255 |  | √ | ' ' | 源单单据编码 |
| 4 | ftargetbillentryid | 目标单分录内码 | int8 | 64 |  | √ | 0 | 目标单分录内码 |
| 5 | fsrcbillid | 源单单据内码 | int8 | 64 |  | √ | 0 | 源单单据内码 |
| 6 | fsrcreserverecordid | 源预留记录内码 | int8 | 64 |  | √ | 0 | 源预留记录内码 |
| 7 | ftarentryseq | 目标单分录行号 | int4 | 32 |  | √ | 0 | 目标单分录行号 |
| 8 | ftargetbillno | 目标单单据编码 | varchar | 255 |  | √ | ' ' | 目标单单据编码 |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsrcbillobj | 源单单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fsrcbillentryid | 源单分录内码 | int8 | 64 |  | √ | 0 | 源单分录内码 |
| 12 | ftargetbillid | 目标单单据内码 | int8 | 64 |  | √ | 0 | 目标单单据内码 |
| 13 | fsrcentryseq | 源单分录行号 | int4 | 32 |  | √ | 0 | 源单分录行号 |
| 14 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 15 | ftranstype | 转移类型 | varchar | 10 |  | √ | ' ' | 转移类型,枚举: 1 :在途-在库 2 :在库-在库 3 :需求-需求 4 :在途-在途 6 :下推创建 |
| 16 | ftargetbillobj | 目标单单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fbaseqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_transrecord |  | fid |
| 2 | idx_reserve_transrecord_teid |  | ftargetbillentryid |
