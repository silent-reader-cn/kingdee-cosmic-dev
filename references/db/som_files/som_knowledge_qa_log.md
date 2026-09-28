# 知识问询明细记录-som_knowledge_qa_log

## 知识问询明细记录-主表 t_tk_scs_qa_log

- **表名称：** 知识问询明细记录-主表
- **表名：** t_tk_scs_qa_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ffeedback | 用户反馈 | bpchar | 1 |  | √ | '0' | 用户反馈,枚举: 0 :没有 1 :赞 2 :踩 |
| 4 | faskuser | 提问用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | faskusername | 提问用户名 | varchar | 255 |  | √ | ' ' | 提问用户名 |
| 7 | freplay | 系统回复 | varchar | 250 |  | √ | ' ' | 系统回复 |
| 8 | fasktime | 提问时间 | timestamp | 0 |  |  | null | 提问时间 |
| 9 | ftriggerkeyword | 触发关键词 | varchar | 30 |  | √ | ' ' | 触发关键词 |
| 10 | freplay_tag | 系统回复_详情 | text | 0 |  |  | null | 系统回复_详情 |
| 11 | fknowledge | 问题/知识编码 | int8 | 64 |  | √ | 0 | [知识问答 som_knowledge_info](../som_files/som_knowledge_info.md) |
| 12 | finput | 用户输入 | varchar | 50 |  | √ | ' ' | 用户输入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_scsqalog_asktimeqaid |  | fasktime,fknowledge |
| 2 | pk_t_tk_scs_qa_log |  | fid |
