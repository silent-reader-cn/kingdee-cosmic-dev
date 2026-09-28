# 业务异常白名单-evt_whitelist_config

## 业务异常白名单-多语言表 t_evt_subscription_l

- **表名称：** 业务异常白名单-多语言表
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

## 单据体-多语言表 t_evt_whitelist_l

- **表名称：** 单据体-多语言表
- **表名：** t_evt_whitelist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fcontent | 业务异常内容 | varchar | 200 |  | √ | ' ' | 业务异常内容 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_whitelist_l |  | fentryid,flocaleid |
| 2 | pk_evt_whitelist_l |  | fpkid |

---

## 业务异常白名单-主表 t_evt_subscription

- **表名称：** 业务异常白名单-主表
- **表名：** t_evt_subscription

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fispreinsdata | fispreinsdata | bpchar | 1 |  | √ | '0' |  |
| 3 | fisconcurrent | fisconcurrent | bpchar | 1 |  | √ | '1' |  |
| 4 | ferrornotify | ferrornotify | text | 0 |  |  | null |  |
| 5 | fservicenumber | fservicenumber | varchar | 100 |  | √ | ' ' |  |
| 6 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |
| 7 | fstatus | fstatus | bpchar | 1 |  | √ | '1' |  |
| 8 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 9 | fsequence | fsequence | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 11 | fismodified | fismodified | bpchar | 1 |  | √ | '1' |  |
| 12 | fcreater | fcreater | int8 | 64 |  | √ | 0 |  |
| 13 | fexecutorvalue | fexecutorvalue | varchar | 2000 |  | √ | ' ' |  |
| 14 | fcondition | fcondition | text | 0 |  |  | null |  |
| 15 | fevent | fevent | int8 | 64 |  | √ | 0 |  |
| 16 | fname | 订阅名称 | varchar | 500 |  | √ | ' ' | 订阅名称 |
| 17 | fnotifytext | fnotifytext | varchar | 300 |  | √ | ' ' |  |
| 18 | ftimingstrategy | ftimingstrategy | varchar | 100 |  | √ | ' ' |  |
| 19 | fexpression | fexpression | text | 0 |  |  | null |  |
| 20 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 21 | fserviceconfig | fserviceconfig | text | 0 |  |  | null |  |
| 22 | ferrorstrategy | ferrorstrategy | varchar | 30 |  | √ | ' ' |  |
| 23 | fexecutor | fexecutor | varchar | 255 |  | √ | ' ' |  |
| 24 | fservice | fservice | int8 | 64 |  | √ | 0 |  |
| 25 | feventnumber | feventnumber | varchar | 100 |  | √ | ' ' |  |
| 26 | fnumber | 订阅编码 | varchar | 500 |  | √ | ' ' | 订阅编码 |
| 27 | feventsplitconfig | feventsplitconfig | varchar | 1000 |  | √ | ' ' |  |
| 28 | fexecutionstrategy | fexecutionstrategy | varchar | 50 |  | √ | ' ' |  |

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

---

## 单据体-子表 t_evt_whitelist

- **表名称：** 单据体-子表
- **表名：** t_evt_whitelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatus | 是否启用 | varchar | 50 |  | √ | ' ' | 是否启用,枚举: 0 :禁用 1 :启用 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftype | 异常匹配方式 | varchar | 50 |  | √ | ' ' | 异常匹配方式,枚举: 0 :异常编码 1 :异常信息包含的关键字 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcontent | 业务异常内容 | varchar | 200 |  | √ | ' ' | 业务异常内容 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evt_whitelist |  | fentryid |
| 2 | idx_evt_whitelist_status |  | fstatus |
| 3 | idx_evt_whitelist_fid |  | fid |
