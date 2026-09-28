# 交单F7-lc_present_f7

## 交单F7-多语言表 t_lc_present_l

- **表名称：** 交单F7-多语言表
- **表名：** t_lc_present_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 4 | fexceedreson | fexceedreson | varchar | 255 |  | √ | ' ' |  |
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

## 交单F7-分表 t_lc_present_e

- **表名称：** 交单F7-分表
- **表名：** t_lc_present_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farrivalcurrencyid | 交单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fexceedtime | fexceedtime | timestamp | 0 |  |  | null |  |
| 4 | farrivalsignid | 交单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | farrivalno | 交单编号 | varchar | 50 |  | √ | ' ' | 交单编号 |
| 6 | farrivalamount | 交单金额 | numeric | 19 | 6 | √ | 0 | 交单金额 |
| 7 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 8 | fendpaydate | 对方最迟付款日期 | timestamp | 0 |  |  | null | 对方最迟付款日期 |
| 9 | fisdiscrepancy | 有不符点 | bpchar | 1 |  | √ | '0' | 有不符点 |
| 10 | fendacceptdate | 对方最迟承兑/付款确认日期 | timestamp | 0 |  |  | null | 对方最迟承兑/付款确认日期 |
| 11 | fexceeduserid | fexceeduserid | int8 | 64 |  | √ | 0 |  |
| 12 | farrivallot | farrivallot | int8 | 64 |  | √ | 0 |  |
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

## 交单F7-主表 t_lc_present

- **表名称：** 交单F7-主表
- **表名：** t_lc_present

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 受益人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 4 | flettercreditid | 信用证号 | int8 | 64 |  | √ | 0 | [收证信用证 lc_receipt_f7](../lc_files/lc_receipt_f7.md) |
| 5 | fconfigtime | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 6 | fexceedreson | fexceedreson | varchar | 255 |  | √ | ' ' |  |
| 7 | famount | 信用证金额 | numeric | 19 | 6 | √ | 0 | 信用证金额 |
| 8 | farrivaltype | 交单类型 | varchar | 50 |  | √ | ' ' | 交单类型,枚举: credit :信用证 da :DA交单 dp :DP交单 |
| 9 | fdoneamount | 已收金额 | numeric | 19 | 6 | √ | 0 | 已收金额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frecorddate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 12 | ftodoamount | 未收金额 | numeric | 19 | 6 | √ | 0 | 未收金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbenefiterother | 开证人 | varchar | 255 |  | √ | ' ' | 开证人 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fisreceipt | 存在关联收款单 | bpchar | 1 |  | √ | '0' | 存在关联收款单 |
| 17 | fisfinancapply | fisfinancapply | bpchar | 1 |  | √ | '0' |  |
| 18 | fvaliddate | fvaliddate | timestamp | 0 |  |  | null |  |
| 19 | finvoiceno | 交单发票号 | varchar | 80 |  | √ | ' ' | 交单发票号 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fisforfaiting | 存在关联福费廷 | bpchar | 1 |  | √ | '0' | 存在关联福费廷 |
| 24 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 25 | ffinancamount | ffinancamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | flastdate | flastdate | timestamp | 0 |  |  | null |  |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fpushcount | fpushcount | int8 | 64 |  | √ | 0 |  |
| 30 | fpresendbankid | 交单行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 31 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | farrivalstatus | 交单状态 | varchar | 50 |  | √ | ' ' | 交单状态,枚举: present_register :交单已登记 present_confirm :交单已确认 present_reciect :交单已收款 |
| 33 | fislinkcfm | 融资 | bpchar | 1 |  | √ | '0' | 融资 |
| 34 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 35 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 36 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 37 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 38 | flockamount | 锁定金额 | numeric | 19 | 6 | √ | 0 | 锁定金额 |
| 39 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | freceiptremark | freceiptremark | varchar | 255 |  | √ | ' ' |  |
| 41 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 42 | fbenefitertype | 开证人类型 | varchar | 50 |  | √ | ' ' | 开证人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 43 | fcolnew | fcolnew | varchar | 50 |  | √ | ' ' |  |
| 44 | fcurrencyid | 信用证币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fispayconfig | 手动收款确认 | bpchar | 1 |  | √ | '0' | 手动收款确认 |
| 46 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 47 | fbenefiterid | fbenefiterid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_present |  | fid |
| 2 | idx_lc_present |  | fbillno |
