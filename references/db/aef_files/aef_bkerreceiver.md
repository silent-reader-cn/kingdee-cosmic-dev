# 银行电子回单-aef_bkerreceiver

## 银行电子回单-主表 t_aef_bkerreceiver

- **表名称：** 银行电子回单-主表
- **表名：** t_aef_bkerreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypeofinvoice | 票据类型 | varchar | 50 |  | √ | ' ' | 票据类型 |
| 3 | faccountingentityname | 会计主体名称 | varchar | 50 |  | √ | ' ' | 会计主体名称 |
| 4 | flargejson | 接收端json | varchar | 500 |  | √ | ' ' | 接收端json |
| 5 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 6 | fpayandrevamount | 应收/付款项金额 | numeric | 23 | 10 | √ | 0 | 应收/付款项金额 |
| 7 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fhasbeenclaimed | 是否已认领 | bpchar | 1 |  | √ | ' ' | 是否已认领 |
| 9 | fcurrency | 币种 | varchar | 50 |  | √ | ' ' | 币种 |
| 10 | fdirectvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 11 | fidentifyingcode | 回单校验码 | varchar | 50 |  | √ | ' ' | 回单校验码 |
| 12 | ftransactionamountinfigur | 小写金额 | numeric | 23 | 10 | √ | 0 | 小写金额 |
| 13 | fxbrlurl | xbrlurl | varchar | 200 |  | √ | ' ' | xbrlurl |
| 14 | fsocialcreditcode | 会计主体统一社会信用代码 | varchar | 50 |  | √ | ' ' | 会计主体统一社会信用代码 |
| 15 | fhasbeenreconciled | 是否已对账 | bpchar | 1 |  | √ | ' ' | 是否已对账 |
| 16 | fhasbeentransfer | 是否已流转 | bpchar | 1 |  | √ | ' ' | 是否已流转 |
| 17 | farchivedate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 18 | fcontractnumber | 合同编号 | varchar | 50 |  | √ | ' ' | 合同编号 |
| 19 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 20 | fhasbeenbooked | 是否已入账 | bpchar | 1 |  | √ | ' ' | 是否已入账 |
| 21 | funiquecode | 发票号 | varchar | 50 |  | √ | ' ' | 发票号 |
| 22 | fsourcebillno | 源单号码 | varchar | 30 |  | √ | ' ' | 源单号码 |
| 23 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 24 | flargejson_tag | 接收端json_详情 | text | 0 |  |  | null | 接收端json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_bkerreceiver |  | fid |
| 2 | idx_aef_bker |  | forgid,farchivedate |

---

## 单据体-子表 t_aef_bkerreceiverentry

- **表名称：** 单据体-子表
- **表名：** t_aef_bkerreceiverentry

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
| 1 | pk_t_aef_bkerreceiverentry |  | fentryid |
| 2 | idx_aef_bkerreceiverentry_fid |  | fid |
