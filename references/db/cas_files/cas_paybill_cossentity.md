# 跨主体转账-cas_paybill_cossentity

## 还款明细-子表 t_cas_paycossentityentry

- **表名称：** 还款明细-子表
- **表名：** t_cas_paycossentityentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpayeetypeid | 收款单位类型 | varchar | 30 |  | √ | ' ' | 收款单位类型,枚举: bos_org :公司 bd_customer :客户 bd_supplier :供应商 |
| 6 | factpayamt | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 7 | frepairedamount | 本次还款金额 | numeric | 23 | 10 | √ | 0 | 本次还款金额 |
| 8 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | funpaidamount | 可还款金额 | numeric | 23 | 10 | √ | 0 | 可还款金额 |
| 13 | fitempayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fcossentityreceipt | 跨主体转账单编号 | int8 | 64 |  | √ | 0 | 跨主体转账 cas_paybill_cossentity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_paycossentityentry |  | fentryid |

---

## 跨主体转账-关联追踪表 t_cas_paybillcossentity_tc

- **表名称：** 跨主体转账-关联追踪表
- **表名：** t_cas_paybillcossentity_tc

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
| 1 | idx_cas_paybillcossentity_tc_tid |  | ftid |
| 2 | pk_cas_paybillcossentity_tc |  | fid |
| 3 | idx_cas_paybillcossentity_tc_tbill |  | ftbillid |

---

## 跨主体转账-反写记录表 t_cas_paybillcossentity_wb

- **表名称：** 跨主体转账-反写记录表
- **表名：** t_cas_paybillcossentity_wb

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
| 1 | pk_cas_paybillcossentity_wb |  | fentryid |
| 2 | idx_cas_paybillcossentity_wb_fk |  | fid |

---

## 关联子实体-子表 t_cas_paycossentityentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_paycossentityentry_lk

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
| 1 | pk_cas_paycossentityentry_lk |  | fpkid |
| 2 | idx_cas_paycossentityentry_lk_fk |  | fentryid |

---

## 跨主体转账-主表 t_cas_paybillcossentity

- **表名称：** 跨主体转账-主表
- **表名：** t_cas_paybillcossentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpayeetypeid | 收款单位类型 | varchar | 30 |  | √ | ' ' | 收款单位类型,枚举: bos_org :公司 bd_customer :客户 bd_supplier :供应商 |
| 4 | fpayeebankid | 收款账户开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0 | 付款汇率 |
| 7 | fpayeeacctbankid | 收款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 8 | fpayeeacctcashid | 收款账号 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 9 | frecbillorgid | 对方收款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fitempayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | factpayamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 14 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpayeracctname | 付款账户名称 | varchar | 255 |  | √ | ' ' | 付款账户名称 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已付款 E :付款处理中 |
| 17 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 18 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fisrecing | 收款单自动收款 | bpchar | 1 |  | √ | '0' | 收款单自动收款 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fisperiod | 期初 | bpchar | 1 |  | √ | '0' | 期初 |
| 23 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 24 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 25 | fcommitbetime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 26 | frecaccbankname | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 27 | frelatedrepayamount | 关联还款金额 | numeric | 23 | 10 | √ | 0 | 关联还款金额 |
| 28 | ffee | 手续费 | numeric | 23 | 10 | √ | 0 | 手续费 |
| 29 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 30 | fcheckboxfee | 手续费独立流水 | bpchar | 1 |  | √ | '0' | 手续费独立流水 |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | funpaidamount | 未还款金额 | numeric | 23 | 10 | √ | 0 | 未还款金额 |
| 33 | fpayeracctbankid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 34 | fpayeracctcashid | 付款账号 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 35 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | flocalamount | 付款金额本位币 | numeric | 23 | 10 | √ | 0 | 付款金额本位币 |
| 37 | fpayerbankid | 付款账户开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 38 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 39 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 40 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 41 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 42 | frepairedamount | 已还款金额 | numeric | 23 | 10 | √ | 0 | 已还款金额 |
| 43 | frecbanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 44 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 46 | fpayquotation | 付款汇率换算方式 | varchar | 30 |  | √ | '0' | 付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 47 | frecbillcurrency | 对方组织本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 49 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 50 | fconfirmpaydate | 确认付款时间 | timestamp | 0 |  |  | null | 确认付款时间 |
| 51 | fcurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pbce_fpayeracctbankid |  | fpayeracctbankid |
| 2 | idx_cas_pbce_fbilltype |  | fbilltypeid |
| 3 | idx_cas_pbce_fbillno |  | fbillno |
| 4 | idx_cas_pbce_forgid |  | forgid |
| 5 | pk_t_cas_paybillcossentity |  | fid |

---

## 跨主体转账-分表 t_cas_paybillcossentity_a

- **表名称：** 跨主体转账-分表
- **表名：** t_cas_paybillcossentity_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 3 | fbankcheckflag | 对账标识码 | varchar | 1024 |  | √ | ' ' | 对账标识码 |
| 4 | fpaycountryid | 付款方国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 5 | fsourcebilltypeid | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_paybill_cossentity :跨主体转账 |
| 6 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 7 | fbankpayingid | 银行付款单ID | int8 | 64 |  | √ | 0 | 银行付款单ID |
| 8 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 9 | fpaybillnumber | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单 cas_paybill |
| 10 | fbefileexporttimes | 网银文件导出次数 | int4 | 32 |  | √ | 0 | 网银文件导出次数 |
| 11 | fbankpaystatus | 银行付款单状态 | varchar | 5 |  | √ | ' ' | 银行付款单状态,枚举: OP :准备提交 OS :银企处理中 OZ :银企处理中止 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 12 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 13 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 14 | frecbillnumber | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单 cas_recbill |
| 15 | fbankcheckflag_tag | 对账标识码_详情 | varchar | 1024 |  | √ | ' ' | 对账标识码_详情 |
| 16 | fbatchseqid | 提交银企批次流水 | varchar | 80 |  | √ | ' ' | 提交银企批次流水 |
| 17 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 18 | fbankreturndate | 银行返回日期 | timestamp | 0 |  |  | null | 银行返回日期 |
| 19 | fsourceentry | 源单分录标识 | varchar | 50 |  | √ | ' ' | 源单分录标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_paybillcossentity_a |  | fid |
