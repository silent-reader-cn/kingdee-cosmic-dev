# 火车票退票凭证-eafc_inv_train_refund

## 火车票退票凭证-主表 t_eafc_inv_train_refund

- **表名称：** 火车票退票凭证-主表
- **表名：** t_eafc_inv_train_refund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源,枚举: |
| 8 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 11 | forg_id | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | ftotal_amount | 票价 | numeric | 23 | 2 |  | null | 票价 |
| 14 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | finvoice_date | 发票日期 | timestamp | 0 |  |  | null | 发票日期 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fvoucher_title | 抬头标题 | varchar | 50 |  | √ | ' ' | 抬头标题 |
| 19 | ftax_org | 纳税主体 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fdelete | 可用状态 | varchar | 50 |  | √ | ' ' | 可用状态,枚举: 1 :可用 2 :作废 3 :删除 |
| 21 | fexpense_status | 报销状态 | varchar | 50 |  | √ | ' ' | 报销状态,枚举: 1 :未报销 30 :审核中 60 :已报销 65 :已入账 |
| 22 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 23 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 24 | fnumber | 收据号码 | varchar | 32 |  | √ | ' ' | 收据号码 |
| 25 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_train_refund |  | fid |
