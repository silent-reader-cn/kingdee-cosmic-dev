# 回单报文-receipt_json

## 回单报文-主表 t_receipt_json

- **表名称：** 回单报文-主表
- **表名：** t_receipt_json

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fjson | 回单报文 | varchar | 255 |  | √ | ' ' | 回单报文 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbank_version | 银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 9 | fcustom_id | 租户编号 | varchar | 50 |  | √ | ' ' | 租户编号 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | freceipt_detail_id | 回单详情编号 | varchar | 50 |  | √ | ' ' | 回单详情编号 |
| 12 | fjson_tag | 回单报文_详情 | text | 0 |  |  | null | 回单报文_详情 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_receipt_json_pk |  | freceipt_detail_id |
| 2 | t_receipt_json_pkey |  | fid |
| 3 | idx_receipt_j_b_index |  | fbank_version |
