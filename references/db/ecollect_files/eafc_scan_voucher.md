# 扫码凭证组卷-eafc_scan_voucher

## 扫码凭证组卷-主表 tk_eafc_scan_voucher

- **表名称：** 扫码凭证组卷-主表
- **表名：** tk_eafc_scan_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_period_new | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间 |
| 3 | fk_eafc_book_type | 机构问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fk_eafc_file_sign | 文件题名 | varchar | 50 |  | √ | ' ' | 文件题名 |
| 5 | fk_eafc_coverno | 封面编号 | varchar | 50 |  | √ | ' ' | 封面编号 |
| 6 | fk_eafc_volume_serial_no | 卷内序号 | varchar | 50 |  | √ | ' ' | 卷内序号 |
| 7 | fk_eafc_billno | 文件编号 | varchar | 50 |  | √ | ' ' | 文件编号 |
| 8 | fk_eafc_voucher_id | 凭证id | varchar | 50 |  | √ | ' ' | 凭证id |
| 9 | fk_eafc_vouchernum | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 10 | fk_eafc_billid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 11 | fk_eafc_scan_type | 扫码方式 | varchar | 30 |  |  | null | 扫码方式,枚举: bill :单据扫码 voucher :凭证扫码 |
| 12 | fk_eafc_voucher_type | 凭证字 | varchar | 50 |  | √ | ' ' | 凭证字 |
| 13 | fk_eafc_time_millis | 时间戳 | int8 | 64 |  |  | null | 时间戳 |
| 14 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 15 | fk_eafc_page_id | 页面id | varchar | 50 |  | √ | ' ' | 页面id |
| 16 | fk_currenttime | 时间 | timestamp | 0 |  |  | null | 时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_scan_voucher |  | fid |
