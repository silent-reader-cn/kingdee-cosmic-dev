# 票据业务处理单-cdm_drafttradebill

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
| 7 | fdepositbillno | 单据编号 | int8 | 64 |  | √ | 0 | [保证金存入处理F7 fbd_suretybill_f7](../fbd_files/fbd_suretybill_f7.md) |
| 8 | fdp_source | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: gm :担保管理 |
| 9 | fdinterestamount | 利息金额 | numeric | 23 | 10 | √ | 0 | 利息金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdpbillnos | 票据号码 | varchar | 255 |  | √ | ' ' | 票据号码 |

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

## 票据业务处理单-主表 t_cdm_drafttradebill

- **表名称：** 票据业务处理单-主表
- **表名：** t_cdm_drafttradebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 3 | fdiscount_days | 贴现调整天数 | int4 | 32 |  |  | null | 贴现调整天数 |
| 4 | frecbodyid | 受理机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 5 | fpledgeebase | 质权人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 7 | fisrejectrefundgen | 拒收退票生成 | bpchar | 1 |  | √ | '0' | 拒收退票生成 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | frecbodyname | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 12 | frate | 贴现利率（%） | numeric | 19 | 6 | √ | 0.000000 | 贴现利率（%） |
| 13 | fallbillsamount | 票据总金额 | numeric | 19 | 6 | √ | 0 | 票据总金额 |
| 14 | fdraftbilltranstatus | 票据交易状态 | varchar | 50 |  |  | null | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 porsuccess :部分成功 failing :交易失败 |
| 15 | fisfaildiscount | 贴现失败打回 | bpchar | 1 |  | √ | '0' | 贴现失败打回 |
| 16 | fpledgeeaccount | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 17 | fdraftcount | 票据张数 | varchar | 30 |  | √ | '0' | 票据张数 |
| 18 | fdepositaccountid | 保证金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | bankcode | 被背书人开户行行号 | varchar | 100 |  | √ | ' ' | 被背书人开户行行号 |
| 21 | fpledgeeopenbank | 质权人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 22 | fpledgeeaccounttext | 质权人银行账号 | varchar | 100 |  | √ | ' ' | 质权人银行账号 |
| 23 | fsettleway | 电票结算方式 | varchar | 50 |  | √ | ' ' | 电票结算方式,枚举: ST01 :票款兑付 ST02 :纯票过户 |
| 24 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 25 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: |
| 26 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 S :已作废 |
| 27 | fpoundage | 手续费 | numeric | 19 | 6 |  | null | 手续费 |
| 28 | fdeposit | 划扣保证金 | bpchar | 1 |  | √ | '0' | 划扣保证金 |
| 29 | fpledgeeopenbanknumber | 质权人开户行行号 | varchar | 100 |  | √ | ' ' | 质权人开户行行号 |
| 30 | fpayeetype | 被背书人基础资料类型 | varchar | 80 |  | √ | ' ' | 被背书人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 31 | fvouchernum | 凭证号 | varchar | 150 |  |  | ' ' | 凭证号 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 34 | fpledgeenddate | 质押到期日期 | timestamp | 0 |  |  | null | 质押到期日期 |
| 35 | fdeductamount | 抵扣保证金金额 | numeric | 19 | 6 | √ | 0 | 抵扣保证金金额 |
| 36 | froughly_interest | 匡算贴现利息金额 | numeric | 19 | 6 | √ | 0 | 匡算贴现利息金额 |
| 37 | fisvoucher | 已生成凭证 | bpchar | 1 |  |  | '0' | 已生成凭证 |
| 38 | fdiscamt | 贴现收款金额 | numeric | 19 | 6 | √ | 0.000000 | 贴现收款金额 |
| 39 | fbankid | 被背书人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fiseditdiscountentry | 编辑贴现利息明细 | bpchar | 1 |  | √ | '0' | 编辑贴现利息明细 |
| 42 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 43 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fbankaccountid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 45 | frefunddesc | 退票原因 | varchar | 50 |  | √ | ' ' | 退票原因 |
| 46 | fpledgeetypebase | 质权人基础资料类型 | varchar | 50 |  | √ | ' ' | 质权人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 bd_finorginfo :合作金融机构 cas_othercontactunit :其他往来单位 |
| 47 | fisdrawfail | 是否确认失败 | bpchar | 1 |  | √ | '0' | 是否确认失败 |
| 48 | ftradetype | 业务处理 | varchar | 30 |  | √ | ' ' | 业务处理,枚举: endorse :背书转让 discount :票据贴现 pledge :票据质押 rlspledge :质押解除 collect :票据托收 trusteeship :票据托管 retrieve :托管取回 refund :票据退票 payoff :票据解付 billsplit :票据拆分 payinterest :买方付息 |
| 49 | fisrejectrefund | 是否拒收退票 | bpchar | 1 |  | √ | '0' | 是否拒收退票 |
| 50 | famount | 合计金额 | numeric | 19 | 6 | √ | 0.000000 | 合计金额 |
| 51 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: hand :手工登记 cas :出纳 bei :银企互联 cdm-draftallocate :票据调度 receiablebill :收票登记 payablebill :开票登记 repay :失败重付 bizapply :票据业务申请 |
| 52 | fbankacct | 被背书人银行账号 | varchar | 80 |  | √ | ' ' | 被背书人银行账号 |
| 53 | fcollection | 收款金额 | numeric | 19 | 6 |  | null | 收款金额 |
| 54 | fisreverserec | 红冲原收款 | bpchar | 1 |  | √ | '0' | 红冲原收款 |
| 55 | fstatus | 数据状态(用于对应F7) | varchar | 80 |  | √ | ' ' | 数据状态(用于对应F7),枚举: C :已审核 |
| 56 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 57 | fpledgeetext | 质权人 | varchar | 100 |  | √ | ' ' | 质权人 |
| 58 | fisonlinecalc | 线上清算 | bpchar | 1 |  | √ | '0' | 线上清算 |
| 59 | fdiscount_interest | 实付贴现利息金额 | numeric | 19 | 6 |  | null | 实付贴现利息金额 |
| 60 | fpayeetypetext | 被背书人类型 | varchar | 80 |  | √ | ' ' | 被背书人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 other :其他 |
| 61 | felectag | 提交电票 | bpchar | 1 |  |  | null | 提交电票 |
| 62 | fisrepay | 是否失败重付 | bpchar | 1 |  |  | '0' | 是否失败重付 |
| 63 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | fdepositdeduct | 保证金抵扣 | bpchar | 1 |  | √ | '0' | 保证金抵扣 |
| 65 | fbizfinishdate | 业务完成日期 | timestamp | 0 |  |  | null | 业务完成日期 |
| 66 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 67 | fdeducttype | 抵扣类型 | varchar | 5 |  | √ | ' ' | 抵扣类型,枚举: 1 :本息抵扣 2 :本金抵扣 |
| 68 | fisalldiscount | 贴现全额到账 | bpchar | 1 |  | √ | '0' | 贴现全额到账 |
| 69 | fbusicontractno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |
| 70 | fpledgeetype | 质权人类型 | varchar | 50 |  | √ | ' ' | 质权人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他 bd_finorginfo :金融机构 |
| 71 | finterestday | 利率转换天数 | varchar | 30 |  | √ | ' ' | 利率转换天数,枚举: 360 :360 365 :365 |
| 72 | fcontractno | 质押合同号 | varchar | 80 |  | √ | ' ' | 质押合同号 |
| 73 | fisrepaygen | 失败重付生成 | bpchar | 1 |  | √ | '0' | 失败重付生成 |
| 74 | fbeendorsorid | 被背书人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 75 | fcleartype | 电票清算类型 | varchar | 50 |  | √ | ' ' | 电票清算类型,枚举: CT01 :全额清算 CT02 :净额清算 |
| 76 | fcreditlimited | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 77 | fallocbillentryid | 票据池调度分录ID | int8 | 64 |  | √ | 0 | 票据池调度分录ID |
| 78 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 79 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 80 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 81 | fbeendorsortext | 被背书人 | varchar | 512 |  | √ | ' ' | 被背书人 |
| 82 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 83 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 84 | fdepositamount | 划扣保证金金额 | numeric | 19 | 6 | √ | 0 | 划扣保证金金额 |

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

---

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
| 5 | fe_draftbill | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
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

## 票据业务处理单-分表 t_cdm_drafttradebill_e

- **表名称：** 票据业务处理单-分表
- **表名：** t_cdm_drafttradebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisequalsplit | 等分化拆分 | bpchar | 1 |  | √ | '1' | 等分化拆分 |
| 3 | fpooldepositamount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 4 | falldiscountinterest | 实付贴现利息合计 | numeric | 19 | 6 | √ | 0 | 实付贴现利息合计 |
| 5 | fowndiscountinterest | 本方实付贴现利息金额（试算） | numeric | 19 | 6 | √ | 0 | 本方实付贴现利息金额（试算） |
| 6 | fequalamount | 等分化金额 | numeric | 23 | 10 | √ | 0 | 等分化金额 |
| 7 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fagreerate | 协议付息比例(%) | numeric | 19 | 6 | √ | 100 | 协议付息比例(%) |
| 9 | fpoolprotocolid | 票据池 | int8 | 64 |  | √ | 0 | [银行票据池协议 cdm_pool_protocol](../cdm_files/cdm_pool_protocol.md) |
| 10 | fpayinterestamount | 付息人承担贴现利息 | numeric | 19 | 6 | √ | 0 | 付息人承担贴现利息 |
| 11 | fpooldepositactid | 票据池保证金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 12 | foppaccname | 对手方账户名称 | varchar | 255 |  | √ | ' ' | 对手方账户名称 |
| 13 | freleaseamount | 释放金额 | numeric | 23 | 10 | √ | 0 | 释放金额 |
| 14 | fpayinteramount_bank | 付息人承担贴现利息（试算） | numeric | 19 | 6 | √ | 0 | 付息人承担贴现利息（试算） |
| 15 | fagreepayertype | 协议付息人类型 | varchar | 50 |  | √ | ' ' | 协议付息人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 other :其他 |
| 16 | fisgenbysplit | 是否等分化生成 | bpchar | 1 |  | √ | '0' | 是否等分化生成 |
| 17 | fisrelpool | 是否关联票据池 | bpchar | 1 |  | √ | '0' | 是否关联票据池 |
| 18 | fpayerofinterest | 付息人 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 19 | fpayinterbankaccount | 付息人银行账号 | varchar | 255 |  | √ | ' ' | 付息人银行账号 |
| 20 | fpayinteropenbank | 付息人账号开户行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 21 | fpoolamount | 票据质押金额 | numeric | 23 | 10 | √ | 0 | 票据质押金额 |
| 22 | fispaybyagree | 协议付息 | bpchar | 1 |  | √ | '0' | 协议付息 |
| 23 | feuqaldifferetype | 上游等分化业务类型 | varchar | 50 |  | √ | ' ' | 上游等分化业务类型 |
| 24 | fpayerofinterestname | 付息人 | varchar | 255 |  | √ | ' ' | 付息人 |
| 25 | fpayerofinteresttype | 协议付息人基础资料类型 | varchar | 80 |  | √ | ' ' | 协议付息人基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :公司 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cdm_drafttradebill_e |  | fid |

---

## 贴现利息明细-子表 t_cdm_discountentry

- **表名称：** 贴现利息明细-子表
- **表名：** t_cdm_discountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdis_days | 贴现调整天数 | int4 | 32 |  | √ | 0 | 贴现调整天数 |
| 3 | fdis_payinterestamount | 付息人承担贴现利息 | numeric | 19 | 6 | √ | 0 | 付息人承担贴现利息 |
| 4 | fdis_discamt | 贴现收款金额 | numeric | 23 | 10 |  | 0 | 贴现收款金额 |
| 5 | fdis_interest | 实付贴现利息 | numeric | 23 | 10 |  | 0 | 实付贴现利息 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdis_subamount | 子票包金额 | numeric | 23 | 10 | √ | 0 | 子票包金额 |
| 8 | fdis_payinterest_bank | 付息人承担贴现利息(试算) | numeric | 19 | 6 | √ | 0 | 付息人承担贴现利息(试算) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdis_selectbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
| 11 | fdis_owninterest_bank | 本方实付贴现利息金额(试算) | numeric | 19 | 6 | √ | 0 | 本方实付贴现利息金额(试算) |
| 12 | fdis_roughlyinterest | 匡算贴现利息 | numeric | 23 | 10 |  | 0 | 匡算贴现利息 |

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
| 2 | fisneedsplit | 是否等分化数据 | bpchar | 1 |  | √ | '0' | 是否等分化数据 |
| 3 | fisnotneedgen | 收付协同生成 | bpchar | 1 |  | √ | '0' | 收付协同生成 |
| 4 | foldelestatus | 操作前电票状态 | varchar | 80 |  | √ | ' ' | 操作前电票状态,枚举: invoice :提示收票待签收 recite :背书待签收 invoicesigned :提示收票已签收 recitesigned :背书已签收 releaseofpledgesigned :提示出票已签收 innit :初始状态 acceptance :提示承兑待签收 registed :出票已登记 acceptancesigned :提示承兑已签收 ensure :保证待签收 releaseofedgsigned :质押解除已签收 notediscount :买断式贴现待签收 notediscountsigned :买断式贴现已签收 pledge :质押待签收 pledgesigned :质押已签收 releaseofpledge :质押解除待签收 relasepledgesigned :质押解除已签收 paymentsigned :提示付款已签收 paymentrefused :提示付款已拒收 searchfor :拒付追索待清偿 promisesearchfor :拒付追索同意清偿待签收 promisesearchforsigned :拒付追索同意清偿已签收 destroy :票据已作废 closedaccount :票据已结清 payment :提示付款待签收 CS01 :已出票 CS02 :已承兑 CS03 :已收票 CS04 :已到期 CS05 :已终止 CS06 :已结清 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fisrejectrefund | 是否拒收退票 | bpchar | 1 |  | √ | '0' | 是否拒收退票 |
| 7 | fedraftbillacct | 票据账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 8 | ftranstatus | 票据交易状态 | varchar | 30 |  | √ | ' ' | 票据交易状态,枚举: pending :准备提交 handleing :电票处理中 success :交易成功 failing :交易失败 |
| 9 | fchangeflag | 换票 | bpchar | 1 |  |  | '0' | 换票 |
| 10 | fbilltradelogid | 票据交易记录 | int8 | 64 |  | √ | 0 | 票据交易记录 |
| 11 | foldstatus | 票据旧状态 | varchar | 30 |  | √ | ' ' | 票据旧状态,枚举: registered :已登记 pledged :已质押 collocated :已托管 |
| 12 | fs_billamount | 转让金额 | numeric | 23 | 10 | √ | 0 | 转让金额 |
| 13 | fisinchange | 是否换票中 | bpchar | 1 |  | √ | '0' | 是否换票中 |
| 14 | fdraftreleaseamount | 释放金额 | numeric | 23 | 10 | √ | 0 | 释放金额 |
| 15 | fisrepay | 是否失败重付 | bpchar | 1 |  | √ | '0' | 是否失败重付 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
| 18 | fdraftdepositamount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 19 | fe_bankmsg | 银行返回信息 | varchar | 2000 |  | √ | ' ' | 银行返回信息 |
| 20 | fdraftpoolamount | 票据质押金额 | numeric | 23 | 10 | √ | 0 | 票据质押金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_drafttrdbill_entry_pkey |  | fentryid |
| 2 | idx_drafttrdbill_entry_fid |  | fid |
