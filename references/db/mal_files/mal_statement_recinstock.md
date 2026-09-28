# 收货入库明细-mal_statement_recinstock

## 明细数据-子表 t_mal_statementdataentry

- **表名称：** 明细数据-子表
- **表名：** t_mal_statementdataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 收货/入库数量 | numeric | 23 | 10 | √ | 0 | 收货/入库数量 |
| 3 | ftaxamount | 收货/入库金额 | numeric | 23 | 10 | √ | 0 | 收货/入库金额 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fsrcbillno | 收货/入库单号 | varchar | 80 |  | √ | ' ' | 收货/入库单号 |
| 6 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 7 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 8 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 11 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 14 | fdate | 收货/入库日期 | timestamp | 0 |  |  | null | 收货/入库日期 |
| 15 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 16 | fentryunitid | fentryunitid | int8 | 64 |  | √ | 0 |  |
| 17 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_stm_entry_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_statementdataentry |  | fentryid |

---

## 收货入库明细-主表 t_mal_statementdata

- **表名称：** 收货入库明细-主表
- **表名：** t_mal_statementdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fecorderid | fecorderid | varchar | 80 |  | √ | ' ' |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fecorderqty | fecorderqty | int4 | 32 |  | √ | 0 |  |
| 5 | fpurcheckno | fpurcheckno | varchar | 80 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 8 | fpurorderbillno | fpurorderbillno | varchar | 80 |  | √ | ' ' |  |
| 9 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | finvoiceresult | finvoiceresult | varchar | 255 |  | √ | ' ' |  |
| 11 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 12 | flocalecorderid | flocalecorderid | varchar | 80 |  | √ | ' ' |  |
| 13 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fmalorderid | fmalorderid | int8 | 64 |  | √ | 0 |  |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 19 | fecreturnqty | fecreturnqty | int4 | 32 |  | √ | 0 |  |
| 20 | feccount | feccount | int4 | 32 |  | √ | 0 |  |
| 21 | fpersonid | fpersonid | int8 | 64 |  | √ | 0 |  |
| 22 | fbusinesstypeid | fbusinesstypeid | int8 | 64 |  | √ | 0 |  |
| 23 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fecreturntaxamount | fecreturntaxamount | numeric | 23 | 10 | √ | 0 |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | finvoicestatus | finvoicestatus | varchar | 10 |  | √ | ' ' |  |
| 27 | fskuid | fskuid | varchar | 80 |  | √ | ' ' |  |
| 28 | fdeporgid | fdeporgid | int8 | 64 |  | √ | 0 |  |
| 29 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 30 | fdiffqty | fdiffqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | flocalecporderid | flocalecporderid | varchar | 80 |  | √ | ' ' |  |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | fcheckresult | fcheckresult | varchar | 10 |  | √ | ' ' |  |
| 34 | faftersalestatus | faftersalestatus | varchar | 10 |  | √ | ' ' |  |
| 35 | fplatform | fplatform | bpchar | 1 |  | √ | ' ' |  |
| 36 | freceiptid | freceiptid | int8 | 64 |  | √ | 0 |  |
| 37 | fectaxamount | fectaxamount | numeric | 23 | 10 | √ | 0 |  |
| 38 | fecporderid | fecporderid | varchar | 80 |  | √ | ' ' |  |
| 39 | fskuname | fskuname | varchar | 255 |  | √ | ' ' |  |
| 40 | ftaxtype | ftaxtype | varchar | 1 |  | √ | ' ' |  |
| 41 | fpurinvoiceno | fpurinvoiceno | varchar | 80 |  | √ | ' ' |  |
| 42 | fecordertaxamount | fecordertaxamount | numeric | 23 | 10 | √ | 0 |  |
| 43 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 44 | fmalorderentryid | fmalorderentryid | int8 | 64 |  | √ | 0 |  |
| 45 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 46 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | finvtypeid | finvtypeid | int8 | 64 |  | √ | 0 |  |
| 48 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 49 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 50 | flocalprice | flocalprice | numeric | 23 | 10 | √ | 0 |  |
| 51 | flocaltaxrate | flocaltaxrate | numeric | 23 | 10 | √ | 0 |  |
| 52 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | fordercreatorid | fordercreatorid | int8 | 64 |  | √ | 0 |  |
| 54 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 55 | fmalorderbillno | fmalorderbillno | varchar | 80 |  | √ | ' ' |  |
| 56 | flocaltaxprice | flocaltaxprice | numeric | 23 | 10 | √ | 0 |  |
| 57 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 58 | fectaxprice | fectaxprice | numeric | 23 | 10 | √ | 0 |  |
| 59 | fdifftaxamount | fdifftaxamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | fcheckstatus | fcheckstatus | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_statementdata |  | fid |
| 2 | idx_mal_stmd_fskuid |  | fskuid |
| 3 | idx_mal_stmd_fecorderid |  | fecorderid |
