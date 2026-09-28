# 本金收回-cim_invest_repaybill

## 关联子实体-子表 t_cfm_repaymentbill_loans_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_repaymentbill_loans_lk

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
| 1 | idx_cfm_repaymentbill_loans_lk_fk |  | fentryid |
| 2 | pk_cfm_repaymentbill_loans_lk |  | fpkid |

---

## 本金收回-多语言表 t_cfm_repaymentbill_l

- **表名称：** 本金收回-多语言表
- **表名：** t_cfm_repaymentbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_repaymentbill_l_pkey |  | fpkid |
| 2 | idx_t_cfm_repaymentbill_l |  | fid,flocaleid |

---

## 本金收回-分表 t_cfm_repaymentbill_e

- **表名称：** 本金收回-分表
- **表名：** t_cfm_repaymentbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flenddraccountid | 借款方借方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 4 | fpayeeacctid | 收款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 5 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: registrying :登记中 waitconfirm :待确认 yetconfirm :已确认 yetreturn :已退回 |
| 6 | fiscycleloan | fiscycleloan | bpchar | 1 |  | √ | '0' |  |
| 7 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 8 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 9 | freturnreason | 退回原因 | varchar | 255 |  | √ | ' ' | 退回原因 |
| 10 | fsettlestatus | 提交结算中心状态 | varchar | 80 |  | √ | ' ' | 提交结算中心状态,枚举: addnew :新增 submit :已提交 accept :已受理 bitback :已退回 |
| 11 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fpayeeaccttext | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 13 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fpayeebanktext | 收款银行 | varchar | 80 |  | √ | ' ' | 收款银行 |
| 15 | floandraccountid | 贷款方借方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 16 | fauto | 自动还款/收回 | bpchar | 1 |  | √ | '0' | 自动还款/收回 |
| 17 | ftextdebtor | 借款人 | varchar | 80 |  | √ | ' ' | 借款人 |
| 18 | frecbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 19 | flendcraccountid | 借款方贷方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 20 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 21 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 22 | fpaybillid | 付款单 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 23 | fpayeetype | 收款人类型 | varchar | 80 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 fbd_other :其他 |
| 24 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 25 | fisratio | 按比例收回 | bpchar | 1 |  | √ | '0' | 按比例收回 |
| 26 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 27 | fpayeeid | 收款人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | fpayamt | fpayamt | numeric | 23 | 10 | √ | 0 |  |
| 29 | fbizdealno | fbizdealno | varchar | 80 |  | √ | ' ' |  |
| 30 | floancraccountid | 贷款方贷方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 31 | floantype | 贷款类型 | varchar | 30 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 32 | ftotalamt | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 33 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 35 | fpayeetext | 收款人 | varchar | 80 |  | √ | ' ' | 收款人 |
| 36 | fconfirmtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 37 | frepayapplyid | 还款申请单 | int8 | 64 |  | √ | 0 | [还款申请 cfm_repayapplybill_f7](../cfm_files/cfm_repayapplybill_f7.md) |
| 38 | floaneracctbankid | 本金收回银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_repaymentbill_e |  | fid |
| 2 | idx_t_cfm_repaymentbill_bns_e |  | fdatasource |

---

## 本金收回-反写记录表 t_cfm_repaymentbill_wb

- **表名称：** 本金收回-反写记录表
- **表名：** t_cfm_repaymentbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_repaymentbill_wb_pkey |  | fentryid |
| 2 | idx_t_cfm_repaymentbill_wb |  | fid |

---

## 本金收回-主表 t_cfm_repaymentbill

- **表名称：** 本金收回-主表
- **表名：** t_cfm_repaymentbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontractbizdate | fcontractbizdate | timestamp | 0 |  |  | null |  |
| 3 | fpaybillno | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单编号 |
| 4 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fnotrepayamount | 未还本金(old) | numeric | 19 | 6 | √ | 0.000000 | 未还本金(old) |
| 6 | famount | 合同收回金额 | numeric | 19 | 6 | √ | 0.000000 | 合同收回金额 |
| 7 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 8 | frenewalexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 9 | factinterest | 实付利息(old) | numeric | 19 | 6 | √ | 0.000000 | 实付利息(old) |
| 10 | fisinit | 初始化 | bpchar | 1 |  | √ | '0' | 初始化 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreditorgid | 债权组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 16 | fexpiredate | fexpiredate | timestamp | 0 |  |  | null |  |
| 17 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 18 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |
| 19 | fdrawamount | 提款金额(old) | numeric | 19 | 6 | √ | 0.000000 | 提款金额(old) |
| 20 | floandate | floandate | timestamp | 0 |  |  | null |  |
| 21 | fbillno | 本金收回编号 | varchar | 80 |  | √ | ' ' | 本金收回编号 |
| 22 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fispayinterest | 付息(old) | bpchar | 1 |  | √ | '0' | 付息(old) |
| 25 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 26 | flendernature | 贷款人性质 | varchar | 30 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | floanbillno | 提款单编号(old) | varchar | 80 |  | √ | ' ' | 提款单编号(old) |
| 30 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 33 | fcontractno | fcontractno | varchar | 80 |  | √ | ' ' |  |
| 34 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 35 | frepaymentway | 本金收回方式 | varchar | 30 |  | √ | ' ' | 本金收回方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 36 | fpredictinterest | 测算利息(old) | numeric | 19 | 6 | √ | 0.000000 | 测算利息(old) |
| 37 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 38 | fbizdate | 收回日期 | timestamp | 0 |  |  | null | 收回日期 |
| 39 | fcontractbillno | fcontractbillno | varchar | 80 |  | √ | ' ' |  |
| 40 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 41 | fstageplanid | 分期本金收回方案 | int8 | 64 |  | √ | 0 | [还款计划方案 cfm_repayagingcheme](../cfm_files/cfm_repayagingcheme.md) |
| 42 | fisvoucher | 是否已生成凭证 | bpchar | 1 |  | √ | '0' | 是否已生成凭证 |
| 43 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | faccountbankid | 还款银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 46 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 47 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 48 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_repaymentbill_bns |  | fbillno,fbillstatus |
| 2 | t_cfm_repaymentbill_pkey |  | fid |
| 3 | idx_t_cfm_repaymentbill_sid |  | fsourcebillid |

---

## 关联子实体-子表 t_cfm_repaymentbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_repaymentbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_repaymentbill_lk |  | fid |
| 2 | t_cfm_repaymentbill_lk_pkey |  | fpkid |

---

## 本金收回-关联追踪表 t_cfm_repaymentbill_tc

- **表名称：** 本金收回-关联追踪表
- **表名：** t_cfm_repaymentbill_tc

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
| 1 | idx_cfm_repaymentbill_tc_tid |  | ftid |
| 2 | idx_t_cfm_repaymentbill_tc |  | ftbillid |
| 3 | t_cfm_repaymentbill_tc_pkey |  | fid |
| 4 | idx_cfm_repaymentbill_tc_tbill |  | ftbillid |

---

## 放款信息-子表 t_cfm_repaymentbill_loans

- **表名称：** 放款信息-子表
- **表名：** t_cfm_repaymentbill_loans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanbillid | 放款单编号 | int8 | 64 |  | √ | 0 | [提款处理单 cfm_loanbill_f7](../cfm_files/cfm_loanbill_f7.md) |
| 3 | fnotrepayamount | 未收回本金 | numeric | 19 | 6 | √ | 0 | 未收回本金 |
| 4 | fintdetail_tag | 利息测算明细_详情 | text | 0 |  |  | null | 利息测算明细_详情 |
| 5 | fdrawamount | 放款金额 | numeric | 19 | 6 | √ | 0 | 放款金额 |
| 6 | fispayinst | 收息 | bpchar | 1 |  | √ | '0' | 收息 |
| 7 | fintdetail | 利息测算明细 | text | 0 |  |  | null | 利息测算明细 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | factintamt | 实收利息 | numeric | 19 | 6 | √ | 0 | 实收利息 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | frepayamount | 收回金额 | numeric | 19 | 6 | √ | 0 | 收回金额 |
| 12 | fcalintamt | 测算利息 | numeric | 19 | 6 | √ | 0 | 测算利息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_repaymentbill_loans |  | fid |
| 2 | pk_t_cfm_repaymentbill_loans |  | fentryid |
