# 收费公路通行费增值税电子普通发票-aef_invtlfreceiver

## 单据体-子表 t_aef_invtlfreceiverentry

- **表名称：** 单据体-子表
- **表名：** t_aef_invtlfreceiverentry

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
| 1 | idx_aef_invtlfreceiverentry |  | fid |
| 2 | pk_t_aef_invtlfreceiverentry |  | fentryid |

---

## 收费公路通行费增值税电子普通发票-主表 t_aef_invtlfreceiver

- **表名称：** 收费公路通行费增值税电子普通发票-主表
- **表名：** t_aef_invtlfreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisredinvoice | 是否红字发票 | bpchar | 1 |  | √ | ' ' | 是否红字发票 |
| 3 | faccountingentityname | 会计主体名称 | varchar | 50 |  | √ | ' ' | 会计主体名称 |
| 4 | flargejson | 接收端json | varchar | 500 |  | √ | ' ' | 接收端json |
| 5 | fbeginperiod | 权责发生制下支出所属期起 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期起 |
| 6 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fusageconfirmation | 用途确认 | varchar | 50 |  | √ | ' ' | 用途确认 |
| 8 | fhasbeenpaid | 是否已付款 | bpchar | 1 |  | √ | ' ' | 是否已付款 |
| 9 | fusageconfirmationperiod | 用途确认所属期 | varchar | 50 |  | √ | ' ' | 用途确认所属期 |
| 10 | fendyear | 所得税税前扣除年度止 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度止 |
| 11 | fnameofseller | 销售方名称 | varchar | 255 |  | √ | ' ' | 销售方名称 |
| 12 | farchivedate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 13 | funiquecode | 发票唯一标识 | varchar | 50 |  | √ | ' ' | 发票唯一标识 |
| 14 | fsourcebillno | 源单号码 | varchar | 30 |  | √ | ' ' | 源单号码 |
| 15 | ftotalamountexcludingtax | 不含税金额合计 | numeric | 23 | 10 | √ | 0 | 不含税金额合计 |
| 16 | felectronicnumber | 银行回单编号 | varchar | 50 |  | √ | ' ' | 银行回单编号 |
| 17 | fendperiod | 权责发生制下支出所属期止 | varchar | 50 |  | √ | ' ' | 权责发生制下支出所属期止 |
| 18 | fbeginyear | 所得税税前扣除年度起 | varchar | 50 |  | √ | ' ' | 所得税税前扣除年度起 |
| 19 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 20 | ftransferredoutamount | 进项税额转出金额 | numeric | 23 | 10 | √ | 0 | 进项税额转出金额 |
| 21 | fdirectvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 22 | ftaxsocialcreditcode | 销售方纳税人识别号（统一社会信用代码） | varchar | 50 |  | √ | ' ' | 销售方纳税人识别号（统一社会信用代码） |
| 23 | fhasbeenconfirmed | 是否已用途确认 | bpchar | 1 |  | √ | ' ' | 是否已用途确认 |
| 24 | fxbrlurl | xbrlurl | varchar | 200 |  | √ | ' ' | xbrlurl |
| 25 | fhasbeenfsos | 是否已做保理、出售、 资产证券化 | bpchar | 1 |  | √ | ' ' | 是否已做保理、出售、 资产证券化 |
| 26 | fsocialcreditcode | 会计主体统一社会信用代码 | varchar | 50 |  | √ | ' ' | 会计主体统一社会信用代码 |
| 27 | fhasbeencompleted | 是否已所得税税前扣除 | bpchar | 1 |  | √ | ' ' | 是否已所得税税前扣除 |
| 28 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 29 | fhasbeenchecked | 是否已验真 | bpchar | 1 |  | √ | ' ' | 是否已验真 |
| 30 | fhasbeenbooked | 是否已入账 | bpchar | 1 |  | √ | ' ' | 是否已入账 |
| 31 | ftaxincludedamountinfigur | 价税合计（小写） | numeric | 23 | 10 | √ | 0 | 价税合计（小写） |
| 32 | fistransferredout | 是否进项税额转出 | bpchar | 1 |  | √ | ' ' | 是否进项税额转出 |
| 33 | ftotaltaxamount | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 34 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 35 | flargejson_tag | 接收端json_详情 | text | 0 |  |  | null | 接收端json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_invtlfreceiver |  | fid |
| 2 | idx_aef_invt |  | farchivedate,forgid |
