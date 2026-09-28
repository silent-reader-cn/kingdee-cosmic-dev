# 代发退款单-cas_agentreturnbill

## 代发退款单-反写记录表 t_cas_agentreturnbill_wb

- **表名称：** 代发退款单-反写记录表
- **表名：** t_cas_agentreturnbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_agentreturnbill_wb |  | fentryid |

---

## 单据体-子表 t_cas_agentreturnentry

- **表名称：** 单据体-子表
- **表名：** t_cas_agentreturnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankcheckflag | 对账标识码 | varchar | 2000 |  | √ | ' ' | 对账标识码 |
| 3 | fsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpayeebankid | fpayeebankid | int8 | 64 |  | √ | 0 |  |
| 6 | famount | 加密金额 | varchar | 100 |  | √ | ' ' | 加密金额 |
| 7 | fmonproject | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 8 | fmatchresult | 是否已匹配 | varchar | 16 |  | √ | '0' | 是否已匹配 |
| 9 | fpayeename | 付款账户名称 | varchar | 255 |  | √ | ' ' | 付款账户名称 |
| 10 | fpayeeacctbank | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 11 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | flocalamount | 加密本位币 | varchar | 100 |  | √ | ' ' | 加密本位币 |
| 13 | fpayeebanknumber | 付款账户联行号 | varchar | 80 |  | √ | ' ' | 付款账户联行号 |
| 14 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 15 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 16 | fpayeebankname | 付款银行开户行 | varchar | 255 |  | √ | ' ' | 付款银行开户行 |
| 17 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 18 | fpayeeid | 付款单位 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 21 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 22 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 23 | fplainlocalamount | 折本位币 | numeric | 19 | 6 | √ | 0 | 折本位币 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fplainamount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_agentreturnentry_pid |  | fpayeeid |
| 2 | pk_cas_agentreturnentry |  | fentryid |
| 3 | idx_agentreturnentry_fid |  | fid |

---

## 代发退款单-关联追踪表 t_cas_agentreturnbill_tc

- **表名称：** 代发退款单-关联追踪表
- **表名：** t_cas_agentreturnbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_cas_agentreturnbill_tc_tbill |  | ftbillid |
| 2 | pk_agentreturnbill_tc |  | fid |
| 3 | idx_cas_agentreturnbill_tc_tid |  | ftid |

---

## 代发退款单-主表 t_cas_agentreturnbill

- **表名称：** 代发退款单-主表
- **表名：** t_cas_agentreturnbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsettlettype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 3 | faccountcashid | 现金账户 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |
| 4 | facttradedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 5 | fisagencypersonpay | 并笔入账 | bpchar | 1 |  | √ | '0' | 并笔入账 |
| 6 | fbankcheckflag | 对账标识码 | varchar | 2000 |  | √ | ' ' | 对账标识码 |
| 7 | forgid | 收款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbusinesstype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 9 | fpayamount | 收款金额 | numeric | 19 | 6 | √ | 0 | 收款金额 |
| 10 | fsource | 单据来源 | varchar | 30 |  | √ | ' ' | 单据来源,枚举: new :手工新增 impot :导入 BOTP :BOTP |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fexchangerate | 收款汇率 | numeric | 23 | 10 | √ | 0 | 收款汇率 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fismatchtransdetail | 是否匹配流水 | varchar | 16 |  | √ | '0' | 是否匹配流水 |
| 15 | fmatchresult | 是否已匹配 | varchar | 16 |  | √ | '0' | 是否已匹配 |
| 16 | fpaytime | 确认收款时间 | timestamp | 0 |  |  | null | 确认收款时间 |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 18 | fcount | 总笔数 | int4 | 32 |  | √ | 0 | 总笔数 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fcashierid | 确认收款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fpayeracctbankid | 收款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | ffundflowitem | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 24 | fpayerbankid | 收款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 25 | flocalamount | 收款金额本位币 | numeric | 19 | 6 | √ | 0 | 收款金额本位币 |
| 26 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: cas_agentpaybill :代发处理 |
| 27 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已收款 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fvouchernum | fvouchernum | varchar | 255 |  | √ | ' ' |  |
| 30 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 34 | fmatchdetailtype | 匹配流水方式 | varchar | 64 |  | √ | ' ' | 匹配流水方式,枚举: automatch :自动匹配 handmatch :手工匹配 |
| 35 | fsettletnumber | 结算号 | varchar | 255 |  | √ | ' ' | 结算号 |
| 36 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fpayquotation | 汇率换算方式 | bpchar | 1 |  | √ | '0' | 汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 38 | fpaymenttypeid | 原付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 39 | fpayeetypelist | 付款单位类型 | varchar | 80 |  | √ | ' ' | 付款单位类型,枚举: bos_user :人员 bos_org :公司 bd_supplier :供应商 bd_customer :客户 cas_othercontactunit :其他往来单位 |
| 40 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 41 | fbankcheckflagtag | 对账标识码tag | varchar | 2000 |  | √ | ' ' | 对账标识码tag |
| 42 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 43 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 44 | fismatchbyhead | 是否已按单头匹配 | varchar | 16 |  | √ | '0' | 是否已按单头匹配 |
| 45 | fcurrencyid | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_agentreturnbill_org |  | forgid |
| 2 | idx_agentreturnbill_date |  | fbizdate |
| 3 | pk_cas_agentreturnbill |  | fid |
| 4 | idx_agentreturnbill_no |  | fbillno |

---

## 关联子实体-子表 t_cas_agentreturnbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_agentreturnbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_agentreturnbill_lk |  | fpkid |

---

## 关联子实体-子表 t_cas_agentreturnentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_agentreturnentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fplainamount_old | 金额_原始携带值 | numeric | 19 | 6 | √ | 0 | 金额_原始携带值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fplainamount | 金额_确认携带值 | numeric | 19 | 6 | √ | 0 | 金额_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_agentreturnentry_lk |  | fpkid |
