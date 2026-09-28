# 业务单元管辖范围差异-perm_log_diff_busiunit

## 业务单元管辖范围差异-主表 t_perm_log_diff_busiunit

- **表名称：** 业务单元管辖范围差异-主表
- **表名：** t_perm_log_diff_busiunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主键id | int8 | 64 |  | √ | 0 | 主键id |
| 2 | fdatachange_type_desc | 数据变更类型描述 | varchar | 20 |  | √ | ' ' | 数据变更类型描述 |
| 3 | fperm_logid | 操作日志ID | int8 | 64 |  | √ | 0 | 操作日志ID |
| 4 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdatachange_type | 数据变更类型 | int4 | 32 |  | √ | 0 | 数据变更类型 |
| 6 | fbusiunit_number | 业务单元编码 | varchar | 50 |  | √ | ' ' | 业务单元编码 |
| 7 | fbusiunit_id | 业务单元id | int8 | 64 |  | √ | 0 | 业务单元id |
| 8 | fop_desc | 操作描述 | varchar | 300 |  | √ | ' ' | 操作描述 |
| 9 | fbusiunit_name | 业务单元名称 | varchar | 255 |  | √ | ' ' | 业务单元名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_logid_busiunit |  | fperm_logid |
| 2 | pk_perm_log_diff_busiunit |  | fid |
