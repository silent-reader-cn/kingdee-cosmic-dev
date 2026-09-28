# 商品条形码-ocdbd_item_barcode

## 商品条形码-主表 t_ocdbd_item_barcode

- **表名称：** 商品条形码-主表
- **表名：** t_ocdbd_item_barcode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fretailprice | 参考零售价 | numeric | 23 | 10 | √ | 0 | 参考零售价 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | fbarcode | 条形码 | varchar | 80 |  | √ | ' ' | 条形码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fonlineprice | 参考线上价 | numeric | 23 | 10 | √ | 0 | 参考线上价 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :创建 B :审核中 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmemberprice | 参考会员价 | numeric | 23 | 10 | √ | 0 | 参考会员价 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fsellingprice | 参考供货价 | numeric | 23 | 10 | √ | 0 | 参考供货价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_item_barcode |  | fid |
| 2 | idx_ocdbd_itembarcode_itemid |  | fitemid |
