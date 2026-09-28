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
| 5 | fsuperiorstockentryid | fsuperiorstockentryid | int8 | 64 |  | √ | 0 |  |
| 6 | funquainwaqty | funquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | frepminbsqty | frepminbsqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | frootdemandentryid | frootdemandentryid | int8 | 64 |  | √ | 0 |  |
| 9 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 10 | fxkstockqty | fxkstockqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | frootdemandentryseq | frootdemandentryseq | int4 | 32 |  | √ | 0 |  |
| 12 | fwaitckbaseqty | fwaitckbaseqty | int8 | 64 |  | √ | 0 |  |
| 13 | fcrossqty | fcrossqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 15 | fxkquainwaqty | fxkquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fendcasetime | fendcasetime | timestamp | 0 |  |  | null |  |
| 17 | fscrinwaqty | fscrinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | frepminqty | frepminqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fapplyid | fapplyid | int8 | 64 |  | √ | 0 |  |
| 20 | frepminrate | frepminrate | numeric | 23 | 10 | √ | 0 |  |
| 21 | freworkbsqty | freworkbsqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 23 | forderentryseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 24 | fplanpreparetime | fplanpreparetime | timestamp | 0 |  |  | null |  |
| 25 | fnotreportqty | fnotreportqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fpickingpairs | fpickingpairs | numeric | 23 | 10 | √ | 0 |  |
| 27 | fapplyentryseq | fapplyentryseq | varchar | 50 |  | √ | ' ' |  |
| 28 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fplansuretime | fplansuretime | timestamp | 0 |  |  | null |  |
| 30 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 31 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 32 | fwaitcheckqty | fwaitcheckqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fxkinwarmin | fxkinwarmin | numeric | 23 | 10 | √ | 0 |  |
| 34 | frptbsqty | frptbsqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 36 | fworkwastebsqty | fworkwastebsqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fpurpushqty | fpurpushqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fscrapbsqty | fscrapbsqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | fsourceentryseq | fsourceentryseq | varchar | 50 |  | √ | ' ' |  |
| 40 | fquainwaqty | fquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 41 | frootdemandbillid | frootdemandbillid | int8 | 64 |  | √ | 0 |  |
| 42 | frepairqty | frepairqty | numeric | 23 | 10 | √ | 0 |  |
| 43 | fcrosspushbaseqty | fcrosspushbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fxkinwarmax | fxkinwarmax | numeric | 23 | 10 | √ | 0 |  |
| 45 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | ftotalsplitqty | ftotalsplitqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fnotreportbsqty | fnotreportbsqty | numeric | 23 | 10 | √ | 0 |  |
| 48 | ftotalsplitbaseqty | ftotalsplitbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fisinspection | fisinspection | bpchar | 1 |  | √ | '0' |  |
| 50 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 51 | fcrossbaseqty | fcrossbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | forderbillno | 采购订单号 | varchar | 50 |  | √ | ' ' | 采购订单号 |
| 53 | fsampledestorybsqty | fsampledestorybsqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | frootdemandentity | frootdemandentity | varchar | 50 |  | √ | ' ' |  |
| 55 | foutwaqty | foutwaqty | numeric | 23 | 10 | √ | 0 |  |
| 56 | fisconreportqty | fisconreportqty | bpchar | 1 |  | √ | '0' |  |
| 57 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 58 | forderentryid | forderentryid | int8 | 64 |  | √ | 0 |  |
| 59 | fxkdemanddate | fxkdemanddate | timestamp | 0 |  |  | null |  |
| 60 | freportbsqty | freportbsqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | frepmaxqty | frepmaxqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 63 | fapplybillno | fapplybillno | varchar | 50 |  | √ | ' ' |  |
| 64 | fxkoutwaqty | fxkoutwaqty | numeric | 23 | 10 | √ | 0 |  |
| 65 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 66 | frepmaxrate | frepmaxrate | numeric | 23 | 10 | √ | 0 |  |
| 67 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 68 | fqualifiedbsqty | fqualifiedbsqty | numeric | 23 | 10 | √ | 0 |  |
| 69 | frootdemandbillno | frootdemandbillno | varchar | 120 |  | √ | ' ' |  |
| 70 | frepmaxbsqty | frepmaxbsqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fcrosspushqty | fcrosspushqty | numeric | 23 | 10 | √ | 0 |  |
| 72 | frepinwaqty | frepinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 73 | fapplyentryid | fapplyentryid | int8 | 64 |  | √ | 0 |  |
| 74 | fsampledestoryqty | fsampledestoryqty | numeric | 23 | 10 | √ | 0 |  |
| 75 | fpurauditqty | fpurauditqty | numeric | 23 | 10 | √ | 0 |  |
| 76 | fsourcebillnumber | fsourcebillnumber | varchar | 50 |  | √ | ' ' |  |
| 77 | fsettletime | fsettletime | timestamp | 0 |  |  | null |  |
| 78 | fxkscrinwaqty | fxkscrinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 79 | finnersupplier | finnersupplier | bpchar | 1 |  | √ | '0' |  |
| 80 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 81 | facceptbsqty | facceptbsqty | numeric | 23 | 10 | √ | 0 |  |
| 82 | fendworktime | fendworktime | timestamp | 0 |  |  | null |  |
| 83 | fmtlcostbsqty | fmtlcostbsqty | numeric | 23 | 10 | √ | 0 |  |

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

## 委外工单分录F7-分表 t_om_mftorderentry_f

- **表名称：** 委外工单分录F7-分表
- **表名：** t_om_mftorderentry_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowsrctype | frowsrctype | varchar | 5 |  | √ | ' ' |  |
| 3 | frepairbaseqty | frepairbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 5 | fstockedbaseqty | fstockedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | fworkwasteinvbsqty | fworkwasteinvbsqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fscrapinvqty | fscrapinvqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fisgeneratedsuborder | fisgeneratedsuborder | bpchar | 1 |  | √ | '0' |  |
| 9 | fpurreturnqty | fpurreturnqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fclosereason | fclosereason | varchar | 500 |  | √ | ' ' |  |
| 11 | fscrapinvbsqty | fscrapinvbsqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fstockedqty | fstockedqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 14 | fworkwasteinvqty | fworkwasteinvqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fcrossreturntype | fcrossreturntype | varchar | 5 |  | √ | ' ' |  |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fpurreturnbaseqty | fpurreturnbaseqty | numeric | 23 | 10 | √ | 0 |  |
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
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | froutereplace | froutereplace | int8 | 64 |  | √ | 0 |  |
| 16 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 17 | finwarconsigner | finwarconsigner | int8 | 64 |  | √ | 0 |  |
| 18 | fismrpcal | fismrpcal | bpchar | 1 |  | √ | '0' |  |
| 19 | fxkdemandbillid | fxkdemandbillid | varchar | 50 |  | √ | ' ' |  |
| 20 | finvkittingqty | finvkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fparententryid | 上级主键 | int8 | 64 |  | √ | 0 | 上级主键 |
| 22 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 23 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 24 | fmanftechstatus | fmanftechstatus | varchar | 50 |  | √ | ' ' |  |
| 25 | finwarmin | finwarmin | numeric | 23 | 10 | √ | 0 |  |
| 26 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | fkittingsupplydate | fkittingsupplydate | timestamp | 0 |  |  | null |  |
| 28 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 29 | fpurorgid | fpurorgid | int8 | 64 |  | √ | 0 |  |
| 30 | fisreserved | fisreserved | bpchar | 1 |  | √ | '0' |  |
| 31 | funqualifiedqty | funqualifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 33 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 34 | fxkdemandbill | fxkdemandbill | varchar | 50 |  | √ | ' ' |  |
| 35 | fworkwasteqty | fworkwasteqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | fkittingbaseqty | fkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 38 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 39 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 40 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 41 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 42 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 43 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 44 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 48 | fkittingid | fkittingid | int8 | 64 |  | √ | 0 |  |
| 49 | frptqty | frptqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fexpoutqty | fexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | fexpkittingqty | fexpkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :结案 |
| 53 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 54 | fmaterialversion | fmaterialversion | int8 | 64 |  | √ | 0 |  |
| 55 | frcvinhighlimit | frcvinhighlimit | numeric | 23 | 10 | √ | 0 |  |
| 56 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 57 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 58 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 59 | fxkdemandbillentryid | fxkdemandbillentryid | varchar | 50 |  | √ | ' ' |  |
| 60 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 61 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 62 | finwardept | finwardept | int8 | 64 |  | √ | 0 |  |
| 63 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 64 | fkittingsign | fkittingsign | varchar | 5 |  | √ | ' ' |  |
| 65 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 66 | fqualifiedqty | fqualifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | fexpkittingbaseqty | fexpkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 68 | fsrcsplitbillseq | fsrcsplitbillseq | int8 | 64 |  | √ | 0 |  |
| 69 | festscrapqty | festscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 70 | fkittingtime | fkittingtime | timestamp | 0 |  |  | null |  |
| 71 | fqualityorg | fqualityorg | int8 | 64 |  | √ | 0 |  |
| 72 | frcvinlowlimit | frcvinlowlimit | numeric | 23 | 10 | √ | 0 |  |
| 73 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 74 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 75 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 76 | finwarmax | finwarmax | numeric | 23 | 10 | √ | 0 |  |
| 77 | freportqty | freportqty | numeric | 23 | 10 | √ | 0 |  |
| 78 | fxkdemandseq | fxkdemandseq | int8 | 64 |  | √ | 0 |  |
| 79 | fkittingqty | fkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 80 | fxkdemandbillentity | fxkdemandbillentity | varchar | 50 |  | √ | ' ' |  |
| 81 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 82 | finvkittingbaseqty | finvkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 83 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 84 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 85 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 86 | foutputoperation | foutputoperation | int8 | 64 |  | √ | 0 |  |
| 87 | fauxptyunit2 | fauxptyunit2 | int8 | 64 |  | √ | 0 |  |
| 88 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mftorderentry_fk |  | fid |
| 2 | pk_t_om_mftorderentry |  | fentryid |
