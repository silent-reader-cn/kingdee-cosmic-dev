# 标段名称-pds_packagef7

## 标段名称-主表 t_src_projectpackage

- **表名称：** 标段名称-主表
- **表名：** t_src_projectpackage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 2 | fisaptassess2 | fisaptassess2 | bpchar | 1 |  | √ | '0' |  |
| 3 | fistecopen | fistecopen | bpchar | 1 |  | √ | '0' |  |
| 4 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fbizopenuser | fbizopenuser | int8 | 64 |  | √ | 0 |  |
| 7 | fisbizassess | fisbizassess | bpchar | 1 |  | √ | '0' |  |
| 8 | fbizassessdate | fbizassessdate | timestamp | 0 |  |  | null |  |
| 9 | fisaptassess | fisaptassess | bpchar | 1 |  | √ | '0' |  |
| 10 | ftecopenuser | ftecopenuser | int8 | 64 |  | √ | 0 |  |
| 11 | ffeeamount | ffeeamount | numeric | 19 | 6 | √ | 0 |  |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 pds_packagef7 |
| 13 | fturns | fturns | varchar | 2 |  | √ | ' ' |  |
| 14 | faptopenuser | faptopenuser | int8 | 64 |  | √ | 0 |  |
| 15 | faptassessdate2 | faptassessdate2 | timestamp | 0 |  |  | null |  |
| 16 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 17 | fistecassess | fistecassess | bpchar | 1 |  | √ | '0' |  |
| 18 | fnegopendate | fnegopendate | timestamp | 0 |  |  | null |  |
| 19 | fbizopendate | fbizopendate | timestamp | 0 |  |  | null |  |
| 20 | ftecopendate | ftecopendate | timestamp | 0 |  |  | null |  |
| 21 | fisnegopen | fisnegopen | bpchar | 1 |  | √ | '0' |  |
| 22 | ftecassessdate | ftecassessdate | timestamp | 0 |  |  | null |  |
| 23 | faptopendate | faptopendate | timestamp | 0 |  |  | null |  |
| 24 | fisaptopen | fisaptopen | bpchar | 1 |  | √ | '0' |  |
| 25 | fpackdocamount | fpackdocamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fnegopenuser | fnegopenuser | int8 | 64 |  | √ | 0 |  |
| 27 | fisbizopen | fisbizopen | bpchar | 1 |  | √ | '0' |  |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fpackage | 标段名称 | varchar | 50 |  | √ | ' ' | 标段名称 |
| 30 | faptassessdate | faptassessdate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_projectpackage |  | fentryid |
| 2 | idx_src_projectpackage_pid |  | fpackageid |
| 3 | idx_src_projectpackage_fid |  | fid |
