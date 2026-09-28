# BOM编辑器索引-plm_plmsm_bomindex

## 单据体-子表 t_plmsm_bomindexentry

- **表名称：** 单据体-子表
- **表名：** t_plmsm_bomindexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsourcelongnumber | 来源行编码 | varchar | 2000 |  | √ | ' ' | 来源行编码 |
| 4 | frowkey | 行编码 | varchar | 50 |  | √ | ' ' | 行编码 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_bomindexentry_fid |  | fid |
| 2 | pk_t_plmsm_bomindexentry |  | fentryid |

---

## BOM编辑器索引-主表 t_plmsm_bomindex

- **表名称：** BOM编辑器索引-主表
- **表名：** t_plmsm_bomindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM plm_pdm_agg_bomview](../plmsm_files/plm_pdm_agg_bomview.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_bomindex |  | fbomid |
| 2 | pk_plmsm_bomindex |  | fid |
