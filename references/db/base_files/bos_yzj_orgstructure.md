# 云之家组织结构-bos_yzj_orgstructure

## 云之家组织结构-多语言表 t_yzj_orgstructure_l

- **表名称：** 云之家组织结构-多语言表
- **表名：** t_yzj_orgstructure_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_orgstructure_l_fid |  | fid,flocaleid |
| 2 | t_yzj_orgstructure_l_pkey |  | fpkid |

---

## 云之家组织结构-主表 t_yzj_orgstructure

- **表名称：** 云之家组织结构-主表
- **表名：** t_yzj_orgstructure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyzjorgid | 云之家组织内码 | varchar | 36 |  | √ | ' ' | 云之家组织内码 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | [云之家组织 bos_yzj_org](../base_files/bos_yzj_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [云之家组织 bos_yzj_org](../base_files/bos_yzj_org.md) |
| 9 | fviewid | 组织视图 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 10 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 11 | fsortcode | 字符串排序码 | varchar | 50 |  | √ | ' ' | 字符串排序码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fyzjparentorgid | 上级云之家组织内码 | varchar | 36 |  | √ | ' ' | 上级云之家组织内码 |
| 14 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fisfreeze | 是否封存 | bpchar | 1 |  | √ | ' ' | 是否封存 |
| 18 | fsortnumber | 排序码 | int8 | 64 |  | √ | 0 | 排序码 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fsealuptime | 封存日期 | timestamp | 0 |  |  | null | 封存日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_orgstructure_longnum |  | flongnumber |
| 2 | idx_t_yzj_orgstructure_view |  | fviewid |
| 3 | t_yzj_orgstructure_pkey |  | fid |
| 4 | idx_t_yzj_orgstructure_org |  | forgid |
| 5 | idx_t_yzj_orgstructure_parent |  | fparentid |
