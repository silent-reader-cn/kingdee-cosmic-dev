# 重复生产工时汇报单-arm_workhoursreport

## 重复生产工时汇报单-主表 t_arm_workhoursreport

- **表名称：** 重复生产工时汇报单-主表
- **表名：** t_arm_workhoursreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpersonnelrep | 汇报人员 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 8 | forgid | 生产组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fteamsgroupsrep | 班组 | int8 | 64 |  |  | null | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 11 | fbiztime | 业务日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 业务日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fproductionlineid | 生产线 | int8 | 64 |  |  | null | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 14 | fworkshopid | 车间 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 18 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 19 | fauxpty | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 23 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |

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
| 3 | fstatotprohoursrep | 标准生产总工时 | numeric | 23 | 10 | √ | 0 | 标准生产总工时 |
| 4 | fbosuser | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 6 | fteamgroup | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 7 | fstalabworprehours | 标准人工准备工时 | numeric | 23 | 10 | √ | 0 | 标准人工准备工时 |
| 8 | ftimeunitrep | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fmachprehoursrep | 机器准备工时 | numeric | 23 | 2 |  | null | 机器准备工时 |
| 11 | fstandworkhoursrep | fstandworkhoursrep | numeric | 23 | 10 | √ | 0 |  |
| 12 | fstalabworkhours | 标准人工实作工时 | numeric | 23 | 10 | √ | 0 | 标准人工实作工时 |
| 13 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | facttotprohoursrep | 实际生产总工时 | numeric | 23 | 2 |  | null | 实际生产总工时 |
| 15 | flblrptqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 16 | fstandworprehoursrep | fstandworprehoursrep | numeric | 23 | 10 | √ | 0 |  |
| 17 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fstamacworhours | 标准机器实作工时 | numeric | 23 | 10 | √ | 0 | 标准机器实作工时 |
| 19 | flabworkhoursrep | 人工实作工时 | numeric | 23 | 2 |  | null | 人工实作工时 |
| 20 | fstamacprehours | 标准机器准备工时 | numeric | 23 | 10 | √ | 0 | 标准机器准备工时 |
| 21 | ftimeonrep | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 22 | fmacworhoursrep | 机器实作工时 | numeric | 23 | 2 |  | null | 机器实作工时 |
| 23 | flabworprehoursrep | 人工准备工时 | numeric | 23 | 2 |  | null | 人工准备工时 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_workhoursrptentry |  | fid,fseq |
| 2 | pk_t_arm_workhoursrptentry |  | fentryid |
