# 工序计划F7-sfc_processplan_f7

## 工序计划F7-主表 t_sfc_processplan

- **表名称：** 工序计划F7-主表
- **表名：** t_sfc_processplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrout | fprocessrout | int8 | 64 |  | √ | 0 |  |
| 3 | fworkentryf7 | fworkentryf7 | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsbillentity | fsbillentity | varchar | 50 |  | √ | ' ' |  |
| 6 | fworkshop | 生产车间(作废) | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 7 | fauxptyunit | fauxptyunit | int8 | 64 |  | √ | 0 |  |
| 8 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | fbaseunit | fbaseunit | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fworkid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 13 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fprojno | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fworkrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 17 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 18 | fworkn | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 19 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 20 | fsourcebillrowid | fsourcebillrowid | int8 | 64 |  | √ | 0 |  |
| 21 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 22 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 23 | fsourcebillno | fsourcebillno | varchar | 80 |  | √ | ' ' |  |
| 24 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 25 | fqty | fqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 27 | fsourcebilltype | fsourcebilltype | int8 | 64 |  | √ | 0 |  |
| 28 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 30 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 33 | fworkrown | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |
| 34 | fsourcebillrow | fsourcebillrow | int4 | 32 |  | √ | 0 |  |
| 35 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 36 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 38 | funit | 单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 39 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |
| 40 | fauxptyqty | fauxptyqty | numeric | 23 | 10 | √ | 0 |  |

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
| 4 | fsrcprocessplanid | 来源工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_bd_processplan |
| 5 | fsplittype | fsplittype | bpchar | 1 |  | √ | ' ' |  |
| 6 | fstartprocessnumber | fstartprocessnumber | int4 | 32 |  | √ | 0 |  |
| 7 | fbillsn | fbillsn | int4 | 32 |  | √ | 0 |  |
| 8 | fcount | fcount | int4 | 32 |  | √ | 0 |  |
| 9 | frootprocessplanid | 主工序计划 | int8 | 64 |  | √ | 0 | 工序计划 sfc_bd_processplan |

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
