# 委外工单变更单-om_xmftorder

## 产品明细-子表 t_om_xmftorderentry

- **表名称：** 产品明细-子表
- **表名：** t_om_xmftorderentry

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
| 9 | fyieldrate | 成品率% | numeric | 23 | 4 | √ | 0 | 成品率% |
| 10 | fmtlcostqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 11 | fbaseunitexpoutqty | 基本单位预计产出数量 | numeric | 23 | 10 | √ | 0 | 基本单位预计产出数量 |
| 12 | fstockqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库基本数量 |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fsrcbillentryseq | 委外工单行号 | varchar | 50 |  | √ | ' ' | 委外工单行号 |
| 15 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | froutereplace | 工艺路线替代号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_routereplace](../mpdm_files/mpdm_routereplace.md) |
| 17 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 18 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 29 | fpurorgid | 采购组织1 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fisreserved | 是否已预留 | bpchar | 1 |  | √ | '0' | 是否已预留 |
| 31 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 32 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 33 | fsrcbillid | 委外工单内码 | varchar | 50 |  | √ | ' ' | 委外工单内码 |
| 34 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 35 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 36 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 37 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 38 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 39 | fbeginbookdate | 投产记账日期 | timestamp | 0 |  |  | null | 投产记账日期 |
| 40 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 41 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 42 | fsrcbillno1 | fsrcbillno1 | varchar | 50 |  | √ | ' ' |  |
| 43 | fmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 44 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 48 | fkittingid | 齐套分析ID | int8 | 64 |  | √ | 0 | 齐套分析ID |
| 49 | frptqty | 关联收货数量 | numeric | 23 | 10 | √ | 0 | 关联收货数量 |
| 50 | fsrcbillno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 51 | fexpoutqty | 预计产出数量 | numeric | 23 | 10 | √ | 0 | 预计产出数量 |
| 52 | fexpkittingqty | 预计齐套数量 | numeric | 23 | 10 | √ | 0 | 预计齐套数量 |
| 53 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 54 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 55 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 56 | frcvinhighlimit | 入库上限允差(%) | numeric | 23 | 10 | √ | 0 | 入库上限允差(%) |
| 57 | fchangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 58 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 59 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 60 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 61 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 62 | freplaceno | 替代号1 | varchar | 50 |  | √ | ' ' | 替代号1 |
| 63 | fsrcsplitbillnumber | 来源拆分工单编码 | varchar | 50 |  | √ | ' ' | 来源拆分工单编码 |
| 64 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 65 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 66 | fkittingsign | 齐套状况 | varchar | 5 |  | √ | ' ' | 齐套状况,枚举: A :库存齐套 B :预计齐套 C :不齐套 D :暂收齐套 E :在途齐套 F :采购申请齐套 G :计划订单齐套 |
| 67 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 68 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 69 | fexpkittingbaseqty | 预计齐套基本数量 | numeric | 23 | 10 | √ | 0 | 预计齐套基本数量 |
| 70 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |
| 71 | festscrapqty | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 72 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 73 | frcvinlowlimit | 入库下限允差(%) | numeric | 23 | 10 | √ | 0 | 入库下限允差(%) |
| 74 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 75 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 76 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 77 | finwarmax | 入库上限基本数量 | numeric | 23 | 10 | √ | 0 | 入库上限基本数量 |
| 78 | fsrcbillentryid | 委外工单行内码 | varchar | 50 |  | √ | ' ' | 委外工单行内码 |
| 79 | freportqty | 收货数量 | numeric | 23 | 10 | √ | 0 | 收货数量 |
| 80 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 81 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 82 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 83 | finvkittingbaseqty | 库存齐套基本数量 | numeric | 23 | 10 | √ | 0 | 库存齐套基本数量 |
| 84 | fplanbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 85 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 86 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 87 | foutputoperation | 产出工序 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 88 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 89 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_xmftorderentry_srceid |  | fsrcbillentryid |
| 2 | pk_om_xmftorderentry |  | fentryid |
| 3 | idx_om_xmftorderentry_fk |  | fid |

---

## 产品明细-分表 t_om_xmftorderentry_f

- **表名称：** 产品明细-分表
- **表名：** t_om_xmftorderentry_f

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
| 1 | pk_om_xmftorderentry_f |  | fentryid |
| 2 | idx_om_xmftorderentry_f_fid |  | fid |

---

## 产品明细-分表 t_om_xmftorderentry_e

- **表名称：** 产品明细-分表
- **表名：** t_om_xmftorderentry_e

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
| 20 | frepminrate | 收货下限允差(%) | numeric | 10 | 2 | √ | 0 | 收货下限允差(%) |
| 21 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 22 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 23 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 24 | forderentryseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 25 | fnotreportqty | 待收货数量 | numeric | 23 | 10 | √ | 0 | 待收货数量 |
| 26 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0 | 已领套数 |
| 27 | fapplyentryseq | 采购申请单行号 | varchar | 50 |  | √ | ' ' | 采购申请单行号 |
| 28 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 29 | fplansuretime | 计划确认时间 | timestamp | 0 |  |  | null | 计划确认时间 |
| 30 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 31 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 32 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | fwaitcheckqty | 待检品入库数量 | numeric | 23 | 10 | √ | 0 | 待检品入库数量 |
| 34 | fxkinwarmin | 入库下限数量 | numeric | 23 | 10 | √ | 0 | 入库下限数量 |
| 35 | frptbsqty | 关联收货基本数量 | numeric | 23 | 10 | √ | 0 | 关联收货基本数量 |
| 36 | fheadbillno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 37 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 38 | fpurpushqty | 关联采购基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购基本数量 |
| 39 | fscrapbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 40 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 41 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 42 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 43 | frepairqty | 判退数量 | numeric | 23 | 10 | √ | 0 | 判退数量 |
| 44 | fcrosspushbaseqty | 跨期退货关联基本数量 | numeric | 23 | 10 | √ | 0 | 跨期退货关联基本数量 |
| 45 | fxkinwarmax | 入库上限数量 | numeric | 23 | 10 | √ | 0 | 入库上限数量 |
| 46 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 47 | ftotalsplitqty | 已拆分数量 | numeric | 23 | 10 | √ | 0 | 已拆分数量 |
| 48 | fnotreportbsqty | 待收货基本数量 | numeric | 23 | 10 | √ | 0 | 待收货基本数量 |
| 49 | ftotalsplitbaseqty | 已拆分基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分基本数量 |
| 50 | fisinspection | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 51 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 52 | fcrossbaseqty | 跨期退货基本数量 | numeric | 23 | 10 | √ | 0 | 跨期退货基本数量 |
| 53 | forderbillno | 采购订单号 | varchar | 50 |  | √ | ' ' | 采购订单号 |
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
| 66 | frepmaxrate | 收货上限允差(%) | numeric | 10 | 2 | √ | 0 | 收货上限允差(%) |
| 67 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 68 | fqualifiedbsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 69 | frootdemandbillno | 根需求单号 | varchar | 120 |  | √ | ' ' | 根需求单号 |
| 70 | frepmaxbsqty | 收货上限基本数量 | numeric | 23 | 10 | √ | 0 | 收货上限基本数量 |
| 71 | fcrosspushqty | 跨期退货关联数量 | numeric | 23 | 10 | √ | 0 | 跨期退货关联数量 |
| 72 | frepinwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 73 | fapplyentryid | 申请单行ID | int8 | 64 |  | √ | 0 | 申请单行ID |
| 74 | fpurauditqty | 采购执行基本数量 | numeric | 23 | 10 | √ | 0 | 采购执行基本数量 |
| 75 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 76 | fsettletime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 77 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 78 | finnersupplier | 内部供应商 | bpchar | 1 |  | √ | '0' | 内部供应商 |
| 79 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 80 | facceptbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 81 | fendworktime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 82 | fmtlcostbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_xmftorderentry_e_fk |  | fid |
| 2 | pk_om_xmftorderentry_e |  | fentryid |
| 3 | idx_om_xmftordere_materialid |  | fmaterielmasterid |

---

## 委外工单变更单-反写记录表 t_om_mftorder_wb

- **表名称：** 委外工单变更单-反写记录表
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

## 委外工单变更单-主表 t_om_xmftorder

- **表名称：** 委外工单变更单-主表
- **表名：** t_om_xmftorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplierhead | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 5 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 6 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsupplier1 | fsupplier1 | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | forg1 | forg1 | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 19 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 20 | freasonid | 变更原因 | int8 | 64 |  | √ | 0 | [变更原因 pdm_ecnreason](../pdm_files/pdm_ecnreason.md) |
| 21 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 9 :迁移生成 |
| 22 | fpurorghead | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fiscrossreturn | 跨期退货 | bpchar | 1 |  | √ | '0' | 跨期退货 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xmftorder |  | fid |
| 2 | idx_om_xmftorder_orgfid |  | forgid |
| 3 | idx_om_xmftorder_createtime |  | fcreatetime |
| 4 | idx_om_xmftorder |  | fbillno |

---

## 委外工单变更单-关联追踪表 t_om_mftorder_tc

- **表名称：** 委外工单变更单-关联追踪表
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
