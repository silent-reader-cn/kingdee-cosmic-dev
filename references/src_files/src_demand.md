# 项目立项-src_demand

## 关联子实体-子表 t_src_demand_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_demand_lk

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
| 1 | idx_src_demand_lk_fk |  | fid |
| 2 | pk_src_demand_lk |  | fpkid |

---

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

## 项目立项-分表 t_src_demand_a

- **表名称：** 项目立项-分表
- **表名：** t_src_demand_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecidelink | 会议决策申请链接 | varchar | 100 |  | √ | ' ' | 会议决策申请链接 |
| 3 | fdecstatus | 关联会议决策单状态 | bpchar | 1 |  | √ | ' ' | 关联会议决策单状态,枚举: A :未关联 B :已上报 C :已关联 |
| 4 | fdecisionid | 采委会决策单号 | int8 | 64 |  | √ | 0 | 采委会决策单号 src_decisionbillnotwo |
| 5 | fistemppush | 临时下推 | bpchar | 1 |  | √ | '0' | 临时下推 |
| 6 | fdecidenumber | 会议决策单号 | varchar | 50 |  | √ | ' ' | 会议决策单号 |
| 7 | fresultstatus | 决议状态 | bpchar | 1 |  | √ | ' ' | 决议状态,枚举: A :待评审 B :通过 C :不通过 D :有条件通过 |
| 8 | ftempreason | 临时下推原因 | varchar | 255 |  | √ | ' ' | 临时下推原因 |
| 9 | fconclusion | 会议决策结论 | varchar | 1000 |  | √ | ' ' | 会议决策结论 |
| 10 | fdecisiontype | 议题类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |

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

## 项目立项-多语言表 t_src_demand_l

- **表名称：** 项目立项-多语言表
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

## 项目立项-反写记录表 t_pur_demandmanage_wb

- **表名称：** 项目立项-反写记录表
- **表名：** t_pur_demandmanage_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_demandmanage_wb |  | fentryid |
| 2 | idx_pur_demandmanage_wb_fk |  | fid |

---

## 项目立项-关联追踪表 t_pur_demandmanage_tc

- **表名称：** 项目立项-关联追踪表
- **表名：** t_pur_demandmanage_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_demandmanage_tc_tbill |  | ftbillid |
| 2 | pk_pur_demandmanage_tc |  | fid |
| 3 | idx_pur_demandmanage_tc_tid |  | ftid |

---

## 采购组织-多选基础资料表 t_src_decisionsceneorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_decisionsceneorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisceneorg_eid |  | fentryid |
| 2 | pk_src_decisionsceneorg |  | fpkid |
| 3 | idx_src_decisceneorg_bid |  | fbasedataid |

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

## 品类-多选基础资料表 t_src_categorydecision

- **表名称：** 品类-多选基础资料表
- **表名：** t_src_categorydecision

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_categorydecision_fid |  | fentryid |
| 2 | idx_src_categorydecision_bid |  | fbasedataid |
| 3 | pk_src_categorydecision |  | fpkid |

---

## 报价单模板-多选基础资料表 t_src_purlisttpl

- **表名称：** 报价单模板-多选基础资料表
- **表名：** t_src_purlisttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlisttpl_bid |  | fbasedataid |
| 2 | idx_src_purlisttpl_eid |  | fentryid |
| 3 | pk_src_purlisttpl |  | fpkid |

---

## 寻源策略附件-附件表 t_src_decideattachment

- **表名称：** 寻源策略附件-附件表
- **表名：** t_src_decideattachment

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
| 1 | idx_src_decideattachment_bid |  | fbasedataid |
| 2 | pk_src_decideattachment |  | fpkid |
| 3 | idx_src_decideattachment_fid |  | fid |

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
| 14 | fprojectno | 寻源项目编号 | varchar | 50 |  | √ | ' ' | 寻源项目编号 |
| 15 | fdetailid | fdetailid | varchar | 50 |  | √ | ' ' |  |
| 16 | fbillno | 场景编号 | varchar | 100 |  | √ | ' ' | 场景编号 |
| 17 | fwinrule | fwinrule | int8 | 64 |  | √ | 0 |  |
| 18 | fisfunction | fisfunction | bpchar | 1 |  | √ | '0' |  |
| 19 | fprojectid | 寻源项目ID | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fbillno2 | fbillno2 | varchar | 50 |  | √ | ' ' |  |
| 22 | fwinerqty | fwinerqty | int8 | 64 |  | √ | 0 |  |
| 23 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 24 | fscenename_des | 寻源场景名称 | varchar | 100 |  | √ | ' ' | 寻源场景名称 |
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

## 关联子实体-子表 t_src_notyearinfo_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_notyearinfo_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_notyearinfo_lk |  | fpkid |
| 2 | idx_src_notyearinfo_lk_fk |  | fentryid |

---

## 项目立项-主表 t_src_demand

- **表名称：** 项目立项-主表
- **表名：** t_src_demand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisproject | fisproject | bpchar | 1 |  | √ | '0' |  |
| 3 | forgid | 采购组织(有效) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fplace | fplace | int8 | 64 |  | √ | 0 |  |
| 5 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 6 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsrcemotion | fsrcemotion | varchar | 30 |  | √ | ' ' |  |
| 9 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | ftitle | 项目名称 | varchar | 300 |  | √ | ' ' | 项目名称 |
| 11 | fwithvatamount | fwithvatamount | numeric | 23 | 10 | √ | 0 |  |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 13 | fdecisonlevelhide | fdecisonlevelhide | int8 | 64 |  | √ | 0 |  |
| 14 | fspecial | fspecial | varchar | 50 |  | √ | ' ' |  |
| 15 | fsumamount | fsumamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | flevelid | flevelid | int8 | 64 |  | √ | 0 |  |
| 17 | fsceneitem | 寻源场景关联标的 | bpchar | 1 |  | √ | ' ' | 寻源场景关联标的 |
| 18 | fsigningcycle | fsigningcycle | varchar | 50 |  | √ | ' ' |  |
| 19 | fbillno | 项目编号 | varchar | 60 |  | √ | ' ' | 项目编号 |
| 20 | fdecisonlevelld | fdecisonlevelld | int8 | 64 |  | √ | 0 |  |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已终止 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fisselloff | 是否变卖需求 | varchar | 30 |  | √ | '0' | 是否变卖需求,枚举: A :是 B :否 |
| 24 | fservicetype | fservicetype | int8 | 64 |  | √ | 0 |  |
| 25 | fdecisiontypeid | fdecisiontypeid | int8 | 64 |  | √ | 0 |  |
| 26 | fproject | fproject | varchar | 50 |  | √ | ' ' |  |
| 27 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 28 | fisproject2 | 下推方式 | bpchar | 1 |  | √ | '0' | 下推方式,枚举: 0 :按场景下推项目启动 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbusiarea | fbusiarea | int8 | 64 |  | √ | 0 |  |
| 31 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 32 | fdemandaffiliateid | fdemandaffiliateid | int8 | 64 |  | √ | 0 |  |
| 33 | famount | 预估未税金额 | numeric | 23 | 10 | √ | 0 | 预估未税金额 |
| 34 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 35 | fsurplusamount | 预估价税合计 | numeric | 23 | 10 | √ | 0 | 预估价税合计 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fnotreason | fnotreason | varchar | 100 |  | √ | ' ' |  |
| 38 | fismultiscene | 是否拆分多个寻源场景 | bpchar | 1 |  | √ | '1' | 是否拆分多个寻源场景 |
| 39 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 40 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 41 | fpurdecision | 会议决策 | bpchar | 1 |  | √ | ' ' | 会议决策 |
| 42 | ftaxtype | 价格录入方式 | bpchar | 1 |  | √ | '1' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fk_basedatafield | fk_basedatafield | int8 | 64 |  | √ | 0 |  |
| 45 | fbusitype | fbusitype | varchar | 30 |  | √ | ' ' |  |
| 46 | fchassisttype | fchassisttype | int8 | 64 |  | √ | 0 |  |
| 47 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | fcostattribution | fcostattribution | int8 | 64 |  | √ | 0 |  |
| 50 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 51 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 53 | fisspecial | fisspecial | bpchar | 1 |  | √ | '0' |  |
| 54 | fsumqty | 合计数量 | numeric | 23 | 10 | √ | 0 | 合计数量 |
| 55 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 56 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 57 | fpurchasetype | fpurchasetype | varchar | 30 |  | √ | ' ' |  |
| 58 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 59 | fsumtaxamount | fsumtaxamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | fsumtax | 合计税额 | numeric | 23 | 10 | √ | 0 | 合计税额 |
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

## 供应商分录-子表 t_src_demandsupplier

- **表名称：** 供应商分录-子表
- **表名：** t_src_demandsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispuragent | 代理投标/报价 | bpchar | 1 |  | √ | '0' | 代理投标/报价 |
| 3 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 4 | faddress | 地址 | varchar | 100 |  | √ | ' ' | 地址 |
| 5 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 6 | fisfeeagent | 代理缴费 | bpchar | 1 |  | √ | '0' | 代理缴费 |
| 7 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 12 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 13 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 14 | fsupname | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 15 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demandsupplier_fid |  | fid |
| 2 | pk_src_demandsupplier |  | fentryid |
| 3 | idx_src_demandsupplier_fpag |  | fpackageid |
| 4 | idx_src_demandsupplier_fsup |  | fsupplierid |

---

## 供应商-多选基础资料表 t_src_scene_supplier2

- **表名称：** 供应商-多选基础资料表
- **表名：** t_src_scene_supplier2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_scene_supplier2 |  | fpkid |
| 2 | idx_src_scene_supplier2_fid |  | fid |

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
| 6 | fiscontrolqty | 是否控制数量 | bpchar | 1 |  | √ | '1' | 是否控制数量 |
| 7 | farrivedate1 | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 8 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fprojectno1 | fprojectno1 | varchar | 50 |  | √ | ' ' |  |
| 12 | fentryrcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcheckboxfield1 | fcheckboxfield1 | bpchar | 1 |  | √ | ' ' |  |
| 14 | fk_sf_city | fk_sf_city | int8 | 64 |  | √ | 0 |  |
| 15 | fsrctypeid | 寻源流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 16 | flinenumber1 | flinenumber1 | varchar | 50 |  | √ | ' ' |  |
| 17 | fapplicationdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | frfqbillno | frfqbillno | varchar | 50 |  | √ | ' ' |  |
| 19 | fapplicationdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 20 | freqsource11 | 需求来源 | varchar | 30 |  | √ | ' ' | 需求来源,枚举: 2 :采购申请 3 :项目立项 4 :项目启动 |
| 21 | fmaterial1 | 标的编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fapplicantid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | findicate1 | findicate1 | varchar | 30 |  | √ | ' ' |  |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fprice3 | 最近含税交易单价 | numeric | 23 | 10 | √ | 0 | 最近含税交易单价 |
| 27 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 28 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 29 | freqqty2 | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 30 | fminiorderqty | 最小起订量 | numeric | 23 | 10 | √ | 0 | 最小起订量 |
| 31 | fmaterialname1 | 标的编码 | varchar | 100 |  | √ | ' ' | 标的编码 |
| 32 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 33 | fk_sf_companycode | fk_sf_companycode | int8 | 64 |  | √ | 0 |  |
| 34 | funit2 | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | freqdescribe | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 37 | frowtypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 38 | fprice2 | 最近未税交易单价 | numeric | 23 | 10 | √ | 0 | 最近未税交易单价 |
| 39 | fyearswitch | fyearswitch | bpchar | 1 |  | √ | ' ' |  |
| 40 | fmaterialname | 标的名称 | varchar | 255 |  | √ | ' ' | 标的名称 |
| 41 | freqorg1 | freqorg1 | int8 | 64 |  | √ | 0 |  |
| 42 | fentryamount | 未税金额 | numeric | 23 | 10 | √ | 0 | 未税金额 |
| 43 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 44 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 45 | ftaxamount2 | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 46 | fcontractline | fcontractline | int8 | 64 |  | √ | 0 |  |
| 47 | fk_sf_place | fk_sf_place | int8 | 64 |  | √ | 0 |  |
| 48 | fspecialreason | 标的描述 | varchar | 1024 |  |  | ' ' | 标的描述 |
| 49 | fmaterialmodel1 | 规格型号 | varchar | 1024 |  | √ | ' ' | 规格型号 |
| 50 | fprice | 预估未税单价 | numeric | 23 | 10 | √ | 0 | 预估未税单价 |
| 51 | fminipackqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 52 | fapplyno1 | fapplyno1 | varchar | 50 |  | √ | ' ' |  |
| 53 | ftaxprice1 | 预估含税单价 | numeric | 23 | 10 | √ | 0 | 预估含税单价 |
| 54 | fsceneid | 寻源场景 | int8 | 64 |  | √ | 0 | 项目寻源场景F7 src_demandscene |
| 55 | fcategory2 | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 56 | fspecialpurreason | fspecialpurreason | varchar | 50 |  | √ | ' ' |  |
| 57 | fcontractnold | fcontractnold | int8 | 64 |  | √ | 0 |  |
| 58 | fld | fld | varchar | 50 |  | √ | ' ' |  |
| 59 | fmaterial1code | fmaterial1code | varchar | 50 |  | √ | ' ' |  |
| 60 | fecpno | fecpno | varchar | 50 |  | √ | ' ' |  |
| 61 | fbdprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 62 | fmaterialgroup1 | fmaterialgroup1 | int8 | 64 |  | √ | 0 |  |
| 63 | freqtype1 | freqtype1 | int8 | 64 |  | √ | 0 |  |
| 64 | ftaxitemid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 65 | fentrystatus11 | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :暂存 B :未执行 C :已执行 D :已终止 |
| 66 | fqty1 | fqty1 | numeric | 23 | 10 | √ | 0 |  |
| 67 | fprojectname1 | fprojectname1 | varchar | 50 |  | √ | ' ' |  |
| 68 | fprice12 | 上次定标未税单价 | numeric | 23 | 10 | √ | 0 | 上次定标未税单价 |
| 69 | fprice13 | 上次定标含税单价 | numeric | 23 | 10 | √ | 0 | 上次定标含税单价 |
| 70 | fprice14 | 历史最优未税)单价 | numeric | 23 | 10 | √ | 0 | 历史最优未税)单价 |
| 71 | fprice15 | 历史最优含税单价 | numeric | 23 | 10 | √ | 0 | 历史最优含税单价 |
| 72 | fapplyno | fapplyno | varchar | 50 |  | √ | ' ' |  |
| 73 | fsuppliername1 | fsuppliername1 | varchar | 50 |  | √ | ' ' |  |
| 74 | fk_sf_busiarea | fk_sf_busiarea | int8 | 64 |  | √ | 0 |  |
| 75 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

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
