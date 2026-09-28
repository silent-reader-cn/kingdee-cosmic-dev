# 库存查询-scp_inventory

## 库存查询-主表 t_pur_inventory

- **表名称：** 库存查询-主表
- **表名：** t_pur_inventory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 3 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 4 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 5 | fgoodsid | fgoodsid | int8 | 64 |  | √ | 0 |  |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 10 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 11 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 13 | fownerid | 货主 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 16 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 17 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 18 | fmaterialdesc | fmaterialdesc | varchar | 255 |  | √ | ' ' |  |
| 19 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 20 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_inventory_fmaterialid |  | fmaterialid |
| 2 | t_pur_inventory_pkey |  | fid |
