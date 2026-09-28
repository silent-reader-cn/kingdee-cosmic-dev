# 采购订单F7-pm_purorder_f7

## 采购订单F7-主表 t_pm_purorderbill

- **表名称：** 采购订单F7-主表
- **表名：** t_pm_purorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmpmpaymethod | fmpmpaymethod | varchar | 5 |  | √ | ' ' |  |
| 3 | fpaidallamount | fpaidallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fproviderlinkmanid | fproviderlinkmanid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 8 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 9 | fsplitschemeid | fsplitschemeid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 12 | finvoicesupplierid | finvoicesupplierid | int8 | 64 |  | √ | 0 |  |
| 13 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 16 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 17 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmarginlevel | fmarginlevel | numeric | 23 | 10 | √ | 0 |  |
| 19 | fisinitbill | fisinitbill | bpchar | 1 |  | √ | '0' |  |
| 20 | ftrdbillno | ftrdbillno | varchar | 50 |  | √ | ' ' |  |
| 21 | fbtbpayrateset | fbtbpayrateset | varchar | 30 |  | √ | ' ' |  |
| 22 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | ftraderouteid | ftraderouteid | int8 | 64 |  | √ | 0 |  |
| 24 | freceivesupplierid | freceivesupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | fpaidpreallamount | fpaidpreallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | fexchangetype | fexchangetype | varchar | 5 |  | √ | ' ' |  |
| 27 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 28 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 29 | ftotaltaxamount | ftotaltaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | ftradetermid | ftradetermid | int8 | 64 |  | √ | 0 |  |
| 32 | flogisticsstatus | flogisticsstatus | varchar | 5 |  | √ | ' ' |  |
| 33 | fk_bj73_operator | fk_bj73_operator | int8 | 64 |  | √ | 0 |  |
| 34 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 35 | fsupplytrans | fsupplytrans | bpchar | 1 |  | √ | '0' |  |
| 36 | fprovideraddress | fprovideraddress | varchar | 512 |  |  | ' ' |  |
| 37 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 38 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 39 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 40 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 41 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 42 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 43 | fmanualclosereason | fmanualclosereason | varchar | 512 |  | √ | ' ' |  |
| 44 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 45 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 46 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 47 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 48 | finternal | finternal | bpchar | 1 |  | √ | '0' |  |
| 49 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 50 | fwholediscountamount | fwholediscountamount | numeric | 23 | 10 | √ | 0 |  |
| 51 | fsrcport | fsrcport | varchar | 512 |  | √ | ' ' |  |
| 52 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 53 | foutmargin | foutmargin | numeric | 23 | 10 | √ | 0 |  |
| 54 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 55 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 56 | favailablemargin | favailablemargin | numeric | 23 | 10 | √ | 0 |  |
| 57 | frelatemargin | frelatemargin | numeric | 23 | 10 | √ | 0 |  |
| 58 | finputamount | finputamount | bpchar | 1 |  | √ | '0' |  |
| 59 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 60 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 61 | fcarrierid | fcarrierid | int8 | 64 |  | √ | 0 |  |
| 62 | faddress | faddress | varchar | 512 |  | √ | ' ' |  |
| 63 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 64 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 65 | fassociatemargin | fassociatemargin | numeric | 23 | 10 | √ | 0 |  |
| 66 | ftransactepathid | ftransactepathid | int8 | 64 |  | √ | 0 |  |
| 67 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 68 | fistax | fistax | bpchar | 1 |  | √ | '1' |  |
| 69 | ftradestatus | ftradestatus | bpchar | 1 |  | √ | ' ' |  |
| 70 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 71 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 72 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 73 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 74 | fdescountryid | fdescountryid | int8 | 64 |  | √ | 0 |  |
| 75 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 76 | fmanualclose | fmanualclose | bpchar | 1 |  | √ | '0' |  |
| 77 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 78 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 79 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 80 | fk_bj73_textfield4 | fk_bj73_textfield4 | varchar | 50 |  | √ | ' ' |  |
| 81 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 82 | fdiscountlist | fdiscountlist | int8 | 64 |  | √ | 0 |  |
| 83 | fconfirmstatus | fconfirmstatus | varchar | 5 |  | √ | ' ' |  |
| 84 | fk_bj73_textfield2 | fk_bj73_textfield2 | varchar | 50 |  | √ | ' ' |  |
| 85 | fendbill | fendbill | bpchar | 1 |  | √ | '0' |  |
| 86 | fbiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 87 | fk_bj73_textfield1 | fk_bj73_textfield1 | varchar | 50 |  | √ | ' ' |  |
| 88 | fpaystatus | fpaystatus | varchar | 5 |  | √ | ' ' |  |
| 89 | fsrccountryid | fsrccountryid | int8 | 64 |  | √ | 0 |  |
| 90 | fiswholediscount | fiswholediscount | bpchar | 1 |  | √ | '0' |  |
| 91 | fisimport | fisimport | bpchar | 1 |  | √ | '0' |  |
| 92 | fbtbpayref | fbtbpayref | varchar | 30 |  | √ | ' ' |  |
| 93 | fmargin | fmargin | numeric | 23 | 10 | √ | 0 |  |
| 94 | fassrefundmargin | fassrefundmargin | numeric | 23 | 10 | √ | 0 |  |
| 95 | fstep | fstep | int4 | 32 |  | √ | 0 |  |
| 96 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 97 | fdesport | fdesport | varchar | 512 |  | √ | ' ' |  |
| 98 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 99 | fprovidersupplierid | fprovidersupplierid | int8 | 64 |  | √ | 0 |  |
| 100 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 101 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 102 | ftransportmodeid | ftransportmodeid | int8 | 64 |  | √ | 0 |  |
| 103 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 104 | ftotalallamount | ftotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorder_supplier |  | fsupplierid |
| 2 | idx_pm_purorderbill_org |  | forgid,fbiztime,fid |
| 3 | idx_pm_purorder_billno_org |  | fbillno,forgid |
| 4 | t_pm_purorderbill_pkey |  | fid |
| 5 | idx_pm_purorder_biztime |  | fbiztime |
