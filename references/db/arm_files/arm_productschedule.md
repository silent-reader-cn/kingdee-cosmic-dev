# 重复生产日程-arm_productschedule

## 重复生产日程-主表 t_arm_prdshedule

- **表名称：** 重复生产日程-主表
- **表名：** t_arm_prdshedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | forg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fprdmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 14 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_prdshedule |  | fid |
| 2 | idx_t_arm_pscdl_no |  | fbillno |

---

## 单据体-子表 t_arm_prdscheduleentry

- **表名称：** 单据体-子表
- **表名：** t_arm_prdscheduleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqtytocomplete | 预计完工数量 | numeric | 23 | 10 | √ | 0 | 预计完工数量 |
| 3 | fmaterialno | 隐藏物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 5 | fduetime | 计划完工时间 | int8 | 64 |  | √ | 0 | 计划完工时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fstarttime | 计划开工时间 | int8 | 64 |  | √ | 0 | 计划开工时间 |
| 8 | fduedate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 9 | fyieldpercent | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 10 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 11 | fstartdate | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 12 | fqtytostart | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 13 | fstartdatetime | 计划开工长日期 | timestamp | 0 |  |  | null | 计划开工长日期 |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fleadtime | 提前期 | int8 | 64 |  | √ | 0 | 提前期 |
| 16 | fprdbillno | 生产工单 | varchar | 30 |  | √ | ' ' | 生产工单 |
| 17 | fqtytoscrap | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | fduedatetime | 计划完工长日期 | timestamp | 0 |  |  | null | 计划完工长日期 |
| 21 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_psdlen |  | fid |
| 2 | pk_t_arm_prdscheduleentry |  | fentryid |
