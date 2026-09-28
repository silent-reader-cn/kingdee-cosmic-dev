# 进项发票项目关系-tcvat_in_invoice_project

## 进项发票项目关系-主表 t_tcvat_invoice_project

- **表名称：** 进项发票项目关系-主表
- **表名：** t_tcvat_invoice_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fradiogroupfield | fradiogroupfield | varchar | 30 |  | √ | ' ' |  |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [预缴项目信息 tcvat_prepay_project_info](../tcvat_files/tcvat_prepay_project_info.md) |
| 4 | fsplit | 是否对外分包 | varchar | 30 |  | √ | ' ' | 是否对外分包,枚举: true :是 false :否 |
| 5 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 4 :增值税专用发票 3 :增值税普通发票 1 :增值税电子发票 15 :通行费电子发票 |
| 6 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 7 | finvoiceid | 发票id | varchar | 50 |  | √ | ' ' | 发票id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_invoice_project |  | fid |
| 2 | idx_tcvat_invoice_project |  | finvoiceid |
