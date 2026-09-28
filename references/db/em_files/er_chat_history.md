# 历史对话-er_chat_history

## 单据体-子表 t_er_chat_content

- **表名称：** 单据体-子表
- **表名：** t_er_chat_content

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 点赞点踩 | varchar | 50 |  | √ | ' ' | 点赞点踩,枚举: 0 :取消点赞点踩 1 :点赞 2 :点踩 |
| 3 | fparentid | parentid | varchar | 100 |  | √ | ' ' | parentid |
| 4 | fskilltype | 技能类型 | varchar | 50 |  | √ | ' ' | 技能类型,枚举: 123 :123 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdislikecontent | 点踩评论 | varchar | 2000 |  | √ | ' ' | 点踩评论 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmsgtype | 消息类型 | varchar | 50 |  | √ | ' ' | 消息类型,枚举: done :done |
| 9 | fmessageid | id | varchar | 100 |  | √ | ' ' | id |
| 10 | ftype | 分类 | varchar | 50 |  | √ | ' ' | 分类,枚举: user :用户 robot :robot |
| 11 | fskillid | 技能id | int8 | 64 |  | √ | 0 | 技能id |
| 12 | fcontent_tag | 消息_详情 | text | 0 |  |  | null | 消息_详情 |
| 13 | fchatmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcontent | 消息 | varchar | 255 |  | √ | ' ' | 消息 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_chat_content |  | fentryid |
| 2 | idx_er_chat_content |  | fid,fmessageid |

---

## 历史对话-主表 t_er_chat_history

- **表名称：** 历史对话-主表
- **表名：** t_er_chat_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 30 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 9 | fchatuser | 对话用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 会话id | varchar | 100 |  | √ | ' ' | 会话id |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_chat_history |  | fnumber |
| 2 | pk_er_chat_history |  | fid |

---

## 历史对话-多语言表 t_er_chat_history_l

- **表名称：** 历史对话-多语言表
- **表名：** t_er_chat_history_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_chat_history_l |  | fid,flocaleid |
| 2 | pk_er_chat_history_l |  | fpkid |
