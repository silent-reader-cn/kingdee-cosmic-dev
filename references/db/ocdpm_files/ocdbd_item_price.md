# 商品价格-ocdbd_item_price

## 商品价格-主表 t_ocdbd_item_price

- **表名称：** 商品价格-主表
- **表名：** t_ocdbd_item_price

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialassistattrid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsaleprice | 销售价格 | numeric | 23 | 10 | √ | 0 | 销售价格 |
| 6 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :保存 1 :审核 2 :禁用 |
| 7 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fitemsaleattrid | 商品销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fchangecount | 变更记录 | int4 | 32 |  | √ | 0 | 变更记录 |
| 12 | fchannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 13 | flowprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 14 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbegindate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | [渠道价格类型 ocdbd_price_type](../ocdpm_files/ocdbd_price_type.md) |
| 21 | fitemid | 商品名称 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 22 | fassistattrid | fassistattrid | int8 | 64 |  | √ | 0 |  |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_itemprice_etime |  | fenddate |
| 2 | idx_ocdbd_itemprice_ctime |  | fcreatedate |
| 3 | idxocdbd_itemprice_chl |  | fchannelid |
| 4 | idx_ocdbd_itemprice_btime |  | fbegindate |
| 5 | idx_ocdbd_itemprice_num |  | fnumber |
| 6 | pk_ocdbd_item_price |  | fid |
| 7 | idx_ocdbd_itemprice_iua |  | fitemid,funitid,fassistattrid |
| 8 | idx_ocdbd_itemprice_sorg |  | fsaleorgid |
