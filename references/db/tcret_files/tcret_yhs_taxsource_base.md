# 印花税税源信息基础资料-tcret_yhs_taxsource_base

## 印花税税源信息基础资料-主表 t_tcret_sycj_yhsxx

- **表名称：** 印花税税源信息基础资料-主表
- **表名：** t_tcret_sycj_yhsxx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxrate | ftaxrate | varchar | 50 |  | √ | ' ' |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fvoucherdate | fvoucherdate | timestamp | 0 |  |  | null |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fvouchertaxno | fvouchertaxno | varchar | 50 |  | √ | ' ' |  |
| 7 | fbizdimensiontype | fbizdimensiontype | varchar | 50 |  | √ | ' ' |  |
| 8 | fsbbbillno | fsbbbillno | varchar | 50 |  | √ | ' ' |  |
| 9 | fdfslrmc | fdfslrmc | varchar | 50 |  | √ | ' ' |  |
| 10 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fsbbbillstatus | fsbbbillstatus | varchar | 50 |  | √ | ' ' |  |
| 12 | fbillstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fverifyrate | fverifyrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fserialno | fserialno | varchar | 50 |  | √ | ' ' |  |
| 15 | ftaxlimit | ftaxlimit | varchar | 50 |  | √ | ' ' |  |
| 16 | fvouchernum | fvouchernum | int8 | 64 |  | √ | 0 |  |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fskssqq | fskssqq | timestamp | 0 |  |  | null |  |
| 19 | fdeductioncode | fdeductioncode | int8 | 64 |  | √ | 0 |  |
| 20 | factualsettledate | factualsettledate | timestamp | 0 |  |  | null |  |
| 21 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 22 | fbusdimension | fbusdimension | int8 | 64 |  | √ | 0 |  |
| 23 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 24 | ftaxoffice | ftaxoffice | int8 | 64 |  | √ | 0 |  |
| 25 | fbizdimensionid | fbizdimensionid | varchar | 50 |  | √ | ' ' |  |
| 26 | factualsettleamount | factualsettleamount | numeric | 23 | 10 | √ | 0 |  |
| 27 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 28 | faccountorg | faccountorg | int8 | 64 |  | √ | 0 |  |
| 29 | fisxgm | fisxgm | bpchar | 1 |  | √ | '0' |  |
| 30 | ftaxitem | ftaxitem | int8 | 64 |  | √ | 0 |  |
| 31 | fdfslrsjje | fdfslrsjje | numeric | 23 | 10 | √ | 0 |  |
| 32 | fgathernumber | fgathernumber | varchar | 50 |  | √ | ' ' |  |
| 33 | fvoucherno | fvoucherno | varchar | 50 |  | √ | ' ' |  |
| 34 | ftaxation | ftaxation | varchar | 50 |  | √ | ' ' |  |
| 35 | fdfslrnssbh | fdfslrnssbh | varchar | 50 |  | √ | ' ' |  |
| 36 | fdeclarestatus | fdeclarestatus | varchar | 50 |  | √ | ' ' |  |
| 37 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 38 | fvouchername | fvouchername | varchar | 50 |  | √ | ' ' |  |
| 39 | fskssqz | fskssqz | timestamp | 0 |  |  | null |  |
| 40 | fsubtaxitem | fsubtaxitem | int8 | 64 |  | √ | 0 |  |
| 41 | fynse | fynse | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fyjse | fyjse | numeric | 23 | 10 | √ | 0 |  |
| 43 | fcalctaxamount | fcalctaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 46 | fbizdimensionname | fbizdimensionname | varchar | 200 |  | √ | ' ' |  |
| 47 | fbusdimensionmap | fbusdimensionmap | int8 | 64 |  | √ | 0 |  |
| 48 | fdeclaretype | fdeclaretype | varchar | 50 |  | √ | ' ' |  |
| 49 | fdeclareid | fdeclareid | int8 | 64 |  | √ | 0 |  |
| 50 | fpaytype | fpaytype | varchar | 50 |  | √ | ' ' |  |
| 51 | fverifybasis | fverifybasis | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fdeducttax | fdeducttax | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_sycj_yhsxx |  | fid |
| 2 | idx_tcret_sycj_yhsxx |  | forgid,fskssqq,fskssqz |
