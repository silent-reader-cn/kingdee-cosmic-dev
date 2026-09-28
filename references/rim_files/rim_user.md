# 收票用户-rim_user

## 收票用户-主表 t_rim_user

- **表名称：** 收票用户-主表
- **表名：** t_rim_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopen_name | open name | varchar | 150 |  | √ | ' ' | open name |
| 3 | fuser | 苍穹用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fclient_type | client type | varchar | 10 |  | √ | ' ' | client type |
| 5 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fopen_id | open id | varchar | 50 |  | √ | ' ' | open id |
| 7 | fresource | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 8 | fexternal_user | 第三方系统用户 | varchar | 50 |  | √ | ' ' | 第三方系统用户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_user |  | fid |
| 2 | idx_rim_user_open |  | fclient_type,fopen_id |
| 3 | idx_rim_user |  | fresource,fexternal_user |
