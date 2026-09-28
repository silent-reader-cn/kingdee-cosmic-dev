# 事件日志统计-evt_jobstatistics

## 事件日志统计-多语言表 t_evt_jobstatistics_l

- **表名称：** 事件日志统计-多语言表
- **表名：** t_evt_jobstatistics_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 136 |  | √ | ' ' | 实体名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_evt_jobstatistics_l |  | fpkid |
| 2 | idx_evt_jobstatistics_l |  | fid,flocaleid |

---

## 事件日志统计-主表 t_evt_jobstatistics

- **表名称：** 事件日志统计-主表
- **表名：** t_evt_jobstatistics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevent | 事件 | int8 | 64 |  | √ | 0 | 事件定义 evt_event |
| 3 | fjobstate | job状态 | varchar | 50 |  | √ | ' ' | job状态 |
| 4 | fjobcurrentcount | job当前数量 | int4 | 32 |  | √ | 0 | job当前数量 |
| 5 | feventnumberview | 事件编码（内部） | varchar | 500 |  | √ | ' ' | 事件编码（内部） |
| 6 | fhandlertype | 服务类型 | varchar | 50 |  | √ | ' ' | 服务类型 |
| 7 | fsubscription | 订阅 | int8 | 64 |  | √ | 0 | 事件订阅 evt_subscription |
| 8 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 9 | ftotalduration | 总耗时 | int8 | 64 |  | √ | 0 | 总耗时 |
| 10 | fsubscriptionnumber | 订阅编码 | varchar | 500 |  | √ | ' ' | 订阅编码 |
| 11 | fservicenumber | 服务编码 | varchar | 500 |  | √ | ' ' | 服务编码 |
| 12 | fentityname | 实体名称 | varchar | 136 |  | √ | ' ' | 实体名称 |
| 13 | feventnumber | 事件编码 | varchar | 500 |  | √ | ' ' | 事件编码 |
| 14 | fservice | 服务 | int8 | 64 |  | √ | 0 | 服务目录 evt_service |
| 15 | fyears | 年月 | varchar | 10 |  | √ | ' ' | 年月 |
| 16 | fjobhistorycount | job历史数量 | int4 | 32 |  | √ | 0 | job历史数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_jobstati_event |  | fevent |
| 2 | idx_evt_jobstati_handler |  | fhandlertype |
| 3 | idx_evt_jobstati_subscription |  | fsubscription |
| 4 | pk_t_evt_jobstatistics |  | fid |
| 5 | idx_evt_jobstati_years |  | fyears |
| 6 | idx_evt_jobstati_service |  | fservice |
