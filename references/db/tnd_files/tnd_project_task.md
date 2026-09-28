# 我的任务-tnd_project_task

## 我的任务-主表 t_src_project

- **表名称：** 我的任务-主表
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
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
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
| 2 | pk_src_project |  | fid |
| 3 | idx_src_project_parentid |  | fparentid |
| 4 | idx_src_project_sourceclassid |  | fsourceclassid |
| 5 | idx_src_project_status |  | fopenstatus |
| 6 | idx_src_project_type |  | fsrctypeid |
