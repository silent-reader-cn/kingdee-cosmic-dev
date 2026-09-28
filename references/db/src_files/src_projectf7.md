# 招标项目F7-src_projectf7

## 关联子实体-子表 t_src_project_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_project_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_lk |  | fpkid |
| 2 | idx_src_project_lk_fk |  | fid |

---

## 采购组织(多选，废弃)-多选基础资料表 t_src_projectpurorg

- **表名称：** 采购组织(多选，废弃)-多选基础资料表
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

## 招标项目F7-主表 t_src_project

- **表名称：** 招标项目F7-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | 报名截止时间 | timestamp | 0 |  |  | null | 报名截止时间 |
| 4 | faptschemeid | 开资审标管控方案 | int8 | 64 |  | √ | 0 | [开标管控方案 src_openscheme](../src_files/src_openscheme.md) |
| 5 | fanswerdate | 答疑截止时间 | timestamp | 0 |  |  | null | 答疑截止时间 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsourceid | 项目立项 | int8 | 64 |  | √ | 0 | [项目立项查询 src_demandno](../src_files/src_demandno.md) |
| 8 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | 缴费截止时间 | timestamp | 0 |  |  | null | 缴费截止时间 |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | 评标方式 | bpchar | 1 |  | √ | ' ' | 评标方式,枚举: 1 :线上评标 2 :线下评标 |
| 14 | fsumamount | 定标未税总价 | numeric | 23 | 10 | √ | 0 | 定标未税总价 |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | 开商务标管控方案 | int8 | 64 |  | √ | 0 | [开标管控方案 src_openscheme](../src_files/src_openscheme.md) |
| 17 | ftendertype | 招标方式 | bpchar | 1 |  | √ | ' ' | 招标方式,枚举: 1 :邀请招标 2 :公开招标 |
| 18 | fbillno | 招标项目编号 | varchar | 30 |  | √ | ' ' | 招标项目编号 |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 21 | fsrcbillid | fsrcbillid | varchar | 50 |  | √ | ' ' |  |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | 中标供应商数量 | int8 | 64 |  | √ | 0 | 中标供应商数量 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | 开标技术管控方案 | int8 | 64 |  | √ | 0 | [开标管控方案 src_openscheme](../src_files/src_openscheme.md) |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | 节点名称 | varchar | 50 |  | √ | ' ' | 节点名称 |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | 投标截止时间 | timestamp | 0 |  |  | null | 投标截止时间 |
| 33 | fruleassess | 商务报价计算规则（评估） | bpchar | 1 |  | √ | ' ' | 商务报价计算规则（评估）,枚举: 1 :标的单价 2 :报价包的采购总金额 3 :报价包内所有产品的平均价 4 :其他 |
| 34 | fratio_syn | fratio_syn | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 36 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
| 37 | fbiderqty | 最低邀请供应商数量(中标原则) | int8 | 64 |  | √ | 0 | 最低邀请供应商数量(中标原则) |
| 38 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 39 | fisautoopen | fisautoopen | bpchar | 1 |  | √ | '0' |  |
| 40 | fisviepublish | 是否发布竞价 | bpchar | 1 |  | √ | '0' | 是否发布竞价 |
| 41 | ftieredtype | 阶梯报价方式 | bpchar | 1 |  | √ | '1' | 阶梯报价方式,枚举: 1 :不启用阶梯报价 2 :采购清单分录阶梯报价 3 :采购清单子表阶梯报价 |
| 42 | fdecidedate | 定标时间 | timestamp | 0 |  |  | null | 定标时间 |
| 43 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 44 | fwinruleid | 中标原则 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 45 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 46 | famount | 项目立项预估价税合计 | numeric | 23 | 10 | √ | 0 | 项目立项预估价税合计 |
| 47 | fsystype | fsystype | bpchar | 1 |  | √ | '1' |  |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | 寻源项目价税合计 | numeric | 23 | 10 | √ | 0 | 寻源项目价税合计 |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | 开标顺序 | bpchar | 1 |  | √ | ' ' | 开标顺序,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 9 :报价即开标(非密封报价) 4 :并行开技术标和商务标 |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 54 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 55 | fismultipackage | 是否多标段 | bpchar | 1 |  | √ | '0' | 是否多标段 |
| 56 | fishidesupplier | 评标时隐藏供应商名称 | bpchar | 1 |  | √ | '0' | 评标时隐藏供应商名称 |
| 57 | fsourceclassid | 招标方式类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 58 | fopenstatus | 开标情况 | bpchar | 1 |  | √ | '1' | 开标情况,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 59 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 3 :按标的 |
| 60 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 61 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |
| 62 | fterminalnode | fterminalnode | int8 | 64 |  | √ | 0 |  |
| 63 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | 是否按标段开标 | bpchar | 1 |  | √ | '0' | 是否按标段开标 |
| 66 | fisbidpublish | 是否发布招标 | bpchar | 1 |  | √ | '0' | 是否发布招标 |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | 预计开标时间 | timestamp | 0 |  |  | null | 预计开标时间 |
| 69 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | 是否启用开标管控 | bpchar | 1 |  | √ | '0' | 是否启用开标管控 |
| 73 | fisbypackage_apt | 是否按标段开资审标 | bpchar | 1 |  | √ | '0' | 是否按标段开资审标 |
| 74 | fsourcetypeid | 招标方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | 定标含税总价 | numeric | 23 | 10 | √ | 0 | 定标含税总价 |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 78 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 79 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 80 | fratiotype | 定标份额分配方式 | bpchar | 1 |  | √ | '1' | 定标份额分配方式,枚举: 1 :手工分配份额 2 :自动分配份额(按项目) 3 :自动分配份额(按标段) 4 :自动分配份额(按标的) 9 :不需要份额分配与控制 |

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

## 招标项目F7-分表 t_src_project_h

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 4 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 5 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 9 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 11 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | 发标时间 | timestamp | 0 |  |  | null | 发标时间 |
| 13 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 16 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_h_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_h |  | fid |

---

## 招标项目F7-分表 t_src_project_j

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_j

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 4 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 5 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 9 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 11 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fdocamount | 标书费 | numeric | 23 | 10 | √ | 0 | 标书费 |
| 16 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 17 | ffeewayid | 收费方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 18 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 19 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 20 | ffeeamount | 投标保证金 | numeric | 23 | 10 | √ | 0 | 投标保证金 |
| 21 | ffeeitemid | 收费项 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 22 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_j |  | fid |
| 2 | idx_src_project_j_fcreatorid |  | fcreatorid |

---

## 招标项目F7-分表 t_src_project_a

- **表名称：** 招标项目F7-分表
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
| 14 | fbillstatus | 项目启动单据状态 | bpchar | 1 |  | √ | ' ' | 项目启动单据状态,枚举: A :暂存 B :已提交 C :已审核 |
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
| 25 | fispaper | 是否有纸质标书 | bpchar | 1 |  | √ | '0' | 是否有纸质标书 |
| 26 | fbizstatus | 项目启动业务状态 | bpchar | 1 |  | √ | ' ' | 项目启动业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止 E :已废标 |
| 27 | fissplitdoc | 是否拆分标书 | bpchar | 1 |  | √ | '0' | 是否拆分标书 |
| 28 | freasonremark_tag | 其他独家谈判原因_详情 | text | 0 |  |  | null | 其他独家谈判原因_详情 |
| 29 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fsceneid | 场景 | int8 | 64 |  | √ | 0 | [采委会寻源场景F7(删除) src_decisionscene](../src_files/src_decisionscene.md) |
| 31 | faftertalkrule | faftertalkrule | varchar | 255 |  |  | ' ' |  |
| 32 | fpurdecision | 会议决策（是否上采委会） | bpchar | 1 |  | √ | '0' | 会议决策（是否上采委会） |
| 33 | fsolereason | 独家谈判原因 | bpchar | 1 |  | √ | ' ' | 独家谈判原因,枚举: 1 :供应商资源唯一 2 :合同续签 3 :合同内议价 4 :内部供应商采购 5 :顺丰客户指定供应商 9 :其他 |
| 34 | forderrule | forderrule | varchar | 255 |  | √ | ' ' |  |
| 35 | freasonremark | 其他独家谈判原因 | varchar | 255 |  | √ | ' ' | 其他独家谈判原因 |
| 36 | fopentypep | fopentypep | varchar | 50 |  | √ | ' ' |  |
| 37 | fdecisionbillno | 采委会决策单号 | varchar | 50 |  | √ | ' ' | 采委会决策单号 |
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
| 48 | fregionid | 所属区域 | int8 | 64 |  | √ | 0 | [区域分组 src_region](../src_files/src_region.md) |
| 49 | fisspecial | 是否特采 | bpchar | 1 |  | √ | '0' | 是否特采 |
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

## 招标项目F7-分表 t_src_project_b

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftendersideld | 招标方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourceamount | 项目立项预估未税金额 | numeric | 23 | 10 | √ | 0 | 项目立项预估未税金额 |
| 4 | fsceneamount | 寻源项目未税金额 | numeric | 23 | 10 | √ | 0 | 寻源项目未税金额 |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: A :流程外包 B :业务外包 C :灵活派遣 D :灵活派遣(集中) |
| 8 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 12 | ffieldnum | ffieldnum | int8 | 64 |  | √ | 0 |  |
| 13 | fisitemsupplier | fisitemsupplier | bpchar | 1 |  | √ | '0' |  |
| 14 | fisadd | 是否允许供应商新增标的 | bpchar | 1 |  | √ | '0' | 是否允许供应商新增标的 |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 18 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 19 | ftemplateid | 采购清单模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 26 | fservicetype | fservicetype | int8 | 64 |  | √ | 0 |  |
| 27 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 28 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 29 | fchassistype | 底盘类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 30 | fissourcesupplier | fissourcesupplier | bpchar | 1 |  | √ | '0' |  |
| 31 | fstandprice | fstandprice | numeric | 23 | 10 | √ | 0 |  |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 34 | fbusiarea | fbusiarea | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_b_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_b |  | fid |

---

## 招标项目F7-分表 t_src_project_y

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_y

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 4 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 5 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 9 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 11 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 14 | ffileschemeid | 归档方案 | int8 | 64 |  | √ | 0 | [归档方案 pds_filescheme](../pds_files/pds_filescheme.md) |
| 15 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 16 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 17 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 18 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fisarchived | fisarchived | bpchar | 1 |  | √ | '0' |  |
| 22 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_y |  | fid |
| 2 | idx_src_project_y_fcreatorid |  | fcreatorid |

---

## 招标项目F7-分表 t_src_project_x

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 4 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 5 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatetime | 签约单创建时间 | timestamp | 0 |  |  | null | 签约单创建时间 |
| 9 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 11 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 16 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_project_x |  | fid |
| 2 | idx_src_project_x_fcreatorid |  | fcreatorid |

---

## 招标项目F7-分表 t_src_project_t

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecisionsumid | fdecisionsumid | int8 | 64 |  | √ | 0 |  |
| 3 | fpurassessid | fpurassessid | int8 | 64 |  | √ | 0 |  |
| 4 | fistemppush | fistemppush | bpchar | 1 |  | √ | '0' |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fiscreatpur | fiscreatpur | bpchar | 1 |  | √ | '0' |  |
| 8 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
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
| 23 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 24 | fpricebiztype | fpricebiztype | int8 | 64 |  | √ | 0 |  |
| 25 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fdecstatus | fdecstatus | bpchar | 1 |  | √ | ' ' |  |
| 28 | ffluctuateamount | ffluctuateamount | varchar | 50 |  | √ | ' ' |  |
| 29 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 30 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fconclusion | fconclusion | varchar | 1000 |  | √ | ' ' |  |
| 33 | fdecisiontype | fdecisiontype | int8 | 64 |  | √ | 0 |  |
| 34 | fwintime | fwintime | timestamp | 0 |  |  | null |  |
| 35 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 36 | fcfmstatus | 定标确认状态 | bpchar | 1 |  | √ | ' ' | 定标确认状态,枚举: A :待确认 B :已确认 |
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

## 招标项目F7-分表 t_src_project_q

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispkgscheme | fispkgscheme | bpchar | 1 |  | √ | '0' |  |
| 3 | fismanualscore | 线下评商务分后，手工录入系统 | bpchar | 1 |  | √ | '0' | 线下评商务分后，手工录入系统 |
| 4 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fschemeid | 推荐方案 | int8 | 64 |  | √ | 0 | [推荐方案 src_pattern](../src_files/src_pattern.md) |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fnegschemeid | 议价管控方案 | int8 | 64 |  | √ | 0 | [议价管控方案 src_negscheme](../src_files/src_negscheme.md) |
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
| 23 | fbasescore | fbasescore | numeric | 23 | 10 | √ | 0 |  |
| 24 | fminscore | fminscore | numeric | 23 | 10 | √ | 0 |  |
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

## 招标项目F7-分表 t_src_project_r

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 4 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 5 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 6 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 7 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 8 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 9 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 10 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 11 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 14 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 15 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 16 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 17 | fsuppliertype | 资审供应商来源 | bpchar | 1 |  | √ | ' ' | 资审供应商来源,枚举: 1 :报名供应商 2 :邀请供应商 3 :回标供应商 |
| 18 | faptitudetype | 资审方式 | bpchar | 1 |  | √ | ' ' | 资审方式,枚举: |
| 19 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 20 | faptitudedate | 资审截止时间 | timestamp | 0 |  |  | null | 资审截止时间 |
| 21 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_r_fcreatorid |  | fcreatorid |
| 2 | pk_src_project_r |  | fid |

---

## 招标项目F7-多语言表 t_src_project_l

- **表名称：** 招标项目F7-多语言表
- **表名：** t_src_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | fnodename | varchar | 100 |  | √ | ' ' |  |
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

## 招标项目F7-分表 t_src_project_o

- **表名称：** 招标项目F7-分表
- **表名：** t_src_project_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidstatus | 竞价状态 | bpchar | 1 |  | √ | ' ' | 竞价状态,枚举: |
| 3 | frankprice | frankprice | varchar | 30 |  | √ | ' ' |  |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fcashdeposit | fcashdeposit | numeric | 23 | 10 | √ | 0 |  |
| 6 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 7 | fchecktype | fchecktype | bpchar | 1 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fplanopendate | 预计竞价开始时间 | timestamp | 0 |  |  | null | 预计竞价开始时间 |
| 10 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 11 | frankamount | frankamount | varchar | 30 |  | √ | ' ' |  |
| 12 | faddtime | faddtime | int8 | 64 |  | √ | 0 |  |
| 13 | fbidtime | fbidtime | int8 | 64 |  | √ | 0 |  |
| 14 | flasttime | flasttime | int8 | 64 |  | √ | 0 |  |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fviepattern | 竞价模式 | bpchar | 1 |  | √ | ' ' | 竞价模式,枚举: 1 :按单价竞价 2 :按比率竞价 3 :按价差竞价 |
| 17 | fresultdate | fresultdate | timestamp | 0 |  |  | null |  |
| 18 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 20 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 21 | friskinfo | friskinfo | varchar | 2000 |  | √ | ' ' |  |
| 22 | faddtimecount | faddtimecount | int4 | 32 |  | √ | 0 |  |
| 23 | fbidcount | fbidcount | int8 | 64 |  | √ | 0 |  |
| 24 | fbidrestoftime | fbidrestoftime | int8 | 64 |  | √ | 0 |  |
| 25 | ftendency | 多轮议价报价趋势 | bpchar | 1 |  | √ | ' ' | 多轮议价报价趋势,枚举: 1 :只允许降价 2 :只允许加价 3 :允许加价或降价 |
| 26 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 27 | fmonthnum | fmonthnum | int4 | 32 |  | √ | 0 |  |
| 28 | fisregioncontrol | 多轮竞价时进行竞价区间控制 | bpchar | 1 |  | √ | ' ' | 多轮竞价时进行竞价区间控制,枚举: 1 :进行竞价区间控制 2 :不进行竞价区间控制 |
| 29 | freducetype | freducetype | bpchar | 1 |  | √ | ' ' |  |
| 30 | flastquotedate | flastquotedate | timestamp | 0 |  |  | null |  |
| 31 | fstopbiddate | fstopbiddate | timestamp | 0 |  |  | null |  |
| 32 | fisnewprice | fisnewprice | bpchar | 1 |  | √ | '0' |  |
| 33 | fenrolldate | fenrolldate | timestamp | 0 |  |  | null |  |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 36 | fisbizscore | 评委通过评标助手评商务分(线上评分) | bpchar | 1 |  | √ | '0' | 评委通过评标助手评商务分(线上评分) |
| 37 | fisdiscarded | fisdiscarded | bpchar | 1 |  | √ | '0' |  |
| 38 | fisnoderank | fisnoderank | bpchar | 1 |  | √ | '0' |  |
| 39 | fmaxamount | fmaxamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 41 | famount | famount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fisautoviebyplan | fisautoviebyplan | bpchar | 1 |  | √ | '0' |  |
| 43 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
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
| 54 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 55 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 56 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 57 | fvie_purlist | fvie_purlist | bpchar | 1 |  | √ | ' ' |  |
| 58 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 59 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 60 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 61 | fminamount | fminamount | numeric | 23 | 10 | √ | 0 |  |
| 62 | faddtimenum | faddtimenum | int4 | 32 |  | √ | 0 |  |
| 63 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 64 | fvietype | 竞价类型 | bpchar | 1 |  | √ | ' ' | 竞价类型,枚举: A :降价(反向拍卖) B :加价(正向拍卖) |
| 65 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 66 | fdelaytime | fdelaytime | int8 | 64 |  | √ | 0 |  |
| 67 | fbidnumber | 竞价最低参与供应商数量(竞价规则) | int8 | 64 |  | √ | 0 | 竞价最低参与供应商数量(竞价规则) |
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
