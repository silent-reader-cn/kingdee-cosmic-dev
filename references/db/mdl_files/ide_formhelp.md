# 帮助文档实体-ide_formhelp

## 帮助文档实体-主表 t_meta_formhelp

- **表名称：** 帮助文档实体-主表
- **表名：** t_meta_formhelp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fformid | 表单id | varchar | 36 |  | √ | ' ' | 表单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_meta_formhelp_form |  | fformid |
| 2 | t_meta_formhelp_pkey |  | fid |

---

## 帮助文档实体-多语言表 t_meta_formhelp_l

- **表名称：** 帮助文档实体-多语言表
- **表名：** t_meta_formhelp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 3 | fcontent | 帮助内容 | text | 0 |  |  | null | 帮助内容 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_formhelp_l_pkey |  | fpkid |
| 2 | idx_t_meta_formhelp_l_id |  | fid,flocaleid |
