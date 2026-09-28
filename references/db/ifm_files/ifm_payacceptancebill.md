# 内部结算受理-ifm_payacceptancebill

## 内部结算受理-反写记录表 t_ifm_payacceptance_wb

- **表名称：** 内部结算受理-反写记录表
- **表名：** t_ifm_payacceptance_wb

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
| 1 | pk_ifm_payacceptance_wb |  | fentryid |
| 2 | idx_ifm_payacceptance_wb_fk |  | fid |

---

## 内部结算受理-关联追踪表 t_ifm_payacceptance_tc

- **表名称：** 内部结算受理-关联追踪表
- **表名：** t_ifm_payacceptance_tc

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
| 1 | idx_ifm_payacceptance_tc_tbill |  | ftbillid |
| 2 | pk_ifm_payacceptance_tc |  | fid |
| 3 | idx_ifm_payacceptance_tc_tid |  | ftid |

---

## 内部结算受理-分表 t_ifm_payacceptance_e

- **表名称：** 内部结算受理-分表
- **表名：** t_ifm_payacceptance_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaymentmode | 付款方式 | varchar | 30 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 3 | facttradedate | facttradedate | timestamp | 0 |  |  | null |  |
| 4 | fapplyorgid | 申请付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fitempayeetypeid | 收款单位类型 | varchar | 30 |  | √ | ' ' | 收款单位类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 6 | fcommitbetime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 7 | fbankcheckflag | fbankcheckflag | varchar | 80 |  | √ | ' ' |  |
| 8 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :待受理 B :已受理 C :已退单 D :已付款 |
| 9 | fdetailseqid | fdetailseqid | varchar | 80 |  | √ | ' ' |  |
| 10 | fbankpayingid | 银行付款单ID | int8 | 64 |  | √ | 0 | 银行付款单ID |
| 11 | freason | 退单原因 | varchar | 255 |  | √ | ' ' | 退单原因 |
| 12 | fbackdate | 退单时间 | timestamp | 0 |  |  | null | 退单时间 |
| 13 | fispersonpay | 是否对私 | bpchar | 1 |  | √ | '0' | 是否对私 |
| 14 | fbankpaystatus | 银行付款单状态 | varchar | 5 |  | √ | ' ' | 银行付款单状态,枚举: OP :准备提交 OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 15 | fbackuserid | 退单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsbilltype | 源单单据类型 | varchar | 50 |  | √ | ' ' | 源单单据类型 |
| 17 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 18 | fiscommitbe | 是否提交银企 | bpchar | 1 |  | √ | '0' | 是否提交银企 |
| 19 | fentrustorgid | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbatchseqid | fbatchseqid | varchar | 80 |  | √ | ' ' |  |
| 21 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 22 | fitempayeeid | 收款单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fcashierid | 出纳 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_payacc_fbankpayingid |  | fbankpayingid |
| 2 | pk_ifm_payacceptance_e |  | fid |

---

## 关联子实体-子表 t_ifm_payacceptanceentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_payacceptanceentry_lk

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
| 1 | idx_ifm_payacceptanceentry_lk_fk |  | fentryid |
| 2 | pk_ifm_payacceptanceentry_lk |  | fpkid |

---

## 内部结算受理-主表 t_ifm_payacceptance

- **表名称：** 内部结算受理-主表
- **表名：** t_ifm_payacceptance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 成员单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpayeetypeid | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 other :其他 |
| 5 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 6 | fpayeeaccformid | 收款账户基础资料标识 | varchar | 30 |  | √ | ' ' | 收款账户基础资料标识 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpayeeformid | 收款人基础资料标识 | varchar | 30 |  | √ | ' ' | 收款人基础资料标识 |
| 9 | fpayeeacctbankid | 收款账户ID | int8 | 64 |  | √ | 0 | 收款账户ID |
| 10 | freccountryid | 收款方国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | factpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 13 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_paybill :付款单 |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fpayeebankname | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 18 | frecprovince | 收款方省 | varchar | 80 |  | √ | ' ' | 收款方省 |
| 19 | ftranstype | 交易类型 | varchar | 30 |  | √ | ' ' | 交易类型,枚举: 1 :内部代付 2 :内部转账 3 :内部划拨 4 :内部收款 5 :内部计息 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 notbei :非银企互联 |
| 22 | fagentfinorgid | 开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 23 | frecaccbankname | 收款账户名称 | varchar | 255 |  | √ | ' ' | 收款账户名称 |
| 24 | fpayerinneracctbankid | 付款账号 | int8 | 64 |  | √ | 0 | [内部账户管理 ifm_inneracct](../ifm_files/ifm_inneracct.md) |
| 25 | facceptuserid | facceptuserid | int8 | 64 |  | √ | 0 |  |
| 26 | fusage | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 27 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fpayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 29 | fpayeracctbankid | 付款账号（银行） | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 30 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 32 | fpayeebanknum | 收款账号 | varchar | 255 |  | √ | ' ' | 收款账号 |
| 33 | fagentfinorgcatid | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 34 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 35 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 36 | fexpectdate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 37 | fscorgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | freccity | 收款方市县 | varchar | 80 |  | √ | ' ' | 收款方市县 |
| 39 | fpayeeid | 收款人ID | int8 | 64 |  | √ | 0 | 收款人ID |
| 40 | fpayeecurrency | 收款账号币种 | int8 | 64 |  | √ | 0 | 收款账号币种 |
| 41 | fisdiffcur | 异币种付款 | bpchar | 1 |  | √ | '0' | 异币种付款 |
| 42 | fagentpayeraccname | fagentpayeraccname | varchar | 255 |  | √ | ' ' |  |
| 43 | frecbanknumber | 收款账户联行号 | varchar | 30 |  | √ | ' ' | 收款账户联行号 |
| 44 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 45 | facceptdatetime | facceptdatetime | timestamp | 0 |  |  | null |  |
| 46 | fsettletnumber | 结算号 | varchar | 30 |  | √ | ' ' | 结算号 |
| 47 | fagentpayeraccountid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 48 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 49 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 50 | fpaymenttypeid | 付款用途 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 51 | fcurrencyid | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_payacceptance |  | fid |
| 2 | idx_ifm_payacc_fscorgid |  | fscorgid |

---

## 分录-子表 t_ifm_payacceptanceentry

- **表名称：** 分录-子表
- **表名：** t_ifm_payacceptanceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率（%） | numeric | 19 | 6 | √ | 0.000000 | 税率（%） |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | frefunddes | 退款说明 | varchar | 255 |  |  | null | 退款说明 |
| 5 | fdiscountamount | 现金折扣 | numeric | 19 | 6 | √ | 0.000000 | 现金折扣 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcorebillno | 核心单据号 | varchar | 255 |  | √ | ' ' | 核心单据号 |
| 8 | factamount | 实付金额 | numeric | 19 | 6 | √ | 0.000000 | 实付金额 |
| 9 | fcontractnumber | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 10 | frefundamt | 退款金额 | numeric | 19 | 6 | √ | 0.000000 | 退款金额 |
| 11 | funlockamount | 未锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 未锁定金额 |
| 12 | fpayableamount | 应付金额 | numeric | 19 | 6 | √ | 0.000000 | 应付金额 |
| 13 | fcorebilltype | 核心单据类型 | varchar | 30 |  | √ | ' ' | 核心单据类型,枚举: pm_purorderbill :采购订单 er_dailyloanbill :借款单 ec_contract :建筑支出合同 |
| 14 | funsettledamount | 未结算金额 | numeric | 19 | 6 | √ | 0.000000 | 未结算金额 |
| 15 | ftaxamt | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 16 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 17 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 18 | flocalamount | 实付折本币 | numeric | 19 | 6 | √ | 0.000000 | 实付折本币 |
| 19 | fsourcebillentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fdiscountlocamount | 折扣折本币 | numeric | 19 | 6 | √ | 0.000000 | 折扣折本币 |
| 22 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 23 | fpayablelocamount | 应付折本币 | numeric | 19 | 6 | √ | 0.000000 | 应付折本币 |
| 24 | fcorebillentryseq | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 25 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 26 | flockamount | 已锁定金额 | numeric | 19 | 6 | √ | 0.000000 | 已锁定金额 |
| 27 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsettledamount | 已结算金额 | numeric | 19 | 6 | √ | 0.000000 | 已结算金额 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_payacceptentry_fid |  | fid |
| 2 | pk_ifm_payacceptanceentry |  | fentryid |

---

## 关联子实体-子表 t_ifm_payacceptance_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_payacceptance_lk

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
| 1 | pk_ifm_payacceptance_lk |  | fpkid |
| 2 | idx_ifm_payacceptance_lk_fk |  | fid |
