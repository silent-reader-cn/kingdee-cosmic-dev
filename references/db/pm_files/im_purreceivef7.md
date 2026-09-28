# 收料通知单F7-im_purreceivef7

## 收料通知单F7-主表 t_im_purrecbill

- **表名称：** 收料通知单F7-主表
- **表名：** t_im_purrecbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 3 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fclosedate | fclosedate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fischargeoff | fischargeoff | bpchar | 1 |  | √ | '0' |  |
| 8 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fistax | fistax | bpchar | 1 |  | √ | '1' |  |
| 10 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 11 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fischargeoffed | fischargeoffed | bpchar | 1 |  | √ | '0' |  |
| 14 | fdeptid | fdeptid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 17 | ftrdbillno | ftrdbillno | varchar | 50 |  | √ | ' ' |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | fbillcretype | fbillcretype | bpchar | 1 |  | √ | '0' |  |
| 20 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | ftraderouteid | ftraderouteid | int8 | 64 |  | √ | 0 |  |
| 22 | fisintransit | fisintransit | bpchar | 1 |  | √ | '0' |  |
| 23 | fbookdate | fbookdate | timestamp | 0 |  |  | null |  |
| 24 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 25 | fbizdeptid | fbizdeptid | int8 | 64 |  | √ | 0 |  |
| 26 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 30 | fhasapbusbill | fhasapbusbill | bpchar | 1 |  | √ | '0' |  |
| 31 | fendbill | fendbill | bpchar | 1 |  | √ | '0' |  |
| 32 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | fbizoperatorid | fbizoperatorid | int8 | 64 |  | √ | 0 |  |
| 34 | finvschemeid | finvschemeid | int8 | 64 |  | √ | 0 |  |
| 35 | fquotation | fquotation | varchar | 50 |  | √ | '0' |  |
| 36 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 37 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 39 | fiswholediscount | fiswholediscount | bpchar | 1 |  | √ | '0' |  |
| 40 | fisimport | fisimport | bpchar | 1 |  | √ | '0' |  |
| 41 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 42 | fdeclareformed | fdeclareformed | bpchar | 1 |  | √ | '0' |  |
| 43 | funitsrctype | funitsrctype | varchar | 30 |  | √ | 'NULL' |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | fstep | fstep | int4 | 32 |  | √ | 0 |  |
| 46 | fcomment | fcomment | varchar | 512 |  | √ | ' ' |  |
| 47 | foperatorgroupid | foperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 48 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 49 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 50 | fwholediscountamount | fwholediscountamount | numeric | 23 | 10 | √ | 0 |  |
| 51 | fbizoperatorgroupid | fbizoperatorgroupid | int8 | 64 |  | √ | 0 |  |
| 52 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 53 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 54 | fclosestatus | fclosestatus | bpchar | 1 |  | √ | 'A' |  |
| 55 | flogistics | flogistics | bpchar | 1 |  | √ | '0' |  |
| 56 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 57 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 58 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 59 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 60 | facceptancestatus | facceptancestatus | bpchar | 1 |  | √ | '0' |  |

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
