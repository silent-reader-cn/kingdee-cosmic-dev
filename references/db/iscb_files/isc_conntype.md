# 连接类型（废弃）-isc_conntype

## 连接类型（废弃）-主表 t_isc_conntype

- **表名称：** 连接类型（废弃）-主表
- **表名：** t_isc_conntype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisprefab | 预制数据 | int8 | 64 |  | √ | 0 | 预制数据 |
| 3 | fconntype | fconntype | varchar | 50 |  | √ | ' ' |  |
| 4 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_conntype_fnum |  | fnumber |
| 2 | t_isc_conntype_pkey |  | fid |

---

## 连接类型（废弃）-多语言表 t_isc_conntype_l

- **表名称：** 连接类型（废弃）-多语言表
- **表名：** t_isc_conntype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 100 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_conntype_l_pkey |  | fpkid |
| 2 | idx_isc_conntype_l_fid |  | fid,flocaleid |
