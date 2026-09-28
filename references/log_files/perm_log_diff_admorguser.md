# 行政组织管辖范围额外用户差异-perm_log_diff_admorguser

## 行政组织管辖范围额外用户差异-主表 t_perm_log_diff_admorgusr

- **表名称：** 行政组织管辖范围额外用户差异-主表
- **表名：** t_perm_log_diff_admorgusr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 操作日志用户关联ID | int8 | 64 |  | √ | 0 | 操作日志用户关联ID |
| 2 | fname | 用户名称 | varchar | 50 |  | √ | ' ' | 用户名称 |
| 3 | fphone | 手机号 | varchar | 36 |  | √ | ' ' | 手机号 |
| 4 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 5 | fuser_name | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 6 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 7 | femail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 8 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 10 | fuser_id | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 11 | fnumber | 用户工号 | varchar | 36 |  | √ | ' ' | 用户工号 |
| 12 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_admorgusr |  | fperm_logid |
| 2 | idx_uname_admorgusr |  | fuser_name |
| 3 | pk_perm_log_diff_admorgusr |  | fid |
