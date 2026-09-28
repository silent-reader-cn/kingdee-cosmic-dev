# 可归档单据范围-bos_cbs_archi_billset

## 可归档单据范围-主表 t_cbs_archi_billset

- **表名称：** 可归档单据范围-主表
- **表名：** t_cbs_archi_billset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fis_store | 允许被归档转储 | bpchar | 1 |  | √ | ' ' | 允许被归档转储 |
| 3 | fis_clean | 允许被归档清除 | bpchar | 1 |  | √ | ' ' | 允许被归档清除 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 6 | fentitynumber | 表单名称 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fis_sync | 允许被归档同步 | bpchar | 1 |  | √ | '0' | 允许被归档同步 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_billset_no |  | fnumber |
| 2 | idx_cbs_archi_billset_eno |  | fentitynumber |
| 3 | pk_cbs_archi_billset |  | fid |

---

## 可归档单据范围-多语言表 t_cbs_archi_billset_l

- **表名称：** 可归档单据范围-多语言表
- **表名：** t_cbs_archi_billset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_billset_l |  | fpkid |
| 2 | idx_cbs_archi_billset_l |  | fid,flocaleid |
