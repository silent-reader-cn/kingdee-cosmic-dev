# 进项发票项目关系-til_in_invoice_project

## 进项发票项目关系-主表 t_til_invoice_project

- **表名称：** 进项发票项目关系-主表
- **表名：** t_til_invoice_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 预缴项目信息 tcvat_prepay_project_info |
| 3 | fsplit | 是否对外分包 | varchar | 50 |  | √ | ' ' | 是否对外分包,枚举: true :是 false :否 updatedtrue :已升级，原为是 updatedfalse :已升级，原为否 updated :已升级 |
| 4 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 6 | finvoiceid | 发票id | varchar | 50 |  | √ | ' ' | 发票id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_til_invoice_project |  | fprojectid,finvoiceid,fbaseinvoicetype |
| 2 | pk_til_invoice_project |  | fid |
