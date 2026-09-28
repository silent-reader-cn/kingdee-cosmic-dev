# 生产领料申请分录F7-im_mdc_mftreqentryf7

## 生产领料申请分录F7-主表 t_im_mdc_mftreqentry

- **表名称：** 生产领料申请分录F7-主表
- **表名：** t_im_mdc_mftreqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | fsrcsystem | varchar | 50 |  | √ | ' ' |  |
| 3 | flogisticsbill | flogisticsbill | bpchar | 1 |  | √ | '0' |  |
| 4 | flength | flength | numeric | 23 | 10 | √ | 0 |  |
| 5 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 6 | fmainbillentity | fmainbillentity | varchar | 50 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 9 | ffilenumber | ffilenumber | varchar | 50 |  | √ | ' ' |  |
| 10 | fdemanddate | fdemanddate | timestamp | 0 |  |  | null |  |
| 11 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 12 | fmainbillid | fmainbillid | int8 | 64 |  | √ | 0 |  |
| 13 | freplacegroup | freplacegroup | varchar | 50 |  | √ | ' ' |  |
| 14 | fdeliverdate | fdeliverdate | timestamp | 0 |  |  | null |  |
| 15 | fauditqty | fauditqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | frowstatus | frowstatus | varchar | 50 |  | √ | ' ' |  |
| 17 | fisstockallot | fisstockallot | bpchar | 1 |  | √ | '0' |  |
| 18 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 19 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 20 | forderentryseq | forderentryseq | varchar | 50 |  | √ | ' ' |  |
| 21 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fsrcbillnumber | fsrcbillnumber | varchar | 50 |  | √ | ' ' |  |
| 23 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 24 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 25 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 26 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 27 | fmainbillnumber | fmainbillnumber | varchar | 50 |  | √ | ' ' |  |
| 28 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 29 | fmversion | fmversion | int8 | 64 |  | √ | 0 |  |
| 30 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 31 | forderno | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 32 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 33 | fmaterialmasterid | fmaterialmasterid | int8 | 64 |  | √ | 0 |  |
| 34 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 35 | flengthunit | flengthunit | int8 | 64 |  | √ | 0 |  |
| 36 | fqtyunit2nd | fqtyunit2nd | numeric | 23 | 10 | √ | 0 |  |
| 37 | fsrcsysbillentryid | fsrcsysbillentryid | varchar | 50 |  | √ | ' ' |  |
| 38 | fsupplymode | fsupplymode | varchar | 50 |  | √ | ' ' |  |
| 39 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 40 | fexpirydate | fexpirydate | timestamp | 0 |  |  | null |  |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | flinetypeid | flinetypeid | int8 | 64 |  | √ | 0 |  |
| 43 | fmaterialname | fmaterialname | varchar | 255 |  | √ | ' ' |  |
| 44 | fmaterialgroup | fmaterialgroup | int8 | 64 |  | √ | 0 |  |
| 45 | foutqty | foutqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | fbigintfield | fbigintfield | int8 | 64 |  | √ | 0 |  |
| 47 | fmainbillentryseq | fmainbillentryseq | int8 | 64 |  | √ | 0 |  |
| 48 | flotnumber | flotnumber | varchar | 50 |  | √ | ' ' |  |
| 49 | fuseoutbaseqty | fuseoutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 51 | funit2ndid | funit2ndid | int8 | 64 |  | √ | 0 |  |
| 52 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 53 | fwmssstatus | fwmssstatus | varchar | 50 |  | √ | ' ' |  |
| 54 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 55 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 56 | forderentryid | forderentryid | int8 | 64 |  | √ | 0 |  |
| 57 | freplaceplan | freplaceplan | int8 | 64 |  | √ | 0 |  |
| 58 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 59 | fworkcard | fworkcard | int8 | 64 |  | √ | 0 |  |
| 60 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 61 | fuseoutqty | fuseoutqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | ffullsize | ffullsize | bpchar | 1 |  | √ | '0' |  |
| 63 | foutinvorg | foutinvorg | int8 | 64 |  | √ | 0 |  |
| 64 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 65 | fpickbaseqty | fpickbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 66 | fwidth | fwidth | numeric | 23 | 10 | √ | 0 |  |
| 67 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 68 | foutbaseqty | foutbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 69 | fauditbaseqty | fauditbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 70 | fdelivercycle | fdelivercycle | int8 | 64 |  | √ | 0 |  |
| 71 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 72 | fmainbillentryid | fmainbillentryid | int8 | 64 |  | √ | 0 |  |
| 73 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 74 | fdoctype | fdoctype | int8 | 64 |  | √ | 0 |  |
| 75 | fentrycomment | fentrycomment | varchar | 512 |  | √ | ' ' |  |
| 76 | fheight | fheight | numeric | 23 | 10 | √ | 0 |  |
| 77 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 78 | fproducedate | fproducedate | timestamp | 0 |  |  | null |  |
| 79 | fwarehousechange | fwarehousechange | bpchar | 1 |  | √ | '0' |  |
| 80 | fsrcsysbillid | fsrcsysbillid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_req_fmainbillid |  | fmainbillid |
| 2 | idx_mdc_req_fmainbillentryid |  | fmainbillentryid |
| 3 | pk_im_mdc_mftreqentry |  | fentryid |
| 4 | idx_mdc_req_fid |  | fid |
| 5 | idx_mdc_req_fmaterielmasterid |  | fmaterielmasterid |
