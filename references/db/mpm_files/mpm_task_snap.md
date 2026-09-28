# 项目任务快照-mpm_task_snap

## 项目任务快照-反写记录表 t_mpm_task_snap_wb

- **表名称：** 项目任务快照-反写记录表
- **表名：** t_mpm_task_snap_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 子单据体-子表 t_mpm_taskbomsentry_snap

- **表名称：** 子单据体-子表
- **表名：** t_mpm_taskbomsentry_snap

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
| 1 | idx_mpm_bomsesnap_fey |  | fentryid |
| 2 | pk_mpm_taskbomsentry_snap |  | fdetailid |

---

## 项目任务快照-分表 t_mpm_task_snap_t

- **表名称：** 项目任务快照-分表
- **表名：** t_mpm_task_snap_t

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
| 1 | pk_t_mpm_task_snap_t |  | fid |
| 2 | idx_mpmc_task_snap_desc |  | fdescription |

---

## 项目任务快照-多语言表 t_mpm_task_snap_l

- **表名称：** 项目任务快照-多语言表
- **表名：** t_mpm_task_snap_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 4 | ftaskstatusinwf | 任务状态(流程中) | varchar | 50 |  | √ | ' ' | 任务状态(流程中) |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_task_snap_l |  | fpkid |
| 2 | idx_mpmc_tasksnap_l_id |  | fid |

---

## 项目任务快照-分表 t_mpm_task_snap_e

- **表名称：** 项目任务快照-分表
- **表名：** t_mpm_task_snap_e

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
| 1 | pk_t_mpm_task_snap_e |  | fid |
| 2 | idx_mpmc_taskspe_c |  | fcustfield001 |

---

## 项目任务快照-分表 t_mpm_task_snap_a

- **表名称：** 项目任务快照-分表
- **表名：** t_mpm_task_snap_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmode | 计划模式 | varchar | 50 |  | √ | ' ' | 计划模式,枚举: A :自动计划 B :手工计划 |
| 3 | fpublishstatus | 发布标识 | varchar | 50 |  | √ | ' ' | 发布标识,枚举: 0 :未发布 1 :已发布 |
| 4 | fisinworkflow | 流程中 | bpchar | 1 |  | √ | '0' | 流程中 |
| 5 | fcalcduration | 计算工期(用于后台计算) | numeric | 23 | 10 | √ | 0 | 计算工期(用于后台计算) |
| 6 | frelatedbasetaskid | 关联基础任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 7 | frelparentmilestoneid | 父项目里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 8 | fsrctaskid | 源项目任务id | int8 | 64 |  | √ | 0 | 源项目任务id |
| 9 | frelplmprojecth | 关联PLM项目 | varchar | 512 |  | √ | ' ' | 关联PLM项目 |
| 10 | fsourcetype | 任务类别 | varchar | 50 |  | √ | ' ' | 任务类别,枚举: A :任务 B :模板任务 |
| 11 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 12 | fcooperatestatus | 协同编制标识 | varchar | 50 |  | √ | ' ' | 协同编制标识,枚举: A :协同编制中 B :协同编制完成 |
| 13 | fiskeytask | 关键任务 | bpchar | 1 |  | √ | '0' | 关键任务 |
| 14 | fplanversionid | 计划版本 | int8 | 64 |  | √ | 0 | [计划版本f7 mpm_planversion_f7](../mpm_files/mpm_planversion_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpmc_planversionid |  | fplanversionid |
| 2 | pk_t_mpm_task_snap_a |  | fid |

---

## 物料和服务-子表 t_mpm_taskentry_snap

- **表名称：** 物料和服务-子表
- **表名：** t_mpm_taskentry_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutqty | 已出库数量 | numeric | 23 | 10 | √ | 0 | 已出库数量 |
| 3 | fmaterialid | 物料（主数据） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fesrcbillentryid | 源单分录行ID | int8 | 64 |  | √ | 0 | 源单分录行ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frelbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 8 | fprdmaterialid | 物料生产信息 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 9 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fesrcbillseq | 源单行号 | int8 | 64 |  | √ | 0 | 源单行号 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | fweight | 权重 | int8 | 64 |  | √ | 0 | 权重 |
| 13 | fisbomexpand | BOM展开 | bpchar | 1 |  | √ | ' ' | BOM展开 |
| 14 | foffsettime | 需求时间偏移量 | numeric | 23 | 10 | √ | 0 | 需求时间偏移量 |
| 15 | ffinishbaseqty | 已完成基本数量 | numeric | 23 | 10 | √ | 0 | 已完成基本数量 |
| 16 | flinemode | 行标识 | varchar | 50 |  | √ | ' ' | 行标识,枚举: A :产品 B :子项 |
| 17 | fesrcbillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 18 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 19 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 20 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 21 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | ffinishqty | 已完成数量 | numeric | 23 | 10 | √ | 0 | 已完成数量 |
| 24 | fqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 25 | fpurmaterialid | 物料采购信息 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 26 | fpurorgid | 建议采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | frelqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | finvmaterialid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fesrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 32 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 33 | finvorgid | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | foutbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0 | 已出库基本数量 |
| 35 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 38 | foffsetunitid | 偏移单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 40 | fplantype | 计划方式 | varchar | 50 |  | √ | ' ' | 计划方式,枚举: A :根据完成日期 B :根据开始日期 |
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
| 1 | pk_t_mpm_taskentry_snap |  | fentryid |
| 2 | idx_mpmc_taskentry_id |  | fid |

---

## 项目任务快照-主表 t_mpm_task_snap

- **表名称：** 项目任务快照-主表
- **表名：** t_mpm_task_snap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flaststartdate | 最晚开始日期 | timestamp | 0 |  |  | null | 最晚开始日期 |
| 3 | fisleaf | 叶节点 | bpchar | 1 |  | √ | '0' | 叶节点 |
| 4 | ftaskseq | 顺序号(已废弃) | int8 | 64 |  | √ | 0 | 顺序号(已废弃) |
| 5 | factualenddate | 实际完成日期 | timestamp | 0 |  |  | null | 实际完成日期 |
| 6 | fdeviationrate | 偏差率(%) | numeric | 23 | 10 | √ | 0 | 偏差率(%) |
| 7 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fenddate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 10 | ftaskstatusinwf | 任务状态(流程中) | varchar | 50 |  | √ | ' ' | 任务状态(流程中) |
| 11 | flastenddate | 最晚完成日期 | timestamp | 0 |  |  | null | 最晚完成日期 |
| 12 | fassignerid | 分配人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 项目任务号 | varchar | 30 |  | √ | ' ' | 项目任务号 |
| 14 | fcopysrcid | 复制源任务id | int8 | 64 |  | √ | 0 | 复制源任务id |
| 15 | fname | 项目任务名称 | varchar | 255 |  | √ | ' ' | 项目任务名称 |
| 16 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 19 | flockdate | 锁定日期 | bpchar | 1 |  | √ | '0' | 锁定日期 |
| 20 | freporthours | 已报工时(小时) | numeric | 23 | 10 | √ | 0 | 已报工时(小时) |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :复制 B :导入 C :模板 D :BOM |
| 23 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | ftimeunit | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: A :天 B :小时 C :分钟 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fprojectphaseid | 阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 27 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: 1 :特高 2 :高 3 :中 4 :低 |
| 28 | factualstartdate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 29 | fprjapprovalbillid | 项目立项单id | int8 | 64 |  | √ | 0 | 项目立项单id |
| 30 | ftaskcntrcodeid | 业务类型 | int8 | 64 |  | √ | 0 | [任务业务类型 mpm_taskcntrcode](../mpm_files/mpm_taskcntrcode.md) |
| 31 | frelprojectid | 关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fisphase | 阶段标识 | bpchar | 1 |  | √ | '0' | 阶段标识 |
| 34 | fschedule | 进度(%) | numeric | 23 | 10 | √ | 0 | 进度(%) |
| 35 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 36 | fdurationsec | 工期（秒） | numeric | 23 | 10 | √ | 0 | 工期（秒） |
| 37 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fmanagerid | 负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fparentid | 上级任务 | int8 | 64 |  | √ | 0 | [项目任务快照F7 mpm_task_snap_f7](../mpm_files/mpm_task_snap_f7.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fganttid | 甘特图id | varchar | 50 |  | √ | ' ' | 甘特图id |
| 44 | fsrcbillentryid | 来源单据分录id | int8 | 64 |  | √ | 0 | 来源单据分录id |
| 45 | fassigntime | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 46 | fplanhours | 计划工时(小时) | numeric | 23 | 10 | √ | 0 | 计划工时(小时) |
| 47 | fduration | 工期(天) | numeric | 23 | 10 | √ | 0 | 工期(天) |
| 48 | ftaskstatusid | 任务状态 | int8 | 64 |  | √ | 0 | [任务状态 mpm_taskstatus](../mpm_files/mpm_taskstatus.md) |
| 49 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |
| 50 | frootid | 根节点 | int8 | 64 |  | √ | 0 | [项目任务快照F7 mpm_task_snap_f7](../mpm_files/mpm_task_snap_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_task_snap |  | fid |
| 2 | idx_mpmc_projectid |  | fprojectid |

---

## 协同编制人-多选基础资料表 t_mpm_taskcooperator_snap

- **表名称：** 协同编制人-多选基础资料表
- **表名：** t_mpm_taskcooperator_snap

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
| 1 | pk_t_mpm_taskcooperator_snap |  | fpkid |
| 2 | idx_mpmc_taskcooperator_id |  | fid |

---

## 协作人-多选基础资料表 t_mpm_taskcollab_snap

- **表名称：** 协作人-多选基础资料表
- **表名：** t_mpm_taskcollab_snap

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
| 1 | pk_t_mpm_taskcollab_snap |  | fpkid |
| 2 | idx_mpmc_taskcollab_id |  | fid |

---

## 关联PLM单据体-子表 t_mpm_taskplment_snap

- **表名称：** 关联PLM单据体-子表
- **表名：** t_mpm_taskplment_snap

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
| 1 | idx_mpm_taskplmsnap_ent |  | fid |
| 2 | pk_mpm_taskplment_snap |  | fentryid |

---

## 项目任务快照-关联追踪表 t_mpm_task_snap_tc

- **表名称：** 项目任务快照-关联追踪表
- **表名：** t_mpm_task_snap_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 物料和服务-分表 t_mpm_taskentry_snap_a

- **表名称：** 物料和服务-分表
- **表名：** t_mpm_taskentry_snap_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismrpcal | MRP计算 | bpchar | 1 |  | √ | ' ' | MRP计算 |
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
| 1 | pk_t_mpm_taskentry_snap_a |  | fentryid |
| 2 | idx_mpmc_taskentry_a_id |  | fid |
