# 计划编制-psw_masterschedule

## 产能分配清单-子表 t_psw_capacityallocbill

- **表名称：** 产能分配清单-子表
- **表名：** t_psw_capacityallocbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 3 | fmatenablelot | 启用批号 | bpchar | 1 |  | √ | '0' | 启用批号 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fstartdatetime | 起始日期时间 | timestamp | 0 |  |  | null | 起始日期时间 |
| 6 | fenddatetime | 截止日期时间 | timestamp | 0 |  |  | null | 截止日期时间 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fauxiliaryproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | ftotalqtytostart | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_capacityallocbill |  | fproductionlineid,fentryid |
| 2 | pk_t_psw_capacityallocbill |  | fentryid |

---

## 订单信息-子表 t_psw_orderinfo

- **表名称：** 订单信息-子表
- **表名：** t_psw_orderinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqtytocomplete | 预计完工数量 | numeric | 23 | 10 | √ | 0 | 预计完工数量 |
| 2 | fordermatenablelot | 启用批号 | bpchar | 1 |  | √ | '0' | 启用批号 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | fordermatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 5 | fqtyreported | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 6 | fsourceid | 来源工单 | int8 | 64 |  | √ | 0 | 来源工单 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | forderversion | 工单版本 | int4 | 32 |  | √ | 0 | 工单版本 |
| 10 | fneeddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 11 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 12 | frowstatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: C :Creating U :Updating |
| 13 | forderstatus | 订单状态 | varchar | 50 |  | √ | ' ' | 订单状态,枚举: P :计划 F :计划确认 E :锁定 R :下达 C :关闭 |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 15 | fordermaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fsrcbillentity | 来源实体 | varchar | 50 |  | √ | ' ' | 来源实体 |
| 19 | fqtytoscrap | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 20 | freleasedatetime | 计划开工 | timestamp | 0 |  |  | null | 计划开工 |
| 21 | fsourcebillno | 上游sourcebillno | varchar | 50 |  | √ | ' ' | 上游sourcebillno |
| 22 | fduedatetime | 计划完工 | timestamp | 0 |  |  | null | 计划完工 |
| 23 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 25 | fsourcebilltype | 上游sourcebilltype | varchar | 50 |  | √ | ' ' | 上游sourcebilltype |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fordernumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 28 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fqtycompleted | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 30 | fqtyscrapped | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 31 | fyieldpercent | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 32 | fproductionseq | 生产顺序 | numeric | 23 | 10 | √ | 0 | 生产顺序 |
| 33 | fqtytostart | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fordermatauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 36 | fsrcbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_orderinfo |  | fordernumber,fordermaterialid,fdetailid |
| 2 | pk_t_psw_orderinfo |  | fdetailid |

---

## deletedorder-子表 t_psw_deletedorder

- **表名称：** deletedorder-子表
- **表名：** t_psw_deletedorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeletedorderid | 删除工单id | int8 | 64 |  | √ | 0 | 删除工单id |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdeletedorderversion | 删除工单版本 | int4 | 32 |  | √ | 0 | 删除工单版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_deletedorder |  | fdeletedorderid,fentryid |
| 2 | pk_t_psw_deletedorder |  | fentryid |

---

## 计划编制-主表 t_psw_masterschedule

- **表名称：** 计划编制-主表
- **表名：** t_psw_masterschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fhidenonworkday | 仅显示工作日 | bpchar | 1 |  | √ | ' ' | 仅显示工作日 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialinfoconfig | fmaterialinfoconfig | varchar | 50 |  | √ | ' ' |  |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_masterschedule |  | fid |
| 2 | idx_t_psw_masterschedule |  | fbillno,fid |
