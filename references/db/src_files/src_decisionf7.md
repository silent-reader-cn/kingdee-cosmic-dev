# 定标F7-src_decisionf7

## 定标F7-主表 t_src_project

- **表名称：** 定标F7-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsourceid | 项目立项 | int8 | 64 |  | √ | 0 | [项目立项F7 src_demandnotwo](../src_files/src_demandnotwo.md) |
| 8 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | 定标未税总价 | numeric | 23 | 10 | √ | 0 | 定标未税总价 |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | 寻源项目编号 | varchar | 30 |  | √ | ' ' | 寻源项目编号 |
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
| 43 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 44 | fwinruleid | fwinruleid | int8 | 64 |  | √ | 0 |  |
| 45 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 46 | famount | 预计采购总金额 | numeric | 23 | 10 | √ | 0 | 预计采购总金额 |
| 47 | fsystype | fsystype | bpchar | 1 |  | √ | '1' |  |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | fopentype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 54 | fbiztypeid | fbiztypeid | int8 | 64 |  | √ | 0 |  |
| 55 | fismultipackage | fismultipackage | bpchar | 1 |  | √ | '0' |  |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | fsourceclassid | int8 | 64 |  | √ | 0 |  |
| 58 | fopenstatus | fopenstatus | bpchar | 1 |  | √ | '1' |  |
| 59 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 60 | ftaxtype | ftaxtype | varchar | 30 |  | √ | ' ' |  |
| 61 | fbidname | 寻源项目名称 | varchar | 300 |  | √ | ' ' | 寻源项目名称 |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | fdecisiontype | bpchar | 1 |  | √ | ' ' |  |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | 定标总价 | numeric | 23 | 10 | √ | 0 | 定标总价 |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | fcurrentnode | int8 | 64 |  | √ | 0 |  |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
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

## 定标F7-分表 t_src_project_t

- **表名称：** 定标F7-分表
- **表名：** t_src_project_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecisionsumid | fdecisionsumid | int8 | 64 |  | √ | 0 |  |
| 3 | fpurassessid | fpurassessid | int8 | 64 |  | √ | 0 |  |
| 4 | fistemppush | fistemppush | bpchar | 1 |  | √ | '0' |  |
| 5 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待定标 B :定商定价 C :定商定价已审核 D :已终止 E :评审中 F :评审通过 G :评审驳回 H :评审失效 I :合同待评审 J :合同评审中 K :合同评审通过 L :合同评审驳回 M :合同评审失效 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fiscreatpur | fiscreatpur | bpchar | 1 |  | √ | '0' |  |
| 8 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fisneedinvite2 | fisneedinvite2 | bpchar | 1 |  | √ | ' ' |  |
| 12 | fiswinnotice | fiswinnotice | bpchar | 1 |  | √ | '0' |  |
| 13 | fpriceeffect | fpriceeffect | timestamp | 0 |  |  | null |  |
| 14 | fresultstatus | fresultstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fisdecisionresult | fisdecisionresult | bpchar | 1 |  | √ | '0' |  |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 19 | fisedited | fisedited | bpchar | 1 |  | √ | '0' |  |
| 20 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 22 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 23 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 24 | fpricebiztype | fpricebiztype | int8 | 64 |  | √ | 0 |  |
| 25 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 26 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 27 | fdecstatus | fdecstatus | bpchar | 1 |  | √ | ' ' |  |
| 28 | ffluctuateamount | ffluctuateamount | varchar | 50 |  | √ | ' ' |  |
| 29 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fconclusion | fconclusion | varchar | 1000 |  | √ | ' ' |  |
| 33 | fdecisiontype | fdecisiontype | int8 | 64 |  | √ | 0 |  |
| 34 | fwintime | fwintime | timestamp | 0 |  |  | null |  |
| 35 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 36 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 37 | fdecidelink | fdecidelink | varchar | 100 |  | √ | ' ' |  |
| 38 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 39 | fcomnum | fcomnum | int8 | 64 |  | √ | 0 |  |
| 40 | fchassistype | fchassistype | int8 | 64 |  | √ | 0 |  |
| 41 | fpurtype | 采购类型 | varchar | 30 |  | √ | ' ' | 采购类型,枚举: A :商超采购 B :小金额采购（非网购） C :小金额采购（网购） D :无需三家比价（分采） |
| 42 | fpurreport | fpurreport | varchar | 30 |  | √ | ' ' |  |
| 43 | fdecidenumber | fdecidenumber | varchar | 50 |  | √ | ' ' |  |
| 44 | ftempreason | ftempreason | varchar | 255 |  | √ | ' ' |  |
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

---

## 定标F7-多语言表 t_src_project_l

- **表名称：** 定标F7-多语言表
- **表名：** t_src_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | fnodename | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbidname | 寻源项目名称 | varchar | 300 |  | √ | ' ' | 寻源项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_l_flocaleid |  | flocaleid,fid |
| 2 | pk__src_project_l |  | fpkid |
