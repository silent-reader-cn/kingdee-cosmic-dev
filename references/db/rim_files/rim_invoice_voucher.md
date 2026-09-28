# 发票电子会计凭证-rim_invoice_voucher

## 发票电子会计凭证-主表 t_rim_invoice_voucher

- **表名称：** 发票电子会计凭证-主表
- **表名：** t_rim_invoice_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxbrl_url | 开具端xbrl的下载地址 | varchar | 200 |  | √ | ' ' | 开具端xbrl的下载地址 |
| 3 | freceive_xbrl_url | 接收端xbrl的下载地址 | varchar | 150 |  |  | ' ' | 接收端xbrl的下载地址 |
| 4 | fserial_no | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 5 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fxbrl_name | 开具端xbrl文件名 | varchar | 150 |  | √ | ' ' | 开具端xbrl文件名 |
| 8 | freceive_xbrl_name | 接收端xbrl文件名 | varchar | 200 |  |  | ' ' | 接收端xbrl文件名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_invoice_voucher |  | fid |
| 2 | idx_rim_invoice_voucher_serial |  | fserial_no |
