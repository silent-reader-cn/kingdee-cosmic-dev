# 报销单-rim_expense_manage

## 报销单-主表 t_rim_expense_manage

- **表名称：** 报销单-主表
- **表名：** t_rim_expense_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :待采集 B :待审核 C :已驳回 D :审核通过 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | finvoice_num | 发票数量 | int8 | 64 |  | √ | 0 | 发票数量 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | finvoice_total_amount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 8 | freimburser | 报销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus_update_time | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 12 | fcompany_tax_no | 费用承担公司税号 | varchar | 50 |  | √ | ' ' | 费用承担公司税号 |
| 13 | fqrcode | 二维码信息 | varchar | 300 |  | √ | ' ' | 二维码信息 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcompany_name | 费用承担公司名称 | varchar | 100 |  | √ | ' ' | 费用承担公司名称 |
| 16 | fbillno | 单据编号 | varchar | 38 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fexpense_type | 单据类型 | int8 | 64 |  | √ | 0 | 手动添加单据类型 rim_expense_type |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_expense_manage |  | fid |
| 2 | idx_rim_expense_manage |  | fbillno |
