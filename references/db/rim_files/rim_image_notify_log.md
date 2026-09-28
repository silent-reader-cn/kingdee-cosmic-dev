# 影像通知日志-rim_image_notify_log

## 影像通知日志-主表 t_rim_image_notify_log

- **表名称：** 影像通知日志-主表
- **表名：** t_rim_image_notify_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | json | varchar | 500 |  | √ | ' ' | json |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fexpense_id | 单据id | varchar | 100 |  | √ | ' ' | 单据id |
| 7 | fscan_bill_no | 影像编码 | varchar | 100 |  | √ | ' ' | 影像编码 |
| 8 | fexpense_type | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_image_notify_log |  | fid |
| 2 | idx_notify_log_expense_id_type |  | fexpense_id,fexpense_type |

---

## 请求日志-子表 t_rim_notify_log_detail

- **表名称：** 请求日志-子表
- **表名：** t_rim_notify_log_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam | 请求参数 | varchar | 500 |  | √ | ' ' | 请求参数 |
| 3 | fuser | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | furl | url | varchar | 100 |  | √ | ' ' | url |
| 6 | fresult | 请求结果 | varchar | 100 |  | √ | ' ' | 请求结果 |
| 7 | ferror_info | 错误信息 | varchar | 100 |  | √ | ' ' | 错误信息 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpost_data | 请求时间 | timestamp | 0 |  |  | null | 请求时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_notify_log_detail_id |  | fid |
| 2 | pk_t_rim_notify_log_detail |  | fentryid |
