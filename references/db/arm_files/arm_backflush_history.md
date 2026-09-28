# 倒冲历史-arm_backflush_history

## 倒冲历史-主表 t_arm_backflush_history

- **表名称：** 倒冲历史-主表
- **表名：** t_arm_backflush_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freportbill | 重复生产汇报 | int8 | 64 |  | √ | 0 | 重复生产汇报平台 arm_report_workbanch |
| 3 | fcomponent | 子项编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | freturnqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 5 | fduetime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 6 | forderlineid | 工单用料行id | int8 | 64 |  | √ | 0 | 工单用料行id |
| 7 | fcompmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fcompunit | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fproductionorder | 重复生产工单 | int8 | 64 |  | √ | 0 | 重复生产工单 arm_productionorder |
| 10 | fbackflushentryid | 倒冲总览id | int8 | 64 |  | √ | 0 | 倒冲总览id |
| 11 | fbackflushqty | 倒冲数量 | numeric | 23 | 10 | √ | 0 | 倒冲数量 |
| 12 | fcompauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_backflush_his |  | freportbill,fproductionorder,forderlineid |
| 2 | pk_t_arm_backflush_history |  | fid |
