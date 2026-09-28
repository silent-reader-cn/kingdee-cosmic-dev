# 付款单-cas_paybill

## 付款单-关联追踪表 t_cas_paymentbill_tc

- **表名称：** 付款单-关联追踪表
- **表名：** t_cas_paymentbill_tc

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
| 1 | t_cas_paymentbill_tc_pkey |  | fid |
| 2 | idx_cas_paymentbill_tc_tbill |  | ftbillid |
| 3 | idx_cas_pb__tc_ftbillid |  | ftbillid |
| 4 | idx_cas_paymentbill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_cas_paymentbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_paymentbillentry_lk

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
| 1 | idx_cas_pbtllk_fseq |  | fseq |
| 2 | t_cas_paymentbillentry_lk_pkey |  | fpkid |
| 3 | idx_cas_pbtllk_fentryid |  | fentryid |

---

## 单据体-子表 t_cas_paybankcheckflag

- **表名称：** 单据体-子表
- **表名：** t_cas_paybankcheckflag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | febankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pbc_fid |  | fid |
| 2 | idx_cas_paybankcheckflag |  | febankcheckflag |
| 3 | pk_t_cas_paybankcheckflag |  | fentryid |

---

## 付款明细-分表 t_cas_paymentbillentry_e

- **表名称：** 付款明细-分表
- **表名：** t_cas_paymentbillentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurdept | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 3 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 4 | fcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 5 | fsalesgroup | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 6 | fsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | '0' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 7 | fsalesorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsetexratetableid | 结算汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fsalesman | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 10 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 11 | fsettlecur | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 13 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fsettlemainbookid | 结算本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fsalesdept | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fpurdepartment | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fsetmainexrate | 结算本币兑本币汇率 | numeric | 23 | 10 | √ | 0 | 结算本币兑本币汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_paymentbillentry_e |  | fentryid |
| 2 | idx_cas_paymentbillentry_e_fid |  | fid |

---

## 结算号-多选基础资料表 t_cas_paymentbill_bl

- **表名称：** 结算号-多选基础资料表
- **表名：** t_cas_paymentbill_bl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 应收应付票据登记 cdm_payandrecdraft_f7 |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_paymentbill_bl_pkey |  | fpkid |
| 2 | idx_cas_paymentbill_bl_fk |  | fid |

---

## 票据信息-子表 t_cas_paybilldraftentry

- **表名称：** 票据信息-子表
- **表名：** t_cas_paybilldraftentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdraftamt | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0.00 | 票面金额(子票包金额) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fourbankid | 我方银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_paybilldraftentry_fid |  | fid |
| 2 | pk_t_cas_paybilldraftentry |  | fentryid |

---

## 付款单-反写记录表 t_cas_paymentbill_wb

- **表名称：** 付款单-反写记录表
- **表名：** t_cas_paymentbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | foperate | foperate | varchar | 30 |  |  | null |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  |  | null |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pbtlwb_fid |  | fid |
| 2 | idx_cas_pbtlwb_fseq |  | fseq |
| 3 | t_cas_paymentbill_wb_pkey |  | fentryid |
| 4 | idx_cas_pb_wb_fsbillid_fsid |  | fsid,fsbillid |

---

## 付款单-主表 t_cas_paymentbill

- **表名称：** 付款单-主表
- **表名：** t_cas_paymentbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayernumber | 付款组织编码 | varchar | 500 |  | √ | ' ' | 付款组织编码 |
| 3 | fpaymentmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 4 | fopenorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbankcheckflag | 对账标识码(旧) | varchar | 1024 |  | √ | ' ' | 对账标识码(旧) |
| 6 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fpayeetypeid | 收款单位类型 | varchar | 30 |  | √ | ' ' | 收款单位类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :公司 other :其他 cas_othercontactunit :其他往来单位 |
| 8 | fpayeebankid | 收款账户开户行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 9 | fpaymentidentifyid | 支付类型 | int8 | 64 |  | √ | 0 | 付款标识 cas_paymentidentify |
| 10 | fpayeeaccformid | 收款账户基础资料标识 | varchar | 30 |  | √ | ' ' | 收款账户基础资料标识 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpayeeformid | 收款单位基础资料标识（废弃） | varchar | 30 |  | √ | ' ' | 收款单位基础资料标识（废弃） |
| 13 | fpayeeacctbankid | 收款账户ID | int8 | 64 |  | √ | 0 | 收款账户ID |
| 14 | fexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 15 | freccountryid | 收款方国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 16 | fbankpaystatus | 银行付款单状态 | varchar | 5 |  | √ | ' ' | 银行付款单状态,枚举: OP :准备提交 OS :银企处理中 OZ :银企处理中止 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 17 | fissingle | 多分录 | bpchar | 1 |  | √ | '0' | 多分录 |
| 18 | fbusinesstypebase | 业务类型(基础资料) | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fbatchseqid | 提交银企批次流水 | varchar | 80 |  | √ | ' ' | 提交银企批次流水 |
| 21 | factpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 22 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fpayeeacctbank | 收款银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 24 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_betransdetail :交易明细 er_dailyreimbursebill :日常报销单 ap_finapbill :财务应付单 cas_recbill :收款单 er_vehiclecheckingbill :用车结算单 er_dailyloanbill :借款单 er_planecheckingbill :机票结算单 er_hotelcheckingbill :酒店结算单 er_tripreimbursebill :差旅报销单 er_checkingpaybill :月结付款单 er_tripreqbill :出差申请单 pm_purorderbill :采购订单 bei_transdetail :交易明细 ap_payapply :付款申请单 fca_transupbill :上划单 cfm_repaymentbill :还款单 cfm_interestbill :付息单 cas_paybill :付款单 cfm_preinterestbill :利息预提单 cdm_drafttradebill :票据业务处理单 er_publicreimbursebill :对公报销单 ec_paymentapply :建筑付款申请单 fr_glreim_paybill :总账付款单 bei_intelpay :被动付款入账 ifm_trandisposebill :交易处理单 pm_om_purorderbill :委外订单 cfm_invest_loanbill :放款单 fca_transdownbill :下拨单 cas_payapplybill :付款申请单 cfm_feebill :费用明细单 lc_arrival :到单处理 cas_transferapply :调拨申请 tm_businessbill :生命周期操作 tm_structdeposit :结构性存款 tm_rateswap :互换 tm_bond_fix :固定利率债券/零息债券 tm_bond_float :浮动利率债券 tm_forex_options :外汇期权 cim_deposit :定期存款处理 cim_noticedeposit :通知存款处理 conm_purcontract :采购合同 sctm_scpo :委外采购订单 sm_salorder :销售订单 conm_salcontract :销售合同 cas_claimcenterbill :认领通知单 scf_fincreditbill :供应链融资债权业务处理 ar_finarbill :财务应收单 er_prepaybill :预付单 ifm_currentintbill :内部利息结息单 ifm_linkpaybill :联动支付单 occba_moneyincome :资金收入单 |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已付款 E :付款处理中 F :银行退票 G :已退单 H :已作废 I :退款 J :票据处理中 |
| 26 | fpayeebankname | 收款账户开户行 | varchar | 255 |  | √ | ' ' | 收款账户开户行 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 29 | frecprovince | 收款方省 | varchar | 80 |  | √ | ' ' | 收款方省 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 33 | fcommitbetime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 34 | fpriority | 紧急程度 | varchar | 30 |  | √ | ' ' | 紧急程度,枚举: prior :优先 public :普通 defer :暂缓 |
| 35 | frecaccbankname | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 36 | fdetailseqid | 交易明细流水 | varchar | 80 |  | √ | ' ' | 交易明细流水 |
| 37 | fbankpayingid | 银行付款单ID | int8 | 64 |  | √ | 0 | 银行付款单ID |
| 38 | fhotaccountbillid | 红冲源单id | int8 | 64 |  | √ | 0 | 红冲源单id |
| 39 | fistop | 是否置顶 | bpchar | 1 |  | √ | '0' | 是否置顶 |
| 40 | fusage | 转账附言 | varchar | 255 |  |  | null | 转账附言 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fsourcetype | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: CAS :出纳 AP :应付 AR :应收 ER :费用 BE :银企互联 PM :采购管理 FCA :资金调度 CFM :融资管理 FR :财务报账 IFM :结算中心 OM :产品委外 CIM :投资管理 FS :资金结算 LC :信用证 TM :交易管理 CDM :票据管理 |
| 43 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 44 | finneraccountid | 账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 45 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 46 | fisrefund | 是否退票 | bpchar | 1 |  | √ | '0' | 是否退票 |
| 47 | fpayeename | 收款单位 | varchar | 255 |  | √ | ' ' | 收款单位 |
| 48 | funiformsocialcreditcode | 付款单位统一社会信用代码 | varchar | 100 |  | √ | ' ' | 付款单位统一社会信用代码 |
| 49 | fpayeracctbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 50 | fpayeracctcashid | 付款账号 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 53 | fpayeebanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 54 | flocalamount | 付款金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 付款金额本位币 |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | ffundflowitemid | 资金流量项目 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 57 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 58 | freccity | 收款方市县 | varchar | 80 |  | √ | ' ' | 收款方市县 |
| 59 | fpayeenumber | 收款单位编码（废弃） | varchar | 500 |  | √ | ' ' | 收款单位编码（废弃） |
| 60 | fpayeeid | 收款单位ID（废弃） | int8 | 64 |  | √ | 0 | 收款单位ID（废弃） |
| 61 | frecbanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 62 | fentrance | 新增入口（废弃） | varchar | 10 |  | √ | ' ' | 新增入口（废弃）,枚举: AP :采购付款 ER :付报销款 OTR :其他付款 |
| 63 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 64 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 65 | fsettletnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 66 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 67 | fpaymenttypeid | 付款用途（废弃） | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 68 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 69 | fcurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 70 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  |  | null | 银行返回信息 |
| 71 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pb_dos |  | fbizdate,forgid,fbillstatus |
| 2 | idx_cas_pb_fbilltypeid |  | fbilltypeid |
| 3 | t_cas_paymentbill_pkey |  | fid |
| 4 | idx_cas_pb_fcurrencyid |  | fcurrencyid |
| 5 | idx_cas_pb_obd |  | forgid,fbilltypeid,fbizdate |
| 6 | idx_cas_pb_fbillno |  | fbillno |
| 7 | idx_cas_pb_fopenorgid |  | fopenorgid |
| 8 | idx_cas_pb_fpayeracctbankid |  | fpayeracctbankid |
| 9 | idx_cas_pb_fsourcebilltype |  | fsourcebilltype |
| 10 | idx_cas_pb_fpaydate |  | fpaydate |
| 11 | idx_cas_pb_fsourcebillid |  | fsourcebillid |
| 12 | idx_cas_pb_fpaymenttypeid |  | fpaymenttypeid |

---

## 关联子实体-子表 t_cas_paymentbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_paymentbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_paymentbill_lk_pkey |  | fpkid |
| 2 | idx_cas_pb_lk_fid |  | fid |

---

## 付款明细-子表 t_cas_paymentbillentry

- **表名称：** 付款明细-子表
- **表名：** t_cas_paymentbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | ftaxrate | 税率（%） | numeric | 19 | 6 | √ | 0.000000 | 税率（%） |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fconbillrownum | 合同行号 | varchar | 255 |  | √ | ' ' | 合同行号 |
| 6 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 7 | fscheid | 排程单id | int8 | 64 |  | √ | 0 | 排程单id |
| 8 | factamount | 实付金额 | numeric | 19 | 6 | √ | 0.000000 | 实付金额 |
| 9 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 10 | fcontractnumber | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 11 | frefundamt | 退款金额 | numeric | 19 | 6 | √ | 0.000000 | 退款金额 |
| 12 | fpayableamount | 应付金额 | numeric | 19 | 6 | √ | 0.000000 | 应付金额 |
| 13 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 er_dailyloanbill :借款单 ec_contract :建筑支出合同 conm_salcontract :销售合同 sm_salorder :销售订单 sctm_scpo :委外采购订单 conm_purcontract :采购合同 |
| 14 | funsettledamount | 未核销金额 | numeric | 19 | 6 | √ | 0.000000 | 未核销金额 |
| 15 | ftaxamt | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 16 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 17 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 19 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fdiscountlocamount | 现金折扣结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣结算本位币 |
| 21 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 22 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 23 | fcorebillentryseq | 核心单据行号 | int8 | 64 |  | √ | 0 | 核心单据行号 |
| 24 | fisfreeze | 冻结标识 | bpchar | 1 |  | √ | '0' | 冻结标识 |
| 25 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fexpectvfydate | fexpectvfydate | timestamp | 0 |  |  | null |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fcorebillentryid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 29 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 30 | fconbillentity | 合同实体 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 31 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 32 | frefunddes | 退款说明 | varchar | 255 |  |  | null | 退款说明 |
| 33 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 34 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 35 | fefreezeamt | 冻结金额 | numeric | 19 | 6 | √ | 0.000000 | 冻结金额 |
| 36 | funsettledlocalamt | 未核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 未核销金额结算本位币 |
| 37 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 38 | fexpiredate | fexpiredate | timestamp | 0 |  |  | null |  |
| 39 | funlockamount | 未锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 未锁定金额 |
| 40 | fsettledlocalamt | 已核销金额结算本位币 | numeric | 19 | 6 | √ | 0 | 已核销金额结算本位币 |
| 41 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 42 | flockrefundamt | 关联退款金额 | numeric | 23 | 10 | √ | 0 | 关联退款金额 |
| 43 | flocalamount | 实付金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 实付金额本位币 |
| 44 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 45 | fpayablelocamount | 应付金额结算本位币 | numeric | 19 | 6 | √ | 0.000000 | 应付金额结算本位币 |
| 46 | fdepartmentid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 48 | flockamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 49 | fsettledamount | 已核销金额 | numeric | 19 | 6 | √ | 0.000000 | 已核销金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pbe_fcorebillno |  | fcorebillno |
| 2 | idx_cas_pbe_fpid |  | fid |
| 3 | idx_paymentbill_e_fscheid |  | fscheid |
| 4 | t_cas_paymentbillentry_pkey |  | fentryid |
| 5 | idx_cas_pbe_fsettleorgid |  | fsettleorgid |

---

## 付款单-分表 t_cas_paymentbill_c

- **表名称：** 付款单-分表
- **表名：** t_cas_paymentbill_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontract | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 3 | freportbiztype | 申报业务类型 | varchar | 50 |  | √ | ' ' | 申报业务类型,枚举: X :保税区 E :出口加工区 D :钻石交易所 S :离岸账户 M :深加工结转 O :其他 A :其他特殊经济区 |
| 4 | fpaycountryid | 付款方国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 5 | fapplyname | 申请人姓名 | varchar | 70 |  | √ | ' ' | 申请人姓名 |
| 6 | ftransactioncode | 交易编码 | varchar | 6 |  | √ | ' ' | 交易编码 |
| 7 | fpaymentterm | 收款方式 | bpchar | 1 |  | √ | '0' | 收款方式,枚举: 0 :收款账号 1 :收款人FPS账号 2 :收款人电话 3 :收款方邮箱 |
| 8 | fproxybebank | 代理行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 9 | fpaymentfps | 收款单位FPS账号 | varchar | 30 |  | √ | ' ' | 收款单位FPS账号 |
| 10 | fmobile | 收款单位电话 | varchar | 50 |  | √ | ' ' | 收款单位电话 |
| 11 | fchecktype | 支票类型 | varchar | 30 |  | √ | ' ' | 支票类型,枚举: BCHQ :BCHQ CCHQ :CCHQ CCCH :CCCH DRFT :DRFT ELDR :ELDR |
| 12 | finforpayment | 通知收款单位 | bpchar | 1 |  | √ | '0' | 通知收款单位 |
| 13 | fapplyid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | finvoicenumber | 发票号 | varchar | 95 |  | √ | ' ' | 发票号 |
| 15 | fproxybebankactname | 代理账号名称 | varchar | 255 |  | √ | ' ' | 代理账号名称 |
| 16 | finformrecemail | 通知收款单位邮箱 | varchar | 255 |  | √ | ' ' | 通知收款单位邮箱 |
| 17 | fproxybebanksc | 代理行Swfit Code | varchar | 50 |  | √ | ' ' | 代理行Swfit Code |
| 18 | ftranstypeid | 交易种类 | int8 | 64 |  | √ | 0 | 交易种类 bei_transtype |
| 19 | frecbankaddress | 收款行地址 | varchar | 400 |  | √ | ' ' | 收款行地址 |
| 20 | fauditparam | 清算要求参数 | varchar | 200 |  | √ | ' ' | 清算要求参数 |
| 21 | fsettlementmethod | 清算方式 | varchar | 50 |  | √ | ' ' | 清算方式 |
| 22 | fserlevel | 服务级别 | varchar | 30 |  | √ | ' ' | 服务级别,枚举: URGP :紧急支付 SDVA :当日支付 PRPT :优先支付 NURG :其他 : |
| 23 | fpaymentareacode | 收款单位地区码 | varchar | 3 |  | √ | ' ' | 收款单位地区码 |
| 24 | finstructmsg | 电文指示 | varchar | 30 |  | √ | ' ' | 电文指示,枚举: 1 :单电文 2 :双电文 |
| 25 | frecemail | 收款方邮箱 | varchar | 500 |  | √ | ' ' | 收款方邮箱 |
| 26 | fproxybebankad | 代理行地址 | varchar | 255 |  | √ | ' ' | 代理行地址 |
| 27 | fisbonded | 是否为保税货物项下付款 | bpchar | 1 |  | √ | '0' | 是否为保税货物项下付款 |
| 28 | fpayproxybankid | 付款代理行（作废） | int8 | 64 |  | √ | 0 | 代理行 bei_proxybank |
| 29 | frecroutingnum | 收款行Routing Number | varchar | 100 |  | √ | ' ' | 收款行Routing Number |
| 30 | fproxybebankcountry | 代理行国家地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 31 | fpayeecurrency | 收款账号币别 | int8 | 64 |  | √ | 0 | 收款账号币别 |
| 32 | fcontractno | 兑换合约号 | varchar | 20 |  | √ | ' ' | 兑换合约号 |
| 33 | frecothercode | 收款行其他行号 | varchar | 100 |  | √ | ' ' | 收款行其他行号 |
| 34 | fiscrosspay | 跨境支付 | bpchar | 1 |  | √ | '0' | 跨境支付 |
| 35 | fpaynature | 付款性质 | varchar | 30 |  | √ | ' ' | 付款性质,枚举: 0 :预付货款 1 :货到付款 2 :退款 3 :其他 |
| 36 | frecaddress | 收款方地址 | varchar | 400 |  | √ | ' ' | 收款方地址 |
| 37 | fproxybebankname | 代理行名称 | varchar | 255 |  | √ | ' ' | 代理行名称 |
| 38 | ffeepayer | 手续费承担方 | varchar | 30 |  | √ | ' ' | 手续费承担方,枚举: 01 :付款方 02 :收款方 03 :共同承担 |
| 39 | fproxybebankactno | 代理账号 | varchar | 80 |  | √ | ' ' | 代理账号 |
| 40 | fsendway | 寄送方式 | varchar | 30 |  | √ | ' ' | 寄送方式,枚举: |
| 41 | fcheckuse | 支票用途 | varchar | 30 |  | √ | ' ' | 支票用途,枚举: |
| 42 | fapplyphone | 申请人电话 | varchar | 50 |  | √ | ' ' | 申请人电话 |
| 43 | fpaymethod | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: TRA :TRA TRF :TRF CHK :CHK |
| 44 | fcrosstrantypeid | 交易类型 | int8 | 64 |  | √ | 0 | 银行交易类型 bei_crosstrantype |
| 45 | frecswiftcode | 收款行Swift Code | varchar | 100 |  | √ | ' ' | 收款行Swift Code |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_paymentbill_c_cross |  | fiscrosspay,fcrosstrantypeid |
| 2 | t_cas_paymentbill_c_pkey |  | fid |

---

## 付款单-分表 t_cas_paymentbill_e

- **表名称：** 付款单-分表
- **表名：** t_cas_paymentbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisheadpush | 是否整单下推 | bpchar | 1 |  | √ | '0' | 是否整单下推 |
| 3 | facttradedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 4 | fpayeeacctcash | 收款现金账号 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 5 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 6 | fdpcurrency | 异币别付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | fadjusteprofitloss | 调整损益 | numeric | 23 | 10 | √ | 0 | 调整损益 |
| 8 | fdpexratetableid | 异币别付款汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fispushrefund | 是否直接退款 | bpchar | 1 |  | √ | '0' | 是否直接退款 |
| 10 | fprojectdataid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 11 | fpayeeacctcashid | 收款现金账户ID | int8 | 64 |  | √ | 0 | 收款现金账户ID |
| 12 | fissingleca | 是否加签 | bpchar | 1 |  | √ | '0' | 是否加签 |
| 13 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 15 | ffeeactbank | 手续费账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 16 | fentrustorgid | 委托付款受托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fitempayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | fsourceentry | 源单分录标识 | varchar | 50 |  | √ | ' ' | 源单分录标识 |
| 19 | fitempayeetypeid | 收款单位类型（基础资料类型） | varchar | 30 |  | √ | ' ' | 收款单位类型（基础资料类型）,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 20 | ffeepaydate | 手续费付款日期 | timestamp | 0 |  |  | null | 手续费付款日期 |
| 21 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 22 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 23 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 24 | fmatchdetailtype | 匹配流水方式 | varchar | 64 |  | √ | ' ' | 匹配流水方式,枚举: rule :自动生成 hand :手工生成 automatch :自动匹配 handmatch :手工匹配 claim :认领生成 noclaim :未认领生成 beipay :对账标识码匹配 ecommerce :电商流水合并生成 |
| 25 | fbankcheckflagtag | 对账标识码 | text | 0 |  |  | null | 对账标识码 |
| 26 | frefundbillid | 退收款单ID | int8 | 64 |  | √ | 0 | 退收款单ID |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fdppayquotation | 异币别付款汇率换算方式 | varchar | 30 |  | √ | '0' | 异币别付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 29 | fsinglestream | 手续费独立流水 | bpchar | 1 |  | √ | '0' | 手续费独立流水 |
| 30 | fisperiod | 往来期初 | bpchar | 1 |  | √ | '0' | 往来期初 |
| 31 | ffeepay | 手续费付款 | bpchar | 1 |  | √ | '0' | 手续费付款 |
| 32 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 33 | fhandmttransdetail | 手工匹配关联银行交易明细 | bpchar | 1 |  | √ | '0' | 手工匹配关联银行交易明细 |
| 34 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: cashin :现金存款 cashout :现金取款 |
| 35 | fbankcheckflagtag_tag | 对账标识码_详情 | text | 0 |  |  | null | 对账标识码_详情 |
| 36 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 37 | fispersonpay | 对私支付 | bpchar | 1 |  | √ | '0' | 对私支付 |
| 38 | ffee | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 39 | fdpexchangerate | 异币别付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 异币别付款汇率 |
| 40 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 41 | fismatchtransdetail | 是否匹配流水 | varchar | 16 |  | √ | '0' | 是否匹配流水 |
| 42 | fdpexratedate | 异币别付款汇率日期 | timestamp | 0 |  |  | null | 异币别付款汇率日期 |
| 43 | fdpamt | 异币别付款金额 | numeric | 19 | 6 | √ | 0.000000 | 异币别付款金额 |
| 44 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 45 | ftotalpayamt | 付款金额(含手续费) | numeric | 19 | 6 | √ | 0 | 付款金额(含手续费) |
| 46 | fhotaccount | 红冲标识 | bpchar | 1 |  | √ | '0' | 红冲标识,枚举: 1 :被红冲单 2 :红冲单 |
| 47 | ffeecurrency | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 48 | fapplyorgid | 委托付款委托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | fdplocalamt | 异币别付款金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 异币别付款金额折本位币 |
| 50 | fagreedquotation | 兑换汇率换算方式 | varchar | 30 |  | √ | '0' | 兑换汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 51 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 52 | fbookdate_hw | fbookdate_hw | timestamp | 0 |  |  | null |  |
| 53 | fisdiffcur | 异币别付款 | bpchar | 1 |  | √ | '0' | 异币别付款 |
| 54 | fnetbankacctid | 网银子账户 | int8 | 64 |  | √ | 0 | 网银子账户 bd_netbankacct |
| 55 | finternalacctid | 内部账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 56 | factualpaydate_hw | factualpaydate_hw | timestamp | 0 |  |  | null |  |
| 57 | fpayquotation | 付款汇率换算方式 | varchar | 30 |  | √ | '0' | 付款汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 58 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 59 | fiswaitsche | 待排程 | bpchar | 1 |  | √ | '0' | 待排程 |
| 60 | fconfirmpaydate | 确认付款时间 | timestamp | 0 |  |  | null | 确认付款时间 |
| 61 | fparentacctid | 母账户银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_paymentbill_e_itempayeeid |  | fitempayeeid |
| 2 | idx_paymentbill_e_apporg |  | fapplyorgid |
| 3 | idx_paymentbill_e_fvouchernum |  | fvouchernum |
| 4 | t_cas_paymentbill_e_pkey |  | fid |
| 5 | idx_paymentbill_e_ffeeactbank |  | ffeeactbank |
