# 融资申请-cfm_loan_apply_f7

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
| 2 | fbitbackinfo | fbitbackinfo | varchar | 255 |  | √ | ' ' |  |
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

## 融资申请-主表 t_cfm_loanapply

- **表名称：** 融资申请-主表
- **表名：** t_cfm_loanapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | fterm | varchar | 30 |  | √ | ' ' |  |
| 3 | fratecycle | fratecycle | int4 | 32 |  | √ | 0 |  |
| 4 | flender | flender | varchar | 255 |  | √ | ' ' |  |
| 5 | fapplicat | fapplicat | varchar | 255 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 9 | fcreditorid | fcreditorid | int8 | 64 |  | √ | 0 |  |
| 10 | fbitbackinfo | fbitbackinfo | varchar | 255 |  | √ | ' ' |  |
| 11 | fratefloatpoint | fratefloatpoint | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fcreditordatatype | fcreditordatatype | varchar | 50 |  | √ | ' ' |  |
| 13 | ffloatingratio | ffloatingratio | numeric | 23 | 10 | √ | 0 |  |
| 14 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 15 | fclientorgid | fclientorgid | int8 | 64 |  | √ | 0 |  |
| 16 | flendernature | flendernature | varchar | 50 |  | √ | ' ' |  |
| 17 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 18 | ffinproductid | ffinproductid | int8 | 64 |  | √ | 0 |  |
| 19 | fconversiondays | fconversiondays | varchar | 50 |  | √ | ' ' |  |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | fdescription | 融资用途 | varchar | 255 |  | √ | ' ' | 融资用途 |
| 23 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 24 | frepaymentway | frepaymentway | varchar | 50 |  | √ | ' ' |  |
| 25 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 26 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: outgroup :银行 nonbank :非银金融机构 ingroup :内部单位 merchants :客商 other :其他 |
| 27 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 28 | fratecyclesign | fratecyclesign | varchar | 30 |  | √ | ' ' |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | faccountbankid | faccountbankid | int8 | 64 |  | √ | 0 |  |
| 31 | flocamt | flocamt | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fcompanyid | 借款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 34 | floanperson | floanperson | int8 | 64 |  | √ | 0 |  |
| 35 | finteresttype | finteresttype | varchar | 50 |  | √ | ' ' |  |
| 36 | fisneedscheme | 需出具方案 | varchar | 30 |  | √ | ' ' | 需出具方案 |
| 37 | famount | 借款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款金额 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 40 | fbusinessstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :办理中 3 :未办理 4 :已办理 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fguarantee | fguarantee | varchar | 50 |  | √ | ' ' |  |
| 44 | floantype | 融资业务分类 | varchar | 50 |  | √ | ' ' | 融资业务分类,枚举: bankloan :普通贷款 entrustloan :委托贷款 banksloan :银团贷款 linklend :企业往来 |
| 45 | fratetypeid | fratetypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 47 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 48 | fadjustcycle | fadjustcycle | varchar | 19 |  | √ | ' ' |  |
| 49 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | finterestrate | finterestrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 51 | finterestsettledplanid | finterestsettledplanid | int8 | 64 |  | √ | 0 |  |
| 52 | fratesign | fratesign | varchar | 50 |  | √ | ' ' |  |
| 53 | fcreditlimitid | 预占授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 54 | fratedeadlineid | fratedeadlineid | int8 | 64 |  | √ | 0 |  |

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
