# 历史消息日志-wf_msg_hifailmessage

## 历史消息日志-主表 t_wf_himsgfail

- **表名称：** 历史消息日志-主表
- **表名：** t_wf_himsgfail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannelname | 消息渠道名称 | varchar | 200 |  | √ | ' ' | 消息渠道名称 |
| 3 | ftoall | 全员消息 | bpchar | 1 |  | √ | '0' | 全员消息 |
| 4 | fretry | 重发次数 | int4 | 32 |  | √ | 0 | 重发次数 |
| 5 | fsendername | 发送人名称 | varchar | 100 |  | √ | ' ' | 发送人名称 |
| 6 | fpubaccnumber | 公共号编码 | varchar | 100 |  | √ | ' ' | 公共号编码 |
| 7 | fdeletereason | 删除原因 | varchar | 50 |  | √ | ' ' | 删除原因 |
| 8 | freason | 消息失败描述 | text | 0 |  |  | null | 消息失败描述 |
| 9 | fdeletedate | 删除日期 | timestamp | 0 |  |  | null | 删除日期 |
| 10 | fruntimeconfig | 运行期参数集合 | text | 0 |  |  | null | 运行期参数集合 |
| 11 | ftitle | 标题 | varchar | 500 |  | √ | ' ' | 标题 |
| 12 | fentityname | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 13 | fmessageid | 消息关联ID | int8 | 64 |  | √ | 0 | 消息关联ID |
| 14 | fstate | 消息状态 | varchar | 100 |  | √ | ' ' | 消息状态,枚举: normal :队列堆积 success :推送成功 fail :推送失败 intervene :业务干预 dealfail :标记已读失败 |
| 15 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fconfig | 参数集合 | varchar | 2000 |  | √ | ' ' | 参数集合 |
| 17 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fuserids | 消息接收人ID集合 | text | 0 |  |  | null | 消息接收人ID集合 |
| 19 | ftplscene | 消息模板场景 | varchar | 100 |  | √ | ' ' | 消息模板场景 |
| 20 | fserviceclass | 渠道处理类 | varchar | 200 |  | √ | ' ' | 渠道处理类 |
| 21 | fchannelcontent | fchannelcontent | text | 0 |  |  | null |  |
| 22 | fchannel | 渠道编码 | varchar | 100 |  | √ | ' ' | 渠道编码 |
| 23 | ftemplate | 适用模板 | varchar | 100 |  | √ | ' ' | 适用模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_himsgfail_msgid |  | fmessageid |
| 2 | idx_wf_himsgfail_deldate |  | fdeletedate |
| 3 | pk_t_wf_himsgfail |  | fid |

---

## 历史消息日志-多语言表 t_wf_himsgfail_l

- **表名称：** 历史消息日志-多语言表
- **表名：** t_wf_himsgfail_l

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
| 1 | idx_wf_himsgfail_l |  | fid,flocaleid |
| 2 | pk_t_wf_himsgfail_l |  | fpkid |
| 3 | idx_wf_himsgfail_l_cname |  | fchannelname |
