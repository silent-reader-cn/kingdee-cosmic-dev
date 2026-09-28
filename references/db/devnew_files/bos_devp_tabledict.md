# 数据表字典(废弃)-bos_devp_tabledict

## 单据体-子表 t_meta_tableref

- **表名称：** 单据体-子表
- **表名：** t_meta_tableref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fmainentityid | 主实体 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 3 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 4 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_meta_tableref |  | fentryid |
| 2 | idx_meta_tableref_fid |  | fid |
| 3 | idx_meta_tableref_mainentityid |  | fmainentityid |

---

## 数据表字典(废弃)-主表 t_meta_tabledict

- **表名称：** 数据表字典(废弃)-主表
- **表名：** t_meta_tabledict

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fissystable | fissystable | bpchar | 1 |  | √ | '0' |  |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | ftablename | 表名 | varchar | 64 |  | √ | ' ' | 表名 |
| 7 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_meta_tabledict |  | fid |
| 2 | idx_meta_tabledict_ftablename |  | ftablename |
