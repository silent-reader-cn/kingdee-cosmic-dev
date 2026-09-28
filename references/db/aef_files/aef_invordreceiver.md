# 增值税电子普通发票-aef_invordreceiver

## 单据体-子表 t_aef_invordreceiverentry

- **表名称：** 单据体-子表
- **表名：** t_aef_invordreceiverentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 3 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 4 | fvouchernumber | 凭证编号 | varchar | 80 |  | √ | ' ' | 凭证编号 |
| 5 | fperiod | 会计期间 | varchar | 30 |  | √ | ' ' | 会计期间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_invordreceiverentry |  | fid |
| 2 | pk_t_aef_invordreceiverentry |  | fentryid |

---

## 增值税电子普通发票-主表 t_aef_invordreceiver

- **表名称：** 增值税电子普通发票-主表
- **表名：** t_aef_invordreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisredinvoice | 是否红字发票 | bpchar | 1 |  | √ | ' ' | 是否红字发票 |
| 3 | faccountingentityname | 会计主体名称 | varchar | 50 |  | √ | ' ' | 会计主体名称 |
| 4 | flargejson | 接收端json | varchar | 500 |  | √ | ' ' | 接收端json |
| 5 | fbeginperiod | 权责发生制下支出所属期起 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期起 |
| 6 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fhasbeenpaid | 是否已付款 | bpchar | 1 |  | √ | ' ' | 是否已付款 |
| 8 | fendyear | 所得税税前扣除年度止 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度止 |
| 9 | fnameofseller | 销售方名称 | varchar | 255 |  | √ | ' ' | 销售方名称 |
| 10 | farchivedate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 11 | fcontractnumber | 合同编码 | varchar | 50 |  | √ | ' ' | 合同编码 |
| 12 | funiquecode | 发票唯一标识 | varchar | 50 |  | √ | ' ' | 发票唯一标识 |
| 13 | fsourcebillno | 源单号码 | varchar | 30 |  | √ | ' ' | 源单号码 |
| 14 | ftotalamountexcludingtax | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 15 | felectronicnumber | 银行回单编号 | varchar | 50 |  | √ | ' ' | 银行回单编号 |
| 16 | fendperiod | 权责发生制下支出所属期止 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期止 |
| 17 | fbeginyear | 所得税税前扣除年度起 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度起 |
| 18 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 19 | fdirectvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 20 | ftaxsocialcreditcode | 销售方纳税人识别号（统一社会信用代码） | varchar | 50 |  | √ | ' ' | 销售方纳税人识别号（统一社会信用代码） |
| 21 | famortizationmethod | 摊销方法 | varchar | 50 |  | √ | ' ' | 摊销方法 |
| 22 | fmatchingstate | 发票匹配状态 | varchar | 50 |  | √ | ' ' | 发票匹配状态 |
| 23 | fxbrlurl | xbrlurl | varchar | 200 |  | √ | ' ' | xbrlurl |
| 24 | fhasbeenfsos | 是否已做保理、出售、 资产证券化 | bpchar | 1 |  | √ | ' ' | 是否已做保理、出售、 资产证券化 |
| 25 | fsocialcreditcode | 会计主体统一社会信用代码 | varchar | 50 |  | √ | ' ' | 会计主体统一社会信用代码 |
| 26 | fhasbeencompleted | 是否已所得税税前扣除 | bpchar | 1 |  | √ | ' ' | 是否已所得税税前扣除 |
| 27 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 28 | fhasbeenchecked | 是否已验真 | bpchar | 1 |  | √ | ' ' | 是否已验真 |
| 29 | fhasbeenbooked | 是否已入账 | bpchar | 1 |  | √ | ' ' | 是否已入账 |
| 30 | ftaxincludedamountinfigur | 价税合计（小写） | numeric | 23 | 10 | √ | 0 | 价税合计（小写） |
| 31 | ftotaltaxamount | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 32 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 33 | flargejson_tag | 接收端json_详情 | text | 0 |  |  | null | 接收端json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_invo |  | forgid,farchivedate |
| 2 | pk_t_aef_invordreceiver |  | fid |
