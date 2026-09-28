# 采购入库单-im_purinbill

## 采购入库单-反写记录表 t_im_purinbill_wb

- **表名称：** 采购入库单-反写记录表
- **表名：** t_im_purinbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purinbill_wb_pkey |  | fentryid |
| 2 | idx_im_purinbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_im_purinbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_purinbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purinbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_purinbillentry_lk_fk |  | fentryid |

---

## 采购入库单-多语言表 t_im_purinbill_l

- **表名称：** 采购入库单-多语言表
- **表名：** t_im_purinbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purinbill_l_pkey |  | fpkid |
| 2 | idx_im_purinbill_l_id |  | fid,flocaleid |

---

## 物料明细-分表 t_im_purinbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_purinbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purinbillentry_c |  | fid |
| 2 | pk_im_purinbillentry_c |  | fentryid |

---

## 物料明细-分表 t_im_purinbillentry_f

- **表名称：** 物料明细-分表
- **表名：** t_im_purinbillentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | ' ' |  |
| 5 | fdiscountrate | fdiscountrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fintercostamt | 计成本金额 | numeric | 23 | 10 | √ | 0 | 计成本金额 |
| 7 | fdiscountamount | fdiscountamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | famountandtax | famountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fcurdeductibleamt | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 12 | factualtaxprice | factualtaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fcuramountandtax | fcuramountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fcurtaxamount | fcurtaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fcuramount | fcuramount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fentrysettleorgid | fentrysettleorgid | int8 | 64 |  | √ | 0 |  |
| 17 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 18 | fdeductiblerate | 可抵扣率(%) | numeric | 23 | 10 | √ | 0 | 可抵扣率(%) |
| 19 | factualprice | factualprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purinbillentry_f |  | fid |
| 2 | t_im_purinbillentry_f_pkey |  | fentryid |

---

## 物料明细-多语言表 t_im_purinbillentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_im_purinbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprovideraddress | 供货地址 | varchar | 512 |  | √ | ' ' | 供货地址 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_purinbille_l_id_local |  | fentryid,flocaleid |
| 2 | t_im_purinbillentry_l_pkey |  | fpkid |

---

## 物料明细-分表 t_im_purinbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_purinbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 6 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 7 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽基本数量 |
| 8 | fvmisettleqty | VMI已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI已结算数量 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 11 | fjoinpriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 15 | funjoinpurinvoiceqty | 应付未关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票数量 |
| 16 | frejectdiscountamount | 不良品折让金额 | numeric | 23 | 10 | √ | 0 | 不良品折让金额 |
| 17 | fjoinbusqty | 暂估应付数量 | numeric | 23 | 10 | √ | 0 | 暂估应付数量 |
| 18 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 19 | fomprdinid | 委外完工入库单ID | int8 | 64 |  | √ | 0 | 委外完工入库单ID |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | fvmisettlebaseqty | VMI已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI已结算基本数量 |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 25 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽基本数量 |
| 26 | fjoinpricedamagebaseqty | 关联应付采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 关联应付采购损耗基本数量 |
| 27 | fjoinbusunwoffqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 28 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 29 | fremainjoinpricebaseqty | 剩余应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付基本数量 |
| 30 | fremainjoinpriceqty | 剩余应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付数量 |
| 31 | fvmiremainsettlebaseqty | VMI剩余结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI剩余结算基本数量 |
| 32 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 33 | fomprdinentryid | 委外完工入库单行ID | int8 | 64 |  | √ | 0 | 委外完工入库单行ID |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fjoinbusbaseqty | 暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量 |
| 36 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 37 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 38 | fjoinpurinvoicebaseqty | 关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票基本数量 |
| 39 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 40 | fjoinrejectdiscountamount | 关联应付不良品折让金额 | numeric | 23 | 10 | √ | 0 | 关联应付不良品折让金额 |
| 41 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 42 | fjoinpricebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付基本数量 |
| 43 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 44 | fdamagebaseqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 45 | funjoinpurinvoicebaseqty | 应付未关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票基本数量 |
| 46 | fremainreturnbaseqty | 未退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库基本数量 |
| 47 | fverifyqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 48 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 49 | fvmiremainsettleqty | VMI剩余结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI剩余结算数量 |
| 50 | fjoinpricedamageqty | 关联应付采购损耗数量 | numeric | 23 | 10 | √ | 0 | 关联应付采购损耗数量 |
| 51 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 52 | fjoinpurinvoiceamount | 关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联采购发票价税合计 |
| 53 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 54 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 55 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 56 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 57 | fjoinpurinvoiceqty | 关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票数量 |
| 58 | fremainreturnqty | 未退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库数量 |
| 59 | fdamageqty | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 60 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_pibillentry_r_srceid |  | fsrcbillentryid |
| 2 | idx_im_pibillentry_r_maineid |  | fmainbillentryid |
| 3 | idx_im_pibillentry_r_mainid |  | fmainbillid |
| 4 | idx_im_pibillentry_r_srcid |  | fsrcbillid |
| 5 | idx_im_pibillentry_r |  | fid |
| 6 | dx_im_pibillentry_r_maininum |  | fmainbillnumber |
| 7 | t_im_purinbillentry_r_pkey |  | fentryid |

---

## 关联子实体-子表 t_im_purinbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_purinbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purinbill_lk_pkey |  | fpkid |
| 2 | idx_im_purinbill_lk_fk |  | fid |

---

## 物料明细-子表 t_im_purinbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_purinbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceivedate | 收货日期 | timestamp | 0 |  |  | null | 收货日期 |
| 3 | ftaxrate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 5 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 6 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 11 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 12 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 13 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 14 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 15 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 17 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 21 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 28 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | fentrybizorgid | fentrybizorgid | int8 | 64 |  | √ | 0 |  |
| 31 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 32 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 33 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 34 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 35 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 36 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 38 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 39 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 40 | freturnmaterialtype | 退料类型 | bpchar | 1 |  | √ | '0' | 退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 41 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 42 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 43 | fhasgenapbusbill | 已生成暂估应付单 | bpchar | 1 |  | √ | '0' | 已生成暂估应付单 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 46 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 47 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fproductcategory | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 49 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 50 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 51 | fsettleroute | 结算路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 52 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 53 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 55 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 57 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 58 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 59 | fpurunitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 60 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 61 | fprovideraddress | 供货地址 | varchar | 512 |  | √ | ' ' | 供货地址 |
| 62 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 64 | foutlocationid | 出库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 65 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 66 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 67 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 68 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 69 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 70 | fprovidersupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 71 | fpurqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 72 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 73 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 74 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 75 | foutwarehouseid | 出库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 76 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 77 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 78 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 80 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 81 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 82 | fhasvirtualbill | 已生成内部单据 | bpchar | 1 |  | √ | '0' | 已生成内部单据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_pbill_e_ow |  | fownerid |
| 2 | idx_im_pbill_e_mrname |  | fmaterialname |
| 3 | idx_im_pbill_e_mmt |  | fmaterialmasterid |
| 4 | idx_im_purinbillentry_billid |  | fid |
| 5 | idx_im_pbill_e_oow |  | foutownerid |
| 6 | t_im_purinbillentry_pkey |  | fentryid |
| 7 | idx_im_pbill_e_wh |  | fwarehouseid |

---

## 采购入库单-关联追踪表 t_im_purinbill_tc

- **表名称：** 采购入库单-关联追踪表
- **表名：** t_im_purinbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | idx_im_purinbill_tc_tbill |  | ftbillid |
| 2 | t_im_purinbill_tc_pkey |  | fid |
| 3 | idx_im_purinbill_tc_tid |  | ftid |
| 4 | idx_t_im_pibill_ftbidtid |  | ftbillid,ftid |

---

## 采购入库单-主表 t_im_purinbill

- **表名称：** 采购入库单-主表
- **表名：** t_im_purinbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fisredbill | 是否红字 | bpchar | 1 |  | √ | '0' | 是否红字 |
| 4 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | ftransactepathid | 结算路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | fpurcostshare | 采购费用分摊 | bpchar | 1 |  | √ | '0' | 采购费用分摊 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 14 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 17 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 20 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 23 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 25 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 26 | fbizdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 31 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 32 | fhasapbusbill | 是否生成暂估应付单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应付单 |
| 33 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 34 | fbizoperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 35 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 36 | finnerbilltype | 内部交易单据类别 | varchar | 10 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 37 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 38 | fquotation | 换算方式 | varchar | 50 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 42 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 43 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 44 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | fbizuserid | fbizuserid | int8 | 64 |  | √ | 0 |  |
| 50 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 51 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 53 | fbizoperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 54 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 55 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 56 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 57 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 58 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 59 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purinbill_fbiztime_forgid_fbillno_idx1 |  | fbiztime,forgid,fbillno |
| 2 | t_im_purinbill_pkey |  | fid |
| 3 | t_im_purinbill_fsupplierid_idx1 |  | fsupplierid |
| 4 | t_im_purinbill_fbillno_idx1 |  | fbillno |
| 5 | t_im_purinbill_forgid_idx1 |  | forgid |
| 6 | idx_im_pbill_forgbillno |  | fbillno,forgid |
| 7 | t_im_purinbill_fbookdate_forgid_fbillno_idx1 |  | fbookdate,forgid,fbillno |
| 8 | idx_im_pbill_biztimeno |  | fbiztime,fbillno |
| 9 | t_im_purinbill_forgid_fbiztime_fbillno_idx1 |  | forgid,fbiztime,fbillno |
