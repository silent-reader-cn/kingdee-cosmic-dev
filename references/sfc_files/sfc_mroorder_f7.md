# 检修工单分录F7(废弃)-sfc_mroorder_f7

## 检修工单分录F7(废弃)-分表 t_pom_mroorderentry_e

- **表名称：** 检修工单分录F7(废弃)-分表
- **表名：** t_pom_mroorderentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facceptqty | facceptqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fisshortage | fisshortage | bpchar | 1 |  | √ | '0' |  |
| 4 | funquainwaqty | funquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fiscontrolqty | fiscontrolqty | bpchar | 1 |  | √ | '0' |  |
| 6 | fswspageno | 补充工作单页码 | int8 | 64 |  | √ | 0 | 补充工作单页码 |
| 7 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0 |  |
| 8 | fmtlcostqty | fmtlcostqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fstockqty | fstockqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fcontrolno | 控制号 | varchar | 50 |  | √ | ' ' | 控制号 |
| 11 | froutereplace | froutereplace | int8 | 64 |  | √ | 0 |  |
| 12 | finwarconsigner | finwarconsigner | int8 | 64 |  | √ | 0 |  |
| 13 | fendcasetime | fendcasetime | timestamp | 0 |  |  | null |  |
| 14 | fscrinwaqty | fscrinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | frepminqty | frepminqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fappendixno | 附录编号 | varchar | 50 |  | √ | ' ' | 附录编号 |
| 17 | frepminrate | frepminrate | numeric | 23 | 10 | √ | 0 |  |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | fplanpreparetime | fplanpreparetime | timestamp | 0 |  |  | null |  |
| 20 | ftarno | 技术文件编号 | varchar | 50 |  | √ | ' ' | 技术文件编号 |
| 21 | finwarmin | finwarmin | numeric | 23 | 10 | √ | 0 |  |
| 22 | freasonoferror | freasonoferror | varchar | 255 |  | √ | ' ' |  |
| 23 | fpickingpairs | fpickingpairs | numeric | 23 | 10 | √ | 0 |  |
| 24 | funqualifiedqty | funqualifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fwaitcheckqty | fwaitcheckqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fisomtool | fisomtool | bpchar | 1 |  | √ | '0' |  |
| 28 | fworkwasteqty | fworkwasteqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fquainwaqty | fquainwaqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | frepairqty | frepairqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 32 | freworkqty | freworkqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | farea | 工作区域 | int8 | 64 |  | √ | 0 | 工作区域 mpdm_area |
| 34 | fisinspection | fisinspection | bpchar | 1 |  | √ | '0' |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | frptqty | frptqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fisfirstexe | fisfirstexe | bpchar | 1 |  | √ | '0' |  |
| 38 | frcvinhighlimit | frcvinhighlimit | numeric | 23 | 10 | √ | 0 |  |
| 39 | fisconreportqty | fisconreportqty | bpchar | 1 |  | √ | '0' |  |
| 40 | fplandays | fplandays | int8 | 64 |  | √ | 0 |  |
| 41 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 42 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 43 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 44 | frepmaxqty | frepmaxqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | fisomexe | fisomexe | bpchar | 1 |  | √ | '0' |  |
| 46 | fqualifiedqty | fqualifiedqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | frepmaxrate | frepmaxrate | numeric | 23 | 10 | √ | 0 |  |
| 48 | fsrcsplitbillseq | fsrcsplitbillseq | int8 | 64 |  | √ | 0 |  |
| 49 | festscrapqty | festscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | frepinwaqty | frepinwaqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | fqualityorg | fqualityorg | int8 | 64 |  | √ | 0 |  |
| 52 | frcvinlowlimit | frcvinlowlimit | numeric | 23 | 10 | √ | 0 |  |
| 53 | finwarmax | finwarmax | numeric | 23 | 10 | √ | 0 |  |
| 54 | freportqty | freportqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fexpendbomtime | fexpendbomtime | timestamp | 0 |  |  | null |  |
| 56 | foutputoperation | foutputoperation | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mroorderentry_e_fk |  | fid |
| 2 | pk_pom_mroorderentry_e |  | fentryid |

---

## 检修工单分录F7(废弃)-主表 t_pom_mroorderentry

- **表名称：** 检修工单分录F7(废弃)-主表
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
| 8 | fworkcardid | fworkcardid | int8 | 64 |  | √ | 0 |  |
| 9 | fbdproject | 系统云项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fexecondition | 执行条件 | int8 | 64 |  | √ | 0 | 执行条件 mpdm_execondition |
| 12 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 15 | fataid | fataid | int8 | 64 |  | √ | 0 |  |
| 16 | fpageseq | 页码 | varchar | 50 |  | √ | ' ' | 页码 |
| 17 | fparententryid | 上级主键 | int8 | 64 |  | √ | 0 | 上级主键 |
| 18 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 E :取消 F :保留 G :重下达 H :暂停 J :废弃 |
| 19 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 20 | fmanftechstatus | fmanftechstatus | varchar | 50 |  | √ | ' ' |  |
| 21 | fisassistmanual | fisassistmanual | bpchar | 1 |  | √ | '0' |  |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | fisom | fisom | bpchar | 1 |  | √ | '0' |  |
| 24 | fdefecttypeid | fdefecttypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 26 | fplansuretime | fplansuretime | timestamp | 0 |  |  | null |  |
| 27 | fstartworktime | fstartworktime | timestamp | 0 |  |  | null |  |
| 28 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 29 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 30 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fheadbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 32 | fismajordefect | fismajordefect | bpchar | 1 |  | √ | '0' |  |
| 33 | factualhours | 实际消耗工时 | numeric | 23 | 10 | √ | 0 | 实际消耗工时 |
| 34 | fprocessroute | 工艺路线编码 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 35 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 36 | fsourceentryseq | fsourceentryseq | varchar | 50 |  | √ | ' ' |  |
| 37 | fmartype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 38 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 39 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 40 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 41 | fwbsid | fwbsid | int8 | 64 |  | √ | 0 |  |
| 42 | fdefectdesc | fdefectdesc | varchar | 500 |  | √ | ' ' |  |
| 43 | fkittingstatus | 齐套状态 | varchar | 50 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 44 | fmaterielmtc | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 45 | fworkstage | 工作类别 | int8 | 64 |  | √ | 0 | 工作类别 mpdm_workcategories |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 48 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 49 | fassisterid | fassisterid | int8 | 64 |  | √ | 0 |  |
| 50 | fzone | fzone | int8 | 64 |  | √ | 0 |  |
| 51 | fpriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 52 | fata | fata | varchar | 50 |  | √ | ' ' |  |
| 53 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :结案 |
| 54 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 55 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 56 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 57 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 58 | finwardept | finwardept | int8 | 64 |  | √ | 0 |  |
| 59 | fpickstatus | 领料状态 | varchar | 50 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 60 | fworkcenterid | fworkcenterid | int8 | 64 |  | √ | 0 |  |
| 61 | fprojecttaskid | fprojecttaskid | int8 | 64 |  | √ | 0 |  |
| 62 | fmaintrade | fmaintrade | int8 | 64 |  | √ | 0 |  |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 64 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 65 | fisrecheck | fisrecheck | bpchar | 1 |  | √ | '0' |  |
| 66 | fmodifystatustime | fmodifystatustime | timestamp | 0 |  |  | null |  |
| 67 | fdefectreasonid | fdefectreasonid | int8 | 64 |  | √ | 0 |  |
| 68 | fworkhourunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 69 | fisassist | fisassist | bpchar | 1 |  | √ | '0' |  |
| 70 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 71 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 72 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 73 | fproductmodel | fproductmodel | int8 | 64 |  | √ | 0 |  |
| 74 | fplanhours | fplanhours | numeric | 23 | 10 | √ | 0 |  |
| 75 | fsourcebillnumber | fsourcebillnumber | varchar | 50 |  | √ | ' ' |  |
| 76 | fassisthours | fassisthours | numeric | 23 | 10 | √ | 0 |  |
| 77 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 78 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 80 | fresourcestatus | 资源就绪状态 | varchar | 50 |  | √ | ' ' | 资源就绪状态,枚举: A :未就绪 B :预计就绪 C :实际就绪 |
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

---

## WBS-多选基础资料表 t_pom_mulwbs

- **表名称：** WBS-多选基础资料表
- **表名：** t_pom_mulwbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | WBS pmts_wbs |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_mulwbs |  | fpkid |
| 2 | idx_pom_mulwbs_fk |  | fentryid |
