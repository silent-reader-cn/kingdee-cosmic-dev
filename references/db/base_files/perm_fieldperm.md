# 字段权限-perm_fieldperm

## 字段规则列表-子表 t_perm_fieldpermdetail

- **表名称：** 字段规则列表-子表
- **表名：** t_perm_fieldpermdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | ffieldname | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 3 | fpermitemid | 权限项 | varchar | 36 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 6 | fcontrolmode | 列权限条件 | varchar | 10 |  | √ | ' ' | 列权限条件 |
| 7 | fentryid | fentryid | varchar | 18 |  | √ | ' ' | id |
| 8 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ix_perm_fld_ent |  | fentitytypeid,ffieldname |
| 2 | ix_perm_00000008 |  | fid |
| 3 | t_perm_fieldpermdetail_pkey |  | fentryid |

---

## 字段权限-主表 t_perm_fieldperm

- **表名称：** 字段权限-主表
- **表名：** t_perm_fieldperm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_fieldperm |  | fnumber |
| 2 | t_perm_fieldperm_pkey |  | fid |

---

## 字段权限-多语言表 t_perm_fieldperm_l

- **表名称：** 字段权限-多语言表
- **表名：** t_perm_fieldperm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_fieldperm_l_pkey |  | fpkid |
| 2 | idx_perm_fieldperm_l |  | fid,flocaleid |
