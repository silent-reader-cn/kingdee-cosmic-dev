# 余额调节表-cas_balanceadjust

## 单据体-子表 t_cas_unbankdetail

- **表名称：** 单据体-子表
- **表名：** t_cas_unbankdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvouchertype | 凭证类型 | varchar | 50 |  | √ | ' ' | 凭证类型 |
| 3 | fpddate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 4 | fbanksourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型 |
| 5 | forgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsettlenumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 8 | fbanksource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 1 :手工录入 2 :单据生成 3 :标准导入 4 :凭证登帐 |
| 9 | fcashier | 出纳 | varchar | 100 |  | √ | ' ' | 出纳 |
| 10 | favddate | 期望付款日期 | timestamp | 0 |  |  | null | 期望付款日期 |
| 11 | fbankbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 12 | fsettletype | 结算方式 | varchar | 50 |  | √ | ' ' | 结算方式 |
| 13 | fvouchernumber | 凭证字号 | varchar | 1024 |  | √ | ' ' | 凭证字号 |
| 14 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 15 | fcreditamount | 企业已付银行未付 | numeric | 19 | 6 | √ | 0.000000 | 企业已付银行未付 |
| 16 | freason | 未达原因 | varchar | 255 |  | √ | ' ' | 未达原因 |
| 17 | fdebitamount | 企业已收银行未收 | numeric | 19 | 6 | √ | 0.000000 | 企业已收银行未收 |
| 18 | fpreparationdate | 制单日期 | timestamp | 0 |  |  | null | 制单日期 |
| 19 | fbillnumber | 单据编号 | varchar | 1024 |  | √ | ' ' | 单据编号 |
| 20 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 21 | ffeepayer | 手续费承担方 | varchar | 50 |  | √ | ' ' | 手续费承担方,枚举: 01 :付款方 02 :收款方 03 :共同承担 |
| 22 | fsysdate | 系统日期 | timestamp | 0 |  |  | null | 系统日期 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fbilltype | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_unbankdetail_fid |  | fid |
| 2 | pk_t_cas_unbankdetail |  | fentryid |
| 3 | idx_cas_unbankdetail_bd |  | fbankbillid,fbanksourcetype |

---

## 单据体-子表 t_cas_uncompanydetail

- **表名称：** 单据体-子表
- **表名：** t_cas_uncompanydetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettletype | 结算方式 | varchar | 50 |  | √ | ' ' | 结算方式 |
| 3 | fbankvouvherno | 明细流水号 | varchar | 50 |  | √ | ' ' | 明细流水号 |
| 4 | fratesdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 5 | ftradenumber | 业务参考号 | varchar | 50 |  | √ | ' ' | 业务参考号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsettlenumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 8 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 9 | fcreditamount | 银行已收企业未收 | numeric | 19 | 6 | √ | 0.000000 | 银行已收企业未收 |
| 10 | freason | 未达原因 | varchar | 255 |  | √ | ' ' | 未达原因 |
| 11 | fdebitamount | 银行已付企业未付 | numeric | 19 | 6 | √ | 0.000000 | 银行已付企业未付 |
| 12 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 1 :银行交易下载 2 :内部金融机构下载 3 :手工引入 4 :手工新增 |
| 13 | fbalanceamt | 余额 | numeric | 19 | 6 | √ | 0.000000 | 余额 |
| 14 | fsourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型 |
| 15 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 16 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_uncompanydetail_bi |  | fbillid,fsettletype |
| 2 | pk_t_cas_uncompanydetail |  | fentryid |

---

## 余额调节表-主表 t_cas_bankbalanceadjust

- **表名称：** 余额调节表-主表
- **表名：** t_cas_bankbalanceadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankaccountid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdiffamount | 差异 | numeric | 19 | 6 | √ | 0.000000 | 差异 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fjournalbalamt | 日记账余额 | numeric | 19 | 6 | √ | 0.000000 | 日记账余额 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 9 | fimageno | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 10 | fadjuststatementamt | 调整后余额 | numeric | 19 | 6 | √ | 0.000000 | 调整后余额 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbankgotamt | 加：企业未收 | numeric | 19 | 6 | √ | 0.000000 | 加：企业未收 |
| 14 | fperiodid | 期初期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审批 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fbankaccountnumber | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fentprgotamt | 加：银行未收 | numeric | 19 | 6 | √ | 0.000000 | 加：银行未收 |
| 20 | fentprpayedamt | 减：银行未付 | numeric | 19 | 6 | √ | 0.000000 | 减：银行未付 |
| 21 | fadjustjournalamt | 调整后余额 | numeric | 19 | 6 | √ | 0.000000 | 调整后余额 |
| 22 | fbizdate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 23 | fbankcgsetting | 银行类别 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 24 | fstatmntbalamt | 对账单余额 | numeric | 19 | 6 | √ | 0.000000 | 对账单余额 |
| 25 | fbankpayedamt | 减：企业未付 | numeric | 19 | 6 | √ | 0.000000 | 减：企业未付 |
| 26 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_bankbalanceadjust_pkey |  | fid |
| 2 | idx_cas_pbe_forgid |  | forgid |
