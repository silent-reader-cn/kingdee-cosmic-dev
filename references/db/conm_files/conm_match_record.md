# 合同匹配记录-conm_match_record

## 合同匹配记录-主表 t_conm_match_record

- **表名称：** 合同匹配记录-主表
- **表名：** t_conm_match_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 4 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 8 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fmatchtype | 匹配类型 | varchar | 50 |  | √ | ' ' | 匹配类型,枚举: qty :数量 amount :金额 |
| 11 | fcuramountandtax | 价税合计（本位币） | numeric | 23 | 10 | √ | 0 | 价税合计（本位币） |
| 12 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 13 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 14 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 15 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_conm_match_record |  | fid |
| 2 | idx_conm_match_record_m0 |  | fmatchtype |
