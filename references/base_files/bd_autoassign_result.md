# 自动分配执行结果-bd_autoassign_result

## 自动分配执行结果-主表 t_bd_autoassign_result

- **表名称：** 自动分配执行结果-主表
- **表名：** t_bd_autoassign_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fplandetailid | 方案分录ID | int8 | 64 |  | √ | 0 | 方案分录ID |
| 4 | fexecutetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 5 | fresult | 执行结果 | varchar | 255 |  | √ | ' ' | 执行结果 |
| 6 | fnumber | 方案编码 | varchar | 36 |  | √ | ' ' | 方案编码 |
| 7 | fentityid | 基础资料标识ID | varchar | 36 |  | √ | ' ' | 基础资料标识ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_autoassignresult_entity |  | fentityid |
| 2 | pk_t_bd_autoassign_result |  | fid |
