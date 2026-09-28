# 消息队列服务器-isc_mq_server

## 消息队列服务器-多语言表 t_iscb_mq_server_l

- **表名称：** 消息队列服务器-多语言表
- **表名：** t_iscb_mq_server_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_mq_server_l_pkey |  | fpkid |
| 2 | idx_iscb_mq_server_l |  | fid,fname |

---

## 消息队列服务器-主表 t_iscb_mq_server

- **表名称：** 消息队列服务器-主表
- **表名：** t_iscb_mq_server

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserver_ip | 服务器IP | varchar | 100 |  | √ | ' ' | 服务器IP |
| 3 | fvhost | 虚拟主机 | varchar | 100 |  | √ | ' ' | 虚拟主机 |
| 4 | fbootstrap_servers | 连接地址 | varchar | 500 |  | √ | ' ' | 连接地址 |
| 5 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmechanism_protocol | 协议机制 | varchar | 50 |  | √ | ' ' | 协议机制,枚举: PLAIN :PLAIN SCRAM-SHA-256 :SCRAM-SHA-256 SCRAM-SHA-512 :SCRAM-SHA-512 OAUTHBEARER :OAUTHBEARER GSSAPI :GSSAPI |
| 9 | fencrypt_transport | 加密传输 | bpchar | 1 |  | √ | '0' | 加密传输 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcustom_config | 自定义参数配置 | varchar | 1000 |  | √ | ' ' | 自定义参数配置 |
| 13 | fserver_port | 服务器端口 | int8 | 64 |  | √ | 0 | 服务器端口 |
| 14 | flicense_info | 许可状态 | varchar | 20 |  | √ | ' ' | 许可状态,枚举: free :默认免费 yes :正常 no :许可不足 expired :许可失效 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fpull_interval | 消息拉取频率 | int4 | 32 |  |  | null | 消息拉取频率 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fuser | 用户 | varchar | 100 |  | √ | ' ' | 用户 |
| 19 | fpassword_enp | fpassword_enp | text | 0 |  |  | null |  |
| 20 | flicense_sn | 许可序号 | int8 | 64 |  | √ | 0 | 许可序号 |
| 21 | ftype | 服务器类型 | varchar | 30 |  | √ | ' ' | 服务器类型,枚举: InternalRabbit :内部RabbitMQ ExternalRabbit :外部RabbitMQ ExternalKafka :外部Kafka ExternalRocket :外部RocketMQ ExternalMqs :华为MQS ExternalActive :外部ActiveMQ ExternalMsmq :外部MSMQ |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 24 | fcurrent_account_id | 所属账套ID | varchar | 100 |  | √ | ' ' | 所属账套ID |
| 25 | fsecurity_protocol | 安全协议 | varchar | 50 |  | √ | ' ' | 安全协议,枚举: SASL_PLAINTEXT :SASL_PLAINTEXT SASL_SSL :SASL_SSL |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mq_server |  | fnumber |
| 2 | t_iscb_mq_server_pkey |  | fid |
| 3 | idx_iscb_mq_server_ip |  | fserver_ip,fserver_port,fvhost,fbootstrap_servers |
