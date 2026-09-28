# AI页页签-xkai_page_tab

## AI页页签-主表 t_xk_ai_page_tab

- **表名称：** AI页页签-主表
- **表名：** t_xk_ai_page_tab

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbtntype | 按钮类型 | int4 | 32 |  | √ | 0 | 按钮类型,枚举: 0 :立即下载 1 :立即前往 |
| 3 | findex | 排序 | int4 | 32 |  | √ | 0 | 排序 |
| 4 | ftabicon | 页签图标 | text | 0 |  |  | null | 页签图标 |
| 5 | fappid | 关联应用ID | varchar | 64 |  | √ | ' ' | 关联应用ID |
| 6 | ftitle | 标题 | varchar | 64 |  | √ | ' ' | 标题 |
| 7 | ftabtitle | 页签标题 | varchar | 32 |  | √ | ' ' | 页签标题 |
| 8 | fbtntext | 按钮文本 | varchar | 32 |  | √ | ' ' | 按钮文本 |
| 9 | faipageid | 关联主数据 | int8 | 64 |  | √ | 0 | [AI页主数据 xkai_page_master](../xkportal_files/xkai_page_master.md) |
| 10 | furl | 按钮链接 | varchar | 2000 |  | √ | ' ' | 按钮链接 |
| 11 | fcoverimg_tag | 智能大图_详情 | text | 0 |  |  | null | 智能大图_详情 |
| 12 | ftabicon_tag | 页签图标_详情 | text | 0 |  |  | null | 页签图标_详情 |
| 13 | fdesc | 描述 | varchar | 256 |  | √ | ' ' | 描述 |
| 14 | fcoverimg | 智能大图 | text | 0 |  |  | null | 智能大图 |
| 15 | fmenuid | 关联菜单ID | varchar | 64 |  | √ | ' ' | 关联菜单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_ai_page_tab |  | fid |
| 2 | idx_ai_page_tab_fid |  | faipageid |

---

## AI页页签-多语言表 t_xk_ai_page_tab_l

- **表名称：** AI页页签-多语言表
- **表名：** t_xk_ai_page_tab_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 256 |  | √ | ' ' | 标题 |
| 3 | ftabtitle | 页签标题 | varchar | 128 |  | √ | ' ' | 页签标题 |
| 4 | fbtntext | 按钮文本 | varchar | 128 |  | √ | ' ' | 按钮文本 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 6 | fdesc | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xk_ai_page_tab_l |  | fpkid |
| 2 | idx_ai_page_tab_l_fid_flocid |  | fid,flocaleid |
