# 报销单信息-rim_expense

## 报销单信息-主表 t_rim_expense

- **表名称：** 报销单信息-主表
- **表名：** t_rim_expense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fcreator_id | 制单人 | varchar | 50 |  | √ | ' ' | 制单人 |
| 4 | finvoice_amount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 5 | fcreator_phone | 制单人手机 | varchar | 50 |  | √ | ' ' | 制单人手机 |
| 6 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 7 | fexpense_num | 报销单编码 | varchar | 50 |  | √ | ' ' | 报销单编码 |
| 8 | fupdate_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | freimbursing_id | 苍穹的原始报销单ID | varchar | 50 |  | √ | ' ' | 苍穹的原始报销单ID |
| 11 | fapprove_amount | 核准金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核准金额 |
| 12 | fappid | appid | varchar | 50 |  | √ | ' ' | appid |
| 13 | fstatus | 报销单状态 | varchar | 2 |  | √ | ' ' | 报销单状态,枚举: 1 :未用 30 :在用 60 :已用 65 :已入账 |
| 14 | fexpense_id | 报销单id | varchar | 50 |  | √ | ' ' | 报销单id |
| 15 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fresource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 1 :手工维护 2 :正常提交报销单 |
| 17 | fentityid | 报销单实体id | varchar | 50 |  | √ | ' ' | 报销单实体id |
| 18 | fexpense_amount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 19 | fcreator_name | 制单人姓名 | varchar | 50 |  | √ | ' ' | 制单人姓名 |
| 20 | fview_page | 详情页面 | varchar | 50 |  | √ | ' ' | 详情页面 |
| 21 | fcreator_email | 制单人邮箱 | varchar | 50 |  | √ | ' ' | 制单人邮箱 |
| 22 | fexpense_type | 报销单类型 | varchar | 50 |  | √ | ' ' | 报销单类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_expense |  | fexpense_id |
| 2 | pk_rim_expense |  | fid |
