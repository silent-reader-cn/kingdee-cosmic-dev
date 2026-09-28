# 收款结算单-ifm_transrecvbill

## 收款结算单-反写记录表 t_ifm_transrecvbill_wb

- **表名称：** 收款结算单-反写记录表
- **表名：** t_ifm_transrecvbill_wb

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
| 1 | idx_ifm_transrecvbill_wb_fk |  | fid |
| 2 | pk_ifm_transrecvbill_wb |  | fentryid |

---

## 收款结算单-主表 t_ifm_receitptbill

- **表名称：** 收款结算单-主表
- **表名：** t_ifm_receitptbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayerbanknum | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 3 | fitempayerid | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fagentfinorgid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 5 | funclaimamt | 待分配金额 | numeric | 23 | 10 | √ | 0 | 待分配金额 |
| 6 | fitempayertypeid | 付款单位类型 | varchar | 100 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 7 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 8 | forg | 资金组织(没有使用) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 收款汇率 | numeric | 23 | 10 | √ | 0.00 | 收款汇率 |
| 11 | fpayername | 付款单位 | varchar | 255 |  | √ | ' ' | 付款单位 |
| 12 | fagentpayeeaccountid | 收款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 13 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpayeracctbank | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 16 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 20 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: ifm_payacceptancebill :内部结算受理 fca_transdownbill :下拨单 ifm_deduction :结算中心扣款 ifm_interestbill :贷款结息单 ifm_repaymentbill :贷款收回单 scf_finrepaybill :供应链融资还款处理 ifm_notice_release :内部通知存款解活处理 ifm_release :内部定期存款解活处理 ifm_notice_deposit :内部通知存款 ifm_deposit :内部定期存款 cas_recbill :收款单 |
| 21 | fagentfinorgcatid | 银行类别 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fbackuser | 退单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 26 | freceiptstatus | 收款状态 | varchar | 50 |  | √ | ' ' | 收款状态,枚举: A :待收款 B :收款处理中 C :已退单 D :已收款 |
| 27 | fsumrecamt | 明细收款金额汇总 | numeric | 23 | 10 | √ | 0 | 明细收款金额汇总 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 30 | fscorgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fbackreason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 32 | fisdiffcur | 异币别付款 | bpchar | 1 |  | √ | '0' | 异币别付款 |
| 33 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 34 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | flocalamt | 收款金额本位币 | numeric | 23 | 10 | √ | 0.00 | 收款金额本位币 |
| 36 | ftranstype | 交易类型 | varchar | 50 |  | √ | ' ' | 交易类型,枚举: 1 :内部代付 2 :内部转账 3 :资金下拨 6 :内部扣款 7 :贷款收回 8 :贷款结息 10 :银行扣款 11 :活转定 12 :定转活 13 :供应链融资还款 14 :内部代收 |
| 37 | fsettletnumber | 结算号 | varchar | 200 |  | √ | ' ' | 结算号 |
| 38 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 39 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 40 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 41 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 42 | freceiptamt | 收款金额 | numeric | 23 | 10 | √ | 0.00 | 收款金额 |
| 43 | fcurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_receitptbill |  | fid |
| 2 | idx_ifm_receitptbill_billno |  | fbillno |

---

## 关联子实体-子表 t_ifm_transrecvbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_transrecvbill_lk

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
| 1 | pk_ifm_transrecvbill_lk |  | fpkid |
| 2 | idx_ifm_transrecvbill_lk_fk |  | fid |

---

## 收款结算单-关联追踪表 t_ifm_transrecvbill_tc

- **表名称：** 收款结算单-关联追踪表
- **表名：** t_ifm_transrecvbill_tc

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
| 1 | pk_ifm_transrecvbill_tc |  | fid |
| 2 | idx_ifm_transrecvbill_tc_tid |  | ftid |
| 3 | idx_ifm_transrecvbill_tc_tbill |  | ftbillid |

---

## 单据体-子表 t_ifm_receitptbillentry

- **表名称：** 单据体-子表
- **表名：** t_ifm_receitptbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fpushrecamt | 已下推收款单金额 | numeric | 23 | 10 | √ | 0.00 | 已下推收款单金额 |
| 4 | fcontactunittype | 往来单位类型 | varchar | 36 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 5 | fsetquotation | 结算汇率换算方式 | varchar | 30 |  | √ | ' ' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 6 | ffundallocid | 代收资金分配单id | int8 | 64 |  | √ | 0 | 代收资金分配单id |
| 7 | freceivablelocalamt | 收款金额本位币 | numeric | 23 | 10 | √ | 0 | 收款金额本位币 |
| 8 | fconfirmstatus | 收款单确认状态 | varchar | 50 |  | √ | ' ' | 收款单确认状态,枚举: 0 :待确认 1 :已确认 2 : |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | ffundallocno | 代收资金分配单号 | varchar | 100 |  | √ | ' ' | 代收资金分配单号 |
| 11 | freceivableamt | 收款金额 | numeric | 23 | 10 | √ | 0.00 | 收款金额 |
| 12 | finnerpayeeaccount | 内部账户 | int8 | 64 |  | √ | 0 | 内部账户管理 ifm_inneracct |
| 13 | fpayeebank | 内部账户开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 14 | fsettlecur | 内部账户币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0 | 结算汇率 |
| 16 | fmemberorgid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 18 | fdatasource | 数据来源 | varchar | 36 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :手工分配 2 :下推生成 |
| 19 | frecbilltypeid | 收款单类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fsettleamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 22 | frecbillid | 收款单编号 | int8 | 64 |  | √ | 0 | 收款单 cas_recbill |
| 23 | fpayeeaccount | 收款账户（银行） | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 24 | fsettlementlocalamt | 结算金额本位币 | numeric | 23 | 10 | √ | 0 | 结算金额本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_receitptbillentry_fk |  | fid |
| 2 | pk_ifm_receitptbillentry |  | fentryid |

---

## 收款结算单-分表 t_ifm_receitptbill_e

- **表名称：** 收款结算单-分表
- **表名：** t_ifm_receitptbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankcheckflag | 对账标识码 | varchar | 1024 |  | √ | ' ' | 对账标识码 |
| 3 | frecvdate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 4 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 5 | ftoallocatedtlocalamt | 待分配金额本位币 | numeric | 23 | 10 | √ | 0 | 待分配金额本位币 |
| 6 | freceiptamtlocalamt | 收款金额汇总本位币 | numeric | 23 | 10 | √ | 0 | 收款金额汇总本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_receitptbill_e |  | fid |
| 2 | idx_ifm_receitptbill_e_rdate |  | frecvdate |
