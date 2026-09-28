# 借款合同展期单-cfm_contractextend_loan

## 借款合同展期单-主表 t_cfm_extendbill

- **表名称：** 借款合同展期单-主表
- **表名：** t_cfm_extendbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontractbizdate | fcontractbizdate | timestamp | 0 |  |  | null |  |
| 3 | flender | flender | varchar | 80 |  | √ | ' ' |  |
| 4 | frenewalexpiredate | 展期后合同到期日期 | timestamp | 0 |  |  | null | 展期后合同到期日期 |
| 5 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fenddate | 合同结束日期 | timestamp | 0 |  |  | null | 合同结束日期 |
| 9 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 11 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0.000000 | 利率浮动基点 |
| 12 | fbillno | 展期单编号 | varchar | 80 |  | √ | ' ' | 展期单编号 |
| 13 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 14 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 15 | flendernature | 贷款人性质 | varchar | 30 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcontractname | fcontractname | varchar | 255 |  | √ | ' ' |  |
| 18 | frenewalinteresttype | 利率类型 | varchar | 30 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fdescription | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 21 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 22 | fstartdate | 合同开始日期 | timestamp | 0 |  |  | null | 合同开始日期 |
| 23 | fcontractbillno | 合同单据编号 | varchar | 80 |  | √ | ' ' | 合同单据编号 |
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 bond :债券 ifm :内部金融管理 |
| 25 | fconfirmtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 28 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 29 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 30 | frateadjustcycle | 利率重置周期 | int8 | 64 |  | √ | 0 | 利率重置周期 |
| 31 | frenewalinterestrate | 展期利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 展期利率（%） |
| 32 | fnotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 33 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: registrying :登记中 waitconfirm :待确认 yetconfirm :已确认 yetreturn :已退回 |
| 34 | fcompanyer | fcompanyer | varchar | 30 |  | √ | ' ' |  |
| 35 | famount | 借款金额 | numeric | 19 | 6 | √ | 0.000000 | 借款金额 |
| 36 | freturnreason | 退回原因 | varchar | 255 |  | √ | ' ' | 退回原因 |
| 37 | fisinit | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fdrawamount | 已提款金额 | numeric | 19 | 6 | √ | 0.000000 | 已提款金额 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fcontractno | fcontractno | varchar | 80 |  | √ | ' ' |  |
| 43 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 44 | floantype | 贷款类型 | varchar | 30 |  | √ | ' ' | 贷款类型,枚举: loan :银行贷款 entrust :企业贷款 |
| 45 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fbizdate | 展期签订日期 | timestamp | 0 |  |  | null | 展期签订日期 |
| 48 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 49 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | fratesign | 利率浮动基点（BP） | varchar | 80 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 51 | fprotocolno | 展期协议号 | varchar | 80 |  | √ | ' ' | 展期协议号 |
| 52 | fratedeadlineid | fratedeadlineid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_extendbill_sid |  | fsourcebillid |
| 2 | idx_t_cfm_extendbill_bns |  | fbillno,fbillstatus |
| 3 | t_cfm_extendbill_pkey |  | fid |

---

## 借款合同展期单-关联追踪表 t_cfm_extendbill_tc

- **表名称：** 借款合同展期单-关联追踪表
- **表名：** t_cfm_extendbill_tc

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
| 1 | idx_t_cfm_extendbill_tc |  | ftbillid |
| 2 | t_cfm_extendbill_tc_pkey |  | fid |
| 3 | idx_cfm_extendbill_tc_tid |  | ftid |
| 4 | idx_cfm_extendbill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_cfm_extendbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_extendbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_extendbill_lk |  | fid |
| 2 | t_cfm_extendbill_lk_pkey |  | fpkid |

---

## 借款合同展期单-多语言表 t_cfm_extendbill_l

- **表名称：** 借款合同展期单-多语言表
- **表名：** t_cfm_extendbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 3 | fcontractname | fcontractname | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_extendbill_l_pkey |  | fpkid |
| 2 | idx_t_cfm_extendbill_l |  | fid,flocaleid |

---

## 借款合同展期单-分表 t_cfm_extendbill_e

- **表名称：** 借款合同展期单-分表
- **表名：** t_cfm_extendbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftextdebtor | 借款人 | varchar | 255 |  | √ | ' ' | 借款人 |
| 3 | fprevrenewalexpiredate | 展期前合同到期日期 | timestamp | 0 |  |  | null | 展期前合同到期日期 |
| 4 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 5 | freferrateid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 6 | forgid | 借款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 8 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 9 | ftextcreditor | 债权人 | varchar | 255 |  | √ | ' ' | 债权人 |
| 10 | frateadjustcycletype | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 11 | fsettlestatus | 提交结算中心状态 | varchar | 30 |  | √ | ' ' | 提交结算中心状态,枚举: addnew :新增 submit :已提交 accept :已受理 bitback :已退回 |
| 12 | fisadjustinterestrate | 调整利率 | bpchar | 1 |  | √ | '0' | 调整利率 |
| 13 | fextendapplyid | 展期申请 | int8 | 64 |  | √ | 0 | [展期申请 cfm_extapplybill_f7](../cfm_files/cfm_extapplybill_f7.md) |
| 14 | frenewalnum | 展期次数 | int4 | 32 |  | √ | 0 | 展期次数 |
| 15 | fbizdealno | fbizdealno | varchar | 80 |  | √ | ' ' |  |
| 16 | fcreditorgid | 债权组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbondtype | fbondtype | varchar | 50 |  | √ | ' ' |  |
| 18 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 19 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: bank :银行 finorg :非银行金融机构 custom :客商 other :其他 |
| 20 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_extendbill_e_orgid |  | forgid |
| 2 | pk_t_cfm_extendbill_e |  | fid |
| 3 | idx_cfm_extendbill_e_pfid |  | fproductfactoryid |

---

## 提款展期单据体-子表 t_cfm_extendbill_entry

- **表名称：** 提款展期单据体-子表
- **表名：** t_cfm_extendbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdrawcurrencyid | 提款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fprevrenewalexpiredate | 展期前到期日期 | timestamp | 0 |  |  | null | 展期前到期日期 |
| 4 | finteresttype | finteresttype | varchar | 20 |  | √ | ' ' |  |
| 5 | fdrawbillno | 提款单编号 | varchar | 80 |  | √ | ' ' | 提款单编号 |
| 6 | fextendamount | 展期金额 | numeric | 19 | 6 | √ | 0.000000 | 展期金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | flnotrepayamount | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 9 | fisadjustinterestrate | fisadjustinterestrate | bpchar | 1 |  | √ | '0' |  |
| 10 | frepayamount | 已还本金 | numeric | 19 | 6 | √ | 0.000000 | 已还本金 |
| 11 | frateadjuststyle | frateadjuststyle | varchar | 80 |  | √ | ' ' |  |
| 12 | fisrenewal | 展期 | bpchar | 1 |  | √ | '0' | 展期 |
| 13 | floanrate | 放款利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 放款利率（%） |
| 14 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 15 | freferencerateid | freferencerateid | int8 | 64 |  | √ | 0 |  |
| 16 | fdrawbillid | 提款单主键 | int8 | 64 |  | √ | 0 | 提款单主键 |
| 17 | fratefloatpoint | fratefloatpoint | numeric | 19 | 6 | √ | 0 |  |
| 18 | fldrawamount | 提款金额 | numeric | 19 | 6 | √ | 0.000000 | 提款金额 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | floandate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 21 | fexrateadjustdate | 首次展期利率调整日 | timestamp | 0 |  |  | null | 首次展期利率调整日 |
| 22 | flrenewalexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 23 | fratesign | fratesign | varchar | 80 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_extendbill_entry_pkey |  | fentryid |
| 2 | idx_t_cfm_extendbill_entry |  | fid |

---

## 借款合同展期单-反写记录表 t_cfm_extendbill_wb

- **表名称：** 借款合同展期单-反写记录表
- **表名：** t_cfm_extendbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_extendbill_wb_pkey |  | fentryid |
| 2 | idx_t_cfm_extendbill_wb |  | fid |
