# 业务提示-isc_init_detailinfo

## 业务提示-主表 t_isc_initdetail

- **表名称：** 业务提示-主表
- **表名：** t_isc_initdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexcutepercent | 执行百分比 | varchar | 100 |  | √ | ' ' | 执行百分比 |
| 3 | flastreceivetime | 任务下达时间 | varchar | 100 |  | √ | ' ' | 任务下达时间 |
| 4 | fexcutestatus | 执行状态 | varchar | 100 |  | √ | ' ' | 执行状态 |
| 5 | fuseguide | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_initdetail_pkey |  | fid |
| 2 | idx_isc_initde_fuguide |  | fuseguide |
