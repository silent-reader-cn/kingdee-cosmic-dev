# 火车票退票凭证-rim_inv_train_refund

## 火车票退票凭证-主表 t_rim_inv_train_refund

- **表名称：** 火车票退票凭证-主表
- **表名：** t_rim_inv_train_refund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 7 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 8 | fbillno | 单据编号 | varchar | 36 |  | √ | ' ' | 单据编号 |
| 9 | forg_id | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | faws_serial_no | AWS发票流水号 | varchar | 36 |  | √ | ' ' | AWS发票流水号 |
| 12 | ftotal_amount | 票价 | numeric | 23 | 10 | √ | 0 | 票价 |
| 13 | fbillstatus | 单据状态 | varchar | 2 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | finvoice_date | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fvoucher_title | 抬头标题 | varchar | 50 |  | √ | ' ' | 抬头标题 |
| 18 | ftax_org | 纳税主体 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fdelete | 可用状态 | varchar | 4 |  | √ | '1' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 20 | fexpense_status | 报销状态 | varchar | 2 |  |  | null | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 21 | foriginal_state | 原件签收状态 | varchar | 2 |  |  | null | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 22 | finvoice_type | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 23 | fnumber | 收据号码 | varchar | 32 |  | √ | ' ' | 收据号码 |
| 24 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_inv_train_refund_num |  | fnumber |
| 2 | idx_rim_inv_train_refund |  | fserial_no |
| 3 | pk_t_rim_inv_train_refund |  | fid |
