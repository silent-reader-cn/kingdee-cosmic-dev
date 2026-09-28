# 消息渠道-msg_channel

## 消息渠道-主表 t_msg_channel

- **表名称：** 消息渠道-主表
- **表名：** t_msg_channel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 应用ID | varchar | 100 |  | √ | ' ' | 应用ID |
| 3 | fmobileappconfig | 移动应用配置 | text | 0 |  |  | null | 移动应用配置 |
| 4 | fappsecret | 应用秘钥 | varchar | 500 |  | √ | ' ' | 应用秘钥 |
| 5 | fdomain | 服务器域名 | varchar | 500 |  | √ | ' ' | 服务器域名 |
| 6 | fsmscode | 短信模板 | varchar | 100 |  | √ | ' ' | 短信模板 |
| 7 | fpassword | 密码 | varchar | 200 |  | √ | ' ' | 密码 |
| 8 | fusername | 用户名 | varchar | 100 |  | √ | ' ' | 用户名 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 10 | fconfig | 参数配置 | varchar | 3000 |  | √ | ' ' | 参数配置 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fserviceclass | 实现类 | varchar | 400 |  | √ | ' ' | 实现类 |
| 13 | fcorpid | 企业ID | varchar | 100 |  | √ | ' ' | 企业ID |
| 14 | flogenable | 启用日志 | bpchar | 1 |  | √ | '0' | 启用日志 |
| 15 | ftplprocesscode | 模板唯一码 | varchar | 500 |  | √ | ' ' | 模板唯一码 |
| 16 | ftplname | 模板名称 | varchar | 200 |  | √ | ' ' | 模板名称 |
| 17 | ffromusername | 发件人名称 | varchar | 230 |  | √ | ' ' | 发件人名称 |
| 18 | fmobileapp | 移动应用 | varchar | 30 |  | √ | ' ' | 移动应用,枚举: cloudHub :协同云 dingding :钉钉 weixinqy :企业微信 welink :WeLink other :其他 |
| 19 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 20 | fcategory | 渠道类型 | varchar | 30 |  | √ | ' ' | 渠道类型,枚举: mobileApp :移动应用 shortMsg :短信 email :电子邮件 |
| 21 | fsmtphost | 邮件服务地址 | varchar | 100 |  | √ | ' ' | 邮件服务地址 |
| 22 | fappkey | 应用Key | varchar | 100 |  | √ | ' ' | 应用Key |
| 23 | fclientid | 客户ID | varchar | 100 |  | √ | ' ' | 客户ID |
| 24 | ftls | 使用TLS协议 | bpchar | 1 |  | √ | '0' | 使用TLS协议 |
| 25 | ffromaccount | 发件人账号 | varchar | 100 |  | √ | ' ' | 发件人账号 |
| 26 | fsmsapiurl | 短信接口 | varchar | 400 |  | √ | ' ' | 短信接口 |
| 27 | fclientsecret | 客户密钥 | varchar | 100 |  | √ | ' ' | 客户密钥 |
| 28 | fenable | 启用渠道 | bpchar | 1 |  | √ | '1' | 启用渠道 |
| 29 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 30 | fishasdingtpl | 是否有模板 | bpchar | 1 |  | √ | '0' | 是否有模板 |
| 31 | fsmtpport | 邮件服务端口 | varchar | 100 |  | √ | ' ' | 邮件服务端口 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_channel_pkey |  | fid |
| 2 | idx_msg_channel_number |  | fnumber |

---

## 消息渠道-多语言表 t_msg_channel_l

- **表名称：** 消息渠道-多语言表
- **表名：** t_msg_channel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | ffromusername | 发件人名称 | varchar | 230 |  | √ | ' ' | 发件人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_channel_l_pkey |  | fpkid |
| 2 | idx_msg_channel_localeid |  | fid,flocaleid |
