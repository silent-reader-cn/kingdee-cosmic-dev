# 计划产量归集-cad_plannedoutputbill

## 计划产量归集-主表 t_cad_plannedoutputbill

- **表名称：** 计划产量归集-主表
- **表名：** t_cad_plannedoutputbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fclosedatetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fclosestyle | 关闭方式 | varchar | 30 |  | √ | ' ' | 关闭方式,枚举: 0 :自动关闭 1 :手工关闭 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | ffromlogid | 来源日志id | int8 | 64 |  | √ | 0 | 来源日志id |
| 8 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fsource | 来源 | varchar | 30 |  | √ | '0' | 来源,枚举: 0 :手工录入 1 :模板引入 2 :API引入 3 :生产工单引入 4 :委外工单引入 5 :完工产量归集单引入 6 :生产工单变更单 7 :生产工单拆分单 8 :委外工单变更单 9 :委外工单拆分单 10 :按配置方案引入 |
| 11 | ftotalinqty | 累计完工入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 累计完工入库数量 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fclosestatu | 关闭状态 | bpchar | 1 |  | √ | '0' | 关闭状态 |
| 15 | fismodifybizdate | 是否修改业务日期 | bpchar | 1 |  | √ | '0' | 是否修改业务日期 |
| 16 | fbillno | 单据编号 | varchar | 225 |  | √ | ' ' | 单据编号 |
| 17 | fsrctransmittime | 源单投产日期 | timestamp | 0 |  |  | null | 源单投产日期 |
| 18 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fsourcebillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fcloseuserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fplanneddate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 27 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fwipqty | 在产品数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在产品数量 |
| 29 | fsourcebillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 30 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | 成本归集配置单 cad_costcollectconfig |
| 31 | faccountorgid | 核算组织(废弃-230629多核算体系改造) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsourcebiztime | 来源单据业务日期 | timestamp | 0 |  |  | null | 来源单据业务日期 |
| 33 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 34 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
