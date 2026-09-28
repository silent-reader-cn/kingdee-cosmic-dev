# 知识库栏目-bos_knowledgehub_column

## 知识库栏目-主表 t_meta_knowledgehubcolumn

- **表名称：** 知识库栏目-主表
- **表名：** t_meta_knowledgehubcolumn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 3 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 4 | fcolumnimage | 栏目图片 | varchar | 100 |  | √ | ' ' | 栏目图片 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_knowledgehubcolumn_pkey |  | fid |
| 2 | idx_kdp_column_num |  | fnumber |

---

## 知识库栏目-多语言表 t_meta_knowledgehubcolumn_l

- **表名称：** 知识库栏目-多语言表
- **表名：** t_meta_knowledgehubcolumn_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_column_l_num |  | fname |
| 2 | t_meta_knowledgehubcolumn_l_pkey |  | fpkid |
