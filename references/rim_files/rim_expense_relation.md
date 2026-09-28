# 报销单发票关系-rim_expense_relation

## 报销单发票关系-主表 t_rim_expense_relation

- **表名称：** 报销单发票关系-主表
- **表名：** t_rim_expense_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreset_deduction_purpose | 单据抵扣用途 | varchar | 2 |  | √ | ' ' | 单据抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 3 | fexpense_num | 报销单编号 | varchar | 50 |  | √ | ' ' | 报销单编号 |
| 4 | fdeduction_flag | 是否可抵扣 | varchar | 2 |  | √ | ' ' | 是否可抵扣,枚举: 1 :是 0 :否 |
| 5 | fdeduction_amount | 可抵扣金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣金额 |
| 6 | fstatus | 报销单状态 | varchar | 2 |  | √ | ' ' | 报销单状态,枚举: 1 :未用 30 :在用 60 :已用 65 :已入账 70 :已归档 |
| 7 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 8 | frollout_amount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 9 | fcheck_status | 查验状态 | varchar | 2 |  | √ | ' ' | 查验状态,枚举: |
| 10 | fexpense_id | 报销单id | varchar | 50 |  | √ | ' ' | 报销单id |
| 11 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | freimbursingid | 原单据id | varchar | 50 |  | √ | ' ' | 原单据id |
| 13 | fentry_id | 分录id | varchar | 50 |  | √ | ' ' | 分录id |
| 14 | frollout_remark | 转出原因 | varchar | 300 |  | √ | ' ' | 转出原因 |
| 15 | fresource | 报销单来源 | varchar | 50 |  | √ | ' ' | 报销单来源 |
| 16 | fentityid | 报销单实体id | varchar | 50 |  | √ | ' ' | 报销单实体id |
| 17 | fexpense_amount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 18 | fview_page | 详情页面 | varchar | 50 |  | √ | ' ' | 详情页面 |
| 19 | fexpense_type | 报销单类型 | varchar | 50 |  | √ | ' ' | 报销单类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_expense_relation2 |  | fexpense_id,fresource |
| 2 | pk_rim_expense_relation |  | fid |
| 3 | idx_rim_expense_relation |  | fserial_no |
