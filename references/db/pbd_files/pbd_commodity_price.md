# 大宗商品市场价格单-pbd_commodity_price

## 大宗商品市场价格单-主表 t_pbd_commodity_price

- **表名称：** 大宗商品市场价格单-主表
- **表名：** t_pbd_commodity_price

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricetype | 价格类型 | varchar | 50 |  | √ | ' ' | 价格类型 |
| 3 | fmarketid | 市场配置 | int8 | 64 |  | √ | 0 | [大宗商品市场配置 pbd_commodity_market](../pbd_files/pbd_commodity_market.md) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | funitname | 单位名称 | varchar | 50 |  | √ | ' ' | 单位名称 |
| 8 | fprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 9 | fcurid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_commodity_p_materialid |  | fmaterialid |
| 2 | idx_pbd_commodity_price_date |  | fdate |
| 3 | pk_pbd_commodity_price |  | fid |
