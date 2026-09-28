# 脚本操作日志-bos_devp_scriptoperatelog

## 脚本操作日志-主表 t_meta_scriptlog

- **表名称：** 脚本操作日志-主表
- **表名：** t_meta_scriptlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsessionid | 会话id | varchar | 200 |  | √ | ' ' | 会话id |
| 3 | fuserid | 操作人 | varchar | 100 |  | √ | ' ' | 操作人 |
| 4 | fdata | 数据 | varchar | 500 |  | √ | ' ' | 数据 |
| 5 | fcurrenttime | 时间戳 | timestamp | 0 |  |  | null | 时间戳 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_scriptlog_num |  | fsessionid |
| 2 | t_meta_scriptlog_pkey |  | fid |
