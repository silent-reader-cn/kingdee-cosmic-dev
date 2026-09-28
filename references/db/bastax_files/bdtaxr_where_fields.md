# 条件字段-bdtaxr_where_fields

## 条件字段-多语言表 t_bastax_where_fields_l

- **表名称：** 条件字段-多语言表
- **表名：** t_bastax_where_fields_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 字段名称 | varchar | 500 |  | √ | ' ' | 字段名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_where_fields_l_0 |  | fid,flocaleid |
| 2 | pk_bastax_where_fields_l |  | fpkid |

---

## 条件字段-主表 t_bastax_where_fields

- **表名称：** 条件字段-主表
- **表名：** t_bastax_where_fields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [条件字段 bdtaxr_where_fields](../bastax_files/bdtaxr_where_fields.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | frefentitykey | 关联实体 | varchar | 50 |  | √ | ' ' | 关联实体 |
| 7 | flongnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 8 | fbillname | 单据名称 | varchar | 200 |  | √ | ' ' | 单据名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbillnumber | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 字段标识 | varchar | 700 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_where_fieldsa |  | fbillnumber |
| 2 | pk_bastax_where_fields |  | fid |
