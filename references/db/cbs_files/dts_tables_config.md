# 基础资料关联表配置-dts_tables_config

## 单据体-子表 t_dts_table_config_entry

- **表名称：** 单据体-子表
- **表名：** t_dts_table_config_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 300 |  | √ | ' ' |  |
| 3 | flevel | flevel | int4 | 32 |  | √ | 0 |  |
| 4 | fprimarykey | fprimarykey | varchar | 50 |  | √ | ' ' |  |
| 5 | fparentfield | fparentfield | varchar | 50 |  | √ | ' ' |  |
| 6 | fparenttable | fparenttable | varchar | 50 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | frelationfield | 关联字段 | varchar | 50 |  | √ | ' ' | 关联字段 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | frelationtable | 关联表 | varchar | 50 |  | √ | ' ' | 关联表 |
| 11 | fconfigtype | 配置类型 | varchar | 50 |  | √ | ' ' | 配置类型,枚举: 1 :默认 0 :手动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dts_table_config_entry |  | fentryid |
| 2 | idx_dts_table_config_entry |  | fid |

---

## 基础资料关联表配置-主表 t_dts_table_config

- **表名称：** 基础资料关联表配置-主表
- **表名：** t_dts_table_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcloudid | fcloudid | varchar | 50 |  | √ | ' ' |  |
| 3 | fentitynumber | 实体名称 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fappid | fappid | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dts_table_config |  | fid |
| 2 | idx_dts_table_config |  | fentitynumber |
