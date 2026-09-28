# 汇报倒冲明细-arm_backflushdetail

## 日程冲销-子表 t_arm_schedulewriteoff

- **表名称：** 日程冲销-子表
- **表名：** t_arm_schedulewriteoff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 工单数量 | numeric | 23 | 10 | √ | 0 | 工单数量 |
| 3 | forderunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 5 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 6 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 7 | forderid | 查看详情 | int8 | 64 |  | √ | 0 | 查看详情 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | funreportqty | 未汇报数量 | numeric | 23 | 10 | √ | 0 | 未汇报数量 |
| 10 | foperate | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 11 | fwriteoffqty | 冲销数量 | numeric | 23 | 10 | √ | 0 | 冲销数量 |
| 12 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 13 | forderstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: P :计划 F :计划确认 E :锁定 R :下达 C :关闭 |
| 14 | fstartdatetime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fduedatetime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_schedulewriteoff |  | fid |
| 2 | pk_t_arm_schedulewriteoff |  | fentryid |

---

## 汇报倒冲明细-主表 t_arm_interbackflush

- **表名称：** 汇报倒冲明细-主表
- **表名：** t_arm_interbackflush

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 3 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnotmatchqty | 多余数量 | numeric | 23 | 10 | √ | 0 | 多余数量 |
| 8 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 11 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 12 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fdetail | 详情 | varchar | 10 |  | √ | ' ' | 详情 |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | freportbillid | 汇报单 | int8 | 64 |  | √ | 0 | 重复生产汇报平台 arm_report_workbanch |
| 16 | fmastermaterial | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 17 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_interbackflush |  | fmaterialno,fmaterialversionid,fauxpty |
| 2 | pk_t_arm_interbackflush |  | fid |

---

## 倒冲明细-子表 t_arm_backflushdetail

- **表名称：** 倒冲明细-子表
- **表名：** t_arm_backflushdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 2 | fdetailmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcompdetailauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 7 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 8 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 9 | fisallowneginv | fisallowneginv | bpchar | 1 |  | √ | ' ' |  |
| 10 | fcompdetailunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | fdetailbackflushqty | 倒冲数量 | numeric | 23 | 10 | √ | 0 | 倒冲数量 |
| 13 | fmastermaterialid | 子项编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 15 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 16 | fdetailbackflushbaseqty | 倒冲基本数量 | numeric | 23 | 10 | √ | 0 | 倒冲基本数量 |
| 17 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 18 | fshortageqty | 短缺数量 | numeric | 23 | 10 | √ | 0 | 短缺数量 |
| 19 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 20 | fcompbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 22 | fcomponentdetailid | 子项编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 23 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 25 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_backflushdetail |  | fdetailid |
| 2 | idx_t_arm_backflushdetail |  | fentryid |

---

## 倒冲-子表 t_arm_backflush

- **表名称：** 倒冲-子表
- **表名：** t_arm_backflush

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flock | 是否锁定 | bpchar | 1 |  | √ | ' ' | 是否锁定,枚举: 0 :不锁定 1 :锁定 |
| 3 | fcompunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcompmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 7 | fnewline | 是否新增行 | bpchar | 1 |  | √ | ' ' | 是否新增行,枚举: 0 :0 1 :1 |
| 8 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 : 1 :不足 2 :超发 |
| 9 | fcomponentid | 子项编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 10 | fbackflushedqty | 应倒冲数量 | numeric | 23 | 10 | √ | 0 | 应倒冲数量 |
| 11 | fentrylisenceno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 12 | fmastermaterial | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | fbackflushqty | 倒冲数量 | numeric | 23 | 10 | √ | 0 | 倒冲数量 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fcompauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_backflush |  | fcomponentid,fcompmaterialversionid,fcompauxpty |
| 2 | pk_t_arm_backflush |  | fentryid |
