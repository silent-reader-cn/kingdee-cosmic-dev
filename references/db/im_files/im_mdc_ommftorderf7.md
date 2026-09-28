# 委外工单分录F7-im_mdc_ommftorderf7

## 委外工单分录F7-分表 t_om_mftorderentry_e

- **表名称：** 委外工单分录F7-分表
- **表名：** t_om_mftorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | facceptqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fxkunquainwaqty | fxkunquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fbuspurpushqty | fbuspurpushqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | funquainwaqty | funquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | frepminbsqty | frepminbsqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 8 | fxkstockqty | fxkstockqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fwaitckbaseqty | fwaitckbaseqty | int8 | 64 |  | √ | 0 |  |
| 10 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 11 | fxkquainwaqty | fxkquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fendcasetime | fendcasetime | timestamp | 0 |  |  | null |  |
| 13 | fscrinwaqty | fscrinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | frepminqty | frepminqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fapplyid | fapplyid | int8 | 64 |  | √ | 0 |  |
| 16 | frepminrate | frepminrate | numeric | 23 | 10 | √ | 0 |  |
| 17 | freworkbsqty | freworkbsqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | forderentryseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 20 | fplanpreparetime | fplanpreparetime | timestamp | 0 |  |  | null |  |
| 21 | fnotreportqty | fnotreportqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fpickingpairs | fpickingpairs | numeric | 23 | 10 | √ | 0 |  |
| 23 | fapplyentryseq | fapplyentryseq | varchar | 50 |  | √ | ' ' |  |
| 24 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fplansuretime | fplansuretime | timestamp | 0 |  |  | null |  |
| 26 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 27 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 28 | fwaitcheckqty | fwaitcheckqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fxkinwarmin | fxkinwarmin | numeric | 23 | 10 | √ | 0 |  |
| 30 | frptbsqty | frptbsqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 32 | fworkwastebsqty | fworkwastebsqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fpurpushqty | fpurpushqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fscrapbsqty | fscrapbsqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | fsourceentryseq | fsourceentryseq | varchar | 50 |  | √ | ' ' |  |
| 36 | fquainwaqty | fquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | frepairqty | frepairqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fxkinwarmax | fxkinwarmax | numeric | 23 | 10 | √ | 0 |  |
| 39 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | ftotalsplitqty | ftotalsplitqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | fnotreportbsqty | fnotreportbsqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | ftotalsplitbaseqty | ftotalsplitbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 43 | fisinspection | fisinspection | bpchar | 1 |  | √ | '0' |  |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 45 | forderbillno | 采购订单号 | varchar | 50 |  | √ | ' ' | 采购订单号 |
| 46 | fsampledestorybsqty | fsampledestorybsqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fisconreportqty | fisconreportqty | bpchar | 1 |  | √ | '0' |  |
| 48 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 49 | forderentryid | forderentryid | int8 | 64 |  | √ | 0 |  |
| 50 | fxkdemanddate | fxkdemanddate | timestamp | 0 |  |  | null |  |
| 51 | freportbsqty | freportbsqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | frepmaxqty | frepmaxqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 54 | fapplybillno | fapplybillno | varchar | 50 |  | √ | ' ' |  |
| 55 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 56 | frepmaxrate | frepmaxrate | numeric | 23 | 10 | √ | 0 |  |
| 57 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 58 | fqualifiedbsqty | fqualifiedbsqty | numeric | 23 | 10 | √ | 0 |  |
| 59 | frepmaxbsqty | frepmaxbsqty | numeric | 23 | 10 | √ | 0 |  |
| 60 | frepinwaqty | frepinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | fapplyentryid | fapplyentryid | int8 | 64 |  | √ | 0 |  |
| 62 | fsampledestoryqty | fsampledestoryqty | numeric | 23 | 10 | √ | 0 |  |
| 63 | fpurauditqty | fpurauditqty | numeric | 23 | 10 | √ | 0 |  |
| 64 | fsourcebillnumber | fsourcebillnumber | varchar | 50 |  | √ | ' ' |  |
| 65 | fsettletime | fsettletime | timestamp | 0 |  |  | null |  |
| 66 | fxkscrinwaqty | fxkscrinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | finnersupplier | finnersupplier | bpchar | 1 |  | √ | '0' |  |
| 68 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 69 | facceptbsqty | facceptbsqty | numeric | 23 | 10 | √ | 0 |  |
| 70 | fendworktime | fendworktime | timestamp | 0 |  |  | null |  |
| 71 | fmtlcostbsqty | fmtlcostbsqty | numeric | 23 | 10 | √ | 0 |  |

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

## 委外工单分录F7-主表 t_om_mftorderentry

- **表名称：** 委外工单分录F7-主表
- **表名：** t_om_mftorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | fplanqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fauxptyqty2 | fauxptyqty2 | numeric | 23 | 10 | √ | 0 |  |
| 5 | fclosetype | fclosetype | varchar | 10 |  | √ | ' ' |  |
| 6 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 7 | flocation | flocation | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0 |  |
| 10 | fmtlcostqty | fmtlcostqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fbaseunitexpoutqty | fbaseunitexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fstockqty | fstockqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | froutereplace | froutereplace | int8 | 64 |  | √ | 0 |  |
| 16 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 17 | finwarconsigner | finwarconsigner | int8 | 64 |  | √ | 0 |  |
| 18 | fismrpcal | fismrpcal | bpchar | 1 |  | √ | '0' |  |
| 19 | fxkdemandbillid | fxkdemandbillid | varchar | 50 |  | √ | ' ' |  |
| 20 | fparententryid | 上级主键 | int8 | 64 |  | √ | 0 | 上级主键 |
| 21 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 22 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 23 | fmanftechstatus | fmanftechstatus | varchar | 50 |  | √ | ' ' |  |
| 24 | finwarmin | finwarmin | numeric | 23 | 10 | √ | 0 |  |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 27 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 28 | funqualifiedqty | funqualifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 30 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fxkdemandbill | fxkdemandbill | varchar | 50 |  | √ | ' ' |  |
| 32 | fworkwasteqty | fworkwasteqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fkittingbaseqty | fkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 35 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 36 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 37 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 38 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 39 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 40 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 41 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 45 | frptqty | frptqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | fexpoutqty | fexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :结案 |
| 48 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 49 | fmaterialversion | fmaterialversion | int8 | 64 |  | √ | 0 |  |
| 50 | frcvinhighlimit | frcvinhighlimit | numeric | 23 | 10 | √ | 0 |  |
| 51 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 52 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 53 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 54 | fxkdemandbillentryid | fxkdemandbillentryid | varchar | 50 |  | √ | ' ' |  |
| 55 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 56 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 57 | finwardept | finwardept | int8 | 64 |  | √ | 0 |  |
| 58 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 59 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 60 | fqualifiedqty | fqualifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | fsrcsplitbillseq | fsrcsplitbillseq | int8 | 64 |  | √ | 0 |  |
| 62 | festscrapqty | festscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 63 | fkittingtime | fkittingtime | timestamp | 0 |  |  | null |  |
| 64 | fqualityorg | fqualityorg | int8 | 64 |  | √ | 0 |  |
| 65 | frcvinlowlimit | frcvinlowlimit | numeric | 23 | 10 | √ | 0 |  |
| 66 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 67 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 68 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 69 | finwarmax | finwarmax | numeric | 23 | 10 | √ | 0 |  |
| 70 | freportqty | freportqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fxkdemandseq | fxkdemandseq | int8 | 64 |  | √ | 0 |  |
| 72 | fkittingqty | fkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 73 | fxkdemandbillentity | fxkdemandbillentity | varchar | 50 |  | √ | ' ' |  |
| 74 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 75 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 76 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 77 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 78 | foutputoperation | foutputoperation | int8 | 64 |  | √ | 0 |  |
| 79 | fauxptyunit2 | fauxptyunit2 | int8 | 64 |  | √ | 0 |  |
| 80 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mftorderentry_fk |  | fid |
| 2 | pk_t_om_mftorderentry |  | fentryid |
