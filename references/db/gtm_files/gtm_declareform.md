# 报关单-gtm_declareform

## 报关明细-子表 t_gtm_declareformmat

- **表名称：** 报关明细-子表
- **表名：** t_gtm_declareformmat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fsrcbillnumber | 来源单据编号 | varchar | 255 |  | √ | ' ' | 来源单据编号 |
| 4 | fentrynote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 15 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | fisfree | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 17 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 19 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_declareformmat_id |  | fid |
| 2 | pk_gtm_declareformmat |  | fentryid |

---

## 报关单-反写记录表 t_gtm_declareform_wb

- **表名称：** 报关单-反写记录表
- **表名：** t_gtm_declareform_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
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
| 1 | idx_gtm_declareform_wb_fk |  | fid |
| 2 | pk_gtm_declareform_wb |  | fentryid |

---

## 报关单-主表 t_gtm_declareform

- **表名称：** 报关单-主表
- **表名：** t_gtm_declareform

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funloadportid | 卸货港 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 3 | fclearstatus | 结关状态 | varchar | 5 |  | √ | ' ' | 结关状态,枚举: A :未结关 B :已结关 D :结关中 |
| 4 | funifyno | 统一编号 | varchar | 255 |  | √ | ' ' | 统一编号 |
| 5 | ftransmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 6 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | fcleanserid | 结关处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | floadportid | 装货港 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 12 | ftransobjecttype | 交易对象类型 | varchar | 50 |  | √ | ' ' | 交易对象类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmorelessval | 溢短装% | numeric | 23 | 2 | √ | 0 | 溢短装% |
| 15 | fcleardate | 结关时间 | timestamp | 0 |  |  | null | 结关时间 |
| 16 | ftranstoolname | 运输工具名称 | varchar | 255 |  | √ | ' ' | 运输工具名称 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcountryareaid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 20 | fmark | 唛头 | varchar | 255 |  | √ | ' ' | 唛头 |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fexpcountryid | 出口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 23 | fdestaddr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fdeclaretype | 报关类型 | varchar | 50 |  | √ | ' ' | 报关类型,枚举: im :进口报关 exp :出口报关 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | ftransobjectid | 交易对象 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 28 | fdeclareformno | 报关单号 | varchar | 255 |  | √ | ' ' | 报关单号 |
| 29 | fstartaddr | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 30 | fimpcountryid | 进口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 31 | fcustomsedino | 海关ediNo | varchar | 255 |  | √ | ' ' | 海关ediNo |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_declareform |  | fid |
| 2 | idx_gtm_declareform_org |  | forgid,fbillno |
| 3 | idx_gtm_declareform_cdt |  | fcreatetime |
| 4 | idx_gtm_declareform_edi |  | fcustomsedino |
| 5 | idx_gtm_declareform_billno |  | fbillno |

---

## 报关单-分表 t_gtm_declareform_t

- **表名称：** 报关单-分表
- **表名：** t_gtm_declareform_t

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
| 1 | pk_gtm_declareform_t |  | fid |

---

## 报关单-多语言表 t_gtm_declareform_l

- **表名称：** 报关单-多语言表
- **表名：** t_gtm_declareform_l

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
| 1 | idx_gtm_declareform_l_id |  | fid,flocaleid |
| 2 | pk_gtm_declareform_l |  | fpkid |

---

## 报关明细-多语言表 t_gtm_declareformmat_l

- **表名称：** 报关明细-多语言表
- **表名：** t_gtm_declareformmat_l

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
| 1 | idx_gtm_declareformmat_l_eid |  | fentryid,flocaleid |
| 2 | pk_gtm_declareformmat_l |  | fpkid |

---

## 报关单-分表 t_gtm_declareform_d

- **表名称：** 报关单-分表
- **表名：** t_gtm_declareform_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgrossweight | 毛重 | numeric | 23 | 2 | √ | 0 | 毛重 |
| 3 | fnetweight | 净重 | numeric | 23 | 2 | √ | 0 | 净重 |
| 4 | fexpimpport | 出入境口岸 | varchar | 255 |  | √ | ' ' | 出入境口岸 |
| 5 | fdeclarecustomsid | 申报海关 | int8 | 64 |  | √ | 0 | [海关关区 gtm_customsdistrict](../gtm_files/gtm_customsdistrict.md) |
| 6 | fpacklistno | 装箱单号 | varchar | 255 |  | √ | ' ' | 装箱单号 |
| 7 | finvoicedate | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 8 | fgrossunitid | 毛重单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fexemptionnatureid | 征免性质 | int8 | 64 |  | √ | 0 | [征免性质 gtm_naturelevy](../gtm_files/gtm_naturelevy.md) |
| 10 | finvoiceno | 发票号 | varchar | 255 |  | √ | ' ' | 发票号 |
| 11 | fbflno | 提单号 | varchar | 255 |  | √ | ' ' | 提单号 |
| 12 | fplanshipdate | 预计发运时间 | timestamp | 0 |  |  | null | 预计发运时间 |
| 13 | fdeclaredate | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 14 | fdeclarecategoryid | 申报类别 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 15 | fcustomschannel | 海关通道 | varchar | 255 |  | √ | ' ' | 海关通道 |
| 16 | fpackmode | fpackmode | varchar | 255 |  | √ | ' ' |  |
| 17 | fcswarehouseid | 海关监管仓 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 18 | fthroughimmgdate | 出入境日期 | timestamp | 0 |  |  | null | 出入境日期 |
| 19 | fnetunitid | 净重单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 21 | fsize | 体积 | numeric | 23 | 2 | √ | 0 | 体积 |
| 22 | fpackmodeid | 包装方式 | int8 | 64 |  | √ | 0 | [包装方式 bd_packagingtype](../sbd_files/bd_packagingtype.md) |
| 23 | fitemnumber | 件数 | numeric | 23 | 2 | √ | 0 | 件数 |
| 24 | fregulatypeid | 监管方式 | int8 | 64 |  | √ | 0 | [监管方式 gtm_regulatorymode](../gtm_files/gtm_regulatorymode.md) |
| 25 | flicenseno | 许可证号 | varchar | 255 |  | √ | ' ' | 许可证号 |
| 26 | fplanarrivedate | 预计到达时间 | timestamp | 0 |  |  | null | 预计到达时间 |
| 27 | fsizeunitid | 体积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_declareform_d_dcdate |  | fdeclaredate |
| 2 | pk_gtm_declareform_d |  | fid |

---

## 报关单-分表 t_gtm_declareform_f

- **表名称：** 报关单-分表
- **表名：** t_gtm_declareform_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 3 | fcurallexpense | 费用合计(本位币) | numeric | 23 | 10 | √ | 0 | 费用合计(本位币) |
| 4 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 5 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fcurallamount | 总金额(本位币) | numeric | 23 | 10 | √ | 0 | 总金额(本位币) |
| 7 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 8 | fallamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 9 | fallexpense | 费用合计 | numeric | 23 | 10 | √ | 0 | 费用合计 |
| 10 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 13 | fdeclareallamount | 申报总金额 | numeric | 23 | 10 | √ | 0 | 申报总金额 |
| 14 | fexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 15 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fdeclarecurallamount | 申报总金额(本位币) | numeric | 23 | 10 | √ | 0 | 申报总金额(本位币) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_declareform_f |  | fid |

---

## 关联子实体-子表 t_gtm_declareformmat_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gtm_declareformmat_lk

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
| 1 | pk_gtm_declareformmat_lk |  | fpkid |
| 2 | idx_gtm_declareformmat_lk_eid |  | fentryid |

---

## 报关单-关联追踪表 t_gtm_declareform_tc

- **表名称：** 报关单-关联追踪表
- **表名：** t_gtm_declareform_tc

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
| 1 | idx_gtm_declareform_tc_tid |  | ftid |
| 2 | pk_gtm_declareform_tc |  | fid |
| 3 | idx_gtm_declareform_tc_tbill |  | ftbillid |

---

## 税务信息-子表 t_gtm_declareformtax

- **表名称：** 税务信息-子表
- **表名：** t_gtm_declareformtax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 2 | ftaxcurrencyid | ftaxcurrencyid | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 2 | √ | 0 | 税率(%) |
| 4 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 5 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_declareformtax |  | fdetailid |
| 2 | idx_gtm_declareformtax_eid |  | fentryid |

---

## 报关商品信息-子表 t_gtm_declareformgood

- **表名称：** 报关商品信息-子表
- **表名：** t_gtm_declareformgood

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsdeclareprice | 申报单价 | numeric | 23 | 10 | √ | 0 | 申报单价 |
| 3 | fgoodsecondqty | 法定第二单位数量 | numeric | 23 | 10 | √ | 0 | 法定第二单位数量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fgoodsunitsecond | 法定第二单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | foriginplace | foriginplace | varchar | 255 |  | √ | ' ' |  |
| 7 | fgoodfirstqty | 法定第一单位数量 | numeric | 23 | 10 | √ | 0 | 法定第一单位数量 |
| 8 | fgoodsqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 9 | fcustomscodeid | 海关商品编码 | int8 | 64 |  | √ | 0 | [海关编码对应表明细 bd_customscodeinfo](../sbd_files/bd_customscodeinfo.md) |
| 10 | fgoodsunitfirst | 法定第一单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fgoodsdeclareamount | 申报金额 | numeric | 23 | 10 | √ | 0 | 申报金额 |
| 12 | fgoodsunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | foriginplaceid | 原产地 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 14 | fcustomscodeno | 海关商品编码编码 | varchar | 255 |  | √ | ' ' | 海关商品编码编码 |
| 15 | fdeclarelement | 申报要素 | varchar | 255 |  | √ | ' ' | 申报要素 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fgoodsdeclarecuramount | 申报金额(本位币) | numeric | 23 | 10 | √ | 0 | 申报金额(本位币) |
| 18 | fgoodsmatid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_declareformgood_id |  | fid |
| 2 | pk_gtm_declareformgood |  | fentryid |
