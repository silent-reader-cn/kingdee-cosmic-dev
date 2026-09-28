# 生产工单数量记录-pom_orderqtyrecord

## 生产工单数量记录-主表 t_pom_orderqtyrecord

- **表名称：** 生产工单数量记录-主表
- **表名：** t_pom_orderqtyrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisproduction | 是否投产 | bpchar | 1 |  | √ | '0' | 是否投产 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | forderid | 工单f7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 6 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fnewqty | 新数量 | numeric | 23 | 10 | √ | 0 | 新数量 |
| 8 | fmaterielmasterid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fnewbaseqty | 新基本数量 | numeric | 23 | 10 | √ | 0 | 新基本数量 |
| 10 | flogid | 日志记录id | int8 | 64 |  | √ | 0 | 日志记录id |
| 11 | fsrctype | 来源类型 | varchar | 5 |  | √ | ' ' | 来源类型,枚举: A :工单改制 |
| 12 | forderentryid | 工单分录f7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | foldqty | 旧数量 | numeric | 23 | 10 | √ | 0 | 旧数量 |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | foldbaseqty | 旧基本数量 | numeric | 23 | 10 | √ | 0 | 旧基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_orderqtyrecord_oeid |  | forderentryid |
| 2 | pk_pom_orderqtyrecord |  | fid |
