# AI页主数据-xkai_page_master

## AI页主数据-多语言表 t_xk_ai_page_master_l

- **表名称：** AI页主数据-多语言表
- **表名：** t_xk_ai_page_master_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 512 |  | √ | ' ' | 标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fdesc | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_page_m_l_fid_flocaleid |  | fid,flocaleid |
| 2 | pk_t_xk_ai_page_master_l |  | fpkid |

---

## AI页主数据-主表 t_xk_ai_page_master

- **表名称：** AI页主数据-主表
- **表名：** t_xk_ai_page_master

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 64 |  | √ | ' ' | 标题 |
| 3 | ftype | 类型 | varchar | 32 |  | √ | ' ' | 类型 |
| 4 | fbgimg_tag | 背景图_详情 | text | 0 |  |  | null | 背景图_详情 |
| 5 | fdesc | 描述 | varchar | 256 |  | √ | ' ' | 描述 |
| 6 | fbgimg | 背景图 | text | 0 |  |  | null | 背景图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_page_master_type |  | ftype |
| 2 | pk_t_xk_ai_page_master |  | fid |
