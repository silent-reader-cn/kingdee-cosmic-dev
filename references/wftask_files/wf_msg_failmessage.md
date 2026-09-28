# 消息日志-wf_msg_failmessage

## 消息日志-主表 t_wf_msgfail

- **表名称：** 消息日志-主表
- **表名：** t_wf_msgfail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelname | 消息渠道名称 | varchar | 200 |  | √ | ' ' | 消息渠道名称 |
| 3 | ftoall | 全员消息 | bpchar | 1 |  | √ | '0' | 全员消息 |
| 4 | fretry | 重发次数 | int8 | 64 |  | √ | 0 | 重发次数 |
| 5 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 6 | fpubaccnumber | 公共号编码 | varchar | 100 |  | √ | ' ' | 公共号编码 |
| 7 | freason | 消息失败描述 | text | 0 |  |  | null | 消息失败描述 |
| 8 | fruntimeconfig | 运行期参数集合 | text | 0 |  |  | null | 运行期参数集合 |
| 9 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 10 | fentityname | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 11 | fmessageid | 消息关联ID | int8 | 64 |  | √ | 0 | 消息关联ID |
| 12 | fstate | 消息状态 | varchar | 100 |  | √ | ' ' | 消息状态,枚举: normal :队列堆积 success :推送成功 fail :推送失败 intervene :业务干预 dealfail :标记已读失败 |
| 13 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | fconfig | 参数集合 | varchar | 2000 |  | √ | ' ' | 参数集合 |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fuserids | 消息接收人ID集合 | text | 0 |  |  | null | 消息接收人ID集合 |
| 17 | ftplscene | 消息模板场景 | varchar | 100 |  | √ | ' ' | 消息模板场景 |
| 18 | fserviceclass | 渠道处理类 | varchar | 200 |  | √ | ' ' | 渠道处理类 |
| 19 | fchannelcontent | fchannelcontent | text | 0 |  |  | null |  |
| 20 | fchannel | 渠道编码 | varchar | 100 |  | √ | ' ' | 渠道编码 |
| 21 | ftemplate | 适用模板 | varchar | 100 |  | √ | ' ' | 适用模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_msgfail_msgid |  | fmessageid |
| 2 | idx_wf_msgfail_datechlstate |  | fcreatedate,fchannel,fstate |
| 3 | idx_wf_msgfail_datestatetry |  | fmodifydate,fstate,fretry |
| 4 | t_wf_msgfail_pkey |  | fid |

---

## 消息日志-多语言表 t_wf_msgfail_l

- **表名称：** 消息日志-多语言表
- **表名：** t_wf_msgfail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 3 | fentityname | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 4 | fchannelname | 消息渠道名称 | varchar | 200 |  | √ | ' ' | 消息渠道名称 |
| 5 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 6 | fchannelcontent | 内容 | text | 0 |  |  | null | 内容 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_msgfail_l |  | fid,flocaleid |
| 2 | idx_wf_msgfail_l_cname |  | fchannelname |
| 3 | t_wf_msgfail_l_pkey |  | fpkid |
