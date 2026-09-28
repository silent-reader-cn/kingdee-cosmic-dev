# 渠道价格政策-ocdbd_pricepolicy

## 渠道价格政策-主表 t_ocdbd_pricepolicy

- **表名称：** 渠道价格政策-主表
- **表名：** t_ocdbd_pricepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fchannelrange | 客户范围 | bpchar | 1 |  | √ | '0' | 客户范围,枚举: A :渠道 B :渠道分类 C :所有 |
| 5 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbegindate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | 渠道价格类型 ocdbd_price_type |
| 11 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 15 | fsupplierchannel | 供货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsupplierrelation | 供货关系 | bpchar | 1 |  | √ | 'A' | 供货关系,枚举: A :组织供货 B :渠道供货 |
| 19 | fgoodsbrandid | 品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fbusinesstypeid | 经营方式 | int8 | 64 |  | √ | 0 | 商品经营方式 ocdbd_item_businesstype |
| 22 | fnumber | 价格政策编码 | varchar | 80 |  | √ | ' ' | 价格政策编码 |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_pricepolicy |  | fid |
| 2 | idx_ocdbd_pricepolicy_no |  | fnumber |
| 3 | idx_ocdbd_pricepolicy_schl |  | fsalechannelid |

---

## 客户范围-子表 t_ocdbd_channelscope

- **表名称：** 客户范围-子表
- **表名：** t_ocdbd_channelscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprovinceid | 省 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 3 | forderchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fcityid | 市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 5 | fchannelclassid | 渠道分类编码 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fareaid | 区 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_channelscope_fid |  | fid |
| 2 | pk_ocdbd_channelscope |  | fentryid |

---

## 渠道价格政策-多语言表 t_ocdbd_pricepolicy_l

- **表名称：** 渠道价格政策-多语言表
- **表名：** t_ocdbd_pricepolicy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 价格政策名称 | varchar | 100 |  | √ | ' ' | 价格政策名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_pricepolicyl_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_pricepolicy_l |  | fpkid |

---

## 价格明细-子表 t_ocdbd_priceplcentry

- **表名称：** 价格明细-子表
- **表名：** t_ocdbd_priceplcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fdiscountway | 折扣方式 | bpchar | 1 |  | √ | ' ' | 折扣方式,枚举: A :单位折扣率% B :单位折扣额 |
| 5 | fbegindate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 8 | fsaleattrid | 商品销售属性 | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fflexauxpropid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fdiscount | 折扣 | numeric | 23 | 10 | √ | 0 | 折扣 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 14 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 15 | flowestprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 16 | fgoodsbrandid | 品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 17 | fqtyto | 销售数量（到） | numeric | 23 | 10 | √ | 0 | 销售数量（到） |
| 18 | fqtyfrom | 销售数量（从） | numeric | 23 | 10 | √ | 0 | 销售数量（从） |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_priceplcentry_item |  | fitemid |
| 2 | pk_ocdbd_priceplcentry |  | fentryid |
| 3 | idx_ocdbd_priceplcentry_fid |  | fid |

---

## 子单据体-子表 t_ocdbd_priceplcsentry

- **表名称：** 子单据体-子表
- **表名：** t_ocdbd_priceplcsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 2 | fpricingway | 定价方式 | bpchar | 1 |  | √ | '1' | 定价方式,枚举: 1 :按价格分摊 2 :自由定价 3 :按比例 |
| 3 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 5 | fsaleattrid | 商品销售属性 | int8 | 64 |  | √ | 0 | 商品销售属性 ocdbd_item_saleattr |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fflexauxpropid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fsubqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 9 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | fcombinprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fproportion | 比例（%） | numeric | 23 | 10 | √ | 0 | 比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_priceplcsentry |  | fdetailid |
| 2 | idx_ocdbd_priceplcsentry_eid |  | fentryid |
