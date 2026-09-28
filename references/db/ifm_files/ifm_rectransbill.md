# 收款记账中心-ifm_rectransbill

## 收款记账中心-关联追踪表 t_ifm_rectransbill_tc

- **表名称：** 收款记账中心-关联追踪表
- **表名：** t_ifm_rectransbill_tc

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
| 1 | pk_ifm_rectransbill_tc |  | fid |
| 2 | idx_ifm_rectransbill_tc_tid |  | ftid |
| 3 | idx_ifm_rectransbill_tc_tbill |  | ftbillid |

---

## 收款记账中心-主表 t_ifm_rectransbill

- **表名称：** 收款记账中心-主表
- **表名：** t_ifm_rectransbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpayeeorgid | 收款人（公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpayernumber | 付款人编码 | varchar | 30 |  | √ | ' ' | 付款人编码 |
| 4 | fopenorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fitempayerid | 付款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | facttradedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 7 | fbankcheckflag | 对账标识码 | varchar | 100 |  | √ | ' ' | 对账标识码 |
| 8 | fitempayertypeid | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 9 | fsettlenumber | 结算号 | varchar | 100 |  | √ | ' ' | 结算号 |
| 10 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 11 | fpaccountbankid | 子账户银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fpayeeacctbankid | 收款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 14 | fpayername | 付款人名称 | varchar | 255 |  | √ | ' ' | 付款人名称 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpayerid | 付款人ID | int8 | 64 |  | √ | 0 | 付款人ID |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fpayeracctbankid | 付款账户ID | int8 | 64 |  | √ | 0 | 付款账户ID |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fpayerbankaccnum | 付款账号 | varchar | 100 |  | √ | ' ' | 付款账号 |
| 21 | fpayerbankid | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 22 | fsourcebillentryid | 源单分录明显ID | int8 | 64 |  | √ | 0 | 源单分录明显ID |
| 23 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_recbill :收款单 ifm_loanbill :贷款放款单 fca_transupbill :上划单 ifm_currentintbill :存款结息单 ifm_release :内部定期存款解活处理 ifm_notice_release :内部通知存款解活处理 |
| 24 | fpaidstatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: A :待付款 B :已付款 |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fvouchernum | 凭证号 | varchar | 100 |  | √ | ' ' | 凭证号 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 30 | fpayertypeid | 付款人类型 | varchar | 30 |  | √ | ' ' | 付款人类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :公司 bos_user :职员 other :其他 |
| 31 | fscorgid | 结算中心组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 33 | fpayerformid | 付款人类型标识ID | varchar | 30 |  | √ | ' ' | 付款人类型标识ID |
| 34 | fsourcebillnumber | 源单编码 | varchar | 100 |  | √ | ' ' | 源单编码 |
| 35 | ftranstype | 交易类型 | varchar | 30 |  | √ | ' ' | 交易类型,枚举: 4 :内部收款 5 :资金上划 6 :贷款发放 9 :存款结息 |
| 36 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 38 | factrecamt | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 39 | fpayeraccformid | 付款账户类型标识ID | varchar | 30 |  | √ | ' ' | 付款账户类型标识ID |
| 40 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fpayerbankname | 付款银行 | varchar | 255 |  | √ | ' ' | 付款银行 |
| 44 | fpayeedate | 收款日期 | timestamp | 0 |  |  | null | 收款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_rectransbill_bizdate |  | fbizdate |
| 2 | pk_ifm_rectransbill |  | fid |

---

## 关联子实体-子表 t_ifm_rectransbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_rectransbill_lk

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
| 1 | pk_ifm_rectransbill_lk |  | fpkid |
| 2 | idx_ifm_rectransbill_lk_fk |  | fid |

---

## 收款记账中心-反写记录表 t_ifm_rectransbill_wb

- **表名称：** 收款记账中心-反写记录表
- **表名：** t_ifm_rectransbill_wb

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
| 1 | idx_ifm_rectransbill_wb_fk |  | fid |
| 2 | pk_ifm_rectransbill_wb |  | fentryid |
