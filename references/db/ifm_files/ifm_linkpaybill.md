# 联动支付单-ifm_linkpaybill

## 关联子实体-子表 t_ifm_linkpay_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_linkpay_lk

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
| 1 | pk_ifm_linkpay_lk |  | fpkid |
| 2 | idx_ifm_linkpay_lk_fk |  | fid |

---

## 分录-子表 t_ifm_linkpayentry

- **表名称：** 分录-子表
- **表名：** t_ifm_linkpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayeracctbankid | 内部账号（银行） | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fpayeraccountid | 子账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 5 | fpayeraccountcode | 子账户联行号 | varchar | 255 |  | √ | ' ' | 子账户联行号 |
| 6 | fpayerbankid | 内部账户开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 7 | fconfirmpayamount | fconfirmpayamount | numeric | 23 | 10 | √ | 0 |  |
| 8 | fpaidstatus | fpaidstatus | varchar | 30 |  | √ | ' ' |  |
| 9 | fcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 10 | fsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | ' ' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | forgid | 成员单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fpayerinneracctbankid | 内部账号 | int8 | 64 |  | √ | 0 | [内部账户管理 ifm_inneracct](../ifm_files/ifm_inneracct.md) |
| 13 | fpaybillid | 付款单编号 | int8 | 64 |  | √ | 0 | 付款单 cas_paybill |
| 14 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 15 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 16 | fpayeraccountbankid | 子账户开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 17 | fsettlecur | 内部账户币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 19 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fpaymentbilltype | 付款单类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 21 | fdatasource | fdatasource | varchar | 30 |  | √ | ' ' |  |
| 22 | fpayableamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_linkpayentry |  | fentryid |
| 2 | idx_ifm_linkpayentry_fid |  | fid |

---

## 联动支付单-分表 t_ifm_linkpay_e

- **表名称：** 联动支付单-分表
- **表名：** t_ifm_linkpay_e

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
| 9 | fpaccountbankid | fpaccountbankid | int8 | 64 |  | √ | 0 |  |
| 10 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 11 | fispersonpay | 是否对私 | bpchar | 1 |  | √ | '0' | 是否对私 |
| 12 | fbankpaystatus | 银行付款单状态 | varchar | 5 |  | √ | ' ' | 银行付款单状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 13 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsbilltype | 源单单据类型 | varchar | 50 |  | √ | ' ' | 源单单据类型 |
| 15 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 16 | fbatchseqid | fbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 17 | fitempayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbeibankcheckflag | 银企返回的对账标识码 | varchar | 80 |  | √ | ' ' | 银企返回的对账标识码 |
| 20 | fsourcebillentryid | 源单分录明细ID | int8 | 64 |  | √ | 0 | 源单分录明细ID |
| 21 | fitempayeetypeid | 收款单位类型 | varchar | 30 |  | √ | ' ' | 收款单位类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 22 | fpaidstatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: A :待付款 B :付款处理中 C :已退单 D :已付款 |
| 23 | fvouchernum | fvouchernum | varchar | 100 |  | √ | ' ' |  |
| 24 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 25 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 26 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 27 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_linkpay_e |  | fid |
| 2 | idx_ifm_linkpay_e_fbankpayid |  | fbankpayingid |

---

## 联动支付单-反写记录表 t_ifm_linkpay_wb

- **表名称：** 联动支付单-反写记录表
- **表名：** t_ifm_linkpay_wb

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
| 1 | pk_ifm_linkpay_wb |  | fentryid |
| 2 | idx_ifm_linkpay_wb_fk |  | fid |

---

## 关联子实体-子表 t_ifm_linkpayentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_linkpayentry_lk

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
| 1 | pk_ifm_linkpayentry_lk |  | fpkid |
| 2 | idx_ifm_linkpayentry_lk_fk |  | fentryid |

---

## 联动支付单-主表 t_ifm_linkpay

- **表名称：** 联动支付单-主表
- **表名：** t_ifm_linkpay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | fopenorgid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 付款组织(不用) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpayeetypeid | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 other :其他 |
| 5 | fpayeebankid | 收款账户开户行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 6 | fpayeeaccformid | 收款账户基础资料标识 | varchar | 30 |  | √ | ' ' | 收款账户基础资料标识 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpayeeformid | 收款人基础资料标识 | varchar | 30 |  | √ | ' ' | 收款人基础资料标识 |
| 9 | fpayeeacctbankid | 收款账户ID | int8 | 64 |  | √ | 0 | 收款账户ID |
| 10 | fexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0 | 付款汇率 |
| 11 | freccountryid | 收款方国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | factpayamount | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 15 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ifm_payacceptancebill :内部结算受理 fca_transdownbill :下拨单 ifm_deduction :结算中心扣款 ifm_interestbill :贷款结息单 ifm_repaymentbill :贷款收回单 scf_finrepaybill :供应链融资还款处理 ifm_notice_release :内部通知存款解活处理 ifm_release :内部定期存款解活处理 ifm_notice_deposit :内部通知存款 ifm_deposit :内部定期存款 cas_paybill :付款单 |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fpayeebankname | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 20 | frecprovince | 收款方省 | varchar | 80 |  | √ | ' ' | 收款方省 |
| 21 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 24 | fagentfinorgid | 开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 25 | frecaccbankname | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 26 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 27 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fpayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 29 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fpayamountsubtract | fpayamountsubtract | numeric | 23 | 10 | √ | 0 |  |
| 31 | fpayeebanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 32 | flocalamount | 付款金额本位币 | numeric | 19 | 6 | √ | 0 | 付款金额本位币 |
| 33 | fagentfinorgcatid | 付款银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 34 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 35 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 36 | fpayamountsum | fpayamountsum | numeric | 23 | 10 | √ | 0 |  |
| 37 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 38 | fscorgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | freccity | 收款方市县 | varchar | 80 |  | √ | ' ' | 收款方市县 |
| 40 | fpayeecurrency | 收款账号币种 | int8 | 64 |  | √ | 0 | 收款账号币种 |
| 41 | fpayeeid | 收款人ID | int8 | 64 |  | √ | 0 | 收款人ID |
| 42 | fisdiffcur | fisdiffcur | bpchar | 1 |  | √ | '0' |  |
| 43 | fagentpayeraccname | fagentpayeraccname | varchar | 255 |  | √ | ' ' |  |
| 44 | frecbanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 45 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 46 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | fsettletnumber | 结算号 | varchar | 30 |  | √ | ' ' | 结算号 |
| 48 | fagentpayeraccountid | 母账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 49 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 50 | fpayquotation | 付款汇率换算方式 | varchar | 5 |  | √ | ' ' | 付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 51 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 52 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 53 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 54 | fcurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_linkpay_fscorgid |  | fscorgid |
| 2 | pk_ifm_linkpay |  | fid |

---

## 联动支付单-关联追踪表 t_ifm_linkpay_tc

- **表名称：** 联动支付单-关联追踪表
- **表名：** t_ifm_linkpay_tc

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
| 1 | pk_ifm_linkpay_tc |  | fid |
| 2 | idx_ifm_linkpay_tc_tbill |  | ftbillid |
| 3 | idx_ifm_linkpay_tc_tid |  | ftid |
