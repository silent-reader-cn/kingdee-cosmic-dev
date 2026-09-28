# 发票预警数据表-rim_inv_warning_data

## 发票预警数据表-主表 t_rim_inv_warning_data

- **表名称：** 发票预警数据表-主表
- **表名：** t_rim_inv_warning_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdata_type | 预警类型 | varchar | 50 |  | √ | ' ' | 预警类型 |
| 3 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdata_period | 数据期限 | varchar | 10 |  | √ | ' ' | 数据期限 |
| 5 | fdata_value | 计算值 | numeric | 23 | 10 | √ | 0 | 计算值 |
| 6 | forg | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_inv_warning_data |  | fid |
| 2 | idx_rim_inv_warning_data |  | forg,fdata_period |
