# 代收资金分配单-ifm_innerfundalloc

## 代收资金分配单-反写记录表 t_ifm_fundalloc_wb

- **表名称：** 代收资金分配单-反写记录表
- **表名：** t_ifm_fundalloc_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.00 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_fundalloc_wb |  | fentryid |
| 2 | idx_ifm_fundalloc_wb_fk |  | fid |

---

## 关联子实体-子表 t_ifm_fundallocbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_fundallocbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_fallocbillentry_lk_fk |  | fentryid |
| 2 | pk_ifm_fundallocbillentry_lk |  | fpkid |

---

## 代收资金分配单-主表 t_ifm_fundalloc

- **表名称：** 代收资金分配单-主表
- **表名：** t_ifm_fundalloc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayerbanknum | 付款账号 | varchar | 255 |  | √ | ' ' | 付款账号 |
| 3 | fitempayerid | 付款单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fagentfinorgid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 5 | fitempayertypeid | 付款单位类型 | varchar | 50 |  | √ | ' ' | 付款单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 6 | forg | 资金组织(没有使用) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 收款汇率 | numeric | 23 | 10 | √ | 0.00 | 收款汇率 |
| 9 | fpayername | 付款单位 | varchar | 255 |  | √ | ' ' | 付款单位 |
| 10 | fagentpayeeaccountid | 收款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 11 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fpayeracctbank | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 18 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: ifm_transrecvbill :收款结算单 |
| 19 | fagentfinorgcatid | 银行类别 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 25 | fscorgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fisdiffcur | 异币别付款 | bpchar | 1 |  | √ | '0' | 异币别付款 |
| 27 | fsourcebillnumber | 源单编码 | varchar | 255 |  | √ | ' ' | 源单编码 |
| 28 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 29 | flocalamt | 收款金额本位币 | numeric | 23 | 10 | √ | 0.00 | 收款金额本位币 |
| 30 | ftranstype | 交易类型 | varchar | 50 |  | √ | ' ' | 交易类型,枚举: 1 :内部代付 2 :内部转账 3 :资金下拨 6 :内部扣款 7 :贷款收回 8 :贷款结息 10 :银行扣款 11 :活转定 12 :定转活 13 :供应链融资还款 14 :内部代收 |
| 31 | fsettletnumber | 结算号 | varchar | 50 |  | √ | ' ' | 结算号 |
| 32 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 34 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 35 | freceiptamt | 收款金额 | numeric | 23 | 10 | √ | 0.00 | 收款金额 |
| 36 | fcurrencyid | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_fundalloc |  | fid |
| 2 | idx_ifm_fundalloc_bizdate |  | fbizdate |

---

## 关联子实体-子表 t_ifm_fundalloc_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_fundalloc_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_fundalloc_lk_fk |  | fid |
| 2 | pk_ifm_fundalloc_lk |  | fpkid |

---

## 单据体-子表 t_ifm_fundallocentry

- **表名称：** 单据体-子表
- **表名：** t_ifm_fundallocentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fsrcentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 4 | fcontactunittype | 往来单位类型 | varchar | 50 |  | √ | ' ' | 往来单位类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 other :其他 |
| 5 | fsetquotation | 结算汇率换算方式 | varchar | 50 |  | √ | ' ' | 结算汇率换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 6 | freceivablelocalamt | 收款金额本位币 | numeric | 23 | 10 | √ | 0 | 收款金额本位币 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freceivableamt | 收款金额 | numeric | 23 | 10 | √ | 0.0 | 收款金额 |
| 9 | finnerpayeeaccount | 内部账户 | int8 | 64 |  | √ | 0 | 内部账户管理 ifm_inneracct |
| 10 | fpayeebank | 收款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 11 | fsettlecur | 内部账户币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 12 | fsettlerate | 结算汇率 | numeric | 23 | 10 | √ | 0.00 | 结算汇率 |
| 13 | fmemberorgid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fcontactunit | 往来单位 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 15 | frecbilltypeid | 收款单类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fsettleamount | 结算金额 | numeric | 23 | 10 | √ | 0.00 | 结算金额 |
| 18 | fpayeeaccount | 收款账户（银行） | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 19 | fsettlementlocalamt | 结算金额本位币 | numeric | 23 | 10 | √ | 0 | 结算金额本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_fundallocentry |  | fentryid |
| 2 | idx_ifm_fundallocentry_fk |  | fid |

---

## 代收资金分配单-分表 t_ifm_fundalloc_e

- **表名称：** 代收资金分配单-分表
- **表名：** t_ifm_fundalloc_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankcheckflag | 对账标识码 | varchar | 1024 |  | √ | ' ' | 对账标识码 |
| 3 | frecvdate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |
| 4 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_fundalloc_e |  | fid |
| 2 | idx_ifm_fundalloc_e_rdate |  | frecvdate |

---

## 代收资金分配单-关联追踪表 t_ifm_fundalloc_tc

- **表名称：** 代收资金分配单-关联追踪表
- **表名：** t_ifm_fundalloc_tc

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
| 1 | idx_ifm_fundalloc_tc_tid |  | ftid |
| 2 | pk_ifm_fundalloc_tc |  | fid |
| 3 | idx_ifm_fundalloc_tc_tbill |  | ftbillid |
