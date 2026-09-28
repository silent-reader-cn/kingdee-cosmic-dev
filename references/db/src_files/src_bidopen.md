# 开标准备-src_bidopen

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | [组件注册 pds_compreg](../pds_files/pds_compreg.md) |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 50 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projecttpl_fscp |  | fsrctplid |
| 2 | idx_src_projecttpl_fobj |  | fbizobject |
| 3 | pk_src_projecttpl |  | fentryid |
| 4 | idx_src_projecttpl_fcom |  | fcomponentid |
| 5 | idx_src_projecttpl_fid |  | fid |
| 6 | idx_src_projecttpl_ftem |  | ftemplateid |

---

## 关键流程分录-子表 t_src_projectnode

- **表名称：** 关键流程分录-子表
- **表名：** t_src_projectnode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbiznodeid | 关键业务节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 4 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 6 | fbizobject | 关键业务对象 | varchar | 50 |  | √ | ' ' | 关键业务对象 |
| 7 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已关闭 Z :无需处理 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectnode_fobj |  | fbizobject |
| 2 | idx_src_projectnode_fid |  | fid |
| 3 | pk_src_projectnode |  | fentryid |
| 4 | idx_src_projectnode_feobj |  | fextobject |
| 5 | idx_src_projectnode_fnod |  | fbiznodeid |
| 6 | idx_src_projectnode_ftem |  | ftemplateid |

---

## 附属流程分录-子表 t_src_projectnodesub

- **表名称：** 附属流程分录-子表
- **表名：** t_src_projectnodesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbiznodeid | 附属业务节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 2 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 3 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :创建 B :已提交 C :已审核 D :已关闭 |
| 5 | fbizobject | 附属业务对象 | varchar | 50 |  | √ | ' ' | 附属业务对象 |
| 6 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已关闭 Z :无需处理 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fextobject | 对应状态表 | varchar | 50 |  | √ | ' ' | 对应状态表 |
| 9 | fisaudit | 是否需要审核 | bpchar | 1 |  | √ | '0' | 是否需要审核 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fisflowchart | 是否在流程图显示 | bpchar | 1 |  | √ | '0' | 是否在流程图显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectnodesub_fobj |  | fbizobject |
| 2 | idx_src_projectnodesub_feid |  | fentryid |
| 3 | pk_src_projectnodesub |  | fdetailid |
| 4 | idx_src_projectnodesub_fnod |  | fbiznodeid |
| 5 | idx_src_projectnodesub_feobj |  | fextobject |
| 6 | idx_src_projectnodesub_ftem |  | ftemplateid |

---

## 采购组织(多选)-多选基础资料表 t_src_projectpurorg

- **表名称：** 采购组织(多选)-多选基础资料表
- **表名：** t_src_projectpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectpurorg_bid |  | fbasedataid |
| 2 | idx_src_projectpurorg_fid |  | fid |
| 3 | pk_src_projectpurorg |  | fpkid |

---

## 开标准备-主表 t_src_project

- **表名称：** 开标准备-主表
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
| 7 | fsourceid | 项目立项 | int8 | 64 |  | √ | 0 | [项目立项查询 src_demandno](../src_files/src_demandno.md) |
| 8 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | 招标方式 | bpchar | 1 |  | √ | ' ' | 招标方式,枚举: 1 :邀请招标 2 :公开招标 |
| 18 | fbillno | 招标项目编号 | varchar | 30 |  | √ | ' ' | 招标项目编号 |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | 当前节点名称 | varchar | 50 |  | √ | ' ' | 当前节点名称 |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | 投标截止时间 | timestamp | 0 |  |  | null | 投标截止时间 |
| 33 | fruleassess | fruleassess | bpchar | 1 |  | √ | ' ' |  |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | fbiderqty | int8 | 64 |  | √ | 0 |  |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | fisviepublish | bpchar | 1 |  | √ | '0' |  |
| 41 | ftieredtype | 阶梯报价方式 | bpchar | 1 |  | √ | '1' | 阶梯报价方式,枚举: 1 :不启用阶梯报价 2 :采购清单分录总量阶梯报价 3 :采购清单子分录总量阶梯报价 4 :采购清单子分录分段阶梯报价 |
| 42 | fdecidedate | fdecidedate | timestamp | 0 |  |  | null |  |
| 43 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 44 | fwinruleid | fwinruleid | int8 | 64 |  | √ | 0 |  |
| 45 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 46 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 47 | fsystype | 来源类型 | bpchar | 1 |  | √ | '1' | 来源类型,枚举: 1 :项目启动 2 :手工新增 3 :外部系统 |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，再开商务标 3 :先开评商务标，再开技术标 |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 54 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 55 | fismultipackage | 是否多标段 | bpchar | 1 |  | √ | '0' | 是否多标段 |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | 寻源方式类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 58 | fopenstatus | 开标状态 | bpchar | 1 |  | √ | '1' | 开标状态,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 59 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 60 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 61 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |
| 62 | fterminalnode | 终止节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 63 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | 是否按标段开标 | bpchar | 1 |  | √ | '0' | 是否按标段开标 |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
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

## 开标准备-分表 t_src_project_a

- **表名称：** 开标准备-分表
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
| 11 | fversion | 版本号 | int8 | 64 |  | √ | 1 | 版本号 |
| 12 | famountrange | famountrange | varchar | 50 |  | √ | ' ' |  |
| 13 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fsourcestateprint | fsourcestateprint | varchar | 100 |  | √ | ' ' |  |
| 16 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 17 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 18 | fprojectcreatorid | 项目创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 32 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | '0' |  |
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
| 46 | fsrcapplyid | 寻源申请 | int8 | 64 |  | √ | 0 | [寻源申请F7 src_applyf7](../src_files/src_applyf7.md) |
| 47 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 48 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 49 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 50 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 51 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 52 | fprojectcreatetime | 项目创建时间 | timestamp | 0 |  |  | null | 项目创建时间 |
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

## 开标准备-多语言表 t_src_project_l

- **表名称：** 开标准备-多语言表
- **表名：** t_src_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | 当前节点名称 | varchar | 100 |  | √ | ' ' | 当前节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_l_flocaleid |  | flocaleid,fid |
| 2 | pk__src_project_l |  | fpkid |

---

## 开标准备-分表 t_src_project_o

- **表名称：** 开标准备-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | fbidstatus | bpchar | 1 |  | √ | ' ' |  |
| 3 | frankprice | frankprice | varchar | 30 |  | √ | ' ' |  |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fcashdeposit | fcashdeposit | numeric | 23 | 10 | √ | 0 |  |
| 6 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 7 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fplanopendate | fplanopendate | timestamp | 0 |  |  | null |  |
| 10 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 11 | frankamount | frankamount | varchar | 30 |  | √ | ' ' |  |
| 12 | faddtime | faddtime | int8 | 64 |  | √ | 0 |  |
| 13 | fbidtime | fbidtime | int8 | 64 |  | √ | 0 |  |
| 14 | flasttime | flasttime | int8 | 64 |  | √ | 0 |  |
| 15 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fviepattern | fviepattern | bpchar | 1 |  | √ | ' ' |  |
| 17 | fresultdate | fresultdate | timestamp | 0 |  |  | null |  |
| 18 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 22 | faddtimecount | faddtimecount | int4 | 32 |  | √ | 0 |  |
| 23 | fbidcount | fbidcount | int8 | 64 |  | √ | 0 |  |
| 24 | fbidrestoftime | fbidrestoftime | int8 | 64 |  | √ | 0 |  |
| 25 | ftendency | ftendency | bpchar | 1 |  | √ | ' ' |  |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 28 | fisregioncontrol | fisregioncontrol | bpchar | 1 |  | √ | ' ' |  |
| 29 | freducetype | freducetype | bpchar | 1 |  | √ | ' ' |  |
| 30 | flastquotedate | flastquotedate | timestamp | 0 |  |  | null |  |
| 31 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 32 | fisnewprice | fisnewprice | bpchar | 1 |  | √ | '0' |  |
| 33 | fenrolldate | fenrolldate | timestamp | 0 |  |  | null |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fisbizscore | fisbizscore | bpchar | 1 |  | √ | '0' |  |
| 37 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 38 | fisnoderank | fisnoderank | bpchar | 1 |  | √ | '0' |  |
| 39 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止/流标 E :已废标 Z :无需处理 |
| 41 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fisautoviebyplan | fisautoviebyplan | bpchar | 1 |  | √ | '0' |  |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fpauseamt | fpauseamt | numeric | 23 | 10 | √ | 0 |  |
| 45 | freducepct | freducepct | numeric | 23 | 10 | √ | 0 |  |
| 46 | fopen4 | fopen4 | bpchar | 1 |  | √ | ' ' |  |
| 47 | fopen2 | fopen2 | bpchar | 1 |  | √ | ' ' |  |
| 48 | fpausetime | fpausetime | timestamp | 0 |  |  | null |  |
| 49 | fsubmittype | fsubmittype | bpchar | 1 |  | √ | ' ' |  |
| 50 | fopen3 | fopen3 | bpchar | 1 |  | √ | ' ' |  |
| 51 | fsumtype | fsumtype | bpchar | 1 |  | √ | ' ' |  |
| 52 | fautoconfirm | fautoconfirm | bpchar | 1 |  | √ | ' ' |  |
| 53 | fopen1 | fopen1 | bpchar | 1 |  | √ | ' ' |  |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 57 | fvie_purlist | fvie_purlist | bpchar | 1 |  | √ | ' ' |  |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 60 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 61 | fminamount | fminamount | numeric | 23 | 10 | √ | 0 |  |
| 62 | faddtimenum | faddtimenum | int4 | 32 |  | √ | 0 |  |
| 63 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 64 | fvietype | fvietype | bpchar | 1 |  | √ | ' ' |  |
| 65 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 66 | fdelaytime | fdelaytime | int8 | 64 |  | √ | 0 |  |
| 67 | fbidnumber | fbidnumber | int8 | 64 |  | √ | 0 |  |
| 68 | fopinion | fopinion | varchar | 255 |  | √ | ' ' |  |
| 69 | fpausestarttime | fpausestarttime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_o_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_o |  | fid |

---

## 中标金额汇总分录(MOV)-子表 t_src_decisionsumsup2

- **表名称：** 中标金额汇总分录(MOV)-子表
- **表名：** t_src_decisionsumsup2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frank | 排名 | int8 | 64 |  | √ | 0 | 排名 |
| 3 | fmaxamount | 标杆未税金额 | numeric | 23 | 10 | √ | 0 | 标杆未税金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fresult | 是否中标 | varchar | 30 |  | √ | ' ' | 是否中标,枚举: 1 :中标 2 :未中标 |
| 6 | famount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 7 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 8 | fpreorderratio1 | 预定标含税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标含税占比(%) |
| 9 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 10 | floctaxamount | 报价含税金额 | numeric | 23 | 10 | √ | 0 | 报价含税金额 |
| 11 | fpreorderratio | 预定标未税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标未税占比(%) |
| 12 | forderratio | 中标未税占比(%) | numeric | 23 | 10 | √ | 0 | 中标未税占比(%) |
| 13 | fbudgetamount | fbudgetamount | numeric | 23 | 10 | √ | 0 |  |
| 14 | fpreamount | 预定标未税金额 | numeric | 23 | 10 | √ | 0 | 预定标未税金额 |
| 15 | ftaxamountrate | 含税价差率(%) | numeric | 23 | 10 | √ | 0 | 含税价差率(%) |
| 16 | fpretaxamount | 预定标含税金额 | numeric | 23 | 10 | √ | 0 | 预定标含税金额 |
| 17 | fcontracttype | fcontracttype | bpchar | 1 |  | √ | ' ' |  |
| 18 | ftaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 19 | famountrate | 未税价差率(%) | numeric | 23 | 10 | √ | 0 | 未税价差率(%) |
| 20 | fphone | fphone | varchar | 50 |  | √ | ' ' |  |
| 21 | fmaxtaxamount | 标杆含税金额 | numeric | 23 | 10 | √ | 0 | 标杆含税金额 |
| 22 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 23 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 24 | femail | femail | varchar | 50 |  | √ | ' ' |  |
| 25 | fbidcount | 中标标的数 | int4 | 32 |  | √ | 0 | 中标标的数 |
| 26 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 27 | fpackagename | fpackagename | varchar | 50 |  | √ | ' ' |  |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 29 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :内部员工 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 30 | flocamount | 报价未税金额 | numeric | 23 | 10 | √ | 0 | 报价未税金额 |
| 31 | ftaxamountdiff | 含税价差 | numeric | 23 | 10 | √ | 0 | 含税价差 |
| 32 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 33 | famountdiff | 未税价差 | numeric | 23 | 10 | √ | 0 | 未税价差 |
| 34 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | forderratio1 | 中标含税占比(%) | numeric | 23 | 10 | √ | 0 | 中标含税占比(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsumsup2_fpid |  | fparentid |
| 2 | pk_src_decisionsumsup2 |  | fentryid |
| 3 | idx_src_decisionsumsup2_fpag |  | fpackageid |
| 4 | idx_src_decisionsumsup2_fid |  | fid |
| 5 | idx_src_decisionsumsup2_fcid |  | fcategoryid |
| 6 | idx_src_decisionsumsup2_fsup |  | fsupplierid |
| 7 | idx_src_decisionsumsup2_fpro |  | fprojectid |
