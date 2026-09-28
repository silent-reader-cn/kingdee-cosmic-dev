# 重复生产汇报平台-arm_report_workbanch

## 领料记录-子表 t_arm_pickoutentry

- **表名称：** 领料记录-子表
- **表名：** t_arm_pickoutentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foutbillno | 领料单单据编号 | varchar | 30 |  | √ | ' ' | 领料单单据编号 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_pickoutentry |  | fentryid |
| 2 | idx_arm_pickoutentry_fk |  | fid |

---

## 工时明细-子表 t_arm_batchworkoursreport

- **表名称：** 工时明细-子表
- **表名：** t_arm_batchworkoursreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmachpreptimeentry | 机器准备工时 | numeric | 23 | 10 | √ | 0 | 机器准备工时 |
| 3 | fstartdatetimeentry | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 4 | frealprodtimeentry | 实际生产总工时 | numeric | 23 | 10 | √ | 0 | 实际生产总工时 |
| 5 | fteamgroupentry | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 6 | fmachrealtimeentry | 机器实作工时 | numeric | 23 | 10 | √ | 0 | 机器实作工时 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmanurealtimeentry | 人工实作工时 | numeric | 23 | 2 | √ | 0 | 人工实作工时 |
| 9 | faddall |  | varchar | 50 |  | √ | ' ' |  |
| 10 | fisnewadd | 是否新增行 | int8 | 64 |  | √ | 0 | 是否新增行 |
| 11 | frealtimeunitentry | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 12 | fenddatetimeentry | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fmanupreptimeentry | 人工准备工时 | numeric | 23 | 10 | √ | 0 | 人工准备工时 |
| 15 | fbosusersentry | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_batchworkoursreport |  | fentryid |
| 2 | idx_arm_batchworkoursreport_fk |  | fid |

---

## 重复生产汇报平台-关联追踪表 t_arm_report_workbanch_tc

- **表名称：** 重复生产汇报平台-关联追踪表
- **表名：** t_arm_report_workbanch_tc

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
| 1 | pk_arm_report_workbanch_tc |  | fid |
| 2 | idx_arm_report_workbanch_tc_tbill |  | ftbillid |
| 3 | idx_arm_report_workbanch_tc_tid |  | ftid |

---

## 汇报条码单据体-子表 t_arm_barcodeentry

- **表名称：** 汇报条码单据体-子表
- **表名：** t_arm_barcodeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryreportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 3 | fentrybaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fjoinstockdamagebaseqty | 关联入库采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗基本数量 |
| 5 | fentryauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbasematerial | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | finvmaterial | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 9 | fmaterialno1 | fmaterialno1 | int8 | 64 |  | √ | 0 |  |
| 10 | fentrymaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 11 | fmftmaterial | 物料生产信息 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fentrymftunit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_barcodeentry |  | fentryid |
| 2 | idx_arm_barcodeentry_fk |  | fid |

---

## 重复生产汇报平台-主表 t_arm_report_workbanch

- **表名称：** 重复生产汇报平台-主表
- **表名：** t_arm_report_workbanch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddatetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fpushcheckbillqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 4 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | flocation | 完工入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 6 | fpretimeunit | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | forg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fproductinvbillno | 重复生产完工入库单 | varchar | 50 |  | √ | ' ' | 重复生产完工入库单 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fisrework | 是否返工 | bpchar | 1 |  | √ | '0' | 是否返工 |
| 12 | fisusestdtime | 使用标准准备工时 | bpchar | 1 |  | √ | '0' | 使用标准准备工时 |
| 13 | fdetail | fdetail | varchar | 50 |  | √ | ' ' |  |
| 14 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 15 | fcheckedqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 16 | fscrapreason | 报废原因 | int8 | 64 |  | √ | 0 | [原因代码 arm_screason](../arm_files/arm_screason.md) |
| 17 | fprdbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 18 | fsourcebillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fbaseunitreportqty | 汇报数量（基本） | numeric | 23 | 10 | √ | 0 | 汇报数量（基本） |
| 21 | fmanupreptime | 人工准备工时 | numeric | 23 | 2 | √ | 0 | 人工准备工时 |
| 22 | fmaterialno | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 23 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fteamgroup | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 26 | fprdqualifiedqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | fpushscrapinvqty | 关联报废品入库数量 | numeric | 23 | 10 | √ | 0 | 关联报废品入库数量 |
| 29 | fmachpreptime | 机器准备工时 | numeric | 23 | 2 | √ | 0 | 机器准备工时 |
| 30 | fwarehouse | 完工入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | frealtimeunit | 时间单位 | varchar | 50 |  |  | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 32 | fprdunit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fmanurealtime | 人工实作工时 | numeric | 23 | 2 | √ | 0 | 人工实作工时 |
| 34 | freportstatus | freportstatus | bpchar | 1 |  | √ | ' ' |  |
| 35 | frepairqty | 返修数量 | numeric | 23 | 10 | √ | 0 | 返修数量 |
| 36 | fstartdatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 37 | fworkhoursreportbillno | 工时汇报单 | varchar | 50 |  | √ | ' ' | 工时汇报单 |
| 38 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 39 | fmachrealtime | 机器实作工时 | numeric | 23 | 2 | √ | 0 | 机器实作工时 |
| 40 | fbookdate | 记账日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 记账日期 |
| 41 | fpushdownwareprdqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 42 | frealprodtime | 实际生产总工时 | numeric | 23 | 2 | √ | 0 | 实际生产总工时 |
| 43 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 44 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 45 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 46 | fprdunqualifiedqty | 不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库数量 |
| 47 | fbosusers | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fprdscrapqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 49 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 50 | fpushqualiinvqty | 关联合格品入库数量 | numeric | 23 | 10 | √ | 0 | 关联合格品入库数量 |
| 51 | fbiztime | 业务日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 业务日期 |
| 52 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fpushnoqualiinvqty | 关联不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 关联不合格品入库数量 |
| 54 | fbackflushid | 交互式倒冲 | int8 | 64 |  | √ | 0 | 交互式倒冲 |
| 55 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 56 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 57 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 58 | fpickoutbillno | 重复生产领料单 | varchar | 50 |  | √ | ' ' | 重复生产领料单 |
| 59 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 60 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 61 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 62 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 63 | fuaiqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 64 | fisvalid | 有效位 | bpchar | 1 |  | √ | '1' | 有效位 |
| 65 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 66 | fischeck | 是否质检 | bpchar | 1 |  | √ | '0' | 是否质检 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_report_wb |  | fmaterialno,fmaterialversion,fauxpty |
| 2 | pk_t_arm_report_workbanch |  | fid |

---

## 入库记录-子表 t_arm_prdinvordernoentry

- **表名称：** 入库记录-子表
- **表名：** t_arm_prdinvordernoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvbillno | 入库单单据编号 | varchar | 50 |  | √ | ' ' | 入库单单据编号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_prdinvordernoentry_fk |  | fid |
| 2 | pk_arm_prdinvordernoentry |  | fentryid |

---

## 关联子实体-子表 t_arm_report_workbanch_lk

- **表名称：** 关联子实体-子表
- **表名：** t_arm_report_workbanch_lk

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
| 1 | pk_arm_report_workbanch_lk |  | fpkid |
| 2 | idx_arm_report_workbanch_lk_fk |  | fid |

---

## 重复生产汇报平台-反写记录表 t_arm_report_workbanch_wb

- **表名称：** 重复生产汇报平台-反写记录表
- **表名：** t_arm_report_workbanch_wb

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
| 1 | idx_arm_report_workbanch_wb_fk |  | fid |
| 2 | pk_arm_report_workbanch_wb |  | fentryid |

---

## 报废明细-子表 t_arm_scrapreportentry

- **表名称：** 报废明细-子表
- **表名：** t_arm_scrapreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffentryscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 3 | fscrapdescription | fscrapdescription | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryscrapreason | 报废原因 | int8 | 64 |  | √ | 0 | [原因代码 arm_screason](../arm_files/arm_screason.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmftunit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fid_entryid |  | fid,fentryid |
| 2 | pk_t_arm_scrapreportentry |  | fentryid |
