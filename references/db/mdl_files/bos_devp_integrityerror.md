# 完整性错误实体-bos_devp_integrityerror

## 完整性错误实体-主表 t_meta_integrityerror

- **表名称：** 完整性错误实体-主表
- **表名：** t_meta_integrityerror

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态 |
| 3 | ftype | 错误类型 | varchar | 50 |  | √ | ' ' | 错误类型 |
| 4 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 5 | fchecktime | 检查时间 | timestamp | 0 |  |  | null | 检查时间 |
| 6 | ferrorid | 错误id | varchar | 36 |  | √ | ' ' | 错误id |
| 7 | ffixtime | 修复时间 | timestamp | 0 |  |  | null | 修复时间 |
| 8 | fappid | 应用id | varchar | 36 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_errorinfo_app |  | fappid |
| 2 | t_meta_integrityerror_pkey |  | fid |
