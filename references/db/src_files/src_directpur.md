# 紧急采购-src_directpur

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

## 关联子实体-子表 t_src_directattach_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_directattach_lk

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
| 1 | pk_src_directattach_lk |  | fpkid |
| 2 | idx_src_directattach_lk_fk |  | fentryid |

---

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

## 紧急采购-关联追踪表 t_src_project_tc

- **表名称：** 紧急采购-关联追踪表
- **表名：** t_src_project_tc

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
| 1 | pk_src_project_tc |  | fid |
| 2 | idx_src_project_tc_tid |  | ftid |
| 3 | idx_src_project_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_src_projectnode_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_projectnode_lk

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
| 1 | pk_src_projectnode_lk |  | fpkid |
| 2 | idx_src_projectnode_lk_fk |  | fentryid |

---

## 文件附件-附件表 t_src_directattach_fj

- **表名称：** 文件附件-附件表
- **表名：** t_src_directattach_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_directattach_fj_feid |  | fentryid |
| 2 | idx_src_directattach_fj_bid |  | fbasedataid |
| 3 | pk_src_directattach_fj |  | fpkid |

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

## 关联子实体-子表 t_src_projectnodesub_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_projectnodesub_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projectnodesub_lk_fk |  | fdetailid |
| 2 | pk_src_projectnodesub_lk |  | fpkid |

---

## 紧急采购-主表 t_src_project

- **表名称：** 紧急采购-主表
- **表名：** t_src_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplanschemeid | fplanschemeid | int8 | 64 |  | √ | 0 |  |
| 3 | freplydate | freplydate | timestamp | 0 |  |  | null |  |
| 4 | faptschemeid | faptschemeid | int8 | 64 |  | √ | 0 |  |
| 5 | fanswerdate | fanswerdate | timestamp | 0 |  |  | null |  |
| 6 | forgid | 采购组织(后台) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsourceid | 项目编号 | int8 | 64 |  | √ | 0 | [项目立项查询 src_demandno](../src_files/src_demandno.md) |
| 8 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 9 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 10 | ffeewayid | ffeewayid | int8 | 64 |  | √ | 0 |  |
| 11 | fpayenddate | fpayenddate | timestamp | 0 |  |  | null |  |
| 12 | forigin | forigin | varchar | 30 |  | √ | ' ' |  |
| 13 | fscoretype | fscoretype | bpchar | 1 |  | √ | ' ' |  |
| 14 | fsumamount | 未税总价 | numeric | 23 | 10 | √ | 0 | 未税总价 |
| 15 | fisbyproject | fisbyproject | bpchar | 1 |  | √ | '0' |  |
| 16 | fbizschemeid | fbizschemeid | int8 | 64 |  | √ | 0 |  |
| 17 | ftendertype | ftendertype | bpchar | 1 |  | √ | ' ' |  |
| 18 | fbillno | 招标项目编号 | varchar | 30 |  | √ | ' ' | 招标项目编号 |
| 19 | fratio_oth | fratio_oth | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 21 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 22 | ftodotask | ftodotask | varchar | 255 |  | √ | ' ' |  |
| 23 | falterqty | falterqty | int8 | 64 |  | √ | 0 |  |
| 24 | fbidcount | fbidcount | int4 | 32 |  | √ | 0 |  |
| 25 | fwinerqty | 中标供应商数量 | int8 | 64 |  | √ | 0 | 中标供应商数量 |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | ftecschemeid | ftecschemeid | int8 | 64 |  | √ | 0 |  |
| 28 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 29 | fnodename | 当前节点名称 | varchar | 50 |  | √ | ' ' | 当前节点名称 |
| 30 | fscoremethod | fscoremethod | bpchar | 1 |  | √ | ' ' |  |
| 31 | fsendtendertime | fsendtendertime | timestamp | 0 |  |  | null |  |
| 32 | fstopbiddate | 截标时间 | timestamp | 0 |  |  | null | 截标时间 |
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
| 43 | fbilldate | 采购时间 | timestamp | 0 |  |  | null | 采购时间 |
| 44 | fwinruleid | 中标原则 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 45 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 46 | famount | 预估采购总金额(未税) | numeric | 23 | 10 | √ | 0 | 预估采购总金额(未税) |
| 47 | fsystype | 来源类型 | bpchar | 1 |  | √ | '1' | 来源类型,枚举: 1 :项目启动 2 :手工新增 3 :外部系统 |
| 48 | fisaptitude | fisaptitude | bpchar | 1 |  | √ | '0' |  |
| 49 | fsurplusamount | fsurplusamount | numeric | 23 | 10 | √ | 0 |  |
| 50 | fsupopentype | fsupopentype | bpchar | 1 |  | √ | '1' |  |
| 51 | fopentype | 开标顺序 | bpchar | 1 |  | √ | ' ' | 开标顺序,枚举: 1 :同时开技术标和商务标 2 :先开评技术标，后开商务标 |
| 52 | fclosetask | fclosetask | varchar | 255 |  | √ | ' ' |  |
| 53 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 54 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 55 | fismultipackage | 是否多标段 | bpchar | 1 |  | √ | '0' | 是否多标段 |
| 56 | fishidesupplier | fishidesupplier | bpchar | 1 |  | √ | '0' |  |
| 57 | fsourceclassid | 寻源方式类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 58 | fopenstatus | 开标状态 | bpchar | 1 |  | √ | '1' | 开标状态,枚举: 1 :待开标 2 :已开技术标 3 :已开商务标 4 :已开标 5 :议价中 9 :已定标 A :已归档 B :已终止 |
| 59 | fmanagetype | 管理方式 | bpchar | 1 |  | √ | ' ' | 管理方式,枚举: 1 :按项目 2 :按标段 |
| 60 | ftaxtype | 价格录入方式 | varchar | 30 |  | √ | ' ' | 价格录入方式,枚举: 1 :录入含税价 2 :录入未税价 3 :价内税(含税) |
| 61 | fbidname | 招标项目名称 | varchar | 300 |  | √ | ' ' | 招标项目名称 |
| 62 | fterminalnode | 终止节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 63 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 64 | fdonetask | fdonetask | varchar | 255 |  | √ | ' ' |  |
| 65 | fisbypackage | fisbypackage | bpchar | 1 |  | √ | '0' |  |
| 66 | fisbidpublish | fisbidpublish | bpchar | 1 |  | √ | '0' |  |
| 67 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 68 | fopendate | fopendate | timestamp | 0 |  |  | null |  |
| 69 | fdecisiontype | 决标方式 | bpchar | 1 |  | √ | ' ' | 决标方式,枚举: 1 :按单价决标 2 :按金额决标 |
| 70 | fratio_biz | fratio_biz | numeric | 23 | 10 | √ | 0 |  |
| 71 | fratio_tec | fratio_tec | numeric | 23 | 10 | √ | 0 |  |
| 72 | fisopencontrol | fisopencontrol | bpchar | 1 |  | √ | '0' |  |
| 73 | fisbypackage_apt | fisbypackage_apt | bpchar | 1 |  | √ | '0' |  |
| 74 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 75 | fsumtaxamount | 定标含税总价 | numeric | 23 | 10 | √ | 0 | 定标含税总价 |
| 76 | fextfilterid | fextfilterid | int8 | 64 |  | √ | 0 |  |
| 77 | fcurrentnode | 当前节点 | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
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

## 附件分录-子表 t_src_directattach

- **表名称：** 附件分录-子表
- **表名：** t_src_directattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilename | 文件名称 | varchar | 512 |  |  | ' ' | 文件名称 |
| 3 | ffiletype | 文件类型 | bpchar | 1 |  | √ | ' ' | 文件类型,枚举: 1 :发票/送货单/报价单 2 :需求说明 3 :其他附件 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_directattach_fid |  | fid |
| 2 | pk_src_directattach |  | fentryid |

---

## 紧急采购-分表 t_src_project_j

- **表名称：** 紧急采购-分表
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
| 15 | fdocamount | fdocamount | numeric | 23 | 10 | √ | 0 |  |
| 16 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 17 | ffeewayid | 收费方式 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 18 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 19 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 20 | ffeeamount | ffeeamount | numeric | 23 | 10 | √ | 0 |  |
| 21 | ffeeitemid | ffeeitemid | int8 | 64 |  | √ | 0 |  |
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

## 紧急采购-分表 t_src_project_a

- **表名称：** 紧急采购-分表
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
| 17 | fisendnotice | 已发布流标公告 | bpchar | 1 |  | √ | '0' | 已发布流标公告 |
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
| 30 | fsceneid | 寻源场景名称 | int8 | 64 |  | √ | 0 | [寻源场景F7 src_demandscene](../src_files/src_demandscene.md) |
| 31 | faftertalkrule | faftertalkrule | varchar | 255 |  |  | ' ' |  |
| 32 | fpurdecision | fpurdecision | bpchar | 1 |  | √ | '0' |  |
| 33 | fsolereason | fsolereason | bpchar | 1 |  | √ | ' ' |  |
| 34 | forderrule | 订单分配原则 | varchar | 255 |  | √ | ' ' | 订单分配原则 |
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

## 紧急采购-分表 t_src_project_b

- **表名称：** 紧急采购-分表
- **表名：** t_src_project_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftendersideld | 招标方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsourceamount | fsourceamount | numeric | 23 | 10 | √ | 0 |  |
| 4 | fsceneamount | 寻源项目金额（未税） | numeric | 23 | 10 | √ | 0 | 寻源项目金额（未税） |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fbusinesstype | fbusinesstype | varchar | 30 |  | √ | ' ' |  |
| 8 | funauditdate | funauditdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fisdiscardbid | fisdiscardbid | bpchar | 1 |  | √ | '0' |  |
| 12 | ffieldnum | ffieldnum | int8 | 64 |  | √ | 0 |  |
| 13 | fisitemsupplier | fisitemsupplier | bpchar | 1 |  | √ | '0' |  |
| 14 | fisadd | fisadd | bpchar | 1 |  | √ | '0' |  |
| 15 | funauditorid | funauditorid | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | funsubmitterid | funsubmitterid | int8 | 64 |  | √ | 0 |  |
| 18 | funsubmitdate | funsubmitdate | timestamp | 0 |  |  | null |  |
| 19 | ftemplateid | ftemplateid | int8 | 64 |  | √ | 0 |  |
| 20 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 21 | fsubmitterid | fsubmitterid | int8 | 64 |  | √ | 0 |  |
| 22 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 23 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fregionid | fregionid | int8 | 64 |  | √ | 0 |  |
| 26 | fservicetype | fservicetype | int8 | 64 |  | √ | 0 |  |
| 27 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 28 | fsubmitdate | fsubmitdate | timestamp | 0 |  |  | null |  |
| 29 | fchassistype | fchassistype | int8 | 64 |  | √ | 0 |  |
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

## 紧急采购-分表 t_src_project_t

- **表名称：** 紧急采购-分表
- **表名：** t_src_project_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdecisionsumid | fdecisionsumid | int8 | 64 |  | √ | 0 |  |
| 3 | fpurassessid | fpurassessid | int8 | 64 |  | √ | 0 |  |
| 4 | fistemppush | fistemppush | bpchar | 1 |  | √ | '0' |  |
| 5 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :待定标 B :定商定价 C :定商定价已审核 D :已终止/流标 E :已废标 Z :无需处理 N :项目失效 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fiscreatpur | fiscreatpur | bpchar | 1 |  | √ | '0' |  |
| 8 | funauditdate | 反审核时间 | timestamp | 0 |  |  | null | 反审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fisneedinvite2 | 预中标函状态 | bpchar | 1 |  | √ | ' ' | 预中标函状态,枚举: 1 :待发送 2 :已发送 |
| 12 | fiswinnotice | 已发布中标公告 | bpchar | 1 |  | √ | '0' | 已发布中标公告 |
| 13 | fpriceeffect | fpriceeffect | timestamp | 0 |  |  | null |  |
| 14 | fresultstatus | fresultstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | funauditorid | 反审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fisdecisionresult | 关联会议决策 | bpchar | 1 |  | √ | '0' | 关联会议决策 |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fisedited | 需要综合计算 | bpchar | 1 |  | √ | '0' | 需要综合计算 |
| 20 | funsubmitterid | 撤销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | funsubmitdate | 撤销时间 | timestamp | 0 |  |  | null | 撤销时间 |
| 22 | ftemplateid | 采购清单模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 23 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fpricebiztype | fpricebiztype | int8 | 64 |  | √ | 0 |  |
| 25 | fsubmitterid | 提交人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdecstatus | fdecstatus | bpchar | 1 |  | √ | ' ' |  |
| 28 | ffluctuateamount | 上涨/下降金额(含税/元) | varchar | 50 |  | √ | ' ' | 上涨/下降金额(含税/元) |
| 29 | fisendnotice | fisendnotice | bpchar | 1 |  | √ | '0' |  |
| 30 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fconclusion | fconclusion | varchar | 1000 |  | √ | ' ' |  |
| 33 | fdecisiontype | fdecisiontype | int8 | 64 |  | √ | 0 |  |
| 34 | fwintime | fwintime | timestamp | 0 |  |  | null |  |
| 35 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 36 | fcfmstatus | 报价锁定状态 | bpchar | 1 |  | √ | ' ' | 报价锁定状态,枚举: A :未锁定 B :已锁定 |
| 37 | fdecidelink | fdecidelink | varchar | 100 |  | √ | ' ' |  |
| 38 | fsubmitdate | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 39 | fcomnum | fcomnum | int8 | 64 |  | √ | 0 |  |
| 40 | fchassistype | fchassistype | int8 | 64 |  | √ | 0 |  |
| 41 | fpurtype | 采购类型 | varchar | 30 |  | √ | ' ' | 采购类型,枚举: A :商超采购 B :小金额采购（非网购） C :小金额采购（网购） D :无需三家比价（分采） |
| 42 | fpurreport | 采购报告单号 | varchar | 30 |  | √ | ' ' | 采购报告单号 |
| 43 | fdecidenumber | fdecidenumber | varchar | 50 |  | √ | ' ' |  |
| 44 | ftempreason | ftempreason | varchar | 255 |  | √ | ' ' |  |
| 45 | fisneedinvite | 中标函状态 | bpchar | 1 |  | √ | ' ' | 中标函状态,枚举: 1 :待发送 2 :已发送 |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fapprovaltype | 审批方式 | varchar | 30 |  | √ | ' ' | 审批方式,枚举: 1 :采购评审 2 :合同评审 |

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

## 紧急采购-分表 t_src_project_q

- **表名称：** 紧急采购-分表
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

## 紧急采购-多语言表 t_src_project_l

- **表名称：** 紧急采购-多语言表
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

## 紧急采购-反写记录表 t_src_project_wb

- **表名称：** 紧急采购-反写记录表
- **表名：** t_src_project_wb

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
| 1 | idx_src_project_wb_fk |  | fid |
| 2 | pk_src_project_wb |  | fentryid |

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

---

## 当前有效评委-多选基础资料表 t_src_allscorers

- **表名称：** 当前有效评委-多选基础资料表
- **表名：** t_src_allscorers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_allscorers_fid |  | fid |
| 2 | pk_src_allscorers |  | fpkid |
| 3 | idx_src_allscorers_bid |  | fbasedataid |

---

## 关联子实体-子表 t_src_projecttpl_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_projecttpl_lk

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
| 1 | pk_src_projecttpl_lk |  | fpkid |
| 2 | idx_src_projecttpl_lk_fk |  | fentryid |
