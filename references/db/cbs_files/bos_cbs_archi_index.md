# 单据归档索引配置-bos_cbs_archi_index

## 单据归档索引配置-多语言表 t_cbs_archi_index_l

- **表名称：** 单据归档索引配置-多语言表
- **表名：** t_cbs_archi_index_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_index_l |  | fpkid |
| 2 | idx_cbs_archi_index_l |  | fid,flocaleid |

---

## 单据归档索引配置-主表 t_cbs_archi_index

- **表名称：** 单据归档索引配置-主表
- **表名：** t_cbs_archi_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 7 | fbillset | 归档实体 | int8 | 64 |  | √ | 0 | [可归档单据范围 bos_cbs_archi_billset](../cbs_files/bos_cbs_archi_billset.md) |
| 8 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | findicesfields | 归档索引 | varchar | 100 |  | √ | ' ' | 归档索引 |
| 11 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_ai_entitynumber |  | fentitynumber |
| 2 | pk_cbs_archi_index |  | fid |
