# 数据流实例-iscx_data_stream

## 数据流实例-主表 t_iscx_datax_stream

- **表名称：** 数据流实例-主表
- **表名：** t_iscx_datax_stream

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fhost | 服务器 | varchar | 50 |  | √ | ' ' | 服务器 |
| 4 | fexecute_count | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcontext | 上下文环境 | varchar | 255 |  | √ | ' ' | 上下文环境 |
| 7 | fstart_time | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fparams | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 9 | fexecute_time | 执行耗时（秒） | numeric | 19 | 2 | √ | 0 | 执行耗时（秒） |
| 10 | fevent_type | 启动方式 | varchar | 50 |  | √ | ' ' | 启动方式,枚举: EventModel.Manual :人工启动 EventModel.Timer :定时启动 EventModel.BizEvent :单据事件 EventModel.MQ :MQ订阅 EventModel.Poll :轮询事件 EventModel.API :API触发 EventModel.UserDefined :自定义事件 |
| 11 | fcontext_tag | 上下文环境_详情 | text | 0 |  |  | null | 上下文环境_详情 |
| 12 | fmodifytime | 结束 / 修改时间 | timestamp | 0 |  |  | null | 结束 / 修改时间 |
| 13 | fdata_flow_def | 数据流定义ID | int8 | 64 |  | √ | 0 | 数据流定义ID |
| 14 | fstate | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: C :创建 R :执行中 S :结束 F :失败 X :撤销 P :部分成功 H :暂停 B :中断 |
| 15 | fdata_flow_trigger | 数据流启动方案 | int8 | 64 |  | √ | 0 | [数据流启动方案 iscx_data_flow_trigger](../iscx_files/iscx_data_flow_trigger.md) |
| 16 | fparams_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fversion | 版本号 | int8 | 64 |  | √ | 0 | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_datax_stream |  | fid |
| 2 | idx_t_iscx_datax_stream_i |  | fnumber |
