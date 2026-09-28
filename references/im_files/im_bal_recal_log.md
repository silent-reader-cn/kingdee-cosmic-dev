# 余额重算任务消息日志-im_bal_recal_log

## 余额重算任务消息日志-主表 t_im_bal_recal_log

- **表名称：** 余额重算任务消息日志-主表
- **表名：** t_im_bal_recal_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrormsg | 错误信息 | varchar | 200 |  | √ | ' ' | 错误信息 |
| 3 | fstart | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbal | 余额表 | varchar | 30 |  | √ | ' ' | 余额表 |
| 5 | fmsgusertime | 耗时/ms | int4 | 32 |  | √ | 0 | 耗时/ms |
| 6 | fbillfs | 单据过条件（序列化） | varchar | 2000 |  | √ | ' ' | 单据过条件（序列化） |
| 7 | fbillname | 单据实体 | varchar | 50 |  | √ | ' ' | 单据实体 |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fstatus | 状态 | bpchar | 1 |  | √ | 'C' | 状态,枚举: A :成功 B :失败 C :已创建 D :异常 E :重试中 |
| 10 | fmsgid | 消息ID | varchar | 50 |  | √ | ' ' | 消息ID |
| 11 | fstartid | 起始单据ID | int8 | 64 |  | √ | 0 | 起始单据ID |
| 12 | ftaskno | 任务号 | varchar | 20 |  | √ | ' ' | 任务号 |
| 13 | fbillfs_view | 单据过条件 | varchar | 2000 |  | √ | ' ' | 单据过条件 |
| 14 | fmsgstart | 消息开始时间 | timestamp | 0 |  |  | null | 消息开始时间 |
| 15 | fruleid | 余额规则 | varchar | 30 |  | √ | ' ' | 余额规则 |
| 16 | ftruecount | 实际重算单据数量 | int4 | 32 |  | √ | 0 | 实际重算单据数量 |
| 17 | ferrormsg_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_bal_recal_log |  | fid |
| 2 | idx_im_recal_log_timeno |  | ftaskno |
