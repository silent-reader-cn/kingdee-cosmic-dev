# 融资申请-cfm_loan_apply

## 融资申请-分表 t_cfm_loanapply_e

- **表名称：** 融资申请-分表
- **表名：** t_cfm_loanapply_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: lc_present :交单处理 lc_arrival :到单处理 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_loanapply_e |  | fid |
| 2 | idx_cfm_loanapply_e |  | fsourcebilltype |

---

## 融资申请-多语言表 t_cfm_loanapply_l

- **表名称：** 融资申请-多语言表
- **表名：** t_cfm_loanapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 融资用途 | varchar | 255 |  | √ | ' ' | 融资用途 |
| 5 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loan_l_applyid |  | fid |
| 2 | pk_t_cfm_loanapply_l |  | fpkid |

---

## 融资申请-关联追踪表 t_cfm_loanapply_tc

- **表名称：** 融资申请-关联追踪表
- **表名：** t_cfm_loanapply_tc

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
| 1 | idx_cfm_loanapply_tc_tid |  | ftid |
| 2 | idx_cfm_loanapply_tc_tbill |  | ftbillid |
| 3 | pk_cfm_loanapply_tc |  | fid |

---

## 融资申请-主表 t_cfm_loanapply

- **表名称：** 融资申请-主表
- **表名：** t_cfm_loanapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 30 |  | √ | ' ' | 期限（ymd） |
| 3 | fratecycle | 利率重置周期 | int4 | 32 |  | √ | 0 | 利率重置周期 |
| 4 | flender | flender | varchar | 255 |  | √ | ' ' |  |
| 5 | fapplicat | 申请人 | varchar | 255 |  | √ | ' ' | 申请人 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | fenddate | 预计结束日期 | timestamp | 0 |  |  | null | 预计结束日期 |
| 9 | fcreditorid | 债权人Id | int8 | 64 |  | √ | 0 | 债权人Id |
| 10 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 11 | fratefloatpoint | 利率浮动基点 | numeric | 23 | 10 | √ | 0.0000000000 | 利率浮动基点 |
| 12 | fcreditordatatype | fcreditordatatype | varchar | 50 |  | √ | ' ' |  |
| 13 | ffloatingratio | 逾期利率浮动比例（%） | numeric | 23 | 10 | √ | 0 | 逾期利率浮动比例（%） |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 16 | flendernature | flendernature | varchar | 50 |  | √ | ' ' |  |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 19 | fconversiondays | 利率转换天数（废弃） | varchar | 50 |  | √ | ' ' | 利率转换天数（废弃）,枚举: 360 :360 365 :365 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 融资用途 | varchar | 255 |  | √ | ' ' | 融资用途 |
| 23 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 24 | frepaymentway | 还款方式 | varchar | 50 |  | √ | ' ' | 还款方式,枚举: bqhblsbq :到期还本，利随本清 dqhblsbq :定期还本，利随本清 bqhbdqhx :到期还本，定期还息 dqhbdqhx :定期还本，定期还息 debx :等额本息 debj :等额本金 dbdx :等本等息 zdyhk :自定义还款 |
| 25 | fstartdate | 预计开始日期 | timestamp | 0 |  |  | null | 预计开始日期 |
| 26 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: bank :银行 finorg :非银金融机构 settlecenter :结算中心 innerunit :内部单位 custom :客商 other :其他 |
| 27 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 28 | fratecyclesign | 利率重置周期 | varchar | 30 |  | √ | ' ' | 利率重置周期,枚举: D :按天 W :按周 M :按月 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | faccountbankid | 借款人银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 31 | flocamt | 金额折本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 金额折本位币 |
| 32 | fcompanyid | 借款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 34 | floanperson | floanperson | int8 | 64 |  | √ | 0 |  |
| 35 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 36 | fisneedscheme | 需出具方案 | varchar | 30 |  | √ | ' ' | 需出具方案 |
| 37 | famount | 借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额 |
| 38 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 40 | fbusinessstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :办理中 3 :未办理 4 :已办理 5 :已退单 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 1 :信用 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :无担保 |
| 44 | floantype | 融资业务分类 | varchar | 50 |  | √ | ' ' | 融资业务分类,枚举: loan :普通贷款 entrust :委托贷款 sl :银团贷款 ec :企业往来 |
| 45 | fratetypeid | 参考利率 | int8 | 64 |  | √ | 0 | [参考利率表 tbd_referrate](../fbd_files/tbd_referrate.md) |
| 46 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 47 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 48 | fadjustcycle | fadjustcycle | varchar | 19 |  | √ | ' ' |  |
| 49 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | finterestrate | 贷款年利率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 贷款年利率（%） |
| 51 | finterestsettledplanid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 52 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 53 | fcreditlimitid | 预占授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 54 | fratedeadlineid | 利率期限(废弃) | int8 | 64 |  | √ | 0 | [期限类别码表 fbd_termcategorycode](../fbd_files/fbd_termcategorycode.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_loan_applyorg |  | fcompanyid |
| 2 | pk_t_cfm_loanapply |  | fid |
| 3 | idx_cfm_loan_applysta |  | fbillstatus,fbizdate,floantype |

---

## 单据体-子表 t_cfm_loanapply_entry

- **表名称：** 单据体-子表
- **表名：** t_cfm_loanapply_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feschemeid | 方案编码 | int8 | 64 |  | √ | 0 | [融资方案 cfm_financingscheme](../cfm_files/cfm_financingscheme.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fereson | 选择原因 | varchar | 255 |  | √ | ' ' | 选择原因 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | feisselect | 方案选择 | bpchar | 1 |  | √ | ' ' | 方案选择 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_loanapply_entry |  | fentryid |
| 2 | idx_cfm_loanapply_entry |  | fid |

---

## 关联子实体-子表 t_cfm_loanapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_loanapply_lk

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
| 1 | idx_cfm_loanapply_lk_fk |  | fid |
| 2 | pk_cfm_loanapply_lk |  | fpkid |

---

## 融资申请-反写记录表 t_cfm_loanapply_wb

- **表名称：** 融资申请-反写记录表
- **表名：** t_cfm_loanapply_wb

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
| 1 | pk_cfm_loanapply_wb |  | fentryid |
| 2 | idx_cfm_loanapply_wb_fk |  | fid |
