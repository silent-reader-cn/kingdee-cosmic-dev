# ai招聘历史记录-recru_chat_history

## 节点确认内容分录-子表 t_recru_makesurecontent

- **表名称：** 节点确认内容分录-子表
- **表名：** t_recru_makesurecontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmakesurecontent_tag | 确认内容_详情 | text | 0 |  |  | null | 确认内容_详情 |
| 3 | fmakesurecontent | 确认内容 | varchar | 255 |  | √ | ' ' | 确认内容 |
| 4 | fnodeid | 节点 | int8 | 64 |  | √ | 0 | [任务节点编排 recru_agenttask](../recru_files/recru_agenttask.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_makesurecontent_fid |  | fid |
| 2 | pk_recru_makesurecontent |  | fentryid |

---

## ai招聘历史记录-主表 t_recru_chathistory

- **表名称：** ai招聘历史记录-主表
- **表名：** t_recru_chathistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fhistory_tag | 历史对话_详情 | text | 0 |  |  | null | 历史对话_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fclose | 关闭会话 | bpchar | 1 |  | √ | '0' | 关闭会话 |
| 7 | fbosuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fthink | 思考过程 | varchar | 255 |  | √ | ' ' | 思考过程 |
| 9 | fchatsessionid | ai平台最新对话id | varchar | 50 |  | √ | ' ' | ai平台最新对话id |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fthink_tag | 思考过程_详情 | text | 0 |  |  | null | 思考过程_详情 |
| 15 | fsessionid | 会话 | varchar | 50 |  | √ | ' ' | 会话 |
| 16 | fnodeid | 当前节点 | int8 | 64 |  | √ | 0 | [任务节点编排 recru_agenttask](../recru_files/recru_agenttask.md) |
| 17 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fhistory | 历史对话 | varchar | 255 |  | √ | ' ' | 历史对话 |
| 19 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_chathistory_session |  | fsessionid |
| 2 | pk_recru_chathistory |  | fid |

---

## ai招聘历史记录-多语言表 t_recru_chathistory_l

- **表名称：** ai招聘历史记录-多语言表
- **表名：** t_recru_chathistory_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_chathistory_l_fid |  | fid,flocaleid |
| 2 | pk_recru_chathistory_l |  | fpkid |
