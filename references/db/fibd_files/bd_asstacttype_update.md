# 核算维度更新记录-bd_asstacttype_update

## 核算维度更新记录-主表 t_bd_accttypeuprecord

- **表名称：** 核算维度更新记录-主表
- **表名：** t_bd_accttypeuprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fmetadata | 业务对象 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdataid | 基础资料数据主键ID | int8 | 64 |  | √ | 0 | 基础资料数据主键ID |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ffieldname | 字段名 | varchar | 80 |  | √ | ' ' | 字段名 |
| 8 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 9 | fentryname | 分录标识 | varchar | 100 |  | √ | ' ' | 分录标识 |
| 10 | fchangetype | 修改类型 | bpchar | 1 |  | √ | ' ' | 修改类型,枚举: 0 :删除 1 :替换 |
| 11 | fbefasstvalue_tag | 版本化前核算维度值_详情 | text | 0 |  |  | null | 版本化前核算维度值_详情 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdataentryid | 基础资料数据分录ID | int8 | 64 |  | √ | 0 | 基础资料数据分录ID |
| 14 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | ' ' | 字段类型,枚举: A :核算维度类型 B :核算维度值 |
| 15 | fbefasstvalue | 版本化前核算维度值 | varchar | 2000 |  | √ | ' ' | 版本化前核算维度值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_act_medaorg |  | fmetadata,fdataid,forgid |
| 2 | pk_t_bd_accttypeuprecord |  | fid |

---

## 版本化前核算维度类型-多选基础资料表 t_bd_befassttype

- **表名称：** 版本化前核算维度类型-多选基础资料表
- **表名：** t_bd_befassttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_befassttype |  | fid |
| 2 | pk_t_bd_befassttype |  | fpkid |
