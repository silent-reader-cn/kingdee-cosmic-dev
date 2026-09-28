# 销售计划单下推记录-ids_salesplan_push_his

## 销售计划单下推记录-主表 t_ids_salesplan_push_his

- **表名称：** 销售计划单下推记录-主表
- **表名：** t_ids_salesplan_push_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsalesplanid | 销售计划单 | int8 | 64 |  | √ | 0 | 销售计划单 ids_salesplan |
| 3 | fperiodid | 销售计划周期 | int8 | 64 |  | √ | 0 | [销售计划周期 ids_salesplan_period](../ids_files/ids_salesplan_period.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | frequireplanid | 需求计划单 | int8 | 64 |  | √ | 0 | 需求计划单 ids_requireplan |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_salesplan_push_p |  | fperiodid |
| 2 | pk_t_ids_salesplan_push_his |  | fid |
| 3 | idx_ids_salesplan_push_s |  | fsalesplanid |
| 4 | idx_ids_salesplan_push_r |  | frequireplanid |
