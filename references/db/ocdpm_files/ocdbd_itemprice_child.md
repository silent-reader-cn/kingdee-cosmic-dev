# 组合商品价格-ocdbd_itemprice_child

## 组合商品价格-主表 t_ocdbd_itemprice_child

- **表名称：** 组合商品价格-主表
- **表名：** t_ocdbd_itemprice_child

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 商品价格 | int8 | 64 |  | √ | 0 | [商品价格 ocdbd_item_price](../ocdpm_files/ocdbd_item_price.md) |
| 2 | fchild | fchild | int8 | 64 |  | √ | 0 | id |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fcombitemid | 组合商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fmaterialattrid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fsubqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fprice | 销售价格 | numeric | 23 | 10 | √ | 0 | 销售价格 |
| 10 | fitemid | 子件商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 11 | fpricemode | 定价方式 | bpchar | 1 |  | √ | '0' | 定价方式,枚举: 0 :总价分摊 1 :自由定价 2 :比例定价 |
| 12 | fproportion | 比例 | numeric | 23 | 10 | √ | 0 | 比例 |
| 13 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fchild | fchild |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_itemprice_child |  | fchild |
| 2 | idx_ocdbd_itempricechild_fid |  | fid |
