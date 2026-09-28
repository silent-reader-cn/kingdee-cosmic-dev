# 生产工单分录f7-pom_mftorder_f7

## 生产工单分录f7-分表 t_pom_mftorderentry_e

- **表名称：** 生产工单分录f7-分表
- **表名：** t_pom_mftorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | facceptqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fxkunquainwaqty | 不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库数量 |
| 4 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 不合格品入库基本数量 |
| 5 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | frepminbsqty | frepminbsqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 8 | flocation | flocation | int8 | 64 |  | √ | 0 |  |
| 9 | fmtlcostqty | fmtlcostqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fxkstockqty | 下推入库数量 | numeric | 23 | 10 | √ | 0 | 下推入库数量 |
| 11 | fstockqty | 下推入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推入库基本数量 |
| 12 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 13 | fxkquainwaqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 14 | finwarconsigner | finwarconsigner | int8 | 64 |  | √ | 0 |  |
| 15 | fendcasetime | fendcasetime | timestamp | 0 |  |  | null |  |
| 16 | fbrokenbsqty | fbrokenbsqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废品入库基本数量 |
| 18 | frepminqty | frepminqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | frepminrate | frepminrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | freworkbsqty | freworkbsqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 22 | fnotreportqty | fnotreportqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | finwarmin | finwarmin | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fpickingpairs | fpickingpairs | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | funqualifiedqty | funqualifiedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 26 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | fplansuretime | fplansuretime | timestamp | 0 |  |  | null |  |
| 28 | fstartworktime | fstartworktime | timestamp | 0 |  |  | null |  |
| 29 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 30 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fwaitcheckqty | fwaitcheckqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fxkinwarmin | fxkinwarmin | numeric | 23 | 10 | √ | 0 |  |
| 33 | frptbsqty | 下推汇报基本数量 | numeric | 23 | 10 | √ | 0 | 下推汇报基本数量 |
| 34 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 35 | fworkwastebsqty | fworkwastebsqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | ffirstinspectioncontrol | ffirstinspectioncontrol | bpchar | 1 |  | √ | 'A' |  |
| 37 | fscrapbsqty | fscrapbsqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fworkwasteqty | fworkwasteqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fisgenprocessplan | fisgenprocessplan | bpchar | 1 |  | √ | '0' |  |
| 40 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 41 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 42 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 合格品入库基本数量 |
| 43 | frepairqty | frepairqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fxkinwarmax | fxkinwarmax | numeric | 23 | 10 | √ | 0 |  |
| 45 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | ftotalsplitqty | ftotalsplitqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | ffirstinspectionstatus | ffirstinspectionstatus | bpchar | 1 |  | √ | 'N' |  |
| 48 | ftotalsplitbaseqty | ftotalsplitbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fnotreportbsqty | fnotreportbsqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fisinspection | fisinspection | bpchar | 1 |  | √ | '0' |  |
| 51 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 52 | frptqty | 下推汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推汇报数量 |
| 53 | foutwaqty | foutwaqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | frcvinhighlimit | frcvinhighlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 55 | ffirstinspection | ffirstinspection | bpchar | 1 |  | √ | '0' |  |
| 56 | fisconreportqty | fisconreportqty | bpchar | 1 |  | √ | '0' |  |
| 57 | fxkdemanddate | fxkdemanddate | timestamp | 0 |  |  | null |  |
| 58 | freworkorderqty | freworkorderqty | numeric | 23 | 10 | √ | 0 |  |
| 59 | finwardept | finwardept | int8 | 64 |  | √ | 0 |  |
| 60 | freportbsqty | 汇报基本数量 | numeric | 23 | 10 | √ | 0 | 汇报基本数量 |
| 61 | frepmaxqty | frepmaxqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 62 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 63 | fxkoutwaqty | fxkoutwaqty | numeric | 23 | 10 | √ | 0 |  |
| 64 | fqualifiedqty | fqualifiedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 65 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 66 | frepmaxrate | frepmaxrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 67 | fqualifiedbsqty | fqualifiedbsqty | numeric | 23 | 10 | √ | 0 |  |
| 68 | frepmaxbsqty | frepmaxbsqty | numeric | 23 | 10 | √ | 0 |  |
| 69 | frepairbsqty | frepairbsqty | numeric | 23 | 10 | √ | 0 |  |
| 70 | frepinwaqty | frepinwaqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 71 | frcvinlowlimit | frcvinlowlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 72 | finwarmax | finwarmax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 73 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0.0000000000 | 汇报数量 |
| 74 | fsourcebillnumber | fsourcebillnumber | varchar | 50 |  | √ | ' ' |  |
| 75 | fislastproceplanend | fislastproceplanend | bpchar | 1 |  | √ | '1' |  |
| 76 | fbrokenqty | fbrokenqty | numeric | 23 | 10 | √ | 0 |  |
| 77 | fmanuseq | fmanuseq | int8 | 64 |  | √ | 0 |  |
| 78 | fsettletime | fsettletime | timestamp | 0 |  |  | null |  |
| 79 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 80 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 81 | facceptbsqty | facceptbsqty | numeric | 23 | 10 | √ | 0 |  |
| 82 | foutputoperation | foutputoperation | int8 | 64 |  | √ | 0 |  |
| 83 | fendworktime | fendworktime | timestamp | 0 |  |  | null |  |
| 84 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 85 | fmtlcostbsqty | fmtlcostbsqty | numeric | 23 | 10 | √ | 0 |  |

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
| 2 | fplanqty | fplanqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fclosetype | fclosetype | varchar | 10 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fbaseunitexpoutqty | fbaseunitexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | froutereplace | froutereplace | int8 | 64 |  | √ | 0 |  |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 12 | fismrpcal | fismrpcal | bpchar | 1 |  | √ | '0' |  |
| 13 | fxkdemandbillid | fxkdemandbillid | varchar | 50 |  | √ | ' ' |  |
| 14 | fparententryid | 上级主键 | int8 | 64 |  | √ | 0 | 上级主键 |
| 15 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 16 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 17 | fmanftechstatus | fmanftechstatus | varchar | 30 |  | √ | ' ' |  |
| 18 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fsrcorderentryid | fsrcorderentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fxkdemandbill | fxkdemandbill | varchar | 50 |  | √ | ' ' |  |
| 24 | fkittingbaseqty | fkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 26 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 27 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 29 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 30 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 34 | fexpoutqty | fexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :结案 |
| 36 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fmaterialversion | fmaterialversion | int8 | 64 |  | √ | 0 |  |
| 38 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 39 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 40 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 41 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 42 | fxkdemandbillentryid | fxkdemandbillentryid | varchar | 50 |  | √ | ' ' |  |
| 43 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 44 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 45 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | 生产工单分录f7 pom_mftorder_f7 |
| 48 | festscrapqty | festscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | fkittingtime | fkittingtime | timestamp | 0 |  |  | null |  |
| 50 | fqualityorg | fqualityorg | int8 | 64 |  | √ | 0 |  |
| 51 | fecnversion | fecnversion | int8 | 64 |  | √ | 0 |  |
| 52 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 53 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 54 | fplanstatus | 计划状态 | varchar | 30 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 55 | fpurqty | fpurqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | fxkdemandseq | fxkdemandseq | int8 | 64 |  | √ | 0 |  |
| 57 | fkittingqty | fkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 58 | foprentryid | foprentryid | int8 | 64 |  | √ | 0 |  |
| 59 | fxkdemandbillentity | fxkdemandbillentity | varchar | 50 |  | √ | ' ' |  |
| 60 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 61 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 63 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 64 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |

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
