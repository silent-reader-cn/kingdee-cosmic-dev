# 业务云-bos_devportal_bizcloud

## 单据体-子表 t_meta_bizcloudentry

- **表名称：** 单据体-子表
- **表名：** t_meta_bizcloudentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | frefcloudid | 编码 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_bizcloudentryentry |  | fid,fseq |
| 2 | pk_meta_bizcloudentry |  | fentryid |

---

## 业务云-主表 t_meta_bizcloud

- **表名称：** 业务云-主表
- **表名：** t_meta_bizcloud

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fvisible | 可见性 | bpchar | 1 |  | √ | ' ' | 可见性 |
| 3 | fseq | 序号 | int8 | 64 |  | √ | 254 | 序号 |
| 4 | fmodifier | 修改者 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 6 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 7 | fbaseapp | 基础应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 8 | fismodel | 模板库 | bpchar | 1 |  | √ | '0' | 模板库 |
| 9 | fbackimage | 背景图片 | varchar | 500 |  | √ | ' ' | 背景图片 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fsimplenumber | 简码 | varchar | 20 |  | √ | ' ' | 简码 |
| 12 | ftype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: 1 :原厂 2 :扩展 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreater | 创建者 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 16 | findustry | 行业 | int8 | 64 |  | √ | 0 | [行业信息 bos_devp_industry](../devportal_files/bos_devp_industry.md) |
| 17 | fimage | 主题图片 | varchar | 500 |  | √ | ' ' | 主题图片 |
| 18 | fversion | 版本 | varchar | 100 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizcloud_fnumber_key |  | fnumber |
| 2 | t_meta_bizcloud_pkey |  | fid |

---

## 业务云-多语言表 t_meta_bizcloud_l

- **表名称：** 业务云-多语言表
- **表名：** t_meta_bizcloud_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizcloud_l_pkey |  | fpkid |
| 2 | idx_kdp_bizcloud_localeid |  | fid,flocaleid |
