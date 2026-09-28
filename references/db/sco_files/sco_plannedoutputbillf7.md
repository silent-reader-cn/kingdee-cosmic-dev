# 计划生产数量归集f7-sco_plannedoutputbillf7

## 计划生产数量归集f7-主表 t_sco_plannedoutputbill

- **表名称：** 计划生产数量归集f7-主表
- **表名：** t_sco_plannedoutputbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | fmanuorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fclosedatetime | fclosedatetime | timestamp | 0 |  |  | null |  |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fclosestyle | fclosestyle | varchar | 30 |  | √ | ' ' |  |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | ffromlogid | ffromlogid | int8 | 64 |  | √ | 0 |  |
| 8 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fsource | fsource | varchar | 30 |  | √ | '0' |  |
| 12 | ftotalinqty | 累计完工入库数量 | numeric | 23 | 10 | √ | 0 | 累计完工入库数量 |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fclosestatu | 关闭状态 | bpchar | 1 |  | √ | '0' | 关闭状态 |
| 16 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 17 | flot | flot | varchar | 255 |  | √ | ' ' |  |
| 18 | fismodifybizdate | fismodifybizdate | bpchar | 1 |  | √ | ' ' |  |
| 19 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 20 | fsrctransmittime | fsrctransmittime | timestamp | 0 |  |  | null |  |
| 21 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 22 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 23 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 24 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 25 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 26 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :创建 B :审核中 C :已审核 |
| 27 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 28 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 29 | fcloseuserid | fcloseuserid | int8 | 64 |  | √ | 0 |  |
| 30 | fplanneddate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 31 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 32 | fwipqty | 在产品数量 | numeric | 23 | 10 | √ | 0 | 在产品数量 |
| 33 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 34 | fcollconfigid | fcollconfigid | int8 | 64 |  | √ | 0 |  |
| 35 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fsourcebiztime | fsourcebiztime | timestamp | 0 |  |  | null |  |
| 37 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 38 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 39 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fappnum |
| 2 | fappnum | fid,fappnum |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_plannedoutputbill2 |  | faccountorgid,fcostobjectid |
| 2 | pk_sco_plannedoutputbill |  | fid,fappnum |
| 3 | idx_sco_planoutputbill_df |  | fcostcenterid,fmaterialid,fcostobjectid,fappnum |
