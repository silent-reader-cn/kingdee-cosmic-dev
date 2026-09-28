# 支付信息变更单-cas_paychgbill

## 关联子实体-子表 t_cas_paychgbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_paychgbillentry_lk

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
| 1 | idx_cas_paychgbillentry_lk_fk |  | fentryid |
| 2 | pk_cas_paychgbillentry_lk |  | fpkid |

---

## 支付信息变更单-关联追踪表 t_cas_paychgbill_tc

- **表名称：** 支付信息变更单-关联追踪表
- **表名：** t_cas_paychgbill_tc

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
| 1 | pk_cas_paychgbill_tc |  | fid |
| 2 | idx_cas_paychgbill_tc_tid |  | ftid |
| 3 | idx_cas_paychgbill_tc_tbill |  | ftbillid |

---

## 支付信息变更单-反写记录表 t_cas_paychgbill_wb

- **表名称：** 支付信息变更单-反写记录表
- **表名：** t_cas_paychgbill_wb

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
| 1 | idx_cas_paychgbill_wb_fk |  | fid |
| 2 | pk_cas_paychgbill_wb |  | fentryid |

---

## 变更详情-子表 t_cas_paychgbillentry

- **表名称：** 变更详情-子表
- **表名：** t_cas_paychgbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faftersettletypeid | 变更后结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 3 | fsourceentryid | 源单分录id(隐藏) | int8 | 64 |  | √ | 0 | 源单分录id(隐藏) |
| 4 | fchgpayeeaccbankid | 变更后收款账号id | int8 | 64 |  | √ | 0 | 变更后收款账号id |
| 5 | frecerid | 收款人id(隐藏) | int8 | 64 |  | √ | 0 | 收款人id(隐藏) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fafterrecerbankid | 变更后收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 8 | factpayamt | 实付金额 | numeric | 19 | 6 | √ | 0.000000 | 实付金额 |
| 9 | frecername | 收款人实名 | varchar | 255 |  | √ | ' ' | 收款人实名 |
| 10 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 11 | frecacctbank | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 12 | fpayeeamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 13 | frecer | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 14 | fafterrecername | 变更后收款人实名 | varchar | 255 |  | √ | ' ' | 变更后收款人实名 |
| 15 | fafterrecacctbankid | fafterrecacctbankid | int8 | 64 |  | √ | 0 |  |
| 16 | fisaftercombinerecord | 变更后是否并笔入账 | bpchar | 1 |  | √ | '0' | 变更后是否并笔入账 |
| 17 | fafterrecerbankname | 变更后收款银行 | varchar | 255 |  | √ | ' ' | 变更后收款银行 |
| 18 | faftersettletnumber | 变更后结算号 | varchar | 100 |  | √ | ' ' | 变更后结算号 |
| 19 | frecerbankid | 收款银行(基础资料) | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 20 | fiscombinerecord | 是否并笔入账 | bpchar | 1 |  | √ | '0' | 是否并笔入账 |
| 21 | fafterpayeracctbankid | 变更后付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 22 | fpayeracctbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 23 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 24 | fafterpaychannel | 变更后支付渠道 | varchar | 40 |  | √ | ' ' | 变更后支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 25 | fpayeebankname | 收款银行 | varchar | 100 |  | √ | ' ' | 收款银行 |
| 26 | fafterusage | 变更后转账附言 | varchar | 255 |  | √ | ' ' | 变更后转账附言 |
| 27 | fpaychannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 28 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 other :其他 cas_othercontactunit :其他往来单位 |
| 29 | fchguseraccbank | 变更收款信息基础资料(隐藏) | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 30 | fafterbizdate | 变更后业务日期 | timestamp | 0 |  |  | null | 变更后业务日期 |
| 31 | fchgaccountname | 变更后账户名称 | varchar | 255 |  | √ | ' ' | 变更后账户名称 |
| 32 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 33 | fsettletnumber | 结算号 | varchar | 100 |  | √ | ' ' | 结算号 |
| 34 | fchgpayeeaccbank | 变更收款账号基础资料(隐藏) | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | flinenumber | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fchangerecacctbank | 变更后收款账号 | varchar | 100 |  | √ | ' ' | 变更后收款账号 |
| 39 | fafterpayerbankid | 变更后付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pcbe_fpid |  | fid |
| 2 | t_cas_paychgbillentry_pkey |  | fentryid |

---

## 支付信息变更单-主表 t_cas_paychgbill

- **表名称：** 支付信息变更单-主表
- **表名：** t_cas_paychgbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fiscashconfirm | 是否已出纳确认 | bpchar | 1 |  | √ | '0' | 是否已出纳确认 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fapplyuserid | 变更申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbillscode | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 8 | fsourcetype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: cas_paybill :付款单 cas_agentpaybill :代发单 cas_payapplybill :付款申请单 |
| 9 | fsbilltype | 源单据类型 | varchar | 50 |  | √ | ' ' | 源单据类型,枚举: payapply :付款申请 expenses :报销支付 wage_payment :工资支付 cashaccess :现金存取 other_settlement :其他付款(参与结算) other :其他付款 purchase :采购付款 span :跨主体调拨 transfer_same :同名转账 |
| 10 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 11 | fbillno | 变更单号 | varchar | 80 |  | √ | ' ' | 变更单号 |
| 12 | fremark | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsourcebilltype | 源单类型标识 | varchar | 30 |  | √ | ' ' | 源单类型标识,枚举: cas_paybill :付款单 |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsourcecurrencyid | 源单币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fchgtype | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: paychg :付款信息变更 recchg :收款信息变更 |
| 20 | falterationuser | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbillname | 关联单据名称 | varchar | 50 |  | √ | ' ' | 关联单据名称 |
| 22 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 23 | fchgdate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fchangerecacctbank | fchangerecacctbank | varchar | 100 |  | √ | ' ' |  |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pcb_fbillno |  | fbillno |
| 2 | t_cas_paychgbill_pkey |  | fid |

---

## 关联子实体-子表 t_cas_paychgbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_paychgbill_lk

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
| 1 | pk_cas_paychgbill_lk |  | fpkid |
| 2 | idx_cas_paychgbill_lk_fk |  | fid |
