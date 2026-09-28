# 实体配置引用关系-ais_entity_relation

## 实体配置引用关系-主表 t_ais_entity_relation

- **表名称：** 实体配置引用关系-主表
- **表名：** t_ais_entity_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcfgid | 配置表内码 | int8 | 64 |  | √ | 0 | 配置表内码 |
| 3 | frefid | 引用表内码 | int8 | 64 |  | √ | 0 | 引用表内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ais_entity_relation_pkey |  | fid |
| 2 | idx_t_ais_entity_relation |  | fcfgid |
