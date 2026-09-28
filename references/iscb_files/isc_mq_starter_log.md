# 内部MQ日志-isc_mq_starter_log

## 内部MQ日志-主表 t_isc_mq_starter_log

- **表名称：** 内部MQ日志-主表
- **表名：** t_isc_mq_starter_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 接收消息 | varchar | 255 |  | √ | ' ' | 接收消息 |
| 3 | fboid | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 4 | ffunction | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型,枚举: START_SERVICE_PROCESS :启动服务流程 START_DATA_COPY :启动数据集成 INVOKE_EXTERNAL_API :调用外部API INVOKE_SCRIPT_API :调用自定义API |
| 5 | fdetail_tag | 详细信息_详情 | text | 0 |  |  | null | 详细信息_详情 |
| 6 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 7 | fentity | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 8 | fmessageid | 消息ID | varchar | 50 |  | √ | ' ' | 消息ID |
| 9 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: S :已处理 F :失败 N :忽略 |
| 10 | fdetail | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 11 | freceived_time | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |
| 12 | fnumber | 接口编码 | varchar | 100 |  | √ | ' ' | 接口编码 |
| 13 | foperation | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 14 | fmessage_tag | 接收消息_详情 | text | 0 |  |  | null | 接收消息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_mq_starter_log |  | fnumber |
| 2 | pk_isc_mq_starter_log |  | fid |
