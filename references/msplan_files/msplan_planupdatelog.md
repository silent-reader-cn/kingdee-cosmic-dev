# 计划订单修改日志-msplan_planupdatelog

## 计划订单修改日志-主表 t_msplan_planupdatelog

- **表名称：** 计划订单修改日志-主表
- **表名：** t_msplan_planupdatelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprevalue | 修改前 | varchar | 50 |  | √ | ' ' | 修改前 |
| 3 | fpropname | 修改字段 | varchar | 50 |  | √ | ' ' | 修改字段 |
| 4 | fplanorderentry | 计划订单分录标识 | varchar | 50 |  | √ | ' ' | 计划订单分录标识 |
| 5 | fopdesc | 操作描述 | varchar | 50 |  | √ | ' ' | 操作描述 |
| 6 | fplanorderentryno | 计划订单分录行号 | varchar | 50 |  | √ | ' ' | 计划订单分录行号 |
| 7 | fopdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | fusername | 操作人 | varchar | 50 |  | √ | ' ' | 操作人 |
| 9 | fopname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 10 | fnextvalue | 修改后 | varchar | 50 |  | √ | ' ' | 修改后 |
| 11 | fplanorderbillno | 计划建议编码 | varchar | 50 |  | √ | ' ' | 计划建议编码 |
| 12 | fplanorderentryid | 计划订单分录id | int8 | 64 |  | √ | 0 | 计划订单分录id |
| 13 | fplanorderid | 计划订单id | int8 | 64 |  | √ | 0 | 计划订单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_planupdatelog |  | fusername,fplanorderbillno |
| 2 | pk_t_msplan_planupdatelog |  | fid |
