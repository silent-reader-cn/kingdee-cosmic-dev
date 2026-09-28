# 合同-clm_related_contract

## 合同-分表 t_clm_contractdraft_t

- **表名称：** 合同-分表
- **表名：** t_clm_contractdraft_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplatedatas_tag | ftemplatedatas_tag | text | 0 |  |  | null |  |
| 3 | ftemplatedatas | ftemplatedatas | text | 0 |  |  | null |  |
| 4 | fcontracttemplate | 合同模板 | int8 | 64 |  | √ | 0 | 合同模板 clm_contract_template |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_draft_t_fid |  | fcontracttemplate |
| 2 | pk_t_clm_contractdraft_t |  | fid |

---

## 合同-多语言表 t_clm_contractdraft_l

- **表名称：** 合同-多语言表
- **表名：** t_clm_contractdraft_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 3 | fcounterpartycontact | fcounterpartycontact | varchar | 50 |  | √ | ' ' |  |
| 4 | fconsubjecaccountbankname | fconsubjecaccountbankname | varchar | 100 |  | √ | ' ' |  |
| 5 | fdisputeresolutionplace | fdisputeresolutionplace | varchar | 100 |  | √ | ' ' |  |
| 6 | fcounterpartyaccbankname | fcounterpartyaccbankname | varchar | 100 |  | √ | ' ' |  |
| 7 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 8 | fconsubjectaccountname | fconsubjectaccountname | varchar | 100 |  | √ | ' ' |  |
| 9 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 10 | fcontractplace | fcontractplace | varchar | 100 |  | √ | ' ' |  |
| 11 | fcounterpartyaccountname | fcounterpartyaccountname | varchar | 100 |  | √ | ' ' |  |
| 12 | fconsubjectcreditcode | fconsubjectcreditcode | varchar | 50 |  | √ | ' ' |  |
| 13 | fconsubjectaddress | fconsubjectaddress | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_conract_draft_lflocaleid |  | flocaleid |
| 2 | pk_t_clm_contractdraft_l |  | fpkid |

---

## 合同-主表 t_clm_contractdraft

- **表名称：** 合同-主表
- **表名：** t_clm_contractdraft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | fcontractdate | fcontractdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 6 | fcounterpartyaccbankname | fcounterpartyaccbankname | varchar | 100 |  | √ | ' ' |  |
| 7 | fcontractcopies | fcontractcopies | int4 | 32 |  | √ | 0 |  |
| 8 | fisreviewing | fisreviewing | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 11 | fisfromreview | 是否从合同评审起草 | bpchar | 1 |  | √ | '0' | 是否从合同评审起草 |
| 12 | fcounterparty | 合同相对方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fcounterpartycontactphone | fcounterpartycontactphone | varchar | 50 |  | √ | ' ' |  |
| 14 | fcounterpartyfax | fcounterpartyfax | varchar | 50 |  | √ | ' ' |  |
| 15 | fdrafttype | 合同起草方式 | varchar | 50 |  | √ | ' ' | 合同起草方式,枚举: FROM_TPL :模板起草 FROM_UPLOAD :上传文本起草 |
| 16 | fpurorg | fpurorg | int8 | 64 |  | √ | 0 |  |
| 17 | fbillno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 18 | fcontracttype | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 19 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 20 | fcounterpartycontact | fcounterpartycontact | varchar | 50 |  | √ | ' ' |  |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcontractstatus | 合同进度 | varchar | 50 |  | √ | ' ' | 合同进度,枚举: SAVE :起草中 CONFIRM_FILLING :已起草 TO_REVIEW :评审中 TO_AUDIT :审批中 REVIEWED :已审批 SIGNED :已签章 PERFORMANCE :履行中 COMPLETED :已完成 |
| 23 | fconsubjecaccountbankname | fconsubjecaccountbankname | varchar | 255 |  | √ | ' ' |  |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fsalorg | fsalorg | int8 | 64 |  | √ | 0 |  |
| 26 | fcontractplace | fcontractplace | varchar | 200 |  | √ | ' ' |  |
| 27 | finvoicetype | finvoicetype | int8 | 64 |  | √ | 0 |  |
| 28 | fcounterpartyaccountname | fcounterpartyaccountname | varchar | 100 |  | √ | ' ' |  |
| 29 | ftax | ftax | int8 | 64 |  | √ | 0 |  |
| 30 | fexchangetype | fexchangetype | varchar | 30 |  | √ | ' ' |  |
| 31 | ffileid | ffileid | int8 | 64 |  | √ | 0 |  |
| 32 | fconsubjectaddress | fconsubjectaddress | varchar | 255 |  | √ | ' ' |  |
| 33 | fconsubjectbillinginfo | fconsubjectbillinginfo | varchar | 50 |  | √ | ' ' |  |
| 34 | ftotaltaxamount | ftotaltaxamount | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fisallowededit | fisallowededit | bpchar | 1 |  | √ | '0' |  |
| 38 | fcounterpartybankaccount | fcounterpartybankaccount | varchar | 100 |  | √ | ' ' |  |
| 39 | fconsubjectpostcode | fconsubjectpostcode | varchar | 255 |  | √ | ' ' |  |
| 40 | ftotalallamountinwords | ftotalallamountinwords | varchar | 100 |  | √ | ' ' |  |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fconsubjectcontactmail | fconsubjectcontactmail | varchar | 50 |  | √ | ' ' |  |
| 43 | fsignstatus | 签章状态 | varchar | 50 |  | √ | ' ' | 签章状态,枚举: NOT_SIGN :未签章 SIGNED :已签章 |
| 44 | fconsubjectcontactphone | fconsubjectcontactphone | varchar | 100 |  | √ | ' ' |  |
| 45 | fcounterpartycontactpost | fcounterpartycontactpost | varchar | 50 |  | √ | ' ' |  |
| 46 | fcounterpartycreditcode | fcounterpartycreditcode | varchar | 100 |  | √ | ' ' |  |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fsettletype | fsettletype | int8 | 64 |  | √ | 0 |  |
| 49 | fcounterpartypostcode | fcounterpartypostcode | varchar | 50 |  | √ | ' ' |  |
| 50 | fcounterpartybillinginfo | fcounterpartybillinginfo | varchar | 50 |  | √ | ' ' |  |
| 51 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 52 | fcounterpartytype | 合同相对方类型 | varchar | 50 |  | √ | ' ' | 合同相对方类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 53 | fconsubjectaccountbank | fconsubjectaccountbank | varchar | 50 |  | √ | ' ' |  |
| 54 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 55 | fconsubjectfax | fconsubjectfax | varchar | 50 |  | √ | ' ' |  |
| 56 | fdisputeresolutionplace | fdisputeresolutionplace | varchar | 200 |  | √ | ' ' |  |
| 57 | fconsubjectmailbox | fconsubjectmailbox | varchar | 200 |  | √ | ' ' |  |
| 58 | fconsubjectaccountname | fconsubjectaccountname | varchar | 100 |  | √ | ' ' |  |
| 59 | fconsubjectcontact | fconsubjectcontact | int8 | 64 |  | √ | 0 |  |
| 60 | fcounterpartymail | fcounterpartymail | varchar | 50 |  | √ | ' ' |  |
| 61 | fcontractdateinword | fcontractdateinword | varchar | 50 |  | √ | ' ' |  |
| 62 | fcounterpartyphone | fcounterpartyphone | varchar | 100 |  | √ | ' ' |  |
| 63 | fcontractfilecopies | fcontractfilecopies | int4 | 32 |  | √ | 0 |  |
| 64 | fcounterpartyaddress | fcounterpartyaddress | varchar | 200 |  | √ | ' ' |  |
| 65 | fcontractsubject | 合同主体 | int8 | 64 |  | √ | 0 | 合同主体 conm_contparties |
| 66 | fconsubjectcreditcode | fconsubjectcreditcode | varchar | 255 |  | √ | ' ' |  |
| 67 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 68 | fconsubjectphone | fconsubjectphone | varchar | 100 |  | √ | ' ' |  |
| 69 | ftotalallamount | 合同总金额 | numeric | 23 | 10 | √ | 0 | 合同总金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_contractdraft |  | fid |
| 2 | idx_contract_draft_billno |  | fbillno |

---

## 关联合同-多选基础资料表 t_clm_related_contract

- **表名称：** 关联合同-多选基础资料表
- **表名：** t_clm_related_contract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 合同 clm_related_contract |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_clm_related_contract_id |  | fid |
| 2 | pk_t_clm_related_contract |  | fpkid |
