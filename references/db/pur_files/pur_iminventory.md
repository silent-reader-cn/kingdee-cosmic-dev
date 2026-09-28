# 即时库存后台表-pur_iminventory

## 即时库存后台表-主表 t_pur_iminventory

- **表名称：** 即时库存后台表-主表
- **表名：** t_pur_iminventory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | foutqty | 缺货数量 | numeric | 23 | 10 | √ | 0 | 缺货数量 |
| 4 | finqty | 发生在途数量 | numeric | 23 | 10 | √ | 0 | 发生在途数量 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 7 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fsourceid | 来源单据id | varchar | 80 |  | √ | ' ' | 来源单据id |
| 10 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 11 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 12 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :缺货 B :正常 C :超量 |
| 15 | fmaxqty | 最大库存 | numeric | 23 | 10 | √ | 0 | 最大库存 |
| 16 | frecorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 18 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | frepqty | 申请补货数量 | numeric | 23 | 10 | √ | 0 | 申请补货数量 |
| 20 | forderqty | 订单待发数量 | numeric | 23 | 10 | √ | 0 | 订单待发数量 |
| 21 | fminqty | 最小库存 | numeric | 23 | 10 | √ | 0 | 最小库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_iminventory_matid |  | fmaterialid |
| 2 | idx_pur_iminventory_frecorgid |  | frecorgid |
| 3 | pk_t_pur_iminventory |  | fid |
