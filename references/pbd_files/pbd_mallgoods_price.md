# 电商商品价格-pbd_mallgoods_price

## 电商商品价格-主表 t_mal_goods_price

- **表名称：** 电商商品价格-主表
- **表名：** t_mal_goods_price

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiscountrate | 折扣率 | numeric | 19 | 6 | √ | 0.000000 | 折扣率 |
| 3 | ftaxrate | 税率 | numeric | 19 | 6 | √ | 0.000000 | 税率 |
| 4 | fmallgoodsid | 电商商品 | int8 | 64 |  | √ | 0 | 电商商品 pbd_mallgoods |
| 5 | ftaxprice | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 6 | fmallprice | 电商价 | numeric | 23 | 10 | √ | 0.0000000000 | 电商价 |
| 7 | fnakedprice | 不含税价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税价 |
| 8 | fprice | 结算价 | numeric | 23 | 10 | √ | 0.0000000000 | 结算价 |
| 9 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goods_price |  | fid |
| 2 | idx_mal_goods_price_fmal_ftime |  | fmallgoodsid,fmodifytime |
