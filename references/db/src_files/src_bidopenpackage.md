# 开标情况F7-src_bidopenpackage

## 开标情况F7-主表 t_src_projectpackage

- **表名称：** 开标情况F7-主表
- **表名：** t_src_projectpackage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID(招标项目ID) | int8 | 64 |  | √ | 0 | 单据ID(招标项目ID) |
| 2 | fisaptassess2 | 资质后审已评标 | bpchar | 1 |  | √ | '0' | 资质后审已评标 |
| 3 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 4 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | fbizopenuser | 商务标开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fisbizassess | 商务标已评标 | bpchar | 1 |  | √ | '0' | 商务标已评标 |
| 8 | fbizassessdate | 商务标评标时间 | timestamp | 0 |  |  | null | 商务标评标时间 |
| 9 | fisaptassess | 资质预审已评标 | bpchar | 1 |  | √ | '0' | 资质预审已评标 |
| 10 | ftecopenuser | 技术标开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ffeeamount | ffeeamount | numeric | 19 | 6 | √ | 0 |  |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 13 | fturns | 当前轮次 | varchar | 2 |  | √ | ' ' | 当前轮次 |
| 14 | faptopenuser | 资审开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | faptassessdate2 | 资质后审评标时间 | timestamp | 0 |  |  | null | 资质后审评标时间 |
| 16 | fisnegotiate | 是否议标 | bpchar | 1 |  | √ | '0' | 是否议标 |
| 17 | fistecassess | 技术标已评标 | bpchar | 1 |  | √ | '0' | 技术标已评标 |
| 18 | fnegopendate | 议标开标时间 | timestamp | 0 |  |  | null | 议标开标时间 |
| 19 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 20 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 21 | fisnegopen | 议标已开标 | bpchar | 1 |  | √ | '0' | 议标已开标 |
| 22 | ftecassessdate | 技术标评标时间 | timestamp | 0 |  |  | null | 技术标评标时间 |
| 23 | faptopendate | 资审开标时间 | timestamp | 0 |  |  | null | 资审开标时间 |
| 24 | fisaptopen | 资审已开标 | bpchar | 1 |  | √ | '0' | 资审已开标 |
| 25 | fpackdocamount | fpackdocamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fnegopenuser | 议标开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fpackage | fpackage | varchar | 50 |  | √ | ' ' |  |
| 30 | faptassessdate | 资质预审评标时间 | timestamp | 0 |  |  | null | 资质预审评标时间 |

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
