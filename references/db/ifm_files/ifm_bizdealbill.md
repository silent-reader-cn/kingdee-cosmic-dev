# 贷款业务受理-ifm_bizdealbill

## 担保信息分录-子表 t_gm_guaranteeuse_info

- **表名称：** 担保信息分录-子表
- **表名：** t_gm_guaranteeuse_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgcreditortext | fgcreditortext | varchar | 80 |  | √ | ' ' |  |
| 3 | fgcreditguarantee | 是否额度担保 | bpchar | 1 |  | √ | '0' | 是否额度担保 |
| 4 | fgsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fgcontractcurrency | 担保合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 8 | fgcreditorid | fgcreditorid | int8 | 64 |  | √ | 0 |  |
| 9 | fgcontractid | 担保合同编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 10 | fgsrcbilltype | 来源单据 | varchar | 80 |  | √ | ' ' | 来源单据 |
| 11 | fgcurrencyid | fgcurrencyid | int8 | 64 |  | √ | 0 |  |
| 12 | fgstatus | 状态 | varchar | 80 |  | √ | ' ' | 状态,枚举: A :担保中 C :已解除 |
| 13 | fgexchrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 14 | fgratio | 担保比例(%) | numeric | 19 | 6 | √ | 0 | 担保比例(%) |
| 15 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fgcreditortype | fgcreditortype | varchar | 50 |  | √ | ' ' |  |
| 18 | fgcontractamount | 担保合同金额 | numeric | 19 | 6 | √ | 0 | 担保合同金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteeuse_info_efid |  | fid |
| 2 | pk_t_gm_guaranteeuse_info |  | fentryid |

---

## 关联子实体-子表 t_ifm_bizdealbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_bizdealbill_lk

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
| 1 | pk_ifm_bizdealbill_lk |  | fpkid |
| 2 | idx_ifm_bizdealbill_lk_fk |  | fid |

---

## 贷款业务受理-多语言表 t_ifm_bizdealbill_l

- **表名称：** 贷款业务受理-多语言表
- **表名：** t_ifm_bizdealbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdealopinion | 受理意见 | varchar | 255 |  | √ | ' ' | 受理意见 |
| 3 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 4 | flimitclauseexplain | 限制性条款 | varchar | 255 |  | √ | ' ' | 限制性条款 |
| 5 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 6 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 7 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 9 | fsummary | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_bizdealbill_l |  | fpkid |
| 2 | idx_bizdealbill_l_fid |  | fid |

---

## 日历-多选基础资料表 t_ifm_bizdealbill_ca

- **表名称：** 日历-多选基础资料表
- **表名：** t_ifm_bizdealbill_ca

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
| 1 | idx_bizdealbill_ca_fid |  | fid |
| 2 | pk_t_ifm_bizdealbill_ca |  | fpkid |

---

## 贷款业务受理-主表 t_ifm_bizdealbill

- **表名称：** 贷款业务受理-主表
- **表名：** t_ifm_bizdealbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限(ymd) | varchar | 80 |  | √ | ' ' | 期限(ymd) |
| 3 | fappliamt | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 4 | fdealopinion | 受理意见 | varchar | 255 |  | √ | ' ' | 受理意见 |
| 5 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fnotdrawamount | 未提款金额 | numeric | 23 | 10 | √ | 0 | 未提款金额 |
| 7 | fsigndate | 合同签约日期 | timestamp | 0 |  |  | null | 合同签约日期 |
| 8 | frateadjustcycletype | 利率重置周期 | varchar | 80 |  | √ | ' ' | 利率重置周期,枚举: W :按周 M :按月 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | floanuseid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 11 | fenddate | 合同结束日期 | timestamp | 0 |  |  | null | 合同结束日期 |
| 12 | fdealuserid | 受理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcreditorid | 债权人 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 14 | fratefloatpoint | 利率浮动基点 | numeric | 23 | 10 | √ | 0 | 利率浮动基点 |
| 15 | ffloatingratio | 逾期利率浮动比例（%） | numeric | 23 | 10 | √ | 0 | 逾期利率浮动比例（%） |
| 16 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fotherexplain | 其他说明 | varchar | 255 |  | √ | ' ' | 其他说明 |
| 19 | ffinproductid | 结算中心贷款产品 | int8 | 64 |  | √ | 0 | [存贷款产品维护 ifm_ldproduct](../ifm_files/ifm_ldproduct.md) |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | floancontractbillid | 合同单据编号（基础资料） | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 23 | flimitclauseexplain | 限制性条款 | varchar | 255 |  | √ | ' ' | 限制性条款 |
| 24 | fcontractname | 合同名称 | varchar | 255 |  | √ | ' ' | 合同名称 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 27 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 28 | frepaymentway | 本金收回方式 | varchar | 80 |  | √ | ' ' | 本金收回方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 zdyhk :自定义还款 |
| 29 | fcreditortype | 债权人类型 | varchar | 80 |  | √ | ' ' | 债权人类型,枚举: settlecenter :结算中心 |
| 30 | fstartdate | 合同开始日期 | timestamp | 0 |  |  | null | 合同开始日期 |
| 31 | fdealdate | 受理时间 | timestamp | 0 |  |  | null | 受理时间 |
| 32 | fcontractbillno | 合同单据编号 | varchar | 80 |  | √ | ' ' | 合同单据编号 |
| 33 | fbasis | 利率转换天数 | varchar | 80 |  | √ | ' ' | 利率转换天数,枚举: Actual_360 :Actual/360 Actual_365 :Actual/365 |
| 34 | fstageplanid | 本金收回方案 | int8 | 64 |  | √ | 0 | [还款计划方案 cfm_repayagingcheme](../cfm_files/cfm_repayagingcheme.md) |
| 35 | fdrawway | 借款人提款方式 | varchar | 80 |  | √ | ' ' | 借款人提款方式,枚举: once :一次性提款 stage :分期提款 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | faccountbankid | 借款人账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 38 | fpayinttype | 结息类别 | varchar | 80 |  | √ | ' ' | 结息类别,枚举: payinterst :付息 payprinandinte :还本付息 |
| 39 | fislimitclause | 是否有限制性条款 | bpchar | 1 |  | √ | '0' | 是否有限制性条款 |
| 40 | finteresttype | 利率类型 | varchar | 80 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 41 | frateadjustcycle | 利率重置周期值 | int4 | 32 |  | √ | 0 | 利率重置周期值 |
| 42 | fnotrepayamount | 未收回本金 | numeric | 23 | 10 | √ | 0 | 未收回本金 |
| 43 | fiscycleloan | 循环贷款 | bpchar | 1 |  | √ | '0' | 循环贷款 |
| 44 | fapplitype | 申请类型 | varchar | 80 |  | √ | ' ' | 申请类型,枚举: fin_apply :融资申请 loan_apply :提款申请 repay_apply :还款申请 int_apply :付息申请 extend_apply :展期申请 |
| 45 | famount | 借款金额 | numeric | 23 | 10 | √ | 0 | 借款金额 |
| 46 | fstartintdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 47 | fendinstdate | 结息日 | timestamp | 0 |  |  | null | 结息日 |
| 48 | factinterest | 实收利息 | numeric | 23 | 10 | √ | 0 | 实收利息 |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fsrcloanbillno | 还款单对应提款单号 | varchar | 80 |  | √ | ' ' | 还款单对应提款单号 |
| 51 | fapplidate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 52 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 53 | floanrate | 利率（%） | numeric | 23 | 10 | √ | 0 | 利率（%） |
| 54 | fsettleinstdate | 付息日 | timestamp | 0 |  |  | null | 付息日 |
| 55 | fbusinessstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: A :待受理 B :已受理 C :受理失败 D :已退单 |
| 56 | fdrawamount | 提款金额 | numeric | 23 | 10 | √ | 0 | 提款金额 |
| 57 | floandate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 58 | fratedeadline | 利率期限 | varchar | 80 |  | √ | ' ' | 利率期限 |
| 59 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 60 | frateadjustdate | 首次利率重置日 | timestamp | 0 |  |  | null | 首次利率重置日 |
| 61 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 62 | fcontractamt | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 63 | fguarantee | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 64 | fsettleintmode | 结息方式 | varchar | 80 |  | √ | ' ' | 结息方式,枚举: ykx :预扣息 lsbq :利随本清 gdpljx :固定频率结息 |
| 65 | frepayaccountid | 还款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 66 | fsettlecenterid | 结算中心 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 67 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 68 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 69 | fiscallint | 是否结息 | bpchar | 1 |  | √ | '0' | 是否结息 |
| 70 | fapplicatid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 71 | frepayamount | 收回本金 | numeric | 23 | 10 | √ | 0 | 收回本金 |
| 72 | floantype | 融资业务分类 | varchar | 80 |  | √ | ' ' | 融资业务分类,枚举: loan :普通贷款 entrust :委托贷款 sl :银团贷款 ec :企业往来 |
| 73 | fpredictinterest | 测算利息 | numeric | 23 | 10 | √ | 0 | 测算利息 |
| 74 | fsrcloanbillid | 还款单对应提款单id | int8 | 64 |  | √ | 0 | 还款单对应提款单id |
| 75 | fratetypeid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 76 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 77 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 78 | fdeductaccountid | 划扣资金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 79 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 80 | finterestsettledplanid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 81 | fcreditlimitid | 预占授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 82 | fratesign | 利率浮动基点（BP） | varchar | 80 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 83 | fsummary | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_bizdealbill_org |  | forgid |
| 2 | idx_ifm_bizdealbill_billno |  | fbillno |
| 3 | idx_ifm_bizdealbill_center |  | fsettlecenterid |
| 4 | pk_t_ifm_bizdealbill |  | fid |
| 5 | idx_ifm_bizdealbill_srcbillid |  | fsourcebillid |

---

## 贷款业务受理-关联追踪表 t_ifm_bizdealbill_tc

- **表名称：** 贷款业务受理-关联追踪表
- **表名：** t_ifm_bizdealbill_tc

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
| 1 | idx_ifm_bizdealbill_tc_tid |  | ftid |
| 2 | idx_ifm_bizdealbill_tc_tbill |  | ftbillid |
| 3 | pk_ifm_bizdealbill_tc |  | fid |

---

## 贷款业务受理-反写记录表 t_ifm_bizdealbill_wb

- **表名称：** 贷款业务受理-反写记录表
- **表名：** t_ifm_bizdealbill_wb

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
| 1 | pk_ifm_bizdealbill_wb |  | fentryid |
| 2 | idx_ifm_bizdealbill_wb_fk |  | fid |

---

## 单据体-子表 t_ifm_bizdealbill_int

- **表名称：** 单据体-子表
- **表名：** t_ifm_bizdealbill_int

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finstprincipal | 计息本金 | numeric | 23 | 10 | √ | 0 | 计息本金 |
| 3 | frate | 计息利率(%) | numeric | 23 | 10 | √ | 0 | 计息利率(%) |
| 4 | finststartdate | 计息开始日期 | timestamp | 0 |  |  | null | 计息开始日期 |
| 5 | finstdays | 计息天数 | int4 | 32 |  | √ | 0 | 计息天数 |
| 6 | fratetrandays | 利率转换天数 | int4 | 32 |  | √ | 0 | 利率转换天数 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | finstenddate | 计息结束日期 | timestamp | 0 |  |  | null | 计息结束日期 |
| 9 | finstamt | 利息金额 | numeric | 23 | 10 | √ | 0 | 利息金额 |
| 10 | finstctg | 利息类别 | varchar | 80 |  | √ | ' ' | 利息类别,枚举: normal :正常利息 extend :展期利息 overdue :逾期利息 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bizdealintentry_fid |  | fid |
| 2 | pk_t_ifm_bizdealbill_int |  | fentryid |
