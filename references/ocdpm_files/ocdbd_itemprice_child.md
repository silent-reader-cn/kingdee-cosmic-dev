# 组合商品价格子件2-ocdbd_itemprice_child

## 组合商品价格子件2-主表 t_ocdbd_itemprice_child

- **表名称：** 组合商品价格子件2-主表
- **表名：** t_ocdbd_itemprice_child

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 商品价格 | int8 | 64 |  | √ | 0 | 商品价格 ocdbd_item_price |
| 2 | fchild | fchild | int8 | 64 |  | √ | 0 | id |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fmaterialattrid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fsubqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 7 | fpricemode | 定价方式 | bpchar | 1 |  | √ | '0' | 定价方式,枚举: 0 :总价分摊 1 :自由定价 2 :比例定价 |
| 8 | fprice | 销售价格 | numeric | 23 | 10 | √ | 0 | 销售价格 |
| 9 | fproportion | 比例 | numeric | 23 | 10 | √ | 0 | 比例 |
| 10 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fchild | fchild |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_itemprice_child |  | fchild |
| 2 | idx_ocdbd_itempricechild_fid |  | fid |
