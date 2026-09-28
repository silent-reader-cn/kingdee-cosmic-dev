# 销售订单F7-sm_salorder_f7

## 销售订单F7-主表 t_sm_salorder

- **表名称：** 销售订单F7-主表
- **表名：** t_sm_salorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | faddress | varchar | 512 |  |  | null |  |
| 3 | fprereceiptamount | fprereceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 8 | flocation | flocation | varchar | 255 |  |  | null |  |
| 9 | fassociatemargin | fassociatemargin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 11 | ftransactepathid | ftransactepathid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fistax | fistax | bpchar | 1 |  | √ | '0' |  |
| 15 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 16 | fcurtotalamount | fcurtotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | forderstatus | forderstatus | bpchar | 1 |  | √ | 'A' |  |
| 18 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 19 | fcloserid | fcloserid | int8 | 64 |  | √ | 0 |  |
| 20 | freccustomerid | freccustomerid | int8 | 64 |  | √ | 0 |  |
| 21 | fdeliveraddressf7 | fdeliveraddressf7 | int8 | 64 |  | √ | 0 |  |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fversion | fversion | varchar | 20 |  | √ | ' ' |  |
| 24 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fmarginlevel | fmarginlevel | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fisinitbill | fisinitbill | bpchar | 1 |  | √ | '0' |  |
| 28 | fdiscountlistid | fdiscountlistid | int8 | 64 |  | √ | 0 |  |
| 29 | fmpmrecmethod | fmpmrecmethod | varchar | 50 |  | √ | ' ' |  |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 32 | freceiptamount | freceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 34 | fbillsource | fbillsource | bpchar | 1 |  | √ | 'A' |  |
| 35 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 36 | fexchangetype | fexchangetype | varchar | 5 |  | √ | ' ' |  |
| 37 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 38 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 39 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 40 | ftotaltaxamount | ftotaltaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 43 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 44 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 45 | freclinkmanid | freclinkmanid | int8 | 64 |  | √ | 0 |  |
| 46 | fbiztime | fbiztime | timestamp | 0 |  |  | null |  |
| 47 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 48 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 49 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 50 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 51 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 52 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 53 | fpayingcustomerid | fpayingcustomerid | int8 | 64 |  | √ | 0 |  |
| 54 | fiswholediscount | fiswholediscount | bpchar | 1 |  | √ | '0' |  |
| 55 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 56 | frecconditionid | frecconditionid | int8 | 64 |  | √ | 0 |  |
| 57 | fmargin | fmargin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 58 | fassrefundmargin | fassrefundmargin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 59 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 60 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 61 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 62 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 63 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 64 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 65 | fcurtotalallamount | fcurtotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 66 | finternal | finternal | bpchar | 1 |  | √ | '0' |  |
| 67 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 68 | fwholediscountamount | fwholediscountamount | numeric | 23 | 10 | √ | 0 |  |
| 69 | fdeliverywayid | fdeliverywayid | int8 | 64 |  | √ | 0 |  |
| 70 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 71 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 72 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 73 | fclosemanual | fclosemanual | bpchar | 1 |  | √ | '0' |  |
| 74 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 75 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 76 | fbizdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 77 | finputamount | finputamount | bpchar | 1 |  | √ | '0' |  |
| 78 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 79 | fsettlecustomerid | fsettlecustomerid | int8 | 64 |  | √ | 0 |  |
| 80 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 81 | ftotalallamount | ftotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 82 | freceiveaddress | freceiveaddress | varchar | 512 |  |  | null |  |

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
