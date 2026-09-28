# 元数据描述-bos_metadata_desc

## 元素信息-子表 t_knl_metadata_prop

- **表名称：** 元素信息-子表
- **表名：** t_knl_metadata_prop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fpropcontent | 结构化内容 | varchar | 255 |  | √ | ' ' | 结构化内容 |
| 4 | fprimarykey | 主键 | varchar | 50 |  | √ | ' ' | 主键 |
| 5 | fpropenable | 作为元数据描述项 | bpchar | 1 |  | √ | '0' | 作为元数据描述项 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpropdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | freadonly | 只读 | bpchar | 1 |  | √ | '0' | 只读 |
| 9 | fenablenull | 是否允许为空 | bpchar | 1 |  | √ | '0' | 是否允许为空 |
| 10 | fpropcontent_tag | 结构化内容_详情 | text | 0 |  |  | null | 结构化内容_详情 |
| 11 | fdefaultvalue | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 13 | fproptype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 14 | ftablename | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 15 | fpropkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_knl_metadata_prop |  | fentryid |
| 2 | idx_t_knl_metadata_prop |  | fid |

---

## 元数据描述-多语言表 t_knl_metadata_des_l

- **表名称：** 元数据描述-多语言表
- **表名：** t_knl_metadata_des_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fdomaindesc | 领域知识 | varchar | 255 |  | √ | ' ' | 领域知识 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_knl_metadata_des_l |  | fpkid |
| 2 | idx_t_knl_metadata_des_l |  | fid,flocaleid |

---

## 元数据描述-主表 t_knl_metadata_des

- **表名称：** 元数据描述-主表
- **表名：** t_knl_metadata_des

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | varchar | 36 |  | √ | ' ' | [元数据描述分组 bos_metadata_group](../devgptas_files/bos_metadata_group.md) |
| 5 | fmetadata | 结构化描述 | varchar | 255 |  | √ | ' ' | 结构化描述 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 12 | fcloudid | 所属云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fdomaindesc | 领域知识 | varchar | 255 |  | √ | ' ' | 领域知识 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 17 | fmetadata_tag | 结构化描述_详情 | text | 0 |  |  | null | 结构化描述_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_knl_metadata_des |  | fnumber |
| 2 | pk_t_knl_metadata_des |  | fid |

---

## 元素信息-多语言表 t_knl_metadata_prop_l

- **表名称：** 元素信息-多语言表
- **表名：** t_knl_metadata_prop_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpropname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpropdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_knl_metadata_prop_l |  | fentryid,flocaleid |
| 2 | pk_t_knl_metadata_prop_l |  | fpkid |
