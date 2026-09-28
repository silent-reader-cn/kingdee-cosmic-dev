# 商业发票-gtm_cominvoice

## 关联子实体-子表 t_gtm_cominvoiceentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gtm_cominvoiceentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0 | 数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0 | 数量_原始携带值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_cominvoiceentry_lk_fk |  | fentryid |
| 2 | pk_gtm_cominvoiceentry_lk |  | fpkid |

---

## 明细信息-多语言表 t_gtm_cominvoiceentry_l

- **表名称：** 明细信息-多语言表
- **表名：** t_gtm_cominvoiceentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentrynote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_cominvoiceentry_l_lc |  | fentryid,flocaleid |
| 2 | pk_gtm_cominvoiceentry_l |  | fpkid |

---

## 明细信息-子表 t_gtm_cominvoiceentry

- **表名称：** 明细信息-子表
- **表名：** t_gtm_cominvoiceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 4 | fentrynote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 14 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcustomscodeid | 海关商品编码 | int8 | 64 |  | √ | 0 | [海关编码对应表明细 bd_customscodeinfo](../sbd_files/bd_customscodeinfo.md) |
| 16 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 17 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 20 | fmarks | 唛头 | varchar | 512 |  | √ | ' ' | 唛头 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_cominvoiceentry |  | fentryid |
| 2 | idx_gtm_cominvoiceentry_fk |  | fid |

---

## 商业发票-关联追踪表 t_gtm_cominvoice_tc

- **表名称：** 商业发票-关联追踪表
- **表名：** t_gtm_cominvoice_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_cominvoice_tc_tid |  | ftid |
| 2 | pk_gtm_cominvoice_tc |  | fid |
| 3 | idx_gtm_cominvoice_tc_tbill |  | ftbillid |

---

## 商业发票-主表 t_gtm_cominvoice

- **表名称：** 商业发票-主表
- **表名：** t_gtm_cominvoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funloadportid | 卸货港 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 3 | ftransmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 6 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | floadportid | 装货港 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcustomid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 11 | fmorelessval | 溢短装% | numeric | 23 | 2 | √ | 0 | 溢短装% |
| 12 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 13 | ftranstoolname | 运输工具名称 | varchar | 255 |  | √ | ' ' | 运输工具名称 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fexpcountryid | 出口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 19 | fdestaddr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 22 | flocno | 信用证号 | varchar | 255 |  | √ | ' ' | 信用证号 |
| 23 | fstartaddr | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 24 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: prof :形式发票 com :商业发票 |
| 25 | fimpcountryid | 进口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_cominvoice_billno |  | fbillno |
| 2 | pk_gtm_cominvoice |  | fid |
| 3 | idx_gtm_cominvoice_org |  | forgid,fbillno |
| 4 | idx_gtm_cominvoice_cdt |  | fcreatetime |

---

## 商业发票-分表 t_gtm_cominvoice_f

- **表名称：** 商业发票-分表
- **表名：** t_gtm_cominvoice_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fcurallamount | 总金额(本位币) | numeric | 23 | 10 | √ | 0 | 总金额(本位币) |
| 4 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 5 | fallamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 6 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 7 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 8 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 9 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_cominvoice_f |  | fid |

---

## 商业发票-多语言表 t_gtm_cominvoice_l

- **表名称：** 商业发票-多语言表
- **表名：** t_gtm_cominvoice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartaddr | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 3 | fdestaddr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 4 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 7 | ftranstoolname | 运输工具名称 | varchar | 255 |  | √ | ' ' | 运输工具名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_cominvoice_l |  | fpkid |
| 2 | idx_gtm_cominvoice_l_lc |  | fid,flocaleid |

---

## 商业发票-分表 t_gtm_cominvoice_t

- **表名称：** 商业发票-分表
- **表名：** t_gtm_cominvoice_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurphone | 买方联系电话 | varchar | 60 |  | √ | ' ' | 买方联系电话 |
| 3 | fsaldunscode | 卖方邓白氏编码 | varchar | 255 |  | √ | ' ' | 卖方邓白氏编码 |
| 4 | fsalfax | 卖方传真 | varchar | 255 |  | √ | ' ' | 卖方传真 |
| 5 | fsalcontactor | 卖方联系人 | varchar | 255 |  | √ | ' ' | 卖方联系人 |
| 6 | fpuraddress | 买方地址 | varchar | 255 |  | √ | ' ' | 买方地址 |
| 7 | fpurunisocrecode | 买方统一社会信用代码 | varchar | 255 |  | √ | ' ' | 买方统一社会信用代码 |
| 8 | fsalcomp | 卖方企业 | varchar | 255 |  | √ | ' ' | 卖方企业 |
| 9 | fsalunisocrecode | 卖方统一社会信用代码 | varchar | 255 |  | √ | ' ' | 卖方统一社会信用代码 |
| 10 | fpurdunscode | 买方邓白氏编码 | varchar | 255 |  | √ | ' ' | 买方邓白氏编码 |
| 11 | fsalemail | 卖方电子邮箱 | varchar | 255 |  | √ | ' ' | 卖方电子邮箱 |
| 12 | fpurfax | 买方传真 | varchar | 255 |  | √ | ' ' | 买方传真 |
| 13 | fsaltaxno | 卖方纳税人识别号 | varchar | 255 |  | √ | ' ' | 卖方纳税人识别号 |
| 14 | fsalphone | 卖方联系电话 | varchar | 60 |  | √ | ' ' | 卖方联系电话 |
| 15 | fpurcontactor | 买方联系人 | varchar | 255 |  | √ | ' ' | 买方联系人 |
| 16 | fpurcomp | 买方企业 | varchar | 255 |  | √ | ' ' | 买方企业 |
| 17 | fpurtaxno | 买方纳税人识别号 | varchar | 255 |  | √ | ' ' | 买方纳税人识别号 |
| 18 | fsaladdress | 卖方地址 | varchar | 255 |  | √ | ' ' | 卖方地址 |
| 19 | fpuremail | 买方电子邮箱 | varchar | 255 |  | √ | ' ' | 买方电子邮箱 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_cominvoice_t |  | fid |

---

## 商业发票-反写记录表 t_gtm_cominvoice_wb

- **表名称：** 商业发票-反写记录表
- **表名：** t_gtm_cominvoice_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_cominvoice_wb |  | fentryid |
| 2 | idx_gtm_cominvoice_wb_fk |  | fid |
