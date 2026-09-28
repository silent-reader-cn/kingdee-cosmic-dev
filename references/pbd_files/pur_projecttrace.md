# 项目号跟踪号-pur_projecttrace

## 项目号跟踪号-主表 t_pur_project_trace

- **表名称：** 项目号跟踪号-主表
- **表名：** t_pur_project_trace

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 4 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_project_fprojectid |  | fprojectid |
| 2 | t_pur_project_trace_pkey |  | fid |
| 3 | idx_pur_project_ftraceid |  | ftraceid |
