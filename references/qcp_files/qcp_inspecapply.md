# 来料检验申请单-qcp_inspecapply

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

## 检验项目-子表 t_qcp_inspapplyproj

- **表名称：** 检验项目-子表
- **表名：** t_qcp_inspapplyproj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcheckinstructid | 检验仪器 | int8 | 64 |  | √ | 0 | 检验仪器 qcbd_inspectioninstru |
| 2 | fdownvalue | 下限值 | numeric | 23 | 10 |  | null | 下限值 |
| 3 | fcheckcontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 4 | fnormtype | 指标类型 | varchar | 5 |  | √ | ' ' | 指标类型,枚举: A :定量 B :定性 |
| 5 | fspecvalue | 标准值 | varchar | 50 |  | √ | ' ' | 标准值 |
| 6 | funitid | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fisjoininspect | 联合检验项 | bpchar | 1 |  | √ | '0' | 联合检验项 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | ftopvalue | 上限值 | numeric | 23 | 10 |  | null | 上限值 |
| 10 | fjoininspectorid | 联合检验员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fjoininspectqty | 联合检验关联数量 | numeric | 23 | 10 | √ | 0 | 联合检验关联数量 |
| 12 | fjoininspbaseqty | 联合检验关联基本数量 | numeric | 23 | 10 | √ | 0 | 联合检验关联基本数量 |
| 13 | fmatchflagid | 比较符 | int8 | 64 |  | √ | 0 | 比较符 qcbd_matchflag |
| 14 | fjoininspectstatus | 联合检验状态 | varchar | 5 |  | √ | ' ' | 联合检验状态,枚举: P :计划 Y :已完成 |
| 15 | fjoindeptid | 联合检验部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fkeyquality | 特性分类 | varchar | 5 |  | √ | ' ' | 特性分类,枚举: A :关键特性 C :重要特性 B :一般特性 |
| 17 | fcheckfreqid | 检验频率 | int8 | 64 |  | √ | 0 | 检验频率 qcbd_inspectionfreq |
| 18 | fprojsampid | 项目抽样方案 | int8 | 64 |  | √ | 0 | 抽样方案 qcbd_sampscheme |
| 19 | fcheckitemsid | 检验项目 | int8 | 64 |  | √ | 0 | 检验项目 qcbd_inspectionitems |
| 20 | fcheckbasisid | 检验依据 | int8 | 64 |  | √ | 0 | 检验依据 qcbd_inspectioncrit |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 22 | fcheckmethodid | 检验方法 | int8 | 64 |  | √ | 0 | 检验方法 qcbd_inspectionmethod |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspapplyproj |  | fdetailid |
| 2 | idx_qcp_insapppoj_fseq |  | fseq |
| 3 | idx_qcp_insapppoj_fentryid |  | fentryid |

---

## 物料信息-子表 t_qcp_insappnentry

- **表名称：** 物料信息-子表
- **表名：** t_qcp_insappnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 3 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 4 | fordernum | 核心单据编号（废弃） | varchar | 80 |  | √ | ' ' | 核心单据编号（废弃） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 7 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 9 | ffinishtime | 期望完成时间 | timestamp | 0 |  |  | null | 期望完成时间 |
| 10 | fordertype | 核心单据类型（废弃） | varchar | 50 |  | √ | ' ' | 核心单据类型（废弃） |
| 11 | fsrcsubbillentryseq | 来源子单据体分录序号 | int8 | 64 |  | √ | 0 | 来源子单据体分录序号 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 14 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0 |  |
| 15 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | 物料质检信息 bd_inspect_cfg |
| 18 | fauthorizeobjid | 鉴权对象 | int8 | 64 |  | √ | 0 | 鉴权对象 qcbd_authorize_object |
| 19 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 20 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 21 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 22 | fmanutime | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 23 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | finspedeptid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fexpiretime | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 28 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 29 | fbasejoinqty | 基本单位关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位关联数量 |
| 30 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fsrcsubbillentryid | 来源子单据体分录行ID | int8 | 64 |  | √ | 0 | 来源子单据体分录行ID |
| 32 | fmaterielid | 物料主数据 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 33 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 34 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 35 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 36 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 37 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 39 | fresultstatus | fresultstatus | varchar | 10 |  | √ | ' ' |  |
| 40 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 41 | finspectstatus | 检验进度 | varchar | 1 |  | √ | ' ' | 检验进度,枚举: A :计划 B :质检开始 C :质检完成 |
| 42 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 43 | fsrcunitid | 源单单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | finspectorid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 46 | finspectstdid | 检验标准 | int8 | 64 |  | √ | 0 | 检验标准 qcbd_inspectionstd |
| 47 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 48 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 49 | fsrcordernum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 50 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 51 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 52 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 53 | fsrcordertype | 来源单据类型（废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（废弃） |
| 54 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_insappnentry |  | fentryid |
| 2 | idx_qcp_insary_fid |  | fid |
| 3 | idx_qcp_insary_fmat |  | fmaterielid |
| 4 | idx_qcp_insary_fmatcfg |  | fmaterialcfg |
| 5 | idx_qcp_insary_fseq |  | fseq |

---

## 来料检验申请单-多语言表 t_qcp_inspecapplyn_l

- **表名称：** 来料检验申请单-多语言表
- **表名：** t_qcp_inspecapplyn_l

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
| 1 | pk_qcp_inspecapplyn_l |  | fpkid |
| 2 | idx_qcp_inspynl_fid |  | fid,flocaleid |
| 3 | idx_qcp_inspynl_fcomment |  | fcomment |

---

## 检验方案匹配维度-多选基础资料表 t_qcp_applypromatchdimo

- **表名称：** 检验方案匹配维度-多选基础资料表
- **表名：** t_qcp_applypromatchdimo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 检验方案匹配维度 qcbd_promatchdimo |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_applypromatchdimo_fpkid |  | fpkid |
| 2 | pk_qcp_applypromatchdimo |  | fpkid |

---

## 来料检验申请单-反写记录表 t_qcp_inspecapply_wb

- **表名称：** 来料检验申请单-反写记录表
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

## 来料检验申请单-主表 t_qcp_inspecapplyn

- **表名称：** 来料检验申请单-主表
- **表名：** t_qcp_inspecapplyn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finspecorgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fqualityorg | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauthorizeobjid | 鉴权对象 | int8 | 64 |  | √ | 0 | 鉴权对象 qcbd_authorize_object |
| 10 | fapplyuser | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 3 :webApi生成 |
| 13 | fapplytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | finterfaceid | 接口候选键id | varchar | 50 |  | √ | ' ' | 接口候选键id |
| 18 | fjoininspectflag | 启用联合检验 | bpchar | 1 |  | √ | '0' | 启用联合检验 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_inspyn_fcreatetime |  | fcreatetime |
| 2 | pk_qcp_inspecapplyn |  | fid |
| 3 | idx_qcp_inspyn_fbillno |  | fbillno |

---

## 关联子实体-子表 t_qcp_inspapplyproj_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_inspapplyproj_lk

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
| 1 | idx_qcp_inspapplyproj_lk_fk |  | fdetailid |
| 2 | pk_qcp_inspapplyproj_lk |  | fpkid |

---

## 来料检验申请单-关联追踪表 t_qcp_inspecapply_tc

- **表名称：** 来料检验申请单-关联追踪表
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
