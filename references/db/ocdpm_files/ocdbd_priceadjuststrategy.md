# 渠道价格批量调整策略单-ocdbd_priceadjuststrategy

## 渠道价格批量调整策略单-主表 t_ocdbd_priceadstrategy

- **表名称：** 渠道价格批量调整策略单-主表
- **表名：** t_ocdbd_priceadstrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemrange | 商品范围 | bpchar | 1 |  | √ | 'A' | 商品范围,枚举: A :商品 B :商品分类 C :所有 |
| 3 | fdiscountvalue | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fintax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 6 | fpricevalue | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 7 | fdiscountmode | 调整方式 | bpchar | 1 |  | √ | ' ' | 调整方式,枚举: 1 :上调数值 2 :下调数值 5 :等于 |
| 8 | feffectdate | 调整值 | timestamp | 0 |  |  | null | 调整值 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: 0 :未执行 1 :已执行 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ffloorpercent | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 13 | fstrategytype | 策略类型 | bpchar | 1 |  | √ | 'A' | 策略类型,枚举: A :商品分录批量修改 B :商品分录批量删除 |
| 14 | ftaxrateid | 调整值 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fpricemode | 调整方式 | bpchar | 1 |  | √ | '1' | 调整方式,枚举: 1 :上调数值 2 :下调数值 3 :上调百分比 4 :下调百分比 5 :等于 |
| 16 | fexecutiontime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 17 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 18 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 20 | fname | 策略名称 | varchar | 128 |  | √ | ' ' | 策略名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fchannelrange | 客户范围 | bpchar | 1 |  | √ | 'A' | 客户范围,枚举: A :渠道 B :渠道分类 C :所有 |
| 23 | fceilingvalue | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | ffloorvalue | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fdiscountpercent | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 29 | ffloormode | 调整方式 | bpchar | 1 |  | √ | ' ' | 调整方式,枚举: 1 :上调数值 2 :下调数值 3 :上调百分比 4 :下调百分比 5 :等于 |
| 30 | ftaxmode | 调整方式 | bpchar | 1 |  | √ | ' ' | 调整方式,枚举: 1 :上调数值 2 :下调数值 3 :上调百分比 4 :下调百分比 5 :等于 |
| 31 | ftaxvalue | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 32 | fexpirydate | 调整值 | timestamp | 0 |  |  | null | 调整值 |
| 33 | fpricepercent | 调整值 | numeric | 23 | 10 | √ | 0 | 调整值 |
| 34 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fdiscountobj | 调整对象 | bpchar | 1 |  | √ | ' ' | 调整对象,枚举: 1 :已有单位折扣率% 2 :无折扣-调整单位折扣率% 3 :非折扣额-调整单位折扣率% 4 :已有单位折扣额 5 :无折扣-调整单位折扣额 6 :非折扣率-调整单位折扣额 |
| 37 | fceilingmode | 调整方式 | bpchar | 1 |  | √ | ' ' | 调整方式,枚举: 1 :上调数值 2 :下调数值 3 :上调百分比 4 :下调百分比 5 :等于 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_priceadstrategy_no |  | fbillno |
| 2 | pk_ocdbd_priceadstrategy |  | fid |

---

## 价格政策-子表 t_ocdbd_priceads_pentry

- **表名称：** 价格政策-子表
- **表名：** t_ocdbd_priceads_pentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchinfo_tag | 匹配信息_详情 | text | 0 |  |  | ' ' | 匹配信息_详情 |
| 3 | fpprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 4 | fmatchinfo | 匹配信息 | text | 0 |  |  | ' ' | 匹配信息 |
| 5 | fpitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 6 | fplowestprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fexecutestatus | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :未执行 1 :执行成功 2 :执行失败 |
| 9 | fpolicyid | 价格政策编码 | int8 | 64 |  | √ | 0 | [渠道价格政策 ocdbd_pricepolicy](../ocdpm_files/ocdbd_pricepolicy.md) |
| 10 | fpentryenable | 行使用状态 | bpchar | 1 |  | √ | ' ' | 行使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fpicktime | 匹配时间 | timestamp | 0 |  |  | null | 匹配时间 |
| 12 | fpdiscountway | 折扣方式 | bpchar | 1 |  | √ | ' ' | 折扣方式,枚举: A :单位折扣率% B :单位折扣额 |
| 13 | fpdiscount | 折扣 | numeric | 23 | 10 | √ | 0 | 折扣 |
| 14 | fpbegindate | 价格生效日期 | timestamp | 0 |  |  | null | 价格生效日期 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fpenddate | 价格失效日期 | timestamp | 0 |  |  | null | 价格失效日期 |
| 17 | fpriceentryid | 价格政策价格明细ID | int8 | 64 |  | √ | 0 | 价格政策价格明细ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ocdbd_priceads_pentry |  | fentryid |
| 2 | idx_ocdbd_priceads_pentry_fid |  | fid |

---

## 商品范围-子表 t_ocdbd_priceads_ientry

- **表名称：** 商品范围-子表
- **表名：** t_ocdbd_priceads_ientry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemclassid | 商品分类编码 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_priceads_ientry |  | fentryid |
| 2 | idx_ocdbd_priceads_ientry_fid |  | fid |

---

## 客户范围-子表 t_ocdbd_priceads_centry

- **表名称：** 客户范围-子表
- **表名：** t_ocdbd_priceads_centry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fchannelclassid | 渠道分类编码 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_priceads_centry_fid |  | fid |
| 2 | pk_ocdbd_priceads_centry |  | fentryid |

---

## 渠道价格批量调整策略单-多语言表 t_ocdbd_priceadstrategy_l

- **表名称：** 渠道价格批量调整策略单-多语言表
- **表名：** t_ocdbd_priceadstrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 128 |  | √ | ' ' | 策略名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ocdbd_priceadstrategy_l |  | fpkid |
| 2 | idx_ocdbd_priceadstrat_fid |  | fid |
