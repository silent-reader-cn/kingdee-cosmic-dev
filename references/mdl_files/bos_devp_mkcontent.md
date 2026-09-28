# 文档markdown内容编辑-bos_devp_mkcontent

## 文档markdown内容编辑-主表 t_meta_mkcontent

- **表名称：** 文档markdown内容编辑-主表
- **表名：** t_meta_mkcontent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fctlid | Markdown字段标识 | varchar | 100 |  | √ | ' ' | Markdown字段标识 |
| 3 | fformid | 表单id | varchar | 100 |  | √ | ' ' | 表单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_meta_mkcontent_form |  | fformid |
| 2 | t_meta_mkcontent_pkey |  | fid |

---

## 文档markdown内容编辑-多语言表 t_meta_mkcontent_l

- **表名称：** 文档markdown内容编辑-多语言表
- **表名：** t_meta_mkcontent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 3 | fcontent | Markdown内容 | text | 0 |  |  | null | Markdown内容 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_meta_mkcontent_l |  | fid,flocaleid |
| 2 | t_meta_mkcontent_l_pkey |  | fpkid |
