# 数据流启动方案-iscx_data_flow_trigger

## 数据流启动方案-多语言表 t_iscx_datax_trigger_l

- **表名称：** 数据流启动方案-多语言表
- **表名：** t_iscx_datax_trigger_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_datax_trigger_l_n |  | fid,fname |
| 2 | pk_t_iscx_datax_trigger_l |  | fpkid |

---

## 参数绑定-子表 t_iscx_datax_param

- **表名称：** 参数绑定-子表
- **表名：** t_iscx_datax_param

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam_type | 参数类型 | varchar | 200 |  | √ | ' ' | 参数类型 |
| 3 | fparam_number | 参数编码 | varchar | 150 |  | √ | ' ' | 参数编码 |
| 4 | fparam_desc | 参数备注 | varchar | 250 |  | √ | ' ' | 参数备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparam_name | 参数名称 | varchar | 250 |  | √ | ' ' | 参数名称 |
| 7 | fparam_value | 参数赋值 | varchar | 2000 |  | √ | ' ' | 参数赋值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_datax_param |  | fentryid |
| 2 | idx_t_iscx_datax_param_i |  | fid |

---

## 连接器绑定-子表 t_iscx_datax_connector

- **表名称：** 连接器绑定-子表
- **表名：** t_iscx_datax_connector

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconnector_ref | 连接器 | int8 | 64 |  | √ | 0 | 连接器 iscx_connector |
| 3 | fconnector_type | 连接类型 | varchar | 50 |  | √ | ' ' | 连接类型 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconnector_number | 连接编码 | varchar | 50 |  | √ | ' ' | 连接编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fconnector_name | 连接名称 | varchar | 50 |  | √ | ' ' | 连接名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_iscx_datax_connector_i |  | fid |
| 2 | pk_t_iscx_datax_connector |  | fentryid |

---

## 数据流启动方案-主表 t_iscx_datax_trigger

- **表名称：** 数据流启动方案-主表
- **表名：** t_iscx_datax_trigger

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcrc | CRC校验码 | varchar | 8 |  | √ | ' ' | CRC校验码 |
| 4 | fstart_mq_topic | 开始时通知MQ | int8 | 64 |  | √ | 0 | 消息发布主题 isc_mq_publisher |
| 5 | fend_mq_topic | 结束时通知MQ | int8 | 64 |  | √ | 0 | 消息发布主题 isc_mq_publisher |
| 6 | flog_level | 日志级别 | varchar | 50 |  | √ | ' ' | 日志级别,枚举: ERROR :错误 ALL :全部 |
| 7 | fmax_threads | 最大线程数 | int8 | 64 |  | √ | 0 | 最大线程数 |
| 8 | fcheckpoint | 检查点（秒） | int8 | 64 |  | √ | 0 | 检查点（秒） |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsuccess_notice | 完成时通知 | int8 | 64 |  | √ | 0 | 数据流资源 iscx_resource |
| 11 | fversion | 当前版本号 | int8 | 64 |  | √ | 0 | 当前版本号 |
| 12 | fevent_model | 启动事件 | int8 | 64 |  | √ | 0 | 数据流资源 iscx_resource |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fevent | fevent | int8 | 64 |  | √ | 0 |  |
| 15 | fname | 名称 | varchar | 150 |  | √ | ' ' | 名称 |
| 16 | fwork_area_size | 工作区大小 | int8 | 64 |  | √ | 0 | 工作区大小 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fjob_mutex | 后台任务锁 | int8 | 64 |  | √ | 0 | 后台任务组 isc_job_mutex |
| 19 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdata_flow | 数据流 | int8 | 64 |  | √ | 0 | 数据流资源 iscx_resource |
| 21 | fmax_retry_times | 失败重试次数 | int8 | 64 |  | √ | 0 | 失败重试次数 |
| 22 | fmq_topic_id | 消息订阅主题 | int8 | 64 |  | √ | 0 | 消息订阅主题 isc_mq_subscriber |
| 23 | ffailed_notice | 失败时通知 | int8 | 64 |  | √ | 0 | 数据流资源 iscx_resource |
| 24 | fevent_type | 启动方式 | varchar | 50 |  | √ | ' ' | 启动方式,枚举: EventModel.Manual :人工启动 EventModel.Timer :定时启动 EventModel.BizEvent :单据事件 EventModel.MQ :MQ订阅 EventModel.Poll :轮询事件 EventModel.API :API触发 EventModel.UserDefined :自定义事件 |
| 25 | fretry_interval | 重试间隔(分钟) | varchar | 50 |  | √ | ' ' | 重试间隔(分钟) |
| 26 | fenable | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 27 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_iscx_datax_trigger_i |  | fnumber |
| 2 | pk_t_iscx_datax_trigger |  | fid |
