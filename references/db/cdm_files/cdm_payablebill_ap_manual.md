# 批量开票申请-cdm_payablebill_ap_manual

## 开票申请明细-子表 t_cdm_payablebill_ap_m_e

- **表名称：** 开票申请明细-子表
- **表名：** t_cdm_payablebill_ap_m_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 4 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | famount | 开票金额 | numeric | 19 | 6 | √ | 0 | 开票金额 |
| 7 | freceivertype | 收款人全称类型 | varchar | 30 |  | √ | ' ' | 收款人全称类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :人员 bos_org :业务单元 |
| 8 | freceiverbankno | 收款人开户行行号 | varchar | 80 |  | √ | ' ' | 收款人开户行行号 |
| 9 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 10 | fdrawername | 出票人全称 | varchar | 512 |  | √ | ' ' | 出票人全称 |
| 11 | fpayable | 开票登记 | bpchar | 1 |  | √ | '0' | 开票登记 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | freceivername | 收款人全称 | varchar | 80 |  | √ | ' ' | 收款人全称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fdrawerbankno | 出票人开户行行号 | varchar | 80 |  | √ | ' ' | 出票人开户行行号 |
| 18 | fdraweraccountname | 出票人账户名称 | varchar | 80 |  | √ | ' ' | 出票人账户名称 |
| 19 | freceiverid | 收款人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 21 | fdrawerbankname | 出票人开户银行 | varchar | 80 |  | √ | ' ' | 出票人开户银行 |
| 22 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 23 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 25 | fcontractno | 交易合同号 | varchar | 80 |  | √ | ' ' | 交易合同号 |
| 26 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 27 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 28 | fdraftbillnoid | 票据号码 | int8 | 64 |  | √ | 0 | 支票F7数据 cdm_cheque_f7data |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |

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

## 批量开票申请-主表 t_cdm_payablebill_ap_m

- **表名称：** 批量开票申请-主表
- **表名：** t_cdm_payablebill_ap_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccepteraccount | 承兑人账号 | varchar | 80 |  | √ | ' ' | 承兑人账号 |
| 3 | famounttotal | 票据金额合计 | numeric | 19 | 6 | √ | 0 | 票据金额合计 |
| 4 | faccepterbankno | 承兑人开户行行号 | varchar | 80 |  | √ | ' ' | 承兑人开户行行号 |
| 5 | freceivertype | freceivertype | varchar | 30 |  | √ | ' ' |  |
| 6 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 apply :开票申请 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | faccepterfinorgid | 承兑人全称 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | 票据类型 cdm_billtype |
| 11 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | faccepteraccountid | 承兑人账号(基础资料) | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 13 | fbillingtype | 开票方式 | varchar | 80 |  | √ | ' ' | 开票方式,枚举: credit :授信 guarantee :担保 other :其他 |
| 14 | fcount | 票据张数合计 | int8 | 64 |  | √ | 0 | 票据张数合计 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | facceptername | 承兑人全称 | varchar | 1024 |  | √ | ' ' | 承兑人全称 |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 4 :抵押 5 :质押 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fcreditamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0 | 实际占用授信金额 |
| 24 | faccepterbankname | 承兑人开户银行 | varchar | 80 |  | √ | ' ' | 承兑人开户银行 |
| 25 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | 授信额度管理 cfm_creditlimit |
| 29 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | fcompanyid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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
| 5 | fgcontractcurrency | 担保合同币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 7 | fgcontract | 担保单据编号 | int8 | 64 |  | √ | 0 | 担保合同 gm_guaranteecontract_f7 |
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

## 保证金分录-子表 t_cdm_payablebill_sur_e

- **表名称：** 保证金分录-子表
- **表名：** t_cdm_payablebill_sur_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuretycurrency | 保证金币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fsuretyexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 4 | fsuretyfinorg | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 5 | fsuretyamount | 保证金金额 | numeric | 19 | 6 | √ | 0 | 保证金金额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsuretyaccount | 保证金账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 8 | fsuretybill | 单据编号 | int8 | 64 |  | √ | 0 | 保证金存入处理F7 fbd_suretybill_f7 |
| 9 | fguaranteetype | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: deposit :保证金 |
| 10 | fsuretyintdate | 保证金起息日 | timestamp | 0 |  |  | null | 保证金起息日 |
| 11 | fsuretyterm | 期限（ymd） | varchar | 80 |  | √ | ' ' | 期限（ymd） |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fsuretysource | 单据来源 | varchar | 80 |  | √ | ' ' | 单据来源,枚举: hand :债务生成 linkgen :保证金生成 guarantee :担保管理 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_payablebill_sur_e |  | fentryid |
| 2 | idx_cdm_payablebill_sur_e |  | fsuretybill,fguaranteetype |
