# 自动处理策略-evt_rule

## 自动处理策略-主表 t_evt_regulation

- **表名称：** 自动处理策略-主表
- **表名：** t_evt_regulation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftriggertime | 触发时机 | varchar | 50 |  | √ | ' ' | 触发时机,枚举: afterIndicatorCalculate :订阅指标计算完成后 |
| 3 | fparam | 参数集 | varchar | 500 |  | √ | ' ' | 参数集 |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 6 | fdealoption | 处理策略 | varchar | 50 |  | √ | ' ' | 处理策略,枚举: suspendSub :直接挂起 isolateSlowqueue :隔离至慢队列 noRetry :拒绝重试且隔离至慢队列 |
| 7 | fispreset | 来源 | bpchar | 1 |  | √ | '1' | 来源,枚举: 1 :预置 0 :非预置 |
| 8 | fstatus | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 1 :启用 0 :禁用 |
| 9 | ferrorlevel | 处理级别 | bpchar | 2 |  | √ | '0' | 处理级别,枚举: 20 :提醒 30 :警告 40 :异常 |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fscene | 应用场景 | varchar | 50 |  | √ | ' ' | 应用场景,枚举: overtime :执行超时 failureRate :失败率过高 overtimeFailure :超时数量超过阈值限制 |
| 12 | fplugin | 执行插件 | varchar | 500 |  | √ | ' ' | 执行插件 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fexplain | 规则说明 | varchar | 500 |  | √ | ' ' | 规则说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evt_regulation |  | fid |
| 2 | idx_evt_regulation_number |  | fnumber |

---

## 自动处理策略-多语言表 t_evt_regulation_l

- **表名称：** 自动处理策略-多语言表
- **表名：** t_evt_regulation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fexplain | 规则说明 | varchar | 500 |  | √ | ' ' | 规则说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evt_regulation_l |  | fpkid |
| 2 | idx_evt_regulation_l |  | fid,flocaleid |

---

## 屏蔽规则的订阅-子表 t_evt_ruleshieldsubs

- **表名称：** 屏蔽规则的订阅-子表
- **表名：** t_evt_ruleshieldsubs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsubscriptionid | 事件订阅 | int8 | 64 |  | √ | 0 | [事件订阅 evt_subscription](../bec_files/evt_subscription.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_ruleshieldsubs_fid |  | fid |
| 2 | pk_evt_ruleshieldsubs |  | fentryid |
| 3 | idx_evt_ruleshieldsubs_subid |  | fsubscriptionid |
