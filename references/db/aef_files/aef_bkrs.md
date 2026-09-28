# 银行对账单-aef_bkrs

## 单据体-子表 t_aef_bkrsentry

- **表名称：** 单据体-子表
- **表名：** t_aef_bkrsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinessproductstype | 业务产品种类 | varchar | 200 |  | √ | ' ' | 业务产品种类 |
| 3 | fsourcevouchernumber | 原始凭证号码 | varchar | 200 |  | √ | ' ' | 原始凭证号码 |
| 4 | fbalancedirect | 余额方向 | varchar | 10 |  | √ | ' ' | 余额方向 |
| 5 | ftransactioncode | 交易代码 | varchar | 200 |  | √ | ' ' | 交易代码 |
| 6 | fotherinfo | 其他记账信息 | varchar | 200 |  | √ | ' ' | 其他记账信息 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftransactionamount | 交易金额 | numeric | 23 | 10 | √ | 0 | 交易金额 |
| 9 | fbusinessserialnumber | 业务流水号 | varchar | 200 |  | √ | ' ' | 业务流水号 |
| 10 | fsourcevouchertype | 原始凭证种类 | varchar | 200 |  | √ | ' ' | 原始凭证种类 |
| 11 | fcounterpartyname | 对方户名 | varchar | 200 |  | √ | ' ' | 对方户名 |
| 12 | faccountbalance | 账户余额 | numeric | 23 | 10 | √ | 0 | 账户余额 |
| 13 | fcounterpartyaccount | 对方账号 | varchar | 200 |  | √ | ' ' | 对方账号 |
| 14 | fbooktime | 记账时间 | timestamp | 0 |  |  | null | 记账时间 |
| 15 | faccountjournal | 记账流水 | varchar | 200 |  | √ | ' ' | 记账流水 |
| 16 | fdepositorybank | 对方开户行 | varchar | 200 |  | √ | ' ' | 对方开户行 |
| 17 | felectronicreceiptnumber | 银行电子回单编号 | varchar | 200 |  | √ | ' ' | 银行电子回单编号 |
| 18 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 19 | fbookkeeper | 记账柜员 | varchar | 200 |  | √ | ' ' | 记账柜员 |
| 20 | felectronicreceiptinfo | 银行电子回单信息摘要 | varchar | 200 |  | √ | ' ' | 银行电子回单信息摘要 |
| 21 | fcreditordebit | 借贷标志 | varchar | 10 |  | √ | ' ' | 借贷标志 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_bkrsentry_fid |  | fid |
| 2 | pk_t_aef_bkrsentry |  | fentryid |

---

## 银行对账单-主表 t_aef_bkrs

- **表名称：** 银行对账单-主表
- **表名：** t_aef_bkrs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | favailablebal | 对账周期末可用余额 | numeric | 23 | 10 | √ | 0 | 对账周期末可用余额 |
| 3 | flargejson | 接收端json | varchar | 500 |  | √ | ' ' | 接收端json |
| 4 | faccountname | 客户账户名称 | varchar | 200 |  | √ | ' ' | 客户账户名称 |
| 5 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fidentificationorg | 签发机构 | varchar | 200 |  | √ | ' ' | 签发机构 |
| 7 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种 |
| 8 | fbankcustomernumber | 银行客户编码 | varchar | 200 |  | √ | ' ' | 银行客户编码 |
| 9 | foverdraftbal | 对账周期末透支余额 | numeric | 23 | 10 | √ | 0 | 对账周期末透支余额 |
| 10 | freconyear | 银行对账年份 | varchar | 50 |  | √ | ' ' | 银行对账年份 |
| 11 | fbankbranchnumber | 营业网点编号 | varchar | 200 |  | √ | ' ' | 营业网点编号 |
| 12 | freservebal | 对账周期末保留余额 | numeric | 23 | 10 | √ | 0 | 对账周期末保留余额 |
| 13 | fxbrlurl | xbrlurl | varchar | 200 |  | √ | ' ' | xbrlurl |
| 14 | freconmonth | 银行对账月份 | varchar | 50 |  | √ | ' ' | 银行对账月份 |
| 15 | ffrozenbal | 对账周期末冻结余额 | numeric | 23 | 10 | √ | 0 | 对账周期末冻结余额 |
| 16 | fprinttimes | 打印次数 | varchar | 50 |  | √ | ' ' | 打印次数 |
| 17 | farchivedate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 18 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 19 | fprintdate | 打印日期 | timestamp | 0 |  |  | null | 打印日期 |
| 20 | faccountbal | 对账周期末账户余额 | numeric | 23 | 10 | √ | 0 | 对账周期末账户余额 |
| 21 | fsourcebillno | 源单号码 | varchar | 30 |  | √ | ' ' | 源单号码 |
| 22 | flargejson_tag | 接收端json_详情 | text | 0 |  |  | null | 接收端json_详情 |
| 23 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fsettlementaccount | 客户结算账号 | varchar | 200 |  | √ | ' ' | 客户结算账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_bkrs |  | fid |
| 2 | idx_aef_bkrs |  | forgid,farchivedate |
