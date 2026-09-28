# 主题定制-bas_uitheme

## 主题定制-主表 t_bas_uitheme

- **表名称：** 主题定制-主表
- **表名：** t_bas_uitheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbackground | 背景图 | varchar | 255 |  | √ | ' ' | 背景图 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fpreview3 | 预览图3 | varchar | 255 |  | √ | ' ' | 预览图3 |
| 6 | fpreview2 | 预览图2 | varchar | 255 |  | √ | ' ' | 预览图2 |
| 7 | fcolor | 颜色 | varchar | 100 |  |  | '1' | 颜色 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fcontent_tag | 主题内容_详情 | varchar | 255 |  | √ | ' ' | 主题内容_详情 |
| 12 | fthumbnail | 缩略图 | varchar | 255 |  | √ | ' ' | 缩略图 |
| 13 | fpreview1 | 预览图1 | varchar | 255 |  | √ | ' ' | 预览图1 |
| 14 | fdefaultvalue | 默认值 | text | 0 |  |  | null | 默认值 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :已禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fcontent | 主题内容 | text | 0 |  |  | null | 主题内容 |
| 18 | fisdefault | 默认 | bpchar | 1 |  | √ | '1' | 默认 |
| 19 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_uitheme_pkey |  | fid |
| 2 | idx_t_bas_uitheme_num |  | fnumber |

---

## 主题定制-多语言表 t_bas_uitheme_l

- **表名称：** 主题定制-多语言表
- **表名：** t_bas_uitheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_uitheme_l_pkey |  | fpkid |
| 2 | idx_t_bas_uitheme_l_fid |  | fid |
