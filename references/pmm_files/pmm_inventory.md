# 库存查询-pmm_inventory

## 库存查询-主表 t_mal_inventory

- **表名称：** 库存查询-主表
- **表名：** t_mal_inventory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 现有库存量 | numeric | 19 | 6 | √ | 0.000000 | 现有库存量 |
| 3 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品管理 pmm_prodmanage |
| 5 | flockedqty | 锁定库存量 | numeric | 19 | 6 | √ | 0.000000 | 锁定库存量 |
| 6 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_goodsclass |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | favailableqty | 可用库存量 | numeric | 19 | 6 | √ | 0.000000 | 可用库存量 |
| 9 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_inventory_pkey |  | fid |
| 2 | idx_mal_inv_fsupplierid |  | fsupplierid |
| 3 | idx_mal_inv_fgoodsid |  | fgoodsid |
| 4 | idx_mal_inv_fbizpartnerid |  | fbizpartnerid |
