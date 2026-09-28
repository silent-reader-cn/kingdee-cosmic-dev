# 库存计划供应单据-invp_supply_bill

## 库存计划供应单据-主表 t_invp_supply_bill

- **表名称：** 库存计划供应单据-主表
- **表名：** t_invp_supply_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 供应基本数量 | numeric | 23 | 10 | √ | 0 | 供应基本数量 |
| 3 | fsupplywarehouseid | 供应仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 4 | fisinvpdata | 是否即时库存 | bpchar | 1 |  | √ | '0' | 是否即时库存 |
| 5 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fsupplydate | 供应日期 | timestamp | 0 |  |  | null | 供应日期 |
| 8 | fsrcbill | 供应单据 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fsupplylocationid | 供应仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 10 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | flinenum | 供应单据分录行号 | int4 | 32 |  | √ | 0 | 供应单据分录行号 |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 13 | fflexarea | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbillentryid | 供应单据分录ID | int8 | 64 |  | √ | 0 | 供应单据分录ID |
| 15 | fbillid | 供应单据ID | int8 | 64 |  | √ | 0 | 供应单据ID |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillno | 供应单据编号 | varchar | 50 |  | √ | ' ' | 供应单据编号 |
| 19 | fplancalnum | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_supply_bill |  | fid |
