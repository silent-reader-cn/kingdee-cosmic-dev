# 检修工单F7-pom_mroorderno_f7

## 检修工单F7-主表 t_pom_mroorderentry

- **表名称：** 检修工单F7-主表
- **表名：** t_pom_mroorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | fplanqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fdefectsiteid | fdefectsiteid | int8 | 64 |  | √ | 0 |  |
| 4 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 5 | fdisposalmeasuresid | fdisposalmeasuresid | int8 | 64 |  | √ | 0 |  |
| 6 | flocation | flocation | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fworkcardid | 工卡 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 9 | fbdproject | fbdproject | int8 | 64 |  | √ | 0 |  |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fexecondition | fexecondition | int8 | 64 |  | √ | 0 |  |
| 12 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 15 | fataid | fataid | int8 | 64 |  | √ | 0 |  |
| 16 | fpageseq | fpageseq | varchar | 50 |  | √ | ' ' |  |
| 17 | fparententryid | 上级主键 | int8 | 64 |  | √ | 0 | 上级主键 |
| 18 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 19 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 20 | fmanftechstatus | fmanftechstatus | varchar | 50 |  | √ | ' ' |  |
| 21 | fisassistmanual | fisassistmanual | bpchar | 1 |  | √ | '0' |  |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | fisom | fisom | bpchar | 1 |  | √ | '0' |  |
| 24 | fdefecttypeid | fdefecttypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 26 | fplansuretime | fplansuretime | timestamp | 0 |  |  | null |  |
| 27 | fstartworktime | fstartworktime | timestamp | 0 |  |  | null |  |
| 28 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 29 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 30 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 32 | fismajordefect | fismajordefect | bpchar | 1 |  | √ | '0' |  |
| 33 | factualhours | factualhours | numeric | 23 | 10 | √ | 0 |  |
| 34 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 35 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 36 | fsourceentryseq | fsourceentryseq | varchar | 50 |  | √ | ' ' |  |
| 37 | fmartype | 检修设备类型 | int8 | 64 |  | √ | 0 | [检修设备类型 mpdm_mrtype](../mpdm_files/mpdm_mrtype.md) |
| 38 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 39 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 40 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 41 | fwbsid | fwbsid | int8 | 64 |  | √ | 0 |  |
| 42 | fdefectdesc | fdefectdesc | varchar | 500 |  | √ | ' ' |  |
| 43 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 44 | fmaterielmtc | 检修设备注册号 | int8 | 64 |  | √ | 0 | [物料检修信息 mpdm_materialmtcinfo](../mpdm_files/mpdm_materialmtcinfo.md) |
| 45 | fworkstage | fworkstage | int8 | 64 |  | √ | 0 |  |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 48 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 49 | fassisterid | fassisterid | int8 | 64 |  | √ | 0 |  |
| 50 | fzone | fzone | int8 | 64 |  | √ | 0 |  |
| 51 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 52 | fata | fata | varchar | 50 |  | √ | ' ' |  |
| 53 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 54 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 55 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 56 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 57 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 58 | finwardept | finwardept | int8 | 64 |  | √ | 0 |  |
| 59 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 60 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 61 | fprojecttaskid | fprojecttaskid | int8 | 64 |  | √ | 0 |  |
| 62 | fmaintrade | fmaintrade | int8 | 64 |  | √ | 0 |  |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 64 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 65 | fisrecheck | fisrecheck | bpchar | 1 |  | √ | '0' |  |
| 66 | fmodifystatustime | fmodifystatustime | timestamp | 0 |  |  | null |  |
| 67 | fdefectreasonid | fdefectreasonid | int8 | 64 |  | √ | 0 |  |
| 68 | fworkhourunitid | fworkhourunitid | int8 | 64 |  | √ | 0 |  |
| 69 | fisassist | fisassist | bpchar | 1 |  | √ | '0' |  |
| 70 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 71 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 72 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 73 | fproductmodel | fproductmodel | int8 | 64 |  | √ | 0 |  |
| 74 | fplanhours | fplanhours | numeric | 23 | 10 | √ | 0 |  |
| 75 | fsourcebillnumber | fsourcebillnumber | varchar | 50 |  | √ | ' ' |  |
| 76 | fassisthours | fassisthours | numeric | 23 | 10 | √ | 0 |  |
| 77 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 78 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 80 | fresourcestatus | fresourcestatus | varchar | 50 |  | √ | ' ' |  |
| 81 | fendworktime | fendworktime | timestamp | 0 |  |  | null |  |
| 82 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_mroorderentry |  | fentryid |
| 2 | idx_mroorderentry_fcfgcodeid |  | fconfiguredcodeid |
| 3 | idx_mroorderentry_ftrackid |  | ftracknumberid |
| 4 | idx_pom_mroorderentry_fsrcseq |  | fsourceentryseq |
| 5 | idx_mroorderentry_fk |  | fid |
