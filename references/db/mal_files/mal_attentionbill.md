# 我的关注单-mal_attentionbill

## 我的关注单-主表 t_mal_attention

- **表名称：** 我的关注单-主表
- **表名：** t_mal_attention

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 订货数量 | numeric | 19 | 6 | √ | 0.000000 | 订货数量 |
| 3 | ftaxamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 4 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 5 | fcurrid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 7 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 8 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fbilldate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 11 | ftaxprice | 价格 | numeric | 23 | 10 | √ | 0.0000000000 | 价格 |
| 12 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 13 | famount | 不含税金额 | numeric | 19 | 6 | √ | 0.000000 | 不含税金额 |
| 14 | fstockqty | 库存数量 | numeric | 19 | 6 | √ | 0.000000 | 库存数量 |
| 15 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 16 | fsupplierid | 所属供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 17 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 18 | fstockstatus | 库存状态 | bpchar | 1 |  | √ | ' ' | 库存状态,枚举: 1 :充足 2 :有限 9 :不足 |
| 19 | fpersonid | 所属人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_attention_fgoodsid |  | fgoodsid |
| 2 | idx_mal_attention_fpersonid |  | fpersonid |
| 3 | t_mal_attention_pkey |  | fid |
| 4 | idx_mal_attention_fbilldate |  | fbilldate |
