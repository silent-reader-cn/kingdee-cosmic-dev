# 评标设置查询-src_bidopenconfigquery

## 评标设置分录-子表 t_src_assessconfig

- **表名称：** 评标设置分录-子表
- **表名：** t_src_assessconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdateto | 评标结束时间 | timestamp | 0 |  |  | null | 评标结束时间 |
| 4 | fqfilter | fqfilter | varchar | 255 |  | √ | ' ' |  |
| 5 | fproschemeid | fproschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :待下达 B :已下达 C :部分评标 D :已评标 E :已废标 |
| 7 | fschemeid | 评标方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fexpertcount | 评委最低人数 | int4 | 32 |  | √ | 0 | 评委最低人数 |
| 11 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 12 | fqfilter_tag | fqfilter_tag | text | 0 |  |  | null |  |
| 13 | fweight | 类型权重(%) | numeric | 19 | 6 | √ | 0 | 类型权重(%) |
| 14 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 15 | fdatefrom | 评标开始时间 | timestamp | 0 |  |  | null | 评标开始时间 |
| 16 | ftplname | 评标方案名称 | varchar | 100 |  | √ | ' ' | 评标方案名称 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_assessconfig_fid |  | fid |
| 2 | idx_src_assessconfig_fpack |  | fpackageid |
| 3 | pk_src_assessconfig |  | fentryid |

---

## 评标方案(线下)-附件表 t_src_assessconfig_fj

- **表名称：** 评标方案(线下)-附件表
- **表名：** t_src_assessconfig_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_assessconfig_fj |  | fpkid |
| 2 | idx_src_assessconfig_bid |  | fbasedataid |
| 3 | idx_src_assessconfig_fj |  | fentryid |

---

## 评标设置查询-主表 t_src_project

- **表名称：** 评标设置查询-主表
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
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | 评标方式 | bpchar | 1 |  | √ | ' ' | 评标方式,枚举: 1 :线上评标 2 :线下评标 |
| 14 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 15 | fisbyproject | 按项目设置评标方案 | bpchar | 1 |  | √ | '0' | 按项目设置评标方案 |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 19 | fratio_oth | 商务综合占比(%) | numeric | 23 | 10 | √ | 0 | 商务综合占比(%) |
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
| 30 | fscoremethod | 评分方法 | bpchar | 1 |  | √ | ' ' | 评分方法,枚举: 1 :百分制(每个指标按百分制评分，方案=100分) 2 :实际值(每个指标按实际值评分，方案=100分) 3 :最终值(每个指标按最终值评分，方案<100分) |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | 综合评标占比(%) | numeric | 23 | 10 | √ | 0 | 综合评标占比(%) |
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
| 50 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 9 :报价即开标(非密封报价) |
| 51 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 52 | fpurgroupid | fpurgroupid | int8 | 64 |  | √ | 0 |  |
| 53 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 54 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 55 | fishidesupplier | 评标时隐藏供应商名称(盲评) | bpchar | 1 |  | √ | '0' | 评标时隐藏供应商名称(盲评) |
| 56 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 57 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 58 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 59 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 60 | fbidname | fbidname | varchar | 300 |  | √ | ' ' |  |
| 61 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 62 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 63 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 64 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 65 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 66 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 67 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 68 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 69 | fratio_biz | 商务标占比(%) | numeric | 23 | 10 | √ | 0 | 商务标占比(%) |
| 70 | fratio_tec | 技术标占比(%) | numeric | 23 | 10 | √ | 0 | 技术标占比(%) |
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

## 评委-多选基础资料表 t_src_assessscorer

- **表名称：** 评委-多选基础资料表
- **表名：** t_src_assessscorer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_assessscorer_fbid |  | fbasedataid |
| 2 | pk_src_assessscorer |  | fpkid |
| 3 | idx_src_assessscorer_fentryid |  | fentryid |

---

## 评标设置查询-分表 t_src_project_q

- **表名称：** 评标设置查询-分表
- **表名：** t_src_project_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispkgscheme | fispkgscheme | bpchar | 1 |  | √ | '0' |  |
| 3 | fismanualscore | 线下评商务分后，手工录入系统 | bpchar | 1 |  | √ | '0' | 线下评商务分后，手工录入系统 |
| 4 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fnegschemeid | fnegschemeid | int8 | 64 |  | √ | 0 |  |
| 11 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 12 | fremark | fremark | varchar | 510 |  | √ | ' ' |  |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 15 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 16 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 18 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 19 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 22 | ftendency | ftendency | varchar | 50 |  | √ | ' ' |  |
| 23 | fbasescore | 基准商务得分 | numeric | 23 | 10 | √ | 0 | 基准商务得分 |
| 24 | fminscore | 最低商务得分 | numeric | 23 | 10 | √ | 0 | 最低商务得分 |
| 25 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 26 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 27 | ftopsupplier | ftopsupplier | int8 | 64 |  | √ | 1 |  |
| 28 | fnegotiaterule | fnegotiaterule | bpchar | 1 |  | √ | ' ' |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_q_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_q |  | fid |

---

## 评标设置查询-分表 t_src_project_o

- **表名称：** 评标设置查询-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | fbidstatus | bpchar | 1 |  | √ | ' ' |  |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fcashdeposit | fcashdeposit | numeric | 23 | 10 | √ | 0 |  |
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fplanopendate | fplanopendate | timestamp | 0 |  |  | null |  |
| 9 | faddtime | faddtime | int8 | 64 |  | √ | 0 |  |
| 10 | fbidtime | fbidtime | int8 | 64 |  | √ | 0 |  |
| 11 | flasttime | flasttime | int8 | 64 |  | √ | 0 |  |
| 12 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 13 | fviepattern | fviepattern | bpchar | 1 |  | √ | ' ' |  |
| 14 | fresultdate | fresultdate | timestamp | 0 |  |  | null |  |
| 15 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 17 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 18 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 19 | faddtimecount | faddtimecount | int4 | 32 |  | √ | 0 |  |
| 20 | fbidcount | fbidcount | int8 | 64 |  | √ | 0 |  |
| 21 | fbidrestoftime | fbidrestoftime | int8 | 64 |  | √ | 0 |  |
| 22 | ftendency | ftendency | bpchar | 1 |  | √ | ' ' |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 25 | fisregioncontrol | fisregioncontrol | bpchar | 1 |  | √ | ' ' |  |
| 26 | freducetype | freducetype | bpchar | 1 |  | √ | ' ' |  |
| 27 | flastquotedate | flastquotedate | timestamp | 0 |  |  | null |  |
| 28 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 29 | fisnewprice | fisnewprice | bpchar | 1 |  | √ | '0' |  |
| 30 | fenrolldate | fenrolldate | timestamp | 0 |  |  | null |  |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fisbizscore | 评委通过评标助手评商务分(线上评分) | bpchar | 1 |  | √ | '0' | 评委通过评标助手评商务分(线上评分) |
| 34 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 35 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 36 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 37 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 38 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 39 | fpauseamt | fpauseamt | numeric | 23 | 10 | √ | 0 |  |
| 40 | freducepct | freducepct | numeric | 23 | 10 | √ | 0 |  |
| 41 | fopen4 | fopen4 | bpchar | 1 |  | √ | ' ' |  |
| 42 | fopen2 | fopen2 | bpchar | 1 |  | √ | ' ' |  |
| 43 | fpausetime | fpausetime | timestamp | 0 |  |  | null |  |
| 44 | fsubmittype | fsubmittype | bpchar | 1 |  | √ | ' ' |  |
| 45 | fopen3 | fopen3 | bpchar | 1 |  | √ | ' ' |  |
| 46 | fautoconfirm | fautoconfirm | bpchar | 1 |  | √ | ' ' |  |
| 47 | fopen1 | fopen1 | bpchar | 1 |  | √ | ' ' |  |
| 48 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 49 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 50 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 51 | fvie_purlist | fvie_purlist | bpchar | 1 |  | √ | ' ' |  |
| 52 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 53 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 54 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 55 | fminamount | fminamount | numeric | 23 | 10 | √ | 0 |  |
| 56 | faddtimenum | faddtimenum | int4 | 32 |  | √ | 0 |  |
| 57 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 58 | fvietype | fvietype | bpchar | 1 |  | √ | ' ' |  |
| 59 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 60 | fdelaytime | fdelaytime | int8 | 64 |  | √ | 0 |  |
| 61 | fbidnumber | fbidnumber | int8 | 64 |  | √ | 0 |  |
| 62 | fopinion | fopinion | varchar | 255 |  | √ | ' ' |  |
| 63 | fpausestarttime | fpausestarttime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_o_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_o |  | fid |
