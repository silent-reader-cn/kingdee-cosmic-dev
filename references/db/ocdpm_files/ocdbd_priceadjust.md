# 渠道价格调整单-ocdbd_priceadjust

## 客户范围-子表 t_ocdbd_pricead_csentry

- **表名称：** 客户范围-子表
- **表名：** t_ocdbd_pricead_csentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffcityid | 市 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpolicycustomerid | 价格政策客户Id | int8 | 64 |  | √ | 0 | 价格政策客户Id |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fprovinceid | 省 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 8 | fadjustmark | 调整标识 | bpchar | 1 |  | √ | '1' | 调整标识,枚举: 0 :保留 1 :新增 2 :删除 |
| 9 | forderchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 10 | fchannelclassid | 渠道分类编码 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 11 | fareaid | 区 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_pricead_csentry_fid |  | fid |
| 2 | pk_ocdbd_pricead_csentry |  | fentryid |

---

## 渠道价格调整单-反写记录表 t_ocdbd_priceadjust_wb

- **表名称：** 渠道价格调整单-反写记录表
- **表名：** t_ocdbd_priceadjust_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_priceadjust_wb_fk |  | fid |
| 2 | pk_ocdbd_priceadjust_wb |  | fentryid |

---

## 商品价格明细-子表 t_ocdbd_pricead_prentry

- **表名称：** 商品价格明细-子表
- **表名：** t_ocdbd_pricead_prentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fsaleattrid | 商品销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 5 | fnewtaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fflexauxpropid | 物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | foldlowestprice | 原最低限价 | numeric | 23 | 10 | √ | 0 | 原最低限价 |
| 9 | foldbegindate | 原生效日期 | timestamp | 0 |  |  | null | 原生效日期 |
| 10 | foldhighestprice | 原最高限价 | numeric | 23 | 10 | √ | 0 | 原最高限价 |
| 11 | fnewtaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 12 | fnewdiscountway | 折扣方式 | bpchar | 1 |  | √ | ' ' | 折扣方式,枚举: A :单位折扣率% B :单位折扣额 |
| 13 | fqtyfrom | 销售数量（从） | numeric | 23 | 10 | √ | 0 | 销售数量（从） |
| 14 | fnewenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 15 | fpriceentryid | 价格政策价格明细ID | int8 | 64 |  | √ | 0 | 价格政策价格明细ID |
| 16 | fnewbegindate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | foldprice | 原单价 | numeric | 23 | 10 | √ | 0 | 原单价 |
| 18 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 19 | fnewdiscount | 折扣 | numeric | 23 | 10 | √ | 0 | 折扣 |
| 20 | fdiscountway | 原折扣方式 | bpchar | 1 |  | √ | ' ' | 原折扣方式,枚举: A :单位折扣率% B :单位折扣额 |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 23 | fnewhighestprice | 最高限价 | numeric | 23 | 10 | √ | 0 | 最高限价 |
| 24 | fnewlowestprice | 最低限价 | numeric | 23 | 10 | √ | 0 | 最低限价 |
| 25 | fdiscount | 原折扣 | numeric | 23 | 10 | √ | 0 | 原折扣 |
| 26 | foldtaxprice | 原含税单价 | numeric | 23 | 10 | √ | 0 | 原含税单价 |
| 27 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 28 | foldenddate | 原失效日期 | timestamp | 0 |  |  | null | 原失效日期 |
| 29 | fgoodsbrandid | 品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 30 | fqtyto | 销售数量（到） | numeric | 23 | 10 | √ | 0 | 销售数量（到） |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | foldtaxrateid | 原税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_pricead_prentry |  | fentryid |
| 2 | idx_ocdbd_pricead_prentry_fid |  | fid |

---

## 渠道价格调整单-关联追踪表 t_ocdbd_priceadjust_tc

- **表名称：** 渠道价格调整单-关联追踪表
- **表名：** t_ocdbd_priceadjust_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_priceadjust_tc |  | fid |
| 2 | idx_ocdbd_priceadjust_tc_tid |  | ftid |
| 3 | idx_ocdbd_priceadjust_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_ocdbd_priceadjust_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocdbd_priceadjust_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_priceadjust_lk |  | fpkid |
| 2 | idx_ocdbd_priceadjust_lk_fk |  | fid |

---

## 渠道价格调整单-主表 t_ocdbd_priceadjust

- **表名称：** 渠道价格调整单-主表
- **表名：** t_ocdbd_priceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemrange | 商品范围 | bpchar | 1 |  | √ | 'A' | 商品范围,枚举: A :商品 B :商品分类 |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | feffectstatus | 生效状态 | bpchar | 1 |  | √ | '0' | 生效状态,枚举: 0 :未生效 1 :已生效 |
| 5 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fenddate | 原失效日期 | timestamp | 0 |  |  | null | 原失效日期 |
| 8 | fsupplierchannel | 供货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsupplierrelation | 供货关系 | bpchar | 1 |  | √ | 'A' | 供货关系,枚举: A :组织供货 B :渠道供货 |
| 11 | fstrategytype | 对应策略类型 | bpchar | 1 |  | √ | 'A' | 对应策略类型,枚举: A :商品分录批量修改 B :商品分录批量删除 |
| 12 | fexecutiontime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fchannelrange | 客户范围 | bpchar | 1 |  | √ | 'A' | 客户范围,枚举: A :渠道 B :渠道分类 C :所有 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbegindate | 原生效日期 | timestamp | 0 |  |  | null | 原生效日期 |
| 21 | fpricepolicyid | 原价格政策表 | int8 | 64 |  | √ | 0 | [渠道价格政策 ocdbd_pricepolicy](../ocdpm_files/ocdbd_pricepolicy.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fpricetypeid | 价格类型 | int8 | 64 |  | √ | 0 | [渠道价格类型 ocdbd_price_type](../ocdpm_files/ocdbd_price_type.md) |
| 24 | fbusinesstypeid | 经营方式 | int8 | 64 |  | √ | 0 | [商品经营方式 ocdbd_item_businesstype](../ocdpm_files/ocdbd_item_businesstype.md) |
| 25 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_priceadjust |  | fid |
| 2 | idx_ocdbd_priceadjust_no |  | fbillno |
