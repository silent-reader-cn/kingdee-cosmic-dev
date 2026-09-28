# 异常订阅-evt_abnormalsubs

## 异常订阅-主表 t_evt_abnormalsubs

- **表名称：** 异常订阅-主表
- **表名：** t_evt_abnormalsubs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人ID | int8 | 64 |  | √ | 0 | 创建人ID |
| 3 | feventid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 4 | fcreatorname | 创建人名称 | varchar | 200 |  | √ | ' ' | 创建人名称 |
| 5 | fregularid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 6 | fdealoption | 执行操作 | varchar | 50 |  | √ | ' ' | 执行操作,枚举: suspendSub :直接挂起 isolateSlowqueue :隔离至慢队列 noRetry :拒绝重试且隔离至慢队列 |
| 7 | fsubscriptionnumber | 订阅编码 | varchar | 500 |  | √ | ' ' | 订阅编码 |
| 8 | fsubscriptionid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |
| 9 | frelievedate | 解除时间 | timestamp | 0 |  |  | null | 解除时间 |
| 10 | feventname | 事件名称 | varchar | 500 |  | √ | ' ' | 事件名称 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | frelievetype | 解除方式 | varchar | 50 |  | √ | ' ' | 解除方式,枚举: auto :自动解除 manual :人工解除 |
| 13 | fsubscriptionname | 订阅名称 | varchar | 500 |  | √ | ' ' | 订阅名称 |
| 14 | ferrorlevel | 处理级别 | bpchar | 2 |  | √ | '0' | 处理级别,枚举: 20 :提醒 30 :警告 40 :视为异常 |
| 15 | feventnumber | 事件编码 | varchar | 500 |  | √ | ' ' | 事件编码 |
| 16 | foperatetype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: auto :自动 manual :手动 |
| 17 | freliever | 解除人ID | int8 | 64 |  | √ | 0 | 解除人ID |
| 18 | fscene | 应用场景 | varchar | 50 |  | √ | ' ' | 应用场景,枚举: overtime :执行超时 failureRate :失败率过高 |
| 19 | fsubstate | 订阅状态 | bpchar | 1 |  | √ | ' ' | 订阅状态,枚举: 1 :已挂起 0 :执行中 2 :解挂中 |
| 20 | fexplain | 异常原因 | varchar | 2000 |  | √ | ' ' | 异常原因 |
| 21 | frelievername | 解除人名称 | varchar | 200 |  | √ | ' ' | 解除人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_evt_abnsubs_createdate |  | fcreatedate |
| 2 | idx_evt_abnsubs_subsnumber |  | fsubscriptionnumber |
| 3 | idx_evt_abnsubs_subsid |  | fsubscriptionid |
| 4 | pk_evt_abnormalsubs |  | fid |

---

## 异常订阅-多语言表 t_evt_abnormalsubs_l

- **表名称：** 异常订阅-多语言表
- **表名：** t_evt_abnormalsubs_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feventname | 事件名称 | varchar | 500 |  | √ | ' ' | 事件名称 |
| 3 | fsubscriptionname | 订阅名称 | varchar | 500 |  | √ | ' ' | 订阅名称 |
| 4 | fcreatorname | 创建人名称 | varchar | 200 |  | √ | ' ' | 创建人名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fexplain | 异常原因 | varchar | 2000 |  | √ | ' ' | 异常原因 |
| 8 | frelievername | 解除人名称 | varchar | 200 |  | √ | ' ' | 解除人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_evt_abnormalsubs_l |  | fpkid |
| 2 | idx_evt_abnormalsubs_l |  | fid,flocaleid |
