# 商品价格-ocdbd_item_price

## 商品价格-主表 t_ocdbd_item_price

- **表名称：** 商品价格-主表
- **表名：** t_ocdbd_item_price

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmaterialassistattrid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | 渠道价格类型 ocdbd_price_type |
| 8 | fitemid | 商品名称 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 9 | fsaleprice | 销售价格 | numeric | 23 | 10 | √ | 0 | 销售价格 |
| 10 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :保存 1 :审核 2 :禁用 |
| 11 | fassistattrid | fassistattrid | int8 | 64 |  | √ | 0 |  |
| 12 | fitemsaleattrid | 商品销售属性 | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 13 | fchangecount | 变更记录 | int4 | 32 |  | √ | 0 | 变更记录 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fchannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | flowprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_itemprice_num |  | fnumber |
| 2 | pk_ocdbd_item_price |  | fid |
| 3 | idx_ocdbd_itemprice_iua |  | fitemid,funitid,fassistattrid |
| 4 | idxocdbd_itemprice_chl |  | fchannelid |
| 5 | idx_ocdbd_itemprice_sorg |  | fsaleorgid |
