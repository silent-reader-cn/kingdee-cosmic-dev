# 知识库标签设置-aikm_labelconfig

## 知识库标签设置-主表 t_aikm_labelconfig

- **表名称：** 知识库标签设置-主表
- **表名：** t_aikm_labelconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fknl | 知识库 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aikm_labelconfig_knl |  | fknl |
| 2 | pk_aikm_labelconfig |  | fid |

---

## 单据体-子表 t_aikm_labelconfigentry

- **表名称：** 单据体-子表
- **表名：** t_aikm_labelconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcanedit | 审核后允许编辑 | bpchar | 1 |  | √ | '0' | 审核后允许编辑 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | flabel | 标签定义 | int8 | 64 |  | √ | 0 | [标签定义 aikm_labeldefine](../aikm_files/aikm_labeldefine.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fdefaultvalue | 默认值 | varchar | 500 |  | √ | ' ' | 默认值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aikm_labelconfigentry |  | fentryid |
