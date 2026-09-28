# 简单委外入库单（废弃）-im_mdc_ominbill

## 物料明细-多语言表 t_im_mdc_ominbillentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_im_mdc_ominbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprovideraddress | 供货地址 | varchar | 300 |  | √ | ' ' | 供货地址 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_ominbel_fentryid |  | fentryid,flocaleid |
| 2 | pk_im_mdc_ominbillentry_l |  | fpkid |

---

## 物料明细-分表 t_im_mdc_ominbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_ominbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 3 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 4 | foutverifybaseqty | 委外已核销基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委外已核销基本数量 |
| 5 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 6 | foutverifyqty | 委外已核销数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委外已核销数量 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 8 | freturnbaseqty | 累计退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计退库基本数量 |
| 9 | fjoinpricebaseqty | 累计应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计应付基本数量 |
| 10 | funverifybaseqty | 未核销基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销基本数量 |
| 11 | foutunverifyqty | 委外未核销数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委外未核销数量 |
| 12 | fvmisettleqty | VMI已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI已结算数量 |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 14 | foutunverifybaseqty | 委外未核销基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 委外未核销基本数量 |
| 15 | fjoinpriceqty | 累计应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计应付数量 |
| 16 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 17 | fremainreturnbaseqty | 剩余退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余退库基本数量 |
| 18 | fverifyqty | 已核销数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销数量 |
| 19 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 20 | fvmiremainsettleqty | VMI剩余结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI剩余结算数量 |
| 21 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fvmisettlebaseqty | VMI已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI已结算基本数量 |
| 24 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 25 | freturnqty | 累计退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计退库数量 |
| 26 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 27 | fverifybaseqty | 已核销基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已核销基本数量 |
| 28 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 29 | fcompletewriteoff | 完全核销 | bpchar | 1 |  | √ | '0' | 完全核销 |
| 30 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 31 | fremainjoinpricebaseqty | 剩余应付基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付基本数量 |
| 32 | fremainjoinpriceqty | 剩余应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余应付数量 |
| 33 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 34 | fvmiremainsettlebaseqty | VMI剩余结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI剩余结算基本数量 |
| 35 | fremainreturnqty | 剩余退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余退库数量 |
| 36 | funverifyqty | 未核销数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未核销数量 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 38 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_ominber_fid |  | fid |
| 2 | pk_im_mdc_ominbillentry_r |  | fentryid |

---

## 物料明细-分表 t_im_mdc_ominbillentry_f

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_ominbillentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | ftaxrate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 4 | fdiscounttype | 折扣方式 | varchar | 30 |  | √ | ' ' | 折扣方式,枚举: A :折扣率 B :单位折扣额 NULL :无 |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 7 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 11 | fcuramountandtax | 价税合计本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计本位币 |
| 12 | fcurtaxamount | 税额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 税额本位币 |
| 13 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fcuramount | 金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 金额本位币 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 16 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_ominbillentry_f |  | fentryid |
| 2 | idx_im_mdc_ominbef_fid |  | fid |

---

## 关联子实体-子表 t_im_mdc_ominbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mdc_ominbillentry_lk

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
| 1 | idx_im_mdc_ominbillentry_lk_fk |  | fentryid |
| 2 | pk_im_mdc_ominbillentry_lk |  | fpkid |

---

## 简单委外入库单（废弃）-主表 t_im_mdc_ominbill

- **表名称：** 简单委外入库单（废弃）-主表
- **表名：** t_im_mdc_ominbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fhasapbusbill | 是否生成暂估应付单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应付单 |
| 6 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizoperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 10 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 13 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 14 | fquotation | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fasyncstatus | 异步状态 | varchar | 30 |  | √ | ' ' | 异步状态,枚举: A :处理中 B :已完成 |
| 18 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 19 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 24 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 29 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 30 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 31 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fbizoperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 34 | fbillcretype | 单据生成类型 | varchar | 30 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 35 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 37 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 38 | fpaymode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 39 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 40 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 41 | fbizdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 43 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_ominb_fcreatetime |  | fcreatetime |
| 2 | pk_im_mdc_ominbill |  | fid |
| 3 | idx_im_mdc_ominb_fbillno |  | fbillno |

---

## 关联子实体-子表 t_im_mdc_ominbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mdc_ominbill_lk

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
| 1 | idx_im_mdc_ominbill_lk_fk |  | fid |
| 2 | pk_im_mdc_ominbill_lk |  | fpkid |

---

## 简单委外入库单（废弃）-多语言表 t_im_mdc_ominbill_l

- **表名称：** 简单委外入库单（废弃）-多语言表
- **表名：** t_im_mdc_ominbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_ominbill_l |  | fpkid |
| 2 | idx_im_mdc_ominbl_fid |  | fid,flocaleid |

---

## 简单委外入库单（废弃）-关联追踪表 t_im_mdc_ominbill_tc

- **表名称：** 简单委外入库单（废弃）-关联追踪表
- **表名：** t_im_mdc_ominbill_tc

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
| 1 | pk_im_mdc_ominbill_tc |  | fid |
| 2 | idx_im_mdc_ominbill_tc_tbill |  | ftbillid |
| 3 | idx_im_mdc_ominbill_tc_tid |  | ftid |

---

## 物料明细-子表 t_im_mdc_ominbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_mdc_ominbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceivedate | 收货日期 | timestamp | 0 |  |  | null | 收货日期 |
| 3 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 10 | fownertype | 入库货主类型 | varchar | 30 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | finvoicesupplierid | 出票供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 20 | fkeepertype | 入库保管者类型 | varchar | 30 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 23 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 24 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 26 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 28 | fsuplot | 供应商批号 | varchar | 50 |  | √ | ' ' | 供应商批号 |
| 29 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 32 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 34 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 35 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 36 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 38 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 39 | fprovideraddress | 供货地址 | varchar | 300 |  | √ | ' ' | 供货地址 |
| 40 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 41 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 42 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 43 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 44 | fserialnumber | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 45 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 46 | fentrycomment | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 47 | fbackflushstatus | 倒冲状态 | varchar | 100 |  | √ | ' ' | 倒冲状态,枚举: A :无倒冲 B :部分倒冲 C :全部倒冲 D :不倒冲 |
| 48 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 49 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_ominbillentry |  | fentryid |
| 2 | idx_im_mdc_ominbe_fseq |  | fseq |
| 3 | idx_im_mdc_ominbe_fid |  | fid |

---

## 简单委外入库单（废弃）-反写记录表 t_im_mdc_ominbill_wb

- **表名称：** 简单委外入库单（废弃）-反写记录表
- **表名：** t_im_mdc_ominbill_wb

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
| 1 | idx_im_mdc_ominbill_wb_fk |  | fid |
| 2 | pk_im_mdc_ominbill_wb |  | fentryid |
