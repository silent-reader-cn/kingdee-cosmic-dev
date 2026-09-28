# 字段权限方案明细差异-perm_log_diff_fpsd

## 字段权限方案明细差异-主表 t_perm_log_diff_fpsd

- **表名称：** 字段权限方案明细差异-主表
- **表名：** t_perm_log_diff_fpsd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | ID | int8 | 64 |  | √ | 0 | ID |
| 2 | fdatachange_type_desc | 数据范围类型描述 | varchar | 20 |  | √ | ' ' | 数据范围类型描述 |
| 3 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 4 | ffieldname | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 5 | fcloud_id | 云编码 | varchar | 36 |  | √ | ' ' | 云编码 |
| 6 | fcloud_name | 云 | varchar | 100 |  | √ | ' ' | 云 |
| 7 | fentity_name | 实体名 | varchar | 200 |  | √ | ' ' | 实体名 |
| 8 | fcontrolmode | 控制模型 | varchar | 20 |  | √ | ' ' | 控制模型 |
| 9 | fentity_id | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 10 | fapp_name | 应用 | varchar | 100 |  | √ | ' ' | 应用 |
| 11 | ffieldcomment | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 12 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 14 | fcontrolmodedesc | 控制模型描述 | varchar | 30 |  | √ | ' ' | 控制模型描述 |
| 15 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 16 | fapp_id | 应用编码 | varchar | 36 |  | √ | ' ' | 应用编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fpsd_permlogid |  | fperm_logid,fentity_name |
| 2 | pk_perm_log_diff_fpsd |  | fid |
