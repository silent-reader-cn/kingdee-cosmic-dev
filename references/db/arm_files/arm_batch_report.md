# 重复生产批量汇报-arm_batch_report

## 汇报明细-子表 t_arm_batch_qtyreport

- **表名称：** 汇报明细-子表
- **表名：** t_arm_batch_qtyreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freportbillno | 汇报记录编号 | varchar | 30 |  | √ | ' ' | 汇报记录编号 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fshiftentryid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fisrework | 是否返工 | bpchar | 1 |  | √ | '0' | 是否返工 |
| 9 | fmaterialnoid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 10 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 11 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fbackflushid | 交互式倒冲 | int8 | 64 |  | √ | 0 | 交互式倒冲 |
| 13 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fprdbillno | 工单编号 | varchar | 50 |  | √ | ' ' | 工单编号 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fauxptyaffectplan | 辅助属性影响计划 | bpchar | 1 |  | √ | '0' | 辅助属性影响计划 |
| 18 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 19 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 20 | freportdescription | 汇报描述 | varchar | 255 |  | √ | ' ' | 汇报描述 |
| 21 | finvmaterialid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 22 | fwarehouseid | 完工入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | freportdescription_tag | 汇报描述_详情 | text | 0 |  |  | null | 汇报描述_详情 |
| 24 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 25 | flocationid | 完工入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 26 | freportstatus | 汇报状态 | varchar | 50 |  | √ | ' ' | 汇报状态,枚举: S :汇报成功 T :汇报成功 F :汇报失败 |
| 27 | fuaiqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 28 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 29 | fscrapreasonid | 报废原因 | int8 | 64 |  | √ | 0 | [原因代码 arm_screason](../arm_files/arm_screason.md) |
| 30 | fisvalid | 有效位 | bpchar | 1 |  | √ | '1' | 有效位 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fischeck | 是否质检 | bpchar | 1 |  | √ | '0' | 是否质检 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_batch_qtyreport |  | fentryid |
| 2 | idx_arm_batch_qtyreport_fk |  | fid |

---

## 重复生产批量汇报-主表 t_arm_batch_report

- **表名称：** 重复生产批量汇报-主表
- **表名：** t_arm_batch_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbosusersid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbiztime | 汇报日期 | timestamp | 0 |  |  | null | 汇报日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 12 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | freportmode | 汇报方式 | varchar | 50 |  | √ | ' ' | 汇报方式,枚举: D :按日汇报 S :按班次汇报 |
| 15 | fbatchreportstatus | 汇报结果 | bpchar | 1 |  | √ | ' ' | 汇报结果,枚举: N :未汇报 S :汇报成功 F :汇报失败 |
| 16 | fteamgroupid | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 17 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_batch_report_m0 |  | fbillno |
| 2 | pk_arm_batch_report |  | fid |

---

## 工时汇报明细-子表 t_arm_batch_whreport

- **表名称：** 工时汇报明细-子表
- **表名：** t_arm_batch_whreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmachpreptimeentry | 机器准备工时 | numeric | 23 | 2 | √ | 0 | 机器准备工时 |
| 2 | fstartdatetimeentry | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | frealprodtimeentry | 实际生产总工时 | numeric | 23 | 2 | √ | 0 | 实际生产总工时 |
| 4 | fmachrealtimeentry | 机器实作工时 | numeric | 23 | 2 | √ | 0 | 机器实作工时 |
| 5 | fbosusersentryid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fisusestdtime | 使用标准准备工时 | bpchar | 1 |  | √ | '0' | 使用标准准备工时 |
| 8 | fteamgroupentryid | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 9 | fpretimeunitentry | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 10 | fmanurealtimeentry | 人工实作工时 | numeric | 23 | 2 | √ | 0 | 人工实作工时 |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fenddatetimeentry | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fmanupreptimeentry | 人工准备工时 | numeric | 23 | 2 | √ | 0 | 人工准备工时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_batch_whreport |  | fdetailid |
| 2 | idx_arm_batch_whreport_fk |  | fentryid |
