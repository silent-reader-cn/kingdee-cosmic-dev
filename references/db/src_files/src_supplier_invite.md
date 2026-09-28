# 选择供应商组件-src_supplier_invite

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
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

## 选择关联标的-多选基础资料表 t_src_invitesupplier_item

- **表名称：** 选择关联标的-多选基础资料表
- **表名：** t_src_invitesupplier_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_invitesup_item_bid |  | fbasedataid |
| 2 | idx_src_invitesup_item_eid |  | fentryid |
| 3 | pk_src_invitesupplier_item |  | fpkid |

---

## 可供标的范围-多选基础资料表 t_src_invitesupplierscope

- **表名称：** 可供标的范围-多选基础资料表
- **表名：** t_src_invitesupplierscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购清单F7 src_purlistf7 |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_invitesupplierscope |  | fpkid |
| 2 | idx_src_invitesupscope_bid |  | fbasedataid |
| 3 | idx_src_invitesupscope_eid |  | fentryid |

---

## 选择供应商组件-主表 t_src_project

- **表名称：** 选择供应商组件-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 25 | fwinerqty | 中标供应商数量 | int8 | 64 |  | √ | 0 | 中标供应商数量 |
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
| 55 | fismultipackage | 是否包含多标段 | bpchar | 1 |  | √ | '0' | 是否包含多标段 |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 58 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 59 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
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
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
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

## 选择供应商组件-分表 t_src_project_f

- **表名称：** 选择供应商组件-分表
- **表名：** t_src_project_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpickschemeld | 供应商抽取方案 | int8 | 64 |  | √ | 0 | [供应商抽取方案 src_supplierpick](../src_files/src_supplierpick.md) |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fisselect | 关联标的是否默认全选 | bpchar | 1 |  | √ | '0' | 关联标的是否默认全选 |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fchgsrcbillid | fchgsrcbillid | int8 | 64 |  | √ | 0 |  |
| 11 | fpurlistnote | fpurlistnote | varchar | 50 |  | √ | ' ' |  |
| 12 | fcondition | 邀请条件 | varchar | 2000 |  | √ | ' ' | 邀请条件 |
| 13 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 16 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 17 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 19 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 20 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 21 | fexpertcount | 抽取供应商数 | int8 | 64 |  | √ | 0 | 抽取供应商数 |
| 22 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 25 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 26 | fbidchangeid | fbidchangeid | int8 | 64 |  | √ | 0 |  |
| 27 | fcompbillno | fcompbillno | varchar | 30 |  | √ | ' ' |  |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_f_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_f |  | fid |

---

## 选择供应商组件-分表 t_src_project_a

- **表名称：** 选择供应商组件-分表
- **表名：** t_src_project_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherruleassess | fotherruleassess | varchar | 255 |  |  | ' ' |  |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 5 | fresult | fresult | bpchar | 1 |  | √ | ' ' |  |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fisbidnotice | fisbidnotice | bpchar | 1 |  | √ | '0' |  |
| 9 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 10 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 11 | fversion | fversion | int8 | 64 |  | √ | 1 |  |
| 12 | famountrange | famountrange | varchar | 50 |  | √ | ' ' |  |
| 13 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsourcestateprint | fsourcestateprint | varchar | 100 |  | √ | ' ' |  |
| 16 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 17 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 18 | fprojectcreatorid | fprojectcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | fisneedinvite | fisneedinvite | bpchar | 1 |  | √ | ' ' |  |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | fotherwinrule | fotherwinrule | varchar | 255 |  |  | ' ' |  |
| 24 | fdecisionname | fdecisionname | varchar | 100 |  | √ | ' ' |  |
| 25 | fispaper | fispaper | bpchar | 1 |  | √ | '0' |  |
| 26 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 27 | fissplitdoc | fissplitdoc | bpchar | 1 |  | √ | '0' |  |
| 28 | freasonremark_tag | freasonremark_tag | text | 0 |  |  | null |  |
| 29 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 30 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 31 | faftertalkrule | faftertalkrule | varchar | 255 |  |  | ' ' |  |
| 32 | fpurdecision | 采购决策（是否上采委会） | bpchar | 1 |  | √ | '0' | 采购决策（是否上采委会） |
| 33 | fsolereason | fsolereason | bpchar | 1 |  | √ | ' ' |  |
| 34 | forderrule | forderrule | varchar | 255 |  | √ | ' ' |  |
| 35 | freasonremark | freasonremark | varchar | 255 |  | √ | ' ' |  |
| 36 | fopentypep | fopentypep | varchar | 50 |  | √ | ' ' |  |
| 37 | fdecisionbillno | fdecisionbillno | varchar | 50 |  | √ | ' ' |  |
| 38 | fcontractcycle | fcontractcycle | varchar | 50 |  | √ | ' ' |  |
| 39 | fremark | fremark | varchar | 255 |  |  | ' ' |  |
| 40 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 41 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 42 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 43 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 44 | fbidaddress | fbidaddress | varchar | 50 |  | √ | ' ' |  |
| 45 | fsourcestate | fsourcestate | varchar | 30 |  | √ | ' ' |  |
| 46 | fsrcapplyid | fsrcapplyid | int8 | 64 |  | √ | 0 |  |
| 47 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 48 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 49 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 50 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 51 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 52 | fprojectcreatetime | fprojectcreatetime | timestamp | 0 |  |  | null |  |
| 53 | fismustapply | fismustapply | bpchar | 1 |  | √ | '0' |  |
| 54 | fdiscardrule | fdiscardrule | varchar | 255 |  |  | ' ' |  |

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

---

## 风险信息分录-子表 t_src_risksupplier

- **表名称：** 风险信息分录-子表
- **表名：** t_src_risksupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryid2 | fentryid2 | int8 | 64 |  | √ | 0 | id |
| 3 | friskmessage | 风险信息 | varchar | 500 |  | √ | ' ' | 风险信息 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 6 | fpackagename | 标段 | varchar | 50 |  | √ | ' ' | 标段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fdiscerndate | 识别日期 | timestamp | 0 |  |  | null | 识别日期 |
| 9 | frisktype | frisktype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid2 | fentryid2 |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_risksupplier |  | fentryid2 |
| 2 | idx_src_risksupplier_fid |  | fid |

---

## 供应商分录-子表 t_src_invitesupplier_temp

- **表名称：** 供应商分录-子表
- **表名：** t_src_invitesupplier_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismanualselect | fismanualselect | bpchar | 1 |  | √ | '0' |  |
| 3 | faddress | 地址 | varchar | 100 |  | √ | ' ' | 地址 |
| 4 | fisexemptapt | 免资审 | bpchar | 1 |  | √ | '0' | 免资审 |
| 5 | fisbidpush | fisbidpush | bpchar | 1 |  | √ | '0' |  |
| 6 | fisselect | fisselect | bpchar | 1 |  | √ | '0' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 10 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 11 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 12 | fisabandon | 是否弃标 | bpchar | 1 |  | √ | '0' | 是否弃标 |
| 13 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 14 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 15 | fabandonreason | 弃标原因 | varchar | 255 |  | √ | ' ' | 弃标原因 |
| 16 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 17 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 18 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 19 | fisfeeagent | 代理缴费 | bpchar | 1 |  | √ | '0' | 代理缴费 |
| 20 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 21 | freason | 废标原因 | varchar | 255 |  | √ | ' ' | 废标原因 |
| 22 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: bd_supplier :供应商 src_supplier_tmp :临时供应商 |
| 24 | ftempsupplierid | 临时供应商ID | int8 | 64 |  | √ | 0 | 临时供应商ID |
| 25 | fisaptpush2 | fisaptpush2 | bpchar | 1 |  | √ | '0' |  |
| 26 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 27 | fpublishdate | 发标日期 | timestamp | 0 |  |  | null | 发标日期 |
| 28 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fisquote | fisquote | bpchar | 1 |  | √ | '0' |  |
| 31 | frisknum | 风险数 | int4 | 32 |  | √ | 0 | 风险数 |
| 32 | fisaptpush | fisaptpush | bpchar | 1 |  | √ | '0' |  |
| 33 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 34 | fk_sf_textfield | fk_sf_textfield | varchar | 50 |  | √ | ' ' |  |
| 35 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 36 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 9 :补充供应商 |
| 37 | fisaptitude | 资审/评标结果 | bpchar | 1 |  | √ | '0' | 资审/评标结果,枚举: 0 :未资审/评标 1 :资审/评标合格 2 :资审/评标不合格 |
| 38 | fispayfee | 是否已缴纳 | bpchar | 1 |  | √ | '0' | 是否已缴纳 |
| 39 | fcurrentrank | fcurrentrank | int4 | 32 |  | √ | 0 |  |
| 40 | ffeeamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 41 | fpurlistnote | 关联标的 | varchar | 50 |  | √ | ' ' | 关联标的 |
| 42 | fpublisherid | 发标人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fispuraptitude | 代理资审回复 | bpchar | 1 |  | √ | '0' | 代理资审回复 |
| 44 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 45 | fispuragent | 代理投标/报价 | bpchar | 1 |  | √ | '0' | 代理投标/报价 |
| 46 | fquotedate | fquotedate | timestamp | 0 |  |  | null |  |
| 47 | fpublishstatus | 发标状态 | bpchar | 1 |  | √ | ' ' | 发标状态,枚举: A :待发标 B :已发标 |
| 48 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 49 | friskremark | 风险摘要 | varchar | 510 |  | √ | ' ' | 风险摘要 |
| 50 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 51 | faptitudenote | 资审意见 | varchar | 255 |  | √ | ' ' | 资审意见 |
| 52 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 53 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 54 | fisaptitudereply | fisaptitudereply | bpchar | 1 |  | √ | '0' |  |
| 55 | fisvalid | fisvalid | bpchar | 1 |  | √ | '0' |  |

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
