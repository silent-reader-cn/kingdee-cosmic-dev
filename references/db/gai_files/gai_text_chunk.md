# 文本分块信息-gai_text_chunk

## 文本分块信息-主表 t_gai_text_chunk

- **表名称：** 文本分块信息-主表
- **表名：** t_gai_text_chunk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsource | 引用来源 | varchar | 50 |  |  | ' ' | 引用来源,枚举: link :url连接 att :苍穹附件 |
| 3 | ftitle | 块标题 | varchar | 500 |  |  | ' ' | 块标题 |
| 4 | fpageid | 页 | int8 | 64 |  | √ | 0 | 页 |
| 5 | fstatus | 状态 | varchar | 50 |  |  | ' ' | 状态,枚举: A :创建 B :embedding运行中 C :成功 D :失败 |
| 6 | fbusinessid | 业务ID | int8 | 64 |  | √ | 0 | 业务ID |
| 7 | frepoid | 知识库 | int8 | 64 |  | √ | 0 | 知识库 |
| 8 | fcontent_tag | 文本块_详情 | text | 0 |  |  | ' ' | 文本块_详情 |
| 9 | fstrigtotal | 字符数 | int8 | 64 |  | √ | 0 | 字符数 |
| 10 | forder | 分块顺序 | int8 | 64 |  | √ | 0 | 分块顺序 |
| 11 | ffileid | 文件 | int8 | 64 |  | √ | 0 | 文件 |
| 12 | furl | 块引用源 | varchar | 500 |  |  | ' ' | 块引用源 |
| 13 | fcodecontent_tag | 代码示例块_详情 | text | 0 |  |  | ' ' | 代码示例块_详情 |
| 14 | fcontent | 文本块 | varchar | 255 |  |  | ' ' | 文本块 |
| 15 | fcodecontent | 代码示例块 | varchar | 255 |  |  | ' ' | 代码示例块 |
| 16 | ftaskid | 任务ID | varchar | 50 |  |  | null | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_text_chunk |  | frepoid,ffileid |
| 2 | pk_t_gai_text_chunk |  | fid |
