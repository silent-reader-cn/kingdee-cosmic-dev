# 算法模型映射基础资料-task_mapping_basefield

## 算法模型映射基础资料-主表 t_tk_mapped_billtype

- **表名称：** 算法模型映射基础资料-主表
- **表名：** t_tk_mapped_billtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fflagid | 标记id | int8 | 64 |  | √ | 0 | 标记id |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_mapped_billtype |  | fid |
| 2 | idx_tk_mapped_billtype |  | fbilltype |

---

## 单据体-子表 t_tk_mapped_relation

- **表名称：** 单据体-子表
- **表名：** t_tk_mapped_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmappedfieldnumber | 指定字段编码 | varchar | 50 |  | √ | ' ' | 指定字段编码 |
| 3 | fbillfieldsource | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 4 | fmappedtype | 映射方式 | varchar | 4 |  | √ | ' ' | 映射方式,枚举: 0 :映射 1 :无需映射 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmappedfield | 指定字段 | varchar | 50 |  | √ | ' ' | 指定字段 |
| 7 | fbillfieldsourcenumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_mapped_relation |  | fbillfieldsourcenumber |
| 2 | pk_t_tk_mapped_relation |  | fentryid |
