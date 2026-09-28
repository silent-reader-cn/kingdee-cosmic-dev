# MQ消息服务Old-isc_mq

## 生产者扩展信息-子表 t_isc_mq_extend

- **表名称：** 生产者扩展信息-子表
- **表名：** t_isc_mq_extend

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextvalue | 值 | varchar | 100 |  | √ | ' ' | 值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fextname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_mq_ext_fid |  | fid |
| 2 | t_isc_mq_extend_pkey |  | fentryid |

---

## MQ消息服务Old-主表 t_isc_mq

- **表名称：** MQ消息服务Old-主表
- **表名：** t_isc_mq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconnection | MQ服务器 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 3 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 4 | fenablemq | 单据状态 | int8 | 64 |  | √ | 1 | 单据状态,枚举: 0 :禁用 1 :启用 |
| 5 | fmqtype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: rabbitmq :RabbitMQ |
| 6 | fdocksystem | 对接系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_mq_fnum |  | fnumber |
| 2 | t_isc_mq_pkey |  | fid |

---

## 自动订阅信息-子表 t_isc_mq_autocallback

- **表名称：** 自动订阅信息-子表
- **表名：** t_isc_mq_autocallback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconsumerclass | 消费者类 | varchar | 300 |  | √ | ' ' | 消费者类 |
| 3 | fqueuename | 队列名 | varchar | 100 |  | √ | ' ' | 队列名 |
| 4 | fmqqueue | 对应中间件的队列名称 | varchar | 300 |  | √ | ' ' | 对应中间件的队列名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fregion | 分类 | varchar | 100 |  | √ | ' ' | 分类 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_mq_acallb_fid |  | fid |
| 2 | t_isc_mq_autocallback_pkey |  | fentryid |

---

## 生产者扩展信息-多语言表 t_isc_mq_extend_l

- **表名称：** 生产者扩展信息-多语言表
- **表名：** t_isc_mq_extend_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fextalias | 别名 | varchar | 100 |  | √ | ' ' | 别名 |
| 2 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_mq_extend_l_pkey |  | fpkid |
| 2 | idx_isc_mq_ext_l_fentid |  | fentryid,flocaleid |

---

## 消费者信息-子表 t_isc_mq_consumer

- **表名称：** 消费者信息-子表
- **表名：** t_isc_mq_consumer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconsumerclass | 消费者类 | varchar | 300 |  | √ | ' ' | 消费者类 |
| 3 | fautocallback | 自动反馈 | int8 | 64 |  | √ | 1 | 自动反馈 |
| 4 | fqueuename | 队列名 | varchar | 100 |  | √ | ' ' | 队列名 |
| 5 | fthreadcount | 并发数 | int8 | 64 |  | √ | 0 | 并发数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fregion | 分类 | varchar | 100 |  | √ | ' ' | 分类 |
| 8 | fenable | 已生效 | int8 | 64 |  | √ | 1 | 已生效 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_mq_consumer_pkey |  | fentryid |
| 2 | indx_isc_mq_cons_fid |  | fid |

---

## MQ消息服务Old-多语言表 t_isc_mq_l

- **表名称：** MQ消息服务Old-多语言表
- **表名：** t_isc_mq_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_mq_l_fid |  | fid,flocaleid |
| 2 | t_isc_mq_l_pkey |  | fpkid |
