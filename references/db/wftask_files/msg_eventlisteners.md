# 消息监听事件-msg_eventlisteners

## 消息监听事件-多语言表 t_msg_eventlisteners_l

- **表名称：** 消息监听事件-多语言表
- **表名：** t_msg_eventlisteners_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 业务对象名称 | varchar | 100 |  | √ | ' ' | 业务对象名称 |
| 3 | fmsgtypename | 消息类型名称 | varchar | 50 |  | √ | ' ' | 消息类型名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_eventlisteners_l |  | fid,flocaleid |
| 2 | t_msg_eventlisteners_l_pkey |  | fpkid |

---

## 消息监听事件-主表 t_msg_eventlisteners

- **表名称：** 消息监听事件-主表
- **表名：** t_msg_eventlisteners

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 业务对象名称 | varchar | 100 |  | √ | ' ' | 业务对象名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fentitynumber | 业务对象编码 | varchar | 100 |  | √ | ' ' | 业务对象编码 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmsgtypename | 消息类型名称 | varchar | 50 |  | √ | ' ' | 消息类型名称 |
| 9 | fmsgtype | 消息类型编码 | varchar | 100 |  | √ | ' ' | 消息类型编码 |
| 10 | fdata | 事件数据 | text | 0 |  |  | null | 事件数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_eventlisteners |  | fentitynumber,fmsgtype |
| 2 | t_msg_eventlisteners_pkey |  | fid |
