# 日志迁移设置-bos_log_etl_setting

## 日志迁移设置-主表 t_log_etl_setting

- **表名称：** 日志迁移设置-主表
- **表名：** t_log_etl_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 使用状态 | varchar | 20 |  | √ | ' ' | 使用状态 |
| 3 | ftype | 类型 | varchar | 20 |  | √ | ' ' | 类型 |
| 4 | ftablename | 归档表名 | varchar | 30 |  | √ | ' ' | 归档表名 |
| 5 | farchivedays | 归档天数 | int8 | 64 |  | √ | 180 | 归档天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_log_etl_setting |  | fid |
| 2 | idx_etl_setting_tab |  | ftablename |
