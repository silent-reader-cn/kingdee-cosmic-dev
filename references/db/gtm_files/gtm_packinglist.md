# 装箱单-gtm_packinglist

## 明细信息-子表 t_gtm_palistentry

- **表名称：** 明细信息-子表
- **表名：** t_gtm_palistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fboxno | 箱号 | varchar | 512 |  | √ | ' ' | 箱号 |
| 3 | fvolumeunitid | 体积单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fentrynote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fgrossweight | 毛重 | numeric | 23 | 10 | √ | 0 | 毛重 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnetweight | 净重 | numeric | 23 | 10 | √ | 0 | 净重 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fsealno | 铅封号 | varchar | 512 |  | √ | ' ' | 铅封号 |
| 11 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fgrossunitid | 毛重单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fmarks | 唛头 | varchar | 512 |  | √ | ' ' | 唛头 |
| 15 | fqty | 装箱件数 | numeric | 23 | 10 | √ | 0 | 装箱件数 |
| 16 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | fvolume | 体积 | numeric | 23 | 10 | √ | 0 | 体积 |
| 19 | funitid | 装箱单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fnetunitid | 净重单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fcustomscodeid | 海关商品编码 | int8 | 64 |  | √ | 0 | [海关编码对应表明细 bd_customscodeinfo](../sbd_files/bd_customscodeinfo.md) |
| 25 | fpackdetail | 包装详情 | varchar | 512 |  | √ | ' ' | 包装详情 |
| 26 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtm_palistentry_fk |  | fid |
| 2 | pk_gtm_palistentry |  | fentryid |

---

## 装箱单-多语言表 t_gtm_packinglist_l

- **表名称：** 装箱单-多语言表
- **表名：** t_gtm_packinglist_l

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
| 1 | idx_gtm_packinglist_l |  | fid,flocaleid |
| 2 | pk_gtm_packinglist_l |  | fpkid |

---

## 装箱单-分表 t_gtm_packinglist_t

- **表名称：** 装箱单-分表
- **表名：** t_gtm_packinglist_t

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
| 1 | pk_gtm_packinglist_t |  | fid |

---

## 装箱单-关联追踪表 t_gtm_packinglist_tc

- **表名称：** 装箱单-关联追踪表
- **表名：** t_gtm_packinglist_tc

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
| 1 | idx_gtm_packinglist_tc_tid |  | ftid |
| 2 | idx_gtm_packinglist_tc_tbill |  | ftbillid |
| 3 | pk_gtm_packinglist_tc |  | fid |

---

## 明细信息-多语言表 t_gtm_palistentry_l

- **表名称：** 明细信息-多语言表
- **表名：** t_gtm_palistentry_l

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
| 1 | idx_gtm_palistentry_l_lc |  | fentryid,flocaleid |
| 2 | pk_gtm_palistentry_l |  | fpkid |

---

## 关联子实体-子表 t_gtm_palistentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gtm_palistentry_lk

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
| 1 | pk_gtm_palistentry_lk |  | fpkid |
| 2 | idx_gtm_palistentry_lk |  | fentryid |

---

## 装箱单-主表 t_gtm_packinglist

- **表名称：** 装箱单-主表
- **表名：** t_gtm_packinglist

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
| 12 | fpreshipdate | 预计发运日期 | timestamp | 0 |  |  | null | 预计发运日期 |
| 13 | fpacktypeid | 包装方式 | int8 | 64 |  | √ | 0 | [包装方式 bd_packagingtype](../sbd_files/bd_packagingtype.md) |
| 14 | ftranstoolname | 运输工具名称 | varchar | 255 |  | √ | ' ' | 运输工具名称 |
| 15 | finvoiceno | 发票号 | varchar | 255 |  | √ | ' ' | 发票号 |
| 16 | fquantity | 件数 | numeric | 23 | 2 | √ | 0 | 件数 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fprearrivedate | 预计到达日期 | timestamp | 0 |  |  | null | 预计到达日期 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fexpcountryid | 出口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 23 | fdestaddr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fpackdate | 装箱日期 | timestamp | 0 |  |  | null | 装箱日期 |
| 26 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 27 | fstartaddr | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 28 | finvoicetype | finvoicetype | varchar | 50 |  | √ | ' ' |  |
| 29 | fpacktype | fpacktype | varchar | 512 |  | √ | ' ' |  |
| 30 | fimpcountryid | 进口国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_packinglist |  | fid |
| 2 | idx_gtm_packinglist_org |  | forgid,fbillno |
| 3 | idx_gtm_packinglist_billno |  | fbillno |
| 4 | idx_gtm_packinglist_cdt |  | fcreatetime |

---

## 装箱单-反写记录表 t_gtm_packinglist_wb

- **表名称：** 装箱单-反写记录表
- **表名：** t_gtm_packinglist_wb

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
| 1 | idx_gtm_packinglist_wb_fk |  | fid |
| 2 | pk_gtm_packinglist_wb |  | fentryid |
