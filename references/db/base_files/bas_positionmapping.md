# 职位数据映射-bas_positionmapping

## 职位数据映射-多语言表 t_bas_positionmapping_l

- **表名称：** 职位数据映射-多语言表
- **表名：** t_bas_positionmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fextorgname | 外部组织名称 | varchar | 50 |  | √ | ' ' | 外部组织名称 |
| 3 | fextpositionname | 外部职位名称 | varchar | 50 |  | √ | ' ' | 外部职位名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fextpersonname | 外部职员名称 | varchar | 50 |  | √ | ' ' | 外部职员名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_positionmapping_l_pkey |  | fpkid |
| 2 | idx_bas_positionmapping_l_fid |  | fid,flocaleid |

---

## 职位数据映射-主表 t_bas_positionmapping

- **表名称：** 职位数据映射-主表
- **表名：** t_bas_positionmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextorgnumber | 外部组织编码 | varchar | 50 |  | √ | ' ' | 外部组织编码 |
| 3 | fextorgname | fextorgname | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 内部组织ID | int8 | 64 |  | √ | 0 | 内部组织ID |
| 5 | fexternalsysid | 外部系统 | int8 | 64 |  | √ | 0 | [外部系统 bas_externalsys](../base_files/bas_externalsys.md) |
| 6 | fextpositionnumber | 外部职位编码 | varchar | 50 |  | √ | ' ' | 外部职位编码 |
| 7 | fuserid | 内部人员ID | int8 | 64 |  | √ | 0 | 内部人员ID |
| 8 | fextpersonnumber | 外部职员编码 | varchar | 50 |  | √ | ' ' | 外部职员编码 |
| 9 | fextpersonname | fextpersonname | varchar | 50 |  | √ | ' ' |  |
| 10 | fextorgid | 外部组织ID | varchar | 50 |  | √ | ' ' | 外部组织ID |
| 11 | fextpersonid | 外部职员ID | varchar | 50 |  | √ | ' ' | 外部职员ID |
| 12 | fdatatypeid | 数据类型 | int8 | 64 |  | √ | 0 | [数据类型定义 bas_datatype](../base_files/bas_datatype.md) |
| 13 | fextpositionname | fextpositionname | varchar | 50 |  | √ | ' ' |  |
| 14 | fextpositionid | 外部职位ID | varchar | 50 |  | √ | ' ' | 外部职位ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bas_posimap_userorg |  | fuserid,forgid |
| 2 | t_bas_positionmapping_pkey |  | fid |
