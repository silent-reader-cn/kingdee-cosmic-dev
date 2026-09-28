# 字段权限方案差异-perm_log_diff_fps

## 字段权限方案差异-主表 t_perm_log_diff_fps

- **表名称：** 字段权限方案差异-主表
- **表名：** t_perm_log_diff_fps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 4 | fcloud_id | 云编码 | varchar | 36 |  | √ | ' ' | 云编码 |
| 5 | fcloud_name | 云 | varchar | 100 |  | √ | ' ' | 云 |
| 6 | fentity_name | 实体名 | varchar | 200 |  | √ | ' ' | 实体名 |
| 7 | ffpschemeid | 字段方案id | int8 | 64 |  | √ | 0 | 字段方案id |
| 8 | fentity_num | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 9 | fsensitive | 敏感方案 | bpchar | 1 |  | √ | '0' | 敏感方案 |
| 10 | fapp_name | 应用 | varchar | 100 |  | √ | ' ' | 应用 |
| 11 | ffpschemename | 字段方案名 | varchar | 255 |  | √ | ' ' | 字段方案名 |
| 12 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 14 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 15 | fapp_id | 应用编码 | varchar | 36 |  | √ | ' ' | 应用编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fps_permlogid |  | fperm_logid,fentity_name |
| 2 | pk_perm_log_diff_fps |  | fid |
