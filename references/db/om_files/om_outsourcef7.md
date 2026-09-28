# 委外订单分录f7-om_outsourcef7

## 委外订单分录f7-主表 t_pm_om_purbillentry

- **表名称：** 委外订单分录f7-主表
- **表名：** t_pm_om_purbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqtyup | freceiveqtyup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fdiscountrate | fdiscountrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fdeliverlocationid | fdeliverlocationid | int8 | 64 |  | √ | 0 |  |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentrycreatorid | fentrycreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fdeliverdate | fdeliverdate | timestamp | 0 |  |  | null |  |
| 9 | fbomreplacename | fbomreplacename | varchar | 50 |  | √ | ' ' |  |
| 10 | fcuramount | fcuramount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fentrymodifierid | fentrymodifierid | int8 | 64 |  | √ | 0 |  |
| 12 | freceivebaseqtydown | freceivebaseqtydown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | ftaxamount | ftaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 15 | fdeliveraddress | fdeliveraddress | varchar | 512 |  |  | ' ' |  |
| 16 | foproperation | foproperation | varchar | 50 |  | √ | ' ' |  |
| 17 | freceivebaseqtyup | freceivebaseqtyup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fispresent | fispresent | bpchar | 1 |  | √ | '0' |  |
| 20 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 21 | fmaterialmasterid | fmaterialmasterid | int8 | 64 |  | √ | 0 |  |
| 22 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 23 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fentrychangetype | fentrychangetype | varchar | 30 |  | √ | ' ' |  |
| 26 | flinetypeid | flinetypeid | int8 | 64 |  | √ | '1194150915045641216' |  |
| 27 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 28 | freceiveqtydown | freceiveqtydown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fbomversion | fbomversion | int8 | 64 |  | √ | 0 |  |
| 30 | fsupplierlot | fsupplierlot | varchar | 50 |  | √ | ' ' |  |
| 31 | fdiscountamount | fdiscountamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | famount | famount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 34 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 35 | fauxunitid | fauxunitid | int8 | 64 |  | √ | 0 |  |
| 36 | fbomname | fbomname | varchar | 50 |  | √ | ' ' |  |
| 37 | fentryrecorgid | fentryrecorgid | int8 | 64 |  | √ | 0 |  |
| 38 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 39 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 40 | fiscontrolamountup | fiscontrolamountup | bpchar | 1 |  | √ | '0' |  |
| 41 | fbomreplaceno | fbomreplaceno | int8 | 64 |  | √ | 0 |  |
| 42 | fdiscounttype | fdiscounttype | varchar | 5 |  | √ | ' ' |  |
| 43 | fecnversion | fecnversion | int8 | 64 |  | √ | 0 |  |
| 44 | fbomversionname | fbomversionname | varchar | 50 |  | √ | ' ' |  |
| 45 | fentryrecdeptid | fentryrecdeptid | int8 | 64 |  | √ | 0 |  |
| 46 | fentryreqdeptid | fentryreqdeptid | int8 | 64 |  | √ | 0 |  |
| 47 | frowterminatestatus | 行终止状态 | varchar | 30 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 48 | foprentryid | foprentryid | int8 | 64 |  | √ | 0 |  |
| 49 | fentrypurorgid | fentrypurorgid | int8 | 64 |  | √ | 0 |  |
| 50 | fentrycomment | fentrycomment | varchar | 512 |  | √ | ' ' |  |
| 51 | freceivedaydown | freceivedaydown | int4 | 32 |  | √ | 0 |  |
| 52 | ftechid | ftechid | int8 | 64 |  | √ | 0 |  |
| 53 | fentrymodifytime | fentrymodifytime | timestamp | 0 |  |  | null |  |
| 54 | ftaxrate | ftaxrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 55 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 56 | freceiverateup | freceiverateup | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 57 | fentrysettledeptid | fentrysettledeptid | int8 | 64 |  | √ | 0 |  |
| 58 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 59 | fentrysettleorgid | fentrysettleorgid | int8 | 64 |  | √ | 0 |  |
| 60 | foproperationid | foproperationid | int8 | 64 |  | √ | 0 |  |
| 61 | fownertype | fownertype | varchar | 36 |  | √ | ' ' |  |
| 62 | fmaterialversionid | fmaterialversionid | int8 | 64 |  | √ | 0 |  |
| 63 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 64 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 65 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 66 | fexpenseitemid | fexpenseitemid | int8 | 64 |  | √ | 0 |  |
| 67 | fpickingpairs | fpickingpairs | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 68 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 69 | fpromisedate | fpromisedate | timestamp | 0 |  |  | null |  |
| 70 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 71 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 72 | foprdescription | foprdescription | varchar | 50 |  | √ | ' ' |  |
| 73 | fentrycreatetime | fentrycreatetime | timestamp | 0 |  |  | null |  |
| 74 | frouteid | frouteid | int8 | 64 |  | √ | 0 |  |
| 75 | fauxqty | fauxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 76 | fecnversionname | fecnversionname | varchar | 50 |  | √ | ' ' |  |
| 77 | fcuramountandtax | fcuramountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 78 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 79 | fentrypayorgid | fentrypayorgid | int8 | 64 |  | √ | 0 |  |
| 80 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 81 | fentryreqorgid | fentryreqorgid | int8 | 64 |  | √ | 0 |  |
| 82 | frowclosestatus | 行关闭状态 | varchar | 30 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 83 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 84 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 85 | freceiveratedown | freceiveratedown | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 86 | ftechno | ftechno | varchar | 50 |  | √ | ' ' |  |
| 87 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 88 | froutename | froutename | varchar | 50 |  | √ | ' ' |  |
| 89 | fiscontrolday | fiscontrolday | bpchar | 1 |  | √ | '0' |  |
| 90 | famountandtax | famountandtax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 91 | freceivedayup | freceivedayup | int4 | 32 |  | √ | 0 |  |
| 92 | foproperationname | foproperationname | varchar | 50 |  | √ | ' ' |  |
| 93 | famountup | famountup | numeric | 23 | 10 | √ | 0 |  |
| 94 | fexpendbomtime | fexpendbomtime | timestamp | 0 |  |  | null |  |
| 95 | fcurtaxamount | fcurtaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 96 | foprentryseq | foprentryseq | int8 | 64 |  | √ | 0 |  |
| 97 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_om_purbillentry_pkey |  | fentryid |
| 2 | idx_pm_om_purbillentry |  | fid |

---

## 委外订单分录f7-分表 t_pm_om_purbillentry_r

- **表名称：** 委外订单分录f7-分表
- **表名：** t_pm_om_purbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | fsrcsystem | varchar | 100 |  | √ | ' ' |  |
| 3 | finvretqty | finvretqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 4 | fsoubillid | fsoubillid | int8 | 64 |  | √ | 0 |  |
| 5 | freceiptnoticeqty | freceiptnoticeqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | fmainbillentity | fmainbillentity | varchar | 50 |  | √ | ' ' |  |
| 7 | finvbaseqty | finvbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | freturnbaseqty | freturnbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 10 | fconbillrownum | fconbillrownum | varchar | 50 |  | √ | ' ' |  |
| 11 | fconbillnumber | fconbillnumber | varchar | 255 |  | √ | ' ' |  |
| 12 | fmainbillid | fmainbillid | int8 | 64 |  | √ | 0 |  |
| 13 | freceivebaseqty | freceivebaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fsrcsysbillno | fsrcsysbillno | varchar | 100 |  | √ | ' ' |  |
| 15 | fpayableamount | fpayableamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fsrcbillnumber | fsrcbillnumber | varchar | 50 |  | √ | ' ' |  |
| 17 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 18 | fmainbillnumber | fmainbillnumber | varchar | 50 |  | √ | ' ' |  |
| 19 | finvqty | finvqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fsoubillnumber | fsoubillnumber | varchar | 80 |  | √ | ' ' |  |
| 21 | freceiptnoticbaseqty | freceiptnoticbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fsalbillentryseq | fsalbillentryseq | int8 | 64 |  | √ | 0 |  |
| 23 | fsrcsysbillentryid | fsrcsysbillentryid | varchar | 100 |  | √ | ' ' |  |
| 24 | fsalbillid | fsalbillid | int8 | 64 |  | √ | 0 |  |
| 25 | frecretqty | frecretqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | freturnreceiptqty | freturnreceiptqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | fsoubillentryseq | fsoubillentryseq | int8 | 64 |  | √ | 0 |  |
| 29 | fsalbillentryid | fsalbillentryid | int8 | 64 |  | √ | 0 |  |
| 30 | freceiveqty | freceiveqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | fconbillid | fconbillid | int8 | 64 |  | √ | 0 |  |
| 32 | fmainbillentryseq | fmainbillentryseq | int8 | 64 |  | √ | 0 |  |
| 33 | fconbillentity | fconbillentity | varchar | 80 |  | √ | ' ' |  |
| 34 | frecretbaseqty | frecretbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fperformamount | fperformamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fconbillentryid | fconbillentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fmftorderid | fmftorderid | int8 | 64 |  | √ | 0 |  |
| 38 | fjoinpayablebaseqty | fjoinpayablebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | finvretbaseqty | finvretbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fpayablebaseqty | fpayablebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fjoinqty | fjoinqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fmftorderentryseq | fmftorderentryseq | int8 | 64 |  | √ | 0 |  |
| 43 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 44 | fconbillentryseq | fconbillentryseq | varchar | 50 |  | √ | ' ' |  |
| 45 | fjoinamount | fjoinamount | numeric | 23 | 10 | √ | 0 |  |
| 46 | fjoinbaseqty | fjoinbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | fsalbillnumber | fsalbillnumber | varchar | 50 |  | √ | ' ' |  |
| 48 | freturnqty | freturnqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | fsoubillentryid | fsoubillentryid | int8 | 64 |  | √ | 0 |  |
| 50 | fmftorderentryid | fmftorderentryid | int8 | 64 |  | √ | 0 |  |
| 51 | fpayablepriceqty | fpayablepriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fproducttype | fproducttype | varchar | 50 |  | √ | ' ' |  |
| 53 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 54 | fsoubillentity | fsoubillentity | varchar | 36 |  | √ | ' ' |  |
| 55 | fmainbillentryid | fmainbillentryid | int8 | 64 |  | √ | 0 |  |
| 56 | fjoinpayablepriceqty | fjoinpayablepriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 57 | freturnreceiptbaseqty | freturnreceiptbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 58 | fsrcsysbillid | fsrcsysbillid | varchar | 100 |  | √ | ' ' |  |
| 59 | fmftordernumber | fmftordernumber | varchar | 80 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_om_purbillentry_r_pkey |  | fentryid |
| 2 | idx_pm_om_purbillentry_r |  | fid |
