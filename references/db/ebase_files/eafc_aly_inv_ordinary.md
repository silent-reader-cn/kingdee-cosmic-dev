# 增值税电子普通发票-eafc_aly_inv_ordinary

## 单据体-子表 tk_eafc_aly_invordreentry

- **表名称：** 单据体-子表
- **表名：** tk_eafc_aly_invordreentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_bookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 3 | fk_eafc_period | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间 |
| 4 | fk_eafc_vdescription | 摘要 | varchar | 50 |  | √ | ' ' | 摘要 |
| 5 | fk_eafc_vouchernumber | 凭证编号 | varchar | 50 |  | √ | ' ' | 凭证编号 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_aly_invordreentry |  | fentryid |
| 2 | idx__eafc_aly_invordreentry_fk |  | fid |

---

## 增值税电子普通发票-主表 tk_eafc_aly_inv_ordinary

- **表名称：** 增值税电子普通发票-主表
- **表名：** tk_eafc_aly_inv_ordinary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_nameofseller | 销售方名称 | varchar | 200 |  | √ | ' ' | 销售方名称 |
| 4 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 5 | fk_eafc_hasbeenpaid | 是否已付款 | bpchar | 1 |  | √ | '0' | 是否已付款 |
| 6 | fk_eafc_taxincludedamount | 价税合计（小写） | numeric | 23 | 4 |  | null | 价税合计（小写） |
| 7 | fk_eafc_directvoucherid | 凭证ID | int8 | 64 |  |  | null | 凭证ID |
| 8 | fk_eafc_matchingstate | 发票匹配状态 | varchar | 50 |  | √ | ' ' | 发票匹配状态 |
| 9 | fk_eafc_uniquecode | 发票唯一标识 | varchar | 200 |  | √ | ' ' | 发票唯一标识 |
| 10 | fk_eafc_amortizationmetho | 摊销方法 | varchar | 200 |  | √ | ' ' | 摊销方法 |
| 11 | fk_eafc_billid | 单据ID | int8 | 64 |  |  | null | 单据ID |
| 12 | fk_eafc_hasbeenchecked | 是否已验真 | bpchar | 1 |  | √ | '0' | 是否已验真 |
| 13 | fk_eafc_hasbeenbooked | 是否已入账 | bpchar | 1 |  | √ | '0' | 是否已入账 |
| 14 | fk_eafc_isredinvoice | 是否红字发票 | bpchar | 1 |  | √ | '0' | 是否红字发票 |
| 15 | fk_eafc_hasbeencompleted | 是否已所得税税前扣除 | bpchar | 1 |  | √ | '0' | 是否已所得税税前扣除 |
| 16 | fk_eafc_totalamountexclud | 不含税金额合计 | numeric | 23 | 4 |  | null | 不含税金额合计 |
| 17 | fk_eafc_totaltaxamount | 税额合计 | numeric | 23 | 4 |  | null | 税额合计 |
| 18 | fk_eafc_accountingentityn | 会计主体名称 | varchar | 50 |  | √ | ' ' | 会计主体名称 |
| 19 | fk_eafc_dateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 20 | fk_eafc_endyear | 所得税税前扣除年度止 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度止 |
| 21 | fk_eafc_socialcreditcode | 会计主体统一社会信用代码 | varchar | 200 |  | √ | ' ' | 会计主体统一社会信用代码 |
| 22 | fk_eafc_electronicnumber | 银行回单编号 | varchar | 50 |  | √ | ' ' | 银行回单编号 |
| 23 | fk_eafc_beginyear | 所得税税前扣除年度起 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度起 |
| 24 | fk_eafc_hasbeenfsos | 是否已做保理、出售、 资产证券化 | bpchar | 1 |  | √ | '0' | 是否已做保理、出售、 资产证券化 |
| 25 | fk_eafc_contractnumber | 合同编码 | varchar | 50 |  | √ | ' ' | 合同编码 |
| 26 | fk_eafc_endperiod | 权责发生制下支出所属期止 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期止 |
| 27 | fk_eafc_beginperiod | 权责发生制下支出所属期起 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期起 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_aly_inv_ordinary |  | fid |
