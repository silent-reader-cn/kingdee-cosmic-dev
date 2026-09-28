# 查验结果-rim_check_result

## 查验结果-主表 t_rim_check_result

- **表名称：** 查验结果-主表
- **表名：** t_rim_check_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheck_time | 查验时间 | timestamp | 0 |  |  | null | 查验时间 |
| 3 | fcheck_result_tag | 查验结果_详情 | text | 0 |  |  | null | 查验结果_详情 |
| 4 | finvoice_code | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 5 | fcheck_result | 查验结果 | varchar | 255 |  | √ | ' ' | 查验结果 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | finvoice_no | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 8 | fcheck_type | 查验方式 | varchar | 50 |  | √ | ' ' | 查验方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_check_result |  | fid |
| 2 | idx_rim_check_result |  | finvoice_code,finvoice_no |
