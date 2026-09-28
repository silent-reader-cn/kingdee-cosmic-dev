# 商品监控日志-pmm_goodsrulelog

## 单据体-子表 t_mal_rulelogentry

- **表名称：** 单据体-子表
- **表名：** t_mal_rulelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fthreshold | 阈值 | varchar | 50 |  | √ | ' ' | 阈值 |
| 3 | factualval | 实际值 | varchar | 50 |  | √ | ' ' | 实际值 |
| 4 | fcusparam | 自定义参数 | varchar | 255 |  | √ | ' ' | 自定义参数 |
| 5 | fcontroltype | 控制类型 | bpchar | 1 |  | √ | ' ' | 控制类型,枚举: 1 :提示 2 :禁止 3 :不控制 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fruleid | 触发规则 | int8 | 64 |  | √ | 0 | [运营监控规则 pmm_operaterule](../pmm_files/pmm_operaterule.md) |
| 8 | fcompareval | 比价价格 | numeric | 23 | 10 | √ | 0 | 比价价格 |
| 9 | fcusparam_tag | 自定义参数_详情 | text | 0 |  |  | ' ' | 自定义参数_详情 |
| 10 | fgoodstype | 商品类型 | varchar | 50 |  | √ | ' ' | 商品类型,枚举: pbd_mallgoods :电商商品 pmm_prodmanage :自建商品池 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcomparegoodsid | 比较商品 | int8 | 64 |  | √ | 0 | 电商商品 pbd_mallgoods |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_rulelogentry |  | fentryid |
| 2 | idx_mal_rulelogentry |  | fid,fseq |

---

## 商品监控日志-多语言表 t_mal_goodsrulelog_l

- **表名称：** 商品监控日志-多语言表
- **表名：** t_mal_goodsrulelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goodsrulelog_l |  | fpkid |
| 2 | idx_mal_goodsrulelog_l_fid |  | fid,flocaleid |

---

## 商品监控日志-主表 t_mal_goodsrulelog

- **表名称：** 商品监控日志-主表
- **表名：** t_mal_goodsrulelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fgoodsnum | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 5 | fgoodsid | 商品ID | int8 | 64 |  | √ | 0 | 商品ID |
| 6 | fgoodspoolid | 商品池ID | int8 | 64 |  | √ | 0 | [商品池 pmm_prodpool](../pmm_files/pmm_prodpool.md) |
| 7 | fresult | 监控结果 | bpchar | 1 |  | √ | ' ' | 监控结果,枚举: 1 :自动下架 2 :人工下架 3 :人工作废 4 :- |
| 8 | ftaxprice | 结算价 | numeric | 23 | 10 | √ | 0 | 结算价 |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fgoodsclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 11 | fdealstatus | 处理状态 | bpchar | 1 |  | √ | ' ' | 处理状态,枚举: A :未处理 B :已处理 C :已作废 |
| 12 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 13 | fplatform | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 14 | fupdatedate | 监控日期 | timestamp | 0 |  |  | null | 监控日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goodsrulelog |  | fid |
| 2 | idx_mal_goodsrulelog_fgoodnum |  | fgoodsnum,fgoodspoolid,fplatform |
