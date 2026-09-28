# 已对账结果-cas_checkedresult

## 已对账结果-主表 t_cas_checkedresult

- **表名称：** 已对账结果-主表
- **表名：** t_cas_checkedresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatedirection | 对账单方向 | varchar | 30 |  | √ | ' ' | 对账单方向,枚举: debit :借方 credit :贷方 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fbatchno | 对账批次号 | varchar | 5 |  | √ | ' ' | 对账批次号 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmatchrule_tag | 对账匹配规则_详情 | text | 0 |  |  | null | 对账匹配规则_详情 |
| 8 | fjournaldirection | 分户账方向 | varchar | 30 |  | √ | ' ' | 分户账方向,枚举: debit :借方 credit :贷方 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fchecktype | 对账方式 | varchar | 30 |  | √ | ' ' | 对账方式,枚举: byauto :自动对账 byhand :手工对账 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmatchruleid | 匹配规则ID | int8 | 64 |  | √ | 0 | 匹配规则ID |
| 13 | fmatchrule | 对账匹配规则 | text | 0 |  |  | null | 对账匹配规则 |
| 14 | fstateamount | 对账单金额 | numeric | 19 | 6 | √ | 0.000000 | 对账单金额 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcheckdate | 对账日期 | timestamp | 0 |  |  | null | 对账日期 |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fjournalamount | 分户账金额 | numeric | 19 | 6 | √ | 0.000000 | 分户账金额 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 22 | fcompanyid | 所有权组织（主对账组织） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_checkedresult_pkey |  | fid |
| 2 | index_cas_checked_orgacct |  | faccountbankid,fcurrencyid,fcompanyid |

---

## 单据体-子表 t_cas_checkedresultentry

- **表名称：** 单据体-子表
- **表名：** t_cas_checkedresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpddate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 3 | fbankcheckflag | 对账标识码(旧) | varchar | 1024 |  | √ | ' ' | 对账标识码(旧) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | foppunit | 对方单位 | varchar | 255 |  | √ | ' ' | 对方单位 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbankcheckflagtag_tag | 对账标识码_详情 | text | 0 |  |  | null | 对账标识码_详情 |
| 8 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 1 :银行交易下载 2 :内部金融机构下载 3 :手工引入 4 :手工新增 01 :手工录入 02 :单据生成 03 :标准导入 04 :凭证登帐 |
| 9 | fcashier | 出纳 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | favddate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 11 | fsettlementtype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 12 | fsettlementnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 13 | foppacctnumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 14 | fbankvouvherno | 银行流水号 | varchar | 255 |  | √ | ' ' | 银行流水号 |
| 15 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象,枚举: cas_bankstatement :银行对账单 cas_bankjournal :银行日记账 |
| 16 | fvouchernumber | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 17 | ftradenumber | 业务参考号 | varchar | 255 |  | √ | ' ' | 业务参考号 |
| 18 | fcreditamount | 贷方金额 | numeric | 19 | 6 | √ | 0.000000 | 贷方金额 |
| 19 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 20 | fdebitamount | 借方金额 | numeric | 19 | 6 | √ | 0.000000 | 借方金额 |
| 21 | fbalanceamt | 余额 | numeric | 19 | 6 | √ | 0.000000 | 余额 |
| 22 | fbizobjectid | 业务对象id | int8 | 64 |  | √ | 0 | 业务对象id |
| 23 | fsourcebillnumber | 单据号 | varchar | 255 |  | √ | ' ' | 单据号 |
| 24 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 25 | fsysdate | 系统日期 | timestamp | 0 |  |  | null | 系统日期 |
| 26 | fbankcheckflagtag | 对账标识码 | text | 0 |  |  | null | 对账标识码 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fischeck | 是否勾对 | bpchar | 1 |  | √ | '1' | 是否勾对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cas_checkedentry_fpid |  | fid |
| 2 | index_cas_checkedentry_date |  | fbizdate |
| 3 | t_cas_checkedresultentry_pkey |  | fentryid |
