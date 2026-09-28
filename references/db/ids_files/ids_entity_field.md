# 业务对象字段-ids_entity_field

## 业务对象字段-主表 t_ids_entity_field

- **表名称：** 业务对象字段-主表
- **表名：** t_ids_entity_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型 |
| 3 | ffieldcomment | 字段描述 | varchar | 255 |  | √ | ' ' | 字段描述 |
| 4 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 5 | fincrementfield | 增量字段 | bpchar | 1 |  | √ | '0' | 增量字段,枚举: 0 :- 1 :是 |
| 6 | ffieldkey | 字段标识 | varchar | 255 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_fieldkey |  | ffieldkey |
| 2 | pk_t_ids_entity_field |  | fid |
