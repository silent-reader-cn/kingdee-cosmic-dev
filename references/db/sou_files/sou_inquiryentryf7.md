# 询价单物料列表-sou_inquiryentryf7

## 询价单物料列表-主表 t_pur_inquiryentry

- **表名称：** 询价单物料列表-主表
- **表名：** t_pur_inquiryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 询价单ID | int8 | 64 |  | √ | 0 | 询价单ID |
| 2 | flatestpricingnotes | 最新议价备注 | varchar | 512 |  | √ | ' ' | 最新议价备注 |
| 3 | fdelidate | fdelidate | timestamp | 0 |  |  | null |  |
| 4 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fblueprintstatus | fblueprintstatus | bpchar | 1 |  |  | ' ' |  |
| 6 | ftaxrate | ftaxrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 10 | fnote | fnote | varchar | 512 |  | √ | ' ' |  |
| 11 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | famount | famount | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fdctamount | fdctamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 16 | fdeliaddr | fdeliaddr | varchar | 255 |  | √ | ' ' |  |
| 17 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 18 | ftaxamount | ftaxamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 19 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 20 | fdctrate | fdctrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 21 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 22 | ftraceid | ftraceid | int8 | 64 |  | √ | 0 |  |
| 23 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 24 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fpcbillno | fpcbillno | varchar | 80 |  | √ | ' ' |  |
| 26 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fnewestturns | fnewestturns | varchar | 10 |  | √ | ' ' |  |
| 28 | fdelitypeid | fdelitypeid | int8 | 64 |  | √ | 0 |  |
| 29 | ftax | ftax | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 31 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 32 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 33 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fpobillno | fpobillno | varchar | 80 |  | √ | ' ' |  |
| 36 | fvalidnum | fvalidnum | int4 | 32 |  | √ | 0 |  |
| 37 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_inquiryentry_pkey |  | fentryid |
| 2 | idx_inquiryentry_fmaterialid |  | fmaterialid |
| 3 | idx_inquiryentry_fid_fseq |  | fid,fseq |
