# 供应商库存查询-pur_stock

## 供应商库存查询-主表 t_pur_supplierstock

- **表名称：** 供应商库存查询-主表
- **表名：** t_pur_supplierstock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fupdatelog | 更新记录 | varchar | 100 |  | √ | ' ' | 更新记录 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | forderqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 8 | finventoryqty | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 9 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_supplierstock |  | fid |
| 2 | idx_pur_supplier_stock |  | fsupplierid |
