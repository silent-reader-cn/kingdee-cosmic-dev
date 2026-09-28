# 日志设置-bos_log_appsetting

## 日志设置-主表 t_log_appsetting

- **表名称：** 日志设置-主表
- **表名：** t_log_appsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | null | id |
| 2 | fdumpedcount | 已转储数量 | int8 | 64 |  | √ | 0 | 已转储数量 |
| 3 | farchivedcount | 已归档数量 | int8 | 64 |  | √ | 0 | 已归档数量 |
| 4 | fsearchappbaktime | fsearchappbaktime | int4 | 32 |  | √ | 0 |  |
| 5 | fapplogretaindays |  | int8 | 64 |  | √ | 0 |  |
| 6 | fdeleteapptime | fdeleteapptime | int4 | 32 |  | √ | 0 |  |
| 7 | fcurrentstep | 当前升级步骤 | varchar | 10 |  | √ | ' ' | 当前升级步骤 |
| 8 | fheartbeattime | fheartbeattime | int4 | 32 |  | √ | 0 |  |
| 9 | fsearcharchivetime | fsearcharchivetime | int4 | 32 |  | √ | 0 |  |
| 10 | fsearchapptime | fsearchapptime | int4 | 32 |  | √ | 0 |  |
| 11 | fopuserformat | 下拉列表 | varchar | 30 |  | √ | ' ' | 下拉列表,枚举: name :姓名 name+number :姓名+工号 name+username :姓名+用户名 name+phone :姓名+手机号 |
| 12 | fautocleartime | 自动清理期限 | int8 | 64 |  |  | null | 自动清理期限 |
| 13 | fautoarchiveamt | 自动归档数量 | int8 | 64 |  |  | null | 自动归档数量 |
| 14 | fupgradestatus | 升级状态 | varchar | 10 |  | √ | ' ' | 升级状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_log_appsetting_archive |  | fautoarchiveamt,fautocleartime |
| 2 | t_log_appsetting_pkey |  | fid |
