# 实例升级记录-plmdc_upgrade_instance

## 实例升级记录-主表 t_plmdc_instance_upgrade

- **表名称：** 实例升级记录-主表
- **表名：** t_plmdc_instance_upgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | finstancemasterid | 实例主数据id | int8 | 64 |  | √ | 0 | 实例主数据id |
| 7 | forigicategoryid | 原分类id | int8 | 64 |  | √ | 0 | 原分类id |
| 8 | fmatchcategoryid | 匹配分类id | int8 | 64 |  | √ | 0 | 匹配分类id |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | finstanceid | 实例id | int8 | 64 |  | √ | 0 | 实例id |
| 11 | fdoctype | 匹配类型 | varchar | 50 |  | √ | ' ' | 匹配类型,枚举: A :MCAD B :ECAD |
| 12 | forigimodelid | 原模型id | int8 | 64 |  | √ | 0 | 原模型id |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fupgrademsg | 升级信息 | varchar | 255 |  | √ | ' ' | 升级信息 |
| 15 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 16 | fmatchmodelid | 匹配模型id | int8 | 64 |  | √ | 0 | 匹配模型id |
| 17 | fupgradestatus | 升级成功 | bpchar | 1 |  | √ | '0' | 升级成功 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_instance_upgrade |  | fid |
| 2 | idx_forigimodelid |  | forigimodelid |

---

## 单据体-子表 t_plmdc_version_instance

- **表名称：** 单据体-子表
- **表名：** t_plmdc_version_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fversionclassifyid | 原分类 | int8 | 64 |  | √ | 0 | 原分类 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fversionid | 版次id | int8 | 64 |  | √ | 0 | 版次id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmatchversionclassifyid | 目标分类 | int8 | 64 |  | √ | 0 | 目标分类 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fversionid |  | fid |
| 2 | pk_t_plmdc_version_instance |  | fentryid |

---

## 实例升级记录-多语言表 t_plmdc_instance_upgrade_l

- **表名称：** 实例升级记录-多语言表
- **表名：** t_plmdc_instance_upgrade_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_instance_upgrade_l_0 |  | fid,flocaleid |
| 2 | pk_t_plmdc_instance_upgrade_l |  | fpkid |
