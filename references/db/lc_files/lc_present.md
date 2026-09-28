# 交单处理-lc_present

## 交单处理-反写记录表 t_lc_present_wb

- **表名称：** 交单处理-反写记录表
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

## 交单处理-关联追踪表 t_lc_present_tc

- **表名称：** 交单处理-关联追踪表
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

## 交单处理-多语言表 t_lc_present_l

- **表名称：** 交单处理-多语言表
- **表名：** t_lc_present_l

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
| 1 | pk_t_lc_present_l |  | fpkid |
| 2 | idx_lc_present_l |  | fid,flocaleid |

---

## 交单处理-分表 t_lc_present_e

- **表名称：** 交单处理-分表
- **表名：** t_lc_present_e

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
| 1 | idx_lc_present_e |  | farrivalno |
| 2 | pk_t_lc_present_e |  | fid |

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

## 交单处理-主表 t_lc_present

- **表名称：** 交单处理-主表
- **表名：** t_lc_present

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
| 15 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 16 | fisreceipt | 存在关联收款单 | bpchar | 1 |  | √ | '0' | 存在关联收款单 |
| 17 | fisfinancapply | 关联融资申请 | bpchar | 1 |  | √ | '0' | 关联融资申请 |
| 18 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 19 | finvoiceno | 交单发票号 | varchar | 80 |  | √ | ' ' | 交单发票号 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fisforfaiting | 存在关联福费廷 | bpchar | 1 |  | √ | '0' | 存在关联福费廷 |
| 24 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 25 | ffinancamount | 融资金额 | numeric | 23 | 10 | √ | 0 | 融资金额 |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fpushcount | 下推次数 | int8 | 64 |  | √ | 0 | 下推次数 |
| 30 | fpresendbankid | 交单行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 31 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | farrivalstatus | 交单状态 | varchar | 50 |  | √ | ' ' | 交单状态,枚举: present_register :交单已登记 present_confirm :交单已确认 present_reciect :交单已收款 |
| 33 | fislinkcfm | 融资合同 | bpchar | 1 |  | √ | '0' | 融资合同 |
| 34 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 37 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 38 | flockamount | 锁定金额 | numeric | 19 | 6 | √ | 0 | 锁定金额 |
| 39 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 40 | freceiptremark | freceiptremark | varchar | 255 |  | √ | ' ' |  |
| 41 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 42 | fbenefitertype | 开证人类型 | varchar | 50 |  | √ | ' ' | 开证人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 43 | fcolnew | 通知显示 | varchar | 50 |  | √ | ' ' | 通知显示,枚举: new :new |
| 44 | fcurrencyid | 信用证币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fispayconfig | 手动收款确认 | bpchar | 1 |  | √ | '0' | 手动收款确认 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fbenefiterid | 开证人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_present |  | fid |
| 2 | idx_lc_present |  | fbillno |

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
