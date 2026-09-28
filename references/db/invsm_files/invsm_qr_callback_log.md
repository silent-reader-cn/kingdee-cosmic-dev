# 扫码开票发票数据回传移动云-invsm_qr_callback_log

## 扫码开票发票数据回传移动云-主表 t_invsm_qr_callback_log

- **表名称：** 扫码开票发票数据回传移动云-主表
- **表名：** t_invsm_qr_callback_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcallbackcode | 回调返回码 | varchar | 50 |  | √ | ' ' | 回调返回码 |
| 4 | fretrytimes | 回调重试次数 | int8 | 64 |  | √ | 0 | 回调重试次数 |
| 5 | fmodifydate | 最后同步时间 | timestamp | 0 |  |  | null | 最后同步时间 |
| 6 | fnoticedata | 业务系统通知消息 | varchar | 300 |  | √ | ' ' | 业务系统通知消息 |
| 7 | fbustype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: M :移动云 E :ERP |
| 8 | fmethodcode | 回调方法名 | varchar | 50 |  | √ | ' ' | 回调方法名 |
| 9 | fvatinvoiceid | 发票记录ID | varchar | 50 |  | √ | ' ' | 发票记录ID |
| 10 | fcallbackmurl | 回调移动云地址 | varchar | 200 |  | √ | ' ' | 回调移动云地址 |
| 11 | fcallbackmsg | 回调返回消息 | varchar | 200 |  | √ | ' ' | 回调返回消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invsm_qr_callback_log |  | fvatinvoiceid |
| 2 | pk_invsm_qr_callback_log |  | fid |
