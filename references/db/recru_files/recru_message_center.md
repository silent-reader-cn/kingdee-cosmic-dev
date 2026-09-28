# 消息中心-recru_message_center

## 消息中心-多语言表 t_recru_messagecenter_l

- **表名称：** 消息中心-多语言表
- **表名：** t_recru_messagecenter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 消息名称 | varchar | 50 |  | √ | ' ' | 消息名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_messagecenter_l |  | fpkid |
| 2 | idx_recru_messagecenter_l_fid |  | fid,flocaleid |

---

## 消息中心-主表 t_recru_messagecenter

- **表名称：** 消息中心-主表
- **表名：** t_recru_messagecenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnotificationtype | 通知场景 | varchar | 50 |  | √ | ' ' | 通知场景,枚举: appupdate :APP更新 sysupdate :系统维护 generalbusiness :通用业务 |
| 3 | fname | 消息名称 | varchar | 50 |  | √ | ' ' | 消息名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbosuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | freadstatus | 读取状态 | varchar | 50 |  | √ | ' ' | 读取状态,枚举: unread :未读 read :已读 archived :已归档 deleted :已删除 |
| 8 | ftriggertype | 推送频率 | varchar | 50 |  | √ | ' ' | 推送频率,枚举: once :单次 persistent :持续 until_read :直到已读 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ftitle | 消息标题 | varchar | 50 |  | √ | ' ' | 消息标题 |
| 11 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: interviewresult :面试结果 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 通知类型 | varchar | 20 |  | √ | ' ' | 通知类型,枚举: system :系统通知 user :用户通知 warning :告警通知 info :通用通知 business :业务通知 |
| 16 | fcontent_tag | 消息_详情 | text | 0 |  |  | null | 消息_详情 |
| 17 | fexpiredate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 18 | fsession | 归属会话 | varchar | 50 |  | √ | ' ' | 归属会话 |
| 19 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 消息编码 | varchar | 50 |  | √ | ' ' | 消息编码 |
| 21 | fcontent | 消息 | varchar | 50 |  | √ | ' ' | 消息 |
| 22 | freaddate | 用户读取时间 | timestamp | 0 |  |  | null | 用户读取时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_messagecenter_sessio |  | fsession |
| 2 | pk_recru_messagecenter |  | fid |
