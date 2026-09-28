# 计划生产数量归集f7-cad_plannedoutputbillf7

## 计划生产数量归集f7-主表 t_cad_plannedoutputbill

- **表名称：** 计划生产数量归集f7-主表
- **表名：** t_cad_plannedoutputbill

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
| 8 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fsource | fsource | varchar | 30 |  | √ | '0' |  |
| 11 | ftotalinqty | 累计完工入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计完工入库数量 |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 14 | fclosestatu | 关闭状态 | bpchar | 1 |  | √ | '0' | 关闭状态 |
| 15 | fismodifybizdate | fismodifybizdate | bpchar | 1 |  | √ | '0' |  |
| 16 | fbillno | 单据编号 | varchar | 225 |  | √ | ' ' | 单据编号 |
| 17 | fsrctransmittime | fsrctransmittime | timestamp | 0 |  |  | null |  |
| 18 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 19 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 20 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 21 | fsourcebillentryid | fsourcebillentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :创建 B :审核中 C :已审核 |
| 23 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | fcloseuserid | fcloseuserid | int8 | 64 |  | √ | 0 |  |
| 26 | fplanneddate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fwipqty | 在产品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在产品数量 |
| 29 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 30 | fcollconfigid | fcollconfigid | int8 | 64 |  | √ | 0 |  |
| 31 | faccountorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fsourcebiztime | fsourcebiztime | timestamp | 0 |  |  | null |  |
| 33 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象 cad_costobjectf7](../aca_files/cad_costobjectf7.md) |
| 34 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 35 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid,fappnum |
| 2 | fappnum | fid,fappnum |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_plannedoutputbill_pkey |  | fid,fappnum |
| 2 | idx_cad_plannedoutputbill2 |  | faccountorgid,fcostobjectid |
| 3 | idx_plan_costobj |  | fcostobjectid |
| 4 | idx_cad_planoutputbill_df |  | fcostcenterid,fmaterialid,fcostobjectid,fappnum |
| 5 | idx_plan_mat |  | fmaterialid |
