# 通知影像失败数据-er_notifyofinvoice_fail

## 通知影像失败数据-主表 t_er_invoice_notify_error

- **表名称：** 通知影像失败数据-主表
- **表名：** t_er_invoice_notify_error

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorloginfo | 上次执行错误信息log | varchar | 255 |  | √ | ' ' | 上次执行错误信息log |
| 3 | flastruntime | 上次执行时间 | timestamp | 0 |  |  | null | 上次执行时间 |
| 4 | ferrorcount | 已失败次数 | int8 | 64 |  | √ | 0 | 已失败次数 |
| 5 | fbillid | 单据id | varchar | 30 |  | √ | ' ' | 单据id |
| 6 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 7 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_notifybillid |  | fbillid |
| 2 | pk_t_er_invoice_notify_error |  | fid |
