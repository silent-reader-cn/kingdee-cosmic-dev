# 齐套汇总-mpdm_kitting_summary

## 齐套汇总-主表 t_mpdm_kittingsummary

- **表名称：** 齐套汇总-主表
- **表名：** t_mpdm_kittingsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkittingid | 齐套ID | int8 | 64 |  | √ | 0 | 齐套ID |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fnoexecuteqty | 未执行数量 | numeric | 23 | 10 | √ | 0 | 未执行数量 |
| 8 | fsuppliernosubqty | 供应商未交货数量 | numeric | 23 | 10 | √ | 0 | 供应商未交货数量 |
| 9 | fsupplyentryid | 供应单据分录ID | int8 | 64 |  | √ | 0 | 供应单据分录ID |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsuppliernosubbaseqty | 供应商未交货基本数量 | numeric | 23 | 10 | √ | 0 | 供应商未交货基本数量 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | fnoexecutebaseqty | 未执行基本数量 | numeric | 23 | 10 | √ | 0 | 未执行基本数量 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fsupplybillid | 供应单据ID | int8 | 64 |  | √ | 0 | 供应单据ID |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fdemandentryid | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 22 | fsupplybillentity | 供应单据 | varchar | 50 |  | √ | ' ' | 供应单据 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdemandbillentity | 需求单据 | varchar | 50 |  | √ | ' ' | 需求单据 |
| 25 | fdemandbillid | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_kittingsummary_kid |  | fkittingid |
| 2 | idx_mpdm_kittingsummary_deid |  | fdemandentryid |
| 3 | pk_t_mpdm_kittingsummary |  | fid |
