# 消息类型-msg_type

## 消息类型-主表 t_msg_type

- **表名称：** 消息类型-主表
- **表名：** t_msg_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | fcategory | 分类 | varchar | 30 |  | √ | ' ' | 分类,枚举: task :任务 notice :警告通知 message :普通消息 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fchannelname | 消息渠道名称 | varchar | 230 |  | √ | ' ' | 消息渠道名称 |
| 6 | fispreinsdata | 是否预置场景 | bpchar | 1 |  | √ | '1' | 是否预置场景 |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 9 | fdesc | 类型说明 | varchar | 500 |  | √ | ' ' | 类型说明 |
| 10 | fchannels | 发送渠道 | varchar | 300 |  | √ | ' ' | 发送渠道,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_type_pkey |  | fid |
| 2 | idx_msg_type_number |  | fnumber |

---

## 消息类型-多语言表 t_msg_type_l

- **表名称：** 消息类型-多语言表
- **表名：** t_msg_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | fchannelname | 消息渠道名称 | varchar | 230 |  | √ | ' ' | 消息渠道名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdesc | 类型说明 | varchar | 500 |  | √ | ' ' | 类型说明 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_type_localeid |  | fid,flocaleid |
| 2 | t_msg_type_l_pkey |  | fpkid |
