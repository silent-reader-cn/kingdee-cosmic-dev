# 商品零售价目表-ocdpm_retailpricelist

## 商品零售价目表-主表 t_ocdpm_itemprice

- **表名称：** 商品零售价目表-主表
- **表名：** t_ocdpm_itemprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 5 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 8 | fistax | 是否含税 | bpchar | 1 |  | √ | '0' | 是否含税 |
| 9 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ffirstauditdate | 首次审核日期 | timestamp | 0 |  |  | null | 首次审核日期 |
| 12 | fiscandistribute | 能否分配 | bpchar | 1 |  | √ | '0' | 能否分配 |
| 13 | fsourcebillno | 源单单据编号 | varchar | 80 |  | √ | ' ' | 源单单据编号 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fisdistributed | 是否总部分配 | bpchar | 1 |  | √ | '0' | 是否总部分配 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbranchid | 渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 18 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fisonlinemarket | 线上商城 | bpchar | 1 |  | √ | '0' | 线上商城 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fisunaudit | 是否反审核 | bpchar | 1 |  | √ | '0' | 是否反审核 |
| 22 | fcontroltype | 控制方式 | bpchar | 1 |  | √ | ' ' | 控制方式,枚举: A :所有门店适用 B :适用指定门店 |
| 23 | fdisablerid | 失效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fisonlinestore | 线上门店 | bpchar | 1 |  | √ | '0' | 线上门店 |
| 26 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 27 | fenable | 生效状态 | bpchar | 1 |  | √ | 'A' | 生效状态,枚举: A :生效 B :失效 |
| 28 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fuseterminal | 适用终端 | bpchar | 1 |  | √ | ' ' | 适用终端,枚举: A :适用线上 B :适用线下 C :线上线下通用 |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 32 | fisstore | 线下门店 | bpchar | 1 |  | √ | '0' | 线下门店 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_itemprice_billno |  | fbillno |
| 2 | pk_ocdpm_itemprice |  | fid |

---

## 渠道分组-多选基础资料表 t_ocdpm_itemprice_brange

- **表名称：** 渠道分组-多选基础资料表
- **表名：** t_ocdpm_itemprice_brange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_brange |  | fpkid |
| 2 | idx_ocdpm_itemprice_brange_id |  | fid |

---

## 商品零售价目表-分表 t_ocdpm_itemprice_y

- **表名称：** 商品零售价目表-分表
- **表名：** t_ocdpm_itemprice_y

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisuseprice1 | 预留价格1 | bpchar | 1 |  | √ | '0' | 预留价格1 |
| 3 | fisusememberprice | 会员价 | bpchar | 1 |  | √ | '0' | 会员价 |
| 4 | fisusespecialprice | 特价 | bpchar | 1 |  | √ | '0' | 特价 |
| 5 | fisuseprice2 | 预留价格2 | bpchar | 1 |  | √ | '0' | 预留价格2 |
| 6 | fisuseprice3 | 预留价格3 | bpchar | 1 |  | √ | '0' | 预留价格3 |
| 7 | fisuseretailprice | 标准零售价 | bpchar | 1 |  | √ | '0' | 标准零售价 |
| 8 | fisuseuniqueprice | 唯一价 | bpchar | 1 |  | √ | '0' | 唯一价 |
| 9 | fisuseprice4 | 预留价格4 | bpchar | 1 |  | √ | '0' | 预留价格4 |
| 10 | fisusefactoryprice | 厂家控价 | bpchar | 1 |  | √ | '0' | 厂家控价 |
| 11 | fisuseprice5 | 预留价格5 | bpchar | 1 |  | √ | '0' | 预留价格5 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_y |  | fid |
| 2 | idx_ocdpm_itemprice_y_up |  | fisuseretailprice |

---

## 价格明细-分表 t_ocdpm_itemprice_dtl_r

- **表名称：** 价格明细-分表
- **表名：** t_ocdpm_itemprice_dtl_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretailprice | 标准零售价 | numeric | 23 | 10 | √ | 0 | 标准零售价 |
| 3 | fp4adjustnum | 预留价格4已调整次数 | int4 | 32 |  | √ | 0 | 预留价格4已调整次数 |
| 4 | ffpadjustnum | 厂家控价已调整次数 | int4 | 32 |  | √ | 0 | 厂家控价已调整次数 |
| 5 | fspecialprice | 特价 | numeric | 23 | 10 | √ | 0 | 特价 |
| 6 | fhpadjustnum | 最高价已调整次数 | int4 | 32 |  | √ | 0 | 最高价已调整次数 |
| 7 | frpadjustnum | 标准零售价已调整次数 | int4 | 32 |  | √ | 0 | 标准零售价已调整次数 |
| 8 | flowprice | 最低价 | numeric | 23 | 10 | √ | 0 | 最低价 |
| 9 | fmpadjustnum | 会员价已调整次数 | int4 | 32 |  | √ | 0 | 会员价已调整次数 |
| 10 | fp1adjustnum | 预留价格1已调整次数 | int4 | 32 |  | √ | 0 | 预留价格1已调整次数 |
| 11 | fprice5 | 预留价格5 | numeric | 23 | 10 | √ | 0 | 预留价格5 |
| 12 | fprice3 | 预留价格3 | numeric | 23 | 10 | √ | 0 | 预留价格3 |
| 13 | flpadjustnum | 最低价已调整次数 | int4 | 32 |  | √ | 0 | 最低价已调整次数 |
| 14 | fprice4 | 预留价格4 | numeric | 23 | 10 | √ | 0 | 预留价格4 |
| 15 | fhighprice | 最高价 | numeric | 23 | 10 | √ | 0 | 最高价 |
| 16 | fupadjustnum | 唯一价已调整次数 | int4 | 32 |  | √ | 0 | 唯一价已调整次数 |
| 17 | fp3adjustnum | 预留价格3已调整次数 | int4 | 32 |  | √ | 0 | 预留价格3已调整次数 |
| 18 | ffactoryprice | 厂家控价 | numeric | 23 | 10 | √ | 0 | 厂家控价 |
| 19 | funiqueprice | 唯一价 | numeric | 23 | 10 | √ | 0 | 唯一价 |
| 20 | fp2adjustnum | 预留价格2已调整次数 | int4 | 32 |  | √ | 0 | 预留价格2已调整次数 |
| 21 | fp5adjustnum | 预留价格5已调整次数 | int4 | 32 |  | √ | 0 | 预留价格5已调整次数 |
| 22 | fspadjustnum | 特价已调整次数 | int4 | 32 |  | √ | 0 | 特价已调整次数 |
| 23 | fmemberprice | 会员价 | numeric | 23 | 10 | √ | 0 | 会员价 |
| 24 | fprice1 | 预留价格1 | numeric | 23 | 10 | √ | 0 | 预留价格1 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fprice2 | 预留价格2 | numeric | 23 | 10 | √ | 0 | 预留价格2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_dtl_r |  | fentryid |
| 2 | idx_ocdpm_itemprice_dtlr_id |  | fid |

---

## 组织范围-多选基础资料表 t_ocdpm_itemprice_org

- **表名称：** 组织范围-多选基础资料表
- **表名：** t_ocdpm_itemprice_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_org |  | fpkid |
| 2 | idx_ocdpm_itemprice_org_fid |  | fid |

---

## 价格明细-子表 t_ocdpm_itemprice_dtl

- **表名称：** 价格明细-子表
- **表名：** t_ocdpm_itemprice_dtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fdisabloperid | 失效操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsaleattrid | 商品销售属性 | int8 | 64 |  | √ | 0 | [商品销售属性 ocdbd_item_saleattr](../ocdbd_files/ocdbd_item_saleattr.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fisinvalid | 是否失效 | bpchar | 1 |  | √ | '0' | 是否失效 |
| 8 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 9 | fpriceunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 11 | fdisableopdate | 失效操作时间 | timestamp | 0 |  |  | null | 失效操作时间 |
| 12 | fstocktypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbarcodeid | 条形码 | int8 | 64 |  | √ | 0 | [商品条形码 ocdbd_item_barcode](../ocdbd_files/ocdbd_item_barcode.md) |
| 15 | fpricenum | 计价数量 | numeric | 23 | 10 | √ | 0 | 计价数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_dtl |  | fentryid |
| 2 | idx_ocdpm_itemprice_dtl_id |  | fid |

---

## 树形单据体-子表 t_ocdpm_itemprice_branch

- **表名称：** 树形单据体-子表
- **表名：** t_ocdpm_itemprice_branch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisdistributed | 是否已分配 | bpchar | 1 |  | √ | '0' | 是否已分配 |
| 3 | fisenable | 是否执行 | bpchar | 1 |  | √ | '0' | 是否执行 |
| 4 | fbranchid | 门店编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 5 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_branch |  | fentryid |
| 2 | idx_ocdpm_itemprice_branch_id |  | fid |

---

## 调整明细-子表 t_ocdpm_itemprice_record

- **表名称：** 调整明细-子表
- **表名：** t_ocdpm_itemprice_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbeforeprice | 调整前 | numeric | 23 | 10 | √ | 0 | 调整前 |
| 2 | fadjusttime | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fbarcodeid | 条形码 | int8 | 64 |  | √ | 0 | [商品条形码 ocdbd_item_barcode](../ocdbd_files/ocdbd_item_barcode.md) |
| 7 | fadjustpricetype | 调整价格类型 | bpchar | 1 |  | √ | ' ' | 调整价格类型,枚举: A :标准零售价 B :厂家控价 C :唯一价 D :会员价 E :特价 F :预留价格1 G :预留价格2 H :预留价格3 I :预留价格4 J :预留价格5 |
| 8 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 9 | fpriceunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fafterprice | 调整后 | numeric | 23 | 10 | √ | 0 | 调整后 |
| 11 | fmoderatorid | 调整人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_itemprice_record |  | fdetailid |
| 2 | idx_ocdpm_itemprice_record_eid |  | fentryid |
