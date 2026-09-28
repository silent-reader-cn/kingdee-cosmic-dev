# JSON对象多语言词条表-gai_json_mlang

## JSON对象多语言词条表-多语言表 t_gai_json_mlang_l

- **表名称：** JSON对象多语言词条表-多语言表
- **表名：** t_gai_json_mlang_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftranslatedentry | 翻译词条 | varchar | 2000 |  | √ | ' ' | 翻译词条 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_json_mlang_l |  | fpkid |

---

## JSON对象多语言词条表-主表 t_gai_json_mlang

- **表名称：** JSON对象多语言词条表-主表
- **表名：** t_gai_json_mlang

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftranslatedentry | 翻译词条 | varchar | 2000 |  | √ | ' ' | 翻译词条 |
| 3 | fresourcetype | 资源类型 | varchar | 5 |  | √ | ' ' | 资源类型,枚举: tf :任务流 tl :工具 |
| 4 | fpkid | pkid | int8 | 64 |  | √ | 0 | pkid |
| 5 | fentrypath | 词条标识 | varchar | 500 |  | √ | ' ' | 词条标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_json_mlang |  | fpkid,fentrypath,fresourcetype |
| 2 | pk_gai_json_mlang |  | fid |
