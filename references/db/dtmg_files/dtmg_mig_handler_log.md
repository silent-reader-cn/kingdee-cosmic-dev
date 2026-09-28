# 数据迁移后置器日志-dtmg_mig_handler_log

## 数据迁移后置器日志-主表 t_dtmg_mighandlerlog

- **表名称：** 数据迁移后置器日志-主表
- **表名：** t_dtmg_mighandlerlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flog_tag | 详情 | text | 0 |  |  | null | 详情 |
| 3 | fsubnumber | 转换关系编码 | varchar | 30 |  | √ | ' ' | 转换关系编码 |
| 4 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | ftaskid | 迁移任务 | int8 | 64 |  | √ | 0 | [迁移任务基础资料 dtmg_mig_task_base](../dtmg_files/dtmg_mig_task_base.md) |
| 6 | fserviceinfo | 微服务信息 | varchar | 255 |  | √ | ' ' | 微服务信息 |
| 7 | fbillno | 日志编码 | varchar | 100 |  | √ | ' ' | 日志编码 |
| 8 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | flog |  | varchar | 255 |  | √ | ' ' |  |
| 10 | fhandleduring | 耗时(S) | int4 | 32 |  | √ | 0 | 耗时(S) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dtmg_mighandlerlog |  | fid |
| 2 | idx_dtmg_mighandlerlog_bill |  | fbillno |
