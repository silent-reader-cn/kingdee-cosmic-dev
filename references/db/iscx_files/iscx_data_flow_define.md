# 数据流已发布定义-iscx_data_flow_define

## 数据流已发布定义-主表 t_iscx_data_flow_define

- **表名称：** 数据流已发布定义-主表
- **表名：** t_iscx_data_flow_define

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 5 | fcrc | CRC校验码 | varchar | 8 |  | √ | ' ' | CRC校验码 |
| 6 | fwork_area_size | 工作区大小 | int8 | 64 |  | √ | 0 | 工作区大小 |
| 7 | fstart_mq_topic | 开始时通知MQ | int8 | 64 |  | √ | 0 | [消息发布主题 isc_mq_publisher](../iscb_files/isc_mq_publisher.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fjob_mutex | 后台任务锁 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 10 | fend_mq_topic | 结束时通知MQ | int8 | 64 |  | √ | 0 | [消息发布主题 isc_mq_publisher](../iscb_files/isc_mq_publisher.md) |
| 11 | flog_level | 日志级别 | varchar | 50 |  | √ | ' ' | 日志级别,枚举: ERROR :错误 ALL :全部 |
| 12 | fmax_threads | 最大线程数 | int8 | 64 |  | √ | 0 | 最大线程数 |
| 13 | fdata_flow | 数据流图 | int8 | 64 |  | √ | 0 | [数据流资源 iscx_resource](../iscx_files/iscx_resource.md) |
| 14 | fmax_retry_times | 最大重试次数 | int8 | 64 |  | √ | 0 | 最大重试次数 |
| 15 | fcheckpoint | 检查点（秒） | int8 | 64 |  | √ | 0 | 检查点（秒） |
| 16 | fdefine_json | 数据流定义Json字符串 | varchar | 255 |  | √ | ' ' | 数据流定义Json字符串 |
| 17 | ffailed_notice | 失败时通知 | int8 | 64 |  | √ | 0 | [数据流资源 iscx_resource](../iscx_files/iscx_resource.md) |
| 18 | fevent_type | 启动方式 | varchar | 50 |  | √ | ' ' | 启动方式,枚举: EventModel.Manual :人工启动 EventModel.Timer :定时启动 EventModel.BizEvent :单据事件 EventModel.MQ :MQ订阅 EventModel.Poll :轮询事件 EventModel.API :API触发 EventModel.UserDefined :自定义事件 |
| 19 | fsuccess_notice | 完成时通知 | int8 | 64 |  | √ | 0 | [数据流资源 iscx_resource](../iscx_files/iscx_resource.md) |
| 20 | fretry_interval | 重试间隔(分钟) | varchar | 50 |  | √ | ' ' | 重试间隔(分钟) |
| 21 | fdata_flow_trigger | 数据流启动方案 | int8 | 64 |  | √ | 0 | [数据流启动方案 iscx_data_flow_trigger](../iscx_files/iscx_data_flow_trigger.md) |
| 22 | fdefine_json_tag | 数据流定义Json字符串_详情 | text | 0 |  |  | null | 数据流定义Json字符串_详情 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_iscx_data_flow_define_i |  | fnumber |
| 2 | pk_t_iscx_data_flow_define |  | fid |
