# 委外工单变更单-om_xmftorder

## 产品明细-子表 t_om_xmftorderentry

- **表名称：** 产品明细-子表
- **表名：** t_om_xmftorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | 拆分前数量 | numeric | 23 | 10 | √ | 0 | 拆分前数量 |
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 5 | fclosetype | 关闭类型 | varchar | 10 |  | √ | ' ' | 关闭类型,枚举: A :自动关闭 B :手工关闭 C :拆分关闭 |
| 6 | fiscontrolqty | 控制入库数量 | bpchar | 1 |  | √ | '0' | 控制入库数量 |
| 7 | flocation | 入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fyieldrate | 成品率% | numeric | 23 | 4 | √ | 0 | 成品率% |
| 10 | fmtlcostqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 11 | fbaseunitexpoutqty | 基本单位预计产出数量 | numeric | 23 | 10 | √ | 0 | 基本单位预计产出数量 |
| 12 | fstockqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库基本数量 |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fsrcbillentryseq | 委外工单行号 | varchar | 50 |  | √ | ' ' | 委外工单行号 |
| 15 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | froutereplace | 工艺路线替代号 | int8 | 64 |  | √ | 0 | 基础资料带组织模板 mpdm_routereplace |
| 17 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 18 | finwarconsigner | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fxkdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 21 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 22 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 23 | fmanftechstatus | 工序计划状态 | varchar | 50 |  | √ | ' ' | 工序计划状态,枚举: T :存在工序计划 F :不存在工序计划 |
| 24 | finwarmin | 入库下限基本数量 | numeric | 23 | 10 | √ | 0 | 入库下限基本数量 |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 27 | fpurorgid | 采购组织1 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 29 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 30 | fsrcbillid | 委外工单内码 | varchar | 50 |  | √ | ' ' | 委外工单内码 |
| 31 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 32 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 33 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线 mpdm_sfcprocessroute |
| 34 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 35 | fwarehouse | 入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 36 | fbeginbookdate | 开工记账日期 | timestamp | 0 |  |  | null | 开工记账日期 |
| 37 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 38 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 39 | fsrcbillno1 | fsrcbillno1 | varchar | 50 |  | √ | ' ' |  |
| 40 | fmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | 生产版本 pdm_manuversion |
| 41 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 45 | frptqty | 关联收货数量 | numeric | 23 | 10 | √ | 0 | 关联收货数量 |
| 46 | fsrcbillno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 47 | fexpoutqty | 预计产出数量 | numeric | 23 | 10 | √ | 0 | 预计产出数量 |
| 48 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 49 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 50 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 51 | frcvinhighlimit | 入库上限允差(%) | numeric | 23 | 10 | √ | 0 | 入库上限允差(%) |
| 52 | fchangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 53 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 54 | fmaterialspread | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 55 | fclosebookdate | 关闭记账日期 | timestamp | 0 |  |  | null | 关闭记账日期 |
| 56 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 57 | freplaceno | 替代号1 | varchar | 50 |  | √ | ' ' | 替代号1 |
| 58 | fsrcsplitbillnumber | 来源拆分工单编码 | varchar | 50 |  | √ | ' ' | 来源拆分工单编码 |
| 59 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 60 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 61 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 62 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 63 | fsrcsplitbillseq | 来源拆分工单行号 | int8 | 64 |  | √ | 0 | 委外工单分录F7 om_mftorder_f7 |
| 64 | festscrapqty | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 65 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 66 | frcvinlowlimit | 入库下限允差(%) | numeric | 23 | 10 | √ | 0 | 入库下限允差(%) |
| 67 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 68 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 69 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 70 | finwarmax | 入库上限基本数量 | numeric | 23 | 10 | √ | 0 | 入库上限基本数量 |
| 71 | fsrcbillentryid | 委外工单行内码 | varchar | 50 |  | √ | ' ' | 委外工单行内码 |
| 72 | freportqty | 收货数量 | numeric | 23 | 10 | √ | 0 | 收货数量 |
| 73 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 74 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 75 | fexpendbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 76 | fplanbaseqty | 拆分前基本数量 | numeric | 23 | 10 | √ | 0 | 拆分前基本数量 |
| 77 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 78 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 79 | foutputoperation | 产出工序 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 80 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 81 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

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
| 5 | funquainwaqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库基本数量 |
| 6 | frepminbsqty | 收货下限基本数量 | numeric | 23 | 10 | √ | 0 | 收货下限基本数量 |
| 7 | forderid | 采购订单ID | int8 | 64 |  | √ | 0 | 采购订单ID |
| 8 | fxkstockqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 9 | fwaitckbaseqty | 待检品入库基本数量 | int8 | 64 |  | √ | 0 | 待检品入库基本数量 |
| 10 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 11 | fxkquainwaqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 12 | fendcasetime | 齐套时间 | timestamp | 0 |  |  | null | 齐套时间 |
| 13 | fscrinwaqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品入库基本数量 |
| 14 | frepminqty | 收货下限数量 | numeric | 23 | 10 | √ | 0 | 收货下限数量 |
| 15 | fapplyid | 采购申请单ID | int8 | 64 |  | √ | 0 | 采购申请单ID |
| 16 | frepminrate | 收货下限允差(%) | numeric | 10 | 2 | √ | 0 | 收货下限允差(%) |
| 17 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 20 | forderentryseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 21 | fnotreportqty | 待收货数量 | numeric | 23 | 10 | √ | 0 | 待收货数量 |
| 22 | fpickingpairs | 已领套数 | numeric | 23 | 10 | √ | 0 | 已领套数 |
| 23 | fapplyentryseq | 采购申请单行号 | varchar | 50 |  | √ | ' ' | 采购申请单行号 |
| 24 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 25 | fplansuretime | 计划确认时间 | timestamp | 0 |  |  | null | 计划确认时间 |
| 26 | fstartworktime | 开工时间 | timestamp | 0 |  |  | null | 开工时间 |
| 27 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 28 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 29 | fwaitcheckqty | 待检品入库数量 | numeric | 23 | 10 | √ | 0 | 待检品入库数量 |
| 30 | fxkinwarmin | 入库下限数量 | numeric | 23 | 10 | √ | 0 | 入库下限数量 |
| 31 | frptbsqty | 关联收货基本数量 | numeric | 23 | 10 | √ | 0 | 关联收货基本数量 |
| 32 | fheadbillno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 33 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 34 | fpurpushqty | 关联采购基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购基本数量 |
| 35 | fscrapbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 36 | fsourceentryseq | 来源单据分录行号 | varchar | 50 |  | √ | ' ' | 来源单据分录行号 |
| 37 | fquainwaqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 38 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0 | 返修数量 |
| 39 | fxkinwarmax | 入库上限数量 | numeric | 23 | 10 | √ | 0 | 入库上限数量 |
| 40 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 41 | ftotalsplitqty | 已拆分数量 | numeric | 23 | 10 | √ | 0 | 已拆分数量 |
| 42 | fnotreportbsqty | 待收货基本数量 | numeric | 23 | 10 | √ | 0 | 待收货基本数量 |
| 43 | ftotalsplitbaseqty | 已拆分基本数量 | numeric | 23 | 10 | √ | 0 | 已拆分基本数量 |
| 44 | fisinspection | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 46 | forderbillno | 采购订单号 | varchar | 50 |  | √ | ' ' | 采购订单号 |
| 47 | fisconreportqty | 控制收货数量 | bpchar | 1 |  | √ | '0' | 控制收货数量 |
| 48 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 49 | forderentryid | 采购订单行ID | int8 | 64 |  | √ | 0 | 采购订单行ID |
| 50 | fxkdemanddate | 订单需求日期 | timestamp | 0 |  |  | null | 订单需求日期 |
| 51 | freportbsqty | 收货基本数量 | numeric | 23 | 10 | √ | 0 | 收货基本数量 |
| 52 | frepmaxqty | 收货上限数量 | numeric | 23 | 10 | √ | 0 | 收货上限数量 |
| 53 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 54 | fapplybillno | 采购申请单号 | varchar | 50 |  | √ | ' ' | 采购申请单号 |
| 55 | ftransmittime | 下达时间 | timestamp | 0 |  |  | null | 下达时间 |
| 56 | frepmaxrate | 收货上限允差(%) | numeric | 10 | 2 | √ | 0 | 收货上限允差(%) |
| 57 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 58 | fqualifiedbsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 59 | frepmaxbsqty | 收货上限基本数量 | numeric | 23 | 10 | √ | 0 | 收货上限基本数量 |
| 60 | frepinwaqty | 返工品入库数量 | numeric | 23 | 10 | √ | 0 | 返工品入库数量 |
| 61 | fapplyentryid | 申请单行ID | int8 | 64 |  | √ | 0 | 申请单行ID |
| 62 | fpurauditqty | 采购执行基本数量 | numeric | 23 | 10 | √ | 0 | 采购执行基本数量 |
| 63 | fsourcebillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 64 | fsettletime | 结算时间 | timestamp | 0 |  |  | null | 结算时间 |
| 65 | fxkscrinwaqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 66 | finnersupplier | 内部供应商 | bpchar | 1 |  | √ | '0' | 内部供应商 |
| 67 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 68 | facceptbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 69 | fendworktime | 完工时间 | timestamp | 0 |  |  | null | 完工时间 |
| 70 | fmtlcostbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_xmftorderentry_e_fk |  | fid |
| 2 | idx_om_xmftordere_materialid |  | fmaterielmasterid |
| 3 | pk_om_xmftorderentry_e |  | fentryid |

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
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | forg1 | forg1 | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsupplierhead | 委外加工商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 10 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | freason | 变更原因 | varchar | 512 |  | √ | ' ' | 变更原因 |
| 13 | freasonid | 变更原因 | int8 | 64 |  | √ | 0 | 变更原因 pdm_ecnreason |
| 14 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fpurorghead | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fsupplier1 | fsupplier1 | int8 | 64 |  | √ | 0 |  |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
