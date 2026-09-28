# 消息服务配置-msg_srvcfg

## 消息服务配置-主表 t_msg_srvcfg

- **表名称：** 消息服务配置-主表
- **表名：** t_msg_srvcfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpubaccapiurl | 公共号接口 | varchar | 255 |  | √ | ' ' | 公共号接口 |
| 3 | fsmtphost | 发送服务地址 | varchar | 255 |  | √ | ' ' | 发送服务地址 |
| 4 | fclientid | 客户ID | varchar | 255 |  | √ | ' ' | 客户ID |
| 5 | ffromaccount | 发送账号 | varchar | 255 |  | √ | ' ' | 发送账号 |
| 6 | fsmsapiurl | 短信接口 | varchar | 255 |  | √ | ' ' | 短信接口 |
| 7 | fsmscode | 短信模板 | varchar | 255 |  | √ | ' ' | 短信模板 |
| 8 | fpassword | 密码 | varchar | 255 |  | √ | ' ' | 密码 |
| 9 | fclientsecret | 客户密钥 | varchar | 255 |  | √ | ' ' | 客户密钥 |
| 10 | fconsumer | 消息消费器 | varchar | 255 |  | √ | ' ' | 消息消费器 |
| 11 | fusername | 用户名 | varchar | 255 |  | √ | ' ' | 用户名 |
| 12 | fsmtpport | 发送服务端口 | varchar | 10 |  | √ | ' ' | 发送服务端口 |
| 13 | ffromusername | 发送用户名 | varchar | 255 |  | √ | ' ' | 发送用户名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_srvcfg_pkey |  | fid |
| 2 | idx_msg_srvcfg_host |  | fsmtphost |

---

## 消息服务配置-多语言表 t_msg_srvcfg_l

- **表名称：** 消息服务配置-多语言表
- **表名：** t_msg_srvcfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | ffromusername | 发送用户名 | varchar | 255 |  | √ | ' ' | 发送用户名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msg_srvcfg_l_fid |  | fid,flocaleid |
| 2 | t_msg_srvcfg_l_pkey |  | fpkid |
