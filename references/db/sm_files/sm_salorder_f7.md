# 销售订单F7-sm_salorder_f7

## 销售订单F7-主表 t_sm_salorder

- **表名称：** 销售订单F7-主表
- **表名：** t_sm_salorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprereceiptamount | fprereceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 6 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fconsigngencrossorg | fconsigngencrossorg | bpchar | 1 |  | √ | '0' |  |
| 9 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 10 | forderstatus | forderstatus | bpchar | 1 |  | √ | 'A' |  |
| 11 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 12 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 13 | fdeliveraddressf7 | fdeliveraddressf7 | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fversion | fversion | varchar | 20 |  | √ | ' ' |  |
| 16 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmarginlevel | fmarginlevel | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | fisinitbill | fisinitbill | bpchar | 1 |  | √ | '0' |  |
| 19 | fdiscountlistid | fdiscountlistid | int8 | 64 |  | √ | 0 |  |
| 20 | ftraderouteid | ftraderouteid | int8 | 64 |  | √ | 0 |  |
| 21 | freceiptamount | freceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fk_bj73_assistantfield1 | fk_bj73_assistantfield1 | int8 | 64 |  |  | null |  |
| 23 | fk_bj73_assistantfield2 | fk_bj73_assistantfield2 | int8 | 64 |  | √ | 0 |  |
| 24 | fbillsource | fbillsource | bpchar | 1 |  | √ | 'A' |  |
| 25 | fexchangetype | fexchangetype | varchar | 5 |  | √ | ' ' |  |
| 26 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 28 | ftotaltaxamount | ftotaltaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | ftradetermid | ftradetermid | int8 | 64 |  | √ | 0 |  |
| 31 | fprojinvctrltype | fprojinvctrltype | varchar | 50 |  | √ | ' ' |  |
| 32 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 33 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 34 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 35 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 36 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 37 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 38 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 39 | frecconditionid | frecconditionid | int8 | 64 |  | √ | 0 |  |
| 40 | funreceiptamount | funreceiptamount | numeric | 23 | 10 | √ | 0 |  |
| 41 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 42 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 43 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 44 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 45 | fcurtotalallamount | fcurtotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | finternal | finternal | bpchar | 1 |  | √ | '0' |  |
| 47 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 48 | fwholediscountamount | fwholediscountamount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fdeliverywayid | fdeliverywayid | int8 | 64 |  | √ | 0 |  |
| 50 | fsrcport | fsrcport | varchar | 512 |  | √ | ' ' |  |
| 51 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 52 | foutmargin | foutmargin | numeric | 23 | 10 | √ | 0 |  |
| 53 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 54 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 55 | favailablemargin | favailablemargin | numeric | 23 | 10 | √ | 0 |  |
| 56 | frelatemargin | frelatemargin | numeric | 23 | 10 | √ | 0 |  |
| 57 | finputamount | finputamount | bpchar | 1 |  | √ | '0' |  |
| 58 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 59 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 60 | freceiveaddress | freceiveaddress | varchar | 200 |  |  | null |  |
| 61 | fcarrierid | fcarrierid | int8 | 64 |  | √ | 0 |  |
| 62 | faddress | faddress | varchar | 512 |  |  | null |  |
| 63 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 64 | flocation | flocation | varchar | 255 |  |  | null |  |
| 65 | fassociatemargin | fassociatemargin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 66 | ftransactepathid | ftransactepathid | int8 | 64 |  | √ | 0 |  |
| 67 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 68 | fistax | fistax | bpchar | 1 |  | √ | '0' |  |
| 69 | ftradestatus | ftradestatus | bpchar | 1 |  | √ | ' ' |  |
| 70 | fcurtotalamount | fcurtotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 71 | freccustomerid | freccustomerid | int8 | 64 |  | √ | 0 |  |
| 72 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 73 | fmpmrecmethod | fmpmrecmethod | varchar | 50 |  | √ | ' ' |  |
| 74 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 75 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 76 | fdescountryid | fdescountryid | int8 | 64 |  | √ | 0 |  |
| 77 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 78 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 79 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 80 | fk_bj73_assistantfield | fk_bj73_assistantfield | int8 | 64 |  |  | null |  |
| 81 | flinkaddressf7 | flinkaddressf7 | int8 | 64 |  | √ | 0 |  |
| 82 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 83 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 84 | fk_bj73_datetimefield | fk_bj73_datetimefield | timestamp | 0 |  |  | null |  |
| 85 | fk_bj73_textfield4 | fk_bj73_textfield4 | varchar | 50 |  | √ | ' ' |  |
| 86 | fk_bj73_textfield5 | fk_bj73_textfield5 | varchar | 50 |  | √ | ' ' |  |
| 87 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 88 | freclinkmanid | freclinkmanid | int8 | 64 |  | √ | 0 |  |
| 89 | fk_bj73_textfield2 | fk_bj73_textfield2 | varchar | 50 |  | √ | ' ' |  |
| 90 | fendbill | fendbill | bpchar | 1 |  | √ | '0' |  |
| 91 | fk_bj73_textfield3 | fk_bj73_textfield3 | varchar | 50 |  | √ | ' ' |  |
| 92 | fbiztime | fbiztime | timestamp | 0 |  |  | null |  |
| 93 | fk_bj73_textfield1 | fk_bj73_textfield1 | varchar | 50 |  | √ | ' ' |  |
| 94 | fsrccountryid | fsrccountryid | int8 | 64 |  | √ | 0 |  |
| 95 | fpayingcustomerid | fpayingcustomerid | int8 | 64 |  | √ | 0 |  |
| 96 | fiswholediscount | fiswholediscount | bpchar | 1 |  | √ | '0' |  |
| 97 | fmargin | fmargin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 98 | fassrefundmargin | fassrefundmargin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 99 | fstep | fstep | int4 | 32 |  | √ | 0 |  |
| 100 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 101 | fdesport | fdesport | varchar | 512 |  | √ | ' ' |  |
| 102 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 103 | fclosemanual | fclosemanual | bpchar | 1 |  | √ | '0' |  |
| 104 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 105 | fisexport | fisexport | bpchar | 1 |  | √ | '0' |  |
| 106 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 107 | fbizdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 108 | ftransportmodeid | ftransportmodeid | int8 | 64 |  | √ | 0 |  |
| 109 | fk_bj73_textfield | fk_bj73_textfield | varchar | 50 |  | √ | ' ' |  |
| 110 | fsettlecustomerid | fsettlecustomerid | int8 | 64 |  | √ | 0 |  |
| 111 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 112 | ftotalallamount | ftotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_salorder_customer |  | fcustomerid |
| 2 | idx_sm_salorder_fbizdate |  | fbizdate |
| 3 | t_sm_salorder_pkey |  | fid |
| 4 | idx_uniq_salorder_billnoorg |  | fbillno,forgid |
| 5 | idx_sm_salorder_forgid |  | forgid,fbizdate,fbiztime,fid |
