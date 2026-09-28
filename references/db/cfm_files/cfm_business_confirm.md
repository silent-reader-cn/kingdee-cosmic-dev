# 业务确认-cfm_business_confirm

## 业务确认-主表 t_cfm_loancontractbill

- **表名称：** 业务确认-主表
- **表名：** t_cfm_loancontractbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnotdrawamount | fnotdrawamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 3 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 4 | fexchangerate | fexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | floanuseid | floanuseid | int8 | 64 |  | √ | 0 |  |
| 6 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 7 | ffloatingratio | ffloatingratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fisextend | fisextend | bpchar | 1 |  | √ | '0' |  |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fclientorgid | fclientorgid | int8 | 64 |  | √ | 0 |  |
| 11 | fotherexplain | fotherexplain | varchar | 255 |  | √ | ' ' |  |
| 12 | ffinproductid | ffinproductid | int8 | 64 |  | √ | 0 |  |
| 13 | flendernature | flendernature | varchar | 30 |  | √ | ' ' |  |
| 14 | fconversiondays | fconversiondays | varchar | 30 |  | √ | ' ' |  |
| 15 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcontractstatus | fcontractstatus | varchar | 30 |  | √ | ' ' |  |
| 18 | flimitclauseexplain | flimitclauseexplain | varchar | 255 |  | √ | ' ' |  |
| 19 | fcontractname | fcontractname | varchar | 255 |  | √ | ' ' |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | frepaymentway | frepaymentway | varchar | 30 |  | √ | ' ' |  |
| 23 | fextendstatus | fextendstatus | varchar | 30 |  | √ | ' ' |  |
| 24 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 25 | fnotpayinterestamount | fnotpayinterestamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 26 | finitid | finitid | int8 | 64 |  | √ | 0 |  |
| 27 | fstageplanid | fstageplanid | int8 | 64 |  | √ | 0 |  |
| 28 | fdrawway | fdrawway | varchar | 30 |  | √ | ' ' |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | faccountbankid | faccountbankid | int8 | 64 |  | √ | 0 |  |
| 31 | flocamt | flocamt | numeric | 19 | 6 | √ | 0.000000 |  |
| 32 | fcompanyid | 借款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | ffinorginfoid | ffinorginfoid | int8 | 64 |  | √ | 0 |  |
| 34 | fislimitclause | fislimitclause | bpchar | 1 |  | √ | '0' |  |
| 35 | finteresttype | finteresttype | varchar | 30 |  | √ | ' ' |  |
| 36 | fisclientloan | fisclientloan | bpchar | 1 |  | √ | '0' |  |
| 37 | fnotrepayamount | fnotrepayamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 38 | famount | famount | numeric | 19 | 6 | √ | 0.000000 |  |
| 39 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 40 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 41 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 42 | fpayinterestamount | fpayinterestamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 43 | fdrawamount | fdrawamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fguarantee | fguarantee | varchar | 300 |  |  | ' ' |  |
| 47 | fcontractno | fcontractno | varchar | 80 |  | √ | ' ' |  |
| 48 | floanorgid | floanorgid | int8 | 64 |  | √ | 0 |  |
| 49 | frepayamount | frepayamount | numeric | 19 | 6 | √ | 0.000000 |  |
| 50 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 51 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 52 | finterestrate | finterestrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 53 | finterestsettledplanid | finterestsettledplanid | int8 | 64 |  | √ | 0 |  |
| 54 | fcreditlimitid | fcreditlimitid | int8 | 64 |  | √ | 0 |  |
| 55 | fisoverdue | fisoverdue | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_loancontractbill_pkey |  | fid |
| 2 | idx_t_cfm_loancontractbill_bns |  | fbillno,fbillstatus |
