# 银行流水号表-aqap_bank_serial_no

## 银行流水号表-主表 t_aqap_bank_serial_no

- **表名称：** 银行流水号表-主表
- **表名：** t_aqap_bank_serial_no

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fbank_version | 银行版本 | varchar | 50 |  | √ | null | 银行版本 |
| 3 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 4 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fnumber | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_bank_serial_no_sr1 |  | fnumber,fcustom_id,fbank_version |
| 2 | t_aqap_bank_serial_no_pkey |  | fid |
