# 资金上划单-fca_transupbill

## 划拨明细-子表 t_fca_transupbill_entry

- **表名称：** 划拨明细-子表
- **表名：** t_fca_transupbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisifmbill | 是否生成内部结算 | bpchar | 1 |  | √ | '0' | 是否生成内部结算 |
| 3 | fsubmitpaytime | 提交支付时间 | timestamp | 0 |  |  | null | 提交支付时间 |
| 4 | flockedamtpay | 锁定金额-付款处理 | numeric | 19 | 6 | √ | 0.0000000000 | 锁定金额-付款处理 |
| 5 | fdiscarduserid | 作废操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fbankcheckflag | 对账标识码 | varchar | 50 |  | √ | ' ' | 对账标识码 |
| 7 | fbcamount | 上划金额本位币 | numeric | 23 | 10 | √ | 0 | 上划金额本位币 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdiscardreason | 作废原因 | varchar | 255 |  | √ | ' ' | 作废原因 |
| 10 | flockedamtifm | 锁定金额-内部金融 | numeric | 19 | 6 | √ | 0.0000000000 | 锁定金额-内部金融 |
| 11 | fisinneracccashbill | 是否已生成内部账户回单 | bpchar | 1 |  | √ | '0' | 是否已生成内部账户回单 |
| 12 | fdiscardtime | 作废时间 | timestamp | 0 |  |  | null | 作废时间 |
| 13 | finneracctid | 子账户内部账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 14 | fpaystatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: beiproc :银企处理中 payproc :银行处理中 paysuccess :交易成功 payfail :交易失败 noconfirm :交易未确认 init : |
| 15 | fmatchresult | 是否已匹配 | bpchar | 1 |  | √ | '0' | 是否已匹配 |
| 16 | fpaychanel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 17 | ftransamt | 上划金额 | numeric | 19 | 6 | √ | 0.000000 | 上划金额 |
| 18 | fpayuser | 支付人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | freferamt | 参考上划金额 | numeric | 19 | 6 | √ | 0.000000 | 参考上划金额 |
| 20 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fpayreturntime | 返回时间 | timestamp | 0 |  |  | null | 返回时间 |
| 22 | flockedamtrec | 锁定金额-收款处理 | numeric | 19 | 6 | √ | 0.0000000000 | 锁定金额-收款处理 |
| 23 | fdiscardtimestr | 作废时间(文本) | varchar | 60 |  | √ | ' ' | 作废时间(文本) |
| 24 | fstate | 明细状态 | varchar | 30 |  | √ | ' ' | 明细状态,枚举: normal :正常 discard :已作废 back :打回 delete :删除 |
| 25 | fpayreturninfo | 支付返回信息 | varchar | 255 |  | √ | ' ' | 支付返回信息 |
| 26 | fiscashbill | 是否生成回单 | bpchar | 1 |  | √ | '0' | 是否生成回单 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fsubacctid | 子账户银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 29 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 30 | fsubacctcompid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transupbill_fid |  | fid |
| 2 | t_fca_transupbill_entry_pkey |  | fentryid |

---

## 关联子实体-子表 t_fca_transupbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fca_transupbill_lk

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
| 1 | t_fca_trupbill_lk_fid |  | fid |
| 2 | t_fca_transupbill_lk_pkey |  | fpkid |

---

## 资金上划单-关联追踪表 t_fca_transupbill_tc

- **表名称：** 资金上划单-关联追踪表
- **表名：** t_fca_transupbill_tc

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
| 1 | idx_fca_transupbill_tc_tbill |  | ftbillid |
| 2 | t_fca_transupbill_tc_pkey |  | fid |
| 3 | idx_fca_transupbill_tc_tid |  | ftid |
| 4 | t_fca_trubi_tc_ftbillid |  | ftbillid |

---

## 资金上划单-主表 t_fca_transupbill

- **表名称：** 资金上划单-主表
- **表名：** t_fca_transupbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织(不用) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | facctgrpid | 母子账户组 | int8 | 64 |  | √ | 0 | 母子账户组 fca_acctgroup |
| 4 | ftranscount | 上划总笔数 | int8 | 64 |  | √ | 0 | 上划总笔数 |
| 5 | famount | 上划总金额 | numeric | 19 | 6 | √ | 0.000000 | 上划总金额 |
| 6 | fpayflagid | 付款标识 | int8 | 64 |  | √ | 0 | 付款标识 cas_paymentidentify |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpaymentchanel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsourcetype | 业务来源 | varchar | 30 |  | √ | ' ' | 业务来源,枚举: generate :申请单生成 manual :手工创建 autotran :自动划拨 recinitiative :收款入账中心 paypassive :付款入账中心 |
| 12 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 P :付款处理中 D :已付款 S :已作废 |
| 16 | fispushifm | 是否下推内部金融 | bpchar | 1 |  | √ | '1' | 是否下推内部金融 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fvouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 19 | fbcsuccesstotalamount | 上划成功总金额本位币 | numeric | 23 | 10 | √ | 0 | 上划成功总金额本位币 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | ftransbilldate | 上划日期 | timestamp | 0 |  |  | null | 上划日期 |
| 23 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | ftranssuccount | 上划成功总笔数 | int8 | 64 |  | √ | 0 | 上划成功总笔数 |
| 25 | fbizdate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 26 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 27 | fbctotalamount | 上划总金额本位币 | numeric | 23 | 10 | √ | 0 | 上划总金额本位币 |
| 28 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 29 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 30 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 31 | fbankid | 母账户开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 32 | ftranssucamt | 上划成功总金额 | numeric | 19 | 6 | √ | 0.000000 | 上划成功总金额 |
| 33 | fismatchbyhead | 是否按单头匹配 | bpchar | 1 |  | √ | '0' | 是否按单头匹配 |
| 34 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | faccountbankid | 母账户银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 37 | fischangepaych | 是否在变更支付渠道 | bpchar | 1 |  | √ | '0' | 是否在变更支付渠道 |
| 38 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 39 | fcompanyid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fcombofield | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transupbill_pkey |  | fid |
| 2 | t_fca_transupbill_createtime |  | fcreatetime |
| 3 | t_fca_transupbill_num |  | fbillno |

---

## 关联子实体-子表 t_fca_transupbill_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fca_transupbill_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transupbill_entry_lk_pkey |  | fpkid |
| 2 | t_fca_trubi_et_lk_fid |  | fentryid |

---

## 资金上划单-多语言表 t_fca_transupbill_l

- **表名称：** 资金上划单-多语言表
- **表名：** t_fca_transupbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fca_transupbill_l_pkey |  | fpkid |
| 2 | t_fca_transupbill_l_fid |  | fid,flocaleid |

---

## 资金上划单-反写记录表 t_fca_transupbill_wb

- **表名称：** 资金上划单-反写记录表
- **表名：** t_fca_transupbill_wb

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
| 1 | t_fca_trubill_wb_fid |  | fid |
| 2 | t_fca_transupbill_wb_pkey |  | fentryid |
