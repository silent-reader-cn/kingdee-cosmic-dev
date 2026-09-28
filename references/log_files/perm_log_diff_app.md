# 应用授权范围-perm_log_diff_app

## 应用授权范围-主表 t_perm_log_diff_app

- **表名称：** 应用授权范围-主表
- **表名：** t_perm_log_diff_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fapp_name | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 7 | fcloud_id | 云ID | varchar | 36 |  | √ | ' ' | 云ID |
| 8 | fcloud_name | 云名称 | varchar | 100 |  | √ | ' ' | 云名称 |
| 9 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 10 | fapp_id | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_app |  | fperm_logid |
| 2 | pk_perm_log_diff_app |  | fid |
