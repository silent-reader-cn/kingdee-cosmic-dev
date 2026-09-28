# 重复生产工时汇报单-arm_workhoursreport

## 重复生产工时汇报单-主表 t_arm_workhoursreport

- **表名称：** 重复生产工时汇报单-主表
- **表名：** t_arm_workhoursreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fpersonnelrep | 人员 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 7 | forgid | 生产组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fteamsgroupsrep | 班组 | int8 | 64 |  |  | null | 班组 mpdm_classgroup |
| 10 | fbiztime | 业务日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 业务日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fproductionlineid | 生产线 | int8 | 64 |  |  | null | 生产线 arm_linecapacity |
| 13 | fworkshopid | 车间 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 14 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | 物料版本 bd_bomversion_new |
| 17 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fauxpty | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_workhoursreport |  | fid |
| 2 | idx_t_arm_workhoursreport |  | fbillno |

---

## 重复生产工时汇报单-反写记录表 t_arm_workhoursreport_wb

- **表名称：** 重复生产工时汇报单-反写记录表
- **表名：** t_arm_workhoursreport_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_workhoursreport_wb |  | fentryid |
| 2 | idx_arm_workhoursreport_wb_fk |  | fid |

---

## 重复生产工时汇报单-关联追踪表 t_arm_workhoursreport_tc

- **表名称：** 重复生产工时汇报单-关联追踪表
- **表名：** t_arm_workhoursreport_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_workhoursreport_tc_tbill |  | ftbillid |
| 2 | pk_arm_workhoursreport_tc |  | fid |
| 3 | idx_arm_workhoursreport_tc_tid |  | ftid |

---

## 关联子实体-子表 t_arm_workhoursreport_lk

- **表名称：** 关联子实体-子表
- **表名：** t_arm_workhoursreport_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_workhoursreport_lk_fk |  | fid |
| 2 | pk_arm_workhoursreport_lk |  | fpkid |

---

## 单据体-子表 t_arm_workhoursrptentry

- **表名称：** 单据体-子表
- **表名：** t_arm_workhoursrptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstoptimerep | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 4 | ftimeunitrep | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmachprehoursrep | 机器准备工时 | numeric | 23 | 2 |  | null | 机器准备工时 |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 8 | facttotprohoursrep | 实际生产总工时 | numeric | 23 | 2 |  | null | 实际生产总工时 |
| 9 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | flabworkhoursrep | 人工实作工时 | numeric | 23 | 2 |  | null | 人工实作工时 |
| 11 | ftimeonrep | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fmacworhoursrep | 机器实作工时 | numeric | 23 | 2 |  | null | 机器实作工时 |
| 13 | flabworprehoursrep | 人工准备工时 | numeric | 23 | 2 |  | null | 人工准备工时 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_workhoursrptentry |  | fid,fseq |
| 2 | pk_t_arm_workhoursrptentry |  | fentryid |
