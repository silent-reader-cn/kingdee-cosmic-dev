# 应付调汇单-ap_adjexchbill

## 关联子实体-子表 t_ap_adjexchbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_adjexchbillentry_lk

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
| 1 | idx_ap_adjexchbillentry_lk_fk |  | fentryid |
| 2 | pk_ap_adjexchbillentry_lk |  | fpkid |

---

## 关联子实体-子表 t_ap_adjexchbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_adjexchbill_lk

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
| 1 | idx_ap_adjexchbill_lk_fk |  | fid |
| 2 | pk_ap_adjexchbill_lk |  | fpkid |

---

## 应付调汇单-主表 t_ap_adjexchbill

- **表名称：** 应付调汇单-主表
- **表名：** t_ap_adjexchbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherbillno | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 3 | fcurbusgainloss | 调汇暂估成本金额 | numeric | 23 | 10 | √ | 0 | 调汇暂估成本金额 |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fgainloss | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 6 | flastgainloss | 上期汇兑损益（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 上期汇兑损益（废弃） |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fistaxdeduction | 税额不计入成本 | bpchar | 1 |  | √ | '0' | 税额不计入成本 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | flocalbalance | 调汇前余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 调汇前余额（本位币） |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ap_busbill :暂估应付单 ar_busbill :暂估应收单 ap_finapbill :财务应付单 ar_finarbill :财务应收单 cas_recbill :收款单 cas_paybill :付款单 ap_paidbill :期初预付单 ar_receivedbill :期初预收单 |
| 14 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 15 | fhadwrittenoff | 已冲回 | bpchar | 1 |  | √ | '0' | 已冲回 |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fsrcbiztype | 源单业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbalance | 原币余额 | numeric | 23 | 10 | √ | 0.0000000000 | 原币余额 |
| 20 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 21 | fcurgainloss | 调汇金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调汇金额 |
| 22 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 23 | fsrcbilltype | 源单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fisperiod | 初始化 | bpchar | 1 |  | √ | '0' | 初始化 |
| 26 | fsrcbillno | 源单据编号 | varchar | 80 |  | √ | ' ' | 源单据编号 |
| 27 | fisincludeentry | 是否含分录 | bpchar | 1 |  | √ | '0' | 是否含分录 |
| 28 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 29 | fcurlocalbalance | 调汇后余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 调汇后余额（本位币） |
| 30 | fquotation | 当前换算方式 | varchar | 30 |  | √ | '0' | 当前换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 31 | fbiztype | 业务分类 | varchar | 50 |  | √ | ' ' | 业务分类,枚举: achieved_adjust :已实现调汇 final_adjust :期末调汇 final_adjust_writtenoff :期末调汇冲回 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | flastexchangerate | 源单汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 源单汇率 |
| 34 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 35 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 37 | fasstactid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 38 | fbuscostamt | 原币暂估成本金额 | numeric | 23 | 10 | √ | 0 | 原币暂估成本金额 |
| 39 | fbuscostamtlocal | 调汇前暂估成本余额（本位币） | numeric | 23 | 10 | √ | 0 | 调汇前暂估成本余额（本位币） |
| 40 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fsourcebilldate | 源单日期 | timestamp | 0 |  |  | null | 源单日期 |
| 42 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 43 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 44 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 45 | fbizsystem | 业务系统 | varchar | 30 |  | √ | ' ' | 业务系统,枚举: AR :应收 AP :应付 CAS :出纳 |
| 46 | fsrcbillquotation | 源单换算方式 | varchar | 30 |  | √ | '0' | 源单换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 47 | fcurbuscostamtlocal | 调汇后暂估成本余额（本位币） | numeric | 23 | 10 | √ | 0 | 调汇后暂估成本余额（本位币） |
| 48 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_adjexch_bizdate |  | fbizdate |
| 2 | idx_ap_adjexch_billno |  | fbillno |
| 3 | idx_ap_adjexch_srcebillid |  | fsourcebillid |
| 4 | idx_ap_adjexch_orgid |  | forgid,fperiodid,fbizsystem |
| 5 | pk_ap_adjexchbill |  | fid |

---

## 明细-子表 t_ap_adjexchbillentry

- **表名称：** 明细-子表
- **表名：** t_ap_adjexchbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | frectype | 收款用途 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpaytype | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 10 | fcurlocalbalance | 调汇后余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 调汇后余额（本位币） |
| 11 | fgainloss | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 12 | flastgainloss | 上期汇兑损益（废弃） | numeric | 23 | 10 | √ | 0.0000000000 | 上期汇兑损益（废弃） |
| 13 | febuscostamt | 原币暂估成本金额 | numeric | 23 | 10 | √ | 0 | 原币暂估成本金额 |
| 14 | febuscostamtlocal | 调汇前暂估成本余额（本位币） | numeric | 23 | 10 | √ | 0 | 调汇前暂估成本余额（本位币） |
| 15 | fecurbusgainloss | 调汇暂估成本金额 | numeric | 23 | 10 | √ | 0 | 调汇暂估成本金额 |
| 16 | fspectype | 规格型号 | varchar | 512 |  | √ | ' ' | 规格型号 |
| 17 | fecurbuscostamtlocal | 调汇后暂估成本余额（本位币） | numeric | 23 | 10 | √ | 0 | 调汇后暂估成本余额（本位币） |
| 18 | fbalance | 原币余额 | numeric | 23 | 10 | √ | 0.0000000000 | 原币余额 |
| 19 | fcurgainloss | 调汇金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调汇金额 |
| 20 | flocalbalance | 调汇前余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 调汇前余额（本位币） |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_adjexch_pid |  | fid |
| 2 | pk_ap_adjexchbillentry |  | fentryid |
| 3 | idx_ap_adjexch_srcentryid |  | fsrcentryid |
| 4 | idx_ap_adjexch_entry_srcbillid |  | fsrcbillid |

---

## 应付调汇单-反写记录表 t_ap_adjexchbill_wb

- **表名称：** 应付调汇单-反写记录表
- **表名：** t_ap_adjexchbill_wb

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
| 1 | pk_ap_adjexchbill_wb |  | fentryid |
| 2 | idx_ap_adjexchbill_wb_fk |  | fid |

---

## 应付调汇单-关联追踪表 t_ap_adjexchbill_tc

- **表名称：** 应付调汇单-关联追踪表
- **表名：** t_ap_adjexchbill_tc

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
| 1 | pk_ap_adjexchbill_tc |  | fid |
| 2 | idx_ap_adjexchbill_tc_tbill |  | ftbillid |
| 3 | idx_ap_adjexchbill_tc_tid |  | ftid |
