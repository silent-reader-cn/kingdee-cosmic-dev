# 批量开票申请-cdm_payablebill_ap_manual

## 开票申请明细-子表 t_cdm_payablebill_ap_m_e

- **表名称：** 开票申请明细-子表
- **表名：** t_cdm_payablebill_ap_m_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 4 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 5 | fsuretyamount | 保证金 | numeric | 23 | 10 | √ | 0 | 保证金 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | 开票金额 | numeric | 19 | 6 | √ | 0 | 开票金额 |
| 8 | freceivertype | 收款人全称类型 | varchar | 30 |  | √ | ' ' | 收款人全称类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 9 | freceiverbankno | 收款人开户行行号 | varchar | 80 |  | √ | ' ' | 收款人开户行行号 |
| 10 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 11 | fdrawername | 出票人全称 | varchar | 512 |  | √ | ' ' | 出票人全称 |
| 12 | fpayable | 开票登记 | bpchar | 1 |  | √ | '0' | 开票登记 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 15 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 16 | finvalid | 作废 | bpchar | 1 |  | √ | '0' | 作废 |
| 17 | freceivername | 收款人全称 | varchar | 80 |  | √ | ' ' | 收款人全称 |
| 18 | fdraftuseamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fdrawerbankno | 出票人开户行行号 | varchar | 80 |  | √ | ' ' | 出票人开户行行号 |
| 21 | fdraweraccountname | 出票人账户名称 | varchar | 80 |  | √ | ' ' | 出票人账户名称 |
| 22 | fsuretyinput | 存入保证金 | bpchar | 1 |  | √ | '0' | 存入保证金 |
| 23 | freceiverid | 收款人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 24 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 25 | fdrawerbankname | 出票人开户银行 | varchar | 80 |  | √ | ' ' | 出票人开户银行 |
| 26 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 27 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 29 | fcontractno | 交易合同号 | varchar | 80 |  | √ | ' ' | 交易合同号 |
| 30 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 31 | famountofcredit | 实际占用授信额度 | numeric | 19 | 6 | √ | 0 | 实际占用授信额度 |
| 32 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 33 | fentry_suretyremainamount | 保证金剩余金额 | numeric | 19 | 4 | √ | 0 | 保证金剩余金额 |
| 34 | fdraftbillnoid | 票据号码 | int8 | 64 |  | √ | 0 | [支票F7数据 cdm_cheque_f7data](../cdm_files/cdm_cheque_f7data.md) |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_payablebill_ap_m_e |  | fissuedate,fdraftbillexpiredate |
| 2 | pk_t_cdm_payablebill_ap_m_e |  | fentryid |

---

## 担保信息分录-子表 t_cdm_payablebill_gcon_e

- **表名称：** 担保信息分录-子表
- **表名：** t_cdm_payablebill_gcon_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgguarantortext | fgguarantortext | varchar | 100 |  | √ | ' ' |  |
| 3 | fgcreditguarantee | 是否额度担保 | bpchar | 1 |  | √ | '0' | 是否额度担保 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fgcontractcurrency | 担保合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 7 | fgcontract | 担保单据编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 8 | fgexchrate | 折算汇率 | numeric | 19 | 6 | √ | 0 | 折算汇率 |
| 9 | fgratio | 担保比例(%) | numeric | 19 | 6 | √ | 0 | 担保比例(%) |
| 10 | fguaranteeway | fguaranteeway | varchar | 80 |  | √ | ' ' |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fgcontractamount | 担保合同金额 | numeric | 19 | 6 | √ | 0 | 担保合同金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_payablebill_gcon_e |  | fentryid |
| 2 | idx_cdm_payablebill_gcon_e |  | fgcontract,fguaranteeway |

---

## 批量开票申请-主表 t_cdm_payablebill_ap_m

- **表名称：** 批量开票申请-主表
- **表名：** t_cdm_payablebill_ap_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccepteraccount | 承兑人账号 | varchar | 80 |  | √ | ' ' | 承兑人账号 |
| 3 | famounttotal | 票据金额合计 | numeric | 19 | 6 | √ | 0 | 票据金额合计 |
| 4 | fpromisrate | 保证金比例(%) | numeric | 19 | 6 | √ | 0 | 保证金比例(%) |
| 5 | faccepterbankno | 承兑人开户行行号 | varchar | 80 |  | √ | ' ' | 承兑人开户行行号 |
| 6 | freceivertype | freceivertype | varchar | 30 |  | √ | ' ' |  |
| 7 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 apply :开票申请 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | faccepterfinorgid | 承兑人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 10 | fpoolprotocolid | 票据池 | int8 | 64 |  | √ | 0 | [银行票据池协议 cdm_pool_protocol](../cdm_files/cdm_pool_protocol.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 13 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | faccepteraccountid | 承兑人账号(基础资料) | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 15 | fbillingtype | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: credit :授信 guarantee :保证金 other :其他 |
| 16 | fcount | 票据张数合计 | int8 | 64 |  | √ | 0 | 票据张数合计 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | facceptername | 承兑人全称 | varchar | 1024 |  | √ | ' ' | 承兑人全称 |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 4 :抵押 5 :质押 |
| 24 | fsuretymoney | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fcreditamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0 | 实际占用授信金额 |
| 27 | faccepterbankname | 承兑人开户银行 | varchar | 80 |  | √ | ' ' | 承兑人开户银行 |
| 28 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 29 | fiseditsuretyamount | 是否编辑保证金明细 | bpchar | 1 |  | √ | '0' | 是否编辑保证金明细 |
| 30 | fuseamount | 占用额度 | numeric | 23 | 10 | √ | 0 | 占用额度 |
| 31 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 34 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 35 | fcompanyid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_payablebill_ap_m |  | fid |
| 2 | idx_cdm_payablebill_a |  | fbillstatus,fbizdate |

---

## 开票申请明细-多语言表 t_cdm_payablebill_ap_m_e_l

- **表名称：** 开票申请明细-多语言表
- **表名：** t_cdm_payablebill_ap_m_e_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 2 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_payablebill_ap_m_e_l |  | fpkid |
| 2 | idx_cdm_payablebill_ap_m_e_l |  | fentryid,flocaleid |
