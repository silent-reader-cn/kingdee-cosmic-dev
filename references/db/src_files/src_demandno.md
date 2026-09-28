# 项目立项查询-src_demandno

## 项目立项查询-分表 t_src_demand_a

- **表名称：** 项目立项查询-分表
- **表名：** t_src_demand_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecidelink | fdecidelink | varchar | 100 |  | √ | ' ' |  |
| 3 | fdecstatus | 关联采委会状态 | bpchar | 1 |  | √ | ' ' | 关联采委会状态,枚举: A :未上报 B :已上报 C :已关联 |
| 4 | fdecisionid | 采委会决策单号 | int8 | 64 |  | √ | 0 | 采委会决策单号 src_decisionbillnotwo |
| 5 | fistemppush | fistemppush | bpchar | 1 |  | √ | '0' |  |
| 6 | fdecidenumber | 会议决策单号 | varchar | 50 |  | √ | ' ' | 会议决策单号 |
| 7 | fresultstatus | fresultstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | ftempreason | ftempreason | varchar | 255 |  | √ | ' ' |  |
| 9 | fconclusion | fconclusion | varchar | 1000 |  | √ | ' ' |  |
| 10 | fdecisiontype | fdecisiontype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demand_a_fid |  | fdecidenumber |
| 2 | pk_src_demand_a |  | fid |

---

## 项目立项查询-多语言表 t_src_demand_l

- **表名称：** 项目立项查询-多语言表
- **表名：** t_src_demand_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 项目名称 | varchar | 300 |  | √ | ' ' | 项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_demand_l |  | fpkid |
| 2 | idx_src_demand_l_flocaleid |  | fid,flocaleid |

---

## 采购组织(多选)-多选基础资料表 t_src_demandpurorg

- **表名称：** 采购组织(多选)-多选基础资料表
- **表名：** t_src_demandpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demandpurorg_fid |  | fid |
| 2 | pk_src_demandpurorg |  | fpkid |
| 3 | idx_src_demandpurorg_bid |  | fbasedataid |

---

## 寻源场景-子表 t_src_decisionscene

- **表名称：** 寻源场景-子表
- **表名：** t_src_decisionscene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fotherruleassess | fotherruleassess | varchar | 1000 |  | √ | ' ' |  |
| 3 | fsceneno_des | fsceneno_des | varchar | 100 |  | √ | ' ' |  |
| 4 | fsceneamount | 寻源项目未税金额 | numeric | 23 | 10 | √ | 0 | 寻源项目未税金额 |
| 5 | fotherreason | fotherreason | varchar | 255 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fbargainrule | fbargainrule | varchar | 30 |  | √ | ' ' |  |
| 9 | fsuppliernum | fsuppliernum | int8 | 64 |  | √ | 0 |  |
| 10 | ftitle | ftitle | varchar | 50 |  | √ | ' ' |  |
| 11 | frange | frange | varchar | 50 |  | √ | ' ' |  |
| 12 | fscenestatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :未下推 B :已下推 |
| 13 | fchassisttypeid | fchassisttypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fprojectno | fprojectno | varchar | 50 |  | √ | ' ' |  |
| 15 | fdetailid | fdetailid | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | fbillno | varchar | 100 |  | √ | ' ' |  |
| 17 | fwinrule | fwinrule | int8 | 64 |  | √ | 0 |  |
| 18 | fisfunction | fisfunction | bpchar | 1 |  | √ | '0' |  |
| 19 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbillno2 | fbillno2 | varchar | 50 |  | √ | ' ' |  |
| 22 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fscenename_des | 寻源项目名称 | varchar | 100 |  | √ | ' ' | 寻源项目名称 |
| 25 | fpurtype | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 26 | fruleassess | fruleassess | varchar | 30 |  | √ | ' ' |  |
| 27 | fquerycondition | fquerycondition | varchar | 255 |  | √ | ' ' |  |
| 28 | fscenechasisstid | fscenechasisstid | int8 | 64 |  | √ | 0 |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fotherwinrule | fotherwinrule | varchar | 1000 |  | √ | ' ' |  |
| 32 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 33 | famount | 寻源项目价税合计 | numeric | 23 | 10 | √ | 0 | 寻源项目价税合计 |
| 34 | fseq1 | fseq1 | varchar | 50 |  | √ | ' ' |  |
| 35 | fcompreper | fcompreper | numeric | 23 | 10 | √ | 0 |  |
| 36 | fwinrule2 | fwinrule2 | int8 | 64 |  | √ | 0 |  |
| 37 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 38 | fbiztype | fbiztype | varchar | 30 |  | √ | ' ' |  |
| 39 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 40 | faftertalkrule | faftertalkrule | varchar | 1000 |  | √ | ' ' |  |
| 41 | fsolereason | fsolereason | varchar | 100 |  | √ | ' ' |  |
| 42 | forderrule | forderrule | varchar | 1000 |  | √ | ' ' |  |
| 43 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | ftalkrule | ftalkrule | int8 | 64 |  | √ | 0 |  |
| 46 | fskillper | fskillper | numeric | 23 | 10 | √ | 0 |  |
| 47 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 48 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 49 | fbusinessper | fbusinessper | numeric | 23 | 10 | √ | 0 |  |
| 50 | fisprice | fisprice | bpchar | 1 |  | √ | '0' |  |
| 51 | fsrcflowconfig | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 52 | fdiscardrule | fdiscardrule | varchar | 1000 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_deciscene_pid |  | fprojectid |
| 2 | pk_src_decisionscene |  | fentryid |
| 3 | idx_src_deciscene_fid |  | fid |

---

## 关联标的-多选基础资料表 t_src_decisionitem

- **表名称：** 关联标的-多选基础资料表
- **表名：** t_src_decisionitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目立项分录F7 src_demandf7two |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_decisionitem |  | fpkid |
| 2 | idx_src_decisionitem_bid |  | fbasedataid |
| 3 | idx_src_decisionitem_fid |  | fentryid |

---

## 项目立项查询-主表 t_src_demand

- **表名称：** 项目立项查询-主表
- **表名：** t_src_demand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fisproject | fisproject | bpchar | 1 |  | √ | '0' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fplace | fplace | int8 | 64 |  | √ | 0 |  |
| 5 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 6 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fsrcemotion | fsrcemotion | varchar | 30 |  | √ | ' ' |  |
| 9 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | ftitle | 项目名称 | varchar | 300 |  | √ | ' ' | 项目名称 |
| 11 | fwithvatamount | fwithvatamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 13 | fdecisonlevelhide | fdecisonlevelhide | int8 | 64 |  | √ | 0 |  |
| 14 | fspecial | fspecial | varchar | 50 |  | √ | ' ' |  |
| 15 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | flevelid | flevelid | int8 | 64 |  | √ | 0 |  |
| 17 | fsceneitem | 寻源场景关联标的 | bpchar | 1 |  | √ | ' ' | 寻源场景关联标的 |
| 18 | fsigningcycle | fsigningcycle | varchar | 50 |  | √ | ' ' |  |
| 19 | fbillno | 项目编号 | varchar | 60 |  | √ | ' ' | 项目编号 |
| 20 | fdecisonlevelld | fdecisonlevelld | int8 | 64 |  | √ | 0 |  |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fisselloff | 是否变卖需求 | varchar | 30 |  | √ | '0' | 是否变卖需求,枚举: A :是 B :否 |
| 24 | fservicetype | fservicetype | int8 | 64 |  | √ | 0 |  |
| 25 | fdecisiontypeid | fdecisiontypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fproject | fproject | varchar | 50 |  | √ | ' ' |  |
| 27 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 28 | fisproject2 | fisproject2 | bpchar | 1 |  | √ | '0' |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | fbusiarea | fbusiarea | int8 | 64 |  | √ | 0 |  |
| 31 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 32 | fdemandaffiliateid | fdemandaffiliateid | int8 | 64 |  | √ | 0 |  |
| 33 | famount | 预估未税金额 | numeric | 23 | 10 | √ | 0 | 预估未税金额 |
| 34 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 35 | fsurplusamount | 预估价税合计 | numeric | 23 | 10 | √ | 0 | 预估价税合计 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fnotreason | fnotreason | varchar | 100 |  | √ | ' ' |  |
| 38 | fismultiscene | fismultiscene | bpchar | 1 |  | √ | '1' |  |
| 39 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 40 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 41 | fpurdecision | 会议决策 | bpchar | 1 |  | √ | ' ' | 会议决策 |
| 42 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | '1' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 43 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 44 | fk_basedatafield | fk_basedatafield | int8 | 64 |  | √ | 0 |  |
| 45 | fbusitype | fbusitype | varchar | 30 |  | √ | ' ' |  |
| 46 | fchassisttype | fchassisttype | int8 | 64 |  | √ | 0 |  |
| 47 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 48 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 49 | fcostattribution | fcostattribution | int8 | 64 |  | √ | 0 |  |
| 50 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 51 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 52 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 53 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 54 | fsumqty | fsumqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 56 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 57 | fpurchasetype | 采购类型 | varchar | 30 |  | √ | ' ' | 采购类型,枚举: 0 :年采 1 :非年采 2 :混和采购 |
| 58 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 59 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | fsumtax | fsumtax | numeric | 23 | 10 | √ | 0 |  |
| 61 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_demand |  | fid |
| 2 | idx_src_demand_fbillno |  | fbillno |
| 3 | idx_src_demand_fparentid |  | fparentid |

---

## 标的附件-附件表 t_src_purlistentry_fj

- **表名称：** 标的附件-附件表
- **表名：** t_src_purlistentry_fj

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
| 1 | idx_src_purlistentry_fj_bid |  | fbasedataid |
| 2 | pk_src_purlistentry_fj |  | fpkid |
| 3 | idx_src_purlistentry_fj_fid |  | fentryid |

---

## 供应商-多选基础资料表 t_src_scene_supplier

- **表名称：** 供应商-多选基础资料表
- **表名：** t_src_scene_supplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_scene_supplier |  | fpkid |
| 2 | idx_src_scene_supplier_fid |  | fentryid |

---

## 标的信息-子表 t_src_notyearinfo

- **表名称：** 标的信息-子表
- **表名：** t_src_notyearinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftextfield1 | ftextfield1 | varchar | 50 |  | √ | ' ' |  |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fsupplierno1 | fsupplierno1 | int8 | 64 |  | √ | 0 |  |
| 6 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '1' |  |
| 7 | farrivedate1 | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 8 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauxptyid | fauxptyid | int8 | 64 |  | √ | 0 |  |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fprojectno1 | fprojectno1 | varchar | 50 |  | √ | ' ' |  |
| 12 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcheckboxfield1 | fcheckboxfield1 | bpchar | 1 |  | √ | ' ' |  |
| 14 | fk_sf_city | fk_sf_city | int8 | 64 |  | √ | 0 |  |
| 15 | fsrctypeid | fsrctypeid | int8 | 64 |  | √ | 0 |  |
| 16 | flinenumber1 | flinenumber1 | varchar | 50 |  | √ | ' ' |  |
| 17 | fapplicationdeptid | fapplicationdeptid | int8 | 64 |  | √ | 0 |  |
| 18 | frfqbillno | frfqbillno | varchar | 50 |  | √ | ' ' |  |
| 19 | fapplicationdate | fapplicationdate | timestamp | 0 |  |  | null |  |
| 20 | freqsource11 | freqsource11 | varchar | 30 |  | √ | ' ' |  |
| 21 | fmaterial1 | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | fbaseunitid | fbaseunitid | int8 | 64 |  | √ | 0 |  |
| 23 | fapplicantid | fapplicantid | int8 | 64 |  | √ | 0 |  |
| 24 | findicate1 | findicate1 | varchar | 30 |  | √ | ' ' |  |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fprice3 | fprice3 | numeric | 23 | 10 | √ | 0 |  |
| 27 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 28 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 29 | freqqty2 | freqqty2 | numeric | 23 | 10 | √ | 0 |  |
| 30 | fminiorderqty | fminiorderqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fmaterialname1 | fmaterialname1 | varchar | 100 |  | √ | ' ' |  |
| 32 | ftax | ftax | numeric | 23 | 10 | √ | 0 |  |
| 33 | fk_sf_companycode | fk_sf_companycode | int8 | 64 |  | √ | 0 |  |
| 34 | funit2 | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | freqdescribe | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 37 | frowtypeid | frowtypeid | int8 | 64 |  | √ | 0 |  |
| 38 | fprice2 | fprice2 | numeric | 23 | 10 | √ | 0 |  |
| 39 | fyearswitch | fyearswitch | bpchar | 1 |  | √ | ' ' |  |
| 40 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 41 | freqorg1 | freqorg1 | int8 | 64 |  | √ | 0 |  |
| 42 | fentryamount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 43 | fsrcentryid | fsrcentryid | varchar | 50 |  | √ | ' ' |  |
| 44 | fsrcbillno | fsrcbillno | varchar | 50 |  | √ | ' ' |  |
| 45 | ftaxamount2 | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 46 | fcontractline | fcontractline | int8 | 64 |  | √ | 0 |  |
| 47 | fk_sf_place | fk_sf_place | int8 | 64 |  | √ | 0 |  |
| 48 | fspecialreason | 标的描述 | varchar | 1024 |  |  | ' ' | 标的描述 |
| 49 | fmaterialmodel1 | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 50 | fprice | 预估未税单价 | numeric | 23 | 10 | √ | 0 | 预估未税单价 |
| 51 | fminipackqty | fminipackqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | fapplyno1 | fapplyno1 | varchar | 50 |  | √ | ' ' |  |
| 53 | ftaxprice1 | 预估含税单价 | numeric | 23 | 10 | √ | 0 | 预估含税单价 |
| 54 | fsceneid | fsceneid | int8 | 64 |  | √ | 0 |  |
| 55 | fcategory2 | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 56 | fspecialpurreason | fspecialpurreason | varchar | 50 |  | √ | ' ' |  |
| 57 | fcontractnold | fcontractnold | int8 | 64 |  | √ | 0 |  |
| 58 | fld | fld | varchar | 50 |  | √ | ' ' |  |
| 59 | fmaterial1code | fmaterial1code | varchar | 50 |  | √ | ' ' |  |
| 60 | fecpno | fecpno | varchar | 50 |  | √ | ' ' |  |
| 61 | fbdprojectid | fbdprojectid | int8 | 64 |  | √ | 0 |  |
| 62 | fmaterialgroup1 | fmaterialgroup1 | int8 | 64 |  | √ | 0 |  |
| 63 | freqtype1 | freqtype1 | int8 | 64 |  | √ | 0 |  |
| 64 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 65 | fentrystatus11 | fentrystatus11 | varchar | 30 |  | √ | ' ' |  |
| 66 | fqty1 | fqty1 | numeric | 23 | 10 | √ | 0 |  |
| 67 | fprojectname1 | fprojectname1 | varchar | 50 |  | √ | ' ' |  |
| 68 | fprice12 | fprice12 | numeric | 23 | 10 | √ | 0 |  |
| 69 | fprice13 | fprice13 | numeric | 23 | 10 | √ | 0 |  |
| 70 | fprice14 | fprice14 | numeric | 23 | 10 | √ | 0 |  |
| 71 | fprice15 | fprice15 | numeric | 23 | 10 | √ | 0 |  |
| 72 | fapplyno | fapplyno | varchar | 50 |  | √ | ' ' |  |
| 73 | fsuppliername1 | fsuppliername1 | varchar | 50 |  | √ | ' ' |  |
| 74 | fk_sf_busiarea | fk_sf_busiarea | int8 | 64 |  | √ | 0 |  |
| 75 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_notyearinfo_fid |  | fid |
| 2 | idx_src_notyearinfo_pid |  | fprojectid |
| 3 | idx_src_notyearinfo_applyno |  | fapplyno |
| 4 | pk_src_notyearinfo |  | fentryid |
