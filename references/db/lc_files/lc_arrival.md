# 到单处理-lc_arrival

## 单据体-子表 t_lc_arrival_entry

- **表名称：** 单据体-子表
- **表名：** t_lc_arrival_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpayremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 3 | fpayno | 付款单编号 | varchar | 50 |  | √ | ' ' | 付款单编号 |
| 4 | fpaycurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | freturnamount | 退金额 | numeric | 19 | 6 | √ | 0 | 退金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 8 | frealpaydate | 实际付款日期 | timestamp | 0 |  |  | null | 实际付款日期 |
| 9 | farrpaycurrencyid | 到单付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fisdiffcur | 异币种付款 | bpchar | 1 |  | √ | '0' | 异币种付款 |
| 11 | fexchangerate | 兑换汇率 | numeric | 23 | 10 | √ | 0 | 兑换汇率 |
| 12 | foperatetype | 业务操作类型 | varchar | 50 |  | √ | ' ' | 业务操作类型,枚举: payment :付款 refund :退款 renote :退票 chargeback :退单 |
| 13 | farrpayamount | 到单付款金额 | numeric | 19 | 6 | √ | 0 | 到单付款金额 |
| 14 | fpayid | 付款单主键ID | int8 | 64 |  | √ | 0 | 付款单主键ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_arrival_entry |  | fentryid |
| 2 | idx_lc_arrival_entry |  | fid |

---

## 到单处理-主表 t_lc_arrival

- **表名称：** 到单处理-主表
- **表名：** t_lc_arrival

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facceptreturnmsg | 承兑银行返回信息 | varchar | 255 |  | √ | ' ' | 承兑银行返回信息 |
| 3 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 5 | flettercreditid | 信用证号 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 6 | fconfigtime | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 7 | fexceedreson | 到单金额超出原因 | varchar | 255 |  | √ | ' ' | 到单金额超出原因 |
| 8 | famount | 信用证金额 | numeric | 19 | 6 | √ | 0 | 信用证金额 |
| 9 | farrivaltype | 到单类型 | varchar | 50 |  | √ | ' ' | 到单类型,枚举: credit :信用证 da :DA到单 dp :DP到单 |
| 10 | fdoneamount | 已付金额 | numeric | 19 | 6 | √ | 0 | 已付金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | frecorddate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 13 | ftodoamount | 未付金额 | numeric | 19 | 6 | √ | 0 | 未付金额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbenefiterother | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 16 | fisfinancapply | 关联融资申请 | bpchar | 1 |  | √ | '0' | 关联融资申请 |
| 17 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 18 | frejectinfo | 拒付处理意见 | varchar | 255 |  | √ | ' ' | 拒付处理意见 |
| 19 | ffrombankname | 来单银行名称 | varchar | 255 |  | √ | ' ' | 来单银行名称 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fpayremark | fpayremark | varchar | 255 |  | √ | ' ' |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fispayment | 存在关联付款单 | bpchar | 1 |  | √ | '0' | 存在关联付款单 |
| 25 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 26 | ffinancamount | 融资金额 | numeric | 23 | 10 | √ | 0 | 融资金额 |
| 27 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fpushcount | 下推次数 | int8 | 64 |  | √ | 0 | 下推次数 |
| 31 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | farrivalstatus | 到单状态 | varchar | 50 |  | √ | ' ' | 到单状态,枚举: arrival_register :到单已登记 arrival_confirm :到单已确认 arrival_pay :到单已付款 |
| 33 | fislinkcfm | 融资 | bpchar | 1 |  | √ | '0' | 融资 |
| 34 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | freturnmsg | 付款/拒付银行返回信息 | varchar | 255 |  | √ | ' ' | 付款/拒付银行返回信息 |
| 37 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 38 | farrivalbankid | 到单银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 39 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 40 | flockamount | 锁定金额 | numeric | 19 | 6 | √ | 0 | 锁定金额 |
| 41 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 42 | fbenefitertype | 受益人类型 | varchar | 50 |  | √ | ' ' | 受益人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 43 | fcolnew | 通知显示 | varchar | 50 |  | √ | ' ' | 通知显示,枚举: new :new |
| 44 | fcurrencyid | 信用证币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fispayconfig | 手动付款确认 | bpchar | 1 |  | √ | '0' | 手动付款确认 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fbenefiterid | 受益人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_arrival |  | fbillno |
| 2 | pk_t_lc_arrival |  | fid |

---

## 到单处理-反写记录表 t_lc_arrival_wb

- **表名称：** 到单处理-反写记录表
- **表名：** t_lc_arrival_wb

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
| 1 | idx_lc_arrival_wb_fk |  | fid |
| 2 | pk_lc_arrival_wb |  | fentryid |

---

## 单据体-子表 t_lc_arrcommitentry

- **表名称：** 单据体-子表
- **表名：** t_lc_arrcommitentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcommittime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbatchseqid | 提交银企批次号 | int8 | 64 |  | √ | 0 | 提交银企批次号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_arrcommitentry |  | fentryid |
| 2 | idx_lc_arrcomentry_fid |  | fid |

---

## 到单处理-分表 t_lc_arrival_e

- **表名称：** 到单处理-分表
- **表名：** t_lc_arrival_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexceedtime | 到单超出确认时间 | timestamp | 0 |  |  | null | 到单超出确认时间 |
| 3 | farrivalno | 到单编号 | varchar | 50 |  | √ | ' ' | 到单编号 |
| 4 | facceptreturnmsg | facceptreturnmsg | varchar | 255 |  | √ | ' ' |  |
| 5 | freceivedflag | 到单标识 | varchar | 50 |  | √ | '0' | 到单标识,枚举: 0 :一次到单 1 :二次到单 2 :修改/替换单据 3 :电索后来单 |
| 6 | ffrombankno | 来单银行编号 | varchar | 50 |  | √ | ' ' | 来单银行编号 |
| 7 | fopetype | 提交银企方式 | varchar | 50 |  | √ | ' ' | 提交银企方式,枚举: accept :承兑 payment :付款 protest :拒付 |
| 8 | ffeemode | 收费方式 | varchar | 50 |  | √ | ' ' | 收费方式,枚举: 1 :现收 2 :迟收 3 :免收 |
| 9 | fbuyerintamt | 付息金额 | numeric | 23 | 10 | √ | 0 | 付息金额 |
| 10 | fisinit | 初始化 | bpchar | 1 |  | √ | '0' | 初始化 |
| 11 | fendpaydate | 最迟付款日期 | timestamp | 0 |  |  | null | 最迟付款日期 |
| 12 | fbebankstatus | 付款/拒付直联提交状态 | varchar | 50 |  | √ | ' ' | 付款/拒付直联提交状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 13 | fisdiscrepancy | 有不符点 | bpchar | 1 |  | √ | '0' | 有不符点 |
| 14 | facceptbebankstatus | 承兑直联提交状态 | varchar | 50 |  | √ | ' ' | 承兑直联提交状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 15 | fexceeduserid | 到单超出确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fintcurrencyid | 付息币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fbuyerintid | 买方付息ID | int8 | 64 |  | √ | 0 | 买方付息ID |
| 18 | farrivallot | 到单批次 | int8 | 64 |  | √ | 0 | 到单批次 |
| 19 | fpayaccid | 付款账号一 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 20 | farrivalcurrencyid | 到单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | farrivalsignid | 到单签收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fpayamt2 | 账号二支付金额 | numeric | 23 | 10 | √ | 0 | 账号二支付金额 |
| 23 | farrivalamount | 到单金额 | numeric | 19 | 6 | √ | 0 | 到单金额 |
| 24 | fibppaytype | 预付款 | bpchar | 1 |  | √ | '0' | 预付款 |
| 25 | fcostbearparty | 费用承担方 | varchar | 50 |  | √ | ' ' | 费用承担方,枚举: 1 :开证方 2 :收证方 |
| 26 | fibpisref | 保税货物项下付汇 | bpchar | 1 |  | √ | '0' | 保税货物项下付汇 |
| 27 | fpayaccid2 | 付款账号二 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 28 | fsubmittime | 付款/拒付提交日期 | timestamp | 0 |  |  | null | 付款/拒付提交日期 |
| 29 | ftrancode | 交易编码 | varchar | 50 |  | √ | ' ' | 交易编码 |
| 30 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 31 | fbuyerint | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 32 | fisresubmit | 失败重提 | bpchar | 1 |  | √ | '0' | 失败重提 |
| 33 | fpayamt | 账号一支付金额 | numeric | 23 | 10 | √ | 0 | 账号一支付金额 |
| 34 | feassrcid | eas单据id | varchar | 50 |  | √ | ' ' | eas单据id |
| 35 | fdocpcsmode | 单据处理方式 | varchar | 50 |  | √ | ' ' | 单据处理方式,枚举: 1 :NOTIFY 2 :HOLD 3 :RETURN 4 :PREVINST |
| 36 | facceptsubmittime | 承兑提交日期 | timestamp | 0 |  |  | null | 承兑提交日期 |
| 37 | fpaynature | 付汇性质 | varchar | 50 |  | √ | ' ' | 付汇性质,枚举: X :保税区 E :出口加工区 D :钻石交易所 A :其他特殊经济区 M :深加工结转 O :其他 |
| 38 | fendacceptdate | 最迟承兑/付款确认日期 | timestamp | 0 |  |  | null | 最迟承兑/付款确认日期 |
| 39 | finvoiceamt | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 40 | fimagebatchno | 影像批次号 | varchar | 150 |  | √ | ' ' | 影像批次号 |
| 41 | fdatasource | 数据来源 | varchar | 50 |  | √ | 'hand_increase' | 数据来源,枚举: hand_increase :手工下推 bank_increase :在线登记 |
| 42 | ftradechannel | 交易渠道 | varchar | 50 |  | √ | 'offline' | 交易渠道,枚举: offline :线下处理 online :银企直联 |
| 43 | farrivalway | 到单处理方式 | varchar | 50 |  | √ | ' ' | 到单处理方式,枚举: accept :承兑 payment :付款 protest :拒付 |
| 44 | farrivaldate | 到单日期 | timestamp | 0 |  |  | null | 到单日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_arrival_e |  | fid |
| 2 | idx_lc_arrival_e_eassrcid |  | feassrcid |
| 3 | idx_lc_arrival_e |  | farrivalno |

---

## 到单处理-多语言表 t_lc_arrival_l

- **表名称：** 到单处理-多语言表
- **表名：** t_lc_arrival_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 4 | facceptreturnmsg | 承兑银行返回信息 | varchar | 255 |  | √ | ' ' | 承兑银行返回信息 |
| 5 | fexceedreson | 到单金额超出原因 | varchar | 255 |  | √ | ' ' | 到单金额超出原因 |
| 6 | frejectinfo | 拒付处理意见 | varchar | 255 |  | √ | ' ' | 拒付处理意见 |
| 7 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 8 | ffrombankname | 来单银行名称 | varchar | 255 |  | √ | ' ' | 来单银行名称 |
| 9 | freturnmsg | 付款/拒付银行返回信息 | varchar | 255 |  | √ | ' ' | 付款/拒付银行返回信息 |
| 10 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_arrival_l |  | fpkid |
| 2 | idx_lc_arrival_l |  | fid,flocaleid |

---

## 单据体-多语言表 t_lc_arrival_entry_l

- **表名称：** 单据体-多语言表
- **表名：** t_lc_arrival_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpayremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arrival_entry_l |  | fentryid,flocaleid |
| 2 | pk_t_lc_arrival_entry_l |  | fpkid |

---

## 关联子实体-子表 t_lc_arrival_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_arrival_lk

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
| 1 | pk_lc_arrival_lk |  | fpkid |
| 2 | idx_lc_arrival_lk_fk |  | fid |

---

## 到单处理-关联追踪表 t_lc_arrival_tc

- **表名称：** 到单处理-关联追踪表
- **表名：** t_lc_arrival_tc

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
| 1 | pk_lc_arrival_tc |  | fid |
| 2 | idx_lc_arrival_tc_tid |  | ftid |
| 3 | idx_lc_arrival_tc_tbill |  | ftbillid |
