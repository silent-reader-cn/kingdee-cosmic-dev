# 文本合同-clm_contractdraft_tpl

## 单据体-子表 t_clm_contract_review_log

- **表名称：** 单据体-子表
- **表名：** t_clm_contract_review_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogroundname | 轮次名称 | varchar | 50 |  | √ | ' ' | 轮次名称 |
| 3 | flogreviewer | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 3 | famountcn | 不含税金额（中文） | varchar | 50 |  | √ | ' ' | 不含税金额（中文） |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 6 | famountandtaxinwords | 价税合计（中文） | varchar | 200 |  | √ | ' ' | 价税合计（中文） |
| 7 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 10 | fprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 11 | fbasesalunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fdiscountamountcn | 折扣额（中文） | varchar | 50 |  | √ | ' ' | 折扣额（中文） |
| 13 | fsalmaterial | 物料名称 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 14 | fcuramount | 不含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 不含税金额(本位币) |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fbasepurunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 21 | fprojectid | 项目名称 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 23 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 24 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 25 | fsalunit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | ftaxamountcn | 税额（中文） | varchar | 50 |  | √ | ' ' | 税额（中文） |
| 27 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 28 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 29 | fentrycomment | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 30 | fpriceandtaxcn | 含税单价（中文） | varchar | 50 |  | √ | ' ' | 含税单价（中文） |
| 31 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fpurmaterial | 物料名称 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 34 | fpurunit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 36 | fpricecn | 不含税单价（中文） | varchar | 50 |  | √ | ' ' | 不含税单价（中文） |

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
| 5 | fmsguser | 留言人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 2 | fpaymentnode | 款项节点 | int8 | 64 |  | √ | 0 | [合同款项节点 clm_contract_payment_node](../clmcd_files/clm_contract_payment_node.md) |
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

## 文本合同-分表 t_clm_contractdraft_t

- **表名称：** 文本合同-分表
- **表名：** t_clm_contractdraft_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftemplatedatas_tag | 合同模板数据_详情 | text | 0 |  |  | null | 合同模板数据_详情 |
| 3 | ftemplatedatas | 合同模板数据 | text | 0 |  |  | null | 合同模板数据 |
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

## 文本合同-分表 t_clm_contractdraft_r

- **表名称：** 文本合同-分表
- **表名：** t_clm_contractdraft_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrentreviewstatus | 当前评审状态 | varchar | 50 |  | √ | ' ' | 当前评审状态,枚举: NEW_REVIEW :发起评审 NEW_ROUND_REVIEW :发起新一轮评审 END_THIS_ROUND :结束本轮评审 TO_AUDIT :已提交审批 REVIEWED :已审批 |
| 3 | fpushtime | 执行下推时间 | timestamp | 0 |  |  | null | 执行下推时间 |
| 4 | fapprovesubmiter | 审批提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | freviewernewtime | 评审发起时间 | timestamp | 0 |  |  | null | 评审发起时间 |
| 6 | froundindex | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |
| 7 | freviewernewer | 评审发起人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fapprovesubmittime | 审批提交时间 | timestamp | 0 |  |  | null | 审批提交时间 |
| 9 | fpusher | 执行下推人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fendreviewtime | fendreviewtime | timestamp | 0 |  |  | null |  |

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

## 文本合同-分表 t_clm_contractdraft_m

- **表名称：** 文本合同-分表
- **表名：** t_clm_contractdraft_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconpaymenttextdatas | 合同款项样例数据 | text | 0 |  |  | null | 合同款项样例数据 |
| 3 | fcontractpayment | 合同款项方案 | int8 | 64 |  | √ | 0 | [合同款项方案 clm_contract_payment_plan](../clmcd_files/clm_contract_payment_plan.md) |
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

## 文本合同-多语言表 t_clm_contractdraft_l

- **表名称：** 文本合同-多语言表
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
| 8 | fconsubjectaccountname | 合同主体账户名称 | varchar | 100 |  | √ | ' ' | 合同主体账户名称 |
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

## 文本合同-主表 t_clm_contractdraft

- **表名称：** 文本合同-主表
- **表名：** t_clm_contractdraft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | fcontractdate | 签章日期（数字） | timestamp | 0 |  |  | null | 签章日期（数字） |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 合同不含税总额（数字） | numeric | 23 | 10 | √ | 0 | 合同不含税总额（数字） |
| 6 | fcounterpartyaccbankname | 合同相对方开户行名称 | varchar | 100 |  | √ | ' ' | 合同相对方开户行名称 |
| 7 | fcontractcopies | 合同份数 | int4 | 32 |  | √ | 0 | 合同份数 |
| 8 | fisreviewing | 是否发起评审 | bpchar | 1 |  | √ | '0' | 是否发起评审 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fisfromreview | 是否从合同评审起草 | bpchar | 1 |  | √ | '0' | 是否从合同评审起草 |
| 12 | fisamountbaseonobj | 明细金额汇总 | bpchar | 1 |  | √ | '1' | 明细金额汇总 |
| 13 | fcounterparty | 合同相对方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fcounterpartycontactphone | 合同相对方联系人电话 | varchar | 50 |  | √ | ' ' | 合同相对方联系人电话 |
| 15 | fcounterpartyfax | 合同相对方传真 | varchar | 50 |  | √ | ' ' | 合同相对方传真 |
| 16 | fdrafttype | 合同起草方式 | varchar | 50 |  | √ | ' ' | 合同起草方式,枚举: FROM_TPL :模板起草 FROM_UPLOAD :上传文件起草 |
| 17 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillno | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 19 | ftotalamountcn | 合同不含税总额（中文） | varchar | 50 |  | √ | ' ' | 合同不含税总额（中文） |
| 20 | fcontracttype | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 21 | fname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 22 | fcounterpartycontact | 合同相对方联系人 | varchar | 50 |  | √ | ' ' | 合同相对方联系人 |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcontractstatus | 合同进度 | varchar | 50 |  | √ | ' ' | 合同进度,枚举: SAVE :起草中 CONFIRM_FILLING :已起草 TO_REVIEW :评审中 TO_AUDIT :审批中 REVIEWED :已审批 REJECTED :已驳回 SIGNED :已签章 PERFORMANCE :已下推 TERMINATED :已终止 |
| 25 | fconsubjecaccountbankname | 合同主体开户行名称 | varchar | 255 |  | √ | ' ' | 合同主体开户行名称 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fsalorg | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fcontractplace | 合同签订地点 | varchar | 200 |  | √ | ' ' | 合同签订地点 |
| 29 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 30 | fcounterpartyaccountname | 合同相对方账户名称 | varchar | 100 |  | √ | ' ' | 合同相对方账户名称 |
| 31 | ftax | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 32 | fexchangetype | 换算方式 | varchar | 30 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 33 | ffileid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 34 | fconsubjectaddress | 合同主体地址 | varchar | 255 |  | √ | ' ' | 合同主体地址 |
| 35 | fconsubjectbillinginfo | 合同主体开票信息 | varchar | 50 |  | √ | ' ' | 合同主体开票信息 |
| 36 | ftotaltaxamount | 合同税额（数字） | numeric | 23 | 10 | √ | 0 | 合同税额（数字） |
| 37 | fsettlecurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | ffilinger | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fisallowededit | 使用模板在线起草时，允许编辑模板文本 | bpchar | 1 |  | √ | '0' | 使用模板在线起草时，允许编辑模板文本 |
| 42 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 43 | fcounterpartybankaccount | 合同相对方银行账号 | varchar | 100 |  | √ | ' ' | 合同相对方银行账号 |
| 44 | fconsubjectpostcode | 合同主体邮编 | varchar | 255 |  | √ | ' ' | 合同主体邮编 |
| 45 | ftotalallamountinwords | 合同总金额（中文） | varchar | 100 |  | √ | ' ' | 合同总金额（中文） |
| 46 | fdocumentid | 电签合同ID | varchar | 50 |  | √ | ' ' | 电签合同ID |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fconsubjectcontactmail | 合同主体联系人邮箱 | varchar | 50 |  | √ | ' ' | 合同主体联系人邮箱 |
| 49 | ffilingstatus | 归档状态 | varchar | 50 |  | √ | ' ' | 归档状态,枚举: A :未归档 B :已归档 |
| 50 | fsignstatus | 签章状态 | varchar | 50 |  | √ | ' ' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 51 | fconsubjectcontactphone | 合同主体联系人电话 | varchar | 100 |  | √ | ' ' | 合同主体联系人电话 |
| 52 | fcounterpartycontactpost | 合同相对方联系人邮箱 | varchar | 50 |  | √ | ' ' | 合同相对方联系人邮箱 |
| 53 | fcounterpartycreditcode | 合同相对方统一社会信用代码 | varchar | 100 |  | √ | ' ' | 合同相对方统一社会信用代码 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fsigner | 签章确认人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | ftotaltaxamountcn | 合同税额（中文） | varchar | 50 |  | √ | ' ' | 合同税额（中文） |
| 57 | fsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 58 | fcounterpartypostcode | 合同相对方邮编 | varchar | 50 |  | √ | ' ' | 合同相对方邮编 |
| 59 | fcounterpartybillinginfo | 合同相对方开票信息 | varchar | 50 |  | √ | ' ' | 合同相对方开票信息 |
| 60 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 61 | fcounterpartytype | 合同相对方类型 | varchar | 50 |  | √ | ' ' | 合同相对方类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 62 | fconsubjectaccountbank | 合同主体银行账号 | varchar | 50 |  | √ | ' ' | 合同主体银行账号 |
| 63 | fcurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 64 | fconsubjectfax | 合同主体传真 | varchar | 50 |  | √ | ' ' | 合同主体传真 |
| 65 | fdisputeresolutionplace | 争议解决地 | varchar | 200 |  | √ | ' ' | 争议解决地 |
| 66 | fconsubjectmailbox | 合同主体邮箱 | varchar | 200 |  | √ | ' ' | 合同主体邮箱 |
| 67 | fconsubjectaccountname | 合同主体账户名称 | varchar | 100 |  | √ | ' ' | 合同主体账户名称 |
| 68 | fcounterpartymail | 合同相对方邮箱 | varchar | 50 |  | √ | ' ' | 合同相对方邮箱 |
| 69 | fconsubjectcontact | 合同主体联系人 | varchar | 60 |  | √ | ' ' | 合同主体联系人 |
| 70 | fcontractdateinword | 签章日期（中文） | varchar | 50 |  | √ | ' ' | 签章日期（中文） |
| 71 | fcounterpartyphone | 合同相对方电话 | varchar | 100 |  | √ | ' ' | 合同相对方电话 |
| 72 | fcontractfilecopies | 合同附件份数 | int4 | 32 |  | √ | 0 | 合同附件份数 |
| 73 | fcounterpartyaddress | 合同相对方地址 | varchar | 200 |  | √ | ' ' | 合同相对方地址 |
| 74 | fcontractsubject | 合同主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 75 | fconsubjectcreditcode | 合同主体统一社会信用代码 | varchar | 255 |  | √ | ' ' | 合同主体统一社会信用代码 |
| 76 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 77 | fconsubjectphone | 合同主体电话 | varchar | 100 |  | √ | ' ' | 合同主体电话 |
| 78 | ftotalallamount | 合同总金额（数字） | numeric | 23 | 10 | √ | 0 | 合同总金额（数字） |

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

## 文本合同-分表 t_clm_contractdraft_c

- **表名称：** 文本合同-分表
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
| 2 | freviewstatus | 评审状态 | varchar | 50 |  | √ | ' ' | 评审状态,枚举: NEW_REVIEW :发起评审 NOT_VIEWED :未查看 NEW_ROUND_REVIEW :发起新一轮评审 REVIEWING :正在评审 PASS :评审通过 UNPASS :评审不通过 END_THIS_ROUND :结束本轮评审 TERMINATED :终止评审 |
| 3 | freviewerdept | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | frevieweremark | 转办信息 | varchar | 50 |  | √ | ' ' | 转办信息 |
| 6 | freviewerround | 轮次 | int8 | 64 |  | √ | 0 | 轮次 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | freviewer | 评审人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | freviewerrole | 评审角色 | varchar | 50 |  | √ | ' ' | 评审角色,枚举: INITIATOR :发起人 PARTICIPANT :参与人 |
| 10 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 4 | fremarkuser | 评审说明人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
