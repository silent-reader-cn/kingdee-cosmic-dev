# MQ消息记录-cas_mq_record

## MQ消息记录-主表 t_cas_mq_record

- **表名称：** MQ消息记录-主表
- **表名：** t_cas_mq_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | ferrormsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: voucherbook :凭证登账 |
| 7 | fmsginfo_tag | 消息内容_详情 | text | 0 |  |  | null | 消息内容_详情 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | foperateinfo | 操作对象 | varchar | 1024 |  | √ | ' ' | 操作对象 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmsgstatus | 消息状态 | varchar | 30 |  | √ | ' ' | 消息状态,枚举: init :初始化 send :已发送 rec :已接收 fin :已完成 err :发送失败 rep :已重发 |
| 12 | fmsginfo | 消息内容 | varchar | 255 |  | √ | ' ' | 消息内容 |
| 13 | foperate | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbusinessstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: todo :待处理 succ :成功 fail :失败 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ferrormsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_mq_rd_fbillno |  | fbillno |
| 2 | pk_t_cas_mq_record |  | fid |
