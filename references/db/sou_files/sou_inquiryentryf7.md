# 询价单物料列表-sou_inquiryentryf7

## 询价单物料列表-主表 t_pur_inquiryentry

- **表名称：** 询价单物料列表-主表
- **表名：** t_pur_inquiryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 询价单ID | int8 | 64 |  | √ | 0 | 询价单ID |
| 2 | fdelidate | fdelidate | timestamp | 0 |  |  | null |  |
| 3 | freqorgid | freqorgid | int8 | 64 |  | √ | 0 |  |
| 4 | ftaxrate | ftaxrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 8 | fnote | fnote | varchar | 512 |  | √ | ' ' |  |
| 9 | ftaxprice | ftaxprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | famount | famount | numeric | 19 | 6 | √ | 0.000000 |  |
| 11 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fdctamount | fdctamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 13 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 14 | fdeliaddr | fdeliaddr | varchar | 255 |  | √ | ' ' |  |
| 15 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 16 | ftaxamount | ftaxamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fdctrate | fdctrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 19 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 20 | ftraceid | ftraceid | int8 | 64 |  | √ | 0 |  |
| 21 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fpcbillno | fpcbillno | varchar | 80 |  | √ | ' ' |  |
| 24 | fpayorgid | fpayorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fnewestturns | fnewestturns | varchar | 10 |  | √ | ' ' |  |
| 26 | fdelitypeid | fdelitypeid | int8 | 64 |  | √ | 0 |  |
| 27 | ftax | ftax | numeric | 19 | 6 | √ | 0.000000 |  |
| 28 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 29 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 30 | fsettleorgid | fsettleorgid | int8 | 64 |  | √ | 0 |  |
| 31 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fpobillno | fpobillno | varchar | 80 |  | √ | ' ' |  |
| 34 | fvalidnum | fvalidnum | int4 | 32 |  | √ | 0 |  |
| 35 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |

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
