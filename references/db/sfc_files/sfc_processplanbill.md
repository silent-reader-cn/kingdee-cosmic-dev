# 工序计划-sfc_processplanbill

## 工序计划明细-子表 t_sfc_processplanentry

- **表名称：** 工序计划明细-子表
- **表名：** t_sfc_processplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freworksection | （废弃）返工来源工序段 | varchar | 1000 |  | √ | ' ' | （废弃）返工来源工序段 |
| 3 | frelationid | 代码生成id(关联id) | int8 | 64 |  | √ | 0 | 代码生成id(关联id) |
| 4 | ftransinrelationids | 转入工序relationid | varchar | 500 |  | √ | ' ' | 转入工序relationid |
| 5 | fislastprocess | 末序 | bpchar | 1 |  | √ | '0' | 末序 |
| 6 | fprocessqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 7 | fprocesscontrolcode | 工序控制码 | int8 | 64 |  | √ | 0 | [工序控制码 mpdm_processcontrolcode](../mpdm_files/mpdm_processcontrolcode.md) |
| 8 | fsequencetype | 序列类型 | bpchar | 1 |  | √ | ' ' | 序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | freportsbqty | freportsbqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fprocessroutid | 工艺路线id | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 12 | fbegintime | fbegintime | timestamp | 0 |  |  | null |  |
| 13 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 14 | fupprocesstype | （废弃）上工序类型 | varchar | 10 |  | √ | ' ' | （废弃）上工序类型,枚举: A :单个 B :多个 C :群组 |
| 15 | fsendworktype | 派工对象类型（不存数据） | bpchar | 1 |  | √ | ' ' | 派工对象类型（不存数据）,枚举: A :设备 B :人员 C :团队 |
| 16 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | '0' | 首序 |
| 17 | flowerqty | flowerqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | freworkplanqty | （废弃）返工计划数量 | numeric | 23 | 10 | √ | 0 | （废弃）返工计划数量 |
| 20 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 21 | ftobereworkedqty | ftobereworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fprocessinfocode | （废弃）工序编码 | varchar | 30 |  | √ | ' ' | （废弃）工序编码 |
| 23 | fsequenceremark | 序列备注 | varchar | 512 |  | √ | ' ' | 序列备注 |
| 24 | fprocessunit | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | freworkedqty | freworkedqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fhigherqty | fhigherqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | ftransoutrelationids | 转出工序relationid | varchar | 500 |  | √ | ' ' | 转出工序relationid |
| 28 | fprocessorg | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fplanbegintime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 30 | freworksequence | （废弃）返工来源序列号 | int8 | 64 |  | √ | 0 | （废弃）返工来源序列号 |
| 31 | fsumquaqyt | fsumquaqyt | numeric | 23 | 10 | √ | 0 |  |
| 32 | fplanendtime1 | 计划完工日期(上游带入不可改) | timestamp | 0 |  |  | null | 计划完工日期(上游带入不可改) |
| 33 | fpromethod | 加工类型 | varchar | 10 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 34 | fiskeyprocess | 关键工序 | bpchar | 1 |  | √ | '0' | 关键工序 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fsumstockwastqty | fsumstockwastqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | freworkmode | 返工方式 | bpchar | 1 |  | √ | ' ' | 返工方式,枚举: A :直接返工 B :返工序列 |
| 38 | fprocesssequence | 工序序列 | int8 | 64 |  | √ | 0 | 工序序列 |
| 39 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: A :团队作业 B :个人作业 |
| 40 | fintoqty | fintoqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fbasebsqty | 基本批量 | numeric | 23 | 10 | √ | 0 | 基本批量 |
| 42 | fupprocessid | （废弃）上工序id | varchar | 1000 |  | √ | ' ' | （废弃）上工序id |
| 43 | freportmethod | 汇报方式 | varchar | 10 |  | √ | ' ' | 汇报方式,枚举: no :不汇报 must :必须汇报 |
| 44 | frevoveryqty | frevoveryqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
| 46 | foutsourcedqty | foutsourcedqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 48 | fsumworkwastqty | fsumworkwastqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fclosebeforestatus | 工序关闭前状态 | varchar | 10 |  | √ | ' ' | 工序关闭前状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 50 | freportordercontrol | 汇报顺序控制 | bpchar | 1 |  | √ | ' ' | 汇报顺序控制,枚举: A :不控制 B :警告 C :严格控制 |
| 51 | fnextprocessid | （废弃）下工序id | varchar | 1000 |  | √ | ' ' | （废弃）下工序id |
| 52 | freportqty | 可汇报数量 | numeric | 23 | 10 | √ | 0 | 可汇报数量 |
| 53 | fcompleteqty | fcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | fismilestone | （废弃）里程碑 | bpchar | 1 |  | √ | '0' | （废弃）里程碑 |
| 55 | fplanbegintime1 | 计划开工日期(上游带入不可改) | timestamp | 0 |  |  | null | 计划开工日期(上游带入不可改) |
| 56 | ftransinqty | 转入数量 | numeric | 23 | 10 | √ | 0 | 转入数量 |
| 57 | fprocesstatus | 工序状态 | varchar | 10 |  | √ | ' ' | 工序状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 58 | fplanendtime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 59 | ftransinunitid | 转入工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 60 | fismainprocess | （废弃）主工序 | bpchar | 1 |  | √ | '0' | （废弃）主工序 |
| 61 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 62 | fprocesscenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 63 | freworkprocesses | （废弃）返工来源工序 | int8 | 64 |  | √ | 0 | （废弃）返工来源工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry |  | fentryid |
| 2 | idx_sfc_plane_id |  | fid |

---

## 关联子实体-子表 t_sfc_processplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processplan_lk

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
| 1 | idx_sfc_processplan_lk_fk |  | fid |
| 2 | pk_sfc_processplan_lk |  | fpkid |

---

## 工序计划-主表 t_sfc_processplan

- **表名称：** 工序计划-主表
- **表名：** t_sfc_processplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrout | 工艺路线 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 3 | fworkentryf7 | 生产工单分录 | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fworkshop | 生产车间(隐藏) | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 6 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fprojno | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 9 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fworkrowid | 工单行id | int8 | 64 |  | √ | 0 | 工单行id |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | fworkn | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 13 | fprocessroutechange | 工艺路线变更 | bpchar | 1 |  | √ | '0' | 工艺路线变更,枚举: 1 :是 0 :否 |
| 14 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 15 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 16 | fentrustorgid | 委托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 18 | fsourcebillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 19 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | fsourcebilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 24 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 27 | fworkrown | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fmaterielfieldid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 33 | fbizstatus | 生产工单业务状态 | bpchar | 1 |  | √ | ' ' | 生产工单业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 34 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 36 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 37 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 38 | fworkid | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 39 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fisread | 变更已读 | bpchar | 1 |  | √ | '0' | 变更已读,枚举: 1 :是 0 :否 |
| 42 | fpickstatus | 生产工单领料状态 | bpchar | 1 |  | √ | ' ' | 生产工单领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 43 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 47 | fplanstatus | 生产工单计划状态 | bpchar | 1 |  | √ | ' ' | 生产工单计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 48 | fsourcebillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 49 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 50 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 51 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 52 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 53 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_pplan_wid |  | fworkid |
| 2 | pk_t_sfc_processplan |  | fid |

---

## 工序计划-反写记录表 t_sfc_processplan_wb

- **表名称：** 工序计划-反写记录表
- **表名：** t_sfc_processplan_wb

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
| 1 | pk_sfc_processplan_wb |  | fentryid |
| 2 | idx_sfc_processplan_wb_fk |  | fid |

---

## 作业指导书-附件表 t_sfc_procplanentry_opi

- **表名称：** 作业指导书-附件表
- **表名：** t_sfc_procplanentry_opi

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
| 1 | idx_sfc_procplanentry_attachid |  | fentryid,fbasedataid |
| 2 | pk_sfc_procplanentry_opi |  | fpkid |

---

## 工序计划明细-分表 t_sfc_processplanentry_c

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freworkoutproqty | 返工转出生产数量 | numeric | 23 | 10 | √ | 0 | 返工转出生产数量 |
| 3 | fdamageproqty | 损耗生产数量 | numeric | 23 | 10 | √ | 0 | 损耗生产数量 |
| 4 | fsumcompleteqty | fsumcompleteqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | freportsbqty | 关联汇报数量 | numeric | 23 | 10 | √ | 0 | 关联汇报数量 |
| 6 | fsumcompletebaseqty | fsumcompletebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fheadunitfactor | 生产单位换算系数 | int4 | 32 |  | √ | 0 | 生产单位换算系数 |
| 8 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 9 | finproqty | 转入生产数量 | numeric | 23 | 10 | √ | 0 | 转入生产数量 |
| 10 | flowerqty | 汇报下限 | numeric | 23 | 10 | √ | 0 | 汇报下限 |
| 11 | fyetsendworkqty | 已派工数量 | numeric | 23 | 10 | √ | 0 | 已派工数量 |
| 12 | fsumquabaseqyt | 累计合格基本数量 | numeric | 23 | 10 | √ | 0 | 累计合格基本数量 |
| 13 | finbaseqty | 转入基本数量 | numeric | 23 | 10 | √ | 0 | 转入基本数量 |
| 14 | freworkdrawqty | 关联返工数量 | numeric | 23 | 10 | √ | 0 | 关联返工数量 |
| 15 | ftobesendworkbaseqty | 关联派工基本数量 | numeric | 23 | 10 | √ | 0 | 关联派工基本数量 |
| 16 | fouttoqty | （废弃）内协转出数量 | numeric | 23 | 10 | √ | 0 | （废弃）内协转出数量 |
| 17 | ftobereworkedqty | 待返工数量 | numeric | 23 | 10 | √ | 0 | 待返工数量 |
| 18 | ftobereworkedproqty | 待返工生产数量 | numeric | 23 | 10 | √ | 0 | 待返工生产数量 |
| 19 | frelateinbaseqty | 关联转入基本数量 | numeric | 23 | 10 | √ | 0 | 关联转入基本数量 |
| 20 | frelatereworkoutbaseqty | 关联返工转出基本数量 | numeric | 23 | 10 | √ | 0 | 关联返工转出基本数量 |
| 21 | ftobeinsbaseqty | 待检基本单位数量 | numeric | 23 | 10 | √ | 0 | 待检基本单位数量 |
| 22 | foutsourcedsbqty | 关联委外发出数量 | numeric | 23 | 10 | √ | 0 | 关联委外发出数量 |
| 23 | frelateinproqty | 关联转入生产数量 | numeric | 23 | 10 | √ | 0 | 关联转入生产数量 |
| 24 | fprounitfactor | 工序单位换算系数 | int4 | 32 |  | √ | 0 | 工序单位换算系数 |
| 25 | freworkedqty | （废弃）推返工数量 | numeric | 23 | 10 | √ | 0 | （废弃）推返工数量 |
| 26 | fhigherqty | 汇报上限 | numeric | 23 | 10 | √ | 0 | 汇报上限 |
| 27 | fyetsendworkbaseqty | 已派工基本数量 | numeric | 23 | 10 | √ | 0 | 已派工基本数量 |
| 28 | fsumstockwastbaseqty | 累计料废基本数量 | numeric | 23 | 10 | √ | 0 | 累计料废基本数量 |
| 29 | fsampledestorybaseqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 30 | fsendworkstate | 派工状态 | bpchar | 1 |  | √ | ' ' | 派工状态,枚举: A :无需派工 B :待派工 C :派工中 D :已派工 |
| 31 | ftransfersbqty | （废弃）转移选单数量 | numeric | 23 | 10 | √ | 0 | （废弃）转移选单数量 |
| 32 | fsumquaproqyt | 累计合格生产数量 | numeric | 23 | 10 | √ | 0 | 累计合格生产数量 |
| 33 | fsumquaqyt | 累计合格数量 | numeric | 23 | 10 | √ | 0 | 累计合格数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fsumstockwastqty | 累计料废数量 | numeric | 23 | 10 | √ | 0 | 累计料废数量 |
| 36 | freportupperlimit | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 37 | freworkoutqty | 返工转出数量 | numeric | 23 | 10 | √ | 0 | 返工转出数量 |
| 38 | fintoqty | （废弃）内协转入数量 | numeric | 23 | 10 | √ | 0 | （废弃）内协转入数量 |
| 39 | finqty | 转入数量 | numeric | 23 | 10 | √ | 0 | 转入数量 |
| 40 | foutqty | 转出数量 | numeric | 23 | 10 | √ | 0 | 转出数量 |
| 41 | freworkoutbaseqty | 返工转出基本数量 | numeric | 23 | 10 | √ | 0 | 返工转出基本数量 |
| 42 | frelateoutqty | 关联转出数量 | numeric | 23 | 10 | √ | 0 | 关联转出数量 |
| 43 | fsumworkwastbaseqty | 累计工废基本数量 | numeric | 23 | 10 | √ | 0 | 累计工废基本数量 |
| 44 | frelatereworkoutproqty | 关联返工转出生产数量 | numeric | 23 | 10 | √ | 0 | 关联返工转出生产数量 |
| 45 | fsampledestoryproqty | 样本破坏生产数量 | numeric | 23 | 10 | √ | 0 | 样本破坏生产数量 |
| 46 | ftobereworkedbaseqty | 待返工基本数量 | numeric | 23 | 10 | √ | 0 | 待返工基本数量 |
| 47 | freportmethod | freportmethod | varchar | 10 |  | √ | ' ' |  |
| 48 | fdamagebaseqty | 损耗基本数量 | numeric | 23 | 10 | √ | 0 | 损耗基本数量 |
| 49 | fyetsendworkproqty | 已派工生产数量 | numeric | 23 | 10 | √ | 0 | 已派工生产数量 |
| 50 | frelateoutbaseqty | 关联转出基本数量 | numeric | 23 | 10 | √ | 0 | 关联转出基本数量 |
| 51 | fsumworkwastproqty | 累计工废生产数量 | numeric | 23 | 10 | √ | 0 | 累计工废生产数量 |
| 52 | frevoveryqty | 委外接收数量 | numeric | 23 | 10 | √ | 0 | 委外接收数量 |
| 53 | ftobeinspectproqty | 待检生产数量 | numeric | 23 | 10 | √ | 0 | 待检生产数量 |
| 54 | foutsourcedqty | 委外发出数量 | numeric | 23 | 10 | √ | 0 | 委外发出数量 |
| 55 | ftobesendworkproqty | 关联派工生产数量 | numeric | 23 | 10 | √ | 0 | 关联派工生产数量 |
| 56 | foutproqty | 转出生产数量 | numeric | 23 | 10 | √ | 0 | 转出生产数量 |
| 57 | frelatereworkoutqty | 关联返工转出数量 | numeric | 23 | 10 | √ | 0 | 关联返工转出数量 |
| 58 | fsumworkwastqty | 累计工废数量 | numeric | 23 | 10 | √ | 0 | 累计工废数量 |
| 59 | fsumstockwastproqty | 累计料废生产数量 | numeric | 23 | 10 | √ | 0 | 累计料废生产数量 |
| 60 | frelateoutproqty | 关联转出生产数量 | numeric | 23 | 10 | √ | 0 | 关联转出生产数量 |
| 61 | frelateinqty | 关联转入数量 | numeric | 23 | 10 | √ | 0 | 关联转入数量 |
| 62 | ftobeinspectqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 63 | fcompletebaseqty | 完工基本单位数量 | numeric | 23 | 10 | √ | 0 | 完工基本单位数量 |
| 64 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 65 | fcompleteproqty | 完工生产数量 | numeric | 23 | 10 | √ | 0 | 完工生产数量 |
| 66 | foutbaseqty | 转出基本数量 | numeric | 23 | 10 | √ | 0 | 转出基本数量 |
| 67 | fcompleteqty | 完工数量 | numeric | 23 | 10 | √ | 0 | 完工数量 |
| 68 | ftobesendworkqty | 关联派工数量 | numeric | 23 | 10 | √ | 0 | 关联派工数量 |
| 69 | freportdownlimit | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报下限允差（%） |
| 70 | fdamageqty | 损耗数量 | numeric | 23 | 10 | √ | 0 | 损耗数量 |
| 71 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 72 | fyetreworkedqty | 已返工数量 | numeric | 23 | 10 | √ | 0 | 已返工数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_c |  | fentryid |
| 2 | idx_sfc_plane_c_id |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_d

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxratevalue | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 3 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 4 | foutreworkproqty | 委外退回返工生产数量 | numeric | 23 | 10 | √ | 0 | 委外退回返工生产数量 |
| 5 | finreworkproqty | 内协退回返工生产数量 | numeric | 23 | 10 | √ | 0 | 内协退回返工生产数量 |
| 6 | foutsourcepriceandtax | 委外含税单价 | numeric | 23 | 10 | √ | 0 | 委外含税单价 |
| 7 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 8 | foutreworkqty | 委外退回返工数量 | numeric | 23 | 10 | √ | 0 | 委外退回返工数量 |
| 9 | finacceptqty | 内协接收数量 | numeric | 23 | 10 | √ | 0 | 内协接收数量 |
| 10 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | finsendmenuqty | 关联内协发出数量 | numeric | 23 | 10 | √ | 0 | 关联内协发出数量 |
| 12 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | finreworkbaseqty | 内协退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 内协退回返工基本数量 |
| 15 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 16 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 17 | foutreworkbaseqty | 委外退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 委外退回返工基本数量 |
| 18 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 19 | finsendqty | 内协发出数量 | numeric | 23 | 10 | √ | 0 | 内协发出数量 |
| 20 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 21 | finreworkqty | 内协退回返工数量 | numeric | 23 | 10 | √ | 0 | 内协退回返工数量 |
| 22 | foutsourceprice | 委外单价 | numeric | 23 | 10 | √ | 0 | 委外单价 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_d |  | fentryid |
| 2 | idx_sfc_plane_d_id |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_i

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_i

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffirstincontrolmode | 首检控制方式 | bpchar | 1 |  | √ | ' ' | 首检控制方式,枚举: A :严格控制 B :不严格控制 |
| 3 | fpickingstate | 领料状态 | bpchar | 1 |  | √ | ' ' | 领料状态,枚举: E :不领料 A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 4 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 5 | finspectschemeid | 检验方案编码 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 6 | ffirstinstate | 首检状态 | bpchar | 1 |  | √ | ' ' | 首检状态,枚举: A :空 B :待首检 C :首检中 D :首检完成 |
| 7 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fpatrolinstate | 巡检状态 | bpchar | 1 |  | √ | ' ' | 巡检状态,枚举: A :空 B :巡检中 C :巡检合格 D :巡检不合格 |
| 9 | finspectplan | （废弃）检验方案 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 10 | finspectplanrowid | 检验方案分录id | int8 | 64 |  | √ | 0 | 检验方案分录id |
| 11 | ffirstinspect | 首检 | bpchar | 1 |  | √ | '0' | 首检 |
| 12 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpropickingqty | 已领套数 | numeric | 23 | 10 | √ | 0 | 已领套数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_processplanentry_i |  | fentryid |
| 2 | idx_sfc_proplanentry_i_id |  | fid |

---

## 工序计划明细-分表 t_sfc_processplanentry_a

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispal | 准备活动人工 | bpchar | 1 |  | √ | '0' | 准备活动人工 |
| 3 | fraactivityreport | 准备活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 4 | fwamreportqty | 加工活动机器汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器汇报数量 |
| 5 | fsumwamplanqty | 加工活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动机器计划活动总量 |
| 6 | fpamreportqty | 准备活动机器活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器活动汇报数量 |
| 7 | fispam | 准备活动机器 | bpchar | 1 |  | √ | '0' | 准备活动机器 |
| 8 | frmactivityreport | 准备活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 9 | fpmpformulaid | 加工活动机器*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 10 | frapformulaid | 准备活动人工*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 11 | frmresource | 准备活动机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 12 | fwalplanqty | 加工活动人工基本数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工基本数量 |
| 13 | fraresource | 准备活动人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 14 | frmpformulaid | 准备活动机器*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 15 | fpamunit | 准备活动机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fpmactivityreport | 加工活动机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 17 | fwalreportqty | 加工活动人工汇报数量 | numeric | 23 | 10 | √ | 0 | 加工活动人工汇报数量 |
| 18 | fsumwalplanqty | 加工活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 加工活动人工计划活动总量 |
| 19 | fiswal | 加工活动人工 | bpchar | 1 |  | √ | '0' | 加工活动人工 |
| 20 | fiswam | 加工活动机器 | bpchar | 1 |  | √ | '0' | 加工活动机器 |
| 21 | fpalplanqty | 准备活动人工基本数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工基本数量 |
| 22 | fpamplanqty | 准备活动机器基本数量 | numeric | 23 | 10 | √ | 0 | 准备活动机器基本数量 |
| 23 | funitfield | 准备活动人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fpalreportqty | 准备活动人工活动汇报数量 | numeric | 23 | 10 | √ | 0 | 准备活动人工活动汇报数量 |
| 25 | fwalunit | 加工活动人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fpaactivityreport | 加工活动人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 27 | fpapformulaid | 加工活动人工*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 28 | fwamplanqty | 加工活动机器基本数量 | numeric | 23 | 10 | √ | 0 | 加工活动机器基本数量 |
| 29 | fiscomeup3 | 加工人工默认 | bpchar | 1 |  | √ | '0' | 加工人工默认 |
| 30 | fwamunit | 加工活动机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fiscomeup4 | 加工机器默认 | bpchar | 1 |  | √ | '0' | 加工机器默认 |
| 32 | fiscomeup1 | 准备人工默认 | bpchar | 1 |  | √ | '0' | 准备人工默认 |
| 33 | fsumpamplanqty | 准备活动机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动机器计划活动总量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fiscomeup2 | 准备机器默认 | bpchar | 1 |  | √ | '0' | 准备机器默认 |
| 36 | fsumpalplanqty | 准备活动人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 准备活动人工计划活动总量 |
| 37 | fpmresource | 加工活动机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 38 | fparesource | 加工活动人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_a_id |  | fid |
| 2 | pk_sfc_processplanentry_a |  | fentryid |

---

## 工序计划明细-分表 t_sfc_processplanentry_b

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpalreportqty7 | 其他活动一人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工汇报数量 |
| 3 | fomresource | 其他活动一机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 4 | fpalplanqty8 | 其他活动二人工基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工基本数量 |
| 5 | foaresource | 其他活动一人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 6 | ftmresource | 其他活动二机器*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 7 | fompformulaid | 其他活动一机器*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 8 | fsumoomplanqty | 其他活动一机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器计划活动总量 |
| 9 | foapformulaid | 其他活动一人工*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 10 | foaactivityreport | 其他活动一人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 11 | fsumoopplanqty | 其他活动一人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工计划活动总量 |
| 12 | fpamreportqty8 | 其他活动二人工汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工汇报数量 |
| 13 | ftaresource | 其他活动二人工*资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 14 | funitfield8 | 其他活动二人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpamreportqty4 | 其他活动二机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器汇报数量 |
| 16 | ftmactivityreport | 其他活动二机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 17 | funitfield3 | 其他活动一机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fpalplanqty7 | 其他活动一人工基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动一人工基本数量 |
| 19 | ftapformulaid | 其他活动二人工*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 20 | fpalplanqty4 | 其他活动二机器基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器基本数量 |
| 21 | fomactivityreport | 其他活动一机器*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 22 | fpamreportqty3 | 其他活动一机器汇报数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器汇报数量 |
| 23 | ftaactivityreport | 其他活动二人工*汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 24 | funitfield7 | 其他活动一人工单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | fpalplanqty3 | 其他活动一机器基本数量 | numeric | 23 | 10 | √ | 0 | 其他活动一机器基本数量 |
| 26 | funitfield4 | 其他活动二机器单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fsumospplanqty | 其他活动二人工计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二人工计划活动总量 |
| 28 | ftmpformulaid | 其他活动二机器*计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 29 | fispal4 | 其他活动二机器 | bpchar | 1 |  | √ | '0' | 其他活动二机器 |
| 30 | fiscomeup14 | 其他活动二机器默认 | bpchar | 1 |  | √ | '0' | 其他活动二机器默认 |
| 31 | fispal3 | 其他活动一机器 | bpchar | 1 |  | √ | '0' | 其他活动一机器 |
| 32 | fsumosmplanqty | 其他活动二机器计划活动总量 | numeric | 23 | 10 | √ | 0 | 其他活动二机器计划活动总量 |
| 33 | fiscomeup13 | 其他活动一机器默认 | bpchar | 1 |  | √ | '0' | 其他活动一机器默认 |
| 34 | fispal8 | 其他活动二人工 | bpchar | 1 |  | √ | '0' | 其他活动二人工 |
| 35 | fiscomeup18 | 其他活动二人工默认 | bpchar | 1 |  | √ | '0' | 其他活动二人工默认 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fispal7 | 其他活动一人工 | bpchar | 1 |  | √ | '0' | 其他活动一人工 |
| 38 | fiscomeup17 | 其他活动一人工默认 | bpchar | 1 |  | √ | '0' | 其他活动一人工默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_plane_b_id |  | fid |
| 2 | pk_sfc_processplanentry_b |  | fentryid |

---

## 工序计划明细-分表 t_sfc_processplanentry_s

- **表名称：** 工序计划明细-分表
- **表名：** t_sfc_processplanentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fendprocessnumber | 拆分来源结束工序号 | int4 | 32 |  | √ | 0 | 拆分来源结束工序号 |
| 3 | fstartprocessnumber | 拆分来源起始工序号 | int4 | 32 |  | √ | 0 | 拆分来源起始工序号 |
| 4 | finsideplanqty | 生成内协工序计划数量 | numeric | 23 | 10 | √ | 0 | 生成内协工序计划数量 |
| 5 | fsrcprocesssequence | 拆分来源序列号 | int4 | 32 |  | √ | 0 | 拆分来源序列号 |
| 6 | fnormalsplitqty | 普通拆分数量 | numeric | 23 | 10 | √ | 0 | 普通拆分数量 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procplan_entrys_num |  | fstartprocessnumber,fendprocessnumber |
| 2 | pk_sfc_processplanentry_s |  | fentryid |
| 3 | idx_sfc_procplan_entrys_id |  | fid |
| 4 | idx_sfc_procplan_entrys_seq |  | fsrcprocesssequence |

---

## 工序计划明细-多语言表 t_sfc_processplanentry_l

- **表名称：** 工序计划明细-多语言表
- **表名：** t_sfc_processplanentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessinstructions | 工序说明 | varchar | 512 |  | √ | ' ' | 工序说明 |
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
| 1 | idx_sfc_plane_l_id |  | fentryid |
| 2 | pk_t_sfc_processplanentry_l |  | fpkid |

---

## 工序计划-关联追踪表 t_sfc_processplan_tc

- **表名称：** 工序计划-关联追踪表
- **表名：** t_sfc_processplan_tc

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
| 1 | idx_sfc_processplan_tc_tid |  | ftid |
| 2 | pk_sfc_processplan_tc |  | fid |
| 3 | idx_sfc_processplan_tc_tbill |  | ftbillid |

---

## 工序计划-分表 t_sfc_processplan_s

- **表名称：** 工序计划-分表
- **表名：** t_sfc_processplan_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 拆分序列号 | int4 | 32 |  | √ | 0 | 拆分序列号 |
| 3 | fendprocessnumber | 拆分结束工序号 | int4 | 32 |  | √ | 0 | 拆分结束工序号 |
| 4 | fsrcprocessplanid | 来源工序计划 | int8 | 64 |  | √ | 0 | [工序计划 sfc_bd_processplan](../sfc_files/sfc_bd_processplan.md) |
| 5 | fsplittype | 产生方式 | bpchar | 1 |  | √ | ' ' | 产生方式,枚举: A :首序到底拆分 B :中间工序到底拆分 C :指定工序段拆分 D :生成内协工序计划 |
| 6 | fstartprocessnumber | 拆分起始工序号 | int4 | 32 |  | √ | 0 | 拆分起始工序号 |
| 7 | fbillsn | 拆分流水号（直接下级流水） | int4 | 32 |  | √ | 0 | 拆分流水号（直接下级流水） |
| 8 | fcount | 拆分个数（直接下级个数） | int4 | 32 |  | √ | 0 | 拆分个数（直接下级个数） |
| 9 | frootprocessplanid | 主工序计划 | int8 | 64 |  | √ | 0 | [工序计划 sfc_bd_processplan](../sfc_files/sfc_bd_processplan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procplan_srcid |  | fsrcprocessplanid |
| 2 | pk_sfc_processplan_s |  | fid |
| 3 | idx_sfc_procplan_rootid |  | frootprocessplanid |
| 4 | idx_sfc_procplan_sspinfo |  | fsplittype,fprocesssequence,fstartprocessnumber,fendprocessnumber |

---

## 工序计划-多语言表 t_sfc_processplan_l

- **表名称：** 工序计划-多语言表
- **表名：** t_sfc_processplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_proplan_l_id |  | fid |
| 2 | pk_t_sfc_processplan_l |  | fpkid |

---

## 关联子实体-子表 t_sfc_processplanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processplanentry_lk

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
| 1 | idx_sfc_processplanentry_lk_fk |  | fentryid |
| 2 | pk_sfc_processplanentry_lk |  | fpkid |
