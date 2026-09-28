# 事件订阅-evt_subscription

## 事件订阅-多语言表 t_evt_subscription_l

- **表名称：** 事件订阅-多语言表
- **表名：** t_evt_subscription_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 订阅名称 | varchar | 500 |  | √ | ' ' | 订阅名称 |
| 3 | fnotifytext | fnotifytext | varchar | 300 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_subscription_l |  | fid,flocaleid |
| 2 | t_evt_subscription_l_pkey |  | fpkid |

---

## 事件订阅-主表 t_evt_subscription

- **表名称：** 事件订阅-主表
- **表名：** t_evt_subscription

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispreinsdata | 预制数据 | bpchar | 1 |  | √ | '0' | 预制数据 |
| 3 | fisconcurrent | 并发执行 | bpchar | 1 |  | √ | '1' | 并发执行 |
| 4 | ferrornotify | 失败时通知人员 | text | 0 |  |  | null | 失败时通知人员 |
| 5 | fservicenumber | 服务编码 | varchar | 100 |  | √ | ' ' | 服务编码 |
| 6 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |
| 7 | fstatus | 订阅启用 | bpchar | 1 |  | √ | '1' | 订阅启用,枚举: 0 :禁用 1 :启用 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fsequence | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fismodified | 可维护 | bpchar | 1 |  | √ | '1' | 可维护 |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fexecutorvalue | 操作执行人 | varchar | 2000 |  | √ | ' ' | 操作执行人 |
| 14 | fcondition | 触发条件 | text | 0 |  |  | null | 触发条件 |
| 15 | fevent | 绑定事件 | int8 | 64 |  | √ | 0 | 事件定义 evt_event |
| 16 | fname | 订阅名称 | varchar | 100 |  | √ | ' ' | 订阅名称 |
| 17 | fnotifytext | 失败时通知 | varchar | 100 |  | √ | ' ' | 失败时通知 |
| 18 | ftimingstrategy | 定时策略 | varchar | 100 |  | √ | ' ' | 定时策略 |
| 19 | fexpression | 执行条件 | text | 0 |  |  | null | 执行条件 |
| 20 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fserviceconfig | 服务参数 | text | 0 |  |  | null | 服务参数 |
| 22 | ferrorstrategy | 错误处理策略 | varchar | 30 |  | √ | ' ' | 错误处理策略,枚举: retry :重试三次挂起 ignore :直接挂起 donothing :忽略异常 |
| 23 | fexecutor | 服务执行人 | varchar | 255 |  | √ | ' ' | 服务执行人 |
| 24 | fservice | 执行服务 | int8 | 64 |  | √ | 0 | 服务目录 evt_service |
| 25 | feventnumber | 事件编码 | varchar | 100 |  | √ | ' ' | 事件编码 |
| 26 | fnumber | 订阅编码 | varchar | 500 |  | √ | ' ' | 订阅编码 |
| 27 | feventsplitconfig | 事件拆分配置 | varchar | 1000 |  | √ | ' ' | 事件拆分配置 |
| 28 | fexecutionstrategy | 执行策略（拆分或合并） | varchar | 50 |  | √ | ' ' | 执行策略（拆分或合并） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_subscr_servnumber |  | fservicenumber |
| 2 | idx_evt_subscr_evtnumber |  | feventnumber |
| 3 | idx_evt_subscr_service |  | fservice |
| 4 | t_evt_subscription_pkey |  | fid |
| 5 | idx_evt_subscr_event |  | fevent |
