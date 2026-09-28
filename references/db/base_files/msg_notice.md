# 消息公告-msg_notice

## 消息公告-多语言表 t_msg_notice_l

- **表名称：** 消息公告-多语言表
- **表名：** t_msg_notice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 消息标题 | varchar | 255 |  | √ | ' ' | 消息标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fxkabstract | 消息概要 | varchar | 500 |  | √ | ' ' | 消息概要 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_notice_l |  | fpkid |
| 2 | idx_t_msg_notice_l_fid |  | fid,flocaleid |

---

## 消息公告-主表 t_msg_notice

- **表名称：** 消息公告-主表
- **表名：** t_msg_notice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fxkispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fmsgchannelid | 消息渠道 | int8 | 64 |  | √ | 0 | 消息渠道 msg_channel |
| 5 | ftoall | 全员推送 | bpchar | 1 |  | √ | '0' | 全员推送 |
| 6 | fxklink | 链接地址 | varchar | 2000 |  | √ | ' ' | 链接地址 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fvalidtime | 有效时间（分钟） | int8 | 64 |  | √ | 0 | 有效时间（分钟） |
| 9 | fmsgtypeid | 消息类型 | int8 | 64 |  | √ | 0 | 消息类型 msg_type |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmessageid | 消息id | int8 | 64 |  | √ | 0 | 消息id |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcontent_tag | 消息正文_详情 | text | 0 |  |  | ' ' | 消息正文_详情 |
| 14 | fsendtime | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 15 | fxkimage | 消息图片 | varchar | 255 |  | √ | ' ' | 消息图片 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fsendstatus | 发送状态 | varchar | 30 |  | √ | ' ' | 发送状态,枚举: 1 :未发送 2 :已发送 3 :已撤回 |
| 18 | fcontent | 消息正文 | text | 0 |  |  | ' ' | 消息正文 |
| 19 | fshowtype | 展现形式 | varchar | 30 |  | √ | ' ' | 展现形式,枚举: 1 :弹窗展示 2 :悬浮窗展示 3 :列表提示 10 :首页企业公告卡片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_notice |  | fid |
| 2 | idx_msg_notice_number |  | fnumber |

---

## 人员类型-多选基础资料表 t_msg_usertype

- **表名称：** 人员类型-多选基础资料表
- **表名：** t_msg_usertype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员类型 bos_usertype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_usertype |  | fpkid |
| 2 | idx_msg_usertype_id |  | fid |

---

## 人员-多选基础资料表 t_msg_user

- **表名称：** 人员-多选基础资料表
- **表名：** t_msg_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_user_id |  | fid |
| 2 | pk_t_msg_user |  | fpkid |

---

## 行政组织-多选基础资料表 t_msg_adminorg

- **表名称：** 行政组织-多选基础资料表
- **表名：** t_msg_adminorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_adminorg |  | fpkid |
| 2 | idx_msg_adminorg_id |  | fid |
