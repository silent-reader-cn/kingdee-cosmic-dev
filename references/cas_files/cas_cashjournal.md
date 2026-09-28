# 现金日记账-cas_cashjournal

## 现金日记账-关联追踪表 t_cas_cashjournal_tc

- **表名称：** 现金日记账-关联追踪表
- **表名：** t_cas_cashjournal_tc

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
| 1 | idx_cas_cashjournal_tc_tbill |  | ftbillid |
| 2 | t_cas_cashjournal_tc_pkey |  | fid |
| 3 | idx_cas_cashjournal_tc_tid |  | ftid |
| 4 | idx_cas_cj_tc_ftbillid |  | ftbillid |

---

## 现金日记账-反写记录表 t_cas_cashjournal_wb

- **表名称：** 现金日记账-反写记录表
- **表名：** t_cas_cashjournal_wb

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
| 1 | t_cas_cashjournal_wb_pkey |  | fid |
| 2 | idx_cas_cj_wb_fsid_fsbillid |  | fsid,fsbillid |

---

## 资金流量项目分录-子表 t_cas_cashjournalentry

- **表名称：** 资金流量项目分录-子表
- **表名：** t_cas_cashjournalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famount_enp | famount_enp | text | 0 |  |  | null |  |
| 3 | faccountcashid | 账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 4 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 5 | flocalamount_enp | flocalamount_enp | text | 0 |  |  | null |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | foppunit | 对方单位 | varchar | 255 |  |  | null | 对方单位 |
| 8 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_cje_fpid |  | fid |
| 2 | t_cas_cashjournalentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_cas_cashjournal_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_cashjournal_lk

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
| 1 | idx_cas_cj_lk_fid |  | fid |
| 2 | t_cas_cashjournal_lk_pkey |  | fpkid |

---

## 现金日记账-主表 t_cas_cashjournal

- **表名称：** 现金日记账-主表
- **表名：** t_cas_cashjournal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpddate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 5 | foppbank | 对方银行 | varchar | 255 |  | √ | ' ' | 对方银行 |
| 6 | fcashacctid | 现金账户 | int8 | 64 |  | √ | 0 | 现金账户 cas_accountcash |
| 7 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :手工新增 2 :单据生成 3 :标准导入 4 :凭证登帐 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ffee | 手续费 | numeric | 19 | 6 | √ | 0 | 手续费 |
| 10 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0.000000 | 汇率 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | favddate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 13 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 14 | fsettlementnumber | 结算号 | varchar | 255 |  |  | null | 结算号 |
| 15 | foppacctnumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 16 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | flocalamount | 折本位币金额 | numeric | 23 | 10 | √ | 0.0000000000 | 折本位币金额 |
| 21 | fsourcebillentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 22 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 23 | fsourcebilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 单据类型,枚举: cas_paybill :付款单 cas_recbill :收款单 cas_agentpaybill :代发单 gl_voucher :凭证 cas_exchangebill :外币兑换单 cas_manualcashjournal :手工日记账 cas_paybill_cash :现金存取 cas_paybill_synonym :同名转账 ifm_deduction :结算中心扣款单 cas_agentreturnbill :代发退款单 |
| 24 | fbatchno | 批次号 | varchar | 80 |  | √ | ' ' | 批次号 |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 28 | fcreditamount | 贷方金额 | numeric | 19 | 6 | √ | 0.000000 | 贷方金额 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fdebitamount | 借方金额 | numeric | 19 | 6 | √ | 0.000000 | 借方金额 |
| 31 | fpreparationdate | 制单日期 | timestamp | 0 |  |  | null | 制单日期 |
| 32 | frelatedbizdate | 关联业务日期 | timestamp | 0 |  |  | null | 关联业务日期 |
| 33 | fsourcebillnumber | 单据号 | varchar | 80 |  | √ | ' ' | 单据号 |
| 34 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | ffeepayer | 手续费承担方 | varchar | 30 |  | √ | ' ' | 手续费承担方,枚举: 01 :付款方承担 02 :收款方承担 03 :共同承担 |
| 37 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 38 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 39 | ftracedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 40 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 41 | fdirection | 方向 | varchar | 30 |  | √ | ' ' | 方向,枚举: 1 :借 2 :贷 3 :平 |
| 42 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fticketnumber | 核销票据号 | varchar | 80 |  | √ | ' ' | 核销票据号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_cashjournal_pkey |  | fid |
| 2 | idx_cas_cj_orgacc |  | forgid,fcashacctid,fcurrencyid,fbookdate |
| 3 | idx_cas_cj_sourceid |  | fsourcebillid |
