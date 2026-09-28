# 容差方案分配关系-ap_tolerance_assign

## 容差方案分配关系-主表 t_ap_tolerance_assign

- **表名称：** 容差方案分配关系-主表
- **表名：** t_ap_tolerance_assign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypepk | 分配类型主键 | varchar | 50 |  | √ | ' ' | 分配类型主键 |
| 3 | fassigntype | 分配类型 | varchar | 50 |  | √ | ' ' | 分配类型 |
| 4 | fassigndate | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 5 | fschemepk | 容差方案主键 | varchar | 50 |  | √ | ' ' | 容差方案主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_tolerance_assign |  | fid |
| 2 | idx_ap_tol_assigntype |  | fassigntype |
