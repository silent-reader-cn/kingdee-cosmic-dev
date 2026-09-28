# 结算中心扣款-ifm_deduction

## 结算中心扣款-多语言表 t_ifm_deduction_l

- **表名称：** 结算中心扣款-多语言表
- **表名：** t_ifm_deduction_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_deduction_l |  | fpkid |
| 2 | idx_ifm_deduction_l_id |  | fid |

---

## 结算中心扣款-反写记录表 t_ifm_deduction_wb

- **表名称：** 结算中心扣款-反写记录表
- **表名：** t_ifm_deduction_wb

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
| 1 | idx_ifm_deduction_wb_fk |  | fid |
| 2 | pk_ifm_deduction_wb |  | fentryid |

---

## 结算中心扣款-主表 t_ifm_deduction

- **表名称：** 结算中心扣款-主表
- **表名：** t_ifm_deduction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpaybankid | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 4 | fpaymentchannel | 支付渠道 | varchar | 30 |  | √ | ' ' | 支付渠道,枚举: bei :银企互联 onlinebank :网上银行 counter :柜台 |
| 5 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: normal :正常 chargeback :已退单 |
| 6 | frecaccbankname | 收款人实名 | varchar | 255 |  | √ | ' ' | 收款人实名 |
| 7 | fpaybankaccountid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 8 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 9 | fsource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: center :手工新增 company :扣款申请 transdetail :交易明细 |
| 10 | freceivecompanyid | 收款方ID | int8 | 64 |  | √ | 0 | 收款方ID |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fisbackfill | 备注回填转账附言 | bpchar | 1 |  | √ | '0' | 备注回填转账附言 |
| 14 | fdeductiontype | 扣款类型 | varchar | 50 |  | √ | ' ' | 扣款类型,枚举: A :结算中心代扣 B :结算中心扣款 C :银行扣款 D :结算中心退款 E :结算中心代付 |
| 15 | frealamount | 实际扣款金额 | numeric | 19 | 6 | √ | 0.000000 | 实际扣款金额 |
| 16 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fpayeename | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 19 | fbeibankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fpayeebanknum | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 22 | fcenterid | 结算中心 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 23 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_paybill :付款单 bei_transdetail :交易明细 |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fpayeebankname | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |
| 28 | fsettlettypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 29 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 bos_org :公司 other :其他 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | freason | 退单意见 | varchar | 255 |  | √ | ' ' | 退单意见 |
| 32 | fscorgid | 付款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | freceiveaccountid | 收款账号ID | int8 | 64 |  | √ | 0 | 收款账号ID |
| 34 | freceiveamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 35 | frecbanknumber | 收款行号 | varchar | 30 |  | √ | ' ' | 收款行号 |
| 36 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 38 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | freceivecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_deduction |  | fid |
| 2 | idx_ifm_deduction_billno |  | fbillno |

---

## 扣款明细（支出方）-多语言表 t_ifm_deduction_entry_l

- **表名称：** 扣款明细（支出方）-多语言表
- **表名：** t_ifm_deduction_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |
| 4 | ftransfercomment | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_deduc_entry_l_entryid |  | fentryid |
| 2 | pk_t_ifm_deduction_entry_l |  | fpkid |
| 3 | idx_ifm_deduction_entry_l_id |  | fid |

---

## 结算中心扣款-关联追踪表 t_ifm_deduction_tc

- **表名称：** 结算中心扣款-关联追踪表
- **表名：** t_ifm_deduction_tc

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
| 1 | pk_ifm_deduction_tc |  | fid |
| 2 | idx_ifm_deduction_tc_tid |  | ftid |
| 3 | idx_ifm_deduction_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 ifm_deduction_entity_lk

- **表名称：** 关联子实体-子表
- **表名：** ifm_deduction_entity_lk

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
| 1 | pk_m_deduction_entity_lk |  | fpkid |
| 2 | idx_m_deduction_entity_lk_fk |  | fentryid |

---

## 扣款明细（支出方）-子表 t_ifm_deduction_entry

- **表名称：** 扣款明细（支出方）-子表
- **表名：** t_ifm_deduction_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaystatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: wait :待付款 doing :处理中 succeed :已付款 failed :付款失败 |
| 3 | fpayaccountid | 账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 4 | fpaycompanyid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | freturncomment | 返回信息 | varchar | 255 |  | √ | ' ' | 返回信息 |
| 6 | fpaycurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fsourceentryid | 源分录ID | int8 | 64 |  | √ | 0 | 源分录ID |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fpayamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ftransfercomment | 转账附言 | varchar | 255 |  | √ | ' ' | 转账附言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_deduction_entry_id |  | fid |
| 2 | pk_t_ifm_deduction_entry |  | fentryid |
