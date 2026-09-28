# 采购订单F7-pm_purorder_f7

## 采购订单F7-主表 t_pm_purorderbill

- **表名称：** 采购订单F7-主表
- **表名：** t_pm_purorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | faddress | varchar | 512 |  | √ | ' ' |  |
| 3 | fpaidallamount | fpaidallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fproviderlinkmanid | fproviderlinkmanid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 8 | fcancelstatus | fcancelstatus | varchar | 5 |  | √ | ' ' |  |
| 9 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 10 | ftransactepathid | ftransactepathid | int8 | 64 |  | √ | 0 |  |
| 11 | fsplitschemeid | fsplitschemeid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fistax | fistax | bpchar | 1 |  | √ | '1' |  |
| 15 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 16 | finvoicesupplierid | finvoicesupplierid | int8 | 64 |  | √ | 0 |  |
| 17 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 18 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 20 | fversion | fversion | varchar | 30 |  | √ | '1' |  |
| 21 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fisinitbill | fisinitbill | bpchar | 1 |  | √ | '0' |  |
| 24 | fpayconditionid | fpayconditionid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | fbillcretype | fbillcretype | varchar | 5 |  | √ | '0' |  |
| 27 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | freceivesupplierid | freceivesupplierid | int8 | 64 |  | √ | 0 |  |
| 29 | fpaidpreallamount | fpaidpreallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fcanceldate | fcanceldate | timestamp | 0 |  |  | null |  |
| 31 | fchangerid | fchangerid | int8 | 64 |  | √ | 0 |  |
| 32 | fexchangetype | fexchangetype | varchar | 5 |  | √ | ' ' |  |
| 33 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 34 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 35 | fsettlecurrencyid | fsettlecurrencyid | int8 | 64 |  | √ | 0 |  |
| 36 | ftotaltaxamount | ftotaltaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 39 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 40 | fdiscountlist | fdiscountlist | int8 | 64 |  | √ | 0 |  |
| 41 | fconfirmstatus | fconfirmstatus | varchar | 5 |  | √ | ' ' |  |
| 42 | fbiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 43 | flogisticsstatus | flogisticsstatus | varchar | 5 |  | √ | ' ' |  |
| 44 | fchangestatus | fchangestatus | varchar | 5 |  | √ | ' ' |  |
| 45 | fsupplytrans | fsupplytrans | bpchar | 1 |  | √ | '0' |  |
| 46 | fprovideraddress | fprovideraddress | varchar | 512 |  |  | ' ' |  |
| 47 | fcancelerid | fcancelerid | int8 | 64 |  | √ | 0 |  |
| 48 | fpaystatus | fpaystatus | varchar | 5 |  | √ | ' ' |  |
| 49 | fpricelistid | fpricelistid | int8 | 64 |  | √ | 0 |  |
| 50 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 51 | fisvirtualbill | fisvirtualbill | bpchar | 1 |  | √ | '0' |  |
| 52 | fchangedate | fchangedate | timestamp | 0 |  |  | null |  |
| 53 | fiswholediscount | fiswholediscount | bpchar | 1 |  | √ | '0' |  |
| 54 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 55 | funitsrctype | funitsrctype | varchar | 30 |  | √ | ' ' |  |
| 56 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 57 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 58 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 59 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 60 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 61 | finternal | finternal | bpchar | 1 |  | √ | '0' |  |
| 62 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 63 | fwholediscountamount | fwholediscountamount | numeric | 23 | 10 | √ | 0 |  |
| 64 | fprovidersupplierid | fprovidersupplierid | int8 | 64 |  | √ | 0 |  |
| 65 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 66 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 67 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 68 | fpaymode | fpaymode | varchar | 30 |  | √ | 'CREDIT' |  |
| 69 | fsubversion | fsubversion | varchar | 30 |  | √ | '1' |  |
| 70 | finputamount | finputamount | bpchar | 1 |  | √ | '0' |  |
| 71 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 72 | ftaxinprice | ftaxinprice | bpchar | 1 |  | √ | '0' |  |
| 73 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 74 | ftotalallamount | ftotalallamount | numeric | 23 | 10 | √ | 0.0000000000 |  |

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
