# 图片编辑-ide_pictureresediter

## 图片编辑-主表 t_bas_pictureresource

- **表名称：** 图片编辑-主表
- **表名：** t_bas_pictureresource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftag | 标签 | varchar | 100 |  |  | null | 标签 |
| 3 | fformat | 图片格式 | varchar | 10 |  |  | null | 图片格式,枚举: png :png jpg :jpg |
| 4 | fbizcloudid | fbizcloudid | varchar | 36 |  |  | null |  |
| 5 | fisv | isv | varchar | 8 |  | √ | ' ' | isv |
| 6 | fwidth | fwidth | int8 | 64 |  |  | null |  |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | furl0 | 完整路径 | varchar | 255 |  | √ | ' ' | 完整路径 |
| 9 | ftype | 类型 | varchar | 10 |  |  | null | 类型,枚举: icon :图标 image :图片 |
| 10 | furl5 | furl5 | varchar | 255 |  | √ | ' ' |  |
| 11 | fheight | fheight | int8 | 64 |  |  | null |  |
| 12 | fcategoryid | 分类 | int8 | 64 |  |  | null | [图片分类 bos_resourcecategory](../ide_files/bos_resourcecategory.md) |
| 13 | fpath | 分类路径 | varchar | 50 |  |  | null | 分类路径 |
| 14 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 15 | furl1 | furl1 | varchar | 255 |  | √ | ' ' |  |
| 16 | frtlimageshowtype | RTL镜像 | bpchar | 1 |  | √ | ' ' | RTL镜像,枚举: 2 :直接镜像 1 :替换图片 |
| 17 | furl2 | furl2 | varchar | 255 |  | √ | ' ' |  |
| 18 | furl3 | furl3 | varchar | 255 |  | √ | ' ' |  |
| 19 | furl4 | furl4 | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_pictureresource |  | fnumber |
| 2 | t_bas_pictureresource_pkey |  | fid |
| 3 | idx_bas_pictureresource_furl |  | furl0 |

---

## 图片编辑-多语言表 t_bas_pictureresource_l

- **表名称：** 图片编辑-多语言表
- **表名：** t_bas_pictureresource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdl_pictureresource_l |  | fid,flocaleid |
| 2 | t_bas_pictureresource_l_pkey |  | fpkid |
| 3 | t_bas_pictureresource_l_fid_flocaleid_key |  | fid,flocaleid |
