# 销项标识单据-tcvat_output_invoice_sign

## 销项标识单据-主表 t_tcvat_output_inv_sign

- **表名称：** 销项标识单据-主表
- **表名：** t_tcvat_output_inv_sign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsigntime | 标识时间 | timestamp | 0 |  |  | null | 标识时间 |
| 3 | foperator | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsignedtax | 已标识税额 | numeric | 23 | 10 | √ | 0 | 已标识税额 |
| 5 | fsubinvoiceid | 发票子表id | int8 | 64 |  | √ | 0 | 发票子表id |
| 6 | fjzjtproduct | 即征即退产品 | int8 | 64 |  | √ | 0 | 即征即退产品 tcvat_jzjt_product |
| 7 | fmaininvoiceid | 发票主表id | int8 | 64 |  | √ | 0 | 发票主表id |
| 8 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 9 | fjzjtsign | 即征即退标识 | varchar | 50 |  | √ | ' ' | 即征即退标识,枚举: 1 :是 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_outsign_main_sign |  | fmaininvoiceid,fjzjtsign |
| 2 | idx_taxc_outsign_sub_sign |  | fsubinvoiceid,fjzjtsign |
| 3 | pk_tcvat_output_inv_sign |  | fid |
