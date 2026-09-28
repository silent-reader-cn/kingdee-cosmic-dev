# 投标单F7-tnd_tenderbillf7

## 投标单F7-主表 t_src_biddocbill

- **表名称：** 投标单F7-主表
- **表名：** t_src_biddocbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 3 | fissplitdoc | fissplitdoc | bpchar | 1 |  | √ | '0' |  |
| 4 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fisneedbiddoc | fisneedbiddoc | bpchar | 1 |  | √ | '0' |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | fturns | fturns | varchar | 2 |  | √ | ' ' |  |
| 11 | fisadd | fisadd | bpchar | 1 |  | √ | '0' |  |
| 12 | fbillno | 投标单号 | varchar | 30 |  | √ | ' ' | 投标单号 |
| 13 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 14 | fispuragent | fispuragent | bpchar | 1 |  | √ | '0' |  |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 16 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 17 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :重新审核 |
| 19 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | fistender | fistender | bpchar | 1 |  | √ | '0' |  |
| 22 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 25 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 26 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 27 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 28 | fdeadline | fdeadline | timestamp | 0 |  |  | null |  |
| 29 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 31 | fisnotice | fisnotice | bpchar | 1 |  | √ | '0' |  |
| 32 | fnumber | fnumber | int4 | 32 |  | √ | 0 |  |
| 33 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 34 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 35 | fisquote | fisquote | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_biddocbill_fprojectid |  | fprojectid |
| 2 | idx_src_biddocbill_fbilldate |  | fbilldate |
| 3 | idx_src_biddocbill_fparentid |  | fparentid |
| 4 | idx_src_biddocbill_fsupplierid |  | fsupplierid |
| 5 | pk_src_biddocbill |  | fid |
| 6 | idx_src_biddocbill_fbillno |  | fbillno |
