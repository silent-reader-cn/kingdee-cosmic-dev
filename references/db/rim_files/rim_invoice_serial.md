# 发票流水号-rim_invoice_serial

## 发票流水号-主表 t_rim_invoice_serial

- **表名称：** 发票流水号-主表
- **表名：** t_rim_invoice_serial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodify_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fserial_no | 发票流水号 | varchar | 40 |  | √ | ' ' | 发票流水号 |
| 4 | faws_serial_no | aws流水号 | varchar | 40 |  | √ | ' ' | aws流水号 |
| 5 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_serial |  | faws_serial_no |
| 2 | pk_rim_invoice_serial |  | fid |
