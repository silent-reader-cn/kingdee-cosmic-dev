# 消耗明细-scp_consumpt

## 消耗明细-主表 t_pur_consumpt

- **表名称：** 消耗明细-主表
- **表名：** t_pur_consumpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 消耗数量 | numeric | 19 | 6 | √ | 0.000000 | 消耗数量 |
| 3 | fgoodsid | fgoodsid | int8 | 64 |  | √ | 0 |  |
| 4 | fmaterialid | 商品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | finvqty | 开票数量 | numeric | 19 | 6 | √ | 0.000000 | 开票数量 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fentryseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 10 | fgoodsdesc | fgoodsdesc | varchar | 255 |  | √ | ' ' |  |
| 11 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | flotid | 批号 | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 14 | fsuplot | 销售方批号 | varchar | 80 |  | √ | ' ' | 销售方批号 |
| 15 | fbillid | fbillid | int8 | 64 |  | √ | 0 |  |
| 16 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 17 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fsettleqty | 结算数量 | numeric | 19 | 6 | √ | 0.000000 | 结算数量 |
| 19 | fmaterialdesc | fmaterialdesc | varchar | 255 |  | √ | ' ' |  |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fpayqty | 付款数量 | numeric | 19 | 6 | √ | 0.000000 | 付款数量 |
| 22 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 23 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_consumpt_pkey |  | fid |
| 2 | idx_pur_consumpt_fuseorgid |  | fuseorgid |
| 3 | idx_pur_consumpt_fmaterialid |  | fmaterialid |
