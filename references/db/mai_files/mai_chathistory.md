# 历史对话-mai_chathistory

## 历史对话-主表 t_mai_chathistory

- **表名称：** 历史对话-主表
- **表名：** t_mai_chathistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 会话标题 | varchar | 50 |  | √ | ' ' | 会话标题 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fuser | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsessionid | 会话id | varchar | 50 |  | √ | ' ' | 会话id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mai_chathistory_fsid |  | fsessionid |
| 2 | idx_mai_chathistory_fuser |  | fuser |
| 3 | pk_t_mai_chathistory |  | fid |

---

## 单据体-子表 t_mai_chathistory_d

- **表名称：** 单据体-子表
- **表名：** t_mai_chathistory_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquestionid | 问题id | varchar | 50 |  | √ | ' ' | 问题id |
| 3 | fprocessid | 流程id | varchar | 50 |  | √ | ' ' | 流程id |
| 4 | fquery_tag | 问题_详情 | text | 0 |  |  | null | 问题_详情 |
| 5 | fqueryrewrite_tag | 问题改写_详情 | text | 0 |  |  | null | 问题改写_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fqueryrewrite | 问题改写 | varchar | 255 |  | √ | ' ' | 问题改写 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fcontent_tag | 内容_详情 | text | 0 |  |  | ' ' | 内容_详情 |
| 10 | findicator | 匹配指标 | varchar | 255 |  | √ | ' ' | 匹配指标 |
| 11 | findicator_tag | 匹配指标_详情 | text | 0 |  |  | null | 匹配指标_详情 |
| 12 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fquery | 问题 | varchar | 255 |  | √ | ' ' | 问题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_chathistory_d |  | fentryid |
| 2 | idx_mai_chathistory_d_fid |  | fid |
