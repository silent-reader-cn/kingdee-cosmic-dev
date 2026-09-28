# 日常报销单冲销分录-er_dailyreimbursewfentry

## 日常报销单冲销分录-主表 t_er_writeoffdetail

- **表名称：** 日常报销单冲销分录-主表
- **表名：** t_er_writeoffdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | floanperson | floanperson | varchar | 200 |  | √ | ' ' |  |
| 3 | fstdentrycostcenterid | fstdentrycostcenterid | int8 | 64 |  | √ | 0 |  |
| 4 | floanbill | 单据编号 | int8 | 64 |  | √ | 0 | 单据编号 |
| 5 | floanbillnov1 | floanbillnov1 | varchar | 100 |  | √ | '0' |  |
| 6 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fcostdeptid | fcostdeptid | int8 | 64 |  | √ | 0 |  |
| 8 | fcurrloanamount | fcurrloanamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 10 | faccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 11 | fcurraccloanamount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额(本位币) |
| 12 | floanamount | floanamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | floanexchangerate | floanexchangerate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | floancurrency | floancurrency | int8 | 64 |  | √ | 0 |  |
| 15 | floanapplydatev1 | floanapplydatev1 | timestamp | 0 |  |  | null |  |
| 16 | fsourcesign | fsourcesign | bpchar | 1 |  | √ | '0' |  |
| 17 | fsourcebillid | fsourcebillid | varchar | 100 |  | √ | ' ' |  |
| 18 | fsrcbilltype | fsrcbilltype | varchar | 200 |  | √ | ' ' |  |
| 19 | fcostcompanyid | fcostcompanyid | int8 | 64 |  | √ | 0 |  |
| 20 | floandescriptionv1 | floandescriptionv1 | varchar | 1000 |  | √ | ' ' |  |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fquotetype | fquotetype | bpchar | 1 |  | √ | '0' |  |
| 23 | fsourceexpenseitemid | fsourceexpenseitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_writeoffdetail_pkey |  | fentryid |
| 2 | idx_er_writeoffdetail_fid |  | fid |
