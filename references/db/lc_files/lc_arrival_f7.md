# 到单处理F7-lc_arrival_f7

## 到单处理F7-主表 t_lc_arrival

- **表名称：** 到单处理F7-主表
- **表名：** t_lc_arrival

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | facceptreturnmsg | facceptreturnmsg | varchar | 255 |  | √ | ' ' |  |
| 3 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 5 | flettercreditid | 信用证号 | int8 | 64 |  | √ | 0 | [信用证 lc_lettercredit_f7](../lc_files/lc_lettercredit_f7.md) |
| 6 | fconfigtime | fconfigtime | timestamp | 0 |  |  | null |  |
| 7 | fexceedreson | fexceedreson | varchar | 255 |  | √ | ' ' |  |
| 8 | famount | 信用证金额 | numeric | 19 | 6 | √ | 0 | 信用证金额 |
| 9 | farrivaltype | 到单类型 | varchar | 50 |  | √ | ' ' | 到单类型,枚举: credit :信用证 da :DA到单 dp :DP到单 |
| 10 | fdoneamount | 已付金额 | numeric | 19 | 6 | √ | 0 | 已付金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | frecorddate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 13 | ftodoamount | 未付金额 | numeric | 19 | 6 | √ | 0 | 未付金额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbenefiterother | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 16 | fisfinancapply | fisfinancapply | bpchar | 1 |  | √ | '0' |  |
| 17 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 18 | frejectinfo | frejectinfo | varchar | 255 |  | √ | ' ' |  |
| 19 | ffrombankname | ffrombankname | varchar | 255 |  | √ | ' ' |  |
| 20 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 21 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 22 | fpayremark | fpayremark | varchar | 255 |  | √ | ' ' |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fispayment | fispayment | bpchar | 1 |  | √ | '0' |  |
| 25 | fdiscrepancy | fdiscrepancy | varchar | 255 |  | √ | ' ' |  |
| 26 | ffinancamount | ffinancamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fpushcount | fpushcount | int8 | 64 |  | √ | 0 |  |
| 31 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | farrivalstatus | 到单状态 | varchar | 50 |  | √ | ' ' | 到单状态,枚举: arrival_register :到单已登记 arrival_confirm :到单已确认 arrival_pay :到单已付款 |
| 33 | fislinkcfm | fislinkcfm | bpchar | 1 |  | √ | '0' |  |
| 34 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 35 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 36 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 37 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 38 | farrivalbankid | 到单银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 39 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 40 | flockamount | 锁定金额 | numeric | 19 | 6 | √ | 0 | 锁定金额 |
| 41 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 42 | fbenefitertype | 受益人类型 | varchar | 50 |  | √ | ' ' | 受益人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 43 | fcolnew | fcolnew | varchar | 50 |  | √ | ' ' |  |
| 44 | fcurrencyid | 信用证币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fispayconfig | fispayconfig | bpchar | 1 |  | √ | '0' |  |
| 46 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
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

## 到单处理F7-分表 t_lc_arrival_e

- **表名称：** 到单处理F7-分表
- **表名：** t_lc_arrival_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexceedtime | fexceedtime | timestamp | 0 |  |  | null |  |
| 3 | farrivalno | 到单编号 | varchar | 50 |  | √ | ' ' | 到单编号 |
| 4 | facceptreturnmsg | facceptreturnmsg | varchar | 255 |  | √ | ' ' |  |
| 5 | freceivedflag | freceivedflag | varchar | 50 |  | √ | '0' |  |
| 6 | ffrombankno | ffrombankno | varchar | 50 |  | √ | ' ' |  |
| 7 | fopetype | fopetype | varchar | 50 |  | √ | ' ' |  |
| 8 | ffeemode | ffeemode | varchar | 50 |  | √ | ' ' |  |
| 9 | fbuyerintamt | 付息金额 | numeric | 23 | 10 | √ | 0 | 付息金额 |
| 10 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 11 | fendpaydate | 最迟付款日期 | timestamp | 0 |  |  | null | 最迟付款日期 |
| 12 | fbebankstatus | fbebankstatus | varchar | 50 |  | √ | ' ' |  |
| 13 | fisdiscrepancy | 有不符点 | bpchar | 1 |  | √ | '0' | 有不符点 |
| 14 | facceptbebankstatus | facceptbebankstatus | varchar | 50 |  | √ | ' ' |  |
| 15 | fexceeduserid | fexceeduserid | int8 | 64 |  | √ | 0 |  |
| 16 | fintcurrencyid | 付息币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fbuyerintid | 买方付息ID | int8 | 64 |  | √ | 0 | 买方付息ID |
| 18 | farrivallot | farrivallot | int8 | 64 |  | √ | 0 |  |
| 19 | fpayaccid | fpayaccid | int8 | 64 |  | √ | 0 |  |
| 20 | farrivalcurrencyid | 到单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | farrivalsignid | 到单签收人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fpayamt2 | fpayamt2 | numeric | 23 | 10 | √ | 0 |  |
| 23 | farrivalamount | 到单金额 | numeric | 19 | 6 | √ | 0 | 到单金额 |
| 24 | fibppaytype | fibppaytype | bpchar | 1 |  | √ | '0' |  |
| 25 | fcostbearparty | fcostbearparty | varchar | 50 |  | √ | ' ' |  |
| 26 | fibpisref | fibpisref | bpchar | 1 |  | √ | '0' |  |
| 27 | fpayaccid2 | fpayaccid2 | int8 | 64 |  | √ | 0 |  |
| 28 | fsubmittime | fsubmittime | timestamp | 0 |  |  | null |  |
| 29 | ftrancode | ftrancode | varchar | 50 |  | √ | ' ' |  |
| 30 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
| 31 | fbuyerint | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 32 | fisresubmit | fisresubmit | bpchar | 1 |  | √ | '0' |  |
| 33 | fpayamt | fpayamt | numeric | 23 | 10 | √ | 0 |  |
| 34 | feassrcid | feassrcid | varchar | 50 |  | √ | ' ' |  |
| 35 | fdocpcsmode | fdocpcsmode | varchar | 50 |  | √ | ' ' |  |
| 36 | facceptsubmittime | facceptsubmittime | timestamp | 0 |  |  | null |  |
| 37 | fpaynature | fpaynature | varchar | 50 |  | √ | ' ' |  |
| 38 | fendacceptdate | 最迟承兑/付款确认日期 | timestamp | 0 |  |  | null | 最迟承兑/付款确认日期 |
| 39 | finvoiceamt | finvoiceamt | numeric | 23 | 10 | √ | 0 |  |
| 40 | fimagebatchno | fimagebatchno | varchar | 150 |  | √ | ' ' |  |
| 41 | fdatasource | fdatasource | varchar | 50 |  | √ | 'hand_increase' |  |
| 42 | ftradechannel | ftradechannel | varchar | 50 |  | √ | 'offline' |  |
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

## 到单处理F7-多语言表 t_lc_arrival_l

- **表名称：** 到单处理F7-多语言表
- **表名：** t_lc_arrival_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdiscrepancy | 不符点 | varchar | 255 |  | √ | ' ' | 不符点 |
| 4 | facceptreturnmsg | facceptreturnmsg | varchar | 255 |  | √ | ' ' |  |
| 5 | fexceedreson | fexceedreson | varchar | 255 |  | √ | ' ' |  |
| 6 | frejectinfo | frejectinfo | varchar | 255 |  | √ | ' ' |  |
| 7 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 8 | ffrombankname | ffrombankname | varchar | 255 |  | √ | ' ' |  |
| 9 | freturnmsg | freturnmsg | varchar | 255 |  | √ | ' ' |  |
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
