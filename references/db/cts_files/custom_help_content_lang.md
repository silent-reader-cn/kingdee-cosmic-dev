# 自定义帮助内容(多语言)-custom_help_content_lang

## 自定义帮助内容(多语言)-主表 t_bas_custom_help_cont_l

- **表名称：** 自定义帮助内容(多语言)-主表
- **表名：** t_bas_custom_help_cont_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 自定义帮助主键 | int8 | 64 |  | √ | 0 | 自定义帮助主键 |
| 2 | fcontent_tag | 自定义帮助内容_详情 | text | 0 |  |  | null | 自定义帮助内容_详情 |
| 3 | flocaleid | 语言 | varchar | 20 |  | √ | ' ' | 语言 |
| 4 | fcontent | 自定义帮助内容 | varchar | 255 |  | √ | ' ' | 自定义帮助内容 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_custom_help_pkid_l |  | fid,flocaleid |
| 2 | pk_bas_custom_help_cont_l |  | fpkid |
