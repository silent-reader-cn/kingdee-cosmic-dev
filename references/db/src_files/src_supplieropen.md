# 供应商开标情况F7-src_supplieropen

## 供应商开标情况F7-主表 t_src_invitesupplier

- **表名称：** 供应商开标情况F7-主表
- **表名：** t_src_invitesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID(招标项目ID) | int8 | 64 |  | √ | 0 | 单据ID(招标项目ID) |
| 2 | faptrank | 资审开标顺序 | int4 | 32 |  | √ | 0 | 资审开标顺序 |
| 3 | faddress | faddress | varchar | 100 |  | √ | ' ' |  |
| 4 | fisupload | fisupload | bpchar | 1 |  | √ | '0' |  |
| 5 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 6 | fisexemptapt | fisexemptapt | bpchar | 1 |  | √ | '0' |  |
| 7 | fisbidpush | 评标任务已下达 | bpchar | 1 |  | √ | '0' | 评标任务已下达 |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 10 | fbizopenuser | 商务表开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdocamount | fdocamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fisdownload | fisdownload | bpchar | 1 |  | √ | '0' |  |
| 14 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 15 | ftecrank | 技术开标顺序 | int4 | 32 |  | √ | 0 | 技术开标顺序 |
| 16 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 17 | fcount2 | fcount2 | int4 | 32 |  | √ | 0 |  |
| 18 | fisabandon | fisabandon | bpchar | 1 |  | √ | '0' |  |
| 19 | faptopenuser | 资审开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fisconfirm | fisconfirm | bpchar | 1 |  | √ | '0' |  |
| 21 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 22 | fabandonreason | fabandonreason | varchar | 255 |  | √ | ' ' |  |
| 23 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 24 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 25 | fisfeeagent | fisfeeagent | bpchar | 1 |  | √ | '0' |  |
| 26 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 27 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 28 | fsumscore | fsumscore | numeric | 19 | 4 | √ | 0 |  |
| 29 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 32 | fisaptopen | 资审已开标 | bpchar | 1 |  | √ | '0' | 资审已开标 |
| 33 | ftempsupplierid | ftempsupplierid | int8 | 64 |  | √ | 0 |  |
| 34 | fisaptpush2 | 资质后审已下达 | bpchar | 1 |  | √ | '0' | 资质后审已下达 |
| 35 | fassessorder | fassessorder | int4 | 32 |  | √ | 0 |  |
| 36 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 37 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fisquote | fisquote | bpchar | 1 |  | √ | '0' |  |
| 40 | frank | 开标顺序 | int4 | 32 |  | √ | 0 | 开标顺序 |
| 41 | frisknum | frisknum | int4 | 32 |  | √ | 0 |  |
| 42 | fisaptpush | 资质预审已下达 | bpchar | 1 |  | √ | '0' | 资质预审已下达 |
| 43 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 44 | fsocietycreditcode | fsocietycreditcode | varchar | 255 |  | √ | ' ' |  |
| 45 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 46 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 47 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 48 | fsource | fsource | bpchar | 1 |  | √ | ' ' |  |
| 49 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 50 | fbidderid | fbidderid | int8 | 64 |  | √ | 0 |  |
| 51 | fispayfee | fispayfee | bpchar | 1 |  | √ | '0' |  |
| 52 | fcurrentrank | fcurrentrank | int4 | 32 |  | √ | 0 |  |
| 53 | ffeeamount | ffeeamount | numeric | 23 | 10 | √ | 0 |  |
| 54 | ftecopenuser | 技术标开标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fpurlistnote | fpurlistnote | varchar | 50 |  | √ | ' ' |  |
| 56 | fcount | fcount | int4 | 32 |  | √ | 0 |  |
| 57 | fispuraptitude | fispuraptitude | bpchar | 1 |  | √ | '0' |  |
| 58 | fisexempt | fisexempt | bpchar | 1 |  | √ | '0' |  |
| 59 | fispuragent | fispuragent | bpchar | 1 |  | √ | '0' |  |
| 60 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 61 | fquotedate | fquotedate | timestamp | 0 |  |  | null |  |
| 62 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 63 | friskremark | friskremark | varchar | 510 |  | √ | ' ' |  |
| 64 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 65 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 66 | fisinvite | fisinvite | bpchar | 1 |  | √ | '0' |  |
| 67 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 68 | faptitudenote | faptitudenote | varchar | 255 |  | √ | ' ' |  |
| 69 | fbizrank | 商务开标顺序 | int4 | 32 |  | √ | 0 | 商务开标顺序 |
| 70 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 71 | fduty | fduty | varchar | 50 |  | √ | ' ' |  |
| 72 | fispaydocfee | fispaydocfee | bpchar | 1 |  | √ | '0' |  |
| 73 | faptopendate | 资审开标时间 | timestamp | 0 |  |  | null | 资审开标时间 |
| 74 | fisaptitudereply | fisaptitudereply | bpchar | 1 |  | √ | '0' |  |
| 75 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplier |  | fentryid |
| 2 | idx_src_invitesupplier_fpag |  | fpackageid |
| 3 | idx_src_invitesupplier_fsup |  | fsupplierid |
| 4 | idx_src_invitesupplier_fid |  | fid |
| 5 | idx_src_invitesupplier_fpid |  | fparentid |
