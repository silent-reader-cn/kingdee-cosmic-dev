# 我的购物车单-mal_shopcartbill

## 我的购物车单-主表 t_mal_shopcart

- **表名称：** 我的购物车单-主表
- **表名：** t_mal_shopcart

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 订货数量 | numeric | 19 | 6 | √ | 0.000000 | 订货数量 |
| 3 | ftaxamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fgoodsimg | 商品图片 | varchar | 255 |  | √ | ' ' | 商品图片 |
| 6 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 8 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 9 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fgoodsource | 商品来源 | bpchar | 1 |  | √ | ' ' | 商品来源,枚举: 1 :自建 2 :京东 3 :其他 |
| 12 | fbilldate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 13 | ftaxprice | 价格 | numeric | 23 | 10 | √ | 0.0000000000 | 价格 |
| 14 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 15 | famount | 不含税金额 | numeric | 19 | 6 | √ | 0.000000 | 不含税金额 |
| 16 | fstockqty | 库存数量 | numeric | 19 | 6 | √ | 0.000000 | 库存数量 |
| 17 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 18 | fsupplierid | 所属供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 20 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 21 | fstockstatus | 库存状态 | bpchar | 1 |  | √ | ' ' | 库存状态,枚举: 1 :充足 2 :有限 9 :不足 |
| 22 | fpersonid | 所属人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 24 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_shopcart_pkey |  | fid |
| 2 | idx_mal_shopcart_fbilldate |  | fbilldate |
| 3 | idx_mal_shopcart_fgoodsid |  | fgoodsid |
| 4 | idx_mal_shopcart_fpersonid |  | fpersonid |
