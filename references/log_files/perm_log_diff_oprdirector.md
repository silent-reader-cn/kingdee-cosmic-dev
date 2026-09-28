# 特殊数据权限指定主管差异-perm_log_diff_oprdirector

## 特殊数据权限指定主管差异-主表 t_perm_log_diff_oprdirect

- **表名称：** 特殊数据权限指定主管差异-主表
- **表名：** t_perm_log_diff_oprdirect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fphone | 主管手机号 | varchar | 36 |  | √ | ' ' | 主管手机号 |
| 3 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 4 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 5 | femail | 主管邮箱 | varchar | 100 |  | √ | ' ' | 主管邮箱 |
| 6 | forgid | 部门ID | int8 | 64 |  | √ | 0 | 部门ID |
| 7 | fdirector_id | 主管ID | int8 | 64 |  | √ | 0 | 主管ID |
| 8 | forg_name | 部门名 | varchar | 255 |  | √ | ' ' | 部门名 |
| 9 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 11 | fdirector_number | 主管工号 | varchar | 36 |  | √ | ' ' | 主管工号 |
| 12 | fdirector_username | 主管用户名 | varchar | 255 |  | √ | ' ' | 主管用户名 |
| 13 | fposition | 职位名称 | varchar | 255 |  | √ | ' ' | 职位名称 |
| 14 | fdirector_name | 主管姓名 | varchar | 50 |  | √ | ' ' | 主管姓名 |
| 15 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_perm_log_diff_oprdirect |  | fid |
| 2 | idx_logid_oprdirect |  | fperm_logid |
