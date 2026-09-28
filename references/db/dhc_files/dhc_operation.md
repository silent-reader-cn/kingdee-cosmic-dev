# 单据操作-dhc_operation

## 单据操作-主表 t_dhc_operation

- **表名称：** 单据操作-主表
- **表名：** t_dhc_operation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbindbill | 接入单据 | int8 | 64 |  | √ | 0 | 接入单据 dhc_billaccessed |
| 3 | finnerid | 接入单据内码 | varchar | 50 |  | √ | ' ' | 接入单据内码 |
| 4 | foperationname | 触发操作名称 | varchar | 100 |  | √ | ' ' | 触发操作名称 |
| 5 | foperationnumber | 触发操作编码 | varchar | 100 |  | √ | ' ' | 触发操作编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_dhc_operation_pkey |  | fid |
| 2 | idx_dhc_operation_bindbill |  | fbindbill |
