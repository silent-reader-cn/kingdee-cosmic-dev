# 冲减记录-msplan_writedownrecord

## 冲减记录-主表 t_msplan_writedownrecord

- **表名称：** 冲减记录-主表
- **表名：** t_msplan_writedownrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwdbillobj | 冲减单据 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fwdbillid | 冲减单单据内码 | int8 | 64 |  | √ | 0 | 冲减单单据内码 |
| 4 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 6 | fwdbillentryid | 冲减单分录内码 | int8 | 64 |  | √ | 0 | 冲减单分录内码 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | ftracknumid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 11 | fmodifierfield | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fwdbillno | 冲减单单据编码 | varchar | 80 |  | √ | ' ' | 冲减单单据编码 |
| 13 | fbaseorderqty | 订单确认数量 | numeric | 23 | 10 | √ | 0 | 订单确认数量 |
| 14 | fmodifydatefield | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 15 | fdemandbillno | 需求单据编号 | varchar | 80 |  | √ | ' ' | 需求单据编号 |
| 16 | fbaseremainqty | 剩余需求数量 | numeric | 23 | 10 | √ | 0 | 剩余需求数量 |
| 17 | fdemandbillobj | 需求单据 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | fwdbillseq | 冲减单行号 | int8 | 64 |  | √ | 0 | 冲减单行号 |
| 19 | fdisablestatus | 禁用状态 | bpchar | 1 |  | √ | '0' | 禁用状态,枚举: 0 :启用 1 :禁用 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fbasewdqty | 冲减数量 | numeric | 23 | 10 | √ | 0 | 冲减数量 |
| 22 | fbaseqty | 业务数量 | numeric | 23 | 10 | √ | 0 | 业务数量 |
| 23 | fdemandbillid | 需求单据内码 | int8 | 64 |  | √ | 0 | 需求单据内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_wdrecord_demandid |  | fdemandbillid |
| 2 | idx_msplan_wdrecord_wdeid |  | fwdbillentryid |
| 3 | pk_t_msplan_writedownrecord |  | fid |
