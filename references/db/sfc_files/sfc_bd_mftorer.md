# 生产工单-sfc_bd_mftorer

## 生产工单-主表 t_pom_mftorder

- **表名称：** 生产工单-主表
- **表名：** t_pom_mftorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftransactiontype | ftransactiontype | int8 | 64 |  | √ | 0 |  |
| 5 | fasyncstatuspom | fasyncstatuspom | varchar | 50 |  | √ | ' ' |  |
| 6 | finterprocess | finterprocess | bpchar | 1 |  | √ | '0' |  |
| 7 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 8 | fisinit | fisinit | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fentrustdept | 委托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fisrework | fisrework | bpchar | 1 |  | √ | '0' |  |
| 12 | fbiztype | fbiztype | varchar | 50 |  | √ | ' ' |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | fremark | varchar | 500 |  | √ | ' ' |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | fasyncstatussfc | fasyncstatussfc | varchar | 50 |  | √ | ' ' |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fbillcretype | fbillcretype | varchar | 5 |  | √ | ' ' |  |
| 22 | fisdevproduce | fisdevproduce | bpchar | 1 |  | √ | '0' |  |
| 23 | fk_bj73_textareafield | fk_bj73_textareafield | varchar | 500 |  | √ | ' ' |  |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 25 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
| 14 | finvkittingqty | finvkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 16 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 17 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 18 | fmanftechstatus | fmanftechstatus | varchar | 30 |  | √ | ' ' |  |
| 19 | fplanpreparetime | fplanpreparetime | timestamp | 0 |  |  | null |  |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 21 | fkittingsupplydate | fkittingsupplydate | timestamp | 0 |  |  | null |  |
| 22 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 23 | fisreserved | fisreserved | bpchar | 1 |  | √ | '0' |  |
| 24 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 25 | fsrcorderentryid | fsrcorderentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fxkdemandbill | fxkdemandbill | varchar | 50 |  | √ | ' ' |  |
| 27 | fkittingbaseqty | fkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprocessroute | fprocessroute | int8 | 64 |  | √ | 0 |  |
| 29 | fbeginbookdate | fbeginbookdate | timestamp | 0 |  |  | null |  |
| 30 | fplanbegintime | fplanbegintime | timestamp | 0 |  |  | null |  |
| 31 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 32 | fmanuversion | fmanuversion | int8 | 64 |  | √ | 0 |  |
| 33 | fkittingstatus | 齐套状态 | varchar | 30 |  | √ | ' ' | 齐套状态,枚举: A :未检查 B :短缺 C :可用 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 37 | fkittingid | fkittingid | int8 | 64 |  | √ | 0 |  |
| 38 | fexpoutqty | fexpoutqty | numeric | 23 | 10 | √ | 0 |  |
| 39 | fexpkittingqty | fexpkittingqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 41 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :结案 |
| 42 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 43 | fmaterialversion | fmaterialversion | int8 | 64 |  | √ | 0 |  |
| 44 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 45 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 46 | fmaterialspread | fmaterialspread | bpchar | 1 |  | √ | '1' |  |
| 47 | fclosebookdate | fclosebookdate | timestamp | 0 |  |  | null |  |
| 48 | fxkdemandbillentryid | fxkdemandbillentryid | varchar | 50 |  | √ | ' ' |  |
| 49 | freplaceno | freplaceno | varchar | 50 |  | √ | ' ' |  |
| 50 | fsrcsplitbillnumber | fsrcsplitbillnumber | varchar | 50 |  | √ | ' ' |  |
| 51 | fpickstatus | 领料状态 | varchar | 30 |  | √ | ' ' | 领料状态,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 52 | fkittingsign | fkittingsign | varchar | 5 |  | √ | ' ' |  |
| 53 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 54 | fexpkittingbaseqty | fexpkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fprodline | fprodline | int8 | 64 |  | √ | 0 |  |
| 56 | fsrcsplitbillseq | fsrcsplitbillseq | int8 | 64 |  | √ | 0 |  |
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
| 69 | fexpendbomtime | fexpendbomtime | timestamp | 0 |  |  | null |  |
| 70 | finvkittingbaseqty | finvkittingbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fplanbaseqty | fplanbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 72 | fplanendtime | fplanendtime | timestamp | 0 |  |  | null |  |
| 73 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 74 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0.0000000000 |  |

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
