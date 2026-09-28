# AI页页签分录-xkai_page_tab_entry

## AI页页签分录-多语言表 t_xk_ai_page_tab_entry_l

- **表名称：** AI页页签分录-多语言表
- **表名：** t_xk_ai_page_tab_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 128 |  | √ | ' ' | 标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fcontent | 内容 | varchar | 1024 |  | √ | ' ' | 内容 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_page_tab_e_l_fid_flid |  | fid,flocaleid |
| 2 | pk_t_xk_ai_page_tab_entry_l |  | fpkid |

---

## AI页页签分录-主表 t_xk_ai_page_tab_entry

- **表名称：** AI页页签分录-主表
- **表名：** t_xk_ai_page_tab_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 32 |  | √ | ' ' | 标题 |
| 3 | findex | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 4 | fentryicon | 分录图标 | text | 0 |  |  | null | 分录图标 |
| 5 | fentryicon_tag | 分录图标_详情 | text | 0 |  |  | null | 分录图标_详情 |
| 6 | fcontent | 内容 | varchar | 256 |  | √ | ' ' | 内容 |
| 7 | faipagetabid | AI页页签 | int8 | 64 |  | √ | 0 | [AI页页签 xkai_page_tab](../xkportal_files/xkai_page_tab.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_ai_page_tab_entry |  | fid |
| 2 | idx_ai_page_tab_entry_ftabid |  | faipagetabid |
