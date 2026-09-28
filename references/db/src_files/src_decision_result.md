# 定标会议决策-src_decision_result

## 定标决策附件-附件表 t_src_project_t_fj

- **表名称：** 定标决策附件-附件表
- **表名：** t_src_project_t_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_t_fj |  | fpkid |
| 2 | idx_src_project_t_fj_bid |  | fbasedataid |
| 3 | idx_src_project_t_fj_fid |  | fid |

---

## 定标会议决策-主表 t_src_project

- **表名称：** 定标会议决策-主表
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

## 定标会议决策-分表 t_src_project_t

- **表名称：** 定标会议决策-分表
- **表名：** t_src_project_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecisionsumid | fdecisionsumid | int8 | 64 |  | √ | 0 |  |
| 3 | fpurassessid | fpurassessid | int8 | 64 |  | √ | 0 |  |
| 4 | fistemppush | 临时下推 | bpchar | 1 |  | √ | '0' | 临时下推 |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fiscreatpur | fiscreatpur | bpchar | 1 |  | √ | '0' |  |
| 8 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fisneedinvite2 | fisneedinvite2 | bpchar | 1 |  | √ | ' ' |  |
| 12 | fiswinnotice | fiswinnotice | bpchar | 1 |  | √ | '0' |  |
| 13 | fpriceeffect | fpriceeffect | timestamp | 0 |  |  | null |  |
| 14 | fresultstatus | 决议状态 | bpchar | 1 |  | √ | ' ' | 决议状态,枚举: A :待评审 B :通过 C :不通过 D :有条件通过 |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fisdecisionresult | fisdecisionresult | bpchar | 1 |  | √ | '0' |  |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fisedited | fisedited | bpchar | 1 |  | √ | '0' |  |
| 20 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 22 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 23 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 24 | fpricebiztype | fpricebiztype | int8 | 64 |  | √ | 0 |  |
| 25 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fdecstatus | 关联决策会议单状态 | bpchar | 1 |  | √ | ' ' | 关联决策会议单状态,枚举: A :未关联 B :已上报 C :已关联 |
| 28 | ffluctuateamount | ffluctuateamount | varchar | 50 |  | √ | ' ' |  |
| 29 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fconclusion | 会议决策结论 | varchar | 1000 |  | √ | ' ' | 会议决策结论 |
| 33 | fdecisiontype | 议题类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 34 | fwintime | fwintime | timestamp | 0 |  |  | null |  |
| 35 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 36 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 37 | fdecidelink | 会议决策申请链接 | varchar | 100 |  | √ | ' ' | 会议决策申请链接 |
| 38 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 39 | fcomnum | fcomnum | int8 | 64 |  | √ | 0 |  |
| 40 | fchassistype | fchassistype | int8 | 64 |  | √ | 0 |  |
| 41 | fpurtype | fpurtype | varchar | 30 |  | √ | ' ' |  |
| 42 | fpurreport | fpurreport | varchar | 30 |  | √ | ' ' |  |
| 43 | fdecidenumber | 会议决策单号 | varchar | 50 |  | √ | ' ' | 会议决策单号 |
| 44 | ftempreason | 临时下推原因 | varchar | 255 |  | √ | ' ' | 临时下推原因 |
| 45 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | ' ' |  |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 47 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 48 | fapprovaltype | fapprovaltype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_t |  | fid |
| 2 | idx_src_project_t_fcreatorid |  | fcreatorid |
