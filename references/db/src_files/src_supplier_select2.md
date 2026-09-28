# 供方正式入围-src_supplier_select2

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 供方正式入围-主表 t_src_project

- **表名称：** 供方正式入围-主表
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
| 47 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 48 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 49 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 50 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 51 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 52 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 53 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 54 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 55 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 56 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 57 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 58 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 59 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 60 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 61 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 62 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 63 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 64 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 65 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 66 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 67 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 68 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 69 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 70 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 71 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 72 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 73 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 74 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 75 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 76 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 77 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 78 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 79 | fratiotype | fratiotype | bpchar | 1 |  | √ | '1' |  |

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
| 4 | idx_src_project_type |  | fsrctypeid |
| 5 | idx_src_project_sourceclassid |  | fsourceclassid |
| 6 | idx_src_project_status |  | fopenstatus |

---

## 入围供应商分录-子表 t_src_invitesupplier

- **表名称：** 入围供应商分录-子表
- **表名：** t_src_invitesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 3 | fisupload | fisupload | bpchar | 1 |  | √ | '0' |  |
| 4 | fistecopen | fistecopen | bpchar | 1 |  | √ | '0' |  |
| 5 | fisbidpush | fisbidpush | bpchar | 1 |  | √ | '0' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 推荐原因说明 | varchar | 255 |  | √ | ' ' | 推荐原因说明 |
| 8 | fbizopenuser | fbizopenuser | int8 | 64 |  | √ | 0 |  |
| 9 | fdocamount | fdocamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 12 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 13 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 14 | fcount2 | fcount2 | int4 | 32 |  | √ | 0 |  |
| 15 | fisabandon | fisabandon | bpchar | 1 |  | √ | '0' |  |
| 16 | faptopenuser | faptopenuser | int8 | 64 |  | √ | 0 |  |
| 17 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 18 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 19 | fabandonreason | fabandonreason | varchar | 255 |  | √ | ' ' |  |
| 20 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 21 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 22 | fisfeeagent | 代理缴费 | bpchar | 1 |  | √ | '0' | 代理缴费 |
| 23 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 24 | ftecopendate | ftecopendate | timestamp | 0 |  |  | null |  |
| 25 | fsumscore | fsumscore | numeric | 19 | 4 | √ | 0 |  |
| 26 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 29 | fisaptopen | fisaptopen | bpchar | 1 |  | √ | '0' |  |
| 30 | fisaptpush2 | fisaptpush2 | bpchar | 1 |  | √ | '0' |  |
| 31 | fassessorder | fassessorder | int4 | 32 |  | √ | 0 |  |
| 32 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 33 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 36 | frank | frank | int4 | 32 |  | √ | 0 |  |
| 37 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 38 | fisaptpush | fisaptpush | bpchar | 1 |  | √ | '0' |  |
| 39 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 40 | fbizamount | fbizamount | numeric | 23 | 10 | √ | 0 |  |
| 41 | fentrystatus | fentrystatus | bpchar | 1 |  | √ | ' ' |  |
| 42 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 43 | fsource | fsource | bpchar | 1 |  | √ | ' ' |  |
| 44 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 45 | fbidderid | fbidderid | int8 | 64 |  | √ | 0 |  |
| 46 | fispayfee | 是否已缴纳 | bpchar | 1 |  | √ | '0' | 是否已缴纳 |
| 47 | fcurrentrank | fcurrentrank | int4 | 32 |  | √ | 0 |  |
| 48 | ffeeamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 49 | ftecopenuser | ftecopenuser | int8 | 64 |  | √ | 0 |  |
| 50 | fcount | fcount | int4 | 32 |  | √ | 0 |  |
| 51 | fisexempt | fisexempt | bpchar | 1 |  | √ | '0' |  |
| 52 | fispuragent | 代理投标/报价 | bpchar | 1 |  | √ | '0' | 代理投标/报价 |
| 53 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 54 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 55 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 56 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 57 | fbizopendate | fbizopendate | timestamp | 0 |  |  | null |  |
| 58 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 59 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 60 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 61 | fentrysupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 62 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 63 | fispaydocfee | fispaydocfee | bpchar | 1 |  | √ | '0' |  |
| 64 | faptopendate | faptopendate | timestamp | 0 |  |  | null |  |
| 65 | fisbizopen | fisbizopen | bpchar | 1 |  | √ | '0' |  |

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

---

## 报名供应商分录-子表 t_src_invitesupplier_temp

- **表名称：** 报名供应商分录-子表
- **表名：** t_src_invitesupplier_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismanualselect | fismanualselect | bpchar | 1 |  | √ | '0' |  |
| 3 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 4 | fisbidpush | fisbidpush | bpchar | 1 |  | √ | '0' |  |
| 5 | fisselect | 是否推荐 | bpchar | 1 |  | √ | '0' | 是否推荐 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 推荐原因说明 | varchar | 255 |  | √ | ' ' | 推荐原因说明 |
| 8 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 9 | fisdiscard | fisdiscard | bpchar | 1 |  | √ | '0' |  |
| 10 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 11 | fisabandon | fisabandon | bpchar | 1 |  | √ | '0' |  |
| 12 | fsupname | fsupname | varchar | 255 |  | √ | ' ' |  |
| 13 | fisconfirm | fisconfirm | bpchar | 1 |  | √ | '0' |  |
| 14 | fabandonreason | fabandonreason | varchar | 255 |  | √ | ' ' |  |
| 15 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 16 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 17 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 18 | fisfeeagent | 代理缴费 | bpchar | 1 |  | √ | '0' | 代理缴费 |
| 19 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 20 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 21 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 23 | fisaptpush2 | fisaptpush2 | bpchar | 1 |  | √ | '0' |  |
| 24 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 25 | fpublishdate | 发标日期 | timestamp | 0 |  |  | null | 发标日期 |
| 26 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fisquote | 是否报价 | bpchar | 1 |  | √ | '0' | 是否报价 |
| 29 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 30 | fisaptpush | fisaptpush | bpchar | 1 |  | √ | '0' |  |
| 31 | fsocietycreditcode | fsocietycreditcode | varchar | 255 |  | √ | ' ' |  |
| 32 | fk_sf_textfield | fk_sf_textfield | varchar | 50 |  | √ | ' ' |  |
| 33 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 34 | fsource | fsource | bpchar | 1 |  | √ | ' ' |  |
| 35 | fisaptitude | 资审结果 | bpchar | 1 |  | √ | '0' | 资审结果,枚举: 0 :未资审 1 :资审合格 2 :资审不合格 |
| 36 | fispayfee | fispayfee | bpchar | 1 |  | √ | '0' |  |
| 37 | fcurrentrank | 初选排名 | int4 | 32 |  | √ | 0 | 初选排名 |
| 38 | ffeeamount | ffeeamount | numeric | 23 | 10 | √ | 0 |  |
| 39 | fpublisherid | 发标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 41 | fispuragent | 代理投标/报价 | bpchar | 1 |  | √ | '0' | 代理投标/报价 |
| 42 | fpublishstatus | 发标状态 | bpchar | 1 |  | √ | ' ' | 发标状态,枚举: A :待发标 B :已发标 |
| 43 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 44 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 45 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 46 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 47 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 48 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 49 | fisvalid | 初选合格否 | bpchar | 1 |  | √ | '0' | 初选合格否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplier_temp |  | fentryid |
| 2 | idx_src_invitesup_temp_fpid |  | fparentid |
| 3 | idx_src_invitesup_temp_fid |  | fid |
| 4 | idx_src_invitesup_temp_fpag |  | fpackageid |
| 5 | idx_src_invitesup_temp_fsup |  | fsupplierid |
