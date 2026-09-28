# 发票操作日志-rim_invoice_log

## 发票操作日志-主表 t_rim_invoice_log

- **表名称：** 发票操作日志-主表
- **表名：** t_rim_invoice_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flog_type | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: save :发票保存 delete :全票池删除 sign :发票签收 unsign :发票反签收 expense :维护报销信息 voucher :维护入账信息 deduct_authenticate :勾选认证 transport_deduction :旅客运输抵扣 |
| 3 | fserial_no | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | flog_info | 日志信息 | varchar | 400 |  | √ | ' ' | 日志信息 |
| 7 | fresource | 来源 | varchar | 50 |  | √ | ' ' | 来源 |
| 8 | fcollect_type | 采集方式 | varchar | 20 |  | √ | ' ' | 采集方式,枚举: 1 :手机拍照 2 :文件上传 3 :扫描仪 4 :扫码枪 5 :手工录入 9 :税盘 10 :excel引入 15 :税局同步 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_log |  | fserial_no |
| 2 | pk_t_rim_invoice_log |  | fid |
| 3 | idx_rim_invoice_log2 |  | fcreate_time,fcreater |
