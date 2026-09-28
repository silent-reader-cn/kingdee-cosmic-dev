# 项目供应商变更-src_invitesupplier_chg

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

## 项目供应商变更-主表 t_src_project

- **表名称：** 项目供应商变更-主表
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
| 20 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
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

## 项目供应商变更-分表 t_src_project_f

- **表名称：** 项目供应商变更-分表
- **表名：** t_src_project_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 9 | fcondition | 邀请条件 | varchar | 2000 |  | √ | ' ' | 邀请条件 |
| 10 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 12 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 13 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 14 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 18 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 21 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 22 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 23 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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

## 供应商分录-子表 t_src_invitesupplier_temp

- **表名称：** 供应商分录-子表
- **表名：** t_src_invitesupplier_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismanualselect | fismanualselect | bpchar | 1 |  | √ | '0' |  |
| 3 | faddress | 地址 | varchar | 100 |  | √ | ' ' | 地址 |
| 4 | fisbidpush | fisbidpush | bpchar | 1 |  | √ | '0' |  |
| 5 | fisselect | fisselect | bpchar | 1 |  | √ | '0' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fisdownload | 是否下载标书 | bpchar | 1 |  | √ | '0' | 是否下载标书 |
| 9 | fisdiscard | 是否废标 | bpchar | 1 |  | √ | '0' | 是否废标 |
| 10 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 11 | fisabandon | 是否弃标 | bpchar | 1 |  | √ | '0' | 是否弃标 |
| 12 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 13 | fisconfirm | 是否应标 | bpchar | 1 |  | √ | '0' | 是否应标 |
| 14 | fabandonreason | 弃标原因 | varchar | 255 |  | √ | ' ' | 弃标原因 |
| 15 | fisnegotiate | fisnegotiate | bpchar | 1 |  | √ | '0' |  |
| 16 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 17 | fistender | 是否投标 | bpchar | 1 |  | √ | '0' | 是否投标 |
| 18 | fisfeeagent | 代理缴费 | bpchar | 1 |  | √ | '0' | 代理缴费 |
| 19 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 20 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 21 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 23 | fisaptpush2 | fisaptpush2 | bpchar | 1 |  | √ | '0' |  |
| 24 | fsupplierip | fsupplierip | varchar | 100 |  | √ | ' ' |  |
| 25 | fpublishdate | fpublishdate | timestamp | 0 |  |  | null |  |
| 26 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fisquote | fisquote | bpchar | 1 |  | √ | '0' |  |
| 29 | frisknum | frisknum | int4 | 32 |  | √ | 0 |  |
| 30 | fisaptpush | fisaptpush | bpchar | 1 |  | √ | '0' |  |
| 31 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 32 | fk_sf_textfield | fk_sf_textfield | varchar | 50 |  | √ | ' ' |  |
| 33 | fsuppliercode | fsuppliercode | varchar | 50 |  | √ | ' ' |  |
| 34 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: 1 :来源采委会 2 :立项新增 |
| 35 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 36 | fispayfee | 是否已缴纳 | bpchar | 1 |  | √ | '0' | 是否已缴纳 |
| 37 | fcurrentrank | fcurrentrank | int4 | 32 |  | √ | 0 |  |
| 38 | ffeeamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 39 | fpublisherid | fpublisherid | int8 | 64 |  | √ | 0 |  |
| 40 | fremark | fremark | varchar | 100 |  | √ | ' ' |  |
| 41 | fispuragent | 代理投标/报价 | bpchar | 1 |  | √ | '0' | 代理投标/报价 |
| 42 | fpublishstatus | fpublishstatus | bpchar | 1 |  | √ | ' ' |  |
| 43 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 44 | friskremark | friskremark | varchar | 510 |  | √ | ' ' |  |
| 45 | fisinvite | 是否邀请 | bpchar | 1 |  | √ | '0' | 是否邀请 |
| 46 | faptitudenote | faptitudenote | varchar | 255 |  | √ | ' ' |  |
| 47 | fentrysupplierip | fentrysupplierip | varchar | 100 |  | √ | ' ' |  |
| 48 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 49 | fisvalid | fisvalid | bpchar | 1 |  | √ | '0' |  |

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
