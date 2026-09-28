# 实体库存-ococic_entityinventory

## 实体库存-主表 t_ococic_entityinv

- **表名称：** 实体库存-主表
- **表名：** t_ococic_entityinv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | freservebaseqty | 预留量(基本单位) | numeric | 23 | 10 | √ | 0 | 预留量(基本单位) |
| 4 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | freserveqty | 预留量 | numeric | 23 | 10 | √ | 0 | 预留量 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bos_org :核算组织 bd_customer :客户 bd_supplier :供应商 |
| 10 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 11 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 12 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | favbbbaseqty | 可用量(基本单位) | numeric | 23 | 10 | √ | 0 | 可用量(基本单位) |
| 14 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_customer :客户 bd_supplier :供应商 |
| 15 | favbbqty | 可用量 | numeric | 23 | 10 | √ | 0 | 可用量 |
| 16 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fbaseqty | 数量(基本单位) | numeric | 23 | 10 | √ | 0 | 数量(基本单位) |
| 19 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ococic_entityinv |  | fid |
| 2 | idx_ococic_entityinv_item |  | fitemid |
