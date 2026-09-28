# 语言种类对照关系-inte_language_relation

## 语言种类对照关系-主表 t_int_language_relation

- **表名称：** 语言种类对照关系-主表
- **表名：** t_int_language_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstandardlan | 标品语种编码 | varchar | 64 |  | √ | ' ' | 标品语种编码 |
| 3 | fcustomlan | 客户语种编码 | varchar | 64 |  | √ | ' ' | 客户语种编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_int_language_relation |  | fid |
| 2 | idx_t_int_lang_rel |  | fstandardlan |
