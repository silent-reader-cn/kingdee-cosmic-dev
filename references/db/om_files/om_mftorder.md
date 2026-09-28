# 委外工单-om_mftorder

## 委外工单-反写记录表 t_om_mftorder_wb

- **表名称：** 委外工单-反写记录表
- **表名：** t_om_mftorder_wb

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
| 1 | idx_om_mftorder_wb_fk |  | fid |
| 2 | pk_om_mftorder_wb |  | fentryid |

---

## 产品明细-子表 t_om_mftorderentry

- **表名称：** 产品明细-子表
- **表名：** t_om_mftorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | 拆分前数量 | numeric | 23 | 10 | √ | 0 | 拆分前数量 |
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 5 | fclosetype | 关闭类型 | varchar | 10 |  | √ | ' ' | 关闭类型,枚举: A :自动关闭 B :手工关闭 C :拆分关闭 |
| 6 | fiscontrolqty | 控制入库数量 | bpchar | 1 |  | √ | '0' | 控制入库数量 |
| 7 | flocation | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 10 | fmtlcostqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 11 | fbaseunitexpoutqty | 基本单位预计产出数量 | numeric | 23 | 10 | √ | 0 | 基本单位预计产出数量 |
| 12 | fstockqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库基本数量 |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | froutereplace | 工艺路线替代号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_routereplace](../mpdm_files/mpdm_routereplace.md) |
| 16 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 17 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 19 | fxkdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 20 | finvkittingqty | 库存齐套数量 | numeric | 23 | 10 | √ | 0 | 库存齐套数量 |
| 21 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 22 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 23 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 24 | fmanftechstatus | 工序计划状态 | varchar | 50 |  | √ | ' ' | 工序计划状态,枚举: T :存在工序计划 F :不存在工序计划 |
| 25 | finwarmin | 入库下限基本数量 | numeric | 23 | 10 | √ | 0 | 入库下限基本数量 |
| 26 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | fkittingsupplydate | 预计齐套日期 | timestamp | 0 |  |  | null | 预计齐套日期 |
| 28 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fisreserved | 是否已预留 | bpchar | 1 |  | √ | '0' | 是否已预留 |
| 31 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 32 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 34 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 35 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 36 | fkittingbaseqty | 齐套基本数量 | numeric | 23 | 10 | √ | 0 | 齐套基本数量 |
| 37 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 38 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 39 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 40 | fbeginbookdate | 投产记账日期 | timestamp | 0 |  |  | null | 投产记账日期 |
| 41 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 42 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 43 | fmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 44 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 48 | fkittingid | 齐套分析ID | int8 | 64 |  | √ | 0 | 齐套分析ID |
| 49 | frptqty | 关联收货数量 | numeric | 23 | 10 | √ | 0 | 关联收货数量 |
| 50 | fexpoutqty | 预计产出数量 | numeric | 23 | 10 | √ | 0 | 预计产出数量 |
| 51 | fexpkittingqty | 预计齐套数量 | numeric | 23 | 10 | √ | 0 | 预计齐套数量 |
| 52 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 53 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 54 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 55 | frcvinhighlimit | 入库上限允差(%) | numeric | 23 | 10 | √ | 0 | 入库上限允差(%) |
| 56 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 57 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 58 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 59 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 60 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 61 | fsrcsplitbillnumber | 来源拆分工单编码 | varchar | 50 |  | √ | ' ' | 来源拆分工单编码 |
| 62 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 64 | fkittingsign | 齐套状况 | varchar | 5 |  | √ | ' ' | 齐套状况,枚举: A :库存齐套 B :预计齐套 C :不齐套 D :暂收齐套 E :在途齐套 F :采购申请齐套 G :计划订单齐套 |
| 65 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 66 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 67 | fexpkittingbaseqty | 预计齐套基本数量 | numeric | 23 | 10 | √ | 0 | 预计齐套基本数量 |
| 68 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |
| 69 | festscrapqty | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 70 | fkittingtime | 齐套分析时间 | timestamp | 0 |  |  | null | 齐套分析时间 |
| 71 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 72 | frcvinlowlimit | 入库下限允差(%) | numeric | 23 | 10 | √ | 0 | 入库下限允差(%) |
| 73 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 74 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 75 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 76 | finwarmax | 入库上限基本数量 | numeric | 23 | 10 | √ | 0 | 入库上限基本数量 |
| 77 | freportqty | 收货数量 | numeric | 23 | 10 | √ | 0 | 收货数量 |
| 78 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 79 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 80 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 81 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 82 | finvkittingbaseqty | 库存齐套基本数量 | numeric | 23 | 10 | √ | 0 | 库存齐套基本数量 |
| 83 | fplanbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 84 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 85 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 86 | foutputoperation | 产出工序 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 87 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 88 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mftorderentry_fk |  | fid |
| 2 | pk_t_om_mftorderentry |  | fentryid |

---

## 关联子实体-子表 t_om_mftorderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_mftorderentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseunitexpoutqty_old | 基本单位预计产出数量_原始携带值 | numeric | 23 | 10 |  | null | 基本单位预计产出数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseunitexpoutqty | 基本单位预计产出数量_确认携带值 | numeric | 23 | 10 |  | null | 基本单位预计产出数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftorderentry_lk |  | fpkid |
| 2 | idx_om_mftorderentry_lk_fk |  | fentryid |

---

## 委外工单-主表 t_om_mftorder

- **表名称：** 委外工单-主表
- **表名：** t_om_mftorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 8 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 9 :迁移生成 |
| 12 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 13 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 17 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fiscrossreturn | 跨期退货 | bpchar | 1 |  | √ | '0' | 跨期退货 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mftorder_fno |  | fbillno |
| 2 | idx_om_mftorder_orgfid |  | forgid,fid |
| 3 | idx_om_mftorder_createtime |  | fcreatetime |
| 4 | pk_t_om_mftorder |  | fid |

---

## 委外工单-关联追踪表 t_om_mftorder_tc

- **表名称：** 委外工单-关联追踪表
- **表名：** t_om_mftorder_tc

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
| 1 | idx_om_mftorder_tc_tbill |  | ftbillid |
| 2 | idx_om_mftorder_tc_tid |  | ftid |
| 3 | pk_om_mftorder_tc |  | fid |

---

## 产品明细-分表 t_om_mftorderentry_e

- **表名称：** 产品明细-分表
- **表名：** t_om_mftorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 3 | fxkunquainwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 4 | fbuspurpushqty | 关联采购数量 | numeric | 23 | 10 | √ | 0 | 关联采购数量 |
| 5 | fsuperiorstockentryid | 上级用料清单分录ID | int8 | 64 |  | √ | 0 | 上级用料清单分录ID |
| 6 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库基本数量 |
| 7 | frepminbsqty | 收货下限基本数量 | numeric | 23 | 10 | √ | 0 | 收货下限基本数量 |
| 8 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 9 | forderid | 采购订单ID | int8 | 64 |  | √ | 0 | 采购订单ID |
| 10 | fxkstockqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 11 | frootdemandentryseq | 根需求单据行号 | int4 | 32 |  | √ | 0 | 根需求单据行号 |
| 12 | fwaitckbaseqty | 待检品入库基本数量 | int8 | 64 |  | √ | 0 | 待检品入库基本数量 |
| 13 | fcrossqty | 跨期退货数量 | numeric | 23 | 10 | √ | 0 | 跨期退货数量 |
| 14 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 15 | fxkquainwaqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 16 | fendcasetime | 齐套时间 | timestamp | 0 |  |  | null | 齐套时间 |
| 17 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品入库基本数量 |
| 18 | frepminqty | 收货下限数量 | numeric | 23 | 10 | √ | 0 | 收货下限数量 |
| 19 | fapplyid | 采购申请单ID | int8 | 64 |  | √ | 0 | 采购申请单ID |
| 20 | frepminrate | 收货下限允差(%) | numeric | 23 | 10 | √ | 0 | 收货下限允差(%) |
| 21 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 22 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 23 | forderentryseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 24 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 25 | fnotreportqty | 待收货数量 | numeric | 23 | 10 | √ | 0 | 待收货数量 |
| 26 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0 | 已领套数 |
| 27 | fapplyentryseq | 采购申请单行号 | varchar | 50 |  | √ | ' ' | 采购申请单行号 |
| 28 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 29 | fplansuretime | 计划确认时间 | timestamp | 0 |  |  | null | 计划确认时间 |
| 30 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 31 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 32 | fwaitcheckqty | 待检品入库数量 | numeric | 23 | 10 | √ | 0 | 待检品入库数量 |
| 33 | fxkinwarmin | 入库下限数量 | numeric | 23 | 10 | √ | 0 | 入库下限数量 |
| 34 | frptbsqty | 关联收货基本数量 | numeric | 23 | 10 | √ | 0 | 关联收货基本数量 |
| 35 | fheadbillno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 36 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 37 | fpurpushqty | 关联采购基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购基本数量 |
| 38 | fscrapbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 39 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 40 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 41 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 42 | frepairqty | 判退数量 | numeric | 23 | 10 | √ | 0 | 判退数量 |
| 43 | fcrosspushbaseqty | 跨期退货关联基本数量 | numeric | 23 | 10 | √ | 0 | 跨期退货关联基本数量 |
| 44 | fxkinwarmax | 入库上限数量 | numeric | 23 | 10 | √ | 0 | 入库上限数量 |
| 45 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 46 | ftotalsplitqty | 已拆分数量 | numeric | 23 | 10 | √ | 0 | 已拆分数量 |
| 47 | fnotreportbsqty | 待收货基本数量 | numeric | 23 | 10 | √ | 0 | 待收货基本数量 |
| 48 | ftotalsplitbaseqty | 已拆分基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分基本数量 |
| 49 | fisinspection | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 50 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 51 | fcrossbaseqty | 跨期退货基本数量 | numeric | 23 | 10 | √ | 0 | 跨期退货基本数量 |
| 52 | forderbillno | 采购订单号 | varchar | 50 |  | √ | ' ' | 采购订单号 |
| 53 | fsampledestorybsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 54 | frootdemandentity | 根需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 55 | foutwaqty | 退库基本数量 | numeric | 23 | 10 | √ | 0 | 退库基本数量 |
| 56 | fisconreportqty | 控制收货数量 | bpchar | 1 |  | √ | '0' | 控制收货数量 |
| 57 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 58 | forderentryid | 采购订单行ID | int8 | 64 |  | √ | 0 | 采购订单行ID |
| 59 | fxkdemanddate | 订单需求日期 | timestamp | 0 |  |  | null | 订单需求日期 |
| 60 | freportbsqty | 收货基本数量 | numeric | 23 | 10 | √ | 0 | 收货基本数量 |
| 61 | frepmaxqty | 收货上限数量 | numeric | 23 | 10 | √ | 0 | 收货上限数量 |
| 62 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 63 | fapplybillno | 采购申请单号 | varchar | 50 |  | √ | ' ' | 采购申请单号 |
| 64 | fxkoutwaqty | 退库数量 | numeric | 23 | 10 | √ | 0 | 退库数量 |
| 65 | ftransmittime | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 66 | frepmaxrate | 收货上限允差(%) | numeric | 23 | 10 | √ | 0 | 收货上限允差(%) |
| 67 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 68 | fqualifiedbsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 69 | frootdemandbillno | 根需求单号 | varchar | 120 |  | √ | ' ' | 根需求单号 |
| 70 | frepmaxbsqty | 收货上限基本数量 | numeric | 23 | 10 | √ | 0 | 收货上限基本数量 |
| 71 | fcrosspushqty | 跨期退货关联数量 | numeric | 23 | 10 | √ | 0 | 跨期退货关联数量 |
| 72 | frepinwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 73 | fapplyentryid | 申请单行ID | int8 | 64 |  | √ | 0 | 申请单行ID |
| 74 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 75 | fpurauditqty | 采购执行基本数量 | numeric | 23 | 10 | √ | 0 | 采购执行基本数量 |
| 76 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 77 | fsettletime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 78 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 79 | finnersupplier | 内部供应商 | bpchar | 1 |  | √ | '0' | 内部供应商 |
| 80 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 81 | facceptbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 82 | fendworktime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 83 | fmtlcostbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mfe_mid |  | fmaterielmasterid |
| 2 | pk_t_om_mftorderentry_e |  | fentryid |
| 3 | idx_om_mftorderentry_e_fk |  | fid |
| 4 | idx_om_mfe_headno |  | fheadbillno |

---

## 产品明细-分表 t_om_mftorderentry_f

- **表名称：** 产品明细-分表
- **表名：** t_om_mftorderentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowsrctype | 行来源类型 | varchar | 5 |  | √ | ' ' | 行来源类型,枚举: A :生成下级工单_生成新工单 B :生成下级工单_生成新分录 |
| 3 | frepairbaseqty | 判退基本数量 | numeric | 23 | 10 | √ | 0 | 判退基本数量 |
| 4 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 5 | fstockedbaseqty | 待入库基本数量 | numeric | 23 | 10 | √ | 0 | 待入库基本数量 |
| 6 | fworkwasteinvbsqty | 工废入库基本数量 | numeric | 23 | 10 | √ | 0 | 工废入库基本数量 |
| 7 | fscrapinvqty | 料废入库数量 | numeric | 23 | 10 | √ | 0 | 料废入库数量 |
| 8 | fisgeneratedsuborder | 已生成下级工单 | bpchar | 1 |  | √ | '0' | 已生成下级工单 |
| 9 | fpurreturnqty | 采购退料数量 | numeric | 23 | 10 | √ | 0 | 采购退料数量 |
| 10 | fclosereason | 手工关闭原因 | varchar | 500 |  | √ | ' ' | 手工关闭原因 |
| 11 | fscrapinvbsqty | 料废入库基本数量 | numeric | 23 | 10 | √ | 0 | 料废入库基本数量 |
| 12 | fstockedqty | 待入库数量 | numeric | 23 | 10 | √ | 0 | 待入库数量 |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 14 | fworkwasteinvqty | 工废入库数量 | numeric | 23 | 10 | √ | 0 | 工废入库数量 |
| 15 | fcrossreturntype | 跨期退货类型 | varchar | 5 |  | √ | ' ' | 跨期退货类型,枚举: A :退补货 B :仅退货 C :仅退原料 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fpurreturnbaseqty | 采购退料基本数量 | numeric | 23 | 10 | √ | 0 | 采购退料基本数量 |
| 18 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mftorderentry_f_fid |  | fid |
| 2 | pk_om_mftorderentry_f |  | fentryid |
