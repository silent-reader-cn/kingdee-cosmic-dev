# 工单合并处理-pom_ordermerge

## 目标生产工单-分表 t_pom_mgtarentry_e

- **表名称：** 目标生产工单-分表
- **表名：** t_pom_mgtarentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqtymg | 计划数量 | numeric | 23 | 10 | √ | 0 | 计划数量 |
| 3 | fplanbaseqtymg | 计划基本数量 | numeric | 23 | 10 | √ | 0 | 计划基本数量 |
| 4 | frepmaxratemg | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 5 | fbeginbdtmg | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 6 | fsplitqtymg | 已拆分/改制数量 | numeric | 23 | 10 | √ | 0 | 已拆分/改制数量 |
| 7 | frepmaxqtymg | 汇报上限数量 | numeric | 23 | 10 | √ | 0 | 汇报上限数量 |
| 8 | frepminqtymg | 汇报下限数量 | numeric | 23 | 10 | √ | 0 | 汇报下限数量 |
| 9 | fclosebdtmg | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 10 | fsplitbaseqtymg | 已拆分/改制基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分/改制基本数量 |
| 11 | frepminratemg | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报下限允差（%） |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_mgtarentry_e |  | fentryid |
| 2 | idx_pom_mgtarye_fid |  | fid |

---

## 关联子实体-子表 t_pom_ordermgsrcentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_ordermgsrcentry_lk

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
| 1 | idx_pom_ordermgsrcentry_lk_fk |  | fentryid |
| 2 | pk_pom_ordermgsrcentry_lk |  | fpkid |

---

## 工单合并处理-反写记录表 t_pom_ordermerge_wb

- **表名称：** 工单合并处理-反写记录表
- **表名：** t_pom_ordermerge_wb

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
| 1 | pk_pom_ordermerge_wb |  | fentryid |
| 2 | idx_pom_ordermerge_wb_fk |  | fid |

---

## 源生产工单-分表 t_pom_mgsrcentry_e

- **表名称：** 源生产工单-分表
- **表名：** t_pom_mgsrcentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | 计划数量 | numeric | 23 | 10 | √ | 0 | 计划数量 |
| 3 | frepminqty | 汇报下限数量 | numeric | 23 | 10 | √ | 0 | 汇报下限数量 |
| 4 | fsplitbaseqty | 已拆分/改制基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分/改制基本数量 |
| 5 | fbeginbdt | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 6 | frepmaxqty | 汇报上限数量 | numeric | 23 | 10 | √ | 0 | 汇报上限数量 |
| 7 | frepminrate | 汇报下限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报下限允差（%） |
| 8 | fclosebdt | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 9 | fplanbaseqty | 计划基本数量 | numeric | 23 | 10 | √ | 0 | 计划基本数量 |
| 10 | frepmaxrate | 汇报上限允差（%） | numeric | 23 | 10 | √ | 0 | 汇报上限允差（%） |
| 11 | fsplitqty | 已拆分/改制数量 | numeric | 23 | 10 | √ | 0 | 已拆分/改制数量 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_mgsrcentry_e |  | fentryid |
| 2 | idx_pom_mgoses_fid |  | fid |

---

## 源生产工单-子表 t_pom_mgsrcentry

- **表名称：** 源生产工单-子表
- **表名：** t_pom_mgsrcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 3 | fiscontrolqty | 控制入库数量 | bpchar | 1 |  | √ | ' ' | 控制入库数量 |
| 4 | forderid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 5 | fbizstatus | 业务状态 | varchar | 1 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fyieldrate | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | forderentryid | 生产工单分录 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 10 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | ' ' | 重新展算订单物料 |
| 11 | fmappingid | 关联分录id | varchar | 50 |  | √ | ' ' | 关联分录id |
| 12 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 14 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 15 | fqualityorgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 17 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 18 | ftaskstatus | 任务状态 | varchar | 1 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 21 | fauxptyunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | finllimit | 入库下限允差（%） | numeric | 23 | 10 | √ | 0 | 入库下限允差（%） |
| 24 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 25 | fproducedeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fipid | ipid | int8 | 64 |  | √ | 0 | ipid |
| 27 | fisconrpttqty | 控制汇报数量 | bpchar | 1 |  | √ | '0' | 控制汇报数量 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | finwardeptid | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | forderno | 源生产工单编号 | varchar | 50 |  | √ | ' ' | 源生产工单编号 |
| 32 | fproducttype | 产品类型 | varchar | 5 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 33 | fplanstatus | 计划状态 | varchar | 1 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 34 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 35 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 36 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 37 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 38 | fproductid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 39 | finhlimit | 入库上限允差（%） | numeric | 23 | 10 | √ | 0 | 入库上限允差（%） |
| 40 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 42 | fmanuversionid | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 43 | fisinspection | 产品检验 | bpchar | 1 |  | √ | ' ' | 产品检验 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_odentryid |  | forderentryid |
| 2 | pk_t_pom_mgsrcentry |  | fentryid |
| 3 | idx_pom_mgose_fid |  | fid |
| 4 | idx_pom_odse_orderid |  | forderid |
| 5 | idx_pom_odse_productid |  | fproductid |

---

## 目标生产工单-子表 t_pom_mgtarentry

- **表名称：** 目标生产工单-子表
- **表名：** t_pom_mgtarentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanendtimemerge | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 3 | fbaseqtymerge | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 4 | ftracknomgid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 5 | fexpdbomtmerge | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fplanpretimemerge | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 8 | fipidmerge | pidmerge | int8 | 64 |  | √ | 0 | pidmerge |
| 9 | fqtymerge | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fpcesroutemergeid | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 11 | finhlimitmerge | 入库上限允差（%） | numeric | 23 | 10 | √ | 0 | 入库上限允差（%） |
| 12 | fmaterialspdmerge | 重新展算订单物料 | bpchar | 1 |  | √ | ' ' | 重新展算订单物料 |
| 13 | frouterepmergeid | 工艺路线替代号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_routereplace](../mpdm_files/mpdm_routereplace.md) |
| 14 | finwardeptmergeid | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbizstatusmg | 业务状态 | varchar | 1 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 |
| 16 | fworkcentermgid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 17 | flocationmgid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 18 | fplanbgtimemerge | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 19 | fbatchnomg | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 21 | fbommergeid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 22 | fisconrptqtymerge | 控制汇报数量 | bpchar | 1 |  | √ | '0' | 控制汇报数量 |
| 23 | fmergeordeno | 目标生产工单 | varchar | 50 |  | √ | ' ' | 目标生产工单 |
| 24 | ftaskstamerge | 任务状态 | varchar | 1 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 25 | fyieldratemg | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 26 | fiscontrolqtymg | 控制入库数量 | bpchar | 1 |  | √ | ' ' | 控制入库数量 |
| 27 | funitmergeid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fproddeptmergeid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fisinspectmerge | 产品检验 | bpchar | 1 |  | √ | ' ' | 产品检验 |
| 30 | fbaseunitmergeid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fconfigcodemgid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 32 | fqualityorgmgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | flotmergeid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 34 | faqtymerge | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 35 | fmappingmgid | 关联分录id | varchar | 50 |  | √ | ' ' | 关联分录id |
| 36 | fwarehousemergeid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 37 | fmversionmergeid | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 38 | fplanstamerge | 计划状态 | varchar | 1 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 39 | finllimitmerge | 入库下限允差（%） | numeric | 23 | 10 | √ | 0 | 入库下限允差（%） |
| 40 | fproductmergeid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | faunitmergeid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fauxpromerge | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 44 | fproducttypemerge | 产品类型 | varchar | 5 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mgtary_fid |  | fid |
| 2 | pk_t_pom_mgtarentry |  | fentryid |
| 3 | idx_pom_odst_product |  | fproductmergeid |

---

## 工单合并处理-关联追踪表 t_pom_ordermerge_tc

- **表名称：** 工单合并处理-关联追踪表
- **表名：** t_pom_ordermerge_tc

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
| 1 | pk_pom_ordermerge_tc |  | fid |
| 2 | idx_pom_ordermerge_tc_tid |  | ftid |
| 3 | idx_pom_ordermerge_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_pom_ordermerge_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_ordermerge_lk

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
| 1 | pk_pom_ordermerge_lk |  | fpkid |
| 2 | idx_pom_ordermerge_lk_fk |  | fid |

---

## 关联子实体-子表 t_pom_ordermgtargetentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_ordermgtargetentry_lk

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
| 1 | idx_pom_ordermgtargetentry_lk_fk |  | fentryid |
| 2 | pk_pom_ordermgtargetentry_lk |  | fpkid |

---

## 工单合并处理-主表 t_pom_ordermerge

- **表名称：** 工单合并处理-主表
- **表名：** t_pom_ordermerge

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 合并原因 | varchar | 255 |  | √ | ' ' | 合并原因 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fmergeorderid | 生成的合并工单id | int8 | 64 |  | √ | 0 | 生成的合并工单id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 14 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mgo_orderid |  | fmergeorderid |
| 2 | pk_t_pom_ordermerge |  | fid |
| 3 | idx_pom_mgo_fno |  | fbillno |
