# 启用操作服务-bos_opbizruleset

## 启用操作服务-主表 t_meta_opbizruleset

- **表名称：** 启用操作服务-主表
- **表名：** t_meta_opbizruleset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopbizrule | 服务 | varchar | 30 |  | √ | ' ' | 服务,枚举: |
| 3 | fenabled | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :禁用 1 :启用 |
| 4 | fobjecttypeid | 启用服务的单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fisallop | 启用实体所有操作 | bpchar | 1 |  | √ | '0' | 启用实体所有操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_opbizruleset_bill |  | fobjecttypeid |
| 2 | idx_meta_opbizruleset_op |  | fopbizrule |
| 3 | t_meta_opbizruleset_pkey |  | fid |

---

## 单据体-子表 t_meta_opbizrulesetentry

- **表名称：** 单据体-子表
- **表名：** t_meta_opbizrulesetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperationkey | 操作 | varchar | 30 |  | √ | ' ' | 操作 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_opbizrulesetentry_pkey |  | fentryid |
| 2 | idx_meta_opbizrulesetentry_id |  | fid |
