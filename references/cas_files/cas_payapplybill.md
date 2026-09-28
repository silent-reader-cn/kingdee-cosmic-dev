# 付款申请（已废弃）-cas_payapplybill

## 付款申请（已废弃）-主表 t_cas_payapplybill

- **表名称：** 付款申请（已废弃）-主表
- **表名：** t_cas_payapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplycause | 申请事由 | varchar | 512 |  | √ | ' ' | 申请事由 |
| 3 | fpaycurrencyid | 付款币别（弃用） | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fpayamount | 付款总额（弃用） | numeric | 19 | 6 | √ | 0.000000 | 付款总额（弃用） |
| 5 | fscheuser | 确认排款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fpaymentidentifyid | 付款标识 | int8 | 64 |  | √ | 0 | 付款标识 cas_paymentidentify |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率（弃用） | numeric | 23 | 10 | √ | 0.0000000000 | 汇率（弃用） |
| 9 | fpayeeamount | 收款总额 | numeric | 19 | 6 | √ | 0.000000 | 收款总额 |
| 10 | fquotation | 换算方式(废弃) | varchar | 30 |  | √ | '0' | 换算方式(废弃),枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fexratetableid | 汇率表（弃用） | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 13 | fpartpay | 部分付款 | bpchar | 1 |  | √ | '0' | 部分付款 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fpayeracctbankid | 付款账号（弃用） | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fpaidstatus | 付款状态 | varchar | 5 |  | √ | ' ' | 付款状态,枚举: A :未付款 B :付款中 C :已付款 D :已排款 |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fbackbillflag | 退单 | bpchar | 1 |  | √ | '0' | 退单 |
| 25 | fisdiffcur | 异币别付款（弃用） | bpchar | 1 |  | √ | '0' | 异币别付款（弃用） |
| 26 | fpartpaysche | 部分排款 | bpchar | 1 |  | √ | '0' | 部分排款 |
| 27 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 28 | fexratedate | 汇率日期（弃用） | timestamp | 0 |  |  | null | 汇率日期（弃用） |
| 29 | fpayeecurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | finvalidflag | 作废 | bpchar | 1 |  | √ | '0' | 作废 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fplanpaydate | 计划付款日期 | timestamp | 0 |  |  | null | 计划付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_payapplybill |  | fid |
| 2 | idx_cas_pab_dateorg |  | fpayorgid,fapplydate |
| 3 | idx_cas_pab_fbillno |  | fbillno |
| 4 | idx_cas_pab_billstatus |  | fbillstatus |

---

## 已付款明细分录-子表 t_cas_payapplypaidentry

- **表名称：** 已付款明细分录-子表
- **表名：** t_cas_payapplypaidentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaymentid | 付款单id | int8 | 64 |  | √ | 0 | 付款单id |
| 3 | fapplyid | 申请单分录id | int8 | 64 |  | √ | 0 | 申请单分录id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fwbtime | 反写时间 | timestamp | 0 |  |  | null | 反写时间 |
| 6 | fpayedamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pape_fpaymentid |  | fpaymentid |
| 2 | pk_t_cas_payapplypaidentry |  | fentryid |

---

## 关联子实体-子表 t_cas_payapplybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_payapplybill_lk

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
| 1 | idx_cas_payapplybill_lk_fk |  | fid |
| 2 | pk_cas_payapplybill_lk |  | fpkid |

---

## 业务明细分录-子表 t_cas_businessentry

- **表名称：** 业务明细分录-子表
- **表名：** t_cas_businessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fbuspayeeamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 5 | fmaterielfield | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fcontractnumber | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbusremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_businessentry |  | fentryid |
| 2 | t_cas_businessentry_ch |  | fid,fbuspayeeamount |

---

## 付款申请（已废弃）-关联追踪表 t_cas_payapplybill_tc

- **表名称：** 付款申请（已废弃）-关联追踪表
- **表名：** t_cas_payapplybill_tc

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
| 1 | idx_cas_payapplybill_tc_tid |  | ftid |
| 2 | idx_cas_payapplybill_tc_tbill |  | ftbillid |
| 3 | pk_cas_payapplybill_tc |  | fid |

---

## 票据结算号-多选基础资料表 t_cas_payapplybill_bl

- **表名称：** 票据结算号-多选基础资料表
- **表名：** t_cas_payapplybill_bl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 应收应付票据登记 cdm_payandrecdraft_f7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_payapplybill_bl |  | fpkid |
| 2 | t_cas_payapplybill_blid |  | fentryid,fbasedataid |

---

## 付款明细分录-子表 t_cas_payinfoentry

- **表名称：** 付款明细分录-子表
- **表名：** t_cas_payinfoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdraftamttotal | 票面金额合计 | numeric | 19 | 6 | √ | 0 | 票面金额合计 |
| 3 | farrivalno | 到单编号（隐藏） | int8 | 64 |  | √ | 0 | 到单编号（隐藏） |
| 4 | fpayee | 收款人基础资料(隐藏) | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fpaymentchannel | 支付渠道 | varchar | 50 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 6 | fpriority | 紧急程度 | varchar | 50 |  | √ | ' ' | 紧急程度,枚举: prior :优先 public :普通 defer :暂缓 |
| 7 | fpaybillno | 付款单 | varchar | 30 |  | √ | ' ' | 付款单 |
| 8 | fpaycurrencyid | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | frecaccbankname | 收款人实名 | varchar | 50 |  | √ | ' ' | 收款人实名 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0 | 付款金额 |
| 12 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 14 | fpaystatus | 付款状态 | varchar | 50 |  | √ | ' ' | 付款状态,枚举: A :已付款 B :付款中 C :未付款 D :已排款 E :已退单 |
| 15 | fpayeeamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 16 | fstatusexplain | 状态说明 | varchar | 255 |  | √ | ' ' | 状态说明 |
| 17 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 18 | fapplyid | 申请明细id（隐藏） | int8 | 64 |  | √ | 0 | 申请明细id（隐藏） |
| 19 | finvalid | 拒付 | bpchar | 1 |  | √ | '0' | 拒付 |
| 20 | flastmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 21 | fpayeraccbankid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 22 | flockedamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 23 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 24 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 25 | fpayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 26 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 27 | fbackbill | 退票 | bpchar | 1 |  | √ | '0' | 退票 |
| 28 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 29 | fpayeeaccbanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 30 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 31 | fpayeetype | 收款人类型 | varchar | 50 |  | √ | ' ' | 收款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他 |
| 32 | fisdosche | 是否确认排款 | bpchar | 1 |  | √ | '0' | 是否确认排款 |
| 33 | frecroutingnum | 收款银行Rounting Number | varchar | 50 |  | √ | ' ' | 收款银行Rounting Number |
| 34 | fpayeeid | 收款人ID | int8 | 64 |  | √ | 0 | 收款人ID |
| 35 | feaccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 36 | frecothercode | 收款银行其他代码 | varchar | 50 |  | √ | ' ' | 收款银行其他代码 |
| 37 | fisdiffcur | 异币别付款 | bpchar | 1 |  | √ | '0' | 异币别付款 |
| 38 | fpayeebank | 收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 39 | frecbanknumber | 收款银行联行号 | varchar | 50 |  | √ | ' ' | 收款银行联行号 |
| 40 | fsettletnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 41 | fbalance | 当前余额 | numeric | 19 | 6 | √ | 0.000000 | 当前余额 |
| 42 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 43 | fpaidamount | 已付款金额 | numeric | 19 | 6 | √ | 0.000000 | 已付款金额 |
| 44 | farrivalunlockamt | 到单未锁定金额 | numeric | 19 | 6 | √ | 0 | 到单未锁定金额 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 47 | frecswiftcode | 收款银行Swift Code | varchar | 50 |  | √ | ' ' | 收款银行Swift Code |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_payinfoentry |  | fentryid |
| 2 | idx_t_cas_payinfoentry |  | fid |
| 3 | t_cas_payinfoe_statb |  | fpaystatus,fpaybillno |

---

## 付款申请（已废弃）-反写记录表 t_cas_payapplybill_wb

- **表名称：** 付款申请（已废弃）-反写记录表
- **表名：** t_cas_payapplybill_wb

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
| 1 | pk_cas_payapplybill_wb |  | fentryid |
| 2 | idx_cas_payapplybill_wb_fk |  | fid |

---

## 申请明细分录-子表 t_cas_payapplyentry

- **表名称：** 申请明细分录-子表
- **表名：** t_cas_payapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fepayee | 收款人基础资料(隐藏) | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 3 | fepaydate | 期望付款日 | timestamp | 0 |  |  | null | 期望付款日 |
| 4 | fpriority | 紧急程度 | varchar | 50 |  | √ | ' ' | 紧急程度,枚举: prior :优先 public :普通 defer :暂缓 |
| 5 | fechgpayeeaccbankid | 变更收款账号ID | int8 | 64 |  | √ | 0 | 变更收款账号ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | felockedamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 8 | fchgstatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: A :未变更 B :变更中 C :已变更 |
| 9 | fechguseraccbank | 变更收款信息基础资料(隐藏) | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 10 | fechgpayeeaccbanknum | 变更后收款账号 | varchar | 255 |  | √ | ' ' | 变更后收款账号 |
| 11 | feuseraccbank | 收款信息基础资料(隐藏) | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 12 | fepayeeaccbankid | 收款账号ID | int8 | 64 |  | √ | 0 | 收款账号ID |
| 13 | fepayeeaccbanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 14 | fechgpayeeaccbank | 变更收款账号基础资料(隐藏) | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | fsettlementtypeid | 申请结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 16 | feremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 17 | fechgpayeebankid | 变更后收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 18 | fsplitid | 申请明细id | int8 | 64 |  | √ | 0 | 申请明细id |
| 19 | fepayeeamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 20 | fepayeetype | 收款人类型 | varchar | 100 |  | √ | ' ' | 收款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他 |
| 21 | feaccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 22 | fepaidamount | 已付款金额 | numeric | 19 | 6 | √ | 0.000000 | 已付款金额 |
| 23 | fepayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 24 | fepayeeid | 收款人ID | int8 | 64 |  | √ | 0 | 收款人ID |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fepayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 27 | fepayeeaccbank | 收款账号基础资料(隐藏) | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cas_payapplyentry |  | fentryid |
| 2 | idx_cas_pae_fid |  | fid |
| 3 | idx_cas_pae_fnum |  | fepayeeaccbanknum |
