# 查验日志-rim_check_log

## 查验日志-主表 t_rim_check_log

- **表名称：** 查验日志-主表
- **表名：** t_rim_check_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftake_time | 接口耗时(ms) | int8 | 64 |  | √ | 0 | 接口耗时(ms) |
| 3 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 6 | ferrcode | errcode | varchar | 10 |  | √ | ' ' | errcode |
| 7 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 8 | finterface | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型 |
| 9 | fdescription | description | varchar | 200 |  | √ | ' ' | description |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_check_log_time |  | fcreate_time,ferrcode |
| 2 | idx_rim_check_log |  | finvoice_code,finvoice_no |
| 3 | pk_t_rim_check_log |  | fid |
