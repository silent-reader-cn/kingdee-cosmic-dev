# 票据业务处理单-cdm_drafttradebill

## 票据业务处理单-关联追踪表 t_cdm_drafttradebill_tc

- **表名称：** 票据业务处理单-关联追踪表
- **表名：** t_cdm_drafttradebill_tc

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
| 1 | t_cdm_drafttradebill_tc_pkey |  | fid |
| 2 | idx_cdm_drafttradebill_tc_tbill |  | ftbillid |
| 3 | idx_cdm_drafttradebill_tc_tid |  | ftid |
| 4 | idx_drafttradebill_tc_tbill |  | ftbillid |

---

## 拆分票据-子表 t_cdm_drafttrdbill_subbil

- **表名称：** 拆分票据-子表
- **表名：** t_cdm_drafttrdbill_subbil

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fe_subbillamount | 票面金额(子票包金额) | numeric | 19 | 6 | √ | 0 | 票面金额(子票包金额) |
| 3 | fe_subbillsrange | 子票包区间 | varchar | 50 |  | √ | ' ' | 子票包区间 |
| 4 | fe_billamt | 母票金额 | numeric | 19 | 6 | √ | 0 | 母票金额 |
| 5 | fe_draftbill | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fe_transtatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态 |
| 8 | fe_subbillstartflag | 子票包开始标识 | int8 | 64 |  | √ | 0 | 子票包开始标识 |
| 9 | fe_subdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 |
| 10 | fe_subbillendflag | 子票包结束标识 | int8 | 64 |  | √ | 0 | 子票包结束标识 |
| 11 | fe_oldstatus | 票据旧状态 | varchar | 30 |  | √ | ' ' | 票据旧状态 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fe_subbillquantity | 子票包数量 | int8 | 64 |  | √ | 0 | 子票包数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_drafttrdbill_subbil_fid |  | fid |
| 2 | pk_t_cdm_drafttrdbill_subbil |  | fentryid |

---

## 关联子实体-子表 t_cdm_drafttradebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cdm_drafttradebill_lk

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
| 1 | idx_drafttradebill_lk_fid |  | fid |
| 2 | t_cdm_drafttradebill_lk_pkey |  | fpkid |

---

## 票据业务处理单-多语言表 t_cdm_drafttradebill_l

- **表名称：** 票据业务处理单-多语言表
- **表名：** t_cdm_drafttradebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_drafttradebill_l_fid |  | fid,flocaleid |
| 2 | t_cdm_drafttradebill_l_pkey |  | fpkid |

---

## 保证金明细-子表 t_cdm_depositentry

- **表名称：** 保证金明细-子表
- **表名：** t_cdm_depositentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdpbillnos_tag | 票据号码_详情 | text | 0 |  | √ | ' ' | 票据号码_详情 |
| 3 | fdpdeductamount | 抵扣保证金金额 | numeric | 19 | 6 | √ | 0 | 抵扣保证金金额 |
| 4 | fguarantway | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: deposit :保证金 |
| 5 | fdpremainamount | 保证金剩余金额 | numeric | 19 | 6 | √ | 0 | 保证金剩余金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdepositbillno | 单据编号 | int8 | 64 |  | √ | 0 | 保证金存入处理F7 fbd_suretybill_f7 |
| 8 | fdp_source | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: gm :担保管理 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdpbillnos | 票据号码 | varchar | 255 |  | √ | ' ' | 票据号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_depositentry |  | fentryid |
| 2 | idx_cdm_depositentry |  | fid |

---

## 贴现利息明细-子表 t_cdm_discountentry

- **表名称：** 贴现利息明细-子表
- **表名：** t_cdm_discountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdis_days | 贴现调整天数 | int4 | 32 |  | √ | 0 | 贴现调整天数 |
| 3 | fdis_discamt | 贴现收款金额 | numeric | 16 | 9 | √ | 0 | 贴现收款金额 |
| 4 | fdis_interest | 实付贴现利息 | numeric | 16 | 9 | √ | 0 | 实付贴现利息 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdis_selectbillid | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |
| 8 | fdis_roughlyinterest | 匡算贴现利息 | numeric | 16 | 9 | √ | 0 | 匡算贴现利息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_discountentry |  | fid |
| 2 | pk_t_cdm_discountentry |  | fentryid |

---

## 票据业务处理单-反写记录表 t_cdm_drafttradebill_wb

- **表名称：** 票据业务处理单-反写记录表
- **表名：** t_cdm_drafttradebill_wb

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
| 1 | t_cdm_drafttradebill_wb_pkey |  | fentryid |
| 2 | idx_drafttradebill_wb_fid |  | fid |

---

## 关联子实体-子表 t_cdm_drafttrdbill_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cdm_drafttrdbill_entry_lk

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
| 1 | idx_cdm_drafttrdbill_entry_lk_fk |  | fentryid |
| 2 | pk_cdm_drafttrdbill_entry_lk |  | fpkid |

---

## 单据体-子表 t_cdm_drafttrdbill_entry

- **表名称：** 单据体-子表
- **表名：** t_cdm_drafttrdbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foldstatus | 票据旧状态 | varchar | 30 |  | √ | ' ' | 票据旧状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | 票据登记 cdm_draftbillf7 |
| 6 | ftranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_drafttrdbill_entry_pkey |  | fentryid |
| 2 | idx_drafttrdbill_entry_fid |  | fid |

---

## 票据业务处理单-主表 t_cdm_drafttradebill

- **表名称：** 票据业务处理单-主表
- **表名：** t_cdm_drafttradebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiscount_days | 贴现调整天数 | int4 | 32 |  |  | null | 贴现调整天数 |
| 3 | frecbodyid | 受理机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 4 | fpledgeebase | 质权人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 5 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | frecbodyname | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | 授信类别 cfm_credittype |
| 10 | frate | 贴现利率（%） | numeric | 19 | 6 | √ | 0.000000 | 贴现利率（%） |
| 11 | fdraftbilltranstatus | 票据交易状态 | varchar | 50 |  |  | null | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 porsuccess :部分成功 failing :交易失败 |
| 12 | fpledgeeaccount | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 13 | fdraftcount | 票据张数 | varchar | 30 |  | √ | '0' | 票据张数 |
| 14 | fdepositaccountid | 保证金账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | bankcode | 被背书人开户行行号 | varchar | 100 |  | √ | ' ' | 被背书人开户行行号 |
| 17 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 18 | fpledgeeaccounttext | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 19 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 20 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: |
| 21 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 S :已作废 |
| 22 | fpoundage | 手续费 | numeric | 19 | 6 |  | null | 手续费 |
| 23 | fdeposit | 划扣保证金 | bpchar | 1 |  | √ | '0' | 划扣保证金 |
| 24 | fpledgeeopenbanknumber | 质权人开户行行号 | varchar | 100 |  | √ | ' ' | 质权人开户行行号 |
| 25 | fpayeetype | 被背书人基础资料类型 | varchar | 80 |  | √ | ' ' | 被背书人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 |
| 26 | fvouchernum | 凭证号 | varchar | 150 |  |  | ' ' | 凭证号 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 29 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 30 | fdeductamount | 抵扣保证金金额 | numeric | 19 | 6 | √ | 0 | 抵扣保证金金额 |
| 31 | froughly_interest | 匡算贴现利息金额 | numeric | 19 | 6 | √ | 0 | 匡算贴现利息金额 |
| 32 | fisvoucher | 已生成凭证 | bpchar | 1 |  |  | '0' | 已生成凭证 |
| 33 | fdiscamt | 贴现收款金额 | numeric | 19 | 6 | √ | 0.000000 | 贴现收款金额 |
| 34 | fbankid | 被背书人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fiseditdiscountentry | 编辑贴现利息明细 | bpchar | 1 |  | √ | '0' | 编辑贴现利息明细 |
| 37 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 38 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fbankaccountid | 银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 40 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 41 | fpledgeetypebase | 质权人基础资料类型 | varchar | 50 |  | √ | ' ' | 质权人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 bd_finorginfo :合作金融机构 |
| 42 | ftradetype | 业务处理 | varchar | 30 |  | √ | ' ' | 业务处理,枚举: endorse :背书转让 discount :票据贴现 pledge :票据质押 rlspledge :质押解除 collect :票据托收 trusteeship :票据托管 retrieve :托管取回 refund :票据退票 payoff :票据解付 billsplit :票据拆分 payinterest :买方付息 |
| 43 | famount | 合计金额 | numeric | 19 | 6 | √ | 0.000000 | 合计金额 |
| 44 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: hand :手工登记 cas :出纳 bei :银企互联 cdm-draftallocate :票据调度 receiablebill :收票登记 payablebill :开票登记 repay :失败重付 bizapply :票据业务申请 |
| 45 | fbankacct | 被背书人银行账号 | varchar | 80 |  | √ | ' ' | 被背书人银行账号 |
| 46 | fcollection | 收款金额 | numeric | 19 | 6 |  | null | 收款金额 |
| 47 | fisreverserec | 红冲原收款 | bpchar | 1 |  | √ | '0' | 红冲原收款 |
| 48 | fstatus | 数据状态(用于对应F7) | varchar | 80 |  | √ | ' ' | 数据状态(用于对应F7),枚举: C :已审核 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fpledgeetext | 质权人 | varchar | 100 |  | √ | ' ' | 质权人 |
| 51 | fisonlinecalc | 线上清算 | bpchar | 1 |  | √ | '0' | 线上清算 |
| 52 | fdiscount_interest | 实付贴现利息金额 | numeric | 19 | 6 |  | null | 实付贴现利息金额 |
| 53 | fpayeetypetext | 被背书人类型 | varchar | 80 |  | √ | ' ' | 被背书人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 54 | felectag | 提交电票 | bpchar | 1 |  |  | null | 提交电票 |
| 55 | fisrepay | 是否失败重付 | bpchar | 1 |  |  | '0' | 是否失败重付 |
| 56 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 57 | fdepositdeduct | 保证金抵扣 | bpchar | 1 |  | √ | '0' | 保证金抵扣 |
| 58 | fbizfinishdate | 业务完成日期 | timestamp | 0 |  |  | null | 业务完成日期 |
| 59 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 60 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他 bd_finorginfo :金融机构 |
| 61 | finterestday | 利率转换天数 | varchar | 30 |  | √ | ' ' | 利率转换天数,枚举: 360 :360 365 :365 |
| 62 | fcontractno | 质押合同号 | varchar | 80 |  | √ | ' ' | 质押合同号 |
| 63 | fbeendorsorid | 被背书人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 64 | fcreditlimited | 占用授信 | int8 | 64 |  | √ | 0 | 授信额度管理 cfm_creditlimit |
| 65 | fallocbillentryid | 票据池调度分录ID | int8 | 64 |  | √ | 0 | 票据池调度分录ID |
| 66 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 67 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 68 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 69 | fbeendorsortext | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 70 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 71 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 72 | fdepositamount | 划扣保证金金额 | numeric | 19 | 6 | √ | 0 | 划扣保证金金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_drafttradebill_pkey |  | fid |
| 2 | idx_drafttradebill_billno |  | fbillno |
| 3 | idx_cdm_drafttrad_allocentid |  | fallocbillentryid |
