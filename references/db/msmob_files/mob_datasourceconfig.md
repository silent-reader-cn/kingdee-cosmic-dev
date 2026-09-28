# 数据源配置-mob_datasourceconfig

## 字段映射关系-子表 t_mob_fieldmaprelation

- **表名称：** 字段映射关系-子表
- **表名：** t_mob_fieldmaprelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmobentrykey | 分录 | varchar | 80 |  | √ | ' ' | 分录 |
| 3 | fpcfieldkey | 字段标识 | varchar | 150 |  | √ | ' ' | 字段标识 |
| 4 | fpcfieldminlen | 最小长度 | int4 | 32 |  | √ | 0 | 最小长度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmobfieldkey | 字段标识 | varchar | 150 |  | √ | ' ' | 字段标识 |
| 7 | fmobfieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 8 | fpcfieldmaxlen | 最大长度 | int4 | 32 |  | √ | 0 | 最大长度 |
| 9 | fispreset | 出厂预设 | bpchar | 1 |  | √ | '0' | 出厂预设 |
| 10 | fpcfieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 11 | fmobfieldminlen | 最小长度 | int4 | 32 |  | √ | 0 | 最小长度 |
| 12 | fmobfieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 13 | fmobfieldmaxlen | 最大长度 | int4 | 32 |  | √ | 0 | 最大长度 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fpcfieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mob_fieldmaprelat_fid |  | fid |
| 2 | idx_mob_fieldmaprelat_mobfkey |  | fmobfieldkey |
| 3 | pk_mob_fieldmaprelation |  | fentryid |

---

## 数据源配置-多语言表 t_mob_datasourceconfig_l

- **表名称：** 数据源配置-多语言表
- **表名：** t_mob_datasourceconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mob_dsconfig_l_id_locale |  | fid,flocaleid |
| 2 | pk_mob_datasourceconfig_l |  | fpkid |

---

## 搜索控件字段-子表 t_mob_searchkey_e

- **表名称：** 搜索控件字段-子表
- **表名：** t_mob_searchkey_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsearchfieldkey | 字段标识 | varchar | 150 |  | √ | ' ' | 字段标识 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsearchfieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 5 | fispresetsearchkey | 出厂预设 | bpchar | 1 |  | √ | '0' | 出厂预设 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mob_searchkey_e |  | fentryid |
| 2 | idx_mob_searchkey_e_fsfkey |  | fsearchfieldkey |
| 3 | idx_mob_searchkey_e_fid |  | fid |

---

## 数据源配置-主表 t_mob_datasourceconfig

- **表名称：** 数据源配置-主表
- **表名：** t_mob_datasourceconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpcentityobjectid | PC端实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmobformid | 移动表单 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mob_datasourceconfig |  | fid |
| 2 | idx_mob_dsconfig_fmobformid |  | fmobformid |

---

## 分录映射关系-子表 t_mob_entrymapping

- **表名称：** 分录映射关系-子表
- **表名：** t_mob_entrymapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpcentryname | 分录名称 | varchar | 80 |  | √ | ' ' | 分录名称 |
| 3 | fmobentryname | 分录名称 | varchar | 80 |  | √ | ' ' | 分录名称 |
| 4 | fpc_entrykey | 分录标识 | varchar | 80 |  | √ | ' ' | 分录标识 |
| 5 | fispresetentrykey | 出厂预设 | bpchar | 1 |  | √ | '0' | 出厂预设 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmob_entrykey | 分录标识 | varchar | 80 |  | √ | ' ' | 分录标识 |
| 8 | fpc_entryidkey | 分录ID标识 | varchar | 80 |  | √ | ' ' | 分录ID标识 |
| 9 | fmob_entryidkey | 分录ID标识 | varchar | 80 |  | √ | ' ' | 分录ID标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mob_entrymap_fid |  | fid |
| 2 | idx_mob_entrymap_entryidkey |  | fmob_entryidkey |
| 3 | pk_mob_entrymapping |  | fentryid |
