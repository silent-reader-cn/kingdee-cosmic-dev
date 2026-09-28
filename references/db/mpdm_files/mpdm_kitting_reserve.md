# 齐套预留-mpdm_kitting_reserve

## 齐套预留-主表 t_mpdm_kittingreserve

- **表名称：** 齐套预留-主表
- **表名：** t_mpdm_kittingreserve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkittingid | 齐套ID | int8 | 64 |  | √ | 0 | 齐套ID |
| 3 | fsupplybaseqty | 供应基本数量 | numeric | 23 | 10 | √ | 0 | 供应基本数量 |
| 4 | freservetype | 预留类型 | varchar | 5 |  | √ | ' ' | 预留类型,枚举: 1 :强预留 0 :弱预留 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 7 | fbalentryid | 供应分录ID | int8 | 64 |  | √ | 0 | 供应分录ID |
| 8 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fsentryseq | 供应分录序号 | int4 | 32 |  | √ | 0 | 供应分录序号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 物料（主数据） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbalid | 供应ID | int8 | 64 |  | √ | 0 | 供应ID |
| 19 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 23 | fsbillnum | 供应单据编号 | varchar | 50 |  | √ | ' ' | 供应单据编号 |
| 24 | fsupplytime | 供应时间 | timestamp | 0 |  |  | null | 供应时间 |
| 25 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 26 | fbalobj | 供应对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 27 | fbillentryid | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 28 | fbillid | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |
| 29 | fbaseqty | 预留基本数量 | numeric | 23 | 10 | √ | 0 | 预留基本数量 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_kittingreserve |  | fid |
| 2 | idx_kitting_reserve |  | fkittingid |
