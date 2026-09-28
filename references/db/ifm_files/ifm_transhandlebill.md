# 付款结算单-ifm_transhandlebill

## 关联子实体-子表 t_ifm_transhandle_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_transhandle_lk

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
| 1 | idx_ifm_transhandle_lk_fk |  | fid |
| 2 | pk_ifm_transhandle_lk |  | fpkid |

---

## 分录-子表 t_ifm_transhandleentry

- **表名称：** 分录-子表
- **表名：** t_ifm_transhandleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayeracctbankid | 付款账号（银行） | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 3 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 4 | fpayerbankid | 内部账户开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 5 | fconfirmpayamount | 已下推付款单金额 | numeric | 23 | 10 | √ | 0 | 已下推付款单金额 |
| 6 | fpaidstatus | 付款单确认状态 | varchar | 30 |  | √ | ' ' | 付款单确认状态,枚举: 0 :待确认 1 :已确认 2 : |
| 7 | fcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 8 | fsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | '0' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 9 | forgid | 成员单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fpayerinneracctbankid | 内部账户 | int8 | 64 |  | √ | 0 | [内部账户管理 ifm_inneracct](../ifm_files/ifm_inneracct.md) |
| 11 | fpaybillid | 付款单编号 | int8 | 64 |  | √ | 0 | 付款单 cas_paybill |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 14 | fpaylocalamt | 付款金额本位币 | numeric | 23 | 10 | √ | 0 | 付款金额本位币 |
| 15 | fsettlecur | 内部账户币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 17 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | fpaymentbilltype | 付款单类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 19 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :代付认领 2 :下推生成 |
| 20 | fpayableamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fsettlementlocalamt | 结算金额本位币 | numeric | 23 | 10 | √ | 0 | 结算金额本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_transhandleentry |  | fentryid |
| 2 | idx_ifm_transhandleentry_fid |  | fid |

---

## 付款结算单-分表 t_ifm_transhandle_e

- **表名称：** 付款结算单-分表
- **表名：** t_ifm_transhandle_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaymentmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 INNERPAY :内部付款 |
| 3 | ffaildescription | ffaildescription | varchar | 500 |  | √ | ' ' |  |
| 4 | facttradedate | facttradedate | timestamp | 0 |  |  | null |  |
| 5 | fcommitbetime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 6 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 7 | fdetailseqid | fdetailseqid | varchar | 80 |  | √ | ' ' |  |
| 8 | fbankpayingid | 银行付款单ID | int8 | 64 |  | √ | 0 | 银行付款单ID |
| 9 | fpaysumlocalamt | 付款金额汇总本位币 | numeric | 23 | 10 | √ | 0 | 付款金额汇总本位币 |
| 10 | fpaccountbankid | 子账户银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 11 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 12 | ftoallocatedtlocalamt | 待分配金额本位币 | numeric | 23 | 10 | √ | 0 | 待分配金额本位币 |
| 13 | fispersonpay | 是否对私 | bpchar | 1 |  | √ | '0' | 是否对私 |
| 14 | fbankpaystatus | 银行付款单状态 | varchar | 5 |  | √ | ' ' | 银行付款单状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 15 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsbilltype | 源单单据类型 | varchar | 50 |  | √ | ' ' | 源单单据类型 |
| 17 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 18 | fentrustorgid | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbatchseqid | fbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 20 | fitempayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbeibankcheckflag | 银企返回的对账标识码 | varchar | 80 |  | √ | ' ' | 银企返回的对账标识码 |
| 23 | fsourcebillentryid | 源单分录明细ID | int8 | 64 |  | √ | 0 | 源单分录明细ID |
| 24 | fapplyorgid | 申请付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fitempayeetypeid | 收款单位类型 | varchar | 30 |  | √ | ' ' | 收款单位类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 26 | fpaidstatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: A :待付款 B :付款处理中 C :已退单 D :已付款 |
| 27 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 28 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 29 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 30 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_transhandle_e |  | fid |
| 2 | idx_ifm_transe_fbankpayid |  | fbankpayingid |

---

## 关联子实体-子表 t_ifm_transhandleentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_transhandleentry_lk

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
| 1 | pk_ifm_transhandleentry_lk |  | fpkid |
| 2 | idx_ifm_transhandleentry_lk_fk |  | fentryid |

---

## 付款结算单-主表 t_ifm_transhandle

- **表名称：** 付款结算单-主表
- **表名：** t_ifm_transhandle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 付款组织(不用) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpayeetypeid | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 other :其他 |
| 5 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 6 | fpayeeaccformid | 收款账户基础资料标识 | varchar | 30 |  | √ | ' ' | 收款账户基础资料标识 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpayeeformid | 收款人基础资料标识 | varchar | 30 |  | √ | ' ' | 收款人基础资料标识 |
| 9 | fpayeeacctbankid | 收款账户ID | int8 | 64 |  | √ | 0 | 收款账户ID |
| 10 | fexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0 | 付款汇率 |
| 11 | freccountryid | 收款方国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | factpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 15 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ifm_payacceptancebill :内部结算受理 fca_transdownbill :下拨单 ifm_deduction :结算中心扣款 ifm_interestbill :贷款结息单 ifm_repaymentbill :贷款收回单 scf_finrepaybill :供应链融资还款处理 ifm_notice_release :内部通知存款解活处理 ifm_release :内部定期存款解活处理 ifm_notice_deposit :内部通知存款 ifm_deposit :内部定期存款 cas_paybill :付款单 |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fpayeebankname | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 20 | frecprovince | 收款方省 | varchar | 80 |  | √ | ' ' | 收款方省 |
| 21 | ftranstype | 交易类型 | varchar | 30 |  | √ | ' ' | 交易类型,枚举: 1 :内部代付 2 :内部转账 3 :资金下拨 6 :内部扣款 7 :贷款收回 8 :贷款结息 10 :银行扣款 11 :活转定 12 :定转活 13 :供应链融资还款 |
| 22 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 25 | fagentfinorgid | 开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | frecaccbankname | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 27 | facceptuserid | facceptuserid | int8 | 64 |  | √ | 0 |  |
| 28 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 29 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fpayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 31 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fpayamountsubtract | 待认领金额 | numeric | 23 | 10 | √ | 0 | 待认领金额 |
| 33 | fpayeebanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 34 | flocalamount | 付款金额本位币 | numeric | 19 | 6 | √ | 0 | 付款金额本位币 |
| 35 | fagentfinorgcatid | 付款银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 36 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 37 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 38 | fpayamountsum | 付款金额汇总 | numeric | 23 | 10 | √ | 0 | 付款金额汇总 |
| 39 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 40 | fscorgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | freccity | 收款方市县 | varchar | 80 |  | √ | ' ' | 收款方市县 |
| 42 | fpayeecurrency | 收款账号币种 | int8 | 64 |  | √ | 0 | 收款账号币种 |
| 43 | fpayeeid | 收款人ID | int8 | 64 |  | √ | 0 | 收款人ID |
| 44 | fisdiffcur | 异币种付款 | bpchar | 1 |  | √ | '0' | 异币种付款 |
| 45 | fagentpayeraccname | fagentpayeraccname | varchar | 255 |  | √ | ' ' |  |
| 46 | frecbanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 47 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 48 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | facceptdatetime | facceptdatetime | timestamp | 0 |  |  | null |  |
| 50 | fsettletnumber | 结算号 | varchar | 30 |  | √ | ' ' | 结算号 |
| 51 | fagentpayeraccountid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 52 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 53 | fpayquotation | 付款汇率换算方式 | varchar | 5 |  | √ | '0' | 付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 54 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 55 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 56 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 57 | fcurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_transhandle_fscorgid |  | fscorgid |
| 2 | pk_ifm_transhandle |  | fid |

---

## 付款结算单-反写记录表 t_ifm_transhandle_wb

- **表名称：** 付款结算单-反写记录表
- **表名：** t_ifm_transhandle_wb

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
| 1 | idx_ifm_transhandle_wb_fk |  | fid |
| 2 | pk_ifm_transhandle_wb |  | fentryid |

---

## 付款结算单-关联追踪表 t_ifm_transhandle_tc

- **表名称：** 付款结算单-关联追踪表
- **表名：** t_ifm_transhandle_tc

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
| 1 | idx_ifm_transhandle_tc_tbill |  | ftbillid |
| 2 | idx_ifm_transhandle_tc_tid |  | ftid |
| 3 | pk_ifm_transhandle_tc |  | fid |
