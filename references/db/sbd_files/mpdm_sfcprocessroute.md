# 工艺路线-mpdm_sfcprocessroute

## 工序明细-子表 t_bd_processentry

- **表名称：** 工序明细-子表
- **表名：** t_bd_processentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 工序序列 | int8 | 64 |  | √ | 0 | 工序序列 |
| 3 | freworksection | 返工工序段 | varchar | 1000 |  | √ | ' ' | 返工工序段 |
| 4 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: A :团队作业 B :个人作业 |
| 5 | frelationid | 工序ID，本单唯一，用于与左树、转入/转出工序关联的ID | int8 | 64 |  | √ | 0 | 工序ID，本单唯一，用于与左树、转入/转出工序关联的ID |
| 6 | ftransinrelationids | 转入工序relationid | varchar | 500 |  | √ | ' ' | 转入工序relationid |
| 7 | fislastprocess | 末序 | bpchar | 1 |  | √ | '0' | 末序 |
| 8 | fprocesscontrolcode | 工序控制码 | int8 | 64 |  | √ | 0 | [工序控制码 mpdm_processcontrolcode](../mpdm_files/mpdm_processcontrolcode.md) |
| 9 | fsequencetype | 序列类型 | bpchar | 1 |  | √ | ' ' | 序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 10 | fupprocessid | （废弃）下工序id | varchar | 1000 |  | √ | ' ' | （废弃）下工序id |
| 11 | fsourceentryid | 来源分录ID（同步数据来源分录ID） | int8 | 64 |  | √ | 0 | 来源分录ID（同步数据来源分录ID） |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | fgroupnumber | fgroupnumber | int8 | 64 |  | √ | 0 |  |
| 14 | fheadunitfield | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fprocessinstructions | 工序说明 | varchar | 512 |  |  | ' ' | 工序说明 |
| 16 | fupprocesstype | （废弃）上工序类型 | varchar | 30 |  |  | ' ' | （废弃）上工序类型,枚举: A :单个 B :多个 C :群组 |
| 17 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | '0' | 首序 |
| 18 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 19 | fprocessqtyfield | （废弃）工序数量 | numeric | 23 | 10 |  | null | （废弃）工序数量 |
| 20 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fprocessnumber | 工序号 | int8 | 64 |  | √ | 0 | 工序号 |
| 22 | fprocessunitfield | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fbaseqtyfield | 基本批量 | numeric | 23 | 10 |  | null | 基本批量 |
| 24 | fsequenceremark | 序列备注 | varchar | 512 |  | √ | ' ' | 序列备注 |
| 25 | fnextprocessid | （废弃）上工序id | varchar | 1000 |  | √ | ' ' | （废弃）上工序id |
| 26 | ftransoutrelationids | 转出工序relationid | varchar | 500 |  | √ | ' ' | 转出工序relationid |
| 27 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fplmprocessid | plm工序ID（用于查找PLM作业指导书） | int8 | 64 |  | √ | 0 | plm工序ID（用于查找PLM作业指导书） |
| 29 | freworksequence | 返工来源序列 | int8 | 64 |  | √ | 0 | 返工来源序列 |
| 30 | fismilestone | （废弃）里程碑 | bpchar | 1 |  | √ | '0' | （废弃）里程碑 |
| 31 | freportdownlimit | （废弃）汇报下限允差（%） | numeric | 23 | 10 |  | null | （废弃）汇报下限允差（%） |
| 32 | fismainprocess | （废弃）主工序 | bpchar | 1 |  | √ | '1' | （废弃）主工序 |
| 33 | fpromethod | 加工类型 | varchar | 10 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 34 | fiskeyprocess | 关键工序 | bpchar | 1 |  | √ | '0' | 关键工序 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 37 | freportupperlimit | （废弃）汇报上限允差（%） | numeric | 23 | 10 |  | null | （废弃）汇报上限允差（%） |
| 38 | fgrouptype | fgrouptype | varchar | 30 |  | √ | ' ' |  |
| 39 | freworkprocesses | 返工来源工序 | int8 | 64 |  | √ | 0 | 返工来源工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processentry |  | fentryid |
| 2 | idx_bd_processentry |  | fid |

---

## 活动信息-子表 t_bd_subprocessactive

- **表名称：** 活动信息-子表
- **表名：** t_bd_subprocessactive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factivity | 活动名称 | varchar | 30 |  | √ | ' ' | 活动名称,枚举: A :准备活动 B :加工活动 C :其他活动一 D :其他活动二 |
| 2 | factunitid | 活动单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 4 | factivityreport | 汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 5 | fpformulaid | 计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 6 | factivitytype | 活动类型 | varchar | 30 |  | √ | ' ' | 活动类型,枚举: 0 :机器 1 :人工 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdefaultqty | 基本数量 | numeric | 23 | 10 |  | null | 基本数量 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | factivityexpress | 活动汇报量公式 | varchar | 30 |  | √ | ' ' | 活动汇报量公式,枚举: A :准备活动 B :加工活动*CEIL(工序汇报.合格数量/工序计划.基本批量) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_subprocessactive |  | fdetailid |
| 2 | idx_bd_subprocessactive |  | fentryid |

---

## 工艺路线-多语言表 t_bd_processroute_l

- **表名称：** 工艺路线-多语言表
- **表名：** t_bd_processroute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工艺路线名称 | varchar | 255 |  |  | ' ' | 工艺路线名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_nmpr_l_fid |  | fid,flocaleid |
| 2 | pk_bd_processroutel |  | fpkid |

---

## 工艺路线-使用范围表 t_bd_processroute_u

- **表名称：** 工艺路线-使用范围表
- **表名：** t_bd_processroute_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_processroute_u_uo |  | fuseorgid |
| 2 | pk_t_bd_processroute_u |  | fdataid,fuseorgid |

---

## 工艺路线-主表 t_bd_processroute

- **表名称：** 工艺路线-主表
- **表名：** t_bd_processroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 工艺路线分组 | int8 | 64 |  | √ | 0 | [工艺路线分组 bd_routegroup](../sbd_files/bd_routegroup.md) |
| 3 | fprocesscentershow | fprocesscentershow | int8 | 64 |  | √ | 0 |  |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fprocessinstructionsshow | fprocessinstructionsshow | varchar | 512 |  |  | ' ' |  |
| 7 | fsourceid | 来源id | int8 | 64 |  | √ | 0 | 来源id |
| 8 | fworkshop | 车间(隐藏) | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbaseqtyfieldshow | 基本批量 | numeric | 23 | 10 |  | null | 基本批量 |
| 12 | fbatchstartqtyfield | 批量从 | numeric | 23 | 10 |  | null | 批量从 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 15 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 16 | fflexfield | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fprocessorgshow | fprocessorgshow | int8 | 64 |  | √ | 0 |  |
| 20 | fprojnoid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fname | 工艺路线名称 | varchar | 255 |  | √ | ' ' | 工艺路线名称 |
| 22 | funitfield | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 24 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 26 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fismain | 默认工艺路线 | bpchar | 1 |  | √ | '1' | 默认工艺路线 |
| 28 | fnumber | 工艺路线编码 | varchar | 100 |  | √ | ' ' | 工艺路线编码 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 30 | fmaterialgroup | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 31 | fmaterielfield | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fbatchendqtyfield | 批量至 | numeric | 23 | 10 |  | null | 批量至 |
| 33 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 34 | fsource | 来源 | bpchar | 1 |  | √ | '0' | 来源,枚举: 0 :手动新增 1 :接口同步 2 :PLM |
| 35 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 39 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 40 | fprocessunitfieldshow | fprocessunitfieldshow | int8 | 64 |  | √ | 0 |  |
| 41 | fheadunitfieldshow | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | fprocesscontrolcodeshow | fprocesscontrolcodeshow | int8 | 64 |  | √ | 0 |  |
| 43 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fmaterialver | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 47 | fonebaseqty | 表头数量 | numeric | 23 | 10 | √ | 1 | 表头数量 |
| 48 | ferpmaterielfield | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 49 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 50 | fprocessnumbershow | fprocessnumbershow | int8 | 64 |  | √ | 0 |  |
| 51 | fcombofield | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: A :物料 B :物料控制组 C :通用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_route_number |  | fnumber |
| 2 | pk_bd_processroute |  | fid |
| 3 | idx_t_bd_processroute_master |  | fmasterid |
| 4 | idx_t_bd_processroute_createorg |  | fcreateorgid |

---

## （废弃）上工序-多选基础资料表 t_bd_upprocessentry

- **表名称：** （废弃）上工序-多选基础资料表
- **表名：** t_bd_upprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工序信息F7（废弃） mpdm_routeprocess](../sbd_files/mpdm_routeprocess.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_upprocessentry |  | fentryid |
| 2 | pk_bd_upprocessentry |  | fpkid |

---

## 工序明细-分表 t_bd_processentry_a

- **表名称：** 工序明细-分表
- **表名：** t_bd_processentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxratevalue | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 3 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 4 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fheadunitfactor | 生产单位换算系数 | int4 | 32 |  | √ | 0 | 生产单位换算系数 |
| 6 | funitprice | funitprice | numeric | 23 | 10 | √ | 0 |  |
| 7 | finspectplan | （废弃）检验方案 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 8 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 9 | finspectplanrowid | 检验方案分录id | int8 | 64 |  | √ | 0 | 检验方案分录id |
| 10 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 11 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 12 | fproinspect | 工序质检 | bpchar | 1 |  | √ | '0' | 工序质检 |
| 13 | finspectschemeid | 检验方案编码 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 14 | finspectfirst | 首检 | bpchar | 1 |  | √ | ' ' | 首检 |
| 15 | foutsourcepriceandtax | 委外含税单价 | numeric | 23 | 10 | √ | 0 | 委外含税单价 |
| 16 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 17 | fprounitfactor | 工序单位换算系数 | int4 | 32 |  | √ | 0 | 工序单位换算系数 |
| 18 | finspectfirstctrl | 首检控制方式 | bpchar | 1 |  | √ | ' ' | 首检控制方式,枚举: A :严格控制 B :不严格控制 |
| 19 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 22 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | foutsourceprice | 委外单价 | numeric | 23 | 10 | √ | 0 | 委外单价 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 27 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processentry_a |  | fentryid |
| 2 | t_bd_processentry_a_id |  | fid |

---

## （废弃）下工序-多选基础资料表 t_bd_nextprocessentry

- **表名称：** （废弃）下工序-多选基础资料表
- **表名：** t_bd_nextprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工序信息F7（废弃） mpdm_routeprocess](../sbd_files/mpdm_routeprocess.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_nextprocessentry |  | fentryid |
| 2 | pk_bd_nextprocessentry |  | fpkid |

---

## 工序明细-多语言表 t_bd_processentry_l

- **表名称：** 工序明细-多语言表
- **表名：** t_bd_processentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessinstructions | 工序说明 | varchar | 512 |  |  | ' ' | 工序说明 |
| 2 | fsequenceremark | 序列备注 | varchar | 512 |  | √ | ' ' | 序列备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processentryl |  | fpkid |
| 2 | idx_bd_processentryl |  | fentryid,flocaleid |

---

## 作业指导书-附件表 t_bd_processentry_opinst

- **表名称：** 作业指导书-附件表
- **表名：** t_bd_processentry_opinst

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
| 1 | idx_bd_processentry_attachid |  | fentryid,fbasedataid |
| 2 | pk_bd_processentry_opinst |  | fpkid |
