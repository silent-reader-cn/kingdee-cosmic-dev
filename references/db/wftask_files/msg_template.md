# 消息模板-msg_template

## 适用场景-多选基础资料表 t_msg_selectscene

- **表名称：** 适用场景-多选基础资料表
- **表名：** t_msg_selectscene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [消息场景 msg_tplscene](../wftask_files/msg_tplscene.md) |
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
| 2 | fname | 名称 | varchar | 165 |  | √ | ' ' | 名称 |
| 3 | fxkisdefault | 默认模板 | bpchar | 1 |  | √ | '0' | 默认模板 |
| 4 | fmsgscene | 模板场景编码 | varchar | 300 |  | √ | ' ' | 模板场景编码 |
| 5 | fmsgtype | 适用类型 | varchar | 30 |  | √ | ' ' | 适用类型,枚举: task :任务 message :通知 alarm :报警 warning :预警 |
| 6 | fmsgchannel | 消息渠道 | varchar | 30 |  | √ | ' ' | 消息渠道,枚举: email :邮件 sms :短信 yunzhijia :协同云 dingding :钉钉 weixinqy :企业微信 welink :WeLink yunzhijiaeco :生态协同云 yunzhijiaup :协同云统一流程 mcenter :消息中心 |
| 7 | fbizplugin | 业务插件 | varchar | 1000 |  | √ | ' ' | 业务插件 |
| 8 | fxkfiletype | 附件类型 | varchar | 30 |  | √ | ' ' | 附件类型 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmsgentity | 单据名称 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 13 | fcommonlang | 通用语言 | text | 0 |  |  | null | 通用语言 |
| 14 | fmsgtemplate | fmsgtemplate | text | 0 |  |  | null |  |
| 15 | fmsgscenename | 模板场景名称 | varchar | 500 |  | √ | ' ' | 模板场景名称 |

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

## 单据体-子表 t_msg_tmplrecentry

- **表名称：** 单据体-子表
- **表名：** t_msg_tmplrecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fxkcontactsrange | 联系人范围 | varchar | 50 |  | √ | ' ' | 联系人范围,枚举: default :默认联系人 all :所有联系人 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fxkrecipientemail | 电子邮箱 | varchar | 100 |  | √ | ' ' | 电子邮箱 |
| 5 | fxksendingmode | 发送方式 | varchar | 50 |  | √ | ' ' | 发送方式,枚举: normal :收件人 CC :抄送人 BCC :密送人 |
| 6 | fxkrecipientype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: bos_user :用户 bd_supplier :供应商 bd_customer :客户 customize :自定义 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fxkrecipientcontacts | 联系人 | varchar | 100 |  | √ | ' ' | 联系人 |
| 9 | fxkrelatedfield | 关联字段 | varchar | 50 |  | √ | ' ' | 关联字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_tmplrecentry_fk |  | fid |
| 2 | pk_t_msg_tmplrecentry |  | fentryid |

---

## 消息模板-多语言表 t_msg_template_l

- **表名称：** 消息模板-多语言表
- **表名：** t_msg_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 165 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fmsgtemplate | 消息模板 | text | 0 |  |  | null | 消息模板 |
| 5 | fmsgscenename | 模板场景名称 | varchar | 500 |  | √ | ' ' | 模板场景名称 |
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
