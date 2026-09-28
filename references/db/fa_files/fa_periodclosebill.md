# 自动月结-fa_periodclosebill

## 自动月结-主表 t_fa_assetbook

- **表名称：** 自动月结-主表
- **表名：** t_fa_assetbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexchangetableid | fexchangetableid | int8 | 64 |  | √ | 0 |  |
| 3 | facctperiodtypeid | facctperiodtypeid | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdepresystemid | fdepresystemid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdepreuse | 折旧用途 | int8 | 64 |  | √ | 0 | [折旧用途 fa_depreuse](../fa_files/fa_depreuse.md) |
| 8 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fpcstatus | fpcstatus | varchar | 50 |  | √ | 'INIT' |  |
| 12 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 13 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 14 | fxkpolicyid | fxkpolicyid | int8 | 64 |  | √ | 0 |  |
| 15 | fcurrentperiodid | 当前期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | fname | varchar | 100 |  |  | ' ' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fdepresystementryid | fdepresystementryid | int8 | 64 |  | √ | 0 |  |
| 21 | fxkisenabled | fxkisenabled | bpchar | 1 |  | √ | '0' |  |
| 22 | fenableperiodid | fenableperiodid | int8 | 64 |  | √ | 0 |  |
| 23 | fisgroupbook | fisgroupbook | bpchar | 1 |  | √ | '0' |  |
| 24 | fpcsubstatus | fpcsubstatus | varchar | 50 |  | √ | 'INIT' |  |
| 25 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 26 | fismainbook | fismainbook | bpchar | 1 |  | √ | '0' |  |
| 27 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 28 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 29 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 30 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_assetbook_master |  | fmasterid |
| 2 | idx_t_fa_assetbook_createorg |  | fcreateorgid |
| 3 | t_fa_assetbook_pkey |  | fid |
| 4 | idx_fa_assboo_fnumber |  | fnumber |
