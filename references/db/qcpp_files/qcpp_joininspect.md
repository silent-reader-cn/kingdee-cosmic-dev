# 生产联合检验单-qcpp_joininspect

## 关联子实体-子表 t_qcpp_joininspect_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcpp_joininspect_lk

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
| 1 | pk_qcpp_joininspect_lk |  | fpkid |
| 2 | idx_qcpp_joininspect_lk_fk |  | fid |

---

## 检验结果_样本-子表 t_qcpp_joininspsamp_n

- **表名称：** 检验结果_样本-子表
- **表名：** t_qcpp_joininspsamp_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fsampleres | 样本检验结果 | varchar | 5 |  | √ | ' ' | 样本检验结果,枚举: Y :合格 N :不合格 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fsamplenum | 样本编号 | varchar | 50 |  | √ | ' ' | 样本编号 |
| 5 | fsampckval | 实测值（数量） | numeric | 23 | 10 | √ | 0 | 实测值（数量） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fsamplenumid | 样本编号ID | int8 | 64 |  | √ | 0 | 样本编号ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_joinmp_fentryid |  | fentryid |
| 2 | idx_qcpp_joinmp_fseq |  | fseq |
| 3 | pk_qcpp_joininspsamp_n |  | fdetailid |

---

## 生产联合检验单-关联追踪表 t_qcpp_joininspect_tc

- **表名称：** 生产联合检验单-关联追踪表
- **表名：** t_qcpp_joininspect_tc

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
| 1 | pk_qcpp_joininspect_tc |  | fid |
| 2 | idx_qcpp_joininspect_tc_tbill |  | ftbillid |
| 3 | idx_qcpp_joininspect_tc_tid |  | ftid |

---

## 生产联合检验单-反写记录表 t_qcpp_joininspect_wb

- **表名称：** 生产联合检验单-反写记录表
- **表名：** t_qcpp_joininspect_wb

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
| 1 | idx_qcpp_joininspect_wb_fk |  | fid |
| 2 | pk_qcpp_joininspect_wb |  | fentryid |

---

## 样本检验结果_项目样本关系-子表 t_qcpp_joininsprela_n

- **表名称：** 样本检验结果_项目样本关系-子表
- **表名：** t_qcpp_joininsprela_n

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalratstr | 实测值(定量) | varchar | 50 |  | √ | ' ' | 实测值(定量) |
| 2 | fvaldeter | 实测值（定性） | varchar | 5 |  | √ | ' ' | 实测值（定性）,枚举: Y :合格 N :不合格 |
| 3 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fsamp_seq | 按项目录入-样本实测值流水号 | int4 | 32 |  | √ | 0 | 按项目录入-样本实测值流水号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprojuuid | 按项目分录唯一标识 | varchar | 50 |  | √ | ' ' | 按项目分录唯一标识 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fjudge | 实测值判定结果 | varchar | 5 |  | √ | ' ' | 实测值判定结果,枚举: Y :合格 N :不合格 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fexmapleid | 样本编号ID | int8 | 64 |  | √ | 0 | 样本编号ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_joinla_fentryid |  | fentryid |
| 2 | pk_qcpp_joininsprela_n |  | fdetailid |
| 3 | idx_qcpp_joinla_fseq |  | fseq |

---

## 物料信息-子表 t_qcpp_joininspentry

- **表名称：** 物料信息-子表
- **表名：** t_qcpp_joininspentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialcfgid | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 3 | fsrcsystem | 来源系统 | varchar | 10 |  | √ | ' ' | 来源系统 |
| 4 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 5 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 6 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 7 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 8 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fmainbillentity | 核心单据实体 | varchar | 30 |  | √ | ' ' | 核心单据实体 |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 14 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 15 | ffinishtime | 期望完成时间 | timestamp | 0 |  |  | null | 期望完成时间 |
| 16 | foproperationid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 17 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fsrcbillentity | 来源单据实体 | varchar | 30 |  | √ | ' ' | 来源单据实体 |
| 21 | fsupplydepid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fsrcbillnumber | 来源单据编号 | varchar | 30 |  | √ | ' ' | 来源单据编号 |
| 23 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 25 | fmainbillnumber | 核心单据编号 | varchar | 30 |  | √ | ' ' | 核心单据编号 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 28 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 29 | fproposerid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 31 | finspectionstdid | 检验标准 | int8 | 64 |  | √ | 0 | [检验标准 qcbd_inspectionstd](../qcbd_files/qcbd_inspectionstd.md) |
| 32 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 33 | fqrouteid | 工艺路线编码 | int8 | 64 |  | √ | 0 | [质量工艺路线 qcbd_qmcroute](../qcbd_files/qcbd_qmcroute.md) |
| 34 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 35 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 36 | frinsqty | 样本数量 | numeric | 23 | 10 | √ | 0 | 样本数量 |
| 37 | fsupplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | fsrcbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 40 | fprocessseq | 工序序列号 | varchar | 50 |  | √ | ' ' | 工序序列号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_joinry_fid |  | fid |
| 2 | idx_qcpp_joinry_fmat |  | fmaterialid |
| 3 | idx_qcpp_joinry_fseq |  | fseq |
| 4 | pk_qcpp_joininspentry |  | fentryid |
| 5 | idx_qcpp_joinry_fmatcfg |  | fmaterialcfgid |

---

## 检验信息-子表 t_qcpp_joininspproj

- **表名称：** 检验信息-子表
- **表名：** t_qcpp_joininspproj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finspectinstructid | 检验仪器 | int8 | 64 |  | √ | 0 | [检验仪器 qcbd_inspectioninstru](../qcbd_files/qcbd_inspectioninstru.md) |
| 2 | fprojckval | 实测值(数量) | numeric | 23 | 10 | √ | 0 | 实测值(数量) |
| 3 | finspectioncontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 4 | fnormtype | 指标类型 | varchar | 5 |  | √ | ' ' | 指标类型,枚举: A :定量 B :定性 |
| 5 | fspecvalue | 标准值 | varchar | 50 |  | √ | ' ' | 标准值 |
| 6 | fprojckresult | 项目检验结果 | varchar | 5 |  | √ | ' ' | 项目检验结果,枚举: Y :合格 N :不合格 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftopvalue | 上限值 | numeric | 23 | 10 |  | null | 上限值 |
| 9 | fsrcitementity | 检验项来源实体 | varchar | 30 |  | √ | ' ' | 检验项来源实体 |
| 10 | finspeccomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | fjoindeptid | 联合检验部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | finspectbasisid | 检验依据 | int8 | 64 |  | √ | 0 | [检验依据 qcbd_inspectioncrit](../qcbd_files/qcbd_inspectioncrit.md) |
| 13 | fprojsampqty | 项目样本数量 | numeric | 23 | 10 | √ | 0 | 项目样本数量 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fprojqualifiyqty | 项目合格数 | numeric | 23 | 10 | √ | 0 | 项目合格数 |
| 16 | finspectmethodid | 检验方法 | int8 | 64 |  | √ | 0 | [检验方法 qcbd_inspectionmethod](../qcbd_files/qcbd_inspectionmethod.md) |
| 17 | fcomparisonid | 比较符 | int8 | 64 |  | √ | 0 | [比较符 qcbd_matchflag](../qcbd_files/qcbd_matchflag.md) |
| 18 | fdownvalue | 下限值 | numeric | 23 | 10 |  | null | 下限值 |
| 19 | finspectionitemid | 检验项目 | int8 | 64 |  | √ | 0 | [检验项目 qcbd_inspectionitems](../qcbd_files/qcbd_inspectionitems.md) |
| 20 | fisjoininspect | 联合检验项 | bpchar | 1 |  | √ | '0' | 联合检验项 |
| 21 | fuquuid | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |
| 22 | fjoininspectorid | 联合检验员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fsrcitementryid | 检验项来源分录id | int8 | 64 |  | √ | 0 | 检验项来源分录id |
| 24 | fexamples | 实测值导入过程字段 | varchar | 255 |  | √ | ' ' | 实测值导入过程字段 |
| 25 | finspecunitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fprojacceptqty | 项目允收数 | numeric | 23 | 10 | √ | 0 | 项目允收数 |
| 27 | fkeyquality | 特性分类 | varchar | 5 |  | √ | ' ' | 特性分类,枚举: A :关键特性 C :重要特性 B :一般特性 |
| 28 | fprojsampid | 项目抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 29 | fchoosesampqty | 选择样本数量 | numeric | 23 | 10 | √ | 0 | 选择样本数量 |
| 30 | finspectfreqid | 检验频率 | int8 | 64 |  | √ | 0 | [检验频率 qcbd_inspectionfreq](../qcbd_files/qcbd_inspectionfreq.md) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fprojunqualifiyqty | 项目不合格数 | numeric | 23 | 10 | √ | 0 | 项目不合格数 |
| 33 | fexamples_tag | 实测值导入过程字段_详情 | text | 0 |  |  | null | 实测值导入过程字段_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_joinoj_fseq |  | fseq |
| 2 | idx_qcpp_joinoj_fentryid |  | fentryid |
| 3 | pk_qcpp_joininspproj |  | fdetailid |

---

## 生产联合检验单-主表 t_qcpp_joininspect

- **表名称：** 生产联合检验单-主表
- **表名：** t_qcpp_joininspect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 qcbd_biztype](../qcbd_files/qcbd_biztype.md) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_joinct_fbillno |  | fbillno |
| 2 | pk_qcpp_joininspect |  | fid |
| 3 | idx_qcpp_joinct_fcreatetime |  | fcreatetime |

---

## 关联子实体-子表 t_qcpp_joininspentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcpp_joininspentry_lk

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
| 1 | pk_qcpp_joininspentry_lk |  | fpkid |
| 2 | idx_qcpp_joininspentry_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_qcp_joininspproj_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_joininspproj_lk

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
| 1 | pk_qcp_joininspproj_lk |  | fpkid |
| 2 | idx_qcp_joininspproj_lk_fk |  | fdetailid |
