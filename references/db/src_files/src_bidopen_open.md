# 开标情况-src_bidopen_open

## 开标情况-主表 t_src_project

- **表名称：** 开标情况-主表
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
| 24 | fbidcount | 投标/报价 次数 | int4 | 32 |  | √ | 0 | 投标/报价 次数 |
| 25 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | fnodename | varchar | 50 |  | √ | ' ' |  |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | 投标截止时间 | timestamp | 0 |  |  | null | 投标截止时间 |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | 投标截止时间到达时自动开标 | bpchar | 1 |  | √ | '0' | 投标截止时间到达时自动开标 |
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
| 50 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 9 :报价即开标(非密封报价) |
| 51 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 52 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 53 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 54 | fismultipackage | 是否包含多标段 | bpchar | 1 |  | √ | '0' | 是否包含多标段 |
| 55 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 56 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 57 | fopenstatus | 开标状态 | bpchar | 1 |  | √ | '1' | 开标状态,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 58 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 |
| 59 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 60 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 61 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 62 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 63 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 64 | fisbypackage | 是否按标段开标 | bpchar | 1 |  | √ | '0' | 是否按标段开标 |
| 65 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 66 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 67 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 68 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 69 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 70 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 71 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 72 | fisbypackage_apt | 是否按标段开资审标 | bpchar | 1 |  | √ | '0' | 是否按标段开资审标 |
| 73 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 74 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 75 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 76 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
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

## 开标情况分录-子表 t_src_projectpackage

- **表名称：** 开标情况分录-子表
- **表名：** t_src_projectpackage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisaptassess2 | 资审后审已评标 | bpchar | 1 |  | √ | '0' | 资审后审已评标 |
| 3 | fistecopen | 技术标已开标 | bpchar | 1 |  | √ | '0' | 技术标已开标 |
| 4 | fpackfeeitemid | fpackfeeitemid | int8 | 64 |  | √ | 0 |  |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbizopenuser | 商务开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fisbizassess | 商务标已评标 | bpchar | 1 |  | √ | '0' | 商务标已评标 |
| 8 | fbizassessdate | 商务标评标时间 | timestamp | 0 |  |  | null | 商务标评标时间 |
| 9 | fisaptassess | 资质预审已评标 | bpchar | 1 |  | √ | '0' | 资质预审已评标 |
| 10 | ftecopenuser | 技术开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ffeeamount | ffeeamount | numeric | 19 | 6 | √ | 0 |  |
| 12 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 13 | fturns | 当前轮次 | varchar | 2 |  | √ | ' ' | 当前轮次,枚举: 1 :第一轮 2 :第二轮 3 :第三轮 4 :第四轮 5 :第五轮 |
| 14 | faptopenuser | 资质预审开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | faptassessdate2 | 资审后审评标时间 | timestamp | 0 |  |  | null | 资审后审评标时间 |
| 16 | fisnegotiate | 是否议标 | bpchar | 1 |  | √ | '0' | 是否议标 |
| 17 | fistecassess | 技术标已评标 | bpchar | 1 |  | √ | '0' | 技术标已评标 |
| 18 | fnegopendate | 议标开标时间 | timestamp | 0 |  |  | null | 议标开标时间 |
| 19 | fbizopendate | 商务标开标时间 | timestamp | 0 |  |  | null | 商务标开标时间 |
| 20 | ftecopendate | 技术标开标时间 | timestamp | 0 |  |  | null | 技术标开标时间 |
| 21 | fisnegopen | 议标已开标 | bpchar | 1 |  | √ | '0' | 议标已开标 |
| 22 | ftecassessdate | 技术标评标时间 | timestamp | 0 |  |  | null | 技术标评标时间 |
| 23 | faptopendate | 资质预审开标时间 | timestamp | 0 |  |  | null | 资质预审开标时间 |
| 24 | fisaptopen | 资质预审已开标 | bpchar | 1 |  | √ | '0' | 资质预审已开标 |
| 25 | fpackdocamount | fpackdocamount | numeric | 23 | 10 | √ | 0 |  |
| 26 | fnegopenuser | 议标开标人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
