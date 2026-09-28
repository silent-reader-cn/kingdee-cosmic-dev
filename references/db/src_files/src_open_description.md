# 开标说明-src_open_description

## 开标说明-主表 t_src_project

- **表名称：** 开标说明-主表
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
| 73 | fsourcetypeid | fsourcetypeid | int8 | 64 |  | √ | 0 |  |
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

## 开标说明-分表 t_src_project_a

- **表名称：** 开标说明-分表
- **表名：** t_src_project_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherruleassess | fotherruleassess | varchar | 255 |  |  | ' ' |  |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fnote | 开标备注 | varchar | 255 |  | √ | ' ' | 开标备注 |
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fisbidnotice | fisbidnotice | bpchar | 1 |  | √ | '0' |  |
| 8 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 9 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 10 | famountrange | famountrange | varchar | 50 |  | √ | ' ' |  |
| 11 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 12 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fsourcestateprint | fsourcestateprint | varchar | 100 |  | √ | ' ' |  |
| 14 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 15 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 16 | fprojectcreatorid | fprojectcreatorid | int8 | 64 |  | √ | 0 |  |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | ' ' |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 21 | fotherwinrule | fotherwinrule | varchar | 255 |  |  | ' ' |  |
| 22 | fdecisionname | fdecisionname | varchar | 100 |  | √ | ' ' |  |
| 23 | fispaper | fispaper | bpchar | 1 |  | √ | '0' |  |
| 24 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 25 | fissplitdoc | fissplitdoc | bpchar | 1 |  | √ | '0' |  |
| 26 | freasonremark_tag | freasonremark_tag | text | 0 |  |  | null |  |
| 27 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 28 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 29 | faftertalkrule | faftertalkrule | varchar | 255 |  |  | ' ' |  |
| 30 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | '0' |  |
| 31 | fsolereason | fsolereason | bpchar | 1 |  | √ | ' ' |  |
| 32 | forderrule | forderrule | varchar | 255 |  | √ | ' ' |  |
| 33 | freasonremark | freasonremark | varchar | 255 |  | √ | ' ' |  |
| 34 | fopentypep | fopentypep | varchar | 50 |  | √ | ' ' |  |
| 35 | fdecisionbillno | fdecisionbillno | varchar | 50 |  | √ | ' ' |  |
| 36 | fcontractcycle | fcontractcycle | varchar | 50 |  | √ | ' ' |  |
| 37 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 38 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 39 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 40 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 41 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 42 | fbidaddress | 开标地点 | varchar | 50 |  | √ | ' ' | 开标地点 |
| 43 | fsourcestate | fsourcestate | varchar | 30 |  | √ | ' ' |  |
| 44 | fsrcapplyid | fsrcapplyid | int8 | 64 |  | √ | 0 |  |
| 45 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 46 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 47 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 48 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 49 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 50 | fprojectcreatetime | fprojectcreatetime | timestamp | 0 |  |  | null |  |
| 51 | fismustapply | fismustapply | bpchar | 1 |  | √ | '0' |  |
| 52 | fdiscardrule | fdiscardrule | varchar | 255 |  |  | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_a |  | fid |
| 2 | idx_src_project_a_fcreatorid |  | fcreatorid |
| 3 | idx_src_project_a_fsrcapplyid |  | fsrcapplyid |
