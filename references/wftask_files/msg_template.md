# 消息模板-msg_template

## 适用场景-多选基础资料表 t_msg_selectscene

- **表名称：** 适用场景-多选基础资料表
- **表名：** t_msg_selectscene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 消息场景 msg_tplscene |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_selectscene |  | fid,fbasedataid |
| 2 | t_msg_selectscene_pkey |  | fpkid |

---

## 消息模板-主表 t_msg_template

- **表名称：** 消息模板-主表
- **表名：** t_msg_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fmsgscene | 模板场景编码 | varchar | 300 |  | √ | ' ' | 模板场景编码 |
| 4 | fmsgtype | 适用类型 | varchar | 30 |  | √ | ' ' | 适用类型,枚举: task :任务 message :通知 alarm :报警 warning :预警 |
| 5 | fmsgchannel | 应用于 | varchar | 30 |  | √ | ' ' | 应用于,枚举: email :邮件 sms :短信 yunzhijia :协同云 dingding :钉钉 weixinqy :企业微信 welink :WeLink yunzhijiaeco :生态协同云 yunzhijiaup :协同云统一流程 mcenter :消息中心 |
| 6 | fbizplugin | 业务插件 | varchar | 1000 |  | √ | ' ' | 业务插件 |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmsgentity | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 11 | fcommonlang | 通用语言 | text | 0 |  |  | null | 通用语言 |
| 12 | fmsgtemplate | fmsgtemplate | text | 0 |  |  | null |  |
| 13 | fmsgscenename | 模板场景名称 | varchar | 500 |  | √ | ' ' | 模板场景名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_template_pkey |  | fid |
| 2 | idx_msg_template_msgtype |  | fmsgtype |

---

## 消息模板-多语言表 t_msg_template_l

- **表名称：** 消息模板-多语言表
- **表名：** t_msg_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fmsgscenename | 模板场景名称 | varchar | 500 |  | √ | ' ' | 模板场景名称 |
| 5 | fmsgtemplate | 消息模板 | text | 0 |  |  | null | 消息模板 |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_msg_template_l_pkey |  | fpkid |
| 2 | idx_msg_template_l |  | fid,flocaleid |
