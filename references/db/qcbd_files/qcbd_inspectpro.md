# 检验方案-qcbd_inspectpro

## 检验方案-主表 t_qcbd_inspectpro

- **表名称：** 检验方案-主表
- **表名：** t_qcbd_inspectpro

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 检验方案分类 qcbd_inspectpro_group |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fbiztype | 检验业务类型（弃用） | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fxkallocationtype | 分配类型 | varchar | 30 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 16 | fbizstypeid | fbizstypeid | varchar | 5 |  | √ | '0' |  |
| 17 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | '5' | 控制策略,枚举: 5 :全局共享 |
| 21 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspectpro |  | fid |
| 2 | idx_qcbd_inspro_fcreatetime |  | fcreatetime |
| 3 | uidx_qcbd_inspectpro_billno |  | fnumber |
| 4 | idx_t_qcbd_inspectpro_createorg |  | fcreateorgid |
| 5 | idx_t_qcbd_inspectpro_master |  | fmasterid |

---

## 检验业务类型-多选基础资料表 t_qcbd_inspectpro_type

- **表名称：** 检验业务类型-多选基础资料表
- **表名：** t_qcbd_inspectpro_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspprotype_pk |  | fpkid |

---

## 检验方案-使用范围表 t_qcbd_inspectpro_u

- **表名称：** 检验方案-使用范围表
- **表名：** t_qcbd_inspectpro_u

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
| 1 | idx_t_qcbd_inspectpro_u_uo |  | fuseorgid |
| 2 | pk_t_qcbd_inspectpro_u |  | fdataid,fuseorgid |

---

## 检验方案单据体-子表 t_qcbd_inspro_ent

- **表名称：** 检验方案单据体-子表
- **表名：** t_qcbd_inspro_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsampleproid | 抽样方案 | int8 | 64 |  | √ | 0 | 抽样方案 qcbd_sampscheme |
| 3 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 4 | fsetuptype | 设置类型 | varchar | 5 |  | √ | '0' | 设置类型,枚举: 0 :物料 1 :物料分类 2 :通用 3 :物料+工序 |
| 5 | foproperation | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 6 | fqualinsporg | 质检组 | int8 | 64 |  | √ | 0 | 质检业务组 qcbd_qualityorg |
| 7 | fprocessno | 工序 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmaterielid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | finspectstdid | 检验标准 | int8 | 64 |  | √ | 0 | 检验标准 qcbd_inspectionstd |
| 12 | frocessseq | 工序序列号 | varchar | 50 |  | √ | ' ' | 工序序列号 |
| 13 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | finspectorgid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fmaterieltypeid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 16 | fqrouteid | 工艺路线编码 | int8 | 64 |  | √ | 0 | 质量工艺路线 qcbd_qmcroute |
| 17 | fwstrsproid | 宽严度转换方案 | int8 | 64 |  | √ | 0 | 宽严度转换方案 qcbd_widstrict_rule |
| 18 | fsuppliermasterid | 供应商(主数据内码) | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 19 | fjoininspectflag | 启用联合检验 | bpchar | 1 |  | √ | '0' | 启用联合检验 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fmaterielcfgid | 物料编码 | int8 | 64 |  | √ | 0 | 物料质检信息 bd_inspect_cfg |
| 22 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_inspro_fid |  | fid |
| 2 | idx_qcbd_inspro_fseq |  | fseq |
| 3 | idx_qcbd_insproent_fmaterielid |  | fmaterielid |
| 4 | pk_qcbd_inspro_ent |  | fentryid |

---

## 检验方案-使用范围位图表 t_qcbd_inspectpro_m

- **表名称：** 检验方案-使用范围位图表
- **表名：** t_qcbd_inspectpro_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcbd_inspectpro_m |  | forgid |

---

## 检验方案-多语言表 t_qcbd_inspectpro_l

- **表名称：** 检验方案-多语言表
- **表名：** t_qcbd_inspectpro_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_inspectpro_l |  | fpkid |
| 2 | idx_qcbd_insprol_fid |  | fid,flocaleid |
| 3 | idx_qcbd_insprol_fname |  | fname |

---

## 检验项目单据体-子表 t_qcbd_schemeproj

- **表名称：** 检验项目单据体-子表
- **表名：** t_qcbd_schemeproj

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
| 11 | fmatchflagid | 比较符 | int8 | 64 |  | √ | 0 | 比较符 qcbd_matchflag |
| 12 | fjoindeptid | 联合检验部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fkeyquality | 特性分类 | varchar | 5 |  | √ | ' ' | 特性分类,枚举: A :关键特性 C :重要特性 B :一般特性 |
| 14 | fcheckfreqid | 检验频率 | int8 | 64 |  | √ | 0 | 检验频率 qcbd_inspectionfreq |
| 15 | fprojsampid | 项目抽样方案 | int8 | 64 |  | √ | 0 | 抽样方案 qcbd_sampscheme |
| 16 | fcheckitemsid | 检验项目 | int8 | 64 |  | √ | 0 | 检验项目 qcbd_inspectionitems |
| 17 | fcheckbasisid | 检验依据 | int8 | 64 |  | √ | 0 | 检验依据 qcbd_inspectioncrit |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | fcheckmethodid | 检验方法 | int8 | 64 |  | √ | 0 | 检验方法 qcbd_inspectionmethod |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_scheoj_fentryid |  | fentryid |
| 2 | pk_qcbd_schemeproj |  | fdetailid |
| 3 | idx_qcbd_scheoj_fseq |  | fseq |
