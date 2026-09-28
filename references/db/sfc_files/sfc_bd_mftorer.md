# 生产工单-sfc_bd_mftorer

## 生产工单-主表 t_pom_mftorder

- **表名称：** 生产工单-主表
- **表名：** t_pom_mftorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 500 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 8 | fasyncstatussfc | fasyncstatussfc | varchar | 50 |  | √ | ' ' |  |
| 9 | fasyncstatuspom | fasyncstatuspom | varchar | 50 |  | √ | ' ' |  |
| 10 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 11 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 12 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 13 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fisrework | fisrework | bpchar | 1 |  | √ | '0' |  |
| 17 | fbiztype | fbiztype | varchar | 50 |  | √ | ' ' |  |
| 18 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mftorder_fk |  | fbillno |
| 2 | idx_mftorder_createtime |  | fcreatetime |
| 3 | idx_pom_mftorder_orgidfid |  | forgid,fid |
| 4 | t_pom_mftorder_pkey |  | fid |

---

## 生产工单明细-子表 t_pom_mftorderentry

- **表名称：** 生产工单明细-子表
- **表名：** t_pom_mftorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanqty | fplanqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fclosetype | fclosetype | varchar | 10 |  | √ | ' ' |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fbaseunitexpoutqty | fbaseunitexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fbaseunit | fbaseunit | int8 | 64 |  | √ | 0 |  |
| 9 | froutereplace | froutereplace | int8 | 64 |  | √ | 0 |  |
| 10 | fauxproperty | fauxproperty | int8 | 64 |  | √ | 0 |  |
| 11 | fbomid | fbomid | int8 | 64 |  | √ | 0 |  |
| 12 | fismrpcal | fismrpcal | bpchar | 1 |  | √ | '0' |  |
| 13 | fxkdemandbillid | fxkdemandbillid | varchar | 50 |  | √ | ' ' |  |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 15 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 16 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 17 | fmanftechstatus | fmanftechstatus | varchar | 30 |  | √ | ' ' |  |
| 18 | fplanpreparetime | fplanpreparetime | timestamp | 0 |  |  | null |  |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 21 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 22 | fsrcorderentryid | fsrcorderentryid | int8 | 64 |  | √ | 0 |  |
| 23 | fxkdemandbill | fxkdemandbill | varchar | 50 |  | √ | ' ' |  |
| 24 | fkittingbaseqty | fkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fprocessroute | fprocessroute | int8 | 64 |  | √ | 0 |  |
| 26 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 27 | fplanbegintime | fplanbegintime | timestamp | 0 |  |  | null |  |
| 28 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 29 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 30 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 34 | fexpoutqty | fexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :结案 |
| 36 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 37 | fmaterialversion | fmaterialversion | int8 | 64 |  | √ | 0 |  |
| 38 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 39 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 40 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 41 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 42 | fxkdemandbillentryid | fxkdemandbillentryid | varchar | 50 |  | √ | ' ' |  |
| 43 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 44 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 45 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 46 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 47 | fsrcsplitbillseq | fsrcsplitbillseq | int8 | 64 |  | √ | 0 |  |
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
| 60 | fexpendbomtime | fexpendbomtime | timestamp | 0 |  |  | null |  |
| 61 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | fplanendtime | fplanendtime | timestamp | 0 |  |  | null |  |
| 63 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 64 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0.0000000000 |  |

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
