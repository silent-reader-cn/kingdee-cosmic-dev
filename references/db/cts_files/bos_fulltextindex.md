# 全文索引维护-bos_fulltextindex

## 全文索引维护-主表 t_bas_fulltextindex

- **表名称：** 全文索引维护-主表
- **表名：** t_bas_fulltextindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynctime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 3 | ffieldname | 索引字段 | varchar | 4000 |  | √ | ' ' | 索引字段 |
| 4 | fentitynumber | 实体对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_fulltextindex_pkey |  | fid |
| 2 | idx_bas_fulltextindex |  | fentitynumber |
