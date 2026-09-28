# 成本核算对象-cad_costobjectf7

## 成本核算对象-主表 t_cad_costobject

- **表名称：** 成本核算对象-主表
- **表名：** t_cad_costobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcostobjectruleid | 成本核算对象规则 | int8 | 64 |  | √ | 0 | [成本核算对象规则 cad_costobjectrule](../aca_files/cad_costobjectrule.md) |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 7 | fproducenum | 生产编号 | varchar | 50 |  | √ | ' ' | 生产编号 |
| 8 | fprocessnumber | 工序号 | int8 | 64 |  | √ | 0 | 工序号 |
| 9 | fbillno | 成本核算对象编码 | varchar | 510 |  | √ | ' ' | 成本核算对象编码 |
| 10 | fsrcbillnumber | 源单单号 | varchar | 255 |  | √ | ' ' | 源单单号 |
| 11 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 12 | fmainproobjid | 主产品成本核算对象 | int8 | 64 |  | √ | 0 | 主产品成本核算对象 |
| 13 | fname | fname | varchar | 510 |  | √ | ' ' |  |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :提交 C :审核 |
| 15 | fbatchno | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 16 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 17 | fprobillid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录ID |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 19 | frule | 核算规则 | varchar | 30 |  | √ | ' ' | 核算规则,枚举: SN :源单单号+源单行号 PN :产品+生产编号 CP :产品 RULE_SW :源单单号+源单行号+项目号 RULE_SP :项目号 RULE_CU :产品+生产线 |
| 20 | fisenabledsfc | 是否工序 | bpchar | 1 |  | √ | '0' | 是否工序 |
| 21 | fsotype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: PB :工单/委外工单 SB :生产编号 SOTYPE_SW :检修工单 SOTYPE_SP :项目 SOTYPE_ARMIN :重复生产完工入库单 |
| 22 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 23 | fpno | fpno | int8 | 64 |  | √ | 0 |  |
| 24 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 27 | foriginype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: MANUAL :手工录入 API :API EXCEL :列表引入 RULE :规则引入 |
| 28 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fproplanid | 工序计划号 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 30 | fprocesssequence | 工序序列 | int8 | 64 |  | √ | 0 | 工序序列 |
| 31 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | [产品组 cad_productintogroup](../aca_files/cad_productintogroup.md) |
| 33 | fbizstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :未结算 B :已结算 |
| 34 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 35 | fbiztype | 成本计算方法 | varchar | 30 |  | √ | ' ' | 成本计算方法,枚举: RO :工单成本 SO :分批法 PZ :品种法 FL :分类法 SW :服务工单 SP :服务项目 CU :生产线成本 DIY :自定义 |
| 36 | fweight | 分配权重 | numeric | 23 | 10 | √ | 0.0000000000 | 分配权重 |
| 37 | fisoutsource | 委外 | bpchar | 1 |  | √ | '0' | 委外 |
| 38 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 39 | fprocesscode | 工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 40 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 41 | fsettleaccounttime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 42 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 43 | fprdline | fprdline | int8 | 64 |  | √ | 0 |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fprojectnumberid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 47 | fcostcalcdimension | fcostcalcdimension | int8 | 64 |  | √ | 0 |  |
| 48 | fsrcbillrow | 源单行号 | int8 | 64 |  | √ | 0 | 源单行号 |
| 49 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 50 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 51 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 52 | fcollconfigid | fcollconfigid | int8 | 64 |  | √ | 0 |  |
| 53 | fmodelnum | 规格型号 | varchar | 510 |  | √ | ' ' | 规格型号 |
| 54 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cad_costobject2 |  | fbillno |
| 2 | idx_costobj_costc |  | fcostcenterid |
| 3 | idx_costobj_isoutsource |  | fisoutsource |
| 4 | idx_costobj_matpronum |  | fmaterialid |
| 5 | idx_costobj_contrack |  | ftracknumberid,fconfiguredcodeid |
| 6 | index_cad_costobject |  | forgid,fcostcenterid,fmaterialid,fprobillid |
| 7 | t_cad_costobject_pkey |  | fid |
| 8 | idx_costobj_srcidentry |  | fprobillid |

---

## 成本核算对象-多语言表 t_cad_costobject_l

- **表名称：** 成本核算对象-多语言表
- **表名：** t_cad_costobject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fname | 成本核算对象名称 | varchar | 510 |  | √ | ' ' | 成本核算对象名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 6 | fmodelnum | 规格型号 | varchar | 510 |  | √ | ' ' | 规格型号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_costobject_l |  | fid,flocaleid |
| 2 | t_cad_costobject_l_pkey |  | fpkid |
