# 黑名单管理-privacy_blackfield_manage

## 单据体-子表 t_privacy_blackfieldinfo

- **表名称：** 单据体-子表
- **表名：** t_privacy_blackfieldinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffield_strategy | 字段控制策略 | varchar | 50 |  | √ | ' ' | 字段控制策略,枚举: nodes :不允许脱敏 noenc :不允许加密 |
| 3 | ffield_iden | 字段标识 | varchar | 36 |  | √ | ' ' | 字段标识 |
| 4 | ffield_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: String :字符串 DynamicObject :基础资料 Date :日期 Integer :整型 BigDecimal :小数 Long :长整型 ILocaleString :多语言 |
| 5 | ffield_name | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_privacy_bfinfo_field |  | ffield_iden |
| 2 | pk_t_privacy_blackfieldinfo |  | fentryid |

---

## 单据体-多语言表 t_privacy_blackfieldinfo_l

- **表名称：** 单据体-多语言表
- **表名：** t_privacy_blackfieldinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffield_name | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_blackfieldinfo_l |  | fpkid |
| 2 | idx_privacy_blackfield_l_fid |  | fentryid,flocaleid |

---

## 黑名单管理-主表 t_privacy_blackfield

- **表名称：** 黑名单管理-主表
- **表名：** t_privacy_blackfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontrol_strategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: nodes :不允许脱敏 noenc :不允许加密 |
| 3 | fsystem_preset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 4 | fentity_number | fentity_number | varchar | 36 |  | √ | ' ' |  |
| 5 | fcreatedate | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fcreater | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fisv | 开发商标识 | varchar | 10 |  | √ | ' ' | 开发商标识 |
| 10 | fentity_id | 实体基础资料 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 11 | fapp_id | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_privacy_bf_entityid |  | fentity_id |
| 2 | pk_t_privacy_blackfield |  | fid |
