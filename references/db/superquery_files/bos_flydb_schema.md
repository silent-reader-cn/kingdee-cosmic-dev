# Schema管理-bos_flydb_schema

## Schema管理-主表 t_flydb_schema

- **表名称：** Schema管理-主表
- **表名：** t_flydb_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :启用 B :禁用 |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: cosmic :苍穹 kafka :Kafka es :Elasticsearch |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fdatabaseid | 所属库 | int8 | 64 |  | √ | 0 | 库 bos_flydb_database |
| 8 | ftablestype | 实体范围 | bpchar | 1 |  | √ | ' ' | 实体范围,枚举: 1 :默认 2 :自定义 |
| 9 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_flydb_schema |  | fid |
| 2 | idx_flydb_schema_fnum |  | fnumber |

---

## 自定义实体范围-多选基础资料表 t_flydb_schema_ref

- **表名称：** 自定义实体范围-多选基础资料表
- **表名：** t_flydb_schema_ref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_flydb_schema_ref |  | fpkid |
| 2 | idx_flydb_schema_ref_fk |  | fid |

---

## Schema管理-多语言表 t_flydb_schema_l

- **表名称：** Schema管理-多语言表
- **表名：** t_flydb_schema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_flydb_schema_l |  | fpkid |
| 2 | idx_t_flydb_schema_l_fid |  | fid |
