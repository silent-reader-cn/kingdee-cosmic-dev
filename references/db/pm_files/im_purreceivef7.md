# 收料通知单F7-im_purreceivef7

## 收料通知单F7-主表 t_im_purrecbill

- **表名称：** 收料通知单F7-主表
- **表名：** t_im_purrecbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 收料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fischargeoff | fischargeoff | bpchar | 1 |  | √ | '0' |  |
| 7 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fistax | fistax | bpchar | 1 |  | √ | '1' |  |
| 9 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 10 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fischargeoffed | fischargeoffed | bpchar | 1 |  | √ | '0' |  |
| 13 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 16 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 17 | fbillcretype | fbillcretype | bpchar | 1 |  | √ | '0' |  |
| 18 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 19 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 20 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 21 | fbizdeptid | fbizdeptid | int8 | 64 |  | √ | 0 |  |
| 22 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 24 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 25 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 26 | fhasapbusbill | fhasapbusbill | bpchar | 1 |  | √ | '0' |  |
| 27 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fbizoperatorid | fbizoperatorid | int8 | 64 |  | √ | 0 |  |
| 29 | finvschemeid | finvschemeid | int8 | 64 |  | √ | 0 |  |
| 30 | fquotation | fquotation | varchar | 50 |  | √ | '0' |  |
| 31 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 32 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 34 | fiswholediscount | fiswholediscount | bpchar | 1 |  | √ | '0' |  |
| 35 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 36 | funitsrctype | funitsrctype | varchar | 30 |  | √ | 'NULL' |  |
| 37 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 38 | fcomment | fcomment | varchar | 512 |  | √ | ' ' |  |
| 39 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 40 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 41 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 42 | fwholediscountamount | fwholediscountamount | numeric | 23 | 10 | √ | 0 |  |
| 43 | fbizoperatorgroupid | fbizoperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 44 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 45 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 46 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | 'A' |  |
| 47 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 48 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 49 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 50 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 51 | facceptancestatus | facceptancestatus | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_purrecbill_pkey |  | fid |
| 2 | idx_im_purrecbill_forgbillno |  | fbillno,forgid |
| 3 | idx_im_purrecbill_supp |  | fsupplierid |
| 4 | idx_im_purrecbill_org |  | forgid |
| 5 | idx_im_purrecbill_biztorgno |  | fbiztime,forgid,fbillno |
| 6 | idx_im_prbill_bktorgno |  | fbookdate,forgid,fbillno |
