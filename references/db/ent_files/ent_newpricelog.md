# 商品价格日志-ent_newpricelog

## 商品价格日志-多语言表 t_mal_newprice_l

- **表名称：** 商品价格日志-多语言表
- **表名：** t_mal_newprice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_newprice_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_newprice_l |  | fpkid |

---

## 商品价格日志-主表 t_mal_newprice

- **表名称：** 商品价格日志-主表
- **表名：** t_mal_newprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fpricetype | 价格类型 | bpchar | 1 |  | √ | ' ' | 价格类型,枚举: A :固定价 B :阶梯价 |
| 4 | fshopprice | 商城价 | numeric | 23 | 10 | √ | 0 | 商城价 |
| 5 | fname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 6 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 8 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 9 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 10 | fsrcbillid | 来源单据id | varchar | 80 |  | √ | ' ' | 来源单据id |
| 11 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fgoodspoolid | 商品池 | int8 | 64 |  | √ | 0 | [商品池 ent_prodpool](../ent_files/ent_prodpool.md) |
| 13 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0 | 结算价 |
| 14 | fsrcentitytype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型,枚举: pmm_prodaudit :自建上下架管理 ent_prodrequest :上下架申请 pmm_priceaudit :调价审批 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 17 | fadjustdate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 18 | forigin | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :供应商 2 :采购方 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ftaxrateid | 税率编码 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 21 | fnumber | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 22 | fauditorg | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | flastprice | 上次价格 | numeric | 23 | 10 | √ | 0 | 上次价格 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_newprice |  | fid |
| 2 | idx_mal_fgoodspoolid |  | fgoodspoolid |
| 3 | idx_mal_fgoodsid |  | fgoodsid |
