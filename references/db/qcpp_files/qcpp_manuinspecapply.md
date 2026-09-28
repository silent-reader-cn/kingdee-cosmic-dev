# 生产退料请检单-qcpp_manuinspecapply

## 联合检验信息-子表 t_qcpp_inspapplyproj

- **表名称：** 联合检验信息-子表
- **表名：** t_qcpp_inspapplyproj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcheckinstructid | 检验仪器 | int8 | 64 |  | √ | 0 | [检验仪器 qcbd_inspectioninstru](../qcbd_files/qcbd_inspectioninstru.md) |
| 2 | fdownvalue | 下限值 | numeric | 23 | 10 |  | null | 下限值 |
| 3 | fcheckcontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 4 | fnormtype | 指标类型 | varchar | 5 |  | √ | ' ' | 指标类型,枚举: A :定量 B :定性 |
| 5 | fspecvalue | 标准值 | varchar | 50 |  | √ | ' ' | 标准值 |
| 6 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fisjoininspect | 联合检验项 | bpchar | 1 |  | √ | '0' | 联合检验项 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftopvalue | 上限值 | numeric | 23 | 10 |  | null | 上限值 |
| 10 | fjoininspectorid | 联合检验员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fjoininspectqty | 联合检验关联数量 | numeric | 23 | 10 | √ | 0 | 联合检验关联数量 |
| 12 | fjoininspbaseqty | 联合检验关联基本数量 | numeric | 23 | 10 | √ | 0 | 联合检验关联基本数量 |
| 13 | fmatchflagid | 比较符 | int8 | 64 |  | √ | 0 | [比较符 qcbd_matchflag](../qcbd_files/qcbd_matchflag.md) |
| 14 | fjoininspectstatus | 联合检验状态 | varchar | 5 |  | √ | ' ' | 联合检验状态,枚举: P :计划 Y :已完成 |
| 15 | fjoindeptid | 联合检验部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fkeyquality | 特性分类 | varchar | 5 |  | √ | ' ' | 特性分类,枚举: A :关键特性 C :重要特性 B :一般特性 |
| 17 | fcheckfreqid | 检验频率 | int8 | 64 |  | √ | 0 | [检验频率 qcbd_inspectionfreq](../qcbd_files/qcbd_inspectionfreq.md) |
| 18 | fprojsampid | 项目抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 19 | fcheckitemsid | 检验项目 | int8 | 64 |  | √ | 0 | [检验项目 qcbd_inspectionitems](../qcbd_files/qcbd_inspectionitems.md) |
| 20 | fcheckbasisid | 检验依据 | int8 | 64 |  | √ | 0 | [检验依据 qcbd_inspectioncrit](../qcbd_files/qcbd_inspectioncrit.md) |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 22 | fcheckmethodid | 检验方法 | int8 | 64 |  | √ | 0 | [检验方法 qcbd_inspectionmethod](../qcbd_files/qcbd_inspectionmethod.md) |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_inspapp_fseq |  | fseq |
| 2 | pk_qcpp_inspapplyproj |  | fdetailid |
| 3 | idx_qcpp_inspapp_fentryid |  | fentryid |

---

## 关联子实体-子表 t_qcp_inspecapplyentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_inspecapplyentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_qcp_inspecapplyentry_lk_pkey |  | fpkid |
| 2 | idx_qcp_inspecapplyentry_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_qcpp_inspapplyproj_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcpp_inspapplyproj_lk

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
| 1 | pk_qcpp_inspapplyproj_lk |  | fpkid |
| 2 | idx_qcpp_inspapplyproj_lk_fk |  | fdetailid |

---

## 检验方案匹配维度-多选基础资料表 t_qcpp_applypromatchdimo

- **表名称：** 检验方案匹配维度-多选基础资料表
- **表名：** t_qcpp_applypromatchdimo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [检验方案匹配维度 qcbd_promatchdimo](../qcbd_files/qcbd_promatchdimo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_applypromatchdimo |  | fpkid |
| 2 | idx_qcpp_applypromatchdimo_fpkid |  | fpkid |

---

## 物料信息-子表 t_qcpp_insappentry

- **表名称：** 物料信息-子表
- **表名：** t_qcpp_insappentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 3 | fchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 4 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 7 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 8 | ffinishtime | 期望完成时间 | timestamp | 0 |  |  | null | 期望完成时间 |
| 9 | fsrcsubbillentryseq | 来源子单据体分录序号 | int8 | 64 |  | √ | 0 | 来源子单据体分录序号 |
| 10 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 13 | fmanufactureorder | 核心单据编号（废弃） | varchar | 80 |  | √ | ' ' | 核心单据编号（废弃） |
| 14 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 15 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | foproperation | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 19 | fauthorizeobjid | 鉴权对象 | int8 | 64 |  | √ | 0 | [鉴权对象 qcbd_authorize_object](../qcbd_files/qcbd_authorize_object.md) |
| 20 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 23 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 25 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 26 | fsupplymode | 货主类型 | varchar | 54 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 27 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 28 | fqrouteid | 工艺路线编码 | int8 | 64 |  | √ | 0 | [质量工艺路线 qcbd_qmcroute](../qcbd_files/qcbd_qmcroute.md) |
| 29 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 30 | foprworkshop | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | finspedeptid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fprocessseq | 工序序列号 | varchar | 50 |  | √ | ' ' | 工序序列号 |
| 35 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 36 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 37 | fbasejoinqty | 基本单位关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位关联数量 |
| 38 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 39 | fsrcsubbillentryid | 来源子单据体分录行ID | int8 | 64 |  | √ | 0 | 来源子单据体分录行ID |
| 40 | fmaterielid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 41 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 42 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 43 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 44 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 45 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 46 | fmanudate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 47 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 49 | freporderno | 汇报单编号 | varchar | 80 |  | √ | ' ' | 汇报单编号 |
| 50 | fresultstatus | fresultstatus | varchar | 10 |  | √ | ' ' |  |
| 51 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 52 | finspectstatus | 完成状态 | varchar | 1 |  | √ | ' ' | 完成状态,枚举: A :计划 B :进行中 C :质检完成 |
| 53 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 54 | fsrcunitid | 源单单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 55 | finspectorid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 57 | finspectstdid | 检验标准 | int8 | 64 |  | √ | 0 | [检验标准 qcbd_inspectionstd](../qcbd_files/qcbd_inspectionstd.md) |
| 58 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 59 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 60 | fsrcordernum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 61 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 62 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 63 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 64 | fsrcordertype | 来源单据类型（废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（废弃） |
| 65 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_insary_fmat |  | fmaterielid |
| 2 | idx_qcpp_insary_fmatcfg |  | fmaterialcfg |
| 3 | idx_qcpp_insary_fseq |  | fseq |
| 4 | idx_qcpp_insary_fid |  | fid |
| 5 | pk_qcpp_insappentry |  | fentryid |

---

## 物料信息-分表 t_qcpp_insappentry_q

- **表名称：** 物料信息-分表
- **表名：** t_qcpp_insappentry_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperatenstate | 作业不良默认库存状态 | int8 | 64 |  |  | null | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 3 | foperatenfinishbq | 作业不良完成数量 | numeric | 23 | 10 | √ | 0 | 作业不良完成数量 |
| 4 | foperatenselbq | 作业不良选单数量 | numeric | 23 | 10 | √ | 0 | 作业不良选单数量 |
| 5 | flpretfinishbaseqty | 良品退料完成数量 | numeric | 23 | 10 | √ | 0 | 良品退料完成数量 |
| 6 | flpstockstate | 良品默认库存状态 | int8 | 64 |  |  | null | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 7 | finspselbaseqty | 检验选单数量 | numeric | 23 | 10 | √ | 0 | 检验选单数量 |
| 8 | foperatenbaseqty | 作业不良数量 | numeric | 23 | 10 | √ | 0 | 作业不良数量 |
| 9 | finspfinishbaseqty | 完成数量 | numeric | 23 | 10 | √ | 0 | 完成数量 |
| 10 | fincomingnselbq | 来料不良选单数量 | numeric | 23 | 10 | √ | 0 | 来料不良选单数量 |
| 11 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 12 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 13 | fimcomingnstate | 来料不良默认库存状态 | int8 | 64 |  |  | null | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 14 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 16 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fincomingnfinishbq | 来料不良完成数量 | numeric | 23 | 10 | √ | 0 | 来料不良完成数量 |
| 18 | flpretselbaseqty | 良品退料选单数量 | numeric | 23 | 10 | √ | 0 | 良品退料选单数量 |
| 19 | fincomingnbaseqty | 来料不良数量 | numeric | 23 | 10 | √ | 0 | 来料不良数量 |
| 20 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 22 | finsppassbaseqty | 检验合格数量 | numeric | 23 | 10 | √ | 0 | 检验合格数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcpp_insappentry_q |  | fentryid |

---

## 生产退料请检单-反写记录表 t_qcp_inspecapply_wb

- **表名称：** 生产退料请检单-反写记录表
- **表名：** t_qcp_inspecapply_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_inspecapply_wb_fk |  | fid |
| 2 | t_qcp_inspecapply_wb_pkey |  | fentryid |

---

## 生产退料请检单-多语言表 t_qcpp_inspecapply_l

- **表名称：** 生产退料请检单-多语言表
- **表名：** t_qcpp_inspecapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_inspecapply_l |  | fpkid |
| 2 | idx_qcpp_insplyl_fid |  | fid,flocaleid |
| 3 | idx_qcpp_insplyl_fcomment |  | fcomment |

---

## 生产退料请检单-主表 t_qcpp_inspecapply

- **表名称：** 生产退料请检单-主表
- **表名：** t_qcpp_inspecapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finspecorgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fqualityorg | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauthorizeobjid | 鉴权对象 | int8 | 64 |  | √ | 0 | [鉴权对象 qcbd_authorize_object](../qcbd_files/qcbd_authorize_object.md) |
| 10 | fapplyuser | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 3 :webApi生成 |
| 14 | fapplytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 15 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | finterfaceid | 接口候选键id | varchar | 50 |  | √ | ' ' | 接口候选键id |
| 20 | fjoininspectflag | 启用联合检验 | bpchar | 1 |  | √ | '0' | 启用联合检验 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_insply_fbillno |  | fbillno |
| 2 | idx_qcpp_insply_fcreatetime |  | fcreatetime |
| 3 | pk_qcpp_inspecapply |  | fid |

---

## 生产退料请检单-关联追踪表 t_qcp_inspecapply_tc

- **表名称：** 生产退料请检单-关联追踪表
- **表名：** t_qcp_inspecapply_tc

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
| 1 | idx_qcp_inspecapply_tc_tbill |  | ftbillid |
| 2 | idx_qcp_inspecapply_tc_tid |  | ftid |
| 3 | t_qcp_inspecapply_tc_pkey |  | fid |

---

## 关联子实体-子表 t_qcp_inspecapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_inspecapply_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_qcp_inspecapply_lk_pkey |  | fpkid |
| 2 | idx_qcp_inspecapply_lk_fk |  | fid |
