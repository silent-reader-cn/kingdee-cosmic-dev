# 计划订单投放日志-mrp_dropplanorderlog

## 计划订单投放日志-主表 t_mrp_dropplanorderlog

- **表名称：** 计划订单投放日志-主表
- **表名：** t_mrp_dropplanorderlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdropqty | 本次投放数量 | numeric | 23 | 10 | √ | 0 | 本次投放数量 |
| 3 | fplanorderid | 计划建议id | int8 | 64 |  | √ | 0 | 计划建议id |
| 4 | ftargetorderid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 5 | fdropstatus | 投放状态 | varchar | 30 |  | √ | ' ' | 投放状态,枚举: A :未投放 B :投放中 C :取消投放 D :投放成功 E :投放失败 |
| 6 | foperator | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftargetorderbillno | 目标单编号 | varchar | 100 |  | √ | ' ' | 目标单编号 |
| 8 | fsoureorder | 来源单类型 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fbillno | 计划订单编码 | varchar | 50 |  | √ | ' ' | 计划订单编码 |
| 10 | foperationdate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 11 | ftargetorder | 目标单类型 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_dropplanorderlog |  | ftargetorderid |
| 2 | pk_t_mrp_dropplanorderlog |  | fid |
