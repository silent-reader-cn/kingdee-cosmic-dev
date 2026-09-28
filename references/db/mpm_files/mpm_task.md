# 项目任务-mpm_task

## 关联子实体-子表 t_mpm_taskentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_taskentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskentry_lk |  | fpkid |
| 2 | idx_mpm_taskentry_lk_fk |  | fentryid |

---

## 关联风险单据体-子表 t_mpm_taskriskentry

- **表名称：** 关联风险单据体-子表
- **表名：** t_mpm_taskriskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frisk | 风险编码 | int8 | 64 |  | √ | 0 | [项目风险f7 mpm_risk_f7](../mpm_files/mpm_risk_f7.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_taskriskentry |  | fentryid |
| 2 | idx_taskriskentry_id |  | fid |

---

## 协作人-多选基础资料表 t_mpm_taskcollab

- **表名称：** 协作人-多选基础资料表
- **表名：** t_mpm_taskcollab

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
| 1 | pk_mpm_taskcollab |  | fpkid |
| 2 | idx_mpm_taskcollab |  | fid |

---

## 关联子实体-子表 t_mpm_task_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_task_lk

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
| 1 | pk_mpm_task_lk |  | fpkid |
| 2 | idx_mpm_task_lk_fk |  | fid |

---

## 子单据体-子表 t_mpm_taskbomsubentry

- **表名称：** 子单据体-子表
- **表名：** t_mpm_taskbomsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftopbomid | 顶层bom编码id | int8 | 64 |  |  | 0 | 顶层bom编码id |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fbomexpandpath | BOM展开路径 | varchar | 2000 |  | √ | ' ' | BOM展开路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_taskbom_fentry |  | fentryid |
| 2 | pk_mpm_taskbomsubentry |  | fdetailid |

---

## 项目任务-主表 t_mpm_task

- **表名称：** 项目任务-主表
- **表名：** t_mpm_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flaststartdate | 最晚开始日期 | timestamp | 0 |  |  | null | 最晚开始日期 |
| 3 | fisleaf | 叶节点 | bpchar | 1 |  | √ | '1' | 叶节点 |
| 4 | ftaskseq | 顺序号(已废弃) | int4 | 32 |  | √ | 0 | 顺序号(已废弃) |
| 5 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 6 | fdeviationrate | 偏差率(%) | numeric | 23 | 10 | √ | 0 | 偏差率(%) |
| 7 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fplanedhours | 已排期工时(小时) | numeric | 23 | 10 | √ | 0 | 已排期工时(小时) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 11 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 12 | flastenddate | 最晚完成日期 | timestamp | 0 |  |  | null | 最晚完成日期 |
| 13 | fassignerid | 分配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 项目任务号 | varchar | 80 |  | √ | ' ' | 项目任务号 |
| 15 | fcopysrcid | 复制源任务id | int8 | 64 |  | √ | 0 | 复制源任务id |
| 16 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 17 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 20 | flockdate | 锁定日期 | bpchar | 1 |  | √ | '0' | 锁定日期 |
| 21 | freporthours | 已报工时(小时) | numeric | 23 | 10 | √ | 0 | 已报工时(小时) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fsrctype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: A :复制 B :导入 C :模板 D :BOM |
| 24 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 25 | ftimeunit | 时间单位 | bpchar | 1 |  | √ | 'A' | 时间单位,枚举: A :天 B :小时 C :分钟 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fprojectphaseid | 阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 28 | fpriority | 优先级 | bpchar | 1 |  | √ | ' ' | 优先级,枚举: 1 :特高 2 :高 3 :中 4 :低 |
| 29 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 30 | fprjapprovalbillid | 项目立项单id | int8 | 64 |  | √ | 0 | 项目立项单id |
| 31 | ftaskcntrcodeid | 业务类型 | int8 | 64 |  | √ | 0 | [任务业务类型 mpm_taskcntrcode](../mpm_files/mpm_taskcntrcode.md) |
| 32 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisphase | 阶段标识 | bpchar | 1 |  | √ | '0' | 阶段标识 |
| 35 | fschedule | 进度(%) | numeric | 23 | 10 | √ | 0 | 进度(%) |
| 36 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 37 | fdurationsec | 工期（秒） | numeric | 23 | 10 | √ | 0 | 工期（秒） |
| 38 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fparentid | 上级任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fganttid | 甘特图id | varchar | 36 |  | √ | ' ' | 甘特图id |
| 45 | fsrcbillentryid | 来源单据分录id | int8 | 64 |  | √ | 0 | 来源单据分录id |
| 46 | fassigntime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 47 | fplanhours | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 48 | fduration | 工期(天) | numeric | 23 | 10 | √ | 0 | 工期(天) |
| 49 | ftaskstatusid | 任务状态 | int8 | 64 |  | √ | 0 | [任务状态 mpm_taskstatus](../mpm_files/mpm_taskstatus.md) |
| 50 | frootid | 根节点 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 51 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_task_fbillno |  | fbillno,fcreateorgid |
| 2 | idx_mpm_task_fparent |  | fparentid |
| 3 | idx_mpm_task_froot |  | frootid |
| 4 | pk_mpm_task |  | fid |
| 5 | idx_mpm_task_fprj |  | fprojectid |

---

## 物料和服务-子表 t_mpm_taskentry

- **表名称：** 物料和服务-子表
- **表名：** t_mpm_taskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 3 | fmaterialid | 物料（主数据） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fesrcbillentryid | 源单分录行ID | int8 | 64 |  | √ | 0 | 源单分录行ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | frelbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 8 | fprdmaterialid | 物料生产信息 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 9 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fesrcbillseq | 源单行号 | int4 | 32 |  | √ | 0 | 源单行号 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | fweight | 权重 | int4 | 32 |  | √ | 1 | 权重 |
| 13 | fisbomexpand | BOM展开 | bpchar | 1 |  | √ | '0' | BOM展开 |
| 14 | foffsettime | 需求时间偏移量 | numeric | 23 | 10 | √ | 0 | 需求时间偏移量 |
| 15 | ffinishbaseqty | 已完成基本数量 | numeric | 23 | 10 | √ | 0 | 已完成基本数量 |
| 16 | flinemode | 行标识 | bpchar | 1 |  | √ | ' ' | 行标识,枚举: A :产品 B :子项 |
| 17 | fesrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 18 | fownertype | 货主类型 | varchar | 80 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | ffinishqty | 已完成数量 | numeric | 23 | 10 | √ | 0 | 已完成数量 |
| 24 | fqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 25 | fpurmaterialid | 物料采购信息 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 26 | fpurorgid | 建议采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | frelqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | finvmaterialid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fesrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 32 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 33 | finvorgid | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | foutbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 35 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 38 | foffsetunitid | 偏移单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 40 | fplantype | 计划方式 | bpchar | 1 |  | √ | 'A' | 计划方式,枚举: A :根据完成日期 B :根据开始日期 |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 42 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 46 | frequiredtime | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 47 | fesrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_taskentry |  | fid,fseq |
| 2 | pk_mpm_taskentry |  | fentryid |

---

## 关联PLM单据体-子表 t_mpm_taskplmentry

- **表名称：** 关联PLM单据体-子表
- **表名：** t_mpm_taskplmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelplmtaskid | 关联PLM任务id | int8 | 64 |  | √ | 0 | 关联PLM任务id |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fplmrelmethod | 关联方式 | bpchar | 1 |  | √ | ' ' | 关联方式,枚举: A :PLM项目 B :PLM任务 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fplmprojectid | PLM项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_taskplment_fid |  | fid |
| 2 | pk_mpm_taskplmentry |  | fentryid |

---

## 关联问题单据体-子表 t_mpm_taskissueentry

- **表名称：** 关联问题单据体-子表
- **表名：** t_mpm_taskissueentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissue | 问题编码 | int8 | 64 |  | √ | 0 | [项目问题f7 mpm_issue_f7](../mpm_files/mpm_issue_f7.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_taskissueentry |  | fentryid |
| 2 | idx_mpm_taskissueentry_id |  | fid |

---

## 项目任务-反写记录表 t_mpm_task_wb

- **表名称：** 项目任务-反写记录表
- **表名：** t_mpm_task_wb

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
| 1 | idx_mpm_task_wb_fk |  | fid |
| 2 | pk_mpm_task_wb |  | fentryid |

---

## 项目任务-关联追踪表 t_mpm_task_tc

- **表名称：** 项目任务-关联追踪表
- **表名：** t_mpm_task_tc

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
| 1 | idx_mpm_task_tc_tbill |  | ftbillid |
| 2 | pk_mpm_task_tc |  | fid |
| 3 | idx_mpm_task_tc_tid |  | ftid |

---

## 项目任务-分表 t_mpm_task_a

- **表名称：** 项目任务-分表
- **表名：** t_mpm_task_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmode | 计划模式 | bpchar | 1 |  | √ | 'A' | 计划模式,枚举: A :自动计划 B :手工计划 |
| 3 | fpublishstatus | 发布标识 | bpchar | 1 |  | √ | ' ' | 发布标识,枚举: 0 :未发布 1 :已发布 |
| 4 | fisinworkflow | 流程中 | bpchar | 1 |  | √ | '0' | 流程中 |
| 5 | frelplmprojecth | 关联PLM项目 | varchar | 512 |  | √ | ' ' | 关联PLM项目 |
| 6 | fsourcetype | 任务类别 | bpchar | 1 |  | √ | 'A' | 任务类别,枚举: A :任务 B :模板任务 |
| 7 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 8 | fcooperatestatus | 协同编制标识 | bpchar | 1 |  | √ | ' ' | 协同编制标识,枚举: A :协同编制中 B :协同编制完成 |
| 9 | fcalcduration | 计算工期(用于后台计算) | numeric | 23 | 10 | √ | 0 | 计算工期(用于后台计算) |
| 10 | frelatedbasetaskid | 关联基础任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 11 | fiskeytask | 关键任务 | bpchar | 1 |  | √ | '0' | 关键任务 |
| 12 | frelparentmilestoneid | 父项目里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_task_a |  | fid |
| 2 | idx_mpm_task_atask |  | frelatedbasetaskid |
| 3 | pk_mpm_task_a |  | fid |

---

## 项目任务-分表 t_mpm_task_e

- **表名称：** 项目任务-分表
- **表名：** t_mpm_task_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustfield031 | 自定义复选框001 | bpchar | 1 |  | √ | '0' | 自定义复选框001 |
| 3 | fcustfield030 | 自定义日期005 | timestamp | 0 |  |  | null | 自定义日期005 |
| 4 | fcustfield011 | 自定义文本011 | varchar | 80 |  | √ | ' ' | 自定义文本011 |
| 5 | fcustfield033 | 自定义复选框003 | bpchar | 1 |  | √ | '0' | 自定义复选框003 |
| 6 | fcustfield010 | 自定义文本010 | varchar | 80 |  | √ | ' ' | 自定义文本010 |
| 7 | fcustfield032 | 自定义复选框002 | bpchar | 1 |  | √ | '0' | 自定义复选框002 |
| 8 | fcustfield017 | 自定义文本017 | varchar | 80 |  | √ | ' ' | 自定义文本017 |
| 9 | fcustfield016 | 自定义文本016 | varchar | 80 |  | √ | ' ' | 自定义文本016 |
| 10 | fcustfield019 | 自定义文本019 | varchar | 80 |  | √ | ' ' | 自定义文本019 |
| 11 | fcustfield018 | 自定义文本018 | varchar | 80 |  | √ | ' ' | 自定义文本018 |
| 12 | fcustfield013 | 自定义文本013 | varchar | 80 |  | √ | ' ' | 自定义文本013 |
| 13 | fcustfield035 | 自定义复选框005 | bpchar | 1 |  | √ | '0' | 自定义复选框005 |
| 14 | fcustfield012 | 自定义文本012 | varchar | 80 |  | √ | ' ' | 自定义文本012 |
| 15 | fcustfield034 | 自定义复选框004 | bpchar | 1 |  | √ | '0' | 自定义复选框004 |
| 16 | fcustfield015 | 自定义文本015 | varchar | 80 |  | √ | ' ' | 自定义文本015 |
| 17 | fcustfield014 | 自定义文本014 | varchar | 80 |  | √ | ' ' | 自定义文本014 |
| 18 | fcustfield020 | 自定义文本020 | varchar | 80 |  | √ | ' ' | 自定义文本020 |
| 19 | fcustfield022 | 自定义数字002 | numeric | 23 | 10 | √ | 0 | 自定义数字002 |
| 20 | fcustfield021 | 自定义数字001 | numeric | 23 | 10 | √ | 0 | 自定义数字001 |
| 21 | fcustfield009 | 自定义文本009 | varchar | 80 |  | √ | ' ' | 自定义文本009 |
| 22 | fcustfield006 | 自定义文本006 | varchar | 80 |  | √ | ' ' | 自定义文本006 |
| 23 | fcustfield028 | 自定义日期003 | timestamp | 0 |  |  | null | 自定义日期003 |
| 24 | fcustfield005 | 自定义文本005 | varchar | 80 |  | √ | ' ' | 自定义文本005 |
| 25 | fcustfield027 | 自定义日期002 | timestamp | 0 |  |  | null | 自定义日期002 |
| 26 | fcustfield008 | 自定义文本008 | varchar | 80 |  | √ | ' ' | 自定义文本008 |
| 27 | fcustfield007 | 自定义文本007 | varchar | 80 |  | √ | ' ' | 自定义文本007 |
| 28 | fcustfield029 | 自定义日期004 | timestamp | 0 |  |  | null | 自定义日期004 |
| 29 | fcustfield002 | 自定义文本002 | varchar | 80 |  | √ | ' ' | 自定义文本002 |
| 30 | fcustfield024 | 自定义数字004 | numeric | 23 | 10 | √ | 0 | 自定义数字004 |
| 31 | fcustfield001 | 自定义文本001 | varchar | 80 |  | √ | ' ' | 自定义文本001 |
| 32 | fcustfield023 | 自定义数字003 | numeric | 23 | 10 | √ | 0 | 自定义数字003 |
| 33 | fcustfield004 | 自定义文本004 | varchar | 80 |  | √ | ' ' | 自定义文本004 |
| 34 | fcustfield026 | 自定义日期001 | timestamp | 0 |  |  | null | 自定义日期001 |
| 35 | fcustfield003 | 自定义文本003 | varchar | 80 |  | √ | ' ' | 自定义文本003 |
| 36 | fcustfield025 | 自定义数字005 | numeric | 23 | 10 | √ | 0 | 自定义数字005 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_task_e |  | fid |

---

## 项目任务-多语言表 t_mpm_task_l

- **表名称：** 项目任务-多语言表
- **表名：** t_mpm_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 4 | ftaskstatusinwf | 任务状态(流程中) | varchar | 255 |  | √ | ' ' | 任务状态(流程中) |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_task_l |  | fpkid |
| 2 | idx_mpm_task_l |  | fid,flocaleid |

---

## 物料和服务-分表 t_mpm_taskentry_a

- **表名称：** 物料和服务-分表
- **表名：** t_mpm_taskentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismrpcal | MRP计算 | bpchar | 1 |  | √ | '1' | MRP计算 |
| 3 | fbondcontrol | 保税控制 | bpchar | 1 |  | √ | '0' | 保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 5 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskentrya |  | fentryid |
| 2 | idx_mpm_taskentrya |  | fid |

---

## 项目任务-分表 t_mpm_task_t

- **表名称：** 项目任务-分表
- **表名：** t_mpm_task_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescription_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |
| 3 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_task_t |  | fid |
| 2 | idx_mpm_task_t |  | fid |

---

## 协同编制人-多选基础资料表 t_mpm_taskcooperator

- **表名称：** 协同编制人-多选基础资料表
- **表名：** t_mpm_taskcooperator

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
| 1 | idx_mpm_taskcoop |  | fid |
| 2 | pk_mpm_taskcoop |  | fpkid |
