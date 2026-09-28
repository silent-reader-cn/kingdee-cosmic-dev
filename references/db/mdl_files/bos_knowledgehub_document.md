# 知识库文档-bos_knowledgehub_document

## 知识库文档-主表 t_meta_knowledgehubdoc

- **表名称：** 知识库文档-主表
- **表名：** t_meta_knowledgehubdoc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fgoodcount | 点赞数 | int8 | 64 |  | √ | 0 | 点赞数 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcolumnid | 栏目 | varchar | 36 |  | √ | ' ' | 栏目 |
| 5 | ftitle | 标题 | varchar | 100 |  | √ | ' ' | 标题 |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fviewcount | 浏览数 | int8 | 64 |  | √ | 0 | 浏览数 |
| 8 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftitleimage | 主题图片 | varchar | 100 |  | √ | ' ' | 主题图片 |
| 12 | fcontent | 内容 | varchar | 500 |  |  | null | 内容 |
| 13 | fsummary | 摘要 | varchar | 500 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_knowledgehubdoc_pkey |  | fid |
| 2 | idx_kdp_content_num |  | ftitle |
