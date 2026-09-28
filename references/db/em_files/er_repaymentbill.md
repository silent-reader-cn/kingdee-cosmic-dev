# 还款单-er_repaymentbill

## 还款明细-子表 t_er_repaymententry

- **表名称：** 还款明细-子表
- **表名：** t_er_repaymententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forirepayamount | 还款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额 |
| 3 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fsourceentryid | 源单分录id | varchar | 100 |  | √ | ' ' | 源单分录id |
| 5 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | forirepayapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 8 | fexchangerate | 源单汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 源单汇率 |
| 9 | freverseorirepayamount | 反写还款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 反写还款金额 |
| 10 | frelationloanbill | 关联借款id | varchar | 200 |  | √ | ' ' | 关联借款id |
| 11 | fsrcquotetype | 源单换算方式 | bpchar | 1 |  | √ | '0' | 源单换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | frecamount | 已收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已收款金额（本位币） |
| 13 | frepayapproveamount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0 | 核定金额(本位币) |
| 14 | fsourcebillno | 源单编号 | varchar | 100 |  | √ | ' ' | 源单编号 |
| 15 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 16 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 17 | ftotalloanamount | 总借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 总借款金额 |
| 18 | fpushcount | 下推计数器 | int8 | 64 |  | √ | 0 | 下推计数器 |
| 19 | forirecamount | 已收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收款金额 |
| 20 | frepayamount | 还款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额(本位币) |
| 21 | floandescription | 借款事由 | varchar | 1000 |  | √ | ' ' | 借款事由 |
| 22 | freverserepayamount | 反写还款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 反写还款金额（本位币） |
| 23 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 24 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 er_prepaybill :预付单 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | freversecurrency | 反写币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 28 | frepayexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_repaymententry_pkey |  | fentryid |
| 2 | idx_er_repaymententry_fseq |  | fid,fseq |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattstarttime | fattstarttime | timestamp | 0 |  |  | null |  |
| 3 | fattlargetxt | fattlargetxt | varchar | 255 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | fattachserialno | varchar | 255 |  | √ | ' ' |  |
| 6 | fattsource | fattsource | varchar | 30 |  | √ | ' ' |  |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 9 | fattaffairdiscription | fattaffairdiscription | varchar | 1024 |  |  | null |  |
| 10 | fattheadcount | fattheadcount | int8 | 64 |  | √ | 0 |  |
| 11 | fattcity | fattcity | varchar | 255 |  |  | null |  |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | fattenddate | timestamp | 0 |  |  | null |  |
| 14 | fattinvoiceentyid | fattinvoiceentyid | int8 | 64 |  | √ | 0 |  |
| 15 | fattfrom | fattfrom | varchar | 255 |  |  | null |  |
| 16 | fattlargetxt_tag | fattlargetxt_tag | text | 0 |  |  | null |  |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | fattto | varchar | 255 |  |  | null |  |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | fattendtime | timestamp | 0 |  |  | null |  |
| 23 | fattapplydate | fattapplydate | timestamp | 0 |  |  | null |  |
| 24 | fattstartdate | fattstartdate | timestamp | 0 |  |  | null |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | fatttotalamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 28 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoiceattachinfo |  | fentryid |
| 2 | idx_er_invoiceattachinfo_fid |  | fid |

---

## 关联子实体-子表 t_er_repayrecentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_repayrecentry_lk

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
| 1 | pk_er_repayrecentry_lk |  | fpkid |
| 2 | idx_er_repayrecentry_lk_fk |  | fentryid |

---

## 还款单-反写记录表 t_er_repaymentbill_wb

- **表名称：** 还款单-反写记录表
- **表名：** t_er_repaymentbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
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
| 1 | t_er_repaymentbill_wb_pkey |  | fentryid |
| 2 | idx_er_repaybill_wb_fid |  | fid |

---

## 还款单-关联追踪表 t_er_repaymentbill_tc

- **表名称：** 还款单-关联追踪表
- **表名：** t_er_repaymentbill_tc

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
| 1 | idx_er_repaymentbill_tc_tid |  | ftid |
| 2 | idx_er_repaybill_tc_ftbillid |  | ftbillid |
| 3 | t_er_repaymentbill_tc_pkey |  | fid |
| 4 | idx_er_repaymentbill_tc_tbill |  | ftbillid |

---

## 收款明细信息-子表 t_er_recentrydetail

- **表名称：** 收款明细信息-子表
- **表名：** t_er_recentrydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcasbizdate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 3 | fcasbank | 收款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 4 | faccountnumber | 收款账号 | varchar | 50 |  | √ | ' ' | 收款账号 |
| 5 | fcasentryid | 收款单分录id | int8 | 64 |  | √ | 0 | 收款单分录id |
| 6 | fcasid | 收款单id | int8 | 64 |  | √ | 0 | 收款单id |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbankaccountname | 收款账户名称 | varchar | 50 |  | √ | ' ' | 收款账户名称 |
| 9 | fcaselocalamt | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 10 | fcasexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fcaseactamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 12 | fcascurrency | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fcasbillno | 收款单号 | varchar | 50 |  | √ | ' ' | 收款单号 |
| 14 | fcasreceivingtype | 收款类型 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 17 | fcasbankaccount | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 18 | fcascashaccount | 现金账户 | int8 | 64 |  | √ | 0 | [现金账户 cas_accountcash](../cas_files/cas_accountcash.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_recentrydetail_fid |  | fid |
| 2 | pk_t_er_recentrydetail |  | fentryid |

---

## 关联子实体-子表 t_er_repaymentbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_repaymentbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_repaymentbill_lk_pkey |  | fpkid |
| 2 | idx_er_repaybill_lk_fid |  | fid |

---

## 还款单-多语言表 t_er_repaymentbill_l

- **表名称：** 还款单-多语言表
- **表名：** t_er_repaymentbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_repb_l_fid |  | fid,flocaleid |
| 2 | t_er_repaymentbill_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_er_recentrydetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_recentrydetail_lk

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
| 1 | idx_er_recentrydetail_lk_fk |  | fentryid |
| 2 | pk_er_recentrydetail_lk |  | fpkid |

---

## 收款信息-子表 t_er_repayrecentry

- **表名称：** 收款信息-子表
- **表名：** t_er_repayrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freccurrency | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | frecbillno | 收款单号 | varchar | 255 |  | √ | ' ' | 收款单号 |
| 4 | faccountname | 收款账户名称 | varchar | 50 |  | √ | ' ' | 收款账户名称 |
| 5 | foriactrecamt | 整单收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 整单收款金额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frecexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | freceivingtype | 收款类型 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 9 | faccountbank | 收款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 10 | fismanualrelated | 手动关联 | bpchar | 1 |  | √ | '0' | 手动关联 |
| 11 | fpayeebank | 收款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 12 | factrecamt | 整单收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 整单收款金额(本位币) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | frecbillid | 收款单id | int8 | 64 |  | √ | 0 | 收款单id |
| 15 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 16 | fpayeedate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_repayrecentry_fseq |  | fentryid,fseq |
| 2 | pk_t_er_repayrecentry |  | fentryid |
| 3 | idx_er_repayrecentry_frecid |  | frecbillid |

---

## 还款单-主表 t_er_repaymentbill

- **表名称：** 还款单-主表
- **表名：** t_er_repaymentbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalnotactrecamt | 待收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 待收款金额 |
| 3 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 4 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 5 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fpartnerid | fpartnerid | int8 | 64 |  | √ | 0 |  |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 9 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 10 | fbillcode | fbillcode | varchar | 30 |  | √ | ' ' |  |
| 11 | foricurrencyid | foricurrencyid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 14 | forigin | forigin | varchar | 10 |  | √ | ' ' |  |
| 15 | fpayername | 付款人 | varchar | 100 |  | √ | ' ' | 付款人 |
| 16 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 17 | fsupplier | 付款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 18 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 19 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | ftotalactrecamt | 已收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已收款金额 |
| 21 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 22 | fisgeneratereceipt | 生成收款单 | bpchar | 1 |  | √ | ' ' | 生成收款单 |
| 23 | fpushnum | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 24 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 25 | fimageno | 影像编号 | varchar | 80 |  | √ | ' ' | 影像编号 |
| 26 | fbillno | 单据编号 | varchar | 80 |  | √ | '0' | 单据编号 |
| 27 | fcustomer | 付款人（客户） | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 28 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 29 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待收款 G :已收款 H :废弃 I :关闭 |
| 30 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fisenableinvoice | 启用发票云 | bpchar | 1 |  | √ | '0' | 启用发票云 |
| 33 | fapproveamount | 核定金额本位币合计 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额本位币合计 |
| 34 | fnotpayamount | fnotpayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | '0' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 38 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fbalanceamount | fbalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | ftel | 联系方式 | varchar | 30 |  | √ | ' ' | 联系方式 |
| 41 | ftotalorirecamount | (废弃的已收款金额，单头原币金额无用) | numeric | 23 | 10 | √ | 0.0000000000 | (废弃的已收款金额，单头原币金额无用) |
| 42 | fothercontactunit | 其他往来单位 | int8 | 64 |  | √ | 0 | [其他往来单位 cas_othercontactunit](../cas_files/cas_othercontactunit.md) |
| 43 | fpayertype | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 cas_othercontactunit :其他往来单位 |
| 44 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 45 | famount | 还款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额(本位币) |
| 46 | fpayamount | fpayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | fplandays | fplandays | int8 | 64 |  | √ | 0 |  |
| 48 | fsourcebillformid | fsourcebillformid | varchar | 30 |  | √ | ' ' |  |
| 49 | freceiptbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 50 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fusedamount | fusedamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fencashamount | fencashamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 53 | fpayeraccountname | 账户名称 | varchar | 50 |  | √ | ' ' | 账户名称 |
| 54 | fpayerid | 付款人(个人) | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 55 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 |
| 57 | frelatedloan | frelatedloan | int8 | 64 |  | √ | 0 |  |
| 58 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 59 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 60 | ftriptypeid | ftriptypeid | int8 | 64 |  | √ | 0 |  |
| 61 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 62 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 63 | fbuildrelationway | 下游单据来源 | bpchar | 1 |  | √ | ' ' | 下游单据来源,枚举: 1 :BOTP下推 2 :手动绑定 |
| 64 | freimbursetype | 还款类型 | varchar | 50 |  | √ | ' ' | 还款类型,枚举: prepayrefund :预付退款 repayment :个人还款 |
| 65 | fcasorg | 付款人（内部公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 66 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 68 | fsourcebillid | fsourcebillid | varchar | 200 |  | √ | ' ' |  |
| 69 | fpayeraccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 70 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 71 | frepaymentdate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rpb_fcostcompanyid |  | fcostcompanyid |
| 2 | t_er_repaymentbill_pkey |  | fid |
| 3 | idx_er_rpb_fbillno |  | fbillno |

---

## 关联子实体-子表 t_er_repaymententry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_repaymententry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | forirepayamount | 还款金额_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额_确认携带值 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | frepayamount_old | frepayamount_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 8 | freverserepayamount_old | 反写还款金额（本位币）_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 反写还款金额（本位币）_原始携带值 |
| 9 | frepayamount | frepayamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | freverserepayamount | 反写还款金额（本位币）_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 反写还款金额（本位币）_确认携带值 |
| 11 | forirepayamount_old | 还款金额_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 还款金额_原始携带值 |
| 12 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 13 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_repayentry_lk_fid |  | fid |
| 2 | idx_repaymententry_lk_entryid |  | fentryid |
| 3 | t_er_repaymententry_lk_pkey |  | fpkid |
