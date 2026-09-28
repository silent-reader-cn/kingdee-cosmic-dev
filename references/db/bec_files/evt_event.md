# 事件定义-evt_event

## 事件定义-多语言表 t_evt_event_l

- **表名称：** 事件定义-多语言表
- **表名：** t_evt_event_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 事件名称 | varchar | 500 |  | √ | ' ' | 事件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 事件描述 | varchar | 1000 |  | √ | ' ' | 事件描述 |
| 5 | foperation | 操作多语言 | varchar | 200 |  | √ | ' ' | 操作多语言 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_evt_event_l_pkey |  | fpkid |
| 2 | idx_evt_event_l |  | fid,flocaleid |

---

## 事件定义-主表 t_evt_event

- **表名称：** 事件定义-主表
- **表名：** t_evt_event

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopernumber | 操作编码 | varchar | 200 |  | √ | ' ' | 操作编码 |
| 3 | fname | 事件名称 | varchar | 100 |  | √ | ' ' | 事件名称 |
| 4 | fispreinsdata | 预制数据 | bpchar | 1 |  | √ | '0' | 预制数据 |
| 5 | fpassoperparam | 传递操作参数 | bpchar | 1 |  | √ | '0' | 传递操作参数 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdescription | 事件描述 | varchar | 1000 |  | √ | ' ' | 事件描述 |
| 8 | fsource | 来源应用 | varchar | 100 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fentity | 业务对象 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 10 | fstatus | 事件启用 | bpchar | 1 |  | √ | '1' | 事件启用,枚举: 0 :禁用 1 :启用 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | ftype | 事件类型 | varchar | 30 |  | √ | ' ' | 事件类型,枚举: cosmic :苍穹操作事件 custom :自定义事件 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fismodified | 可维护 | bpchar | 1 |  | √ | '1' | 可维护 |
| 15 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fscene | 应用场景 | varchar | 30 |  | √ | ' ' | 应用场景,枚举: operate :操作型事件 analyze :分析型事件 |
| 17 | fnumberview | 事件编码 | varchar | 500 |  | √ | ' ' | 事件编码 |
| 18 | fnumber | 事件编码（内部） | varchar | 500 |  | √ | ' ' | 事件编码（内部） |
| 19 | foperation | 操作多语言 | varchar | 100 |  | √ | ' ' | 操作多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_evt_event_pkey |  | fid |
| 2 | idx_evt_event_entity |  | fentity |
| 3 | idx_evt_event_number |  | fnumber |
| 4 | idx_evt_event_opernumber |  | fopernumber |

---

## 事件参数-子表 t_evt_eventconfig

- **表名称：** 事件参数-子表
- **表名：** t_evt_eventconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscustom | 自定义 | bpchar | 1 |  | √ | '1' | 自定义 |
| 3 | fconfigdescription | 类型描述 | varchar | 100 |  | √ | ' ' | 类型描述 |
| 4 | fconfignumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fconfigname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fistransfer | 传递数据 | bpchar | 1 |  | √ | '0' | 传递数据 |
| 9 | fconfigtype | 属性 | varchar | 3000 |  | √ | ' ' | 属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_eventconfig |  | fid |
| 2 | t_evt_eventconfig_pkey |  | fentryid |

---

## 事件参数-多语言表 t_evt_eventconfig_l

- **表名称：** 事件参数-多语言表
- **表名：** t_evt_eventconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconfigdescription | 类型描述 | varchar | 500 |  | √ | ' ' | 类型描述 |
| 3 | fconfigname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_evt_eventconfig_l_pkey |  | fpkid |
| 2 | idx_evt_eventconfig_l |  | fentryid,flocaleid |
