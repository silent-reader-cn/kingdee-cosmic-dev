# 合同-clm_related_contract

## 评审留言单据体-子表 t_clm_contract_review_m

- **表名称：** 评审留言单据体-子表
- **表名：** t_clm_contract_review_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsgstatus | fmsgstatus | varchar | 50 |  | √ | 'NULL' |  |
| 3 | fremindernames | fremindernames | varchar | 500 |  | √ | ' ' |  |
| 4 | fmsgtime | fmsgtime | timestamp | 0 |  |  | null |  |
| 5 | fmsguser | fmsguser | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmsg | fmsg | varchar | 2000 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmsground | fmsground | int8 | 64 |  | √ | 0 |  |
| 10 | freminders | 提醒关注人用户id | varchar | 1000 |  | √ | ' ' | 提醒关注人用户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_clm_contract_review_m_fk |  | fid |
| 2 | pk_t_clm_contract_review_m |  | fentryid |

---

## 合同-分表 t_clm_contractdraft_t

- **表名称：** 合同-分表
- **表名：** t_clm_contractdraft_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplatedatas_tag | ftemplatedatas_tag | text | 0 |  |  | null |  |
| 3 | ftemplatedatas | ftemplatedatas | text | 0 |  |  | null |  |
| 4 | fcontracttemplate | 合同模板 | int8 | 64 |  | √ | 0 | [合同模板 clm_contract_template](../clmcd_files/clm_contract_template.md) |

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
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 6 | fcounterpartyaccbankname | fcounterpartyaccbankname | varchar | 100 |  | √ | ' ' |  |
| 7 | fcontractcopies | fcontractcopies | int4 | 32 |  | √ | 0 |  |
| 8 | fisreviewing | fisreviewing | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0 |  |
| 11 | fisfromreview | 是否从合同评审起草 | bpchar | 1 |  | √ | '0' | 是否从合同评审起草 |
| 12 | fisamountbaseonobj | fisamountbaseonobj | bpchar | 1 |  | √ | '1' |  |
| 13 | fcounterparty | 合同相对方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fcounterpartycontactphone | fcounterpartycontactphone | varchar | 50 |  | √ | ' ' |  |
| 15 | fcounterpartyfax | fcounterpartyfax | varchar | 50 |  | √ | ' ' |  |
| 16 | fdrafttype | 合同起草方式 | varchar | 50 |  | √ | ' ' | 合同起草方式,枚举: FROM_TPL :模板起草 FROM_UPLOAD :上传文本起草 |
| 17 | fpurorg | fpurorg | int8 | 64 |  | √ | 0 |  |
| 18 | fbillno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 19 | ftotalamountcn | ftotalamountcn | varchar | 50 |  | √ | ' ' |  |
| 20 | fcontracttype | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 21 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 22 | fcounterpartycontact | fcounterpartycontact | varchar | 50 |  | √ | ' ' |  |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcontractstatus | 合同进度 | varchar | 50 |  | √ | ' ' | 合同进度,枚举: SAVE :起草中 CONFIRM_FILLING :已起草 TO_REVIEW :评审中 TO_AUDIT :审批中 REVIEWED :已审批 SIGNED :已签章 PERFORMANCE :已下推 REJECTED :已驳回 TERMINATED :已终止 |
| 25 | fconsubjecaccountbankname | fconsubjecaccountbankname | varchar | 255 |  | √ | ' ' |  |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fsalorg | fsalorg | int8 | 64 |  | √ | 0 |  |
| 28 | fcontractplace | fcontractplace | varchar | 200 |  | √ | ' ' |  |
| 29 | finvoicetype | finvoicetype | int8 | 64 |  | √ | 0 |  |
| 30 | fcounterpartyaccountname | fcounterpartyaccountname | varchar | 100 |  | √ | ' ' |  |
| 31 | ftax | ftax | int8 | 64 |  | √ | 0 |  |
| 32 | fexchangetype | fexchangetype | varchar | 30 |  | √ | ' ' |  |
| 33 | ffileid | ffileid | int8 | 64 |  | √ | 0 |  |
| 34 | fconsubjectaddress | fconsubjectaddress | varchar | 255 |  | √ | ' ' |  |
| 35 | fconsubjectbillinginfo | fconsubjectbillinginfo | varchar | 50 |  | √ | ' ' |  |
| 36 | ftotaltaxamount | ftotaltaxamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 38 | ffilinger | ffilinger | int8 | 64 |  | √ | 0 |  |
| 39 | ffilingdate | ffilingdate | timestamp | 0 |  |  | null |  |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fisallowededit | fisallowededit | bpchar | 1 |  | √ | '0' |  |
| 42 | fiselecsignature | fiselecsignature | bpchar | 1 |  | √ | '0' |  |
| 43 | fcounterpartybankaccount | fcounterpartybankaccount | varchar | 100 |  | √ | ' ' |  |
| 44 | fconsubjectpostcode | fconsubjectpostcode | varchar | 255 |  | √ | ' ' |  |
| 45 | ftotalallamountinwords | ftotalallamountinwords | varchar | 100 |  | √ | ' ' |  |
| 46 | fdocumentid | fdocumentid | varchar | 50 |  | √ | ' ' |  |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fconsubjectcontactmail | fconsubjectcontactmail | varchar | 50 |  | √ | ' ' |  |
| 49 | ffilingstatus | ffilingstatus | varchar | 50 |  | √ | ' ' |  |
| 50 | fsignstatus | 签章状态 | varchar | 50 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 51 | fconsubjectcontactphone | fconsubjectcontactphone | varchar | 100 |  | √ | ' ' |  |
| 52 | fcounterpartycontactpost | fcounterpartycontactpost | varchar | 50 |  | √ | ' ' |  |
| 53 | fcounterpartycreditcode | fcounterpartycreditcode | varchar | 100 |  | √ | ' ' |  |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsigner | fsigner | int8 | 64 |  | √ | 0 |  |
| 56 | ftotaltaxamountcn | ftotaltaxamountcn | varchar | 50 |  | √ | ' ' |  |
| 57 | fsettletype | fsettletype | int8 | 64 |  | √ | 0 |  |
| 58 | fcounterpartypostcode | fcounterpartypostcode | varchar | 50 |  | √ | ' ' |  |
| 59 | fcounterpartybillinginfo | fcounterpartybillinginfo | varchar | 50 |  | √ | ' ' |  |
| 60 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 61 | fcounterpartytype | 合同相对方类型 | varchar | 50 |  | √ | ' ' | 合同相对方类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 62 | fconsubjectaccountbank | fconsubjectaccountbank | varchar | 50 |  | √ | ' ' |  |
| 63 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 64 | fconsubjectfax | fconsubjectfax | varchar | 50 |  | √ | ' ' |  |
| 65 | fdisputeresolutionplace | fdisputeresolutionplace | varchar | 200 |  | √ | ' ' |  |
| 66 | fconsubjectmailbox | fconsubjectmailbox | varchar | 200 |  | √ | ' ' |  |
| 67 | fconsubjectaccountname | fconsubjectaccountname | varchar | 100 |  | √ | ' ' |  |
| 68 | fcounterpartymail | fcounterpartymail | varchar | 50 |  | √ | ' ' |  |
| 69 | fconsubjectcontact | fconsubjectcontact | varchar | 60 |  | √ | ' ' |  |
| 70 | fcontractdateinword | fcontractdateinword | varchar | 50 |  | √ | ' ' |  |
| 71 | fcounterpartyphone | fcounterpartyphone | varchar | 100 |  | √ | ' ' |  |
| 72 | fcontractfilecopies | fcontractfilecopies | int4 | 32 |  | √ | 0 |  |
| 73 | fcounterpartyaddress | fcounterpartyaddress | varchar | 200 |  | √ | ' ' |  |
| 74 | fcontractsubject | 合同主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 75 | fconsubjectcreditcode | fconsubjectcreditcode | varchar | 255 |  | √ | ' ' |  |
| 76 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 77 | fconsubjectphone | fconsubjectphone | varchar | 100 |  | √ | ' ' |  |
| 78 | ftotalallamount | 合同总金额 | numeric | 23 | 10 | √ | 0 | 合同总金额 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [合同 clm_related_contract](../clmcd_files/clm_related_contract.md) |
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

---

## 单据体-子表 t_clm_contract_review_ro

- **表名称：** 单据体-子表
- **表名：** t_clm_contract_review_ro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freviewstatus | freviewstatus | varchar | 50 |  | √ | ' ' |  |
| 3 | freviewerdept | freviewerdept | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 5 | frevieweremark | frevieweremark | varchar | 50 |  | √ | ' ' |  |
| 6 | freviewerround | freviewerround | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freviewer | 评审人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | freviewerrole | freviewerrole | varchar | 50 |  | √ | ' ' |  |
| 10 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_clm_contract_review_ro_fk |  | fid |
| 2 | pk_t_clm_contract_review_ro |  | fentryid |
