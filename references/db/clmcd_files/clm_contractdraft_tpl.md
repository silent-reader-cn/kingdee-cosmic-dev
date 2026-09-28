# 合同起草-clm_contractdraft_tpl

## 单据体-子表 t_clm_contract_review_log

- **表名称：** 单据体-子表
- **表名：** t_clm_contract_review_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogroundname | 轮次名称 | varchar | 50 |  | √ | ' ' | 轮次名称 |
| 3 | flogreviewer | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | floground | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |
| 5 | flogstatus | 评审状态 | varchar | 50 |  | √ | ' ' | 评审状态,枚举: NEW_REVIEW :发起评审 NEW_ROUND_REVIEW :发起新一轮评审 REVIEWING :正在评审 PASS :评审通过 UNPASS :评审不通过 END_THIS_ROUND :结束本轮评审 |
| 6 | flogrole | 角色 | varchar | 50 |  | √ | ' ' | 角色,枚举: |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ffileid | ffileid | int8 | 64 |  | √ | 0 |  |
| 9 | flogreviewtime | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 10 | flogfileid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_contract_review_log |  | fentryid |
| 2 | idx_clm_contract_review_log_fk |  | fid |

---

## 合同标的单据体-子表 t_clm_contractdraft_obj

- **表名称：** 合同标的单据体-子表
- **表名：** t_clm_contractdraft_obj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodel | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 5 | famountandtaxinwords | 价税合计（中文） | varchar | 200 |  | √ | ' ' | 价税合计（中文） |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 9 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 10 | fbasesalunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fsalmaterial | 物料名称 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 12 | fcuramount | 不含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 不含税金额(本位币) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 16 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 17 | fbasepurunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | fprojectid | 项目名称 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 21 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 22 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 23 | fsalunit | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 25 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 26 | fentrycomment | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 27 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fpurmaterial | 物料名称 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 30 | fpurunit | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_draft_obj_fid |  | fid |
| 2 | pk_t_clm_contractdraft_obj |  | fentryid |

---

## 评审留言单据体-子表 t_clm_contract_review_m

- **表名称：** 评审留言单据体-子表
- **表名：** t_clm_contract_review_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsgstatus | 留言状态 | varchar | 50 |  | √ | 'NULL' | 留言状态,枚举: UNPASS :评审不通过 PASS :评审通过 END_THIS_ROUND :结束本轮评审 |
| 3 | fremindernames | 提醒关注人 | varchar | 500 |  | √ | ' ' | 提醒关注人 |
| 4 | fmsgtime | 留言时间 | timestamp | 0 |  |  | null | 留言时间 |
| 5 | fmsguser | 留言人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmsg | 留言 | varchar | 2000 |  | √ | ' ' | 留言 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmsground | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |
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

## 合同款项单据体-子表 t_clm_contractdraft_money

- **表名称：** 合同款项单据体-子表
- **表名：** t_clm_contractdraft_money

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpaymentnode | 款项节点 | int8 | 64 |  | √ | 0 | 合同款项节点 clm_contract_payment_node |
| 3 | fisprepayment | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 4 | fmoneyinwords | 款项金额（中文） | varchar | 200 |  | √ | ' ' | 款项金额（中文） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftimelimit | 时间期限 | numeric | 23 | 1 | √ | 0 | 时间期限 |
| 7 | fisprereceive | 是否预收 | bpchar | 1 |  | √ | '0' | 是否预收 |
| 8 | fbeforeorafter | 前/后 | varchar | 50 |  | √ | ' ' | 前/后,枚举: BEFORE :前 AFTER :后 |
| 9 | frate | 款项比例（%） | numeric | 23 | 10 | √ | 0 | 款项比例（%） |
| 10 | ftimeunit | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: workday :个工作日 naturalday :个自然日 day :日 week :周 month :月 year :年 |
| 11 | forder | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 12 | fmoneytinnum | 款项金额（数字） | numeric | 23 | 10 | √ | 0 | 款项金额（数字） |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ftextsupplement | 条款文本补充 | varchar | 2000 |  | √ | ' ' | 条款文本补充 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_draft_money_fid |  | fid |
| 2 | pk_t_clm_contractdraft_money |  | fentryid |

---

## 合同起草-分表 t_clm_contractdraft_t

- **表名称：** 合同起草-分表
- **表名：** t_clm_contractdraft_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplatedatas_tag | 合同模板数据_详情 | text | 0 |  |  | null | 合同模板数据_详情 |
| 3 | ftemplatedatas | 合同模板数据 | text | 0 |  |  | null | 合同模板数据 |
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

## 合同起草-分表 t_clm_contractdraft_r

- **表名称：** 合同起草-分表
- **表名：** t_clm_contractdraft_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrentreviewstatus | 当前评审状态 | varchar | 50 |  | √ | ' ' | 当前评审状态,枚举: NEW_REVIEW :发起评审 NEW_ROUND_REVIEW :发起新一轮评审 END_THIS_ROUND :结束本轮评审 TO_AUDIT :已提交审批 REVIEWED :已审批 |
| 3 | fapprovesubmiter | 审批提交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | freviewernewtime | 评审发起时间 | timestamp | 0 |  |  | null | 评审发起时间 |
| 5 | froundindex | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |
| 6 | freviewernewer | 评审发起人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fapprovesubmittime | 审批提交时间 | timestamp | 0 |  |  | null | 审批提交时间 |
| 8 | fendreviewtime | fendreviewtime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_roundidex |  | froundindex |
| 2 | pk_t_clm_contractdraft_r |  | fid |

---

## 合同起草-分表 t_clm_contractdraft_m

- **表名称：** 合同起草-分表
- **表名：** t_clm_contractdraft_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconpaymenttextdatas | 合同款项样例数据 | text | 0 |  |  | null | 合同款项样例数据 |
| 3 | fcontractpayment | 合同款项方案 | int8 | 64 |  | √ | 0 | 合同款项方案 clm_contract_payment_plan |
| 4 | fconpaymenttextdatas_tag | 合同款项样例数据_详情 | text | 0 |  |  | null | 合同款项样例数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_contract_draft_money |  | fcontractpayment |
| 2 | pk_t_clm_contractdraft_m |  | fid |

---

## 合同起草-多语言表 t_clm_contractdraft_l

- **表名称：** 合同起草-多语言表
- **表名：** t_clm_contractdraft_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 3 | fcounterpartycontact | 合同相对方联系人 | varchar | 50 |  | √ | ' ' | 合同相对方联系人 |
| 4 | fconsubjecaccountbankname | 合同主体开户行名称 | varchar | 100 |  | √ | ' ' | 合同主体开户行名称 |
| 5 | fdisputeresolutionplace | 争议解决地 | varchar | 100 |  | √ | ' ' | 争议解决地 |
| 6 | fcounterpartyaccbankname | 合同相对方开户行名称 | varchar | 100 |  | √ | ' ' | 合同相对方开户行名称 |
| 7 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 8 | fconsubjectaccountname | fconsubjectaccountname | varchar | 100 |  | √ | ' ' |  |
| 9 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |
| 10 | fcontractplace | 合同签订地点 | varchar | 100 |  | √ | ' ' | 合同签订地点 |
| 11 | fcounterpartyaccountname | 合同相对方账户名称 | varchar | 100 |  | √ | ' ' | 合同相对方账户名称 |
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

## 合同起草-主表 t_clm_contractdraft

- **表名称：** 合同起草-主表
- **表名：** t_clm_contractdraft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 3 | fcontractdate | 签订日期（数字） | timestamp | 0 |  |  | null | 签订日期（数字） |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 6 | fcounterpartyaccbankname | 合同相对方开户行名称 | varchar | 100 |  | √ | ' ' | 合同相对方开户行名称 |
| 7 | fcontractcopies | 合同份数 | int4 | 32 |  | √ | 0 | 合同份数 |
| 8 | fisreviewing | 是否发起评审 | bpchar | 1 |  | √ | '0' | 是否发起评审 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fisfromreview | 是否从合同评审起草 | bpchar | 1 |  | √ | '0' | 是否从合同评审起草 |
| 12 | fcounterparty | 合同相对方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fcounterpartycontactphone | 合同相对方联系人电话 | varchar | 50 |  | √ | ' ' | 合同相对方联系人电话 |
| 14 | fcounterpartyfax | 合同相对方传真 | varchar | 50 |  | √ | ' ' | 合同相对方传真 |
| 15 | fdrafttype | 合同起草方式 | varchar | 50 |  | √ | ' ' | 合同起草方式,枚举: FROM_TPL :模板起草 FROM_UPLOAD :上传文件起草 |
| 16 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbillno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 18 | fcontracttype | 合同类型 | int8 | 64 |  | √ | 0 | 合同类型 conm_type |
| 19 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 20 | fcounterpartycontact | 合同相对方联系人 | varchar | 50 |  | √ | ' ' | 合同相对方联系人 |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcontractstatus | 合同进度 | varchar | 50 |  | √ | ' ' | 合同进度,枚举: SAVE :起草中 CONFIRM_FILLING :已起草 TO_REVIEW :评审中 TO_AUDIT :审批中 REJECTED :已驳回 REVIEWED :已审批 SIGNED :已签章 PERFORMANCE :履行中 COMPLETED :已完成 |
| 23 | fconsubjecaccountbankname | 合同主体开户行名称 | varchar | 255 |  | √ | ' ' | 合同主体开户行名称 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fsalorg | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fcontractplace | 合同签订地点 | varchar | 200 |  | √ | ' ' | 合同签订地点 |
| 27 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 28 | fcounterpartyaccountname | 合同相对方账户名称 | varchar | 100 |  | √ | ' ' | 合同相对方账户名称 |
| 29 | ftax | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 30 | fexchangetype | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 31 | ffileid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 32 | fconsubjectaddress | 合同主体地址 | varchar | 255 |  | √ | ' ' | 合同主体地址 |
| 33 | fconsubjectbillinginfo | 合同主体开票信息 | varchar | 50 |  | √ | ' ' | 合同主体开票信息 |
| 34 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 35 | fsettlecurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fisallowededit | 使用模板在线起草时，允许编辑模板文本 | bpchar | 1 |  | √ | '0' | 使用模板在线起草时，允许编辑模板文本 |
| 38 | fcounterpartybankaccount | 合同相对方银行账号 | varchar | 100 |  | √ | ' ' | 合同相对方银行账号 |
| 39 | fconsubjectpostcode | 合同主体邮编 | varchar | 255 |  | √ | ' ' | 合同主体邮编 |
| 40 | ftotalallamountinwords | 合同总金额（中文） | varchar | 100 |  | √ | ' ' | 合同总金额（中文） |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fconsubjectcontactmail | 合同主体联系人邮箱 | varchar | 50 |  | √ | ' ' | 合同主体联系人邮箱 |
| 43 | fsignstatus | 签章状态 | varchar | 50 |  | √ | ' ' | 签章状态,枚举: NOT_SIGN :未签章 SIGNED :已签章 |
| 44 | fconsubjectcontactphone | 合同主体联系人电话 | varchar | 100 |  | √ | ' ' | 合同主体联系人电话 |
| 45 | fcounterpartycontactpost | 合同相对方联系人邮箱 | varchar | 50 |  | √ | ' ' | 合同相对方联系人邮箱 |
| 46 | fcounterpartycreditcode | 合同相对方统一社会信用代码 | varchar | 100 |  | √ | ' ' | 合同相对方统一社会信用代码 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 49 | fcounterpartypostcode | 合同相对方邮编 | varchar | 50 |  | √ | ' ' | 合同相对方邮编 |
| 50 | fcounterpartybillinginfo | 合同相对方开票信息 | varchar | 50 |  | √ | ' ' | 合同相对方开票信息 |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fcounterpartytype | 合同相对方类型 | varchar | 50 |  | √ | ' ' | 合同相对方类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 53 | fconsubjectaccountbank | 合同主体银行账号 | varchar | 50 |  | √ | ' ' | 银行账户 bd_accountbanks |
| 54 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 55 | fconsubjectfax | 合同主体传真 | varchar | 50 |  | √ | ' ' | 合同主体传真 |
| 56 | fdisputeresolutionplace | 争议解决地 | varchar | 200 |  | √ | ' ' | 争议解决地 |
| 57 | fconsubjectmailbox | 合同主体邮箱 | varchar | 200 |  | √ | ' ' | 合同主体邮箱 |
| 58 | fconsubjectaccountname | 合同主体账户名称 | varchar | 100 |  | √ | ' ' | 合同主体账户名称 |
| 59 | fconsubjectcontact | 合同主体联系人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 60 | fcounterpartymail | 合同相对方邮箱 | varchar | 50 |  | √ | ' ' | 合同相对方邮箱 |
| 61 | fcontractdateinword | 签订日期（中文） | varchar | 50 |  | √ | ' ' | 签订日期（中文） |
| 62 | fcounterpartyphone | 合同相对方电话 | varchar | 100 |  | √ | ' ' | 合同相对方电话 |
| 63 | fcontractfilecopies | 合同附件份数 | int4 | 32 |  | √ | 0 | 合同附件份数 |
| 64 | fcounterpartyaddress | 合同相对方地址 | varchar | 200 |  | √ | ' ' | 合同相对方地址 |
| 65 | fcontractsubject | 合同主体 | int8 | 64 |  | √ | 0 | 合同主体 conm_contparties |
| 66 | fconsubjectcreditcode | 合同主体统一社会信用代码 | varchar | 255 |  | √ | ' ' | 合同主体统一社会信用代码 |
| 67 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 68 | fconsubjectphone | 合同主体电话 | varchar | 100 |  | √ | ' ' | 合同主体电话 |
| 69 | ftotalallamount | 合同总金额（数字） | numeric | 23 | 10 | √ | 0 | 合同总金额（数字） |

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

---

## 合同起草-分表 t_clm_contractdraft_c

- **表名称：** 合同起草-分表
- **表名：** t_clm_contractdraft_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclausedatas_tag | 合同条款数据_详情 | text | 0 |  |  | null | 合同条款数据_详情 |
| 3 | fclausedatas | 合同条款数据 | text | 0 |  |  | null | 合同条款数据 |
| 4 | fclauseid | fclauseid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_contractdraft_c |  | fid |
| 2 | idx_contract_draft_clause |  | fclauseid |

---

## 轮次评审人-子表 t_clm_contract_review_ro

- **表名称：** 轮次评审人-子表
- **表名：** t_clm_contract_review_ro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freviewstatus | 评审状态 | varchar | 50 |  | √ | ' ' | 评审状态,枚举: NEW_REVIEW :发起评审 NOT_VIEWED :未查看 NEW_ROUND_REVIEW :发起新一轮评审 REVIEWING :正在评审 PASS :评审通过 UNPASS :评审不通过 END_THIS_ROUND :结束本轮评审 |
| 3 | freviewerdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | frevieweremark | 转办信息 | varchar | 50 |  | √ | ' ' | 转办信息 |
| 6 | freviewerround | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freviewer | 评审人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | freviewerrole | 评审角色 | varchar | 50 |  | √ | ' ' | 评审角色,枚举: INITIATOR :发起人 PARTICIPANT :参与人 |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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

---

## 评审说明单据体（隐藏）-子表 t_clm_contract_review_re

- **表名称：** 评审说明单据体（隐藏）-子表
- **表名：** t_clm_contract_review_re

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 3 | fremarktime | 时间 | timestamp | 0 |  |  | null | 时间 |
| 4 | fremarkuser | 评审说明人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fremarkround | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_clm_contract_review_re |  | fentryid |
| 2 | idx_clm_contract_review_re_fk |  | fid |
