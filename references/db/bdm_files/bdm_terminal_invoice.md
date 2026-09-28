# 终端发票号段-bdm_terminal_invoice

## 终端发票号段-主表 t_bdm_terminal_invoice

- **表名称：** 终端发票号段-主表
- **表名：** t_bdm_terminal_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsurplus | 剩余份数 | int8 | 64 |  | √ | 0 | 剩余份数 |
| 3 | fendno | 终止发票号码 | varchar | 50 |  | √ | ' ' | 终止发票号码 |
| 4 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 5 | finvoicecount | 发票份数 | int8 | 64 |  | √ | 0 | 发票份数 |
| 6 | fterminalcode | 终端代码 | varchar | 50 |  | √ | ' ' | 终端代码 |
| 7 | fstartno | 起始发票号码 | varchar | 50 |  | √ | ' ' | 起始发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_terminal_invoice_fk |  | fstartno |
| 2 | pk_bdm_terminal_invoice |  | fid |
