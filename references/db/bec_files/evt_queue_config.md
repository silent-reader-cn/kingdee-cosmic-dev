# 队列资源管理-evt_queue_config

## 单据体-子表 t_evt_queueconfigdetail

- **表名称：** 单据体-子表
- **表名：** t_evt_queueconfigdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventid | 事件 | int8 | 64 |  | √ | 0 | [事件定义 evt_event](../bec_files/evt_event.md) |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fsourcetype | 来源 | varchar | 20 |  | √ | ' ' | 来源 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evt_queueconfigdetail |  | fentryid |
| 2 | idx_evt_queuecfgdetail_evtid |  | feventid |
| 3 | idx_evt_queuecfgdetail_fid |  | fid |

---

## 队列资源管理-多语言表 t_evt_queueconfig_l

- **表名称：** 队列资源管理-多语言表
- **表名：** t_evt_queueconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 队列名称 | varchar | 200 |  | √ | ' ' | 队列名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evt_queueconfig_l |  | fpkid |
| 2 | idx_evt_queueconfig_l |  | fid,flocaleid |

---

## 队列资源管理-主表 t_evt_queueconfig

- **表名称：** 队列资源管理-主表
- **表名：** t_evt_queueconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 队列名称 | varchar | 200 |  | √ | ' ' | 队列名称 |
| 3 | ftype | 队列类型 | varchar | 30 |  | √ | ' ' | 队列类型,枚举: urgent :快队列 slow :慢队列 simple :普通队列 |
| 4 | fnumber | 队列编码 | varchar | 200 |  | √ | ' ' | 队列编码 |
| 5 | fappnum | app编码 | varchar | 50 |  | √ | ' ' | app编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_queueconfig_number |  | fnumber |
| 2 | pk_evt_queueconfig |  | fid |
