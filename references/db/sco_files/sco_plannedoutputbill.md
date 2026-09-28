# 计划产量归集-sco_plannedoutputbill

## 计划产量归集-主表 t_sco_plannedoutputbill

- **表名称：** 计划产量归集-主表
- **表名：** t_sco_plannedoutputbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fclosedatetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fclosestyle | 关闭方式 | varchar | 30 |  | √ | ' ' | 关闭方式,枚举: 0 :自动关闭 1 :手工关闭 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | ffromlogid | 来源日志id | int8 | 64 |  | √ | 0 | 来源日志id |
| 8 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fsource | 来源 | varchar | 30 |  | √ | '0' | 来源,枚举: 0 :手工录入 1 :模板导入 2 :API导入 3 :生产工单导入 4 :委外工单导入 5 :完工产量归集单导入 6 :生产工单变更单 7 :生产工单拆分单 8 :委外工单变更单 9 :委外工单拆分单 10 :按配置方案导入 |
| 12 | ftotalinqty | 累计完工入库数量 | numeric | 23 | 10 | √ | 0 | 累计完工入库数量 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fclosestatu | 关闭状态 | bpchar | 1 |  | √ | '0' | 关闭状态 |
| 16 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 17 | flot | flot | varchar | 255 |  | √ | ' ' |  |
| 18 | fismodifybizdate | 是否修改业务日期 | bpchar | 1 |  | √ | ' ' | 是否修改业务日期 |
| 19 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 20 | fsrctransmittime | 源单投产日期 | timestamp | 0 |  |  | null | 源单投产日期 |
| 21 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 24 | fsourcebillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 25 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 26 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fcloseuserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fplanneddate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 31 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 32 | fwipqty | 在产品数量 | numeric | 23 | 10 | √ | 0 | 在产品数量 |
| 33 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 34 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | [成本归集配置单 cad_costcollectconfig](../aca_files/cad_costcollectconfig.md) |
| 35 | faccountorgid | 核算组织核算组织(废弃-240327多核算体系改造) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fsourcebiztime | 来源单据业务日期 | timestamp | 0 |  |  | null | 来源单据业务日期 |
| 37 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 38 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
