# 银行对账单-evp_bkrs

## 单据体-子表 t_evp_bkrsentry

- **表名称：** 单据体-子表
- **表名：** t_evp_bkrsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusinessproductstype | 业务产品种类 | varchar | 200 |  |  | ' ' | 业务产品种类 |
| 3 | fsourcevouchernumber | 原始凭证号码 | varchar | 200 |  |  | ' ' | 原始凭证号码 |
| 4 | fbalancedirect | 余额方向 | varchar | 10 |  | √ | ' ' | 余额方向,枚举: 0 :借方 1 :贷方 |
| 5 | ftransactioncode | 交易代码 | varchar | 200 |  |  | ' ' | 交易代码 |
| 6 | fotherinfo | 其他记账信息 | varchar | 200 |  |  | ' ' | 其他记账信息 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftransactionamount | 交易金额 | numeric | 23 | 10 | √ | 0 | 交易金额 |
| 9 | fbusinessserialnumber | 业务流水号 | varchar | 200 |  |  | ' ' | 业务流水号 |
| 10 | febookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 11 | fsourcevouchertype | 原始凭证种类 | varchar | 200 |  |  | ' ' | 原始凭证种类 |
| 12 | fcounterpartyname | 对方户名 | varchar | 200 |  |  | ' ' | 对方户名 |
| 13 | faccountbalance | 账户余额 | numeric | 23 | 10 | √ | 0 | 账户余额 |
| 14 | fcounterpartyaccount | 对方账号 | varchar | 200 |  |  | ' ' | 对方账号 |
| 15 | fbooktime | 记账时间 | varchar | 200 |  |  | ' ' | 记账时间 |
| 16 | faccountjournal | 记账流水 | varchar | 200 |  |  | ' ' | 记账流水 |
| 17 | fdepositorybank | 对方开户行 | varchar | 200 |  |  | ' ' | 对方开户行 |
| 18 | felectronicreceiptnumber | 银行电子回单编号 | varchar | 200 |  |  | ' ' | 银行电子回单编号 |
| 19 | fbookkeeper | 记账柜员 | varchar | 200 |  |  | ' ' | 记账柜员 |
| 20 | fcreditordebit | 借贷标志 | varchar | 10 |  | √ | ' ' | 借贷标志,枚举: 0 :借 1 :贷 |
| 21 | felectronicreceiptinfo | 银行电子回单信息摘要 | varchar | 200 |  |  | ' ' | 银行电子回单信息摘要 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evp_bkrsentry_fid |  | fid |
| 2 | pk_t_evp_bkrsentry |  | fentryid |

---

## 银行对账单-主表 t_evp_bkrs

- **表名称：** 银行对账单-主表
- **表名：** t_evp_bkrs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 入池操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisintopool | 电子凭证入池 | bpchar | 1 |  | √ | '0' | 电子凭证入池 |
| 4 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdirectbillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 6 | fbankcustomernumber | 银行客户编码 | varchar | 200 |  |  | ' ' | 银行客户编码 |
| 7 | fisdelete | 已删除 | bpchar | 1 |  | √ | '0' | 已删除 |
| 8 | freconyear | 银行对账年份 | varchar | 50 |  | √ | ' ' | 银行对账年份 |
| 9 | fvoucherno | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 10 | ffileurl | 原文件地址 | varchar | 2000 |  |  | ' ' | 原文件地址 |
| 11 | fbankbranchnumber | 营业网点编号 | varchar | 200 |  |  | ' ' | 营业网点编号 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fbasetext | 原文件base64 | varchar | 500 |  |  | null | 原文件base64 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | farchivebatchcode | 归档批次号 | varchar | 255 |  | √ | ' ' | 归档批次号 |
| 16 | ffrozenbal | 对账周期末冻结余额 | numeric | 23 | 10 | √ | 0 | 对账周期末冻结余额 |
| 17 | ffilename | 原文件名 | varchar | 2000 |  |  | ' ' | 原文件名 |
| 18 | fprinttimes | 打印次数 | varchar | 10 |  | √ | ' ' | 打印次数 |
| 19 | fisarchive | 归档 | bpchar | 1 |  | √ | '0' | 归档 |
| 20 | fprintdate | 打印日期 | timestamp | 0 |  |  | null | 打印日期 |
| 21 | faccountbal | 对账周期末账户余额 | numeric | 23 | 10 | √ | 0 | 对账周期末账户余额 |
| 22 | foriginsysid | 集成系统 | int8 | 64 |  | √ | 0 | [集成系统配置 evp_originsys](../evp_files/evp_originsys.md) |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fsettlementaccount | 客户结算账号 | varchar | 200 |  |  | ' ' | 客户结算账号 |
| 25 | fdirectbillno | 关联单据号 | varchar | 50 |  | √ | ' ' | 关联单据号 |
| 26 | favailablebal | 对账周期末可用余额 | numeric | 23 | 10 | √ | 0 | 对账周期末可用余额 |
| 27 | fvoucherid | 关联凭证id | varchar | 50 |  | √ | ' ' | 关联凭证id |
| 28 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 29 | faccountname | 客户账户名称 | varchar | 200 |  |  | ' ' | 客户账户名称 |
| 30 | fidentificationorg | 签发机构 | varchar | 200 |  |  | ' ' | 签发机构 |
| 31 | foverdraftbal | 对账周期末透支余额 | numeric | 23 | 10 | √ | 0 | 对账周期末透支余额 |
| 32 | fseqno | 票据流水号（唯一标识） | varchar | 200 |  | √ | ' ' | 票据流水号（唯一标识） |
| 33 | freservebal | 对账周期末保留余额 | numeric | 23 | 10 | √ | 0 | 对账周期末保留余额 |
| 34 | fdirectbilltype | 关联单据类型 | varchar | 50 |  | √ | ' ' | 关联单据类型 |
| 35 | fbasetext_tag | 原文件base64_详情 | text | 0 |  |  | null | 原文件base64_详情 |
| 36 | fxbrlurl | xbrl文件地址 | varchar | 500 |  |  | ' ' | xbrl文件地址 |
| 37 | freconmonth | 银行对账月份 | varchar | 50 |  | √ | ' ' | 银行对账月份 |
| 38 | fbatchcode | 批次号 | varchar | 128 |  | √ | ' ' | 批次号 |
| 39 | frecondate | 银行对账单日期 | timestamp | 0 |  |  | null | 银行对账单日期 |
| 40 | ffileurl_tag | 原文件地址_详情 | text | 0 |  |  | null | 原文件地址_详情 |
| 41 | fishandle | 数据来源 | bpchar | 1 |  | √ | '0' | 数据来源,枚举: 0 :API导入 1 :手工新增 2 :系统抽取 |
| 42 | fbillid | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 43 | fbookdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 44 | fintopooldate | 入池时间 | timestamp | 0 |  |  | null | 入池时间 |
| 45 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evp_bkrs |  | fid |
| 2 | idx_evp_bkrs |  | forgid,fbillid |
