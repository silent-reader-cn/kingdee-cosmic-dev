# 合同模板-cfm_loancontractbill

## 合同模板-反写记录表 t_cfm_loancontractbill_wb

- **表名称：** 合同模板-反写记录表
- **表名：** t_cfm_loancontractbill_wb

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
| 1 | pk_cfm_loancontractbill_wb |  | fentryid |
| 2 | idx_cfm_loancontractbill_wb_fk |  | fid |

---

## 合同模板-主表 t_cfm_loancontractbill

- **表名称：** 合同模板-主表
- **表名：** t_cfm_loancontractbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnotdrawamount | 未提款金额 | numeric | 19 | 6 | √ | 0.000000 | 未提款金额 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | floanuseid | 借款用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 6 | fenddate | 合同结束日期 | timestamp | 0 |  |  | null | 合同结束日期 |
| 7 | ffloatingratio | 逾期利率浮动比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 逾期利率浮动比例（%） |
| 8 | fisextend | 展期 | bpchar | 1 |  | √ | '0' | 展期 |
| 9 | fbillno | 合同单据编号 | varchar | 80 |  | √ | ' ' | 合同单据编号 |
| 10 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 11 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 12 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 13 | flendernature | 贷款人性质 | varchar | 30 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 14 | fconversiondays | fconversiondays | varchar | 30 |  | √ | ' ' |  |
| 15 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcontractstatus | 合同状态 | varchar | 30 |  | √ | ' ' | 合同状态,枚举: A :登记中 B :已登记 C :执行中 D :已结清 E :变更中 |
| 18 | flimitclauseexplain | 限制性条件说明 | varchar | 255 |  | √ | ' ' | 限制性条件说明 |
| 19 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | frepaymentway | 还款方式 | varchar | 30 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 23 | fextendstatus | 展期状态 | varchar | 30 |  | √ | ' ' | 展期状态,枚举: N :未展期 A :暂存 B :已提交 C :已审核 |
| 24 | fstartdate | 合同开始日期 | timestamp | 0 |  |  | null | 合同开始日期 |
| 25 | fnotpayinterestamount | 测算未付利息 | numeric | 19 | 6 | √ | 0.000000 | 测算未付利息 |
| 26 | finitid | 初始化id | int8 | 64 |  | √ | 0 | 初始化id |
| 27 | fstageplanid | 分期还款方案 | int8 | 64 |  | √ | 0 | [还款计划方案 cfm_repayagingcheme](../cfm_files/cfm_repayagingcheme.md) |
| 28 | fdrawway | 提款方式 | varchar | 30 |  | √ | ' ' | 提款方式,枚举: once :一次性 stage :分期 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | faccountbankid | 借款人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 31 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 32 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 33 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 34 | fislimitclause | 有限制性条款 | bpchar | 1 |  | √ | '0' | 有限制性条款 |
| 35 | finteresttype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 36 | fisclientloan | 是否委托贷款 | bpchar | 1 |  | √ | '0' | 是否委托贷款 |
| 37 | fnotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 38 | famount | 借款金额 | numeric | 19 | 6 | √ | 0.000000 | 借款金额 |
| 39 | fisinit | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 42 | fpayinterestamount | 已付利息 | numeric | 19 | 6 | √ | 0.000000 | 已付利息 |
| 43 | fdrawamount | 已提款金额 | numeric | 19 | 6 | √ | 0.000000 | 已提款金额 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fguarantee | 担保方式 | varchar | 300 |  |  | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 47 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 48 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 49 | frepayamount | 已还本金 | numeric | 19 | 6 | √ | 0.000000 | 已还本金 |
| 50 | fbizdate | 合同签约日期 | timestamp | 0 |  |  | null | 合同签约日期 |
| 51 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | finterestrate | 合同签订利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 合同签订利率（%） |
| 53 | finterestsettledplanid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 54 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 55 | fisoverdue | 逾期 | bpchar | 1 |  | √ | '0' | 逾期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loancontractbill_pkey |  | fid |
| 2 | idx_t_cfm_loancontractbill_bns |  | fbillno,fbillstatus |

---

## 项目分录-子表 t_cfm_loancontractbill_pj

- **表名称：** 项目分录-子表
- **表名：** t_cfm_loancontractbill_pj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目编号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_pj |  | fentryid |
| 2 | idx_cfm_loancontractbi_pj_fid |  | fid |

---

## 统借统还分录-子表 t_cfm_unify_loan_return

- **表名称：** 统借统还分录-子表
- **表名：** t_cfm_unify_loan_return

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuseamt | 用款金额 | numeric | 23 | 10 | √ | 0 | 用款金额 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :已置换 |
| 4 | floanbillid | 关联提款单号 | int8 | 64 |  | √ | 0 | [提款处理单 cfm_loanbill_f7](../cfm_files/cfm_loanbill_f7.md) |
| 5 | fgeneralrate | 综合利率 | numeric | 23 | 10 | √ | 0 | 综合利率 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_unify_loan_return |  | fentryid |
| 2 | index_cfm_unifyloanreturn |  | fid |

---

## 日历-多选基础资料表 t_cfm_loancontractbill_ca

- **表名称：** 日历-多选基础资料表
- **表名：** t_cfm_loancontractbill_ca

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工作日历 tbd_workcalendar](../fbd_files/tbd_workcalendar.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_ca |  | fpkid |
| 2 | idx_cfm_loanctract_ca_fid |  | fid |

---

## 供应链融资分录-子表 t_cfm_loancontractbill_sc

- **表名称：** 供应链融资分录-子表
- **表名：** t_cfm_loancontractbill_sc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexecutedate | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 3 | frelationtype | 关联类型 | varchar | 30 |  | √ | ' ' | 关联类型,枚举: PO :采购订单 SO :销售订单 |
| 4 | fbdpartnerid | 核心企业 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | forderno | 订单编号 | varchar | 50 |  | √ | ' ' | 订单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_sc |  | fentryid |
| 2 | t_cfm_loancontractb_sc_fid |  | fid |

---

## 合同模板-分表 t_cfm_loancontractbill_f

- **表名称：** 合同模板-分表
- **表名：** t_cfm_loancontractbill_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscycleloan | fiscycleloan | bpchar | 1 |  | √ | '0' |  |
| 3 | fisunifyloanreturn | 统借统还 | bpchar | 1 |  | √ | '0' | 统借统还 |
| 4 | frenewalexpiredate | 展期后合同到期日期 | timestamp | 0 |  |  | null | 展期后合同到期日期 |
| 5 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 6 | floanapplyid | 融资申请 | int8 | 64 |  | √ | 0 | [融资申请 cfm_loan_apply_f7](../cfm_files/cfm_loan_apply_f7.md) |
| 7 | fbizdealno | fbizdealno | varchar | 80 |  | √ | ' ' |  |
| 8 | fisunifydebit | 统借借入 | bpchar | 1 |  | √ | '0' | 统借借入 |
| 9 | fisunifycredit | 统借贷出 | bpchar | 1 |  | √ | '0' | 统借贷出 |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fenable | fenable | varchar | 30 |  | √ | '1' |  |
| 12 | fregion | 地域范围 | varchar | 80 |  | √ | ' ' | 地域范围,枚举: R1 :中国大陆 R2 :港澳台 R3 :境外 |
| 13 | fishandend | 手工结束合同 | bpchar | 1 |  | √ | '0' | 手工结束合同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loancontract_f_mid |  | floanapplyid |
| 2 | pk_cfm_loancontractbill_f |  | fid |

---

## 合同模板-多语言表 t_cfm_loancontractbill_l

- **表名称：** 合同模板-多语言表
- **表名：** t_cfm_loancontractbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 3 | flimitclauseexplain | 限制性条件说明 | varchar | 255 |  | √ | ' ' | 限制性条件说明 |
| 4 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 5 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 6 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loancontractbill_l_pkey |  | fpkid |
| 2 | idx_t_cfm_loancontractbill_l |  | fid,flocaleid |

---

## 银团分录-子表 t_cfm_loancontractbill_ba

- **表名称：** 银团分录-子表
- **表名：** t_cfm_loancontractbill_ba

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbankrole | 银团角色 | varchar | 30 |  | √ | ' ' | 银团角色,枚举: MB :管理行 PB :参与行 |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fbankentryid | fbankentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fshareamount | 份额金额 | numeric | 19 | 6 | √ | 0 | 份额金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcreditlimitid | 占用授信单号 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 9 | floanamount | floanamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | ffinorginfoid | 银行名称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loancontractbi_ba_fid |  | fid |
| 2 | pk_cfm_loancontractbill_ba |  | fentryid |

---

## 合同模板-分表 t_cfm_loancontractbill_e

- **表名称：** 合同模板-分表
- **表名：** t_cfm_loancontractbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscandefer | 是否允许展期 | bpchar | 1 |  | √ | '0' | 是否允许展期 |
| 3 | fterm | 期限(ymd) | varchar | 30 |  | √ | ' ' | 期限(ymd) |
| 4 | flenderapplyno | 融资借款申请 | varchar | 100 |  | √ | ' ' | 融资借款申请 |
| 5 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 6 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 8 | frateadjustcycletype | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 9 | fshortname | fshortname | varchar | 30 |  | √ | ' ' |  |
| 10 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fcreditorgid | 债权人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 14 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点 |
| 15 | fratingagencyid | fratingagencyid | int8 | 64 |  | √ | 0 |  |
| 16 | ftextdebtor | 借款人 | varchar | 255 |  | √ | ' ' | 借款人 |
| 17 | fotherexplain | fotherexplain | varchar | 255 |  | √ | ' ' |  |
| 18 | fratingscale | fratingscale | varchar | 30 |  | √ | ' ' |  |
| 19 | fissuemethodid | fissuemethodid | int8 | 64 |  | √ | 0 |  |
| 20 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 21 | flimitclauseexplain | flimitclauseexplain | varchar | 255 |  | √ | ' ' |  |
| 22 | fcontractname | fcontractname | varchar | 255 |  | √ | ' ' |  |
| 23 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 24 | ftextcreditor | 债权人 | varchar | 255 |  | √ | ' ' | 债权人 |
| 25 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 26 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 27 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 28 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_360 :Actual/360 Actual_365 :Actual/365 |
| 29 | fconfirmtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 30 | frateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 31 | funderwritemethod | funderwritemethod | varchar | 30 |  | √ | ' ' |  |
| 32 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: registrying :登记中 waitconfirm :待确认 yetconfirm :已确认 yetreturn :已退回 |
| 33 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 34 | freturnreason | 退回原因 | varchar | 255 |  | √ | ' ' | 退回原因 |
| 35 | fsettlestatus | 提交结算中心状态 | varchar | 80 |  | √ | ' ' | 提交结算中心状态,枚举: addnew :新增 submit :已提交 accept :已受理 bitback :已退回 |
| 36 | fbondtype | fbondtype | varchar | 30 |  | √ | ' ' |  |
| 37 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |
| 38 | frateresetadjustrule | 利率重置日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 利率重置日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 39 | frateadjustdate | 首次利率重置日 | timestamp | 0 |  |  | null | 首次利率重置日 |
| 40 | fissuemarketid | fissuemarketid | int8 | 64 |  | √ | 0 |  |
| 41 | fsettleintmode | 结息方式 | varchar | 30 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 42 | fcustodianfinorgid | fcustodianfinorgid | int8 | 64 |  | √ | 0 |  |
| 43 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 44 | fiscallint | 计息 | bpchar | 1 |  | √ | '0' | 计息 |
| 45 | floantype | 借款类型 | varchar | 30 |  | √ | ' ' | 借款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 46 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 47 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 49 | floaneracctbankid | 债权人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 50 | fpayintadjustrule | 付息日节假日规则 | varchar | 80 |  | √ | 'no_adjust' | 付息日节假日规则,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 51 | fratesign | 利率浮动基点（BP） | varchar | 30 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 52 | fcreditlimitid | 授信合同 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 53 | fratedeadlineid | fratedeadlineid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_loancontractbill_e |  | flender |
| 2 | idx_cfm_loancontract_eorgid |  | forgid |
| 3 | t_cfm_loancontractbill_e_pkey |  | fid |

---

## 提款计划单据体-子表 t_cfm_loancontractbill_dp

- **表名称：** 提款计划单据体-子表
- **表名：** t_cfm_loancontractbill_dp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplandrawdate | 预计提款日期 | timestamp | 0 |  |  | null | 预计提款日期 |
| 3 | fplandrawamt | 预计提款金额 | numeric | 19 | 6 | √ | 0 | 预计提款金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_dp |  | fentryid |
| 2 | idx_loancontractbill_dp_id |  | fid |

---

## 关联子实体-子表 t_cfm_loancontractbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_loancontractbill_lk

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
| 1 | pk_cfm_loancontractbill_lk |  | fpkid |
| 2 | idx_cfm_loancontractbill_lk_fk |  | fid |

---

## 贸融关联分录-子表 t_cfm_loancontractbill_tf

- **表名称：** 贸融关联分录-子表
- **表名：** t_cfm_loancontractbill_tf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelatebillno | 关联单据编号 | varchar | 50 |  | √ | ' ' | 关联单据编号 |
| 3 | fletter | 开证人 | varchar | 50 |  | √ | ' ' | 开证人 |
| 4 | frelationtype | 关联类型 | varchar | 30 |  | √ | ' ' | 关联类型,枚举: IO :进口订单 EO :出口订单 IL :进口信用证 EL :出口信用证 |
| 5 | fbeneficiary | 受益人 | varchar | 50 |  | √ | ' ' | 受益人 |
| 6 | frelatebillid | 关联单据id | int8 | 64 |  | √ | 0 | 关联单据id |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fexpiredate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 10 | frelatebilltype | frelatebilltype | varchar | 30 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | funpaidamount | 未付（收）金额 | numeric | 19 | 6 | √ | 0 | 未付（收）金额 |
| 13 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_loancontractbill_tf |  | fentryid |
| 2 | t_cfm_loancontractb_tf_fid |  | fid |

---

## 合同模板-关联追踪表 t_cfm_loancontractbill_tc

- **表名称：** 合同模板-关联追踪表
- **表名：** t_cfm_loancontractbill_tc

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
| 1 | idx_cfm_loancontractbill_tc_tid |  | ftid |
| 2 | pk_cfm_loancontractbill_tc |  | fid |
| 3 | idx_cfm_loancontractbill_tc_tbill |  | ftbillid |
