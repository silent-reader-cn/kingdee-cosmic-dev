# 短信id记录-wf_smsinfo

## 短信id记录-主表 t_wf_smsinfo

- **表名称：** 短信id记录-主表
- **表名：** t_wf_smsinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftag | 自定义标签 | varchar | 100 |  | √ | ' ' | 自定义标签 |
| 3 | fretrynumber | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 4 | fbizdataid | 业务单据id | varchar | 36 |  | √ | ' ' | 业务单据id |
| 5 | fentitynumber | 实体对象编码 | varchar | 100 |  | √ | ' ' | 实体对象编码 |
| 6 | fuserid | 接收人id | varchar | 100 |  | √ | ' ' | 接收人id |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fstate | 执行状态 | int4 | 32 |  | √ | 0 | 执行状态 |
| 9 | fmessageid | 消息id | int8 | 64 |  | √ | 0 | 消息id |
| 10 | ftype | 消息类型 | varchar | 50 |  | √ | ' ' | 消息类型 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsmsid | 短信id | int8 | 64 |  | √ | 0 | 短信id |
| 13 | fcontent | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_smsinfo_userid |  | fuserid |
| 2 | idx_wf_smsinfo_bizdataid |  | fbizdataid |
| 3 | pk_t_wf_smsinfo |  | fid |
| 4 | idx_wf_smsinfo_createdate |  | fcreatedate |
| 5 | idx_wf_smsinfo_entitynumber |  | fentitynumber |
| 6 | idx_wf_smsinfo_messageid |  | fmessageid |

---

## 短信id记录-多语言表 t_wf_smsinfo_l

- **表名称：** 短信id记录-多语言表
- **表名：** t_wf_smsinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftag | 自定义标签 | varchar | 100 |  | √ | ' ' | 自定义标签 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fcontent | 消息内容 | varchar | 2000 |  | √ | ' ' | 消息内容 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_smsinfo_l |  | fpkid |
| 2 | idx_wf_smsinfo_l |  | fid,flocaleid |
