# 自定义帮助-custom_help_page_list

## 自定义帮助-多语言表 t_bas_custom_help_l

- **表名称：** 自定义帮助-多语言表
- **表名：** t_bas_custom_help_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 标题 | varchar | 250 |  | √ | ' ' | 标题 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | furllink | URL链接 | varchar | 500 |  | √ | ' ' | URL链接 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_custom_help_l |  | fpkid |
| 2 | pk_custom_help_pkid_l |  | fid,flocaleid |

---

## 自定义帮助-主表 t_bas_custom_help

- **表名称：** 自定义帮助-主表
- **表名：** t_bas_custom_help

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flabel | 标签 | bpchar | 1 |  | √ | ' ' | 标签,枚举: 0 :必读 1 :NEW 2 :HOT |
| 3 | fappnumber | 应用 | varchar | 100 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 4 | frichtextdata_tag | 富文本内容保存_详情 | text | 0 |  |  | null | 富文本内容保存_详情 |
| 5 | ftitle | 标题 | varchar | 250 |  | √ | ' ' | 标题 |
| 6 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :启用 B :- C :禁用 |
| 7 | fweight | 权重 | int8 | 64 |  | √ | 0 | 权重 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 9 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :问答 1 :文章 2 :课程 |
| 10 | fbusobject | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpageview | 浏览量 | int8 | 64 |  | √ | 0 | 浏览量 |
| 13 | fissystem | fissystem | bpchar | 1 |  | √ | '0' |  |
| 14 | furl | URL链接 | varchar | 500 |  | √ | ' ' | URL链接 |
| 15 | flinktype | 链接方式 | bpchar | 1 |  | √ | ' ' | 链接方式,枚举: 0 :富文本 1 :URL链接 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | furllink | URL链接 | varchar | 500 |  | √ | ' ' | URL链接 |
| 18 | frichtextdata | 富文本内容保存 | varchar | 255 |  | √ | ' ' | 富文本内容保存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_custom_help |  | fid |
| 2 | idx_bas_custom_h_num |  | fnumber |
| 3 | idx_custom_h_appnum |  | fappnumber |
| 4 | idx_custom_h_busobject |  | fbusobject |
