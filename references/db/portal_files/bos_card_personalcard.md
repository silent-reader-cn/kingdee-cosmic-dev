# 卡片个性化实体-bos_card_personalcard

## 卡片个性化实体-多语言表 t_meta_personalcard_l

- **表名称：** 卡片个性化实体-多语言表
- **表名：** t_meta_personalcard_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_ps_localeid |  | fid,flocaleid |
| 2 | t_meta_personalcard_l_pkey |  | fpkid |

---

## 卡片个性化实体-主表 t_meta_personalcard

- **表名称：** 卡片个性化实体-主表
- **表名：** t_meta_personalcard

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | flabel | 标签 | varchar | 100 |  | √ | ' ' | 标签 |
| 3 | fisrefresh | 是否刷新 | bpchar | 1 |  | √ | '0' | 是否刷新,枚举: 1 :是 0 :否 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 用户 |
| 6 | fappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 7 | fcardconfig | 卡片配置 | text | 0 |  |  | null | 卡片配置 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fisshowtitlearea | 是否显示标题区 | bpchar | 1 |  | √ | ' ' | 是否显示标题区,枚举: 0 :否 1 :是 |
| 10 | ftype | 卡片类型 | varchar | 36 |  | √ | ' ' | 卡片类型 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcardkey | 卡片标识 | varchar | 36 |  | √ | ' ' | 卡片标识 |
| 13 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fscene | 使用场景 | varchar | 5 |  | √ | '0' | 使用场景,枚举: 0 :不限 1 :首页 2 :应用首页 |
| 15 | fplugin | 插件 | varchar | 500 |  | √ | ' ' | 插件 |
| 16 | fnumber | 卡片编码 | varchar | 50 |  | √ | ' ' | 卡片编码 |
| 17 | fentityid | 卡片实体 | varchar | 100 |  | √ | ' ' | 卡片实体 |
| 18 | fformid | 卡片模板ID | varchar | 36 |  | √ | ' ' | 卡片模板ID |
| 19 | ftitleimg | 标题图标 | varchar | 500 |  |  | null | 标题图标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_personalcard_pkey |  | fid |
| 2 | idx_kdp_personalcard_num |  | fnumber |
