# 回标情况-src_tenderinfo

## 回标情况-主表 t_src_project

- **表名称：** 回标情况-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 41 | ftieredtype | ftieredtype | bpchar | 1 |  | √ | '1' |  |
| 42 | fdecidedate | fdecidedate | timestamp | 0 |  |  | null |  |
| 43 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 44 | fwinruleid | fwinruleid | int8 | 64 |  | √ | 0 |  |
| 45 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 46 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsystype | fsystype | bpchar | 1 |  | √ | '1' |  |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 54 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 55 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 58 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 59 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 60 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 61 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
| 75 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 80 | fratiotype | fratiotype | bpchar | 1 |  | √ | '1' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_sourceid |  | fsourceid |
| 2 | idx_src_project_parentid |  | fparentid |
| 3 | pk_src_project |  | fid |
| 4 | idx_src_project_sourceclassid |  | fsourceclassid |
| 5 | idx_src_project_status |  | fopenstatus |
| 6 | idx_src_project_type |  | fsrctypeid |

---

## 回标情况分录-子表 t_src_invitesupplier

- **表名称：** 回标情况分录-子表
- **表名：** t_src_invitesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faptrank | faptrank | int4 | 32 |  | √ | 0 |  |
| 3 | faddress | faddress | varchar | 100 |  | √ | ' ' |  |
| 4 | fisupload | fisupload | bpchar | 1 |  | √ | '0' |  |
| 5 | fistecopen | fistecopen | bpchar | 1 |  | √ | '0' |  |
| 6 | fisexemptapt | fisexemptapt | bpchar | 1 |  | √ | '0' |  |
| 7 | fisbidpush | fisbidpush | bpchar | 1 |  | √ | '0' |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fbizopenuser | fbizopenuser | int8 | 64 |  | √ | 0 |  |
| 11 | fdocamount | fdocamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fisdownload | fisdownload | bpchar | 1 |  | √ | '0' |  |
| 14 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 15 | ftecrank | ftecrank | int4 | 32 |  | √ | 0 |  |
| 16 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 17 | fcount2 | fcount2 | int4 | 32 |  | √ | 0 |  |
| 18 | fisabandon | 是否弃标 | bpchar | 1 |  | √ | '0' | 是否弃标 |
| 19 | faptopenuser | faptopenuser | int8 | 64 |  | √ | 0 |  |
| 20 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 21 | fisnegotiate | 是否议标报价 | bpchar | 1 |  | √ | '0' | 是否议标报价 |
| 22 | fabandonreason | 弃标原因 | varchar | 255 |  | √ | ' ' | 弃标原因 |
| 23 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 24 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 25 | fisfeeagent | fisfeeagent | bpchar | 1 |  | √ | '0' |  |
| 26 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 27 | ftecopendate | ftecopendate | timestamp | 0 |  |  | null |  |
| 28 | fsumscore | fsumscore | numeric | 19 | 4 | √ | 0 |  |
| 29 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 31 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 32 | fisaptopen | fisaptopen | bpchar | 1 |  | √ | '0' |  |
| 33 | ftempsupplierid | ftempsupplierid | int8 | 64 |  | √ | 0 |  |
| 34 | fisaptpush2 | fisaptpush2 | bpchar | 1 |  | √ | '0' |  |
| 35 | fassessorder | fassessorder | int4 | 32 |  | √ | 0 |  |
| 36 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 37 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 40 | frank | frank | int4 | 32 |  | √ | 0 |  |
| 41 | frisknum | frisknum | int4 | 32 |  | √ | 0 |  |
| 42 | fisaptpush | fisaptpush | bpchar | 1 |  | √ | '0' |  |
| 43 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 44 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 45 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 46 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :待下达 B :已下达 C :部分评标 D :已评标 |
| 47 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 48 | fsource | fsource | bpchar | 1 |  | √ | ' ' |  |
| 49 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 50 | fbidderid | fbidderid | int8 | 64 |  | √ | 0 |  |
| 51 | fispayfee | 是否已缴纳 | bpchar | 1 |  | √ | '0' | 是否已缴纳 |
| 52 | fcurrentrank | fcurrentrank | int4 | 32 |  | √ | 0 |  |
| 53 | ffeeamount | 投标保证金 | numeric | 23 | 10 | √ | 0 | 投标保证金 |
| 54 | ftecopenuser | ftecopenuser | int8 | 64 |  | √ | 0 |  |
| 55 | fpurlistnote | fpurlistnote | varchar | 50 |  | √ | ' ' |  |
| 56 | fcount | fcount | int4 | 32 |  | √ | 0 |  |
| 57 | fispuraptitude | fispuraptitude | bpchar | 1 |  | √ | '0' |  |
| 58 | fisexempt | fisexempt | bpchar | 1 |  | √ | '0' |  |
| 59 | fispuragent | fispuragent | bpchar | 1 |  | √ | '0' |  |
| 60 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 61 | fquotedate | 投标/报价时间 | timestamp | 0 |  |  | null | 投标/报价时间 |
| 62 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 63 | friskremark | friskremark | varchar | 510 |  | √ | ' ' |  |
| 64 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 65 | fbizopendate | fbizopendate | timestamp | 0 |  |  | null |  |
| 66 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 67 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 68 | faptitudenote | faptitudenote | varchar | 255 |  | √ | ' ' |  |
| 69 | fbizrank | fbizrank | int4 | 32 |  | √ | 0 |  |
| 70 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 71 | fduty | fduty | varchar | 50 |  | √ | ' ' |  |
| 72 | fispaydocfee | fispaydocfee | bpchar | 1 |  | √ | '0' |  |
| 73 | faptopendate | faptopendate | timestamp | 0 |  |  | null |  |
| 74 | fisaptitudereply | fisaptitudereply | bpchar | 1 |  | √ | '0' |  |
| 75 | fisbizopen | fisbizopen | bpchar | 1 |  | √ | '0' |  |

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
