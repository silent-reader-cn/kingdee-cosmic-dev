# 工序计划F7-sfc_processplan_f7

## 工序计划F7-主表 t_sfc_processplan

- **表名称：** 工序计划F7-主表
- **表名：** t_sfc_processplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrout | fprocessrout | int8 | 64 |  | √ | 0 |  |
| 3 | fworkentryf7 | 生产工单分录 | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fworkshop | 生产车间(作废) | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 6 | fbaseunit | fbaseunit | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fprojno | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 9 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fworkrowid | 工单行id | int8 | 64 |  | √ | 0 | 工单行id |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | fworkn | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 13 | fprocessroutechange | fprocessroutechange | bpchar | 1 |  | √ | '0' |  |
| 14 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 15 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 16 | fentrustorgid | fentrustorgid | int8 | 64 |  | √ | 0 |  |
| 17 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 18 | fsourcebillno | fsourcebillno | varchar | 80 |  | √ | ' ' |  |
| 19 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 20 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fsourcebilltype | fsourcebilltype | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 24 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 27 | fworkrown | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |
| 28 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | funit | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fmaterielfieldid | fmaterielfieldid | int8 | 64 |  | √ | 0 |  |
| 32 | fsbillentity | fsbillentity | varchar | 50 |  | √ | ' ' |  |
| 33 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 34 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 36 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 37 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 38 | fworkid | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 39 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 41 | fisread | fisread | bpchar | 1 |  | √ | '0' |  |
| 42 | fpickstatus | fpickstatus | bpchar | 1 |  | √ | ' ' |  |
| 43 | fsourcebillrowid | fsourcebillrowid | int8 | 64 |  | √ | 0 |  |
| 44 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 45 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 46 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 47 | fplanstatus | fplanstatus | bpchar | 1 |  | √ | ' ' |  |
| 48 | fsourcebillrow | fsourcebillrow | int4 | 32 |  | √ | 0 |  |
| 49 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 50 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 51 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 53 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_pplan_wid |  | fworkid |
| 2 | pk_t_sfc_processplan |  | fid |

---

## 工序计划F7-分表 t_sfc_processplan_s

- **表名称：** 工序计划F7-分表
- **表名：** t_sfc_processplan_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | fprocesssequence | int4 | 32 |  | √ | 0 |  |
| 3 | fendprocessnumber | fendprocessnumber | int4 | 32 |  | √ | 0 |  |
| 4 | fsrcprocessplanid | 来源工序计划 | int8 | 64 |  | √ | 0 | [工序计划 sfc_bd_processplan](../sfc_files/sfc_bd_processplan.md) |
| 5 | fsplittype | fsplittype | bpchar | 1 |  | √ | ' ' |  |
| 6 | fstartprocessnumber | fstartprocessnumber | int4 | 32 |  | √ | 0 |  |
| 7 | fbillsn | fbillsn | int4 | 32 |  | √ | 0 |  |
| 8 | fcount | fcount | int4 | 32 |  | √ | 0 |  |
| 9 | frootprocessplanid | 主工序计划 | int8 | 64 |  | √ | 0 | [工序计划 sfc_bd_processplan](../sfc_files/sfc_bd_processplan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procplan_srcid |  | fsrcprocessplanid |
| 2 | pk_sfc_processplan_s |  | fid |
| 3 | idx_sfc_procplan_rootid |  | frootprocessplanid |
| 4 | idx_sfc_procplan_sspinfo |  | fsplittype,fprocesssequence,fstartprocessnumber,fendprocessnumber |
