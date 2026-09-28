# 重复生产日程-arm_productschedule

## 重复生产日程-主表 t_arm_prdshedule

- **表名称：** 重复生产日程-主表
- **表名：** t_arm_prdshedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | forg | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fprdmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 14 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 3 | fmaterialno | 隐藏物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | fduetime | 计划完工时间 | int8 | 64 |  | √ | 0 | 计划完工时间 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fstarttime | 计划开工时间 | int8 | 64 |  | √ | 0 | 计划开工时间 |
| 7 | fduedate | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 8 | fyieldpercent | 成品率 | numeric | 23 | 10 | √ | 0 | 成品率 |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 10 | fstartdate | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 11 | fqtytostart | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fstartdatetime | 计划开工长日期 | timestamp | 0 |  |  | null | 计划开工长日期 |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 14 | fleadtime | 提前期 | int8 | 64 |  | √ | 0 | 提前期 |
| 15 | fprdbillno | 生产工单 | varchar | 30 |  | √ | ' ' | 生产工单 |
| 16 | fqtytoscrap | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fduedatetime | 计划完工长日期 | timestamp | 0 |  |  | null | 计划完工长日期 |
| 20 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_psdlen |  | fid |
| 2 | pk_t_arm_prdscheduleentry |  | fentryid |
