# 销售订单分录F7-pdm_saleorderentry

## 销售订单分录F7-多语言表 t_sm_salorderentry_l

- **表名称：** 销售订单分录F7-多语言表
- **表名：** t_sm_salorderentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | foldcusmaterialname | foldcusmaterialname | varchar | 255 |  | √ | ' ' |  |
| 5 | foldcusmaterialmod | foldcusmaterialmod | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salorderentry_l |  | fentryid,flocaleid |
| 2 | pk_t_sm_salorderentry_l |  | fpkid |

---

## 销售订单分录F7-主表 t_sm_salorderentry

- **表名称：** 销售订单分录F7-主表
- **表名：** t_sm_salorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 父项ID | int8 | 64 |  | √ | 0 | 父项ID |
| 2 | fdeliverrateup | fdeliverrateup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fexpectqtydate | fexpectqtydate | timestamp | 0 |  |  | null |  |
| 4 | fdiscountrate | fdiscountrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 7 | fdeliverratedown | fdeliverratedown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fprojectconfqty | fprojectconfqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fcuramount | fcuramount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fmpmopportno | fmpmopportno | int8 | 64 |  | √ | 0 |  |
| 12 | foldcusmaterialname | foldcusmaterialname | varchar | 255 |  | √ | ' ' |  |
| 13 | foldcusmaterialmod | foldcusmaterialmod | varchar | 255 |  | √ | ' ' |  |
| 14 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 16 | fispresent | fispresent | bpchar | 1 |  | √ | '0' |  |
| 17 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 18 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 20 | fmaterialmasterid | fmaterialmasterid | int8 | 64 |  | √ | 0 |  |
| 21 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 22 | fsalesorgid | fsalesorgid | int8 | 64 |  | √ | 0 |  |
| 23 | fsuitesettletype | fsuitesettletype | varchar | 50 |  | √ | ' ' |  |
| 24 | fbaseunitdenominator | fbaseunitdenominator | numeric | 23 | 10 | √ | 1 |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fstockorgid | fstockorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fentrychangetype | fentrychangetype | varchar | 5 |  | √ | ' ' |  |
| 28 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |
| 29 | fprojassinvoicebaseqty | fprojassinvoicebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | fbaseunitnumerator | fbaseunitnumerator | numeric | 23 | 10 | √ | 1 |  |
| 31 | flotnumber | flotnumber | varchar | 80 |  | √ | ' ' |  |
| 32 | fprojectinvoicedbaseqty | fprojectinvoicedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fprojassinvoiceqty | fprojassinvoiceqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fdiscountamount | fdiscountamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fdeliverqtyup | fdeliverqtyup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 38 | fsupplytrans | fsupplytrans | bpchar | 1 |  | √ | '0' |  |
| 39 | fdeliverdelaydays | fdeliverdelaydays | int4 | 32 |  | √ | 0 |  |
| 40 | fauxunitid | fauxunitid | int8 | 64 |  | √ | 0 |  |
| 41 | fsettledeptid | fsettledeptid | int8 | 64 |  | √ | 0 |  |
| 42 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 43 | fcorebillrowno | fcorebillrowno | int8 | 64 |  | √ | 0 |  |
| 44 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 45 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | ' ' |  |
| 46 | fprojectinvoicedqty | fprojectinvoicedqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fproducttype | fproducttype | varchar | 50 |  | √ | 'standard' |  |
| 48 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 49 | frowterminatestatus | frowterminatestatus | varchar | 5 |  | √ | ' ' |  |
| 50 | fdeliverqtydown | fdeliverqtydown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 51 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 52 | fmatchdiscountlistid | fmatchdiscountlistid | int8 | 64 |  | √ | 0 |  |
| 53 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 54 | fprojectconfbaseqty | fprojectconfbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fsuitedeliverytype | fsuitedeliverytype | varchar | 50 |  | √ | ' ' |  |
| 56 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 57 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 58 | fdeliveradvdays | fdeliveradvdays | int4 | 32 |  | √ | 0 |  |
| 59 | fparentproduct | fparentproduct | int8 | 64 |  | √ | 0 |  |
| 60 | fdeliverbaseqtyup | fdeliverbaseqtyup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 61 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 62 | fentrysettleorgid | fentrysettleorgid | int8 | 64 |  | √ | 0 |  |
| 63 | fownertype | fownertype | varchar | 36 |  | √ | ' ' |  |
| 64 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 65 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 66 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 67 | foldcusmaterialnum | foldcusmaterialnum | varchar | 255 |  | √ | ' ' |  |
| 68 | fexpectqty | fexpectqty | numeric | 23 | 10 | √ | 0 |  |
| 69 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 70 | fprojectassqty | fprojectassqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fprojectassbaseqty | fprojectassbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 72 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 73 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 74 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 75 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 76 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 77 | fisprojassociated | fisprojassociated | bpchar | 1 |  | √ | '0' |  |
| 78 | freturntype | freturntype | varchar | 5 |  | √ | ' ' |  |
| 79 | fauxqty2 | fauxqty2 | numeric | 23 | 10 | √ | 0 |  |
| 80 | fparentrowid | fparentrowid | int8 | 64 |  | √ | 0 |  |
| 81 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 82 | fauxqty | fauxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 83 | fcuramountandtax | fcuramountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 84 | fminorderbaseqty | fminorderbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 85 | fmatchpricelist | fmatchpricelist | int8 | 64 |  | √ | 0 |  |
| 86 | fcusmatid | fcusmatid | int8 | 64 |  | √ | 0 |  |
| 87 | fmaterialname | fmaterialname | varchar | 255 |  |  | ' ' |  |
| 88 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 89 | frowclosestatus | frowclosestatus | varchar | 5 |  | √ | ' ' |  |
| 90 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 91 | fentrystatus | fentrystatus | varchar | 5 |  | √ | ' ' |  |
| 92 | fissuedqty | fissuedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 93 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 94 | fcorebillno | fcorebillno | varchar | 80 |  | √ | ' ' |  |
| 95 | fproorgid | fproorgid | int8 | 64 |  | √ | 0 |  |
| 96 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 97 | fbomentryid | fbomentryid | int8 | 64 |  | √ | 0 |  |
| 98 | frowterminatemanual | frowterminatemanual | bpchar | 1 |  | √ | '0' |  |
| 99 | fauxunit2id | fauxunit2id | int8 | 64 |  | √ | 0 |  |
| 100 | fdeliverbaseqtydown | fdeliverbaseqtydown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 101 | fsettleamount | fsettleamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 102 | fsuitepricepercent | fsuitepricepercent | numeric | 23 | 10 | √ | 0 |  |
| 103 | fiscontrolday | fiscontrolday | bpchar | 1 |  | √ | '0' |  |
| 104 | famountandtax | famountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 105 | fdeliverydate | fdeliverydate | timestamp | 0 |  |  | null |  |
| 106 | fcurtaxamount | fcurtaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 107 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 108 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_salorderentry_pkey |  | fentryid |
| 2 | idx_sm_salesorderentry_fid |  | fid |
| 3 | idx_sm_soe_matmasterid |  | fmaterialmasterid,fid |
| 4 | idx_sm_soe_fownerid |  | fownerid |
| 5 | idx_sm_soe_matid |  | fmaterialid,fid |
