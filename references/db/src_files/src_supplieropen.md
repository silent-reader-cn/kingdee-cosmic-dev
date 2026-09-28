# 供应商开标情况F7-src_supplieropen

## 供应商开标情况F7-主表 t_src_invitesupplier

- **表名称：** 供应商开标情况F7-主表
- **表名：** t_src_invitesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID(招标项目ID) | int8 | 64 |  | √ | 0 | 单据ID(招标项目ID) |
| 2 | faddress | faddress | varchar | 100 |  | √ | ' ' |  |
| 3 | fisupload | fisupload | bpchar | 1 |  | √ | '0' |  |
| 4 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 5 | fisbidpush | 评标任务已下达 | bpchar | 1 |  | √ | '0' | 评标任务已下达 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 8 | fbizopenuser | 商务表开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdocamount | fdocamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fisdownload | fisdownload | bpchar | 1 |  | √ | '0' |  |
| 12 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 13 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 14 | fcount2 | fcount2 | int4 | 32 |  | √ | 0 |  |
| 15 | fisabandon | fisabandon | bpchar | 1 |  | √ | '0' |  |
| 16 | faptopenuser | 资审开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fisconfirm | fisconfirm | bpchar | 1 |  | √ | '0' |  |
| 18 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 19 | fabandonreason | fabandonreason | varchar | 255 |  | √ | ' ' |  |
| 20 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 21 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 22 | fisfeeagent | fisfeeagent | bpchar | 1 |  | √ | '0' |  |
| 23 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 24 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 25 | fsumscore | fsumscore | numeric | 19 | 4 | √ | 0 |  |
| 26 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fisaptopen | 资审已开标 | bpchar | 1 |  | √ | '0' | 资审已开标 |
| 30 | fisaptpush2 | 资质后审已下达 | bpchar | 1 |  | √ | '0' | 资质后审已下达 |
| 31 | fassessorder | fassessorder | int4 | 32 |  | √ | 0 |  |
| 32 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 33 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fisquote | fisquote | bpchar | 1 |  | √ | '0' |  |
| 36 | frank | 开标顺序 | int4 | 32 |  | √ | 0 | 开标顺序 |
| 37 | frisknum | frisknum | int4 | 32 |  | √ | 0 |  |
| 38 | fisaptpush | 资质预审已下达 | bpchar | 1 |  | √ | '0' | 资质预审已下达 |
| 39 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 40 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 41 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 42 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 43 | fsource | fsource | bpchar | 1 |  | √ | ' ' |  |
| 44 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 45 | fbidderid | fbidderid | int8 | 64 |  | √ | 0 |  |
| 46 | fispayfee | fispayfee | bpchar | 1 |  | √ | '0' |  |
| 47 | fcurrentrank | fcurrentrank | int4 | 32 |  | √ | 0 |  |
| 48 | ffeeamount | ffeeamount | numeric | 23 | 10 | √ | 0 |  |
| 49 | ftecopenuser | 技术标开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fcount | fcount | int4 | 32 |  | √ | 0 |  |
| 51 | fisexempt | fisexempt | bpchar | 1 |  | √ | '0' |  |
| 52 | fispuragent | fispuragent | bpchar | 1 |  | √ | '0' |  |
| 53 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 54 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 55 | friskremark | friskremark | varchar | 510 |  | √ | ' ' |  |
| 56 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 57 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 58 | fisinvite | fisinvite | bpchar | 1 |  | √ | '0' |  |
| 59 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 60 | faptitudenote | faptitudenote | varchar | 255 |  | √ | ' ' |  |
| 61 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 62 | fduty | fduty | varchar | 50 |  | √ | ' ' |  |
| 63 | fispaydocfee | fispaydocfee | bpchar | 1 |  | √ | '0' |  |
| 64 | faptopendate | 资审开标时间 | timestamp | 0 |  |  | null | 资审开标时间 |
| 65 | fisbizopen | 商务标已开标 | bpchar | 1 |  | √ | '0' | 商务标已开标 |

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
