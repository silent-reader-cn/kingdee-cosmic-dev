# 查看勾稽记录-ar_viewverify

## 查看勾稽记录-反写记录表 t_ar_verifyrecord_wb

- **表名称：** 查看勾稽记录-反写记录表
- **表名：** t_ar_verifyrecord_wb

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
| 1 | pk_ar_verifyrecord_wb |  | fentryid |
| 2 | idx_ar_verifyrecord_wb_fk |  | fid |

---

## 查看勾稽记录-主表 t_ar_verifyrecord

- **表名称：** 查看勾稽记录-主表
- **表名：** t_ar_verifyrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | fwfseq | varchar | 50 |  | √ | ' ' |  |
| 3 | fverifytype | 勾稽类型 | varchar | 30 |  | √ | ' ' | 勾稽类型,枚举: auto :自动勾稽 manual :手工勾稽 |
| 4 | fmeasureunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fverifytaxamount | 本次勾稽价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽价税合计 |
| 6 | fwfschemeid | fwfschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | forgid | 勾稽组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 11 | fverifyrelation | 勾稽关系 | varchar | 30 |  | √ | ' ' | 勾稽关系,枚举: arsalout :出库勾稽 arsalreturn :退库勾稽 salself :出库红冲 arfinself :收入红冲 finarwrittenoff :收入红蓝冲销 saloutwrittenoff :出库红蓝冲销 salreturnwrittenoff :退库红蓝冲销 |
| 12 | fverifyseq | 勾稽序号 | int8 | 64 |  | √ | 0 | 勾稽序号 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 16 | fcreatorid | 勾稽人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fheadwfinfo | fheadwfinfo | varchar | 255 |  | √ | ' ' |  |
| 18 | fverifyqty | 本次勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽数量 |
| 19 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fbillno | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 22 | fverifydate | 勾稽日期 | timestamp | 0 |  |  | null | 勾稽日期 |
| 23 | fqty | 计量单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计量单位数量 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fbaseactualcost | 基本单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位实际成本 |
| 26 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 28 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fverifybaseqty | 本次勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽基本数量 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fverifyamount | 本次勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额 |
| 32 | fwriteofftypeid | 勾稽类别 | int8 | 64 |  | √ | 0 | 核销类别 msmod_writeofftype |
| 33 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 34 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | fallrelationcost | 相关总成本 | numeric | 23 | 10 | √ | 0 | 相关总成本 |
| 36 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 37 | fverifylocalamt | 本次勾稽金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额(本位币) |
| 38 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 39 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 40 | finventorycost | 存货成本 | numeric | 23 | 10 | √ | 0.0000000000 | 存货成本 |
| 41 | fwfnumber | fwfnumber | varchar | 50 |  | √ | ' ' |  |
| 42 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 43 | fheadwfinfo_tag | fheadwfinfo_tag | text | 0 |  |  | null |  |
| 44 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 45 | fbilltype | 主方单据类型 | varchar | 30 |  | √ | ' ' | 主方单据类型,枚举: im_saloutbill :销售出库单 ar_revcfmbill :收入成本确认单 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_vr_billno |  | fbillno |
| 2 | idx_ar_vr_orgdate |  | forgid,fcreatetime |
| 3 | idx_ar_vr_billentryid |  | fbillentryid |
| 4 | t_ar_verifyrecord_pkey |  | fid |
| 5 | idx_ar_vr_billid |  | fbillid |

---

## 查看勾稽记录-关联追踪表 t_ar_verifyrecord_tc

- **表名称：** 查看勾稽记录-关联追踪表
- **表名：** t_ar_verifyrecord_tc

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
| 1 | pk_ar_verifyrecord_tc |  | fid |
| 2 | idx_ar_verifyrecord_tc_tid |  | ftid |
| 3 | idx_ar_verifyrecord_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_ar_verifyrecordentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_verifyrecordentry_lk

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
| 1 | idx_ar_verifyrecordentry_lk_fk |  | fentryid |
| 2 | pk_ar_verifyrecordentry_lk |  | fpkid |

---

## 单据体-子表 t_ar_verifyrecordentry

- **表名称：** 单据体-子表
- **表名：** t_ar_verifyrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fverifytaxamount | 本次勾稽价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽价税合计 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fiswrittenoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 8 | fmainverifyamt | 折主方勾稽原币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 折主方勾稽原币金额 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fverifyqty | 本次勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽数量 |
| 12 | fwfinfo_tag | fwfinfo_tag | text | 0 |  |  | null |  |
| 13 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fbillno | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 16 | fqty | 计量单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计量单位数量 |
| 17 | fmainverifyqty | 折主方勾稽单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 折主方勾稽单位数量 |
| 18 | fbaseactualcost | 基本单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位实际成本 |
| 19 | fhadwrittenoff | 被冲销 | bpchar | 1 |  | √ | '0' | 被冲销 |
| 20 | fwrittenoffremark | 冲销原因 | varchar | 512 |  | √ | ' ' | 冲销原因 |
| 21 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fverifybaseqty | 本次勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽基本数量 |
| 23 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 24 | fverifyamount | 本次勾稽金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额 |
| 25 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 26 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fbillentryid | 单据分录id | int8 | 64 |  | √ | 0 | 单据分录id |
| 28 | fverifylocalamt | 本次勾稽金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 本次勾稽金额(本位币) |
| 29 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 30 | fwfinfo | fwfinfo | varchar | 255 |  | √ | ' ' |  |
| 31 | finventorycost | 存货成本 | numeric | 23 | 10 | √ | 0.0000000000 | 存货成本 |
| 32 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 33 | fmeasureunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 36 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: im_saloutbill :销售出库单 ar_revcfmbill :收入成本确认单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_verifyrecordentry_pkey |  | fentryid |
| 2 | idx_ar_vre_billid |  | fbillid |
| 3 | idx_ar_vre_billentryid |  | fbillentryid |
| 4 | idx_ar_vre_fid |  | fid |
| 5 | idx_ar_vre_billno |  | fbillno |

---

## 关联子实体-子表 t_ar_verifyrecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ar_verifyrecord_lk

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
| 1 | idx_ar_verifyrecord_lk_fk |  | fid |
| 2 | pk_ar_verifyrecord_lk |  | fpkid |
