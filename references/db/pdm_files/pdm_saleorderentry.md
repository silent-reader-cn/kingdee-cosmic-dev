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
| 22 | fisintransit | fisintransit | bpchar | 1 |  | √ | '0' |  |
| 23 | fmaterialinvid | fmaterialinvid | int8 | 64 |  | √ | 0 |  |
| 24 | fsalesorgid | fsalesorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fsuitesettletype | fsuitesettletype | varchar | 50 |  | √ | ' ' |  |
| 26 | fbaseunitdenominator | fbaseunitdenominator | numeric | 23 | 10 | √ | 1 |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fstockorgid | fstockorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fentrychangetype | fentrychangetype | varchar | 5 |  | √ | ' ' |  |
| 30 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |
| 31 | fprojassinvoicebaseqty | fprojassinvoicebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | flicenseno | flicenseno | int8 | 64 |  | √ | 0 |  |
| 33 | fbaseunitnumerator | fbaseunitnumerator | numeric | 23 | 10 | √ | 1 |  |
| 34 | fmaterialgroup | fmaterialgroup | int8 | 64 |  | √ | 0 |  |
| 35 | flotnumber | flotnumber | varchar | 80 |  | √ | ' ' |  |
| 36 | fprojectinvoicedbaseqty | fprojectinvoicedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fprojassinvoiceqty | fprojassinvoiceqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fk_bj73_qtyfield1 | fk_bj73_qtyfield1 | numeric | 23 | 10 |  | null |  |
| 39 | fdiscountamount | fdiscountamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fdeliverqtyup | fdeliverqtyup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 43 | fk_bj73_custombasedatafield | fk_bj73_custombasedatafield | int8 | 64 |  | √ | 0 |  |
| 44 | fsupplytrans | fsupplytrans | bpchar | 1 |  | √ | '0' |  |
| 45 | fdeliverdelaydays | fdeliverdelaydays | int4 | 32 |  | √ | 0 |  |
| 46 | fauxunitid | fauxunitid | int8 | 64 |  | √ | 0 |  |
| 47 | fsettledeptid | fsettledeptid | int8 | 64 |  | √ | 0 |  |
| 48 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 49 | fcorebillrowno | fcorebillrowno | int8 | 64 |  | √ | 0 |  |
| 50 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 51 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | ' ' |  |
| 52 | fprojectinvoicedqty | fprojectinvoicedqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | fproducttype | fproducttype | varchar | 50 |  | √ | 'standard' |  |
| 54 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 55 | flogistics | flogistics | bpchar | 1 |  | √ | '0' |  |
| 56 | frowterminatestatus | frowterminatestatus | varchar | 5 |  | √ | ' ' |  |
| 57 | fdeliverqtydown | fdeliverqtydown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 58 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 59 | fmatchdiscountlistid | fmatchdiscountlistid | int8 | 64 |  | √ | 0 |  |
| 60 | fk_bj73_pricefield | fk_bj73_pricefield | numeric | 23 | 10 |  | null |  |
| 61 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 62 | fprojectconfbaseqty | fprojectconfbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 63 | fsuitedeliverytype | fsuitedeliverytype | varchar | 50 |  | √ | ' ' |  |
| 64 | ftaildiffstatus | ftaildiffstatus | bpchar | 1 |  | √ | '0' |  |
| 65 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 66 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 67 | fdeliveradvdays | fdeliveradvdays | int4 | 32 |  | √ | 0 |  |
| 68 | fparentproduct | fparentproduct | int8 | 64 |  | √ | 0 |  |
| 69 | fdeliverbaseqtyup | fdeliverbaseqtyup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 70 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 71 | fentrysettleorgid | fentrysettleorgid | int8 | 64 |  | √ | 0 |  |
| 72 | fownertype | fownertype | varchar | 36 |  | √ | ' ' |  |
| 73 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 74 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 75 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 76 | foldcusmaterialnum | foldcusmaterialnum | varchar | 255 |  | √ | ' ' |  |
| 77 | fexpectqty | fexpectqty | numeric | 23 | 10 | √ | 0 |  |
| 78 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 79 | fprojectassqty | fprojectassqty | numeric | 23 | 10 | √ | 0 |  |
| 80 | fprojectassbaseqty | fprojectassbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 81 | ftaildifflog | ftaildifflog | varchar | 2000 |  | √ | ' ' |  |
| 82 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 83 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 84 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 85 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 86 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 87 | fcusmaterialmod | fcusmaterialmod | varchar | 50 |  | √ | ' ' |  |
| 88 | fk_bj73_materielfield1 | fk_bj73_materielfield1 | int8 | 64 |  | √ | 0 |  |
| 89 | fisprojassociated | fisprojassociated | bpchar | 1 |  | √ | '0' |  |
| 90 | freturntype | freturntype | varchar | 5 |  | √ | ' ' |  |
| 91 | fauxqty2 | fauxqty2 | numeric | 23 | 10 | √ | 0 |  |
| 92 | fparentrowid | fparentrowid | int8 | 64 |  | √ | 0 |  |
| 93 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 94 | fauxqty | fauxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 95 | fcuramountandtax | fcuramountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 96 | fminorderbaseqty | fminorderbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 97 | fmatchpricelist | fmatchpricelist | int8 | 64 |  | √ | 0 |  |
| 98 | fcusmatid | fcusmatid | int8 | 64 |  | √ | 0 |  |
| 99 | fmaterialname | fmaterialname | varchar | 800 |  | √ | ' ' |  |
| 100 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 101 | fk_bj73_textfield6 | fk_bj73_textfield6 | varchar | 50 |  | √ | ' ' |  |
| 102 | frowclosestatus | frowclosestatus | varchar | 5 |  | √ | ' ' |  |
| 103 | fk_bj73_materielfield | fk_bj73_materielfield | int8 | 64 |  | √ | 0 |  |
| 104 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 105 | fentrystatus | fentrystatus | varchar | 5 |  | √ | ' ' |  |
| 106 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 107 | fissuedqty | fissuedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 108 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 109 | fbonded | fbonded | bpchar | 1 |  | √ | '0' |  |
| 110 | fcorebillno | fcorebillno | varchar | 80 |  | √ | ' ' |  |
| 111 | fproorgid | fproorgid | int8 | 64 |  | √ | 0 |  |
| 112 | fk_bj73_materialmasterid | fk_bj73_materialmasterid | int8 | 64 |  | √ | 0 |  |
| 113 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 114 | fbomentryid | fbomentryid | int8 | 64 |  | √ | 0 |  |
| 115 | frowterminatemanual | frowterminatemanual | bpchar | 1 |  | √ | '0' |  |
| 116 | fauxunit2id | fauxunit2id | int8 | 64 |  | √ | 0 |  |
| 117 | fdeliverbaseqtydown | fdeliverbaseqtydown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 118 | fsettleamount | fsettleamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 119 | fsuitepricepercent | fsuitepricepercent | numeric | 23 | 10 | √ | 0 |  |
| 120 | fiscontrolday | fiscontrolday | bpchar | 1 |  | √ | '0' |  |
| 121 | famountandtax | famountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 122 | fdeliverydate | fdeliverydate | timestamp | 0 |  |  | null |  |
| 123 | fcusmaterialname | fcusmaterialname | varchar | 50 |  | √ | ' ' |  |
| 124 | fcurtaxamount | fcurtaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 125 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 126 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

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
