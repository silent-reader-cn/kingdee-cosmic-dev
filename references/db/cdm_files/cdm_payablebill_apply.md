# 开票申请-cdm_payablebill_apply

## 开票申请-主表 t_cdm_draftbill_apply

- **表名称：** 开票申请-主表
- **表名：** t_cdm_draftbill_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocksourcebilltype | 锁票源单类型 | varchar | 50 |  | √ | ' ' | 锁票源单类型 |
| 3 | fdeliverid | fdeliverid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fdraftbillexpiredate | 票据到期日 | timestamp | 0 |  |  | null | 票据到期日 |
| 6 | fdraftbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 7 | fintopooltime | fintopooltime | timestamp | 0 |  |  | null |  |
| 8 | fsourcedraftid | fsourcedraftid | int8 | 64 |  | √ | 0 |  |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 12 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fpayeetype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 14 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 15 | fcreditamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0 | 实际占用授信金额 |
| 16 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 17 | fissuedate | 出票日期 | timestamp | 0 |  |  | null | 出票日期 |
| 18 | fistransfer | 能否转让 | bpchar | 1 |  | √ | '0' | 能否转让 |
| 19 | frecbody | 受理机构 | varchar | 80 |  | √ | ' ' | 受理机构 |
| 20 | fdraftbillstatus | 票据状态 | varchar | 30 |  | √ | ' ' | 票据状态,枚举: registered :已登记 |
| 21 | fdraftbillnoid | 票据号码 | int8 | 64 |  | √ | 0 | [支票F7数据 cdm_cheque_f7data](../cdm_files/cdm_cheque_f7data.md) |
| 22 | fbillpoolid | fbillpoolid | int8 | 64 |  | √ | 0 |  |
| 23 | fuseamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 24 | fpoollockorgid | fpoollockorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fbankaccountid | fbankaccountid | int8 | 64 |  | √ | 0 |  |
| 28 | fdraftbillno | 票据号码 | varchar | 80 |  | √ | ' ' | 票据号码 |
| 29 | fclaimnoticebillno | fclaimnoticebillno | varchar | 80 |  | √ | ' ' |  |
| 30 | famount | 票面金额 | numeric | 19 | 6 | √ | 0 | 票面金额 |
| 31 | fsource | 来源系统 | varchar | 30 |  | √ | ' ' | 来源系统,枚举: handregister :手工登记 cas :出纳 bei :银企互联 cdm :票据管理 apply :开票申请 |
| 32 | flocksourcebillid | 锁票源单id | varchar | 50 |  | √ | ' ' | 锁票源单id |
| 33 | fdelivername | fdelivername | varchar | 80 |  | √ | ' ' |  |
| 34 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 35 | fpoolprotocolid | 票据池 | int8 | 64 |  | √ | 0 | [银行票据池协议 cdm_pool_protocol](../cdm_files/cdm_pool_protocol.md) |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fpoollocktime | fpoollocktime | timestamp | 0 |  |  | null |  |
| 38 | fpoollockstatus | fpoollockstatus | bpchar | 1 |  | √ | '0' |  |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fispayinterest | 买方付息 | bpchar | 1 |  | √ | '0' | 买方付息 |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fisendorsepay | 是否锁定 | bpchar | 1 |  | √ | '0' | 是否锁定 |
| 43 | fallocbillentryid | fallocbillentryid | int8 | 64 |  | √ | 0 |  |
| 44 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 45 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 46 | fbeendorsor | 被背书人 | varchar | 80 |  | √ | ' ' | 被背书人 |
| 47 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 48 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | facceptno | 承兑协议编号 | varchar | 80 |  | √ | ' ' | 承兑协议编号 |
| 50 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 51 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 52 | fdelivertype | fdelivertype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cdm_draftbill_allocentid_a |  | fallocbillentryid |
| 2 | idx_t_cdm_draftbill_a |  | fbizdate,fdraftbillstatus |
| 3 | idx_cdm_draftbill_billpoolid_a |  | fbillpoolid |
| 4 | pk_t_cdm_draftbill_apply |  | fid |

---

## 开票申请-分表 t_cdm_draftbill_apply_e

- **表名称：** 开票申请-分表
- **表名：** t_cdm_draftbill_apply_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpromiseexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 3 | faccepteraccount | 承兑人账号 | varchar | 80 |  | √ | ' ' | 承兑人账号 |
| 4 | fissuepromiserdate | 保证日期 | timestamp | 0 |  |  | null | 保证日期 |
| 5 | faccepterorgid | faccepterorgid | int8 | 64 |  | √ | 0 |  |
| 6 | faccepterbankno | 承兑人开户行行号 | varchar | 80 |  | √ | ' ' | 承兑人开户行行号 |
| 7 | freceiverbankno | 收款人开户行行号 | varchar | 80 |  | √ | ' ' | 收款人开户行行号 |
| 8 | facceptpromiserdate | 保证日期 | timestamp | 0 |  |  | null | 保证日期 |
| 9 | faccpromisetype | 承兑保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 承兑保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 10 | fdrawername | 出票人全称 | varchar | 512 |  | √ | ' ' | 出票人全称 |
| 11 | fissueticketgrade | 评级主体 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 12 | fpayable | 开票登记 | bpchar | 1 |  |  | '0' | 开票登记 |
| 13 | fdrawerorgid | 出票人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 14 | fpromisecreditlevel | 承兑人信用等级 | varchar | 80 |  | √ | ' ' | 承兑人信用等级 |
| 15 | fissueticketexpiredate | 评级到期日期 | timestamp | 0 |  |  | null | 评级到期日期 |
| 16 | facceptpromiseraccount | 保证人账号 | varchar | 80 |  | √ | ' ' | 保证人账号 |
| 17 | fdrawerbankno | 出票人开户行行号 | varchar | 80 |  | √ | ' ' | 出票人开户行行号 |
| 18 | facceptername | 承兑人全称 | varchar | 1024 |  | √ | ' ' | 承兑人全称 |
| 19 | fdraweraccountname | 出票人账号 | varchar | 80 |  | √ | ' ' | 出票人账号 |
| 20 | freceiverid | 收款人全称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 21 | fdrawerbankname | 出票人开户银行 | varchar | 80 |  | √ | ' ' | 出票人开户银行 |
| 22 | fissuepromiseraccount | 保证人账号 | varchar | 80 |  | √ | ' ' | 保证人账号 |
| 23 | faccepterbankname | 承兑人开户银行 | varchar | 80 |  | √ | ' ' | 承兑人开户银行 |
| 24 | fdrawerid | fdrawerid | int8 | 64 |  | √ | 0 |  |
| 25 | fissuepromiser | 出票保证人名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fissuepromisertype | 保证人类型 | varchar | 30 |  | √ | ' ' | 保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 27 | facceptpromisertype | 保证人类型 | varchar | 30 |  | √ | ' ' | 保证人类型,枚举: bos_org :公司 bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 28 | freceiverbankname | freceiverbankname | varchar | 80 |  | √ | ' ' |  |
| 29 | fpromisegrade | 评级主体 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 30 | fdrawersid | fdrawersid | int8 | 64 |  | √ | 0 |  |
| 31 | fdraweraccountid | 出票人账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 32 | fissuepromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 33 | facceptpromiseraddr | 保证人地址 | varchar | 80 |  | √ | ' ' | 保证人地址 |
| 34 | freceivertype | 收款人全称类型 | varchar | 30 |  | √ | ' ' | 收款人全称类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 35 | facceptpromisername | 承兑保证人名称 | varchar | 80 |  | √ | ' ' | 承兑保证人名称 |
| 36 | faccepterfinorgid | 承兑人全称 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 37 | faccepterbankorgid | faccepterbankorgid | int8 | 64 |  | √ | 0 |  |
| 38 | facceptercompanyid | 承兑人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fissueticketcreditlevel | 出票人信用等级 | varchar | 80 |  | √ | ' ' | 出票人信用等级 |
| 40 | fdrawerbankid | fdrawerbankid | int8 | 64 |  | √ | 0 |  |
| 41 | faccepteraccid | faccepteraccid | int8 | 64 |  | √ | 0 |  |
| 42 | freceivername | 收款人全称 | varchar | 80 |  | √ | ' ' | 收款人全称 |
| 43 | fisspromisetype | 出票保证人类型基础资料类型 | varchar | 30 |  | √ | ' ' | 出票保证人类型基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :公司 cas_othercontactunit :其他往来单位 |
| 44 | faccepterbankaccid | faccepterbankaccid | int8 | 64 |  | √ | 0 |  |
| 45 | fdrawercompanyid | 出票人全称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fissuepromisername | 出票保证人名称 | varchar | 80 |  | √ | ' ' | 出票保证人名称 |
| 47 | freceiveraccount | 收款人账号 | varchar | 80 |  | √ | ' ' | 收款人账号 |
| 48 | freceiverbankid | 收款人开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 49 | facceptpromiser | 承兑保证人名称 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_apply_e |  | fid |
| 2 | idx_t_cdm_draftbill_a_e |  | fdrawername |

---

## 开票申请-分表 t_cdm_draftbill_apply_f

- **表名称：** 开票申请-分表
- **表名：** t_cdm_draftbill_apply_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontractno | 交易合同号 | varchar | 50 |  | √ | ' ' | 交易合同号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_apply_f |  | fid |
| 2 | idx_t_cdm_draftbill_a_f |  | fcontractno |

---

## 开票申请-多语言表 t_cdm_draftbill_apply_l

- **表名称：** 开票申请-多语言表
- **表名：** t_cdm_draftbill_apply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_draftbill_apply_l |  | fpkid |
| 2 | idx_t_cdm_draftbill_a_l |  | fid,flocaleid |
