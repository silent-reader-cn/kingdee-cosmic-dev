# 银行下拨单-bei_banktransdownbill

## 分录-子表 t_bei_banktransdown_entry

- **表名称：** 分录-子表
- **表名：** t_bei_banktransdown_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 3 | fissuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 6 | fsonacctorg | 子账户申请公司名称 | varchar | 80 |  | √ | ' ' | 子账户申请公司名称 |
| 7 | fsourceentryid | 源单ID | varchar | 80 |  | √ | ' ' | 源单ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fsonacctbankname | 子账户开户行名称 | varchar | 80 |  | √ | ' ' | 子账户开户行名称 |
| 10 | fisupdatestate | 是否手动修改付款状态 | bpchar | 1 |  | √ | '0' | 是否手动修改付款状态 |
| 11 | fsonacctname | 子账户银企账户名称 | varchar | 80 |  | √ | ' ' | 子账户银企账户名称 |
| 12 | fstatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: OP :准备提交 TS :交易成功 TF :交易失败 NC :交易未确认 OS :银企处理中 BP :银行处理中 |
| 13 | fsubacct | 子账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 14 | fsonacctcity | 子账户开户行城市名称 | varchar | 80 |  | √ | ' ' | 子账户开户行城市名称 |
| 15 | fsonacctnumber | 子账户银行账号 | varchar | 80 |  | √ | ' ' | 子账户银行账号 |
| 16 | ftransamt | 下拨金额 | numeric | 19 | 6 | √ | 0.000000 | 下拨金额 |
| 17 | fsonacctprovince | 子账户开户行省名称 | varchar | 80 |  | √ | ' ' | 子账户开户行省名称 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_banktransdown_entry |  | fid |
| 2 | t_bei_banktransdown_entry_pkey |  | fentryid |

---

## 银行下拨单-多语言表 t_bei_banktransdownbill_l

- **表名称：** 银行下拨单-多语言表
- **表名：** t_bei_banktransdownbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_banktransdownbill_l_pkey |  | fpkid |
| 2 | idx_t_bei_banktransdownbill_l |  | fid,flocaleid |

---

## 银行下拨单-主表 t_bei_banktransdownbill

- **表名称：** 银行下拨单-主表
- **表名：** t_bei_banktransdownbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flastsourcebillid | 失败重付源单 | int8 | 64 |  | √ | 0 | 失败重付源单 |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fpaystate | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OP :准备提交 PS :部分成功 OS :银企处理中 |
| 5 | famount | 下拨总金额 | numeric | 19 | 6 | √ | 0.000000 | 下拨总金额 |
| 6 | fmonacctname | 母账户银企账户名称 | varchar | 255 |  | √ | ' ' | 母账户银企账户名称 |
| 7 | fispersonpay | 对私付款 | bpchar | 1 |  | √ | '1' | 对私付款 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fisupdatingstatus | 是否正在修改付款状态 | bpchar | 1 |  | √ | '0' | 是否正在修改付款状态 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fthirdpaystatus | 支付平台支付状态 | varchar | 255 |  | √ | ' ' | 支付平台支付状态 |
| 13 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 14 | fsourcetype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 15 | factamount | 已下拨金额 | numeric | 19 | 6 | √ | 0.000000 | 已下拨金额 |
| 16 | factcount | 已下拨笔数 | int8 | 64 |  | √ | 0 | 已下拨笔数 |
| 17 | fcount | 下拨总笔数 | int8 | 64 |  | √ | 0 | 下拨总笔数 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 F :已失败重付 T :已打回 |
| 21 | ftransbillno | 下拨单号 | varchar | 80 |  | √ | ' ' | 下拨单号 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fmonacctprovince | 母账户省名称 | varchar | 255 |  | √ | ' ' | 母账户省名称 |
| 24 | fmonacctbankname | 母账户开户行名称 | varchar | 255 |  | √ | ' ' | 母账户开户行名称 |
| 25 | fmonacctcity | 母账户城市名称 | varchar | 255 |  | √ | ' ' | 母账户城市名称 |
| 26 | fsubmittime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 29 | fmonacctorg | 母账户申请公司名称 | varchar | 255 |  | √ | ' ' | 母账户申请公司名称 |
| 30 | fserialnumber | null | varchar | 80 |  | √ | ' ' | null |
| 31 | fpayunique | 付款防重字段 | int8 | 64 |  | √ | 0 | 付款防重字段 |
| 32 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 34 | fbankid | 母账户开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 35 | fmonacctnumber | 母账户银行账号 | varchar | 255 |  | √ | ' ' | 母账户银行账号 |
| 36 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | faccountbankid | 母账户银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 39 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 40 | fcompanyid | 母账户收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fisbitback | 打回标识 | bpchar | 1 |  | √ | '0' | 打回标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_banktransdownbill |  | fbillno |
| 2 | idx_t_bei_banktransdownunique |  | fsourcebillid,fpayunique |
| 3 | t_bei_banktransdownbill_pkey |  | fid |
