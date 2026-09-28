# 银行日记账-cas_bankjournal

## 资金用途分录-子表 t_cas_bankjournalentry

- **表名称：** 资金用途分录-子表
- **表名：** t_cas_bankjournalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famount_enp | famount_enp | text | 0 |  |  | null |  |
| 3 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 4 | flocalamount_enp | flocalamount_enp | text | 0 |  |  | null |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | foppunit | 对方单位 | varchar | 255 |  |  | null | 对方单位 |
| 7 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | faccountbankid | 账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bje_faccountbankid |  | faccountbankid |
| 2 | t_cas_bankjournalentry_pkey |  | fentryid |
| 3 | idx_cas_bje_fpid |  | fid |

---

## 银行日记账-分表 t_cas_bankjournal_e

- **表名称：** 银行日记账-分表
- **表名：** t_cas_bankjournal_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisinternal | 是否内部客商 | bpchar | 1 |  | √ | '0' | 是否内部客商 |
| 3 | fisattention | 是否关注交易 | bpchar | 1 |  | √ | '0' | 是否关注交易 |
| 4 | fisdoubt | 是否可疑交易 | bpchar | 1 |  | √ | '0' | 是否可疑交易 |
| 5 | fissensitive | 是否敏感交易 | bpchar | 1 |  | √ | '0' | 是否敏感交易 |
| 6 | frecpaytypeid | 类型ID | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 7 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 8 | fislargeamount | 是否大额交易 | bpchar | 1 |  | √ | '0' | 是否大额交易 |
| 9 | frecpayertype | 收付款人类型 | varchar | 30 |  | √ | ' ' | 收付款人类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 10 | frecpayer | 收付款人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | frecpaytype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: cas_receivingbilltype :收款用途 cas_paymentbilltype :付款用途 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_bankjournal_e |  | fid |

---

## 银行日记账-主表 t_cas_bankjournal

- **表名称：** 银行日记账-主表
- **表名：** t_cas_bankjournal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpddate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 4 | fbankcheckflag | 对账标识码(旧) | varchar | 1024 |  | √ | ' ' | 对账标识码(旧) |
| 5 | forgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0.000000 | 汇率 |
| 9 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 10 | fsettlementnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 11 | foppacctnumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fsourcebillentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 15 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 16 | fsourcebilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: cas_paybill :付款单 cas_recbill :收款单 cas_agentpaybill :代发单 gl_voucher :凭证 cas_exchangebill :外币兑换单 fca_transupbill :上划单 fca_transdownbill :下拨单 cdm_drafttradebill :业务处理单 ifm_transhandlebill :付款结算单 ifm_rectransbill :收款交易处理单 cas_manualbankjournal :手工日记账 cas_paybill_cash :现金存取 cas_paybill_synonym :同名转账 ifm_deduction :结算中心扣款单 bei_transdetail :交易明细 ifm_inneraccountinit :内部账户期初 ifm_transrecvbill :收款结算单 cas_agentreturnbill :代发退款单 ifm_linkpaybill :联动支付单 |
| 17 | fbatchno | 批次号 | varchar | 1024 |  | √ | ' ' | 批次号 |
| 18 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 20 | fcreditamount | 贷方金额 | numeric | 19 | 6 | √ | 0.000000 | 贷方金额 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdebitamount | 借方金额 | numeric | 19 | 6 | √ | 0.000000 | 借方金额 |
| 23 | fpreparationdate | 制单日期 | timestamp | 0 |  |  | null | 制单日期 |
| 24 | ftracedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 25 | fbankcheckflagtag | 对账标识码 | text | 0 |  |  | null | 对账标识码 |
| 26 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 receiptgen :电子回单生成 fromifm :结算中心 |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fdirection | 方向 | varchar | 30 |  | √ | ' ' | 方向,枚举: 1 :借 2 :贷 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fticketnumber | 核销票据号 | varchar | 80 |  | √ | ' ' | 核销票据号 |
| 31 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 32 | fbankcheckflagtag_tag | 对账标识码_详情 | text | 0 |  |  | null | 对账标识码_详情 |
| 33 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :手工录入 2 :单据生成 3 :标准导入 4 :凭证登账 5 :交易明细生成 |
| 34 | fbillinfo | fbillinfo | varchar | 255 |  |  | null |  |
| 35 | ffee | 手续费 | numeric | 19 | 6 | √ | 0 | 手续费 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fsynccheck | 是否同步 | bpchar | 1 |  | √ | '0' | 是否同步 |
| 38 | favddate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 39 | fsettleinfo | fsettleinfo | varchar | 255 |  |  | null |  |
| 40 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 41 | fbankacctid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 44 | fcreatetime | 系统日期 | timestamp | 0 |  |  | null | 系统日期 |
| 45 | fvouchertypeid | fvouchertypeid | int8 | 64 |  | √ | 0 |  |
| 46 | frelatedbizdate | 关联业务日期 | timestamp | 0 |  |  | null | 关联业务日期 |
| 47 | fsourcebillnumber | 单据号 | varchar | 255 |  | √ | ' ' | 单据号 |
| 48 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 49 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 50 | ffeepayer | 手续费承担方 | varchar | 30 |  | √ | ' ' | 手续费承担方,枚举: 01 :付款方 02 :收款方 03 :共同承担 |
| 51 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 52 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 53 | fischeck | 是否勾对 | bpchar | 1 |  | √ | '0' | 是否勾对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bj_clu |  | fbizdate,fbankcheckflag,fsettlementnumber,fcreditamount,fdebitamount |
| 2 | idx_cas_bj_fsourcebillnumber |  | fsourcebillnumber |
| 3 | idx_cas_bj_bcc |  | fbankacctid,fcurrencyid,fbizdate |
| 4 | idx_cas_bj_fperiodid |  | fperiodid |
| 5 | idx_cas_bj_bizdate |  | forgid,fbankacctid,fcurrencyid,fbizdate |
| 6 | idx_cas_bj_sourceid |  | fsourcebillid |
| 7 | t_cas_bankjournal_pkey |  | fid |

---

## 银行日记账-关联追踪表 t_cas_bankjournal_tc

- **表名称：** 银行日记账-关联追踪表
- **表名：** t_cas_bankjournal_tc

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
| 1 | t_cas_bankjournal_tc_pkey |  | fid |
| 2 | idx_cas_bankjournal_tc_tbill |  | ftbillid |
| 3 | idx_cas_bj_tc_ftbillid |  | ftbillid |
| 4 | idx_cas_bankjournal_tc_tid |  | ftid |

---

## 银行日记账-反写记录表 t_cas_bankjournal_wb

- **表名称：** 银行日记账-反写记录表
- **表名：** t_cas_bankjournal_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  |  | null |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  |  | null |  |
| 9 | fentryid | fentryid | int8 | 64 |  |  | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_bankjournal_wb_pkey |  | fid |
| 2 | idx_cas_bj_wb_fsid_fsbillid |  | fsid,fsbillid |

---

## 单据体-子表 t_cas_journalbankcheck

- **表名称：** 单据体-子表
- **表名：** t_cas_journalbankcheck

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
| 1 | pk_t_cas_journalbankcheck |  | fentryid |
| 2 | idx_cas_bjbc_fid |  | fid |
| 3 | idx_cas_journalbankck |  | febankcheckflag |

---

## 关联子实体-子表 t_cas_bankjournal_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_bankjournal_lk

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
| 1 | t_cas_bankjournal_lk_pkey |  | fpkid |
| 2 | idx_cas_bj_lk_fid |  | fid |
