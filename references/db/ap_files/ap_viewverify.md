# 查看钩稽记录-ap_viewverify

## 关联子实体-子表 t_ap_verifyrecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_verifyrecord_lk

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
| 1 | pk_ap_verifyrecord_lk |  | fpkid |
| 2 | idx_ap_verifyrecord_lk_fk |  | fid |

---

## 单据体-子表 t_ap_verifyrecordentry

- **表名称：** 单据体-子表
- **表名：** t_ap_verifyrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fverifytaxamount | 本次勾稽价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽价税合计 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fswappl | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 5 | fiswrittenoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型 |
| 9 | fmainverifyamt | 折主方勾稽原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 折主方勾稽原币金额 |
| 10 | fverifyintercostamt | 本次勾稽成本金额 | numeric | 23 | 10 | √ | 0 | 本次勾稽成本金额 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 13 | fverifyqty | 本次勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽数量 |
| 14 | fwfinfo_tag | fwfinfo_tag | text | 0 |  |  | null |  |
| 15 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | flocalverifytaxamt | 本次勾稽价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽价税合计(本位币) |
| 18 | fbillno | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 19 | fqty | 计量单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计量单位数量 |
| 20 | fmainverifyqty | 折主方勾稽单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 折主方勾稽单位数量 |
| 21 | fhadwrittenoff | 被冲销 | bpchar | 1 |  | √ | '0' | 被冲销 |
| 22 | fwrittenoffremark | 冲销原因 | varchar | 512 |  | √ | ' ' | 冲销原因 |
| 23 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fverifybaseqty | 本次勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽基本数量 |
| 25 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 26 | fverifyamount | 本次勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额 |
| 27 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 29 | fverifylocalamt | 勾稽金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 勾稽金额(本位币) |
| 30 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 31 | fwfinfo | fwfinfo | varchar | 255 |  | √ | ' ' |  |
| 32 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: im_purinbill :采购入库单 im_purreturnbill :采购退库单 ap_finapbill :采购标准应付 im_mdc_omcmplinbill :委外完工入库单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_vre_billid |  | fbillid |
| 2 | idx_ap_vre_fid |  | fid |
| 3 | t_ap_verifyrecordentry_pkey |  | fentryid |
| 4 | idx_ap_vre_billno |  | fbillno |

---

## 查看钩稽记录-关联追踪表 t_ap_verifyrecord_tc

- **表名称：** 查看钩稽记录-关联追踪表
- **表名：** t_ap_verifyrecord_tc

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
| 1 | pk_ap_verifyrecord_tc |  | fid |
| 2 | idx_ap_verifyrecord_tc_tbill |  | ftbillid |
| 3 | idx_ap_verifyrecord_tc_tid |  | ftid |

---

## 关联子实体-子表 t_ap_verifyrecordentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_verifyrecordentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_verifyrecordentry_lk_fk |  | fentryid |
| 2 | pk_ap_verifyrecordentry_lk |  | fpkid |

---

## 查看钩稽记录-反写记录表 t_ap_verifyrecord_wb

- **表名称：** 查看钩稽记录-反写记录表
- **表名：** t_ap_verifyrecord_wb

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
| 1 | idx_ap_verifyrecord_wb_fk |  | fid |
| 2 | pk_ap_verifyrecord_wb |  | fentryid |

---

## 查看钩稽记录-主表 t_ap_verifyrecord

- **表名称：** 查看钩稽记录-主表
- **表名：** t_ap_verifyrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | fwfseq | varchar | 50 |  | √ | ' ' |  |
| 3 | fverifytype | 勾稽类型 | varchar | 30 |  | √ | ' ' | 勾稽类型,枚举: auto :自动勾稽 manual :手工勾稽 |
| 4 | fmeasureunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fverifytaxamount | 本次勾稽价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽价税合计 |
| 6 | fwfschemeid | fwfschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | forgid | 勾稽组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fswappl | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 10 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 12 | fverifyrelation | 勾稽关系 | varchar | 30 |  | √ | ' ' | 勾稽关系,枚举: appurin :入库勾稽 appurreturn :退库勾稽 purself :入库红冲 apfinself :发票红冲 appurreced :收货核销 apomin :委外核销 apominreturn :委外退库核销 ominself :委外入库红冲 finapwrittenoff :应付红蓝冲销 purwrittenoff :入库红蓝冲销 purreturnwrittenoff :退库红蓝冲销 purrecedwrittenoff :收货红蓝冲销 |
| 13 | fverifyseq | 勾稽序号 | int8 | 64 |  | √ | 0 | 勾稽序号 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fverifyintercostamt | 本次勾稽成本金额 | numeric | 23 | 10 | √ | 0 | 本次勾稽成本金额 |
| 16 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 17 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 18 | fcreatorid | 勾稽人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fheadwfinfo | fheadwfinfo | varchar | 255 |  | √ | ' ' |  |
| 20 | fverifyqty | 本次勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽数量 |
| 21 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | flocalverifytaxamt | 本次勾稽价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽价税合计(本位币) |
| 24 | fbillno | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 25 | fverifydate | 勾稽日期 | timestamp | 0 |  |  | null | 勾稽日期 |
| 26 | fqty | 计量单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计量单位数量 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 30 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fverifybaseqty | 本次勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽基本数量 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fverifyamount | 本次勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额 |
| 34 | fwriteofftypeid | 勾稽类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 35 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 36 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 37 | fverifylocalamt | 本次勾稽金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额(本位币) |
| 38 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 39 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 40 | fwfnumber | fwfnumber | varchar | 50 |  | √ | ' ' |  |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 42 | fheadwfinfo_tag | fheadwfinfo_tag | text | 0 |  |  | null |  |
| 43 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fbilltype | 主方单据类型 | varchar | 30 |  | √ | ' ' | 主方单据类型,枚举: im_purinbill :采购入库单 im_purreturnbill :采购退库单 ap_finapbill :采购标准应付 im_purreceivebill :采购收货单 im_mdc_omcmplinbill :委外完工入库单 |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_vr_billno |  | fbillno |
| 2 | idx_ap_vr_orgdate |  | forgid,fcreatetime |
| 3 | idx_ap_vr_billid |  | fbillid |
| 4 | t_ap_verifyrecord_pkey |  | fid |
