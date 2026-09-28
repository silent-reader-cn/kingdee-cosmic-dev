# 交单确认历史-lc_present_h

## 交单确认历史-反写记录表 t_lc_present_wb

- **表名称：** 交单确认历史-反写记录表
- **表名：** t_lc_present_wb

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
| 1 | idx_lc_present_wb_fk |  | fid |
| 2 | pk_lc_present_wb |  | fentryid |

---

## 费用信息分录-子表 t_lc_fee_h

- **表名称：** 费用信息分录-子表
- **表名：** t_lc_fee_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctbankid | 费用账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 3 | foppacctbank | 对方银行账号 | varchar | 100 |  | √ | ' ' | 对方银行账号 |
| 4 | fschemeid | 费用方案 | int8 | 64 |  | √ | 0 | [费用方案 fbd_feescheme](../fbd_files/fbd_feescheme.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famt | 费用金额 | numeric | 19 | 6 | √ | 0 | 费用金额 |
| 7 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: hand :手工新增 linkgen :费用关联生成 |
| 8 | frate | 费率（%） | numeric | 23 | 10 | √ | 0 | 费率（%） |
| 9 | fissettle | 已结算 | bpchar | 1 |  | √ | '0' | 已结算 |
| 10 | fbillnum | 费用单据编号 | varchar | 30 |  | √ | ' ' | 费用单据编号 |
| 11 | foppunittext | 对方单位 | varchar | 100 |  | √ | ' ' | 对方单位 |
| 12 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | ffeenumber | 费用编码 | varchar | 80 |  | √ | ' ' | 费用编码 |
| 14 | foppunittype | 对方单位类型 | varchar | 80 |  | √ | ' ' | 对方单位类型,枚举: bos_org :内部单位 bd_finorginfo :合作金融机构 bd_supplier :供应商 bd_customer :客户 fbd_other :其他 |
| 15 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 01LETTER :开证处理 02ARRIVAL :到单处理 03PRESENT :交单处理 04FORFAIT :福费廷处理 05CHANGE :改证 06UNSUBMIT :撤证 07ACTIVE :激活 08CLOSE :闭卷 |
| 16 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 17 | ftypeid | 费用类型 | int8 | 64 |  | √ | 0 | [费用类型 fbd_feetype](../fbd_files/fbd_feetype.md) |
| 18 | fexcrate | 折债务币种汇率 | numeric | 23 | 10 | √ | 0 | 折债务币种汇率 |
| 19 | foppbebankid | 对方开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 20 | fbillentryid | 费用单据分录id | int8 | 64 |  | √ | 0 | 费用单据分录id |
| 21 | fbillid | 费用单据id | int8 | 64 |  | √ | 0 | 费用单据id |
| 22 | foppunitid | 对方单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fpaydate | 费用日期 | timestamp | 0 |  |  | null | 费用日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_fee_h |  | fentryid |
| 2 | idx_lc_fee_h |  | fid |

---

## 交单确认历史-多语言表 t_lc_present_h_l

- **表名称：** 交单确认历史-多语言表
- **表名：** t_lc_present_h_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 4 | fexceedreson | 交单金额超出原因 | varchar | 255 |  | √ | ' ' | 交单金额超出原因 |
| 5 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_present_h_l |  | fid,flocaleid |
| 2 | pk_t_lc_present_h_l |  | fpkid |

---

## 单据体-多语言表 t_lc_present_entry_l

- **表名称：** 单据体-多语言表
- **表名：** t_lc_present_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freceiptremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
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
| 1 | idx_lc_present_entry_l |  | fentryid,flocaleid |
| 2 | pk_t_lc_present_entry_l |  | fpkid |

---

## 交单确认历史-分表 t_lc_present_h_e

- **表名称：** 交单确认历史-分表
- **表名：** t_lc_present_h_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farrivalcurrencyid | 交单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fexceedtime | 交单超出确认时间 | timestamp | 0 |  |  | null | 交单超出确认时间 |
| 4 | farrivalsignid | 交单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | farrivalno | 交单编号 | varchar | 50 |  | √ | ' ' | 交单编号 |
| 6 | farrivalamount | 交单金额 | numeric | 19 | 6 | √ | 0 | 交单金额 |
| 7 | fisinit | 初始化 | bpchar | 1 |  | √ | '0' | 初始化 |
| 8 | fendpaydate | 对方最迟付款日期 | timestamp | 0 |  |  | null | 对方最迟付款日期 |
| 9 | fisdiscrepancy | 有不符点 | bpchar | 1 |  | √ | '0' | 有不符点 |
| 10 | fendacceptdate | 对方最迟承兑/付款确认日期 | timestamp | 0 |  |  | null | 对方最迟承兑/付款确认日期 |
| 11 | fexceeduserid | 交单超出确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | farrivallot | 交单批次 | int8 | 64 |  | √ | 0 | 交单批次 |
| 13 | farrivalway | 交单对方处理方式 | varchar | 50 |  | √ | ' ' | 交单对方处理方式,枚举: accept :承兑 payment :付款 protest :拒付 |
| 14 | farrivaldate | 交单日期 | timestamp | 0 |  |  | null | 交单日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_present_h_e |  | farrivalno |
| 2 | pk_t_lc_present_h_e |  | fid |

---

## 交单确认历史-关联追踪表 t_lc_present_tc

- **表名称：** 交单确认历史-关联追踪表
- **表名：** t_lc_present_tc

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
| 1 | idx_lc_present_tc_tbill |  | ftbillid |
| 2 | idx_lc_present_tc_tid |  | ftid |
| 3 | pk_lc_present_tc |  | fid |

---

## 交单确认历史-主表 t_lc_present_h

- **表名称：** 交单确认历史-主表
- **表名：** t_lc_present_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 受益人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 4 | flettercreditid | 信用证号 | int8 | 64 |  | √ | 0 | [收证信用证 lc_receipt_f7](../lc_files/lc_receipt_f7.md) |
| 5 | fconfigtime | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 6 | fexceedreson | 交单金额超出原因 | varchar | 255 |  | √ | ' ' | 交单金额超出原因 |
| 7 | famount | 信用证金额 | numeric | 19 | 6 | √ | 0 | 信用证金额 |
| 8 | farrivaltype | 交单类型 | varchar | 50 |  | √ | ' ' | 交单类型,枚举: credit :信用证 da :DA交单 dp :DP交单 |
| 9 | fdoneamount | 已收金额 | numeric | 19 | 6 | √ | 0 | 已收金额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frecorddate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 12 | ftodoamount | 未收金额 | numeric | 19 | 6 | √ | 0 | 未收金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbenefiterother | 开证人 | varchar | 255 |  | √ | ' ' | 开证人 |
| 15 | fisreceipt | 存在关联收款单 | bpchar | 1 |  | √ | '0' | 存在关联收款单 |
| 16 | fisfinancapply | 关联融资申请 | bpchar | 1 |  | √ | '0' | 关联融资申请 |
| 17 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 18 | finvoiceno | 交单发票号 | varchar | 80 |  | √ | ' ' | 交单发票号 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fisforfaiting | 存在关联福费廷 | bpchar | 1 |  | √ | '0' | 存在关联福费廷 |
| 23 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 24 | ffinancamount | 融资金额 | numeric | 23 | 10 | √ | 0 | 融资金额 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fpushcount | 下推次数 | int8 | 64 |  | √ | 0 | 下推次数 |
| 29 | fpresendbankid | 交单行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 30 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | farrivalstatus | 交单状态 | varchar | 50 |  | √ | ' ' | 交单状态,枚举: present_register :交单已登记 present_confirm :交单已确认 present_reciect :交单已收款 |
| 32 | fislinkcfm | 融资合同 | bpchar | 1 |  | √ | '0' | 融资合同 |
| 33 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 34 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 35 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 36 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 37 | flockamount | 锁定金额 | numeric | 19 | 6 | √ | 0 | 锁定金额 |
| 38 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 39 | fbenefitertype | 开证人类型 | varchar | 50 |  | √ | ' ' | 开证人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 40 | fcolnew | 通知显示 | varchar | 50 |  | √ | ' ' | 通知显示,枚举: new :new |
| 41 | fcurrencyid | 信用证币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fispayconfig | 手动收款确认 | bpchar | 1 |  | √ | '0' | 手动收款确认 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fbenefiterid | 开证人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_present_h |  | fbillno |
| 2 | pk_t_lc_present_h |  | fid |

---

## 关联子实体-子表 t_lc_present_lk

- **表名称：** 关联子实体-子表
- **表名：** t_lc_present_lk

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
| 1 | idx_lc_present_lk_fk |  | fid |
| 2 | pk_lc_present_lk |  | fpkid |

---

## 单据体-子表 t_lc_present_entry

- **表名称：** 单据体-子表
- **表名：** t_lc_present_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiptamount | 收款金额 | numeric | 19 | 6 | √ | 0 | 收款金额 |
| 3 | fserviceamount | 手续费 | numeric | 19 | 6 | √ | 0 | 手续费 |
| 4 | freceiptno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 5 | fprereceiptamount | 交单收款金额 | numeric | 19 | 6 | √ | 0 | 交单收款金额 |
| 6 | fbusinessdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fwritetime | 写入时间 | timestamp | 0 |  |  | null | 写入时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freceiptremark | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 10 | freceiptid | 收款单主键ID | int8 | 64 |  | √ | 0 | 收款单主键ID |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | freceiptcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_present_entry |  | fentryid |
| 2 | idx_lc_present_entry |  | fid |
