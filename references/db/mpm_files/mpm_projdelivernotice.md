# 项目发货通知单-mpm_projdelivernotice

## 关联子实体-子表 t_mpm_delivernoticeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_delivernoticeentry_lk

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
| 1 | pk_mpm_delivernoticeentry_lk |  | fpkid |
| 2 | idx_mpm_delivernoticeentry_lk_fk |  | fentryid |

---

## 物料明细-分表 t_mpm_delivernoticeentry_m

- **表名称：** 物料明细-分表
- **表名：** t_mpm_delivernoticeentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpackedbaseqty | 已装箱基本数量 | numeric | 23 | 10 | √ | 0 | 已装箱基本数量 |
| 3 | frejectedbaseqty | 已拒收基本数量 | numeric | 23 | 10 | √ | 0 | 已拒收基本数量 |
| 4 | fprepackbaseqty | 预装箱基本数量 | numeric | 23 | 10 | √ | 0 | 预装箱基本数量 |
| 5 | fpointedqty | 已点收数量 | numeric | 23 | 10 | √ | 0 | 已点收数量 |
| 6 | factrecbaseqty | 已实收基本数量 | numeric | 23 | 10 | √ | 0 | 已实收基本数量 |
| 7 | factrecqty | 已实收数量 | numeric | 23 | 10 | √ | 0 | 已实收数量 |
| 8 | frejectedqty | 已拒收数量 | numeric | 23 | 10 | √ | 0 | 已拒收数量 |
| 9 | fassotransportqty | 关联运输数量 | numeric | 23 | 10 | √ | 0 | 关联运输数量 |
| 10 | fpointedbaseqty | 已点收基本数量 | numeric | 23 | 10 | √ | 0 | 已点收基本数量 |
| 11 | fassotransportbaseqty | 关联运输基本数量 | numeric | 23 | 10 | √ | 0 | 关联运输基本数量 |
| 12 | fprepackqty | 预装箱数量 | numeric | 23 | 10 | √ | 0 | 预装箱数量 |
| 13 | ftransportbaseqty | 已运输基本数量 | numeric | 23 | 10 | √ | 0 | 已运输基本数量 |
| 14 | fpackedqty | 已装箱数量 | numeric | 23 | 10 | √ | 0 | 已装箱数量 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | ftransportqty | 已运输数量 | numeric | 23 | 10 | √ | 0 | 已运输数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_delivernoticeentry_m |  | fentryid |
| 2 | idx_mpm_deliveentry_mid |  | fid |

---

## 物料明细-多语言表 t_mpm_delivernoticeentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_mpm_delivernoticeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdelivermaterialdes | 发货物资描述 | varchar | 255 |  | √ | ' ' | 发货物资描述 |
| 2 | fdeliveraddress | 发货地点 | varchar | 512 |  |  | null | 发货地点 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_delivernoticeentry_l |  | fpkid |
| 2 | idx_mpm_delinoticeen_l_fid |  | fentryid,flocaleid |

---

## 物料明细-分表 t_mpm_delivernoticeentry_q

- **表名称：** 物料明细-分表
- **表名：** t_mpm_delivernoticeentry_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0 | 发货超发比率(%) |
| 3 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 6 | funit2ndid | 主辅单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | funit2ndrate | 换算率(主辅单位) | numeric | 23 | 10 | √ | 0 | 换算率(主辅单位) |
| 8 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 9 | fdeliverratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0 | 发货欠发比率(%) |
| 10 | fdeliverqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0 | 发货上限数量 |
| 11 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fdeliverbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0 | 发货上限基本数量 |
| 15 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 16 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fdeliverbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0 | 发货下限基本数量 |
| 19 | fexpectqty | 预计可发量 | numeric | 23 | 10 | √ | 0 | 预计可发量 |
| 20 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 23 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 24 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 26 | fqtyunit2nd | 主辅数量 | numeric | 23 | 10 | √ | 0 | 主辅数量 |
| 27 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 28 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 29 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 30 | fdeliverqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0 | 发货下限数量 |
| 31 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 32 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 33 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_delientry_q_fid |  | fid |
| 2 | pk_mpm_delivernoticeentry_q |  | fentryid |

---

## 物料明细-分表 t_mpm_delivernoticeentry_r

- **表名称：** 物料明细-分表
- **表名：** t_mpm_delivernoticeentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvfailqty | 关联不合格出库数量 | numeric | 23 | 10 | √ | 0 | 关联不合格出库数量 |
| 3 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 4 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 5 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 6 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 7 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | ffailqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 9 | finvbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 10 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 11 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 12 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 14 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 15 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 16 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 17 | fassoinvinspectbaseqty | 关联请检基本数量 | numeric | 23 | 10 | √ | 0 | 关联请检基本数量 |
| 18 | ffailsaleableqty | 不合格可销售数量 | numeric | 23 | 10 | √ | 0 | 不合格可销售数量 |
| 19 | fpassbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 20 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 21 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 22 | fpassqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 23 | fconbillentryseq | 合同分录序号 | int8 | 64 |  | √ | 0 | 合同分录序号 |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 25 | finvpassqty | 关联合格出库数量 | numeric | 23 | 10 | √ | 0 | 关联合格出库数量 |
| 26 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | finvqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 29 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 30 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0 | 已退库数量 |
| 31 | finvpassbaseqty | 关联合格出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联合格出库基本数量 |
| 32 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 33 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 34 | fsrcsysbillentryid | 来源系统单据分录id | varchar | 100 |  | √ | ' ' | 来源系统单据分录id |
| 35 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 36 | fassoinvinspectqty | 关联请检数量 | numeric | 23 | 10 | √ | 0 | 关联请检数量 |
| 37 | ffailbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0 | 不合格基本数量 |
| 38 | ffailsaleablebaseqty | 不合格可销售基本数量 | numeric | 23 | 10 | √ | 0 | 不合格可销售基本数量 |
| 39 | fscrapbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | finvfailbaseqty | 关联不合格出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联不合格出库基本数量 |
| 42 | fsrcsysbillid | 来源系统单据id | varchar | 100 |  | √ | ' ' | 来源系统单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_delientry_r_fid |  | fid |
| 2 | pk_mpm_delivernoticeentry_r |  | fentryid |

---

## 项目发货通知单-分表 t_mpm_delivernotice_f

- **表名称：** 项目发货通知单-分表
- **表名：** t_mpm_delivernotice_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 3 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 5 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 8 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 9 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 10 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 14 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 17 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_delinotice_f_stog |  | fsettleorgid |
| 2 | pk_mpm_delivernotice_f |  | fid |

---

## 项目发货通知单-分表 t_mpm_delivernotice_c

- **表名称：** 项目发货通知单-分表
- **表名：** t_mpm_delivernotice_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 3 | faddress | 联系地址 | varchar | 512 |  |  | ' ' | 联系地址 |
| 4 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 5 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 6 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 7 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 8 | freceiveaddress_bak | 发货明细执行地址(后台用) | varchar | 512 |  |  | ' ' | 发货明细执行地址(后台用) |
| 9 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 10 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 11 | freceiveaddress | 收货地址 | varchar | 512 |  |  | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_delivernotice_c |  | fid |

---

## 项目发货通知单-分表 t_mpm_delivernotice_a

- **表名称：** 项目发货通知单-分表
- **表名：** t_mpm_delivernotice_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectdesc_tag | 项目描述大文本_详情 | text | 0 |  |  | null | 项目描述大文本_详情 |
| 3 | fprojectdesc | 项目描述大文本 | text | 0 |  |  | null | 项目描述大文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_delivernotice_a |  | fid |

---

## 项目发货通知单-主表 t_mpm_delivernotice

- **表名称：** 项目发货通知单-主表
- **表名：** t_mpm_delivernotice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvgroupid | 库存组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 3 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 5 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 8 | ftransportstatus | ftransportstatus | bpchar | 1 |  | √ | 'A' |  |
| 9 | fbiztime | 通知日期 | timestamp | 0 |  |  | null | 通知日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :正常 B :已终止 |
| 12 | fdeliverdeptid | 发货部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fterminaterid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 16 | fisvirtualbill | 是否虚单 | bpchar | 1 |  | √ | '0' | 是否虚单 |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fdeliveroperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 19 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fheadprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fencasestatus | 装箱状态 | bpchar | 1 |  | √ | 'A' | 装箱状态,枚举: A :未装箱 B :部分装箱 C :已装箱 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fisprojectbegin | 项目期初 | bpchar | 1 |  | √ | '0' | 项目期初 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 29 | fdeliverpatternid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 30 | flastupdateuserid | 最后修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | flastupdatetime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 33 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 34 | fclosemanual | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 35 | flogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 36 | fdeliveruserid | 发货负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fpointstatus | 点收状态 | bpchar | 1 |  | √ | 'A' | 点收状态,枚举: A :未点收 B :部分点收 C :已点收 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_delivernotice_bilno |  | fbillno |
| 2 | pk_mpm_delivernotice |  | fid |
| 3 | idx_mpm_delinotice_biztim |  | fbiztime |

---

## 项目发货通知单-反写记录表 t_mpm_delivernotice_wb

- **表名称：** 项目发货通知单-反写记录表
- **表名：** t_mpm_delivernotice_wb

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
| 1 | pk_mpm_delivernotice_wb |  | fentryid |
| 2 | idx_mpm_delivernotice_wb_fk |  | fid |

---

## 项目发货通知单-关联追踪表 t_mpm_delivernotice_tc

- **表名称：** 项目发货通知单-关联追踪表
- **表名：** t_mpm_delivernotice_tc

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
| 1 | idx_mpm_delivernotice_tc_tbill |  | ftbillid |
| 2 | pk_mpm_delivernotice_tc |  | fid |
| 3 | idx_mpm_delivernotice_tc_tid |  | ftid |

---

## 物料明细-子表 t_mpm_delivernoticeentry

- **表名称：** 物料明细-子表
- **表名：** t_mpm_delivernoticeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpectqtydate | 获取可发量日期 | timestamp | 0 |  |  | null | 获取可发量日期 |
| 3 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 7 | fdelivermaterialdes | 发货物资描述 | varchar | 255 |  | √ | ' ' | 发货物资描述 |
| 8 | frowstatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 9 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 11 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | fdeliveraddress | 发货地点 | varchar | 512 |  |  | null | 发货地点 |
| 13 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 14 | fdeliveraddresstype | 发货类型和地点 | bpchar | 1 |  | √ | ' ' | 发货类型和地点,枚举: A :生产现场-物料 C :生产现场-物资描述 B :仓库 |
| 15 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 16 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 17 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 20 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 22 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 23 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 25 | fsuitesettletype | 套件结算方式 | varchar | 5 |  | √ | ' ' | 套件结算方式,枚举: |
| 26 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 30 | fmaterialname | 物料名称 | varchar | 255 |  |  | null | 物料名称 |
| 31 | frowclosemanual | 行手工关闭 | bpchar | 1 |  | √ | '0' | 行手工关闭 |
| 32 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 33 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 34 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 35 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 36 | frowclosemanualever | 是否手工行关闭过 | bpchar | 1 |  | √ | '0' | 是否手工行关闭过 |
| 37 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 38 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 39 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 40 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 41 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 42 | fcloseupdatesaleorder | 手工关闭更新订单 | bpchar | 1 |  | √ | '0' | 手工关闭更新订单 |
| 43 | fdeliverydate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 44 | fproducttype | 产品类别 | varchar | 255 |  | √ | '0' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 45 | frowterminatestatus | 行终止状态 | bpchar | 1 |  | √ | ' ' | 行终止状态,枚举: |
| 46 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 47 | fdeliverinspect | 发货检验 | bpchar | 1 |  | √ | '0' | 发货检验 |
| 48 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 49 | fsuitedeliverytype | 套件发货方式 | varchar | 5 |  | √ | ' ' | 套件发货方式,枚举: A :成套发货 B :不成套发货 C :成套退货 D :不成套退货 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_delivernoticeentry |  | fentryid |
| 2 | idx_mpm_delientry_fid |  | fid |
