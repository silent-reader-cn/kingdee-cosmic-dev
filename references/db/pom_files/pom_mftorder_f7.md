# 生产工单分录f7-pom_mftorder_f7

## 生产工单分录f7-分表 t_pom_mftorderentry_f

- **表名称：** 生产工单分录f7-分表
- **表名：** t_pom_mftorderentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowsrctype | frowsrctype | varchar | 5 |  | √ | ' ' |  |
| 3 | fisgeneratedsuborder | fisgeneratedsuborder | bpchar | 1 |  | √ | '0' |  |
| 4 | fclosereason | fclosereason | varchar | 500 |  | √ | ' ' |  |
| 5 | foutputoperationnum | foutputoperationnum | int4 | 32 |  | √ | 0 |  |
| 6 | fstockedqty | fstockedqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 8 | foutputoperationseq | foutputoperationseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 11 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 12 | fstockedbaseqty | fstockedbaseqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorderentry_f_fid |  | fid |
| 2 | pk_pom_mftorderentry_f |  | fentryid |

---

## 生产工单分录f7-分表 t_pom_mftorderentry_e

- **表名称：** 生产工单分录f7-分表
- **表名：** t_pom_mftorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | facceptqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fxkunquainwaqty | 不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库数量 |
| 4 | fsuperiorstockentryid | fsuperiorstockentryid | int8 | 64 |  | √ | 0 |  |
| 5 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 6 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 7 | frepminbsqty | frepminbsqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 9 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 10 | flocation | flocation | int8 | 64 |  | √ | 0 |  |
| 11 | fmtlcostqty | fmtlcostqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fxkstockqty | 下推入库数量 | numeric | 23 | 10 | √ | 0 | 下推入库数量 |
| 13 | fstockqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推入库基本数量 |
| 14 | frootdemandentryseq | 根需求单据行号 | int4 | 32 |  | √ | 0 | 根需求单据行号 |
| 15 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 16 | fxkquainwaqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 17 | finwarconsigner | finwarconsigner | int8 | 64 |  | √ | 0 |  |
| 18 | fendcasetime | fendcasetime | timestamp | 0 |  |  | null |  |
| 19 | fbrokenbsqty | fbrokenbsqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 21 | frepminqty | frepminqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | frepminrate | frepminrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | freworkbsqty | freworkbsqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 25 | fnotreportqty | fnotreportqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | finwarmin | finwarmin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0.0000000000 | 已领套数 |
| 28 | funqualifiedqty | funqualifiedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fplansuretime | fplansuretime | timestamp | 0 |  |  | null |  |
| 31 | fstartworktime | fstartworktime | timestamp | 0 |  |  | null |  |
| 32 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 33 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 34 | fwaitcheckqty | fwaitcheckqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fxkinwarmin | fxkinwarmin | numeric | 23 | 10 | √ | 0 |  |
| 36 | frptbsqty | 下推汇报基本数量 | numeric | 23 | 10 | √ | 0 | 下推汇报基本数量 |
| 37 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 38 | fworkwastebsqty | fworkwastebsqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | ffirstinspectioncontrol | ffirstinspectioncontrol | bpchar | 1 |  | √ | 'A' |  |
| 40 | fscrapbsqty | fscrapbsqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fworkwasteqty | fworkwasteqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fisgenprocessplan | fisgenprocessplan | bpchar | 1 |  | √ | '0' |  |
| 43 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 44 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 45 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 46 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 47 | frepairqty | frepairqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | fxkinwarmax | fxkinwarmax | numeric | 23 | 10 | √ | 0 |  |
| 49 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | ftotalsplitqty | ftotalsplitqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | ffirstinspectionstatus | ffirstinspectionstatus | bpchar | 1 |  | √ | 'N' |  |
| 52 | ftotalsplitbaseqty | ftotalsplitbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | fnotreportbsqty | fnotreportbsqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | fisinspection | fisinspection | bpchar | 1 |  | √ | '0' |  |
| 55 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 56 | frptqty | 下推汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推汇报数量 |
| 57 | frootdemandentity | 根需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 58 | foutwaqty | foutwaqty | numeric | 23 | 10 | √ | 0 |  |
| 59 | frcvinhighlimit | frcvinhighlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 60 | ffirstinspection | ffirstinspection | bpchar | 1 |  | √ | '0' |  |
| 61 | fisconreportqty | fisconreportqty | bpchar | 1 |  | √ | '0' |  |
| 62 | fxkdemanddate | fxkdemanddate | timestamp | 0 |  |  | null |  |
| 63 | freworkorderqty | freworkorderqty | numeric | 23 | 10 | √ | 0 |  |
| 64 | finwardept | finwardept | int8 | 64 |  | √ | 0 |  |
| 65 | freportbsqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0 | 汇报基本数量 |
| 66 | frepmaxqty | frepmaxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 67 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 68 | fxkoutwaqty | fxkoutwaqty | numeric | 23 | 10 | √ | 0 |  |
| 69 | fqualifiedqty | fqualifiedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 70 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 71 | frepmaxrate | frepmaxrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 72 | fqualifiedbsqty | fqualifiedbsqty | numeric | 23 | 10 | √ | 0 |  |
| 73 | frootdemandbillno | 根需求单号 | varchar | 120 |  | √ | ' ' | 根需求单号 |
| 74 | frepmaxbsqty | frepmaxbsqty | numeric | 23 | 10 | √ | 0 |  |
| 75 | frepairbsqty | frepairbsqty | numeric | 23 | 10 | √ | 0 |  |
| 76 | frepinwaqty | frepinwaqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 77 | frcvinlowlimit | frcvinlowlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 78 | finwarmax | finwarmax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 79 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 80 | fsourcebillnumber | fsourcebillnumber | varchar | 50 |  | √ | ' ' |  |
| 81 | fislastproceplanend | fislastproceplanend | bpchar | 1 |  | √ | '1' |  |
| 82 | fbrokenqty | fbrokenqty | numeric | 23 | 10 | √ | 0 |  |
| 83 | fmanuseq | fmanuseq | int8 | 64 |  | √ | 0 |  |
| 84 | fsettletime | fsettletime | timestamp | 0 |  |  | null |  |
| 85 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 86 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 87 | facceptbsqty | facceptbsqty | numeric | 23 | 10 | √ | 0 |  |
| 88 | foutputoperation | foutputoperation | int8 | 64 |  | √ | 0 |  |
| 89 | fendworktime | fendworktime | timestamp | 0 |  |  | null |  |
| 90 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 91 | fmtlcostbsqty | fmtlcostbsqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_mftorderentry_e_pkey |  | fentryid |
| 2 | idx_pom_mftorderentry_e_fk |  | fid |

---

## 生产工单分录f7-主表 t_pom_mftorderentry

- **表名称：** 生产工单分录f7-主表
- **表名：** t_pom_mftorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 2 | fplanqty | 拆分前数量 | numeric | 23 | 10 | √ | 0 | 拆分前数量 |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fclosetype | fclosetype | varchar | 10 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fbaseunitexpoutqty | fbaseunitexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | froutereplace | froutereplace | int8 | 64 |  | √ | 0 |  |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | fismrpcal | fismrpcal | bpchar | 1 |  | √ | '0' |  |
| 13 | fxkdemandbillid | fxkdemandbillid | varchar | 50 |  | √ | ' ' |  |
| 14 | finvkittingqty | finvkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fparententryid | 上级主键 | int8 | 64 |  | √ | 0 | 上级主键 |
| 16 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 17 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 18 | fmanftechstatus | fmanftechstatus | varchar | 30 |  | √ | ' ' |  |
| 19 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 21 | fkittingsupplydate | fkittingsupplydate | timestamp | 0 |  |  | null |  |
| 22 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 23 | fisreserved | fisreserved | bpchar | 1 |  | √ | '0' |  |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fsrcorderentryid | fsrcorderentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fxkdemandbill | fxkdemandbill | varchar | 50 |  | √ | ' ' |  |
| 27 | fkittingbaseqty | fkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 29 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 30 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 31 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 32 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 33 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 37 | fkittingid | fkittingid | int8 | 64 |  | √ | 0 |  |
| 38 | fexpoutqty | fexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | fexpkittingqty | fexpkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 41 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 42 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fmaterialversion | fmaterialversion | int8 | 64 |  | √ | 0 |  |
| 44 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 45 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 46 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 47 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 48 | fxkdemandbillentryid | fxkdemandbillentryid | varchar | 50 |  | √ | ' ' |  |
| 49 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 50 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 51 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 52 | fkittingsign | fkittingsign | varchar | 5 |  | √ | ' ' |  |
| 53 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 54 | fexpkittingbaseqty | fexpkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fprodline | fprodline | int8 | 64 |  | √ | 0 |  |
| 56 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 57 | festscrapqty | festscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 58 | fkittingtime | fkittingtime | timestamp | 0 |  |  | null |  |
| 59 | fqualityorg | fqualityorg | int8 | 64 |  | √ | 0 |  |
| 60 | fecnversion | fecnversion | int8 | 64 |  | √ | 0 |  |
| 61 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 63 | fplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 64 | fpurqty | fpurqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 65 | fxkdemandseq | fxkdemandseq | int8 | 64 |  | √ | 0 |  |
| 66 | fkittingqty | fkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | foprentryid | foprentryid | int8 | 64 |  | √ | 0 |  |
| 68 | fxkdemandbillentity | fxkdemandbillentity | varchar | 50 |  | √ | ' ' |  |
| 69 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 70 | finvkittingbaseqty | finvkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fplanbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 72 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 73 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 74 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_orderen_fconfiguredcode |  | fconfiguredcodeid |
| 2 | idx_pom_mftorderentry_fk |  | fid |
| 3 | idx_pom_moe_fplanstatus |  | fplanstatus |
| 4 | idx_orderen_mid |  | fmaterielmasterid |
| 5 | t_pom_mftorderentry_pkey |  | fentryid |
| 6 | idx_orderen_ftracknumber |  | ftracknumberid |
| 7 | idx_orderen_mftid |  | fmaterial |
