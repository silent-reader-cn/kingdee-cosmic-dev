# 提单-gtm_ladingbill

## 明细信息-多语言表 t_gtm_ladingbillentry_l

- **表名称：** 明细信息-多语言表
- **表名：** t_gtm_ladingbillentry_l

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
| 1 | pk_gtm_ladingbillentry_l |  | fpkid |
| 2 | idx_gtm_ladingbillentry_l_lc |  | fentryid,flocaleid |

---

## 关联子实体-子表 t_gtm_ladingbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gtm_ladingbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 装箱件数_确认携带值 | numeric | 23 | 10 | √ | 0 | 装箱件数_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 装箱件数_原始携带值 | numeric | 23 | 10 | √ | 0 | 装箱件数_原始携带值 |
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
| 1 | idx_gtm_ladingbillentry_lk_fk |  | fentryid |
| 2 | pk_gtm_ladingbillentry_lk |  | fpkid |

---

## 提单-反写记录表 t_gtm_ladingbill_wb

- **表名称：** 提单-反写记录表
- **表名：** t_gtm_ladingbill_wb

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
| 1 | pk_gtm_ladingbill_wb |  | fentryid |
| 2 | idx_gtm_ladingbill_wb_fk |  | fid |

---

## 提单-多语言表 t_gtm_ladingbill_l

- **表名称：** 提单-多语言表
- **表名：** t_gtm_ladingbill_l

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
| 1 | pk_gtm_ladingbill_l |  | fpkid |
| 2 | idx_gtm_ladingbill_l_lc |  | fid,flocaleid |

---

## 提单-主表 t_gtm_ladingbill

- **表名称：** 提单-主表
- **表名：** t_gtm_ladingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funloadportid | 卸货港 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 3 | ftransmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 6 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fbilldate | 提单日期 | timestamp | 0 |  |  | null | 提单日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fladingtype | 提单类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 10 | fdeliveryplace | 交货地点 | varchar | 255 |  | √ | ' ' | 交货地点 |
| 11 | floadportid | 装货港 | int8 | 64 |  | √ | 0 | [装运点 lgm_shippingpoint](../lgm_files/lgm_shippingpoint.md) |
| 12 | foriginalnum | 正本提单数 | int4 | 32 |  | √ | 0 | 正本提单数 |
| 13 | freceivplace | 收货地点 | varchar | 255 |  | √ | ' ' | 收货地点 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | floadingport | floadingport | varchar | 255 |  | √ | ' ' |  |
| 16 | fcustomid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 17 | fmorelessval | 溢短装% | numeric | 23 | 2 | √ | 0 | 溢短装% |
| 18 | ftranstoolname | 运输工具名称 | varchar | 255 |  | √ | ' ' | 运输工具名称 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fdispatchdate | 预计发运日期 | timestamp | 0 |  |  | null | 预计发运日期 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fexpcountryid | 出口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 24 | fdestaddr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fissueplace | 提单签发地 | varchar | 255 |  | √ | ' ' | 提单签发地 |
| 27 | fshipdate | 预计装运日期 | timestamp | 0 |  |  | null | 预计装运日期 |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fstartaddr | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 30 | fdischargingport | fdischargingport | varchar | 255 |  | √ | ' ' |  |
| 31 | fimpcountryid | 进口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 32 | farrivaldate | 预计到达日期 | timestamp | 0 |  |  | null | 预计到达日期 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_ladingbill_cdt |  | fcreatetime |
| 2 | pk_gtm_ladingbill |  | fid |
| 3 | idx_gtm_ladingbill_org |  | forgid,fbillno |
| 4 | idx_gtm_ladingbill_billno |  | fbillno |

---

## 提单-分表 t_gtm_ladingbill_t

- **表名称：** 提单-分表
- **表名：** t_gtm_ladingbill_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurphone | 买方联系电话 | varchar | 60 |  | √ | ' ' | 买方联系电话 |
| 3 | fnotifyparty | 通知方 | varchar | 255 |  | √ | ' ' | 通知方 |
| 4 | fnotifyunisocrecode | 通知方统一社会信用代码 | varchar | 255 |  | √ | ' ' | 通知方统一社会信用代码 |
| 5 | fpuraddress | 买方地址 | varchar | 255 |  | √ | ' ' | 买方地址 |
| 6 | fpurunisocrecode | 买方统一社会信用代码 | varchar | 255 |  | √ | ' ' | 买方统一社会信用代码 |
| 7 | fsalcomp | 卖方企业 | varchar | 255 |  | √ | ' ' | 卖方企业 |
| 8 | fnotifyphone | 通知方联系电话 | varchar | 60 |  | √ | ' ' | 通知方联系电话 |
| 9 | fsalemail | 卖方电子邮箱 | varchar | 255 |  | √ | ' ' | 卖方电子邮箱 |
| 10 | fnotifycontactor | 通知方联系人 | varchar | 255 |  | √ | ' ' | 通知方联系人 |
| 11 | fpurfax | 买方传真 | varchar | 255 |  | √ | ' ' | 买方传真 |
| 12 | fpurcontactor | 买方联系人 | varchar | 255 |  | √ | ' ' | 买方联系人 |
| 13 | fnotifyaddress | 通知方地址 | varchar | 255 |  | √ | ' ' | 通知方地址 |
| 14 | fsaladdress | 卖方地址 | varchar | 255 |  | √ | ' ' | 卖方地址 |
| 15 | fpuremail | 买方电子邮箱 | varchar | 255 |  | √ | ' ' | 买方电子邮箱 |
| 16 | fnotifydunscode | 通知方邓白氏编码 | varchar | 255 |  | √ | ' ' | 通知方邓白氏编码 |
| 17 | fsaldunscode | 卖方邓白氏编码 | varchar | 255 |  | √ | ' ' | 卖方邓白氏编码 |
| 18 | fsalfax | 卖方传真 | varchar | 255 |  | √ | ' ' | 卖方传真 |
| 19 | fsalcontactor | 卖方联系人 | varchar | 255 |  | √ | ' ' | 卖方联系人 |
| 20 | fsalunisocrecode | 卖方统一社会信用代码 | varchar | 255 |  | √ | ' ' | 卖方统一社会信用代码 |
| 21 | fnotifyfax | 通知方传真 | varchar | 255 |  | √ | ' ' | 通知方传真 |
| 22 | fpurdunscode | 买方邓白氏编码 | varchar | 255 |  | √ | ' ' | 买方邓白氏编码 |
| 23 | fnotifyemail | 通知方电子邮箱 | varchar | 255 |  | √ | ' ' | 通知方电子邮箱 |
| 24 | fsaltaxno | 卖方纳税人识别号 | varchar | 255 |  | √ | ' ' | 卖方纳税人识别号 |
| 25 | fsalphone | 卖方联系电话 | varchar | 60 |  | √ | ' ' | 卖方联系电话 |
| 26 | fpurcomp | 买方企业 | varchar | 255 |  | √ | ' ' | 买方企业 |
| 27 | fpurtaxno | 买方纳税人识别号 | varchar | 255 |  | √ | ' ' | 买方纳税人识别号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_ladingbill_t |  | fid |

---

## 明细信息-子表 t_gtm_ladingbillentry

- **表名称：** 明细信息-子表
- **表名：** t_gtm_ladingbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fboxno | 箱号 | varchar | 255 |  | √ | ' ' | 箱号 |
| 3 | fvolumeunitid | 体积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fentrynote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fgrossweight | 毛重 | numeric | 23 | 10 | √ | 0 | 毛重 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnetweight | 净重 | numeric | 23 | 10 | √ | 0 | 净重 |
| 9 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 10 | fprice | fprice | numeric | 23 | 10 | √ | 0 |  |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsealno | 铅封号 | varchar | 255 |  | √ | ' ' | 铅封号 |
| 13 | fcuramount | fcuramount | numeric | 23 | 10 | √ | 0 |  |
| 14 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 15 | fpackagedetail | 包装详情 | varchar | 255 |  | √ | ' ' | 包装详情 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fgrossunitid | 毛重单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fmarks | 唛头 | varchar | 512 |  | √ | ' ' | 唛头 |
| 19 | fqty | 装箱件数 | numeric | 23 | 10 | √ | 0 | 装箱件数 |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | fvolume | 体积 | numeric | 23 | 10 | √ | 0 | 体积 |
| 23 | funitid | 装箱单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fnetunitid | 净重单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 27 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fcustomscodeid | 海关商品编码 | int8 | 64 |  | √ | 0 | [海关编码对应表明细 bd_customscodeinfo](../sbd_files/bd_customscodeinfo.md) |
| 29 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_ladingbillentry |  | fentryid |
| 2 | idx_gtm_ladingbillentry_fk |  | fid |

---

## 提单-关联追踪表 t_gtm_ladingbill_tc

- **表名称：** 提单-关联追踪表
- **表名：** t_gtm_ladingbill_tc

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
| 1 | pk_gtm_ladingbill_tc |  | fid |
| 2 | idx_gtm_ladingbill_tc_tbill |  | ftbillid |
| 3 | idx_gtm_ladingbill_tc_tid |  | ftid |
