# 销售出库单-im_saloutbill

## 关联子实体-子表 t_im_saloutbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_saloutbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_soutbille_lk_sbid |  | fsbillid |
| 2 | idx_im_soutbille_lk_sid |  | fsid |
| 3 | idx_im_saloutbillentry_lk_fk |  | fentryid |
| 4 | t_im_saloutbillentry_lk_pkey |  | fpkid |

---

## 销售出库单-分表 t_im_saloutbill_m

- **表名称：** 销售出库单-分表
- **表名：** t_im_saloutbill_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccmexcessamount | 预估信用超标额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标额度 |
| 3 | fccmexcessdays | 预估信用超标天数 | numeric | 23 | 10 | √ | 0 | 预估信用超标天数 |
| 4 | fccmexcessoveramount | 预估信用超标逾期额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标逾期额度 |
| 5 | fccmexcessbillamount | 预估信用超标单笔限额 | numeric | 23 | 10 | √ | 0 | 预估信用超标单笔限额 |
| 6 | fccmupdatetime | 预估信用超标时点 | timestamp | 0 |  |  | null | 预估信用超标时点 |
| 7 | fccmunsettlecount | 信用未结批数 | int4 | 32 |  | √ | 0 | 信用未结批数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_saloutbill_m_t |  | fccmupdatetime |
| 2 | pk_im_saloutbill_m |  | fid |

---

## 销售出库单-多语言表 t_im_saloutbill_l

- **表名称：** 销售出库单-多语言表
- **表名：** t_im_saloutbill_l

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
| 1 | idx_im_saloutbill_l_fid |  | fid,flocaleid |
| 2 | t_im_saloutbill_l_pkey |  | fpkid |

---

## 销售出库单-分表 t_im_saloutbill_c

- **表名称：** 销售出库单-分表
- **表名：** t_im_saloutbill_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_bj73_datetimefield | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 3 | fk_bj73_checkboxfield1 | 预发货 | bpchar | 1 |  | √ | '0' | 预发货 |
| 4 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_saloutbill_c_pkey |  | fid |
| 2 | idx_im_saloutbill_c |  | fcustomerid |

---

## 物料明细-分表 t_im_saloutbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_saloutbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_saloutbillentry_c |  | fentryid |
| 2 | idx_im_saloutbillentry_c |  | fid |

---

## 销售出库单-反写记录表 t_im_saloutbill_wb

- **表名称：** 销售出库单-反写记录表
- **表名：** t_im_saloutbill_wb

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
| 1 | idx_im_saloutbill_wb_fk |  | fid |
| 2 | t_im_saloutbill_wb_pkey |  | fentryid |

---

## 物料明细-分表 t_im_saloutbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_saloutbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fremaininvoicedbaseqty | 应收未关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票基本数量 |
| 6 | fsignedqty | 已签收数量 | numeric | 23 | 10 | √ | 0 | 已签收数量 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 8 | fentrustunverifybaseqty | 委托代销未结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销未结算基本数量 |
| 9 | ftransitlossbaseqty | 途损基本数量 | numeric | 23 | 10 | √ | 0 | 途损基本数量 |
| 10 | fassociatedagencybaseqty | 关联清单基本数量 | numeric | 23 | 10 | √ | 0 | 关联清单基本数量 |
| 11 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 12 | funverifybaseqty | 未勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽基本数量 |
| 13 | foversignedqty | 多签数量 | numeric | 23 | 10 | √ | 0 | 多签数量 |
| 14 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 15 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 16 | fjoinpriceqty | 应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收数量 |
| 17 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 18 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 19 | fremaininvoicedqty | 应收未关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 应收未关联销售发票数量 |
| 20 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 21 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 22 | fremaincfmqty | 未确认数量 | numeric | 23 | 10 | √ | 0 | 未确认数量 |
| 23 | fassociatedagencyqty | 关联清单数量 | numeric | 23 | 10 | √ | 0 | 关联清单数量 |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 25 | fjoincfmqty | 已确认数量 | numeric | 23 | 10 | √ | 0 | 已确认数量 |
| 26 | fwriteoffstockbaseqty | 冲销基本数量 | numeric | 23 | 10 | √ | 0 | 冲销基本数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 29 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 30 | fentrustunverifyqty | 委托代销未结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销未结算数量 |
| 31 | fverifybaseqty | 已勾稽基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽基本数量 |
| 32 | fwriteoffstockqty | 冲销数量 | numeric | 23 | 10 | √ | 0 | 冲销数量 |
| 33 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 34 | fremainjoinpricebaseqty | 剩余应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应收基本数量 |
| 35 | fremainjoinpriceqty | 剩余应收数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应收数量 |
| 36 | finvoicedqty | 关联销售发票数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票数量 |
| 37 | fassociatedsignbaseqty | 关联签收基本数量 | numeric | 23 | 10 | √ | 0 | 关联签收基本数量 |
| 38 | funverifyqty | 未勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未勾稽数量 |
| 39 | fsrcreceiptbillid | 来源签收单ID(在途退回) | int8 | 64 |  | √ | 0 | 来源签收单ID(在途退回) |
| 40 | fcompleterevcfmdate | 完全结转日期 | timestamp | 0 |  |  | null | 完全结转日期 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 42 | fjoincfmbaseqty | 已确认基本数量 | numeric | 23 | 10 | √ | 0 | 已确认基本数量 |
| 43 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 44 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 45 | finvoicedbaseqty | 关联销售发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联销售发票基本数量 |
| 46 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 47 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 48 | fsignedbaseqty | 已签收基本数量 | numeric | 23 | 10 | √ | 0 | 已签收基本数量 |
| 49 | fjoinpricebaseqty | 应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收基本数量 |
| 50 | fassociatedsignqty | 关联签收数量 | numeric | 23 | 10 | √ | 0 | 关联签收数量 |
| 51 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 52 | fremaincfmbaseqty | 未确认基本数量 | numeric | 23 | 10 | √ | 0 | 未确认基本数量 |
| 53 | fremainreturnbaseqty | 未退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库基本数量 |
| 54 | ftransitgroupnumber | 成组号(在途退回) | varchar | 50 |  | √ | ' ' | 成组号(在途退回) |
| 55 | fverifyqty | 已勾稽数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已勾稽数量 |
| 56 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 57 | fassociatedreturnqty | 关联退货数量 | numeric | 23 | 10 | √ | 0 | 关联退货数量 |
| 58 | ftransitlossqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 59 | fassociatedreturnbaseqty | 关联退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联退货基本数量 |
| 60 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 61 | foversignedbaseqty | 多签基本数量 | numeric | 23 | 10 | √ | 0 | 多签基本数量 |
| 62 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 63 | fentrustverifyqty | 委托代销已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算数量 |
| 64 | fentrustverifybaseqty | 委托代销已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委托代销已结算基本数量 |
| 65 | fsrcreceiptbillentryid | 来源签收单行ID(在途退回) | int8 | 64 |  | √ | 0 | 来源签收单行ID(在途退回) |
| 66 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 67 | finvoicedamountandtax | 关联销售发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联销售发票价税合计 |
| 68 | ftransitgroupseq | 成组行号(在途退回) | varchar | 50 |  | √ | ' ' | 成组行号(在途退回) |
| 69 | fremainreturnqty | 未退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库数量 |
| 70 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sobillentry_r_srceid |  | fsrcbillentryid |
| 2 | idx_im_sobillentry_r_mainid |  | fmainbillid |
| 3 | t_im_saloutbillentry_r_pkey |  | fentryid |
| 4 | idx_im_saloutbillentry_r_id |  | fid |
| 5 | idx_im_sobillentry_r_mainnum |  | fmainbillnumber |
| 6 | idx_im_sobillentry_r_srcid |  | fsrcbillid |
| 7 | idx_im_sobillentry_r_maineid |  | fmainbillentryid |

---

## 物料明细-多语言表 t_im_saloutbillentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_im_saloutbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | freceiveaddress | 收货地址 | varchar | 512 |  | √ | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_saloutbille_l_id_local |  | fentryid,flocaleid |
| 2 | t_im_saloutbillentry_l_pkey |  | fpkid |

---

## 销售出库单-关联追踪表 t_im_saloutbill_tc

- **表名称：** 销售出库单-关联追踪表
- **表名：** t_im_saloutbill_tc

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
| 1 | t_im_saloutbill_tc_pkey |  | fid |
| 2 | idx_im_saloutbill_tc_tbill |  | ftbillid |
| 3 | idx_im_saloutbill_tc_tid |  | ftid |
| 4 | idx_t_im_sobill_ftbidtid |  | ftbillid,ftid |

---

## 关联子实体-子表 t_im_saloutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_saloutbill_lk

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
| 1 | t_im_saloutbill_lk_pkey |  | fpkid |
| 2 | idx_im_saloutbill_lk_fk |  | fid |

---

## 销售出库单-主表 t_im_saloutbill

- **表名称：** 销售出库单-主表
- **表名：** t_im_saloutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fisredbill | 是否红字 | bpchar | 1 |  | √ | '0' | 是否红字 |
| 4 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | fk_bj73_printcountfield | fk_bj73_printcountfield | int8 | 64 |  | √ | '0' |  |
| 8 | ftransactepathid | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | ftradestatus | 贸易转换状态 | bpchar | 1 |  | √ | ' ' | 贸易转换状态,枚举: 0 :未完成 1 :已完成 |
| 14 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 15 | fisdespatchcreate | 是否发运生成 | bpchar | 1 |  | √ | '0' | 是否发运生成 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 18 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 23 | ftraderouteid | 贸易路线 | int8 | 64 |  | √ | 0 | [贸易路线 sbs_traderoute](../sbs_files/sbs_traderoute.md) |
| 24 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 25 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 26 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fcompleterevcfmdate | 完全结转日期 | timestamp | 0 |  |  | null | 完全结转日期 |
| 28 | fbizdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 32 | fcustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 33 | fk_bj73_textfield4 | 收货地址 | varchar | 200 |  | √ | ' ' | 收货地址 |
| 34 | fsettleroutedetailid | 结算路径明细ID | int8 | 64 |  | √ | 0 | 结算路径明细ID |
| 35 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 36 | fhasapbusbill | 是否生成暂估应收单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应收单 |
| 37 | fendbill | 尾单 | bpchar | 1 |  | √ | '0' | 尾单 |
| 38 | fk_bj73_textfield3 | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 39 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 40 | fbizoperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 41 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 42 | finnerbilltype | 内部交易单据类别 | varchar | 10 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 43 | fk_bj73_textfield1 | 考核大区 | varchar | 50 |  | √ | ' ' | 考核大区 |
| 44 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 45 | fquotation | 换算方式 | varchar | 50 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 46 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fbizorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 50 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 51 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 52 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 53 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fstep | 当前步骤 | int4 | 32 |  | √ | 0 | 当前步骤 |
| 56 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 57 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 60 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 62 | fbizoperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 63 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 64 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 65 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现销 CREDIT :赊销 |
| 66 | frevconfirmnode | 收入确认时点 | varchar | 50 |  | √ | ' ' | 收入确认时点,枚举: signIn :签收 saleOut :出库 |
| 67 | fk_bj73_textfield | 考核省区 | varchar | 50 |  | √ | ' ' | 考核省区 |
| 68 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 69 | finorgid | 入库库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 70 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 71 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_complet_erevcfm_date_m |  | fcompleterevcfmdate |
| 2 | idx_im_sobill_biztimeno |  | fbiztime,fbillno |
| 3 | idx_im_sobill_org |  | forgid |
| 4 | idx_im_sobill_bktorgno |  | fbookdate,forgid,fbillno |
| 5 | idx_im_saleoutbl_forgbillno |  | fbillno,forgid |
| 6 | idx_im_sobill_forfbizfno |  | forgid,fbiztime,fbillno |
| 7 | t_im_saloutbill_pkey |  | fid |
| 8 | idx_im_sobill_custm |  | fcustomerid |

---

## 物料明细-子表 t_im_saloutbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_saloutbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 3 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 7 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 9 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 11 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 13 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 14 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 15 | freplacedmatid | 替代原物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 16 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 18 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 20 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 21 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 22 | fqtyunit2nd | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 23 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 25 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 26 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 27 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 30 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 32 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 34 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 37 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 38 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 39 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 40 | finwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 41 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 42 | freceiveaddress_bak | 发货明细执行地址(后台用) | varchar | 512 |  | √ | ' ' | 发货明细执行地址(后台用) |
| 43 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 44 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 45 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 46 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 47 | fdeliverywayid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 48 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 49 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 50 | fisreplacemat | 替代出库 | bpchar | 1 |  | √ | '0' | 替代出库 |
| 51 | freceivecontactid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 52 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 53 | fk_bj73_pricefield | 销售参考价 | numeric | 23 | 10 |  | null | 销售参考价 |
| 54 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 55 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 56 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 57 | fhasvirtualbill | 已生成内部单据 | bpchar | 1 |  | √ | '0' | 已生成内部单据 |
| 58 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 kitreturn :成套退货 nonkitreturn :非成套退货 |
| 59 | freceiveaddress | 收货地址 | varchar | 512 |  | √ | ' ' | 收货地址 |
| 60 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 61 | ftaxrate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 62 | flocation | 交货地点 | varchar | 255 |  | √ | ' ' | 交货地点 |
| 63 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 64 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 65 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 66 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 67 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 68 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 69 | freccustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 70 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 71 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 72 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  | √ | ' ' | 尾差调整日志 |
| 73 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 74 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 75 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 76 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 3 :仅退款不退货 |
| 77 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 78 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 79 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 80 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 81 | funitmaterialcost | 单位材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位材料成本 |
| 82 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 83 | fisnotupdate | 不更新库存 | bpchar | 1 |  | √ | '0' | 不更新库存 |
| 84 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 85 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 86 | fsettleroute | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 87 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 88 | fk_bj73_textfield2 | 客户开票金额 | varchar | 50 |  | √ | ' ' | 客户开票金额 |
| 89 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 90 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 91 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 92 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 93 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 94 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 95 | freturnpath | 退回路径 | bpchar | 1 |  | √ | ' ' | 退回路径,枚举: 1 :供应商 2 :企业 3 :代销商 |
| 96 | finlocationid | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 97 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 98 | fqualitytype | 质量类型 | bpchar | 1 |  | √ | ' ' | 质量类型,枚举: A :合格出库 B :不合格出库 C :合格退货 D :不合格退货 E :报废退货 |
| 99 | fk_bj73_checkboxfield | 是否开票 | bpchar | 1 |  | √ | '0' | 是否开票 |
| 100 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 101 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 102 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 103 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 104 | fmaterialcost | 材料成本 | numeric | 23 | 10 | √ | 0.0000000000 | 材料成本 |
| 105 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sobill_e_oow |  | foutownerid |
| 2 | idx_im_sobill_e_replacedmat |  | freplacedmatid |
| 3 | idx_im_sobill_e_ow |  | fownerid |
| 4 | t_im_saloutbillentry_pkey |  | fentryid |
| 5 | idx_im_saloutbill_settleroute |  | fsettleroute |
| 6 | idx_im_saloutentry_material |  | fmaterialid |
| 7 | idx_im_saloutbillentry_billid |  | fid |
| 8 | idx_im_sobill_e_mmt |  | fmaterialmasterid |
| 9 | idx_im_sobill_e_wh |  | fwarehouseid |
