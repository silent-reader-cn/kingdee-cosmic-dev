# 发票状态修改操作日志-rim_expense_status_log

## 发票状态修改操作日志-主表 t_rim_expense_status_log

- **表名称：** 发票状态修改操作日志-主表
- **表名：** t_rim_expense_status_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forg_id | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fphone | 电话 | varchar | 33 |  | √ | ' ' | 电话 |
| 4 | fexpense_num | 报销单编号 | varchar | 50 |  | √ | ' ' | 报销单编号 |
| 5 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 6 | fprev_status | 修改前状态 | varchar | 50 |  | √ | ' ' | 修改前状态,枚举: |
| 7 | fserial_no | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 8 | fcurrent_status | 修改后状态 | varchar | 50 |  | √ | ' ' | 修改后状态,枚举: |
| 9 | foperate_content | 操作内容 | varchar | 150 |  | √ | ' ' | 操作内容 |
| 10 | fopenid | 接入方openid | varchar | 80 |  | √ | ' ' | 接入方openid |
| 11 | fexpense_id | 报销单id | varchar | 50 |  | √ | ' ' | 报销单id |
| 12 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 13 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fcid | 客户接入id | varchar | 160 |  | √ | ' ' | 客户接入id |
| 15 | foperate_type | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: |
| 16 | fentry_id | 费用分录id | varchar | 50 |  | √ | ' ' | 费用分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_expense_status_log |  | fserial_no |
| 2 | pk_rim_expense_status_log |  | fid |
