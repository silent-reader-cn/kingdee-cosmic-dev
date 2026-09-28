# 调拨申请-cas_transferapply

## 调拨申请-主表 t_cas_transferapplybill

- **表名称：** 调拨申请-主表
- **表名：** t_cas_transferapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplycause | 申请事由 | varchar | 512 |  | √ | ' ' | 申请事由 |
| 3 | fpaycurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 6 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 7 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fpayeeamout | 收款总额 | numeric | 19 | 6 | √ | 0 | 收款总额 |
| 9 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 10 | fpartpay | 部分付款 | bpchar | 1 |  | √ | '0' | 部分付款 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fpaidstatus | 付款状态 | varchar | 5 |  | √ | ' ' | 付款状态,枚举: A :未付款 B :付款中 C :已付款 |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fpayamout | 付款总额 | numeric | 19 | 6 | √ | 0 | 付款总额 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbackbillflag | 退单 | bpchar | 1 |  | √ | '0' | 退单 |
| 20 | fisdiffcur | 异币别付款 | bpchar | 1 |  | √ | '0' | 异币别付款 |
| 21 | fmodifyerid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | ftransfertype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :跨主体调拨 B :同名转账 |
| 23 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 24 | fpayeecurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | finvalidflag | 作废 | bpchar | 1 |  | √ | '0' | 作废 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_trab_fbillno |  | fbillno |
| 2 | pk_t_cas_transferapplybill |  | fid |

---

## 申请明细分录-子表 t_cas_transferapply_entry

- **表名称：** 申请明细分录-子表
- **表名：** t_cas_transferapply_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 3 | fepayee | fepayee | int8 | 64 |  | √ | 0 |  |
| 4 | fpaymentchannel | 支付渠道 | varchar | 50 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 onlinebank :网上银行 counter :柜台 |
| 5 | fpriority | 紧急程度 | varchar | 25 |  | √ | ' ' | 紧急程度,枚举: prior :优先 public :普通 defer :暂缓 |
| 6 | fpaybillno | 调拨单 | varchar | 50 |  | √ | ' ' | 调拨单 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryexrate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fentryexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 10 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 11 | fpaystatus | 付款状态 | varchar | 25 |  | √ | ' ' | 付款状态,枚举: C :未付款 B :付款中 A :已付款 E :已退单 |
| 12 | fstatusexplain | 状态说明 | varchar | 255 |  | √ | ' ' | 状态说明 |
| 13 | feuseraccbank | 收款信息基础资料(隐藏) | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 14 | fentrypaycurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fepayeeaccbankid | 收款账号ID | int8 | 64 |  | √ | 0 | 收款账号ID |
| 16 | flastmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 17 | fepayeeaccbanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 18 | fpayeraccbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 19 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 20 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fbackbill | 退票 | bpchar | 1 |  | √ | '0' | 退票 |
| 22 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 23 | fstandardmoneyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fepayeeamount | 收款金额 | numeric | 19 | 6 | √ | 0 | 收款金额 |
| 25 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 26 | frecroutingnum | 调入银行Rounting Number | varchar | 255 |  | √ | ' ' | 调入银行Rounting Number |
| 27 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fepayeetype | 收款人类型 | varchar | 100 |  | √ | ' ' | 收款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 other :其他 cas_othercontactunit :其他往来单位 |
| 29 | feaccountname | 收款账户简称 | varchar | 255 |  | √ | ' ' | 收款账户简称 |
| 30 | frecothercode | 调入银行其他代码 | varchar | 255 |  | √ | ' ' | 调入银行其他代码 |
| 31 | frecbanknumber | 收款银行联行号 | varchar | 50 |  | √ | ' ' | 收款银行联行号 |
| 32 | feacctshort | 付款账户简称 | varchar | 255 |  | √ | ' ' | 付款账户简称 |
| 33 | fdsmoney | 折本位币 | numeric | 19 | 6 | √ | 0 | 折本位币 |
| 34 | fsettletnumber | 结算号 | varchar | 255 |  | √ | ' ' | 结算号 |
| 35 | fepayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 36 | fbalance | 当前余额 | numeric | 19 | 6 | √ | 0 | 当前余额 |
| 37 | fepayeeid | 收款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fentryquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fpaymentmoney | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 40 | flockedamt | 已锁定金额 | numeric | 19 | 6 | √ | 0 | 已锁定金额 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fepayeename | fepayeename | varchar | 255 |  | √ | ' ' |  |
| 43 | fepayeeaccbank | 收款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 44 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 45 | frecswiftcode | 调入银行Swift Code | varchar | 255 |  | √ | ' ' | 调入银行Swift Code |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_cas_transfer_entry |  | fid |
| 2 | pk_t_cas_transferapply_entry |  | fentryid |

---

## 单据体-子表 t_cas_claimbankcheckflag

- **表名称：** 单据体-子表
- **表名：** t_cas_claimbankcheckflag

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
| 1 | idx_cas_claimbc_fid |  | fid |
| 2 | pk_t_cas_claimbankcheckflag |  | fentryid |
| 3 | idx_cas_claimbankcheckflag |  | febankcheckflag |
