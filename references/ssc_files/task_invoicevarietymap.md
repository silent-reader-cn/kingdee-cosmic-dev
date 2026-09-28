# 发票种类映射-task_invoicevarietymap

## 发票种类映射-主表 t_tk_invoicevarietymap

- **表名称：** 发票种类映射-主表
- **表名：** t_tk_invoicevarietymap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourceinvoicevarietycode | 源发票种类编号 | varchar | 100 |  | √ | ' ' | 源发票种类编号 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | finvoicetypename | 发票类型名称 | varchar | 100 |  | √ | ' ' | 发票类型名称 |
| 5 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | ftargetinvoicevarietycode | 目标发票种类编号 | varchar | 100 |  | √ | ' ' | 目标发票种类编号 |
| 7 | fsourceinvoicesystem | 源发票系统 | int8 | 64 |  | √ | 0 | 源发票系统,枚举: 1 :发票云 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_invoicevarietymap |  | fsourceinvoicesystem |
| 2 | t_tk_invoicevarietymap_pkey |  | fid |
