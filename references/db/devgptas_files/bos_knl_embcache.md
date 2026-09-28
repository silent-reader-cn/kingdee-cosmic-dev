# 嵌入向量缓存-bos_knl_embcache

## 嵌入向量缓存-主表 t_knl_embcache

- **表名称：** 嵌入向量缓存-主表
- **表名：** t_knl_embcache

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmodeltype | 嵌入模型编码 | varchar | 50 |  | √ | ' ' | 嵌入模型编码 |
| 4 | fvector_tag | vector_详情 | text | 0 |  |  | null | vector_详情 |
| 5 | fvector | vector | varchar | 255 |  | √ | ' ' | vector |
| 6 | fhashvalue | 文本HashValue | varchar | 300 |  | √ | ' ' | 文本HashValue |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_knl_embcache |  | fid |
