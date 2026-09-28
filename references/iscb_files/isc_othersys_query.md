# 对接系统查询-isc_othersys_query

## 对接系统查询-主表 t_isc_systementry

- **表名称：** 对接系统查询-主表
- **表名：** t_isc_systementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | 服务器地址 | varchar | 200 |  | √ | ' ' | 服务器地址 |
| 3 | fport | 端口 | int8 | 64 |  | √ | 0 | 端口 |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_sysen_fentid |  | fentryid |
| 2 | t_isc_systementry_pkey |  | fid |
| 3 | idx_isc_sysen_fseq |  | fseq |

---

## 对接系统查询-多语言表 t_isc_systementry_l

- **表名称：** 对接系统查询-多语言表
- **表名：** t_isc_systementry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsysname | 服务名称 | varchar | 255 |  | √ | ' ' | 服务名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_systeme_l_fentid |  | fentryid,flocaleid |
| 2 | t_isc_systementry_l_pkey |  | fpkid |
