# 铁路电子客票行程单-aef_raireceiver

## 铁路电子客票行程单-主表 t_aef_raireceiver

- **表名称：** 铁路电子客票行程单-主表
- **表名：** t_aef_raireceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fisredinvoice | 是否红字发票 | bpchar | 1 |  | √ | ' ' | 是否红字发票 |
| 4 | faccountingentityname | 会计主体名称 | varchar | 50 |  | √ | ' ' | 会计主体名称 |
| 5 | flargejson | 接收端json | varchar | 500 |  | √ | ' ' | 接收端json |
| 6 | fdateofissue | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 7 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 8 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdirectvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 10 | fdeductiontaxperiod | 抵扣税期 | varchar | 50 |  | √ | ' ' | 抵扣税期 |
| 11 | fhasbeendeducted | 是否已抵扣 | bpchar | 1 |  | √ | ' ' | 是否已抵扣 |
| 12 | fxbrlurl | xbrlurl | varchar | 200 |  | √ | ' ' | xbrlurl |
| 13 | ftravelnumber | 电子发票号码 | varchar | 50 |  | √ | ' ' | 电子发票号码 |
| 14 | fsocialcreditcode | 会计主体统一社会信用代码 | varchar | 50 |  | √ | ' ' | 会计主体统一社会信用代码 |
| 15 | farchivedate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 16 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 17 | fhasbeenbooked | 是否已入账 | bpchar | 1 |  | √ | ' ' | 是否已入账 |
| 18 | fsourcebillno | 源单号码 | varchar | 30 |  | √ | ' ' | 源单号码 |
| 19 | ftotalamountexcludingtax | 金额（不含税） | numeric | 23 | 10 | √ | 0 | 金额（不含税） |
| 20 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 21 | flargejson_tag | 接收端json_详情 | text | 0 |  |  | null | 接收端json_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_raireceiver |  | fid |
| 2 | idx_aef_rai |  | farchivedate,forgid |

---

## 单据体-子表 t_aef_raireceiverentry

- **表名称：** 单据体-子表
- **表名：** t_aef_raireceiverentry

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
| 1 | pk_t_aef_raireceiverentry |  | fentryid |
| 2 | idx_aef_raireceiverentry_fid |  | fid |
