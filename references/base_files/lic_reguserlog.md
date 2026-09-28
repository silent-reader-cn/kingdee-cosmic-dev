# 注册用户日志-lic_reguserlog

## 注册用户日志-主表 t_lic_reguserlog

- **表名称：** 注册用户日志-主表
- **表名：** t_lic_reguserlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fopname | 操作名称 | varchar | 255 |  | √ | ' ' | 操作名称 |
| 3 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fopdescription | 操作描述 | varchar | 255 |  | √ | ' ' | 操作描述 |
| 5 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_lic_reguserlog_userid |  | fuserid |
| 2 | t_lic_reguserlog_pkey |  | fid |
