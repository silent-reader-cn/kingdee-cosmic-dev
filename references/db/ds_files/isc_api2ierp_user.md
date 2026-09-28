# 人员-isc_api2ierp_user

## 人员-主表 t_ds_api2ierp_user

- **表名称：** 人员-主表
- **表名：** t_ds_api2ierp_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpresit_string_field_g | 预留字段g | varchar | 200 |  | √ | ' ' | 预留字段g |
| 3 | fpresit_string_field_h | 预留字段h | varchar | 200 |  | √ | ' ' | 预留字段h |
| 4 | fpresit_string_field_e | 预留字段e | varchar | 200 |  | √ | ' ' | 预留字段e |
| 5 | fpresit_string_field_f | 预留字段f | varchar | 200 |  | √ | ' ' | 预留字段f |
| 6 | fmail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 7 | fsuperior | 第三方上级人员id | varchar | 2000 |  | √ | ' ' | 第三方上级人员id |
| 8 | fusername | 用户名 | varchar | 200 |  | √ | ' ' | 用户名 |
| 9 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fid_number | 身份证号 | varchar | 50 |  | √ | ' ' | 身份证号 |
| 11 | fposition | 职位 | varchar | 2000 |  | √ | ' ' | 职位 |
| 12 | fusertype | 用户类型 | varchar | 10 |  | √ | ' ' | 用户类型 |
| 13 | fpresit_string_field_c | 预留字段c | varchar | 200 |  | √ | ' ' | 预留字段c |
| 14 | ffrom | 来源第三方系统 | varchar | 50 |  | √ | ' ' | 来源第三方系统 |
| 15 | fpresit_string_field_d | 预留字段d | varchar | 200 |  | √ | ' ' | 预留字段d |
| 16 | fpresit_string_field_a | 预留字段a | varchar | 200 |  | √ | ' ' | 预留字段a |
| 17 | fpresit_string_field_b | 预留字段b | varchar | 200 |  | √ | ' ' | 预留字段b |
| 18 | fname | 姓名 | varchar | 200 |  | √ | ' ' | 姓名 |
| 19 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 20 | fpresit_timestamp_a | 预留日期a | timestamp | 0 |  |  | null | 预留日期a |
| 21 | fpresit_timestamp_b | 预留日期b | timestamp | 0 |  |  | null | 预留日期b |
| 22 | fgender | 性别 | varchar | 10 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 :保密 |
| 23 | fpresit_bigint_b | 预留长整数b | int8 | 64 |  | √ | 0 | 预留长整数b |
| 24 | fierp_user_id | 苍穹人员反写id | int8 | 64 |  | √ | 0 | 苍穹人员反写id |
| 25 | fdpt | 第三方部门id | varchar | 2000 |  | √ | ' ' | 第三方部门id |
| 26 | ftrd_user_id | 第三方人员ID | varchar | 50 |  | √ | ' ' | 第三方人员ID |
| 27 | fpresit_bigint_a | 预留长整数a | int8 | 64 |  | √ | 0 | 预留长整数a |
| 28 | fenable | 启用状态 | varchar | 10 |  | √ | ' ' | 启用状态,枚举: 1 :启用 0 :禁用 |
| 29 | fcreatime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 30 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_api2ierp_user_f |  | ffrom |
| 2 | index_api2ierp_user_n |  | fnumber |
| 3 | pk_t_ds_api2ierp_user |  | fid |
| 4 | index_api2ierp_user_u |  | ftrd_user_id |
